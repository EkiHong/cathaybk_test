from selenium.webdriver.common.by import By
from common.basic_button import BasicButton
from common.device_manager import DeviceManager


class CreditCardIntro(object):

    def __init__(self):
        self.label = 'Credit Card Intro'
        self.browser = DeviceManager.get_driver()

    def credit_card_intro_title(self):
        return BasicButton(
            f"{self.label} -> credit card intro button",
            (By.XPATH, '//android.view.View[@text="信用卡介紹"]')
        )

    def stopped_card_title(self):
        return BasicButton(
            f"{self.label} -> stopped_card_title",
            (By.XPATH, '//div[text()="停發卡"]')
        )

    def list_of_stopped_card(self):
        return BasicButton(
            f"{self.label} -> list of stopped card",
            (By.XPATH, f'//div[@class="cubre-a-iconTitle__text" and text()="停發卡"]/ancestor::div[@class="cubre-o-block__wrap"]/div[@class="cubre-o-block__component"]//div[@class="cubre-o-slide__item swiper-slide swiper-slide-active"]//div[@class="cubre-m-compareCard__title"]')
        )
