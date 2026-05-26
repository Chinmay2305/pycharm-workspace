#https://www.udemy.com/course/master-selenium-python-using-seleniumbase/learn/lecture/41586524#questions
#working with multiple elements
from _ast import expr
from os import terminal_size

from behave.textutil import text
from nose import selector
from seleniumbase import BaseCase

#code of lecture 33
class WorkingWithInputSlider(BaseCase):
    def test_input_slider_control(self):
        #opening home page
        self.open('https://seleniumbase.io/demo_page')

        #intial stage
        self.assert_attribute('#progressBar','value','50')

        #change slider value
        self.set_value('#mySlider','80')

        #after stage
        self.assert_attribute('#progressBar', 'value', '0')

        self.sleep(3)