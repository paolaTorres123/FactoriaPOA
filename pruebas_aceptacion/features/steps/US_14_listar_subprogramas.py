from behave import given, when, then
from environment import login


@given(u'que quiero consultar los subprogramas')
def step_impl(context):
    login(context)
    context.urlSubprogramas = context.urlBase + "subprograma/"


@when(u'ingreso al sitio')
def step_impl(context):
    context.driver.get(context.urlSubprogramas)


@then(u'puedo ver todos los subprogramas que hay.')
def step_impl(context):
    context.test.assertIsNotNone(
        context.driver.find_element_by_tag_name("thead")
    )
