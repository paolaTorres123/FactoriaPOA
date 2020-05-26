from behave import fixture, use_fixture
from selenium.webdriver import Firefox
from unittest import TestCase
import time

@fixture
def browser_firefox(context):
    # -- BEHAVE-FIXTURE: Similar to @contextlib.contextmanager
    context.driver = Firefox() #Esto lo hace en before
    #Aquí se podría poner el Login, si para todas las pruebas se necesita estar logeado
    context.url = 'http://192.168.33.10:8000/'
    #login(context)
    context.test = TestCase()
    yield context.driver # A partir de aquí, lo hace después de todo
    # -- CLEANUP-FIXTURE PART:
    #context.driver.quit()

def before_all(context):
    use_fixture(browser_firefox, context)
    # -- NOTE: CLEANUP-FIXTURE is called after after_all() hook

def login(context):
    context.driver.get(context.url+'usuarios/login')
    time.sleep(1)
    context.driver.find_element_by_id('id_username').send_keys('directorOperativo')
    context.driver.find_element_by_id('id_password').send_keys('F@@ctoria12')
    context.driver.find_element_by_id('btnLogin').click()