#https://www.udemy.com/course/master-selenium-python-using-seleniumbase/learn/lecture/41586524#questions
#working with multiple elements
from seleniumbase import BaseCase

#code of lecture 36
class HoverOverElement(BaseCase):
    def test_hover_over_element(self):
        #opening home page
        #root DOM
        self.open('https://seleniumbase.io/demo_page')
        #self.hover('#myDropdown')
        #self.click('#dropOption2')

        self.hover('#myDropdown')
        self.click('#dropOption3')
        self.assert_text('Link Three Selected','h3')
        self.sleep(3)

        self.hover_and_click('#myDropdown','#dropOption2')
        self.assert_text('Link Two Selected', 'h3')
        self.sleep(3)