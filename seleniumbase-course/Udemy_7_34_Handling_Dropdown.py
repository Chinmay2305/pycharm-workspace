#https://www.udemy.com/course/master-selenium-python-using-seleniumbase/learn/lecture/41586524#questions
#working with multiple elements
from _ast import expr
from os import terminal_size

from behave.textutil import text
from nose import selector
from seleniumbase import BaseCase

#code of lecture 34
class HandlingDropDown(BaseCase):
    def test_drop_down(self):
        #opening home page
        self.open('https://seleniumbase.io/demo_page')

        #intial stage / #first, assert the before state
        self.assert_element('meter[value="0.25"]')

        # change the slider value by Index
        self.select_option_by_index("#mySelect","2")
        self.assert_element('meter[value="0.75"]')
        self.sleep(3)

        # change the slider value by Text
        self.select_option_by_text("#mySelect", "Set to 100%")
        self.assert_element('meter[value="1"]')
        self.sleep(3)

        # change the slider value by Value
        self.select_option_by_value("#mySelect", "50%")
        self.assert_element('meter[value="0.5"]')
        self.sleep(3)