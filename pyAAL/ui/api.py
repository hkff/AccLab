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
import sys
from io import StringIO
from aalc import *

base_dir = "examples"


# List dir
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

    tmp = tmp[:-1]
    tmp += ']'
    return tmp


# Read file
def api_readFile(f):
    with open(base_dir + "/" + f) as fd:
        return fd.read()


# Write file
def api_writeFile(f, d):
    with open(base_dir + "/" + f, "w+") as fd:
        return str(fd.write(d))


# Delete file
def api_deleteFile(f):
    file = base_dir + "/" + f
    if os.path.isfile(file):
        os.remove(file)


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
        aalc(base_dir + "/" + f, libs_path="libs/aal/", root_path="examples")
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
        res = tspassc(file=base_dir + "/" + f, output="tmp.tspass")["print"]
    except:
        res = "Compilation Error"

    res += "\n" + reportSIO.getvalue() + "\n" + reportEIO.getvalue()

    print(res)
    # Restore context
    sys.stdout = sysout
    sys.stderr = syserr

    return res.replace("\n", "<br>")