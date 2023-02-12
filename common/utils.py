import time
import conftest
from common.device_manager import DeviceManager
from environment import Environment


class Utils(object):

    @staticmethod
    def debug_log(log) -> None:
        print("{} Debug_log: {}".format(time.strftime("%Y-%m-%d %H:%M:%S"), log))

    @staticmethod
    def screenshots(name):
        path = Environment().env(conftest.env)['ROOT'] + Environment().env(conftest.env)['SNAPSHOTS_PATH']
        DeviceManager.get_driver().get_screenshot_as_file(path + f"/{name}.png")

    @staticmethod
    def switch_content(content):
        DeviceManager.get_driver().switch_to.context(content)

    @staticmethod
    def swipe_left(t=500, num=1):
        driver = DeviceManager.get_driver()
        size = driver.get_window_size()
        x1 = size['width'] * 0.9
        x2 = size['width'] * 0.1
        y1 = size['height'] * 0.5
        for i in range(num):
            driver.swipe(x1, y1, x2, y1, t)
