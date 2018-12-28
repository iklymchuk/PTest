from pytest import mark

@mark.smoke
@mark.login
def test_login_work_as_expected():
    assert True

@mark.smoke
@mark.login
@mark.ui
def test_can_navigate_to_the_login_page(chrome_browser):
    chrome_browser.get('https://google.com')
    assert True

@mark.ui
@mark.environment
def test_can_navigate_to_the_env_page(chrome_browser, app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    chrome_browser.get(base_url)
    assert True