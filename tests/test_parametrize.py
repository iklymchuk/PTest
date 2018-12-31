from pytest import mark

@mark.tv
@mark.parametrize('tv_brand',
    [
        ("LG"),
        ("Samsung"),
        ("Sony")
    ]
)
def test_television_turns_on(tv_brand):
    print(f"{tv_brand} turns on as expected")

@mark.e2e
def test_browser_can_open_the_page(browser):
    browser.get('http://google.com')

@mark.external_data
def test_json_params(external_test_data):
    print(f"{external_test_data} was selected")