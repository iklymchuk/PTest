from pytest import fixture
from selenium import webdriver
from config import Config

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="Environment to run tests"
    )

@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome('./chromedriver')
    return browser

@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")

@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg