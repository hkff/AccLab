#!/usr/local/bin/python3.4
"""
<one line to give the program's name and a brief idea of what it does.>
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
# def tspassc(file=None, code="", output="tests/tmp.tspass", use_shell=False, debug=False):
#     return {"res": "sat", "print": "res"}


import getopt
from antlr4 import *
from grammar.tspass.TSPASSLexer import TSPASSLexer
from grammar.tspass.TSPASSParser import TSPASSParser
from grammar.aal.AALLexer import AALLexer
from grammar.aal.AALParser import AALParser
#from grammar.AALListener import AALListener
# from behave import runner
from ASTprinter import Trees2
from antlr4.tree.Trees import Trees
import os
import platform
from AALMetaModel import *
from AALChecker import *
from subprocess import Popen, PIPE
from pprint import *
from shell import *
import pickle
import sys
import io
import time
from tools.hottie import hot
from antlr4.error.ErrorListener import ErrorListener
from AALtoFOTL import *

class DescriptiveErrorListener(ErrorListener):
    """
    Error Listener
    """
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("line " + str(line) + ":" + str(column) + " " + msg)
        self.errors.append("line " + str(line) + ":" + str(column) + " " + msg)

# aalc
def aalc(file, use_shell=False, check=False, monodic=False, compile=False, libs_path="libs/aal/",
         root_path=None, recompile=False, to_ltl=False, show_ast=False):
    """
    Parse AAL
    :param file:
    :return:
    """
    from AALCompiler import AALCompilerListener

    inputfile = FileStream(file)
    lexer = AALLexer(inputfile)
    stream = CommonTokenStream(lexer)
    parser = AALParser(stream)
    desec = DescriptiveErrorListener()
    parser.addParseListener(AALCompilerListener(file=file, libs_path=libs_path, recompile=recompile,
                                                root_path=root_path, errors_listener=desec))
    parser.addErrorListener(desec)
    parser.buildParseTrees = True

    # TODO : important prediction mode optimization (we gain x5 speed up with SLL)
    # use SLL for the first pass, if an error detected we probably have to make a second pass
    # using LL mode (to check, see the doc)
    # parser._interp.predictionMode = PredictionMode.LL  # ~2.5
    parser._interp.predictionMode = PredictionMode.SLL  # ~0.4
    # parser._interp.predictionMode = PredictionMode.LL_EXACT_AMBIG_DETECTION  # ~2.5

    start_time = time.time()
    tr = parser.main()
    exec_time = time.time() - start_time
    print("\nExecution time : " + str(exec_time))

    bt = Trees.toStringTree(tr, recog=parser)
    # print(bt)
    l = parser.getParseListeners().pop(0)
    #print(l.aalprog.clauses[0].usage.to_ltl())

    res = ""
    if monodic or check:
        res += check_aal(l, verbose=check)

    if to_ltl:
        ltl_trans = AALtoFOTL(l)
        res += "\n------------------------- FOTL Translation start -------------------------\n"
        res += ltl_trans
        # Write in disk
        with open(file.replace("aal", "tspass"), mode='w') as f:
            f.write(ltl_trans)
        res += "\n-------------------------- FOTL Translation end --------------------------\n"
    print(res)

    if compile:
        sys.setrecursionlimit(3000)
        with open(file+"c", "wb") as f:
            pickle.dump(l, f, pickle.HIGHEST_PROTOCOL)

    # Show AST
    if show_ast:
        from tools.visu import Visu
        Visu.show_ast(l.aalprog)

    # Run the shell
    if use_shell:
        shell(l)
    res2 = {}
    res2["res"] = res
    res2["mm"] = l
    return res2
# TODO add interactive mode for macros


# tspassc
def tspassc(file=None, code="", output="tests/tmp.tspass", use_shell=False, debug=False):
    """
    Parse tspass
    :param file:
    :return:
    """
    # TODO add binaries for win and mac
    os_name = "linux"
    p = sys.platform
    if p.startswith("linux"):
        os_name = "linux"
    elif p.startswith("darwin"):
        os_name = "mac"
    elif p.startswith("win"):
        os_name = "win"
    else:
        print(Color("{autored}Unknown platform " + p + "{/red}"))
        sys.exit(-1)

    res = ""
    # Handle code from file
    if file is not None:
        inputfile = FileStream(file)
        lexer = TSPASSLexer(inputfile)
        stream = CommonTokenStream(lexer)
        parser = TSPASSParser(stream)
        parser.buildParseTrees = True
        tr = parser.formula()
        bt = Trees2.tspassTree(tr, recog=parser)
        #print(bt)
        generated_tspass = file.replace(".tspass", "_gen.tspass")
    else:  # Handle code from string
        generated_tspass = output.replace(".tspass", "_gen.tspass")
        bt = code

    fotl_file = generated_tspass.replace(".tspass", ".fotl")
    result_file = generated_tspass.replace(".tspass", ".result")

    # TSPASS parsing
    # os.remove(generated_tspass )
    with open(generated_tspass, mode='w') as f:
        f.write(bt)
    if debug:
        pprint(bt)

    # FOTL Translate
    p = Popen(['tools/' + os_name + '/fotl-translate', generated_tspass], stdout=PIPE, stderr=PIPE, stdin=PIPE)
    fotl = p.stdout.read().decode("utf-8")
    if fotl == "":
        fotl = p.stderr.read().decode("utf-8")
        res += fotl + "\n"
    if debug:
        print(fotl)
        print(p.stderr.read().decode("utf-8"))

    # exec("os.system('rm -f tools/demo.fotl')")
    with open(fotl_file, mode='w') as f:
        f.write(fotl)

    # TSPASS
    p = Popen(['tools/' + os_name + '/tspass', fotl_file], stdout=PIPE, stderr=PIPE, stdin=PIPE)
    tspass = p.stdout.read().decode("utf-8")
    if tspass == "":
        tspass = p.stderr.read().decode("utf-8")
        res += tspass + "\n"
    if debug:
        print(tspass)
        print(p.stderr.read().decode("utf-8"))

    # exec("os.system('rm -f tools/demo.result')")
    with open(result_file, mode='w') as f:
        f.write(tspass)

    lookup = "SPASS beiseite:"
    sat = ""
    for line in tspass.split("\n"):
        if lookup in line:
            res += "[TSPASS] " + line.replace("SPASS beiseite:", "")
            sat = line.replace("SPASS beiseite:", "").replace(".", "").replace(" ", "")
            break

    return {"res": sat, "print": res}


# Compile the standard AAL lib
def compile_stdlib():
    libs_path = "libs/aal/"
    for root, dirs, files in os.walk(libs_path):
        for file in files:
            tmp = os.path.join(root, file)
            if tmp.endswith(".aal"):
                aalc(tmp, compile=True)


# Check environment
def check_env():
    python_version = platform.python_version()
    machine = platform.machine()
    system = platform.system()
    if python_version < '3.4':
        print("Python 3.4.x needed :: current version " + python_version)
        sys.exit(-1)

    if sys.platform.startswith("win"):
        Windows.enable()

    try:
        import readline
    except:
        print(Color("{autored}[Warning] You need to install readline module to use the shell.{/red}\n" +
                    "Please visit {autogreen}https://pypi.python.org/pypi/readline{/green}\n"))


###################
# Main
###################
def main(argv):
    """
    Main aalc
    :param argv:
    :return:
    """
    check_env()

    inputfile = ""
    outputfile = ""
    helpStr = "Usage : aalc.py [-c] [-i <inputfile>] [-s]"
    help_str_extended = "aal compiler tool. aalc is a part of Acclab tool.\n" +\
                        "For more information see AccLab home page\n Usage : aalc.py [OPTIONS]" +\
        "\n  -h \t--help          " + "\t display this help and exit" +\
        "\n  -i \t--input         " + "\t the input file" +\
        "\n  -c \t--compile       " + "\t compile the file, that can be loaded after using -l" +\
        "\n  -m \t--monodic       " + "\t apply monodic check on aal file" +\
        "\n  -s \t--shell         " + "\t run a shell after handling aal program" +\
        "\n  -k \t--check         " + "\t perform a verbose check" +\
        "\n  -l \t--load          " + "\t load a compiled aal file (.aalc) and run a shell" +\
        "\n  -t \t--ltl           " + "\t translate the aal program into FOTL" +\
        "\n  -r \t--recompile     " + "\t recompile the external files " +\
        "\n  -b \t--no-colors     " + "\t disable colors in output" +\
        "\n  -x \t--compile-stdlib" + "\t compile the standard library" +\
        "\n  -d \t--hotswap       " + "\t enable hotswaping (for development only)" +\
        "\n  -a \t--ast           " + "\t show ast tree" +\
        "\n\nReport aalc bugs to walid.benghabrit@mines-nantes.fr" +\
        "\nAccLab home page: <http://www.emn.fr/z-info/acclab/>" +\
        "\naalc is a free software released under GPL 3"



    compile = False
    use_shell = False
    monodic = False
    check = False
    load = False
    recompile = False
    initialize = False
    to_ltl = False
    hotswaping = False
    show_ast = False

    try:
        opts, args = getopt.getopt(argv[1:], "hi:o:cmsktlrbxda", ["help", "input=", "ofile=", "compile", "monodic",
                                                                 "shell", "check", "load", "recompile", "init",
                                                                 "no-colors", "compile-stdlib", "hotswap", "ast"])
    except getopt.GetoptError:
        print(helpStr)
        sys.exit(2)

    if len(opts) == 0:
        print(help_str_extended)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(help_str_extended)
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-c", "--compile"):
            compile = True
        elif opt in ("-m", "--monodic"):
            monodic = True
        elif opt in ("-k", "--check"):
            check = True
        elif opt in ("-s", "--shell"):
            use_shell = True
        elif opt in ("-l", "--load"):
            load = True
        elif opt in ("-t", "--ltl"):
            to_ltl = True
        elif opt in ("-r", "--recompile"):
            recompile = True
        elif opt in ("-z", "--init"):
            initialize = True
        elif opt in ("-b", "--no-colors"):
            disable_all_colors()
        elif opt in ("-x", "--compile-stdlib"):
            compile_stdlib()
            return
        elif opt in ("-d", "--hotswap"):
            hotswaping = True
        elif opt in ("-a", "--ast"):
            show_ast = True


    # Use hot swaping decoration on all AALMetaModel classes
    if hotswaping:
        import inspect
        import AALMetaModel
        for name, obj in inspect.getmembers(AALMetaModel):
            if inspect.isclass(obj):
                if "AALMetaModel" in str(obj):
                    obj = hot(obj)

    if initialize:
        check_env()

    elif load and inputfile.endswith(".aalc"):
        sys.setrecursionlimit(3000)
        with open(inputfile, "rb") as f:
            l = pickle.load(f)
        shell(l)

    elif inputfile.endswith(".aal"):
        aalc(inputfile, use_shell=use_shell, check=check, monodic=monodic, compile=compile, recompile=recompile,
             to_ltl=to_ltl, show_ast=show_ast)

    elif inputfile.endswith(".tspass"):
         tspassc(inputfile, use_shell=False, debug=True)


if __name__ == '__main__':
    main(sys.argv)
