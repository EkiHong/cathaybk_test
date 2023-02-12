from appium import webdriver


class DeviceManager(object):

    @staticmethod
    def set_driver(driver):
        global __driver
        __driver = driver

    @staticmethod
    def get_driver():
        global __driver
        return __driver

    @staticmethod
    def get_device():
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10.0'
        desired_caps['deviceName'] = 'Pixel_4a'
        desired_caps['udid'] = 'emulator-5554'
        desired_caps['newCommandTimeout'] = 1000
        desired_caps['appPackage'] = 'com.android.chrome'
        desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'
        desired_caps['noReset'] = True
        return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
