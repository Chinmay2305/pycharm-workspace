#https://www.udemy.com/course/master-selenium-python-using-seleniumbase/learn/lecture/41586488#notes
#verifying web title and URL
from seleniumbase import BaseCase

class TestHomePage(BaseCase):
    def test_verify_page_title_and_url(self):
        #opening home page
        self.open('https://practice-react.sdetunicorns.com/')

        #assert URL and title
        self.assert_url_contains('sdetunicorns')
        self.assert_title_contains('SDETUnicorns')  #Should be "SDET Unicorns" actually
