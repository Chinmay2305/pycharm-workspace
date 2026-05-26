#https://www.udemy.com/course/master-selenium-python-using-seleniumbase/learn/lecture/41586508?start=75#questions
#working with multiple elements
from _ast import expr
from os import terminal_size

from behave.textutil import text
from seleniumbase import BaseCase

class TestHomePage(BaseCase):
    def test_verify_page_title_and_url(self):
        #opening home page
        self.open('https://practice-react.sdetunicorns.com/')

        #assert URL and title
        self.assert_url_contains('sdetunicorns')
        self.assert_title_contains('SDETUnicorns')  #Should be "SDET Unicorns" actually

    #code of lecture 17
    def test_search_flow(self):
        self.open('https://practice-react.sdetunicorns.com/')

        #click on search input field
        self.click("//button[@class='search-active']")

        #type Lenovo in the search field
        self.type("[placeholder='Search']", text('Lenovo'))
        self.click("//button[@class='button-search']")

        #assert the text is visible
        self.assert_text_visible('Showing Results for Lenovo')

    # code of lecture 18
    def test_links(self):
        self.open("https://practice-react.sdetunicorns.com/")
        self.assert_text('Products','.main-menu li:nth-child(2)')
        expected_nav_text=['Home','Products','About Us','Contact','Upload']

        for i, text in enumerate(expected_nav_text, start=1):
            print(i, text)
            self.assert_text(text,f'.main-menu li:nth-child({i})')