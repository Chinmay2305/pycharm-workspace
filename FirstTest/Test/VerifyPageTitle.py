from selenium import webdriver

def test_page_title():
    driver = webdriver.Chrome()
    driver.get("http://www.google.com")
    assert driver.title == "Google", "Title does not match"
    driver.quit()

test_page_title()