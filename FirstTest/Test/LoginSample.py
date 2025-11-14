import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()

try:
    driver.get('http://the-internet.herokuapp.com/login')
    user = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/form/div[1]/div/input')
    password = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/form/div[2]/div/input')
    button = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/form/button')

    user.send_keys('tomsmith')
    password.send_keys('SuperSecretPassword!')
    button.click()

    WebDriverWait(driver,10).until(ec.presence_of_element_located((By.CLASS_NAME,'flash success')))
    success_message = driver.find_element(By.CLASS_NAME,'flash success').text
    print(success_message)
except Exception as e:
    print("Error: ",e)
finally:
    time.sleep(2)
    driver.quit()