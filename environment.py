import os


class Environment(object):
    common = {
        'ROOT': os.path.join(os.path.abspath(os.path.dirname(__file__))),
        'SNAPSHOTS_PATH': '/Snapshots',
        'CREDIT_CARD_STOPPED_RELEASE_PATH': '/credit_card_stopped_release'
    }

    qa = {
        'URL': 'https://www.cathaybk.com.tw/cathaybk',
        'EXPLICIT_WAIT_TIMEOUT': 30,
    }

    def env(self, env):
        if env == 'common':
            self.common.update(self.common)
            return self.common
        elif env == 'qa':
            self.qa.update(self.common)
            return self.qa
