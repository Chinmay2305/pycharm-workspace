import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.python.org")

# Get current title
first_url = driver.current_url
print(first_url)

time.sleep(5)
# doing a search and get current url then
search_bar = driver.find_element(By.NAME,"q")
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
second_url = driver.current_url
print(second_url)

driver.close()