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
import webbrowser
import sys
import threading
from ui.api import *

base_dir = "examples"


# HTTPRequestHandler
class HTTPRequestHandler(SimpleHTTPRequestHandler):

    def get_arg(self, args, name, method):
        if method == "GET":
            return args[name]
        elif method == "POST":
            return args[name][0]
        else:
            return "Method error"

    def handle_req(self, args, method):
        res = "Error"
        val = self.get_arg(args, "action", method)
        if val == "list":
            res = api_listDir(base_dir)
        elif val == "write":
            res = api_writeFile(self.get_arg(args, "file", method), self.get_arg(args, "data", method))
        elif val == "read":
            res = api_readFile(self.get_arg(args, "file", method))
        elif val == "delete":
            res = api_deleteFile(self.get_arg(args, "file", method))
        elif val == "compileAAL":
            res = api_compile_aal(self.get_arg(args, "file", method))
        elif val == "compileFOTL":
            res = api_compile_tspass(self.get_arg(args, "file", method))
        return res

    def do_GET(self):
        print("[GET] " + self.path)
        # Handle request
        res = "Error"
        p = self.path
        k = urlparse(p).query
        args = parse_qs(k)
        print(args)
        if "action" in args.keys():
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            res = self.handle_req(args, "GET")
            self.wfile.write(res.encode("utf-8"))
        else:
            super().do_GET()

    def do_POST(self):
        print("[POST] " + self.path)
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
def run(server_class=HTTPServer, handler_class=HTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stoping server...")
    httpd.server_close()


# Start ui
def start_ui():
    # Open the index page in a web browser
    threading.Thread(target=run).start()
    webbrowser.open("http://127.0.0.1:8000/ui", new=2)
