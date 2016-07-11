"""
Server
Copyright (C) 2014 Walid Benghabrit

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

from http.server import SimpleHTTPRequestHandler
from http.server import HTTPServer
from urllib.parse import urlparse
from socketserver import ThreadingMixIn, ForkingMixIn
import webbrowser
import sys
import os
import threading
from ui.api import *
import signal

base_dir = "examples"
server_port = 8000


def save_current_ps_id(pid):
    print(pid)
    with open(".pid~", "w+") as f:
        f.write(str(pid))


def get_current_ps_id():
    with open(".pid~", "r") as f:
        res = f.readline()
        return int(res)


# Threading server
class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass


# Forking server
class ForkingSimpleServer(ForkingMixIn, HTTPServer):
    pass


# HTTPRequestHandler
class HTTPRequestHandler(SimpleHTTPRequestHandler):

    def get_arg(self, args, name, method):
        try:
            if method == "GET":
                return args[name]
            elif method == "POST":
                return args[name][0]
            else:
                return "Method error"
        except:
            return ""

    def handle_req(self, args, method):
        # print(args)
        res = "Error"
        val = self.get_arg(args, "action", method)

        if val == "list":
            res = api_list_dir(base_dir)
        elif val == "write":
            res = api_write_file(self.get_arg(args, "file", method), self.get_arg(args, "data", method))

        elif val == "read":
            res = api_read_file(self.get_arg(args, "file", method))

        elif val == "delete":
            res = api_delete_file(self.get_arg(args, "file", method))

        elif val == "rename":
            res = api_rename_file(self.get_arg(args, "file", method), self.get_arg(args, "new_name", method))

        elif val == "compileAAL":
            save_current_ps_id(os.getpid())
            res = api_compile_aal(self.get_arg(args, "file", method))

        elif val == "compileFOTL":
            save_current_ps_id(os.getpid())
            res = api_compile_tspass(self.get_arg(args, "file", method))

        elif val == "compileACD":
            save_current_ps_id(os.getpid())
            res = api_compile_acd(self.get_arg(args, "aal", method), self.get_arg(args, "spec", method))

        elif val == "macroCallAPI":
            save_current_ps_id(os.getpid())
            res = api_macro_call(self.get_arg(args, "file", method), self.get_arg(args, "macro", method), self.get_arg(args, "args", method))

        elif val == "listTemplates":
            res = api_list_dir("ui/templates")
            res = res.replace(".json", "")

        elif val == "getTemplate":
            res = api_get_template("ui/templates/" + self.get_arg(args, "file", method))

        elif val == "savePrefs":
            res = api_save_prefs(self.get_arg(args, "prefs", method))

        elif val == "loadPrefs":
            res = api_load_prefs()

        elif val == "getAALdec":
            res = api_get_aal_dec(self.get_arg(args, "file", method))

        elif val == "createDir":
            res = api_create_folder(self.get_arg(args, "file", method))

        elif val == "monitor":
            res = api_monitor()

        elif val == "killPs":
            res = api_kill_ps(self.get_arg(args, "pid", method))

        elif val == "genAccmon":
            res = api_gen_accmon(self.get_arg(args, "file", method), self.get_arg(args, "spec", method))

        elif val == "django":
            res = api_generate_django(self.get_arg(args, "aal_file", method), self.get_arg(args, "spec_file", method),
                                    self.get_arg(args, "output_folder", method))

        elif val == "runDjango":
            save_current_ps_id(os.getpid())
            res = api_run_django(self.get_arg(args, "file", method))

        elif val == "fodtlToDiagram":
            res = api_fodtl_to_vfodtl(self.get_arg(args, "formula", method))

        elif val == "clauseToFodtl":
            res = api_clause_to_fodtl(self.get_arg(args, "file", method), self.get_arg(args, "clause", method))

        elif val == "registerAccMonMonitor":
            res = api_register_accmon_monitor(self.get_arg(args, "formula", method), self.get_arg(args, "name", method),
                                              self.get_arg(args, "accmon_url", method))

        elif val == "svnLog":
            res = svn_log(self.get_arg(args, "target", method))

        elif val == "svnDiff":
            res = svn_diff(self.get_arg(args, "target", method), self.get_arg(args, "r1", method), self.get_arg(args, "r2", method))

        elif val == "svnRevert":
            res = svn_revert(self.get_arg(args, "target", method), self.get_arg(args, "version", method))

        elif val == "cancelCurrentPS":
            res = "No aalc/tspassc process is running"
            ps = get_current_ps_id()
            if ps is not None:
                print("killing ps " + str(ps) + " from " + str(os.getpid()))
                os.kill(ps, signal.SIGKILL)
                Popen(['killall', 'tspass'])
                res = "Operation canceled !"

        elif val == "startSimulation":
            res = start_fodtlmon_server(self.get_arg(args, "port", method))

        elif val == "aal_to_fodtl":
            res = aal_to_fodtl(self.get_arg(args, "file", method), self.get_arg(args, "clause", method))

        elif val == "aal_behaviors":
            res = get_aal_behaviors(self.get_arg(args, "file", method))

        return res

    def do_GET(self):
        # print("[GET] " + self.path)
        # Handle request
        res = "Error"
        p = self.path
        k = urlparse(p).query
        args = parse_qs(k)
        # print(args)
        if "action" in args.keys():
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            res = self.handle_req(args, "GET")
            self.wfile.write(res.encode("utf-8"))
        else:
            super().do_GET()

    def do_POST(self):
        # print("[POST] " + self.path)
        # Handle request
        res = "Error"
        k = urlparse(self.path).query
        varLen = int(self.headers['Content-Length'])
        postVars = self.rfile.read(varLen).decode('utf-8')

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if len(postVars) == 0:
            args = parse_qs(k)
        else:
            args = parse_qs(postVars, encoding="utf8")

        if "action" in args.keys():
            res = self.handle_req(args, "POST")

        self.wfile.write(res.encode("utf-8"))


# Run server
def run(server_class=ForkingSimpleServer, handler_class=HTTPRequestHandler):
    global server_port
    server_address = ('', server_port)
    httpd = server_class(server_address, handler_class)
    print("Server start on port " + str(server_port))
    print("SVN repo initialization...")
    svn_init()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stopping server...")
    httpd.server_close()


# Start ui
def start_ui(port=8000, nobrowser=False):
    global server_port
    server_port = port
    # Open the index page in a web browser
    threading.Thread(target=run).start()
    if not nobrowser:
        webbrowser.open("http://127.0.0.1:" + str(server_port) + "/ui", new=2)
