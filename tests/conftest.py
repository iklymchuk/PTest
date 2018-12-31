import json
from pytest import fixture
from selenium import webdriver
from config import Config

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="Environment to run tests"
    )

# for single browser initialisation
@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome()
    return browser

@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")

@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg

# browser paramerization
@fixture(params=[
    webdriver.Chrome,
    webdriver.Firefox
])
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()

# load json test data for parametrization
def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data

data_path = './data/test_data.json'

# parametrize test use json data
@fixture(params=load_test_data(data_path))
def external_test_data(request):
    data = request.param
    return data