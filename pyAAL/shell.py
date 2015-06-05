"""
Shell
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

import AALCompiler
from AALChecker import *
from importlib import reload
import os
import re
import curses
from tools.hottie import hot
from AALCompiler import AALCompilerListener
# TODO : make it more user friendly

self = None

help_str = "Shell Help" +\
    "\n - call(macro, args) " + "\t call a macro where /\n" +\
    "\t\t\t   *macro : is the name of the macro\n" +\
    "\t\t\t   *args : a list of string; << ex : [\"'args1'\", \"'args2'\", ...\"'argsN'\"] >>" +\
    "\n - clauses()         " + "\t show all declared clauses in the loaded aal program" +\
    "\n - macros()          " + "\t show all declared macros in the loaded aal program" +\
    "\n - load(lib)         " + "\t load the librarie lib" +\
    "\n - quit / q          " + "\t exit the shell" +\
    "\n - help / h / man()  " + "\t show this help" +\
    "\n - self              " + "\t the current compiler instance of the loaded aal program" +\
    "\n - aalprog           " + "\t the current loaded aal program " +\
    "\n - man(arg)          " + "\t print the help for the given arg" +\
    "\n - hs(module)        " + "\t hotswaping : reload the module" +\
    "\n - r()               " + "\t hot-swaping the shell"

help_str = Color(help_str)

COMMANDS = ['clauses()', 'macros()', 'quit', 'q', 'h', 'help', 'self', 'aalprog', 'man()', 'call', 'extra']
RE_SPACE = re.compile('.*\s+$', re.M)


# Completer class
class Completer(object):
    def complete(self, text, state):
        """Generic readline completion entry point."""
        try:
           import readline
        except:
            print(Color("{autored}[ERROR] You need to install readline module to use the shell.{/red}\n"
                  "Please visit {autogreen}https://pypi.python.org/pypi/readline{/green}\n"))
            sys.exit(-1)

        buffer = readline.get_line_buffer()
        line = readline.get_line_buffer().split()
        # show all commands
        if not line:
            return [c + ' ' for c in COMMANDS][state]
        # account for last argument ending in a space
        if RE_SPACE.match(buffer):
            line.append('')
        # resolve command to the implementation function
        cmd = line[0].strip()
        if cmd in COMMANDS:
            impl = getattr(self, 'complete_%s' % cmd)
            args = line[1:]
            if args:
                return (impl(args) + [None])[state]
            return [cmd + ' '][state]
        results = [c + ' ' for c in COMMANDS if c.startswith(cmd)] + [None]
        return results[state]


# Man method
def man(args=None):
    if args is None:
        print(help_str)
    else:
        print("printing manual for " + str(args.__class__))
        arg_type = type(args)
        if isinstance(args, aalmmnode):
            print(args.man())
        else:
            AALCompilerListener.man()


# Interactive mode
@hot
def shell(listener):
    try:
        import readline
    except:
        print(Color("{autored}[ERROR] You need to install readline module to use the shell.{/red}\n"
              "Please visit {autogreen}https://pypi.python.org/pypi/readline{/green}\n"))
        sys.exit(-1)

    import shell, AALMetaModel, inspect  # For hotswaping

    stop = False
    self = listener
    aalprog = self.aalprog

    comp = Completer()
    # we want to treat '/' as part of a word, so override the delimiters
    readline.set_completer_delims(' \t\n;')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(comp.complete)

    # Load a lib on the current AAL file
    def load(lib):
        return self.load_lib(lib)

    # Call a macro on the loaded file
    def call(macro, args=None):
        if args is None:
            args = []
        return self.macro_call(macro, args)

    # Get clauses
    def clauses():
        return self.get_clauses()

    # Get macros
    def macros():
        return self.get_macros()

    # Reload shell
    def r():
        return reload(shell)

    # Reload a module
    def hs(module):
        res = reload(module)
        # Use hot swaping decoration on all AALMetaModel classes
        # NOTE : stop abusing introspection...
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj):
                if "AALMetaModel" in str(obj):
                    obj = hot(obj)
        return res

    # return
    #exec("from AALCompiler import AALCompilerListener");

    while not stop:
        cmd = input("shell >")
        # cmd = sys.stdin.read()

        if cmd == "quit" or cmd == "q":
            stop = True
        elif cmd == "help" or cmd == "h":
            man()
        else:
            try:
                res = eval(cmd)
                if res is not None:
                    print(res)
            except:
                 print("Eval error !",  sys.exc_info()[:2])
