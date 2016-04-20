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
from threading import Thread
from time import sleep
try:
    from fodtlmon.fodtl.fodtlmon import *
except:
    pass

__author__ = 'walid'

import os
from urllib.parse import *
import sys, shutil
from io import StringIO
from aalc import *
from AALtoAccmon import *
import json
base_dir = "examples"

ALLOWED_CMD = ["tspass", "aalc.py", "fotl-translate", "manage.py"]


# Filter ps
def is_cmd_allowed(cmds):
    for x in ALLOWED_CMD:
        if x in cmds:
            return True
    return False


#  List dir
def api_list_dir(wpath):
    tmp = "["
    dirs = sorted(os.listdir(wpath)[::-1])
    for d in dirs:
        if d.startswith("."):
            continue
        tmp += '{' + '"id":"' + wpath+'/'+d + '", "text":"' + d + '"," iconCls":""'

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
    res = -1
    # Add \n at the end
    if d[-1] != "\n":
        d += "\n"
    with open(base_dir + "/" + f, "w+") as fd:
        res = str(fd.write(d))
    check_aal_acd(f)
    return res


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
        api_save_prefs('{"theme": "monokai", "username": "", "fontSize": 14, "recentFiles": [] }')
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


# Compile ACD
def api_compile_acd(aal, spec):
    result = {"compliance": [], "sat": [], "error": ""}
    tmp_file = "_tmp0001_.aal"
    res = ""
    try:
        # Save current context
        sysout = sys.stdout
        syserr = sys.stderr

        # Capture the output
        reportSIO = StringIO()
        reportEIO = StringIO()
        sys.stdout = reportSIO
        sys.stderr = reportEIO

        api_write_file(tmp_file, aal)
        res = aalc(base_dir + "/" + tmp_file, libs_path="libs/aal/", root_path="", web=False)

        # Handling Sat
        for c in res["mm"].aalprog.clauses:
            clause = str(c.name)
            tmp = validate2(res["mm"], "(always (" + c.usage.to_ltl() + "))", check=True)
            result["sat"].append({clause: tmp["sat"]})

        # Handling Compliance
        specs = spec.split(";")
        for x in specs:
            x = x.strip()
            sp = x.split("->")
            if len(sp) == 2:
                _c1 = res["mm"].clause(sp[0].strip())
                _c2 = res["mm"].clause(sp[1].strip())
                tmp = validate(res["mm"], _c1, _c2, resolve=False, verbose=False, use_always=False, acc_formula=0, chk='neg')
                result["compliance"].append({x: tmp["ok"]})

        res = reportSIO.getvalue() + "\n" + reportEIO.getvalue()
        # Restore context
        sys.stdout = sysout
        sys.stderr = syserr
    except Exception as e:
        result["error"] += "\nCompilation Error : " + str(e) + "\n"
    finally:
        result["error"] += res
        result["error"] = to_html_colors(result["error"].replace("\n", "</br>"))
        api_delete_file(tmp_file)
    return json.dumps(result)


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


# Gen accmon
def api_gen_accmon(file, spec):
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
        file_name = file.replace('.aal', '_rules.py')
        api_write_file(file_name, res)
        return file_name
    except:
        # Compilation Error
        return 'Error'


# Generate django app skeleton
def api_generate_django(aal_file, spec_file, output_folder):
    return generate_django_skeleton(aal_file, spec_file, output_folder)


