from behave import *

from lab_python_fp.bisqur import BiSqUr


@given("exemple of class BiSqUr with in: 1 -5 4")
def prepair(context):
    global ur
    ur = BiSqUr(1, -5, 4)


@then('function get_disc called with output is 9')
def get_disc_out_correct(context):
    assert ur.get_disc() == 9

@then('function get_base_solve called with output is 9')
def get_disc_out_correct(context):
    assert sorted(ur.get_base_solve()) == [1, 4]

@then('function get_solve called with output is 9')
def get_disc_out_correct(context):
    assert sorted(ur.get_solve()) == [-2.0, -1.0, 1.0, 2.0]