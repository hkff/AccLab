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
from AALtoDJfodtlmon import *

base_dir = "examples"

ALLOWED_CMD = ["tspass", "aalc.py", "fotl-translate"]


# Filter ps
def is_cmd_allowed(cmds):
    for x in ALLOWED_CMD:
        if x in cmds:
            return True
    return False


#  List dir
def api_list_dir(wpath):
    tmp = "["
    dirs = os.listdir(wpath)[::-1]
    for d in dirs:
        if d.startswith("."):
            continue
        tmp += '{' + '"id":"cb8", "text":"' + d + '"," iconCls":""'

        if os.path.isdir(wpath + "/" + d):
            tmp += ',"children": '
            tmp += api_list_dir(wpath + '/' + d)
        tmp += '},'

    if tmp[-1] == ",":
        tmp = tmp[:-1]
    tmp += ']'

    return tmp


# Read file
def api_read_file(f):
    with open(base_dir + "/" + f) as fd:
        return fd.read()


# Get template
def api_get_template(f):
    with open(f) as fd:
        return fd.read()


# Write file
def api_write_file(f, d):
    # Add \n at the end
    if d[-1] != "\n":
        d += "\n"
    with open(base_dir + "/" + f, "w+") as fd:
        return str(fd.write(d))


# Rename file
def api_rename_file(f, new_name):
    os.rename(base_dir + "/" + f, base_dir + "/" + new_name)
    return "RENAMED"


# Delete file
def api_delete_file(f):
    file = base_dir + "/" + f
    if os.path.isfile(file):
        os.remove(file)
    elif os.path.isdir(file):
        shutil.rmtree(file)
    return "DELETED"


# Save preferences
def api_save_prefs(d):
    # Add \n at the end
    if d[-1] != "\n":
        d += "\n"
    with open("ui/prefs.json", "w+") as fd:
        return str(fd.write(d))


# Load preferences
def api_load_prefs():
    if not os.path.isfile("ui/prefs.json"):
        api_save_prefs('{"theme": "monokai", "username": "", "fontSize": 14 }')
    with open("ui/prefs.json") as fd:
        return fd.read()


# Create Folder
def api_create_folder(d):
    if not os.path.exists(base_dir + "/" + d):
        return str(os.makedirs(base_dir + "/" + d))
    else:
        return "Directory exists !"


# Convert terminal colors to colored div
def to_html_colors(html_code: str):
    html_code = html_code.replace("[91m[ERROR]", "<b style='color:red;'><span class='fa fa-times-circle' "
                                                 "style='padding-top: 2px;padding-right: 5px;'/>[ERROR]")
    html_code = html_code.replace("[93m[WARNING]", "<b style='color:orange;'><span class='fa fa-exclamation-triangle'"
                                                   " style='padding-top: 2px;padding-right: 5px;'/>[WARNING]")

    html_code = html_code.replace("[95mat line", "<b style='color:magenta; text-decoration: underline;  "
                                                 "cursor: pointer;' class='aceLine'>at line")

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
        aalc(base_dir + "/" + f, libs_path="libs/aal/", root_path="", web=True)
    except Exception as e:
        res = "Compilation Error : " + str(e)

    res = reportSIO.getvalue() + "\n" + reportEIO.getvalue()

    # Restore context
    sys.stdout = sysout
    sys.stderr = syserr

    print(res)
    res = to_html_colors(res)
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
    except Exception as e:
        res = "Compilation Error : " + str(e)

    res += "\n" + reportSIO.getvalue() + "\n" + reportEIO.getvalue()

    print(res)
    # Restore context
    sys.stdout = sysout
    sys.stderr = syserr

    return res.replace("\n", "<br>")


