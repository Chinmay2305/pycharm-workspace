import time
from PIL import Image
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.google.com")
print(driver.get_window_size())
print(driver.current_url)
print(driver.title)
driver.save_screenshot("shot1.png")
img = Image.open("shot1.png")
img.show()
img.save("shot2.jpg")
time.sleep(3)