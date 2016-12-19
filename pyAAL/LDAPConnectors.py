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
from ldap3 import Server, Connection, ALL, SUBTREE


def LDAP_Connect(server, port, username, password):
    try:
        s = Server(server, int(port), get_info=ALL)
        c = Connection(s, user=username, password=password)

        if not c.bind():
            print('error in bind', c.result)
            return None
    except:
        print("Exception : Not connected to LDAP")
        return None

    return c


def LDAP_Import(server, port, username, password, usersDN, groupsDN):
    c = LDAP_Connect(server, port, username, password)
    if c is None:
        return "Error : Connection to LDAP error"
    else:
        res = ""
        total_entries = 0
        search_filter = '(objectClass=inetOrgPerson)'
        search_scope = SUBTREE,
        attributes = ['cn', 'givenName']
        paged_size = 5
        c.search(search_base=usersDN, search_filter=search_filter)

        total_entries += len(c.response)
        for entry in c.response:
            res += "%s - %s" % (entry['dn'], entry['attributes'])

        return res
