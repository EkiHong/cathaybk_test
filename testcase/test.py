import os
import conftest
from common.utils import Utils
from environment import Environment
from page.credit_card_intro import CreditCardIntro
from testcase.Setup.cathaybank import TestSetupCathaybank
from page.homepage import HomePage


class TestCathaybank(TestSetupCathaybank):

    def test(self):
        print(f"---------------------- First Step ----------------------")
        HomePage().burger_button().component_ready()
        Utils.screenshots('HomePage')

        print(f"---------------------- Second Step ----------------------")
        HomePage().burger_button().click()
        HomePage().product_category_intro().click()
        HomePage().credit_card_title().click()
        # HomePage().credit_card_items().component_ready()
        items_counts = HomePage().credit_card_items().get_elements()
        count = 0
        for _ in items_counts:
            count += 1
        print(f'Count of credict card item = {count}')
        Utils.screenshots('Credit-card items')

        print(f"---------------------- Third Step ----------------------")
        HomePage().credit_card_intro().click()
        CreditCardIntro().credit_card_intro_title().component_ready()
        Utils.switch_content('WEBVIEW_chrome')
        CreditCardIntro().stopped_card_title().move_to_element()
        #  swipe 一次並截圖，count += 1, 讀取截圖張數，再跟 count 做比對
        stopped_card_list = []
        stopped_card_count = 0
        while True:
            stopped_card = CreditCardIntro().list_of_stopped_card().get_string()
            if stopped_card not in stopped_card_list:
                Utils.screenshots(f'{Environment().env(conftest.env)["CREDIT_CARD_STOPPED_RELEASE_PATH"]}/{stopped_card}')
                stopped_card_list.append(stopped_card)
                Utils.switch_content('NATIVE_APP')
                Utils.swipe_left()
                stopped_card_count += 1
                Utils.switch_content('WEBVIEW_chrome')
            else:
                break
        print(f"stopped_card_count: {stopped_card_count}")

        credit_card_stopped_release_path = Environment().env(conftest.env)['ROOT'] + Environment().env(conftest.env)['SNAPSHOTS_PATH'] + Environment().env(conftest.env)['CREDIT_CARD_STOPPED_RELEASE_PATH']
        count_list = []
        os_list = os.listdir(credit_card_stopped_release_path)
        for file in os_list:
            if file.startswith('.') and os.path.isfile(os.path.join(credit_card_stopped_release_path, file)):
                os_list.remove(file)
            count_list.append(file)
        stopped_card_snapshots_count = len(count_list)
        assert stopped_card_count == stopped_card_snapshots_count




