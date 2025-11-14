from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/button").click()

element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "finish")))
print(element.text)
driver.quit()