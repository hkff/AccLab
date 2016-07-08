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
    # res = p.stdout.read().decode("utf-8")
    res = p.stderr.read().decode("utf-8")
    if res != "": return res

    # 3. Create app
    p = Popen(['python3', project_name+'/manage.py', 'startapp', app_name], stdout=PIPE, stderr=PIPE, stdin=PIPE)
    res = p.stderr.read().decode("utf-8")
    if res != "":
        # Rollaback
        if os.path.isdir(project_name): shutil.rmtree(project_name)
        if os.path.isdir(app_name): shutil.rmtree(app_name)
        return res

    # 4. Configure fodtlmon
    # 4.1 wsgi
    wsgi = project_name + "/" + project_name + "/wsgi.py"
    admin = "from django.contrib.auth.models import User\n# Create a superuser (for test only)\n" \
            "if len(User.objects.filter(username='root')) == 0:\n"\
            "\tUser.objects.create_superuser(username='root', password='root', email='')"
    if not os.path.isfile(wsgi):
        return "wsgi file doesn't exists !"
    with open(wsgi, "a+") as f:
        f.write("\nfrom accmon.sysmon import Sysmon\nSysmon.init()\nimport %s.%s\n\n%s\n"
                % (project_name, spec_file.replace(".py", ""), admin))

    # 4.2 settings
    settings = project_name + "/" + project_name + "/settings.py"
    if not os.path.isfile(settings):
        return "settings file doesn't exists !"
    res = ""
    f = open(settings, "r")
    res = f.read()
    res = res.replace("'django.contrib.staticfiles',",
                      "'django.contrib.staticfiles',\n    'accmon',\n    '%s'" % app_name)
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

    # Move app to the project path
    shutil.move(app_name, project_name+"/")

    # Migration
    p = Popen(['python3', project_name+'/manage.py', 'makemigrations'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
    res = p.stderr.read().decode("utf-8")
    if res != "":
        # Rollaback
        if os.path.isdir(project_name): shutil.rmtree(project_name)
        if os.path.isdir(app_name): shutil.rmtree(app_name)
        return res

    p = Popen(['python3', project_name+'/manage.py', 'migrate'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
    res = p.stderr.read().decode("utf-8")
    if res != "":
        # Rollaback
        if os.path.isdir(project_name): shutil.rmtree(project_name)
        if os.path.isdir(app_name): shutil.rmtree(app_name)
        return res

    # Copy the spec file
    shutil.copy(project_path + spec_file, project_name+"/"+project_name+"/"+spec_file.split("/")[-1])

    # Move project
    shutil.move(project_name, project_path)

    return "Django !"


def aal_clause_to_fodtl(clause: m_clause):
    """
    Transform an AAL clause into fodtl formula
    :param clause:
    :return:
    """
    # TODO handle rectification
    def transform(exp: aalmmnode, ref=False):
        if isinstance(exp, m_clause):
            return transform(exp.usage)
        elif isinstance(exp, m_usage):
            return transform(exp.actionExp[0])

        elif isinstance(exp, m_aexpQvar):
            qs = ""
            for x in exp.qvars:
                qs += transform(x) + "("
            return "%s %s %s" % (qs, transform(exp.actionExp), (")"*(len(exp.qvars))))

        elif isinstance(exp, m_qvar):
            if ref:
                return "%s" % exp.variable.name
            else:
                return "%s[%s]" % (exp.quant.to_ltl(), transform(exp.variable, ref=ref))

        elif isinstance(exp, m_ref):
            return transform(exp.target, ref=ref)

        elif isinstance(exp, m_aexpComb):
            return "(%s %s %s)" % (transform(exp.actionExp1), transform(exp.operator), transform(exp.actionExp2))

        elif isinstance(exp, m_aexpIfthen):
            return "((%s) => (%s))" % (transform(exp.condition), transform(exp.branchTrue))

        elif isinstance(exp, m_booleanOp):
            if exp == m_booleanOp.O_and: return "&"
            elif exp == m_booleanOp.O_or: return "|"
            elif exp == m_booleanOp.O_not: return "~"
            elif exp == m_booleanOp.O_true: return "true"
            elif exp == m_booleanOp.O_false: return "false"
            else: return "<Unsupported boolean op %s>" % exp

        elif isinstance(exp, m_aexpCondition):
            return transform(exp.condition)

        elif isinstance(exp, m_conditionCmp):
            if exp.operator == m_booleanOp.O_equal:
                return "EQUAL(%s,%s)" % (transform(exp.exp1, ref=True), transform(exp.exp2, ref=True))
            elif exp.operator == m_booleanOp.O_inequal:
                return "~EQUAL(%s,%s)" % (transform(exp.exp1, ref=True), transform(exp.exp2, ref=True))
            else:
                return "(%s %s %s)" % (transform(exp.exp1), transform(exp.operator), transform(exp.exp2))

        elif isinstance(exp, m_conditionNotComb):
            return "(%s)" % (transform(exp.exp)) if exp.operator is None else "~(%s)" % (transform(exp.exp))

        elif isinstance(exp, m_conditionComb):
            return "(%s %s %s)" % (transform(exp.cond1), transform(exp.operator), transform(exp.cond2))

        elif isinstance(exp, m_predicate):
            q = []
            for x in exp.args:
                x = str(x)
                if x[0] == '"' and x[-1] == '"':
                    x = 'r\\"%s\\"' % x[1:-1]
                q.append(str(x))
            return "%s(%s)" % (exp.name, ", ".join(q))

        elif isinstance(exp, m_aexpModal):
            return "%s(%s)" % (transform(exp.modality), transform(exp.actionExpression))

        elif isinstance(exp, m_modal):
            if exp == m_modal.T_always: return "G"
            elif exp == m_modal.T_must: return "F"
            elif exp == m_modal.T_unless: return "R"
            elif exp == m_modal.T_until: return "U"
            elif exp == m_modal.T_sometime: return "F"
            else: return "<Unsupported boolean op %s>" % exp

        elif isinstance(exp, m_aexpAuthor):
            return "%s%s" % (transform(exp.author), transform(exp.action))

        elif isinstance(exp, m_aexpAction):
            return "%s" % transform(exp.action)

        elif isinstance(exp, m_author):
            return "P" if exp == m_author.A_permit else "~P"

        elif isinstance(exp, m_action):
            return "%s(%s, %s, %s)" % (exp.service, transform(exp.agent1, ref=True),
                                       transform(exp.agent2, ref=True), transform(exp.args, ref=True))

        elif isinstance(exp, m_agent):
            return "'%s'" % exp.name

        elif isinstance(exp, m_varAttr):
            return "%s(%s)" % (exp.attribute, exp.variable)

        elif isinstance(exp, m_variable):
            if ref:
                return "%s" % exp.name
            else:
                return "%s" % exp

        elif isinstance(exp, m_constant):
            return "%s" % exp.name

        elif isinstance(exp, str):
            return exp
        else:
            return "<Unsupported type %s>" % exp.__class__.__name__

    return transform(clause)
