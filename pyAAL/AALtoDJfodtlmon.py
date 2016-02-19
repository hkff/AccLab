"""
AALtoDJfodtlmon
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

from AALMetaModel import *


class MappingSpec:
    """
    Service ->
    Agent ->
    Type ->
    Clause ->
    """
    def __init__(self):
        self.services = []
        self.agents = []
        self.types = []
        self.clauses = []

    class BaseMap:
        def __init__(self, name, target):
            self.name = name
            self.target = target

    class ServiceMap(BaseMap):
        pass

    class AgentMap(BaseMap):
        pass

    class TypeMap(BaseMap):
        pass

    class ClauseMap(BaseMap):
        def __init__(self, name, target, control_type):
            super().__init__(name, target)
            self.control_type = control_type


# AALtoDJFODTLMON
def AALtoDJFODTLMON(mm: aalmm, spec: MappingSpec, output_file=None):
    log_attributes = []
    custom_predicates = []
    http_rules = []
    view_rules = []
    response_rules = []
    header = ""

    res = """# %s
from fodtlmon_middleware.sysmon import *
from django.contrib.auth.models import User

################################
# Custom attributes to log
################################
%s

################################
# Custom predicates/functions
################################
%s

################################
# HTTP request rules
################################
%s

################################
# View rules
################################
%s

################################
# Response rules
################################
%s
    """ % (header, "\n".join(log_attributes), "\n".join(custom_predicates), "\n".join(http_rules),
           "\n".join(view_rules), "\n".join(response_rules))
    return res
