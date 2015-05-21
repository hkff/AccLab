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

import sys
import os
import platform

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

check_env()


# Import others modules
#from antlr4 import *
from grammar.tspass.TSPASSLexer import TSPASSLexer
from grammar.tspass.TSPASSParser import TSPASSParser
from antlr4.error.ErrorListener import ErrorListener
from grammar.aal.AALLexer import AALLexer
from grammar.aal.AALParser import AALParser
#from grammar.AALListener import AALListener
# from behave import runner
from antlr4.tree.Trees import Trees
from subprocess import Popen, PIPE
from ASTprinter import Trees2
from tools.hottie import hot
from AALMetaModel import *
from AALChecker import *
from pprint import *
from FOTLSynthesizer import *
from AALtoFOTL import *
from shell import *
import pickle
import getopt
import time
import io


# DescriptiveErrorListener
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
def aalc(file, use_shell: bool=False, check: bool=False, monodic: bool=False, compile: bool=False,
         libs_path="libs/aal/", root_path=None, recompile: bool=False, to_ltl: bool=False, show_ast: bool=False):
    """
    Parse AAL.
    :param file: The AAL input file
    :param use_shell: Run an interactive shell after parsing
    :param check: Perform a various checks
    :param monodic: Perform the monodic test
    :param compile: Compile the AAL file into aalc
    :param libs_path: The standard library path
    :param root_path: Base path
    :param recompile: Recompile the file
    :param to_ltl: Transform AAL code into FOTL formula
    :param show_ast: Show an interactive AST graph in a web page
    :return: {"res": the result, "mm": the metamodel instance}
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

    res = ""
    if monodic or check:  # Monodic test
        res += check_aal(l, verbose=check)

    if to_ltl:  # FOTL translation
        ltl_trans = AALtoFOTL(l)
        res += "\n------------------------- FOTL Translation start -------------------------\n"
        res += ltl_trans
        # Write in disk
        with open(file.replace("aal", "tspass"), mode='w') as f:
            f.write(ltl_trans)
        res += "\n-------------------------- FOTL Translation end --------------------------\n"

    if compile:  # Compile aal file to aalc
        sys.setrecursionlimit(3000)
        with open(file+"c", "wb") as f:
            pickle.dump(l, f, pickle.HIGHEST_PROTOCOL)

    if show_ast:  # Show AST
        from tools.visu import Visu
        Visu.show_ast(l.aalprog)

    if use_shell:  # Run the shell
        shell(l)

    return {"res": res, "mm": l}
    # TODO add interactive mode for macros


# tspassc
def tspassc(file=None, code="", output="tests/tmp.tspass", use_shell=False, debug: bool=False,
            synth: bool=False, reparse: bool=False):
    """
    Parse tspass
    :param file: The tspass input file
    :param code: The tspass code (if a file is given the code will be ignored)
    :param output: The output parsing file
    :param use_shell: Run an interactive shell after parsing
    :param debug: boolean enable/disable debug messages
    :param synth: Synthesize monitors specifications from a global FOTL formula
    :return:
    """
    # TODO add binaries for win
    p = sys.platform
    if p.startswith("linux"):
        os_name = "linux"
    elif p.startswith("darwin"):
        os_name = "mac"
    elif p.startswith("win"):
        os_name = "win"
        print(Color("{autored}Windows is not supported yet {/red}"))
        sys.exit(-1)
    else:
        print(Color("{autored}Unknown platform " + p + "{/red}"))
        sys.exit(-1)

    res = ""
    if file is not None:  # Handle code from file
        if reparse:
            input_file = FileStream(file)
            lexer = TSPASSLexer(input_file)
            stream = CommonTokenStream(lexer)
            parser = TSPASSParser(stream)
            parser.buildParseTrees = True

            if synth:  # Adding synthesizer
                parser.addParseListener(FOTLCompilerListener())
                tr = parser.program()
            else:
                tr = parser.formula()

            bt = Trees2.tspassTree(tr, recog=parser)
            # print(bt)
        else:
            with open(file, mode='r') as f:
                bt = f.read()
        generated_tspass = file.replace(".tspass", "_gen.tspass")
    else:  # Handle code from string
        generated_tspass = output.replace(".tspass", "_gen.tspass")
        bt = code

    fotl_file = generated_tspass.replace(".tspass", ".fotl")
    result_file = generated_tspass.replace(".tspass", ".result")

    # TSPASS parsing
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

    with open(result_file, mode='w') as f:  # Writing the result
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
    """
    Compile the standard AAL library (all AAL files in libs/aal/)
    :return:
    """
    libs_path = "libs/aal/"
    for root, dirs, files in os.walk(libs_path):
        for file in files:
            tmp = os.path.join(root, file)
            if tmp.endswith(".aal"):
                aalc(tmp, compile=True)


###################
# Main
###################
def main(argv):
    """
    Main aalc
    :param argv:
    :return:
    """
    inputfile = ""
    outputfile = ""
    helpStr = "Usage : aalc.py [-c] [-i <inputfile>] [-s]"
    help_str_extended = "AAL tools set. aalc is a part of Acclab tool.\n" +\
                        "For more information see AccLab home page\n Usage : aalc.py [OPTIONS]" +\
        "\n  -h \t--help          " + "\t display this help and exit" +\
        "\n  -i \t--input         " + "\t the input file" +\
        "\n  -c \t--compile       " + "\t compile the file, that can be loaded after using -l" +\
        "\n  -m \t--monodic       " + "\t apply monodic check on aal file" +\
        "\n  -s \t--shell         " + "\t run a shell after handling aal program" +\
        "\n  -k \t--check         " + "\t perform a verbose check" +\
        "\n  -l \t--load          " + "\t load a compiled aal file (.aalc) and run a shell" +\
        "\n  -t \t--ltl           " + "\t translate the aal program into FOTL" +\
        "\n  -r \t--reparse       " + "\t reparse tspass file" +\
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
    synth = False
    reparse = False

    # Checking options
    try:
        opts, args = getopt.getopt(argv[1:], "hi:o:cmsktlrbxdaSr",
                                   ["help", "input=", "ofile=", "compile", "monodic",
                                   "shell", "check", "load", "recompile", "init",
                                   "no-colors", "compile-stdlib", "hotswap", "ast", "synth", "reparse"])
    except getopt.GetoptError:
        print(helpStr)
        sys.exit(2)

    if len(opts) == 0:
        print(help_str_extended)

    # Handling options
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
        elif opt in ("-S", "--synth"):
            synth = True
        elif opt in ("-r", "--reparse"):
            reparse = True

    # Use hot swapping decoration on all AALMetaModel classes
    # use this option for debug only
    if hotswaping:
        import inspect
        import AALMetaModel
        for name, obj in inspect.getmembers(AALMetaModel):
            if inspect.isclass(obj):
                if "AALMetaModel" in str(obj):
                    obj = hot(obj)

    if initialize:
        check_env()

    elif load and inputfile.endswith(".aalc"):  # Load a compiled AAL file
        sys.setrecursionlimit(3000)
        with open(inputfile, "rb") as f:
            l = pickle.load(f)
        shell(l)

    elif inputfile.endswith(".aal"):  # Use AAL compiler
        res = aalc(inputfile, use_shell=use_shell, check=check, monodic=monodic, compile=compile, recompile=recompile,
             to_ltl=to_ltl, show_ast=show_ast)
        print(res["res"])

    elif inputfile.endswith(".tspass"):  # Use tspass compiler
        res = tspassc(inputfile, use_shell=False, debug=False, synth=synth, reparse=reparse)
        print(res["print"])


# Call the main
if __name__ == '__main__':
    main(sys.argv)
