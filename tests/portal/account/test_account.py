from pytest import mark

# To prevent the marking all tests within file by the same mark we can mark the class
# and it will apply for all tests inside the class
@mark.account
class AccountTests:
    @mark.smoke
    def test_account_as_user(self, dummy_browser_instance):
        assert "browser" in dummy_browser_instance

    @mark.smoke
    def test_account_as_admin(self, dummy_browser_instance):
        assert "browser" in dummy_browser_instance
