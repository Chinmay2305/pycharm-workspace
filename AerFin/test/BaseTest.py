from seleniumbase import BaseCase
from properties.config import Config

class BaseTest(BaseCase):
    def open_login_page(self):
        self.open(Config.url)

    def perform_login(self):
        self.send_keys(Config.login_user_field, Config.user)
        self.send_keys(Config.login_pwd_field, Config.pwd)
        self.click(Config.login_btn)

    def forgot_password(self):
        self.send_keys(Config.forgot_password_field,Config.user)
        self.click(Config.forgot_password_btn)