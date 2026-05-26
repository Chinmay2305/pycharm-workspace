import pytest
from test.test_forgotpassword import TestForgotPassword
from test.test_login import TestLogin
from components.add_role import TestAddRole

class Main(TestLogin, TestAddRole):
#    @pytest.mark.run_all
    def test_run_all(self):
        self.maximize_window()
        self.test_user_login()
        self.sleep(10)
        self.test_add_role()