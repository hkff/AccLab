from behave import *
# from aalc import aalc
f = open("log", mode="w")
# l = aalc("../tests/healthcare.aal", libs_path="../libs/aal/", root_path="workspace")["mm"]


# TODO checks

@given('a clause {c}')
def step_impl(context, c):
    f.write("CLAUSE " + c + " (\n")

####################
# Actions
####################
@given("allow {agent1} to use {service} service provided by {agent2} on {data}")
def step_impl(context, agent1, service, data, agent2):
    f.write("PERMIT " + agent1 + "." + service + "[" + agent2 + "](" + data + ")")
    assert True

@given("allow {agent1} to {service} {data} on {agent2}")
def step_impl(context, agent1, service, data, agent2):
    f.write("PERMIT " + agent1 + "." + service + "[" + agent2 + "](" + data + ")")
    assert True


@given('we declare a variable {a} with a value {v}')
def step_impl(context, a, v):
    f.write(a + " = " + v + "\n")


@given('we calculate the result of {a} + {b}')
def step_impl(context, a, b):
    f.write("print(" + a + b + ")\n")
    assert True


####################
# Audit
####################
@when('we finish the program')
def step_impl(context):
    assert True is not False


####################
# Rectification
####################
@then('we run it')
def step_impl(context):
    assert True is not False

