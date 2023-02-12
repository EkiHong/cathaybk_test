from common.basic_action import BasicAction
from common.utils import Utils


class BasicButton(BasicAction):

    def __init__(self, label, locator):
        super().__init__(label, locator)
        self.label = label
        self.locator = locator

    def click(self):
        Utils.debug_log(f"{self.label} > click '{self.locator}'")
        self.until_locator_visible().click()

    def get_elements(self):
        return self.until_locators_visible()

    def get_string(self):
        Utils.debug_log(f"{self.label} > get string > {self.locator}")
        return self.until_locator_visible().text

    def move_to_element(self):
        Utils.debug_log(f"{self.label} > move to element > {self.locator}")
        return self.until_locator_visible().location_once_scrolled_into_view
