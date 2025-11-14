from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
text = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/a")
assert text.is_displayed(), "Elemental Selenium is present"