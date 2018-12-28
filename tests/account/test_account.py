from pytest import mark

@mark.account
class AcoountTests:

    @mark.smoke
    def test_account_work_as_expected(self):
        assert True

    def test_account_second_check(self):
        assert True

    @mark.ui
    def test_can_navigate_to_the_account_page(self, chrome_browser):
        chrome_browser.get('https://github.com')
        assert True