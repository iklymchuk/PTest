from pytest import mark

@mark.skip(reason="broken by Issue IS-4244")
@mark.environment
def test_environment_is_qa(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://qa-env.com'
    assert port == 80

@mark.xfail(reason="blocken by Issue IS-4243")
@mark.environment
def test_qa_expect_failure(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://qa-env.com'

@mark.environment
def test_environment_is_dev(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://dev-env.com'
    assert port == 8080