import pytest

env = None
lang = None


def pytest_addoption(parser):
    parser.addoption(
        '--ENV',
        dest='ENV',
        help='which ENV',
        default='qa'
    )

@pytest.fixture(autouse=True, scope='class')
def env_config(request):
    global env
    env = request.config.getoption('ENV')

