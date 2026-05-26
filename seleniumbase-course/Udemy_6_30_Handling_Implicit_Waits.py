#https://www.udemy.com/course/master-selenium-python-using-seleniumbase/learn/lecture/41586524#questions
#working with multiple elements
from _ast import expr
from os import terminal_size

from behave.textutil import text
from nose import selector
from seleniumbase import BaseCase

#code of lecture 30
class TestProductPage(BaseCase):
    def test_add_to_cart(self):
        #opening home page
        self.open('https://practice-react.sdetunicorns.com/product/63448f0500b2931578c0a5a7')
        self.driver.implicitly_wait(5)
        self.click('.pro-details-carts')
        self.assert_text("Added to Cart", ".react-toast-notifications__toast__content")