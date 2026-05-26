import pytest

from test.BaseTest import BaseTest
from properties.config import Config

class TestForgotPassword(BaseTest):
    @pytest.mark.forgotpassword
    def test_forgot_password(self):
        self.open(Config.forgot_password_url)
        self.send_keys(Config.forgot_password_field,Config.user)
        self.click(Config.forgot_password_btn)