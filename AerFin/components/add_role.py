import pytest
from test.BaseTest import BaseTest
from properties.config import Config

class TestAddRole(BaseTest):
#    @pytest.mark.add_role
    def test_add_role(self):
        self.click(Config.settings)
        self.click(Config.settings_role)
        self.sleep(5)