# Get AAL declaration in JSON format
def api_get_aal_dec(f):
    try:
        mm = aalc(base_dir + "/" + f, libs_path="libs/aal/", root_path="", no_exec=True, web=True)["mm"]
    except:
        # Compilation Error
        return '{"agents" : [], "services" : [], "types" : [], "data" : [], "clauses" : [], "dataTypes" : [], "actorTypes" : []}'

    agents = ",".join(mm.get_declared(dtype="agents"))
    services = ",".join(mm.get_declared(dtype="services"))
    data = ",".join(mm.get_declared(dtype="data"))

    tts = mm.aalprog.get_declared(m_type)
    types = ",".join(mm.get_declared(dtype="types"))
    # Filter by data type / actor type
    actorTypes = ",".join(['"' + str(x.name) + '"' for x in list(filter(lambda x: x.subtype_of("Actor"), tts))])
    dataTypes = ",".join(['"' + str(x.name) + '"' for x in list(filter(lambda x: x.subtype_of("data"), tts))])

    clauses = ",".join(['"' + str(x.name) + '"' for x in mm.aalprog.clauses])
    res = '{"agents" : [' + agents + '], "services" : [' + services + '], "types" : [' + \
          types + '], "data" : [' + data + '], "clauses" : [' + clauses + ']' + ', "dataTypes" : [' +\
          dataTypes + ']' + ', "actorTypes" : [' + actorTypes + ']' + '}'

    return res


# Get ps info
def api_monitor():
    # ps -a -o user,pid,%cpu,%mem,start,time,command
    p = Popen(['ps', '-aL', '-o', 'user,pid,%cpu,%mem,time,command'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
    sts = p.stdout.read().decode("utf-8")
    sts = sts.split("\n")
    sts2 = [' '.join(x.split()) for x in sts][1:]

    pss = ""
    for x in sts2:
        x = x.split(" ")
        if len(x) >= 5:
            cmd = ' '.join(x[5:])
            if is_cmd_allowed(cmd):
                pss += (
                    "{"
                    " \"user\": \"" + x[0] + "\","
                    " \"pid\" : \"" + x[1] + "\","
                    " \"cpu\" : \"" + x[2] + "\","
                    " \"mem\" : \"" + x[3] + "\","
                    " \"time\": \"" + x[4] + "\","
                    " \"cmd\" : \"" + cmd + "\" "
                    "},"
                )
    pss = pss[:-1]

    json = "{\"ps\" : [ " + pss + " ]}"
    return json


# kill process by id
def api_kill_ps(pid):
    p = Popen(['kill', '-KILL', pid], stdout=PIPE, stderr=PIPE, stdin=PIPE)
    return p.stdout.read().decode("utf-8")


# Macro API
def api_macro_call(f, macro_name, macro_args):

    res = ""
    try:
        res = aalc(base_dir + "/" + f, libs_path="libs/aal/", root_path="", web=True)

        # Save current context
        sysout = sys.stdout
        syserr = sys.stderr

        # Capture the output
        reportSIO = StringIO()
        reportEIO = StringIO()
        sys.stdout = reportSIO
        sys.stderr = reportEIO
        res["mm"].call(macro_name, macro_args[1:-1].split(','))
        res = reportSIO.getvalue() + "\n" + reportEIO.getvalue()

        # Restore context
        sys.stdout = sysout
        sys.stderr = syserr
    except Exception as e:
        res = "Compilation Error : " + str(e)

    print(res)
    res = to_html_colors(res)
    return res.replace("\n", "<br>")


# Gen Djfodtlmon
def api_gen_Djfodtlmon(file, spec):
    try:
        mspec = MappingSpec()
        tmp = spec.split(";")
        for x in tmp:
            tmp2 = x.split(":")
            if len(tmp2) > 1:
                args = tmp2[1].split("=>")
                if tmp2[0] == "clause":
                    if len(args) > 2:
                        mspec.clauses.append(MappingSpec.ClauseMap(args[0], args[1], args[2]))
                elif tmp2[0] == "service":
                    if len(args) > 1:
                        mspec.services.append(MappingSpec.ServiceMap(args[0], args[1]))
                elif tmp2[0] == "agent":
                    if len(args) > 1:
                        mspec.agents.append(MappingSpec.AgentMap(args[0], args[1]))
                elif tmp2[0] == "type":
                    if len(args) > 1:
                        mspec.types.append(MappingSpec.TypeMap(args[0], args[1]))

        mm = aalc(base_dir + "/" + file, libs_path="libs/aal/", root_path="", no_exec=True, web=True)["mm"]
        res = AALtoDJFODTLMON(mm, mspec)
        api_write_file(file.replace('.aal', '.py'), res)
        return file.replace('.aal', '.py')
    except:
        # Compilation Error
        return 'Error'
