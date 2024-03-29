from pytest import mark

@mark.test_qa_config
def test_env_is_qa(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://qa-env.com'
    assert port == 80

@mark.test_dev_config
def test_env_is_dev(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://dev-env.com'
    assert port == 8080