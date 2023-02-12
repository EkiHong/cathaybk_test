import conftest
from common.device_manager import DeviceManager
from environment import Environment


class TestSetupCathaybank(object):

    def setup_class(self):
        print("------ setup before class Test ------")

    def setup_method(self):
        print("------ setup before method Test ------")
        DeviceManager.set_driver(DeviceManager.get_device())
        DeviceManager.get_driver().get(Environment().env(conftest.env)['URL'])

    def teardown_method(self):
        print("------ teardown after method Test ------")
        DeviceManager.get_driver().quit()

    def teardown_class(self):
        print("------ teardown after class Test ------")