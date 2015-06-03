"""
Visu visualisation of AAL ast in web page
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

import webbrowser
from http.server import SimpleHTTPRequestHandler
from http.server import HTTPServer
import threading
from AALMetaModel import *


# Run server in thread
def run_server():
    """
    Run a localhost server on port 9025
    :return:
    """
    server_address = ('', 9025)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stoping server...")
    httpd.server_close()


# Show ast
def show_ast(aalprog: m_aalprog):
    """
    Show the abstract syntax tree of an aal program in a interactive web page
    :param aalprog: the aal program
    :return:
    """
    ast = aalprog.to_ast()
    ast = ast[:-1]
    with open("tools/visu/ast.json", mode='w') as f:
        f.write(ast)

    ignored = [aalmmnode, aalmm, m_declarable, m_aalprog, m_aexp]
    # ast_stat = "{ 'header: { title: { text: 'A very simple example pie'}}, data: {content: ["
    ast_stat = "["
    classes = get_mm_classes()
    for x in classes:
        if not(x in ignored):
            nbr = len(aalprog.walk(filter_type=x))
            ast_stat += '{"label": "' + str(x.__name__) + '", "value": ' + str(nbr) + '},'

    ast_stat = ast_stat[:-1]
    ast_stat += "]"
    with open("tools/visu/ast_stat.json", mode='w') as f:
        f.write(ast_stat)

    try:
        threading.Thread(target=run_server).start()
        webbrowser.open("http://127.0.0.1:9025/tools/visu/tree.html", new=2)
    except KeyboardInterrupt:
        print("Stoping server...")