#https://www.udemy.com/course/master-selenium-python-using-seleniumbase/learn/lecture/41586524#questions
#working with multiple elements
from _ast import expr
from os import terminal_size

from behave.textutil import text
from nose import selector
from seleniumbase import BaseCase

#code of lecture 36
class CheckboxiniFrames(BaseCase):
    def test_checkbox_in_iFrames(self):
        #opening home page
        #root DOM
        self.open('https://seleniumbase.io/demo_page')
        # assert checkbox is not visible
        self.assert_false(self.is_element_visible('#checkBox6'))

        # move into the iFrame to access the checkbox
        self.switch_to_frame('#myFrame3')

        # select the checkbox and verify it
        self.assert_element('#checkBox6')
        self.assert_false(self.is_selected(('#checkBox6')))

        self.click('#checkBox6')
        self.assert_true(self.is_selected('#checkBox6'))

        self.switch_to_default_content()
        self.assert_element('#progressBar')