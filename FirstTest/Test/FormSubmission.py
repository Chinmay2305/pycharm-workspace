from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.w3schools.com/html/html_forms.asp")
driver.implicitly_wait(10)
driver.find_element(By.ID, "fname").send_keys("Chinmay")
driver.find_element(By.ID, "lname").send_keys("Agrawal")
driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div[1]/div[3]/div/form/input[3]").click()