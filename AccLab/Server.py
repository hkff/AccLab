__author__ = 'hkff'
from http.server import SimpleHTTPRequestHandler
from http.server import HTTPServer
from urllib.parse import urlparse
import webbrowser
import sys
import threading
from api import *

base_dir = "BackendInterface/workspace"

class HTTPRequestHandler(SimpleHTTPRequestHandler):

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

            val = args["action"]
            if val == "list":
                res = api_listDir(base_dir)
            elif val == "write":
                res = api_writeFile(args["file"], args["data"])
            elif val == "read":
                res = api_readFile(args["file"])
            elif val == "delete":
                res = "delete"
            elif val == "compileAAL":
                res = api_compile_aal(args["file"])
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
            val = args["action"][0]
            print(val)
            if val == "list":
                res = api_listDir(base_dir)
            elif val == "write":
                res = api_writeFile(args["file"][0], args["data"][0])
            elif val == "read":
                res = api_readFile(args["file"][0])
            elif val == "delete":
                res = "delete"
            elif val == "compileAAL":
                res = api_compile_aal(args["file"][0])

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


# Open the index page in a web browser
threading.Thread(target=run).start()
webbrowser.open("http://127.0.0.1:8000/", new=2)