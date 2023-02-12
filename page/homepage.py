from selenium.webdriver.common.by import By
from common.basic_button import BasicButton
from common.device_manager import DeviceManager


class HomePage(object):

    def __init__(self):
        self.label = 'Home Page'
        self.browser = DeviceManager.get_driver()

    def burger_button(self):
        return BasicButton(
            f"{self.label} -> burger button",
            (By.XPATH, '//android.view.View[@content-desc=" "]')
        )

    def product_category_intro(self):
        return BasicButton(
            f"{self.label} -> product category intro button",
            (By.XPATH, '//android.widget.TextView[@text="產品介紹"]')
        )

    def credit_card_title(self):
        return BasicButton(
            f"{self.label} -> product category intro button",
            (By.XPATH, '//android.widget.TextView[@text="信用卡"]')
        )

    def credit_card_items(self):
        return BasicButton(
            f"{self.label} -> credit-card items",
            (By.XPATH, '//android.view.View[@resource-id="lnk_Link"]/android.widget.TextView')
        )

    def credit_card_intro(self):
        return BasicButton(
            f"{self.label} -> credit card intro button",
            (By.XPATH, '//android.widget.TextView[@text="卡片介紹"]')
        )
