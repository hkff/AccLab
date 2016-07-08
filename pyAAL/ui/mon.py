"""
Server
Copyright (C) 2016 Walid Benghabrit

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = 'walid'
# from fodtlmon.webservice.webservice import Webservice
import sys
from http.server import SimpleHTTPRequestHandler
from http.server import HTTPServer
from urllib.parse import urlparse, parse_qs
from socketserver import ThreadingMixIn, ForkingMixIn
import threading
from fodtlmon.fodtl.fodtlmon import *


# Threading server
class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass


# Forking server
class ForkingSimpleServer(ForkingMixIn, HTTPServer):
    pass


class Actor:
    def __init__(self, name="", formula=None, trace=None):
        self.name = name
        self.formula = formula
        self.trace = trace
        self.monitor = None
        self.sub_mons = []


class System:
    """
    Distributed system representation
    """
    def __init__(self, name, actors=None, kv_implementation=KVector):
        """
        Init the system
        :param actors: actors list
        :param kv_implementation: the Knowledge vector implementation (IKVector)
        :return:
        """
        self.name = name
        self.actors = [] if actors is None else actors
        self.mons = []
        self.kv_implementation = kv_implementation
        self.forward = []

    def add_actors(self, actor):
        """
        Add an actor / actor list to the system's actors
        :param actor: Actor | list<Actor>
        :return: self
        """
        if isinstance(actor, list):
            self.actors.extend(actor)
        elif isinstance(actor, Actor):
            self.actors.append(actor)
        return self

    def get_actor(self, name):
        """
        Get an actor by name
        :param name: str
        :return:
        """
        return next((x for x in self.actors if x.name == name), None)

    def register_actor(self, actor):
        """

        :param actor:
        :return:
        """
        self.add_actors(actor)

        remotes = actor.formula.walk(filter_type=At)
        # Compute formula hash
        for f in remotes:
            f.compute_hash(sid=actor.name)

        # Create the global monitor for the actor
        actor.monitor = Fodtlmon(actor.formula, actor.trace)

        submons = []
        # Create the remote sub monitors for each @Formula
        for f in remotes:
            remote_actor = self.get_actor(f.agent)
            if remote_actor is not None:
                remote_actor.sub_mons.append(Fodtlmon(f.inner, remote_actor.trace, parent=remote_actor.monitor, fid=f.fid))
                submons.append({"fid": f.fid, "actor": remote_actor.name})
            else:
                self.forward.append(remote_actor)

        # Create the general KV structure
        kv = self.kv_implementation()
        for m in submons:
            kv.add_entry(self.kv_implementation.Entry(m["fid"], agent=m["actor"], value=Boolean3.Unknown, timestamp=0))

        # Add a copy of KV structure for each actor
        # for a in self.actors:
        #     a.monitor.KV = copy.deepcopy(kv)
        # TODO handle forward


class Webservice:
    """
    Web service class
    """
    monitors = {}
    systems = {}
    server_port = 8000
    passkey = ""

    def __init__(self):
        pass

    @staticmethod
    def run(server_class=ThreadingSimpleServer):
        server_address = ('', Webservice.server_port)
        httpd = server_class(server_address, Webservice.HTTPRequestHandler)
        print("Server start on port " + str(Webservice.server_port))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Stopping server...")
        httpd.server_close()

    @staticmethod
    def start(port=8000, passkey=None):
        Webservice.server_port = port
        if passkey is not None:
            Webservice.passkey = passkey
        threading.Thread(target=Webservice.run).start()

    # HTTPRequestHandler
    class HTTPRequestHandler(SimpleHTTPRequestHandler):

        @staticmethod
        def get_arg(args, name, method):
            try:
                if method == "GET":
                    return args[name]
                elif method == "POST":
                    return args[name][0]
                else:
                    return "Method error"
            except:
                return None

        def do_GET(self):
            # print("[GET] " + self.path)
            p = self.path
            k = urlparse(p).query
            args = parse_qs(k)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            path = p.replace(k, "")
            if path[-1] == "?":
                path = path[:-1]
            res = self.handle_req(path, args, "GET")
            self.wfile.write(res.encode("utf-8"))

        def do_POST(self):
            k = urlparse(self.path).query
            var_len = int(self.headers['Content-Length'])
            post_vars = self.rfile.read(var_len).decode('utf-8')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            if len(post_vars) == 0:
                args = parse_qs(k)
            else:
                args = parse_qs(post_vars, encoding="utf8")

            res = self.handle_req(self.path, args, "POST")
            self.wfile.write(res.encode("utf-8"))

        def handle_req(self, path, args, method):
            # print(args)
            print(path)
            res = "Error"
            method_name = path.replace("/", "_")[1:]
            if hasattr(Webservice.API, method_name):
                res = getattr(Webservice.API, method_name)(args, method)
            return res

    class API:
        """
        Webservice API
        """
        @staticmethod
        def require_args(names, args, method):
            res = {}
            for arg in names:
                tmp = Webservice.HTTPRequestHandler.get_arg(args, arg, method)
                if tmp is None:
                    return "Missing %s" % arg
                else:
                    if method == "GET":
                        res[arg] = tmp[0]
                    else:
                        res[arg] = tmp
            return res

        @staticmethod
        def api_monitor_all(args, method):
            """
                URL : /api/monitor/all
            """
            return str([str(x) for x in Webservice.monitors.keys()])

        @staticmethod
        def api_monitor_register(args, method):
            """
                URL : /api/monitor/register
            """
            args_names = ["mon_name", "formula", "trace"]
            _args = Webservice.API.require_args(args_names, args, method)
            if isinstance(_args, str): return _args
            tr = Trace().parse(_args.get("trace"))
            fl = FodtlParser.parse(_args.get("formula"))
            Webservice.monitors[_args.get("mon_name")] = Fotlmon(fl, tr)
            return "Registered"

        @staticmethod
        def api_actor_register(args, method):
            """
                URL : /api/actor/register
            """
            args_names = ["actor", "formula", "trace", "sys"]
            _args = Webservice.API.require_args(args_names, args, method)
            if isinstance(_args, str): return _args
            tr = Trace().parse(_args.get("trace"))
            fl = FodtlParser.parse(_args.get("formula"))
            name = _args.get("actor")
            sys = _args.get("sys")

            system = Webservice.systems.get(sys, None)
            if system is not None:
                a = Actor(name=name, formula=fl, trace=tr)
                system.register_actor(a)
            else:
                return "System not found !"
            return "Registered"

        @staticmethod
        def api_monitor_events_push(args, method):
            """
                URL : /api/monitor/events/push
            """
            args_names = ["mon_name", "event"]
            _args = Webservice.API.require_args(args_names, args, method)
            if isinstance(_args, str): return _args
            mon = Webservice.monitors.get(_args.get("mon_name"))
            res = "Monitor not found !"
            if mon is not None:
                e = Event.parse(_args.get("event"))
                if e is not None:
                    mon.push_event(e)
                    res = "Pushed"
                else:
                    return "Bad event format !"
            return res

        @staticmethod
        def api_monitor_run(args, method):
            """
                URL : /api/monitor/run
            """
            args_names = ["mon_name"]
            _args = Webservice.API.require_args(args_names, args, method)
            if isinstance(_args, str): return _args
            mon = Webservice.monitors.get(_args.get("mon_name"))
            res = "Monitor not found !"
            if mon is not None:
                res = mon.monitor(struct_res=True)
                res["result"] = str(res.get("result"))
            return str(res)

        @staticmethod
        def api_monitor_remove(args, method):
            """
                URL : /api/monitor/remove
            """
            args_names = ["mon_name"]
            _args = Webservice.API.require_args(args_names, args, method)
            if isinstance(_args, str): return _args
            mon = Webservice.monitors.get(_args.get("mon_name"))
            res = "Monitor not found !"
            if mon is not None:
                del Webservice.monitors[_args.get("mon_name")]
                res = "Deleted"
            return res

        @staticmethod
        def api_system_create(args, method):
            """
                URL : /api/system/create
            """
            args_names = ["sys_name"]
            _args = Webservice.API.require_args(args_names, args, method)
            if isinstance(_args, str): return _args

            sys_name = _args.get("sys_name")
            Webservice.systems[sys_name] = System(sys_name)
            res = "System created !"
            return res

        @staticmethod
        def api_system_actors(args, method):
            """
                URL : /api/system/actors
            """
            args_names = ["sys_name"]
            _args = Webservice.API.require_args(args_names, args, method)
            if isinstance(_args, str): return _args

            sys_name = _args.get("sys_name")
            sys = Webservice.systems.get(sys_name, None)
            if sys is not None:
                res = " , ".join([x.name for x in sys.actors])
            else:
                res = "System not found !"
            return res

        @staticmethod
        def api_systems_all(args, method):
            """
                URL : /api/systems/all
            """
            res = "," .join([Webservice.systems[x].name for x in Webservice.systems.keys()])
            return res

        @staticmethod
        def api_shutdown(args, method):
            """
                URL : /api/shutdown
            """
            args_names = ["passkey"]
            _args = Webservice.API.require_args(args_names, args, method)
            if isinstance(_args, str): return _args
            passkey = _args.get("passkey")
            if Webservice.passkey == str(passkey):
                os._exit(0)
            return "Wrong passkey !"


if __name__ == "__main__":
    try:
        server_port = 9999 if len(sys.argv) == 1 else int(sys.argv[1])
    except:
        server_port = 9999
    passkey = "1234" if len(sys.argv) < 3 else sys.argv[2]
    Webservice.start(server_port, passkey=passkey)