# Run django app
def api_run_django(app, port=9000):
    p = Popen(['python3', "examples/"+app, 'migrate'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
    # p = Popen(['python3', "examples/"+app, 'runserver', str(port)], stdout=PIPE, stderr=PIPE, stdin=PIPE)

    # IMPORTANT: Run the server using non blocking IO in order to capture errors and show them to the client
    from queue import Queue, Empty
    ON_POSIX = 'posix' in sys.builtin_module_names

    def enqueue_output(out, err, queue):
        for line in iter(out.readline, b''):
            queue.put(line.decode("utf-8"))
        out.close()
        for line in iter(err.readline, b''):
            queue.put(line.decode("utf-8"))
        err.close()

    p = Popen(['python3', "examples/"+app, 'runserver', str(port)], stdout=PIPE, stderr=PIPE, stdin=PIPE,
              bufsize=1, close_fds=ON_POSIX)
    q = Queue()
    t = Thread(target=enqueue_output, args=(p.stdout, p.stderr, q))
    t.daemon = True
    t.start()

    # Wait to get some data
    sleep(5)

    # Get output
    items = []
    max = 100
    for numOfItemsRetrieved in range(0, max):
        try:
            if numOfItemsRetrieved == max:
                break
            items.append(q.get_nowait())
        except Exception:
            break
    print("=====================================")
    print("".join(items))
    print("=====================================")
    return "".join(items).replace("\n", "<br>")


# Convert Fodtl formula to vFodtl diagram
def api_fodtl_to_vfodtl(formula):
    print(formula)
    try:
        from fodtlmon.parser.Parser import FodtlParser
    except:
        return "fodtlmon is not installed !"
    try:
        def prg(formula):
            res = ""
            js_class = "Fodtl_%s" % formula.__class__.__name__.lower()

            if isinstance(formula, Predicate):
                arguments = []
                for x in formula.args:
                    arguments.append(prg(x))

                res = '{ "%s": [%s] }' % (js_class, ",".join(arguments))

            elif isinstance(formula, Constant):
                res = '{ "%s": {"Fodtl_value": "%s"} }' % (js_class, formula.name)

            elif isinstance(formula, Variable):
                res = '{ "%s": {"Fodtl_value": "%s"} }' % (js_class, formula.name)

            elif isinstance(formula, At):
                pass

            elif isinstance(formula, Forall):
                pass

            elif isinstance(formula, Exists):
                pass

            elif isinstance(formula, true) or isinstance(formula, false):
                res = '{ "%s": "" }' % js_class

            elif isinstance(formula, UExp):
                inner = prg(formula.inner)
                res = '{"%s" : %s}' % (js_class, inner)

            elif isinstance(formula, BExp):
                exp1 = prg(formula.left)
                exp2 = prg(formula.right)
                res = '{ "%s" : [%s, %s] }' % (js_class, exp1, exp2)

            else:
                raise Exception("Error %s of type %s" % (formula, type(formula)))
            return res

        f = FodtlParser.parse(formula)
        res = prg(f)
        return res
    except Exception as e:
        return "%s" % e


# Register formula in accmon
def api_register_accmon_monitor(formula, mon_name, accmon_url):
    import urllib.request, urllib.parse
    res = "Error"
    values = {'formula_id': mon_name, 'formula': formula}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes
    url = accmon_url + "/sysmon/remote/register_formula/"
    with urllib.request.urlopen(url, data) as response:
        res = str(response.read())
        print(res)

    return res


# Transform a clause into Fodtl formula
def api_clause_to_fodtl(file, clause):
    res = "Error"
    mm = aalc(base_dir + "/" + file, libs_path="libs/aal/", root_path="", no_exec=True, web=True)["mm"]
    if mm is not None:
        c = mm.clause(clause)
        if c is not None:
            res = aal_clause_to_fodtl(c)
    return res


# Check and update the corresponding acd/aal file
def check_aal_acd(file):
    def get_clause_node_from_json(acd, clause):
        for x in acd:
            if x["type"] == "PolicyUI":
                c_name = re.search(r'CLAUSE \w+', x["policy"]).group(0).replace("CLAUSE ", "")
                if c_name == clause:
                    return x
        return None

    ext = file.split(".")[-1]
    if ext == "acd":
        # Check acd file
        aal_file_name = base_dir+"/"+file.replace(".acd", ".aal")
        acd_file_name = base_dir+"/"+file
        if os.path.isfile(aal_file_name):  # The corresponding aal file exists
            acd_file = ""
            aal_file = ""

            # Read acd and aal files
            with open(acd_file_name, "r") as f:
                acd_file = json.loads(f.read())
            with open(aal_file_name, "r") as f:
                aal_file = f.read()

            mm = aalc(aal_file_name, libs_path="libs/aal/", root_path="", no_exec=True, web=False)["mm"]
            if mm is not None:
                inputfile = FileStream(aal_file_name)

                # Update aal file
                for x in acd_file:
                    if x["type"] == "PolicyUI":
                        clause_name = re.search(r'CLAUSE \w+', x["policy"]).group(0)
                        if clause_name not in aal_file:  # Add the clause in the aal file
                            aal_file += "\n" + x["policy"]
                        else:  # Update the clause
                            cl = mm.clause(clause_name.replace("CLAUSE ", ""))
                            if cl is not None:
                                rng = cl.source_range
                                original_clause = inputfile.getText(rng[0], rng[1])
                                if x["policy"] != original_clause:
                                    aal_file = aal_file.replace(original_clause, x["policy"])
                        # TODO remove deleted clause

                # Save aal file
                with open(aal_file_name, "w") as f:
                    f.write(aal_file)

    elif ext == "aal":
        # Check aal file
        aal_file_name = base_dir+"/"+file
        acd_file_name = base_dir+"/"+file.replace(".aal", ".acd")
        if os.path.isfile(acd_file_name):  # The corresponding acd file exists
            acd_file = ""
            aal_file = ""

            # Read acd and aal files
            with open(acd_file_name, "r") as f:
                acd_file = json.loads(f.read())
            with open(aal_file_name, "r") as f:
                aal_file = f.read()

            mm = aalc(aal_file_name, libs_path="libs/aal/", root_path="", no_exec=True, web=False)["mm"]

            if mm is not None:
                inputfile = FileStream(aal_file_name)

                # Update acd file
                for x in mm.aalprog.clauses:
                    c = get_clause_node_from_json(acd_file, str(x.name))
                    if c is not None:
                        rng = x.source_range
                        original_clause = inputfile.getText(rng[0], rng[1])
                        if c["policy"] != original_clause:
                            c["policy"] = original_clause

                # Save acd file
                with open(acd_file_name, "w") as f:
                    json.dump(acd_file, f)
