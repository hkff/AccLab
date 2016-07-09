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

    def push_event(self, event):
        self.trace.push_event(event)

    def run_monitor(self):
        # run sub mons and update KV
        for mon in self.sub_mons:
            mon.monitor()
            self.monitor.KV.update(KVector.Entry(mon.fid, agent=self.name, value=mon.last, timestamp=mon.counter))

        # Run main monitor
        res = self.monitor.monitor()
        return res

    def to_html(self):
        return """
        Name: %s </br>
        Formula: %s </br>
        Trace: %s </br>
        Result: %s </br>
        KV: %s </br>
        """ % (self.name, self.formula, self.trace, self.monitor.last, self.monitor.KV)


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

    def to_html(self):
        return """
        <h4># %s</h4>
        <h5>## Actors:</h5>
        %s
        """ % (self.name, "</br>".join([x.to_html() for x in self.actors]))

    def add_actors(self, actor):
        """
        Add an actor
        :param actor: Actor
        :return: self
        """
        if isinstance(actor, Actor):
            exs = list(filter(lambda x: x.name == actor.name, self.actors))
            if len(exs) == 0:
                self.actors.append(actor)
            else:
                self.actors.remove(exs[0])
                self.actors.append(actor)
        return self

    def get_actor(self, name):
        """
        Get an actor by name
        :param name: str
        :return:
        """
        return next((x for x in self.actors if x.name == name), None)

    def register_remotes(self, actor):
        """

        :param actor:
        :return:
        """
        for e in self.forward:
            if e["formula"].agent == actor.name:
                ac = self.get_actor(e["actor"])
                if ac is not None:
                    f = e["formula"]
                    actor.sub_mons.append(Fodtlmon(f.inner, actor.trace, parent=actor.monitor, fid=f.fid))
                    # Add entry into KVs
                    ac.monitor.KV.add_entry(self.kv_implementation.Entry(f.fid, agent=actor.name, value=Boolean3.Unknown, timestamp=0))
                    actor.monitor.KV.add_entry(self.kv_implementation.Entry(f.fid, agent=actor.name, value=Boolean3.Unknown, timestamp=0))

    def register_actor(self, actor):
        """

        :param actor:
        :return:
        """
        remotes = actor.formula.walk(filter_type=At)
        # Compute formula hash
        for f in remotes:
            f.compute_hash(sid=actor.name)

        # Create the global monitor for the actor
        actor.monitor = Fodtlmon(actor.formula, actor.trace)

        # Create the remote sub monitors for each @Formula
        for f in remotes:
            remote_actor = self.get_actor(f.agent)
            if remote_actor is not None:
                remote_actor.sub_mons.append(Fodtlmon(f.inner, remote_actor.trace, parent=remote_actor.monitor, fid=f.fid))
                # Add entry into KVs
                actor.monitor.KV.add_entry(self.kv_implementation.Entry(f.fid, agent=remote_actor.name, value=Boolean3.Unknown, timestamp=0))
                remote_actor.monitor.KV.add_entry(self.kv_implementation.Entry(f.fid, agent=remote_actor.name, value=Boolean3.Unknown, timestamp=0))
            else:
                self.forward.append({"formula": f, "actor": actor.name})

        # Handle forward
        self.register_remotes(actor)

        self.add_actors(actor)


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
            args_names = ["actor", "formula", "sys"]
            _args = Webservice.API.require_args(args_names, args, method)
            if isinstance(_args, str): return _args
            fl = FodtlParser.parse(_args.get("formula"))
            name = _args.get("actor")
            sys = _args.get("sys")

            system = Webservice.systems.get(sys, None)
            if system is not None:
                a = Actor(name=name, formula=fl, trace=Trace())
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
        def api_actor_events_push(args, method):
            """
                URL : /api/actor/events/push
            """
            args_names = ["actor", "event", "sys"]
            _args = Webservice.API.require_args(args_names, args, method)
            if isinstance(_args, str): return _args

            actor_name = _args.get("actor")
            sys = Webservice.systems.get(_args.get("sys"), None)

            res = "System not found !"
            if sys is not None:
                actor = sys.get_actor(actor_name)
                res = "Actor not found !"
                if actor is not None:
                    e = Event.parse(_args.get("event"))
                    if e is not None:
                        actor.push_event(e)
                        res = "Pushed"
                    else:
                        return "Bad event format !"
            return res

        @staticmethod
        def api_actor_monitor_run(args, method):
            """
                URL : /api/actor/monitor/run
            """
            args_names = ["actor", "sys"]
            _args = Webservice.API.require_args(args_names, args, method)
            if isinstance(_args, str): return _args

            actor_name = _args.get("actor")
            sys = Webservice.systems.get(_args.get("sys"), None)

            res = "System not found !"
            if sys is not None:
                actor = sys.get_actor(actor_name)
                res = "Actor not found !"
                if actor is not None:
                    res = actor.run_monitor()
            return res

        @staticmethod
        def api_actor_kv(args, method):
            """
                URL : /api/actor/kv/
            """
            args_names = ["actor", "sys"]
            _args = Webservice.API.require_args(args_names, args, method)
            if isinstance(_args, str): return _args

            actor_name = _args.get("actor")
            sys = Webservice.systems.get(_args.get("sys"), None)

            res = "System not found !"
            if sys is not None:
                actor = sys.get_actor(actor_name)
                res = "Actor not found !"
                if actor is not None:
                    res = str(actor.monitor.KV)
            return res

        @staticmethod
        def api_actor_updatekv(args, method):
            """
                URL : /api/actor/updatekv/
            """
            args_names = ["actor", "sys", "from"]
            _args = Webservice.API.require_args(args_names, args, method)
            if isinstance(_args, str): return _args

            actor_name = _args.get("actor")
            source_name = _args.get("from")
            sys = Webservice.systems.get(_args.get("sys"), None)

            res = "System not found !"
            if sys is not None:
                actor = sys.get_actor(actor_name)
                source_actor = sys.get_actor(source_name)
                res = "Actor not found !"
                if actor is not None:
                    actor.monitor.update_kv(source_actor.monitor.KV)
                    res = "Updates !"
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

        @staticmethod
        def api(args, method):
            """
                URL : /api/
            """
            args_names = ["passkey"]
            _args = Webservice.API.require_args(args_names, args, method)
            if isinstance(_args, str): return _args
            passkey = _args.get("passkey")
            if Webservice.passkey == str(passkey):
                res = """
                <!DOCTYPE html> <html> <head> <meta charset="utf-8"> </head> <body>
                <h2>Systems:</h2>
                %s
                </body></html>
                """ % (" ".join([Webservice.systems[x].to_html() for x in Webservice.systems.keys()]))

                return res
            return "Wrong passkey !"


if __name__ == "__main__":
    try:
        server_port = 9999 if len(sys.argv) == 1 else int(sys.argv[1])
    except:
        server_port = 9999
    passkey = "1234" if len(sys.argv) < 3 else sys.argv[2]
    Webservice.start(server_port, passkey=passkey)
