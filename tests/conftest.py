from pytest import fixture

# Fixture scope: function, module, session
@fixture(scope='function')
def dummy_browser_instance():
    print("Here is a browser fixture")
    return "browser is here"