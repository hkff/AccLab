"""
Server
Copyright (C) 2016 Walid Benghabrit

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
from fodtlmon.webservice.webservice import Webservice
import sys

if __name__ == "__main__":
    try:
        server_port = 9999 if len(sys.argv) == 1 else int(sys.argv[1])
    except:
        server_port = 9999
    Webservice.start(server_port)
