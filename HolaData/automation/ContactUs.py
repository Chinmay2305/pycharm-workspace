import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://dev.holadata.co.za/")
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/ul/a[4]/li").click()
firstname = "Chinmay"
lastname = "Agrawal"
email = "chinmay230587@gmail.com"
contact = "8238997664"
message = "Test message"
time.sleep(5)

driver.find_element(By.XPATH,"//*[@id='first_name']").send_keys(firstname)
driver.find_element(By.XPATH,"/html/body/div[1]/section[1]/div[2]/div/div/div[2]/form/div[1]/div[2]/input").send_keys(lastname)
driver.find_element(By.XPATH,"/html/body/div[1]/section[1]/div[2]/div/div/div[2]/form/div[2]/input").send_keys(email)
driver.find_element(By.XPATH,"/html/body/div[1]/section[1]/div[2]/div/div/div[2]/form/div[3]/input").send_keys(contact)
driver.find_element(By.XPATH,"/html/body/div[1]/section[1]/div[2]/div/div/div[2]/form/div[4]/textarea").send_keys(message)
driver.find_element(By.XPATH,"/html/body/div[1]/section[1]/div[2]/div/div/div[2]/form/div[5]/button").click()
time.sleep(2)