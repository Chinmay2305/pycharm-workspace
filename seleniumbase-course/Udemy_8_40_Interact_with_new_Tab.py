from seleniumbase import BaseCase

#code of lecture 36
class InteractWithNewTab(BaseCase):
    def test_interact_new_tab(self):
        #opening home page
        #root DOM
        self.open('https://practice-react.sdetunicorns.com/')
        print(self.driver.window_handles)
        self.click('#root > footer > div > div > div:nth-child(1) > div > p > a')
        print(self.driver.window_handles)
        self.switch_to_tab(1)
        self.assert_title_contains('Master Software Testing and Automation')
        self.switch_to_default_tab()
        self.assert_title_contains('Practice with React')