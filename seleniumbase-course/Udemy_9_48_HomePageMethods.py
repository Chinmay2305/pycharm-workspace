from seleniumbase import BaseCase

from pages.Udemy_9_46_HomePage import HomePage

class HomePageMethods(BaseCase):
    def test_verify_title_and_url(self):
        homepage = HomePage(self)
        self.open('https://practice-react.sdetunicorns.com/')

        #assert page title and URL
        self.assert_url_contains('sdetunicorns')
        self.assert_title_contains('SDET Unicorns')

    def test_search_flow(self):
        self.open('https://practice-react.sdetunicorns.com/')
        self.click('.search-active')
        self.type("[placeholder='Search']",'Lenovo')
        self.click('.button-search')
        self.assert_text_visible('Showing Results for Lenovo')

    def test_nav_links(self):
        self.open('https://practice-react.sdetunicorns.com/')
        self.assert_text('Products', '.main-menu li:nth-child(2)')
        expected_nav_text = ['Home','Products','About Us','Contact','Upload']

        for i, text in enumerate(expected_nav_text, start=1):
            self.assert_text(text, f'.main-menu li:nth-child({i})')

    def test_click_about_link_verify_url(self):
        self.open('https://practice-react.sdetunicorns.com/')
        self.click('.footer-list [href="/about"]')
        #assert URL
        self.assert_url_contains('about')

    def test_new_tab(self):
        self.open('https://practice-react.sdetunicorns.com/')
        print(self.driver.window_handles)
        self.click('.copyright p a')
        print(self.driver.window_handles)
        self.switch_to_tab(1)
        self.assert_title_contains('Master Software Testing')
        self.switch_to_default_tab()
        self.assert_title_contains('Practice with React')