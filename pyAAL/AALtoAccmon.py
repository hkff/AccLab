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
from datetime import datetime
from subprocess import Popen, PIPE
import os.path
import shutil
from AALMetaModel import *

__author__ = 'walid'


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
            self.name = name.strip()
            self.target = target.strip()

        def __str__(self):
            return "%s: %s => %s" % (self.__class__.__name__, self.name, self.target)

    class ServiceMap(BaseMap):
        pass

    class AgentMap(BaseMap):
        pass

    class TypeMap(BaseMap):
        pass

    class ClauseMap(BaseMap):
        def __init__(self, name, target, control_type):
            super().__init__(name, target)
            self.control_type = control_type.strip()

        def __str__(self):
            return "%s: %s => %s => %s" % (self.__class__.__name__, self.name, self.target, self.control_type)


# AALtoDJFODTLMON
def AALtoDJFODTLMON(mm, spec: MappingSpec, output_file=None):
    """
    Translate AAL program to Djfodtlmon using a spec file
    """
    log_attributes = []
    custom_predicates = []
    http_rules = []
    view_rules = []
    response_rules = []
    header = "###\n# Mapping file for %s\n# created on %s\n###\n" % (mm.file, datetime.today())

    ###################################
    # Attributes
    ###################################
    log_attributes.append("""
## 1. User type log attribute
def log_user_type(request, view, args, kwargs, response):
        # The evaluation function
        # Do your custom logic to determine the user type
        # The current django user can be accessed via : request.user
        #
        user_type = "..."
        return P("USER_TYPE", args=[Constant(user_type)])

# Create and add the attribute
utype_log_attr = LogAttribute('USER_TYPE', enabled=True, eval_fx=log_user_type,
    description='The type of the current user.', )
Sysmon.add_log_attribute(utype_log_attr, target=Monitor.MonType.HTTP)
    """)

    ###################################
    # Predicates/Functions
    ###################################

    ###################################
    # Rules
    ###################################
    for rule in spec.clauses:
        control_type = "Monitor.MonControlType.POSTERIORI"
        if rule.control_type == "REAL_TIME":
            control_type = "Monitor.MonControlType.REAL_TIME"

        formula = ""
        clause = mm.clause(rule.name)
        if clause is not None:
            formula = aal_clause_to_fodtl(clause)

        description = "Rule for clause %s" % rule.name

        if rule.target == "HTTP":
            http_rules.append('Sysmon.add_http_rule("%s", "%s", \n\tdescription="%s", control_type=%s)'
                                  % (rule.name, formula, description, control_type))
        elif rule.target == "VIEW":
            view_rules.append('Sysmon.add_view_rule("%s", "%s", \n\tdescription="%s", control_type=%s)'
                                  % (rule.name, formula, description, control_type))
        elif rule.target == "RESPONSE":
            response_rules.append('Sysmon.add_response_rule("%s", "%s", \n\tdescription="%s", control_type=%s)'
                                  % (rule.name, formula, description, control_type))

    ###################################
    # Result
    ###################################
    res = """%s
from accmon.sysmon import *
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


# Generate django skeleton app
def generate_django_skeleton(aal_file, spec_file, output_folder):
    """
    NOTE : consider using AST modifications for source code
    :param aal_file:
    :param spec_file:
    :param output_folder:
    :return:
    """
    project_name = "test1"
    project_path = "examples/"
    app_name = "app1"
    spec_file = "tuto2_rules.py"
    # 1. Remove previous project
    if os.path.isdir("examples/%s" % project_name):
        shutil.rmtree("examples/%s" % project_name)

    # 2. Start project
    p = Popen(['django-admin', 'startproject', project_name], stdout=PIPE, stderr=PIPE, stdin=PIPE)
    res = p.stdout.read().decode("utf-8")
    if res != "": return res

    # 3. Create app
    p = Popen(['python3', project_name+'/manage.py', 'startapp', app_name], stdout=PIPE, stderr=PIPE, stdin=PIPE)
    res = p.stdout.read().decode("utf-8")
    print(res)
    if res != "": return res

    # 4. Configure fodtlmon
    # 4.1 wsgi
    wsgi = project_name + "/" + project_name + "/wsgi.py"
    if not os.path.isfile(wsgi):
        return "wsgi file doesn't exists !"
    with open(wsgi, "a+") as f:
        f.write("from accmon.sysmon import Sysmon\nSysmon.init()\nimport %s.%s\n" % (project_name, spec_file))

    # 4.2 settings
    settings = project_name + "/" + project_name + "/settings.py"
    if not os.path.isfile(settings):
        return "settings file doesn't exists !"
    res = ""
    f = open(settings, "r")
    res = f.read()
    res = res.replace("'django.contrib.staticfiles',",
                      "'django.contrib.staticfiles',\n    'fodtlmon_middleware',\n    '%s'" % app_name)
    res = res.replace("'django.middleware.security.SecurityMiddleware',",
                      "'django.middleware.security.SecurityMiddleware',\n    'accmon.middleware.FodtlmonMiddleware'")
    f.close()
    f = open(settings, "w")
    f.flush()
    f.write(res)
    f.close()

    # 4.3 urls
    urls = project_name + "/" + project_name + "/urls.py"
    if not os.path.isfile(urls):
        return "urls file doesn't exists !"
    res = ""
    f = open(urls, "r")
    res = f.read()
    res = res.replace("from django.contrib import admin",
                      "from django.contrib import admin\nfrom accmon import urls as fodtlurls")
    res = res.replace("url(r'^admin/', include(admin.site.urls)),",
                      "url(r'^admin/', include(admin.site.urls)),\n    url(r'^mon/', include(fodtlurls.urlpatterns)),")
    f.close()
    f = open(urls, "w")
    f.flush()
    f.write(res)
    f.close()

    # Move to the path
    os.symlink(spec_file, project_name+"/"+project_name+"/"+spec_file.split("/")[-1])
    shutil.move(app_name, project_name+"/")
    shutil.move(project_name, project_path)
    return "Django !"


def aal_clause_to_fodtl(clause: m_clause):
    """
    Transform an AAL clause into fodtl formula
    :param clause:
    :return:
    """
    # TODO handle rectification
    def transform(exp: aalmmnode):
        if isinstance(exp, m_clause):
            return transform(exp.usage)
        if isinstance(exp, m_usage):
            return transform(exp.actionExp[0])

        if isinstance(exp, m_aexpQvar):
            q = [str(x) for x in exp.qvars]
            return "(" + str(" ".join(q)) + "(" + transform(exp.actionExp) + ") " + (")"*len(q)) + ")"

        if isinstance(exp, str):
            return exp
        else:
            return "<Unsupported type %s>" % exp.__class__.__name__

    return transform(clause)
