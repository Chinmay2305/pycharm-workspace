#https://www.udemy.com/course/master-selenium-python-using-seleniumbase/learn/lecture/41586524#questions
#working with multiple elements
from _ast import expr
from os import terminal_size

from behave.textutil import text
from nose import selector
from seleniumbase import BaseCase

#code of lecture 26
class TestContactForm(BaseCase):
    def test_form_submission(self):
        #opening home page
        self.open('https://practice-react.sdetunicorns.com/contact')

        #fill in form fields
        self.type("input[name='name']", "Chinmay Agrawal")
        self.type("input[name='email']", "chinmay230587@gmail.com")
        self.type("input[name='subject']", "Test Subject")
        self.type("textarea[name='message']", "Test message")
        self.click("button[type='submit']")

        #assertions
        self.assert_text("Message sent successfully", 'body > div.react-toast-notifications__container.css-1oqa81j')
        self.assert_element_not_visible('[class*=error]')

    def test_form_submission_without_input(self):
        self.open('https://practice-react.sdetunicorns.com/contact')
        self.click("button[type='submit']")
        #assert the count of error messages
        errors = self.find_elements('[class*=error]')
        self.assert_true(len(errors) == 4)

        #assert the name field error
        self.assert_text("Name is required", 'error-name')
        # assert the email field error - Email is optional hence error should not be visible
        self.assert_false(self.is_text_visible("Email is optional", '.error-email'))
        # subject error should be visible
        self.assert_element_visible('.error-subject')
        #Assert "message" should be present
        error_message = self.get_text('.error-message')
        self.assert_in("Message",error_message)