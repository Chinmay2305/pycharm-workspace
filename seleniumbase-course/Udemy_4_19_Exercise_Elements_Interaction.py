#https://www.udemy.com/course/master-selenium-python-using-seleniumbase/learn/lecture/41586524#questions
#working with multiple elements
from _ast import expr
from os import terminal_size

from behave.textutil import text
from nose import selector
from seleniumbase import BaseCase

#code of lecture 19
class TestHomePage(BaseCase):
    def test_verify_page_url(self):
        #opening home page
        self.open('https://practice-react.sdetunicorns.com/')
        self.click("#root > header > div.header-padding-1.sticky-bar.header-res-padding.clearfix > div.container-fluid > div > div.col-xl-8.col-lg-8.d-none.d-lg-block > div > nav > ul > li:nth-child(3) > a")
        self.assert_url_contains("about")

    def test_text_categories_Productspage(self):
        self.open('https://practice-react.sdetunicorns.com/')
        #Expected li texts
        expected_text = ["All Categories","Laptop","Electronics","Keyboard"]

        self.click("#root > header > div.header-padding-1.sticky-bar.header-res-padding.clearfix > div.container-fluid > div > div.col-xl-8.col-lg-8.d-none.d-lg-block > div > nav > ul > li:nth-child(3) > a")
        for i, text in enumerate(expected_text, start=1):
            self.assert_text(text, f'.sidebar-widget-list mt-30 li:nth-child({i})')