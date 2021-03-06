"""
antlr tool
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

# A basic script that generate calls antlr on AAL/TSPASS grammar files

import sys
import os

cmd = sys.argv[1]
if cmd == "aal":
    exec("os.system('java -jar grammar/antlr4.5.1.jar -Dlanguage=Python3 grammar/aal/AAL.g4')")
elif cmd == "tspass":
        exec("os.system('java -jar grammar/antlr4.5.1.jar -Dlanguage=Python3 grammar/tspass/TSPASS.g4')")
elif cmd == "aaljs":
    exec("os.system('java -jar grammar/antlr4.5.1.jar -Dlanguage=JavaScript grammar/aal/AAL.g4')")