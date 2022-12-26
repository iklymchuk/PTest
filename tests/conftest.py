from pytest import fixture
from config import Config

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="Environment to run tests against"
    )

# Dummy custom fixture
# Fixture scope: function, module, session
@fixture(scope="function")
def dummy_browser_instance():
    print("Here is a browser fixture")
    return "browser is here"

# Fixture for usage of '--env' option
@fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@fixture(scope="session")
def app_config(env):
    cfg = Config(env)
    return cfg
