import conftest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from environment import Environment
from common.device_manager import DeviceManager


class BasicAction(object):

    def __init__(self, label, locator):
        self.browser = DeviceManager.get_driver()
        self.label = label
        self.locator = locator

    def component_ready(self):
        try:
            WebDriverWait(self.browser, Environment().env(conftest.env)['EXPLICIT_WAIT_TIMEOUT']).until(EC.visibility_of_element_located(self.locator))
            return None
        except:
            raise Exception(f"{self.label()} > should exist")

    def set_explicit_wait_timeout(self, timeout: int):
        return WebDriverWait(self.browser, timeout)

    def until_locator_visible(self):
        return self.set_explicit_wait_timeout(Environment().env(conftest.env)['EXPLICIT_WAIT_TIMEOUT']).until(EC.visibility_of_element_located(self.locator))

    def until_locators_visible(self):
        return self.set_explicit_wait_timeout(Environment().env(conftest.env)['EXPLICIT_WAIT_TIMEOUT']).until(EC.visibility_of_all_elements_located(self.locator))


