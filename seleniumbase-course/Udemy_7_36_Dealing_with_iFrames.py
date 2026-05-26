#https://www.udemy.com/course/master-selenium-python-using-seleniumbase/learn/lecture/41586524#questions
#working with multiple elements
from _ast import expr
from os import terminal_size

from behave.textutil import text
from nose import selector
from seleniumbase import BaseCase

#code of lecture 36
class DealingWithiFrames(BaseCase):
    def test_iFrames(self):
        #opening home page
        #root DOM
        self.open('https://seleniumbase.io/demo_page')
        self.assert_element_not_visible('h4')

        #switch to iFrame
        self.switch_to_frame("#myFrame2")
        self.assert_element('h4')
        self.assert_text('iFrame Text','h4')

        #switch back to DOM
        self.switch_to_default_content()
        self.assert_element("#progressBar")