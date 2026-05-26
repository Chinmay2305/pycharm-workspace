#https://www.udemy.com/course/master-selenium-python-using-seleniumbase/learn/lecture/41586524#questions
#working with multiple elements
from _ast import expr
from os import terminal_size

from behave.textutil import text
from nose import selector
from seleniumbase import BaseCase

#code of lecture 35
class ChecktheCheckbox(BaseCase):
    def test_check_checkbox(self):
        #opening home page
        self.open('https://seleniumbase.io/demo_page')

        #assert image logo is not visible
        self.assert_element_not_visible('img#logo')

        #assert checkbox is not selected
        self.assert_false(self.is_selected('#checkBox1'))

        #click on the checkbox
        self.click("#checkBox1")

        #assert checkbox is selected
        self.assert_true(self.is_selected("#checkBox1"))

        # assert image logo is now visible
        self.assert_element_visible('img#logo')

        self.sleep(4)