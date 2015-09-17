"""
Server API
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

import os
from urllib.parse import *
import sys, shutil
from io import StringIO
from aalc import *

base_dir = "examples"


#  List dir
def api_listDir(wpath):
    tmp = "["
    dirs = os.listdir(wpath)[::-1]
    for d in dirs:
        if d.startswith("."):
            continue
        tmp += '{' + '"id":"cb8", "text":"' + d + '"," iconCls":""'

        if os.path.isdir(wpath + "/" + d):
            tmp += ',"children": '
            tmp += api_listDir(wpath + '/' + d)
        tmp += '},'

    if tmp[-1] == ",":
        tmp = tmp[:-1]
    tmp += ']'

    return tmp


# Read file
def api_readFile(f):
    with open(base_dir + "/" + f) as fd:
        return fd.read()


# Read file
def api_getTemplate(f):
    with open(f) as fd:
        return fd.read()


# Write file
def api_writeFile(f, d):
    # Add \n at the end
    if d[-1] != "\n":
        d += "\n"
    with open(base_dir + "/" + f, "w+") as fd:
        return str(fd.write(d))


# Delete file
def api_deleteFile(f):
    file = base_dir + "/" + f
    if os.path.isfile(file):
        os.remove(file)
    elif os.path.isdir(file):
        shutil.rmtree(file)


# Create Folder
def api_createFolder(d):
    if not os.path.exists(base_dir + "/" + d):
        return str(os.makedirs(base_dir + "/" + d))
    else:
        return "Directory exists !"


# Convert terminal colors to colored div
def toHTMLcolors(html_code: str):
    html_code = html_code.replace("[91m[ERROR]", "<b style='color:red;'><span class='fa fa-times-circle' "
                                                 "style='padding-top: 2px;padding-right: 5px;'/>[ERROR]")
    html_code = html_code.replace("[93m[WARNING]", "<b style='color:orange;'><span class='fa fa-exclamation-triangle'"
                                                   " style='padding-top: 2px;padding-right: 5px;'/>[WARNING]")

    html_code = html_code.replace("[91m", "<b style='color:red;'><span class='' style='padding-top: 2px;'/>")
    html_code = html_code.replace("[93m", "<b style='color:orange;'><span class='' style='padding-top: 2px;'/>")

    html_code = html_code.replace("[92m", "<b style='color:green;'><span class='fa fa-exclamation-triangles' "
                                          "style='padding-top: 2px;'/>")
    html_code = html_code.replace("[95m", "<b style='color:magenta;'><span class='fa fa-exclamation-triangles' "
                                          "style='padding-top: 2px;'/>")

    html_code = html_code.replace("[94m", "<b style='color:blue;'><span class='' style='padding-top: 2px;'/>")
    html_code = html_code.replace("[39m", "</b>")
    html_code = html_code.replace("<<", "&lt;&lt;")
    html_code = html_code.replace(">>", "&gt;&gt;")
    return html_code


# Compile AAL
def api_compile_aal(f):
    # Save current context
    sysout = sys.stdout
    syserr = sys.stderr

    # Capture the output
    reportSIO = StringIO()
    reportEIO = StringIO()
    sys.stdout = reportSIO
    sys.stderr = reportEIO

    res = ""
    try:
        aalc(base_dir + "/" + f, libs_path="libs/aal/", root_path="")
    except:
        res = "Compilation Error"

    res = reportSIO.getvalue() + "\n" + reportEIO.getvalue()

    # Restore context
    sys.stdout = sysout
    sys.stderr = syserr

    print(res)
    res = toHTMLcolors(res)
    return res.replace("\n", "<br>")


# Compile tspass
def api_compile_tspass(f):
    # Save current context
    sysout = sys.stdout
    syserr = sys.stderr

    # Capture the output
    reportSIO = StringIO()
    reportEIO = StringIO()
    sys.stdout = reportSIO
    sys.stderr = reportEIO

    try:
        res = tspassc(file=base_dir + "/" + f, output="tmp.tspass", timeout=timeout)["print"]
    except:
        res = "Compilation Error"

    res += "\n" + reportSIO.getvalue() + "\n" + reportEIO.getvalue()

    print(res)
    # Restore context
    sys.stdout = sysout
    sys.stderr = syserr

    return res.replace("\n", "<br>")


# Get AAL declaration in JSON format
def api_getAALDec(f):
    try:
        mm = aalc(base_dir + "/" + f, libs_path="libs/aal/", root_path="", no_exec=True)["mm"]
    except:
        # Compilation Error
        return '{"agents" : [], "services" : [], "types" : [], "data" : [], "clauses" : [], "dataTypes" : [], "actorTypes" : []}'

    agents = ",".join(mm.get_declared(dtype="agents"))
    services = ",".join(mm.get_declared(dtype="services"))
    data = ",".join(mm.get_declared(dtype="data"))

    tts = mm.aalprog.get_declared(m_type)
    print([str(x.name) for x in tts])
    types = ",".join(mm.get_declared(dtype="types"))
    # Filter by data type / actor type

    actorTypes = ",".join(['"' + str(x.name) + '"' for x in list(filter(lambda x: x.subtype_of("actor"), tts))])
    dataTypes = ",".join(['"' + str(x.name) + '"' for x in list(filter(lambda x: x.subtype_of("data"), tts))])
    print(actorTypes)
    print(dataTypes)
    clauses = ",".join(['"' + str(x.name) + '"' for x in mm.aalprog.clauses])
    res = '{"agents" : [' + agents + '], "services" : [' + services + '], "types" : [' + \
          types + '], "data" : [' + data + '], "clauses" : [' + clauses + ']' + ', "dataTypes" : [' +\
          dataTypes + ']' + ', "actorTypes" : [' + actorTypes + ']' + '}'
    print(res)
    return res
