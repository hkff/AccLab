"""
LDAPConnectors
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
from ldap3 import Server, Connection, ALL


def LDAP_Connect(server, port, username, password):
    try:
        s = Server(server, int(port), get_info=ALL)
        c = Connection(s, user=username, password=password)

        if not c.bind():
            print('error in bind', c.result)
            return "Not connected to LDAP"
    except:
        return "Exception : Not connected to LDAP"

    return "Connected to LDAP"
