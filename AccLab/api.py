__author__ = 'hkff'

import os
from urllib.parse import *
import sys
from io import StringIO
#from aalc import *
base_dir = "BackendInterface/workspace"


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
        print(d)
        return str(fd.write(d))


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
    # try:
    #     aalc(base_dir + "/" + f, libs_path="../pyAAL/libs/aal/", root_path="workspace")
    # except:
    #     res = "Compilation Error"

    res = reportSIO.getvalue() + "\n" + reportEIO.getvalue()

    # Restore context
    sys.stdout = sysout
    sys.stderr = syserr

    print(res)
    res = toHTMLcolors(res)
    return res.replace("\n", "<br>")
