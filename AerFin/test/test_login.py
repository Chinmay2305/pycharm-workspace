import pytest
from test.BaseTest import BaseTest
from properties.config import Config

class TestLogin(BaseTest):
#    @pytest.mark.login
    def test_user_login(self):
        self.open_login_page()
        self.perform_login()
        assert self.is_element_visible(Config.profile_img)
