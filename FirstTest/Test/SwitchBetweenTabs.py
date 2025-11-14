import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.python.org")

# Open a different URL in new tab
driver.execute_script("window.open('https://www.google.com', '_blank');")
time.sleep(2)

windows_handles = driver.window_handles

driver.switch_to.window(windows_handles[1])
time.sleep(2)
print(driver.title)

driver.switch_to.window(windows_handles[0])
time.sleep(2)
print(driver.title)