from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Function to check if a URL is broken
def is_broken_link(url):
    try:
        response = requests.head(url, allow_redirects=True)
        return response.status_code != 200
    except requests.exceptions.RequestException:
        return True

try:
    # Open the target website
    driver.get("https://www.example.com")

    # Optional: Wait for some time to ensure the page is fully loaded
    time.sleep(2)

    # Find all links on the page
    links = driver.find_elements(By.TAG_NAME, "a")

    # Store broken links
    broken_links = []

    for link in links:
        href = link.get_attribute("href")
        if href:  # Ensure the link is not None
            if is_broken_link(href):
                print(f"Broken link found: {href}")
                broken_links.append(href)

    print(f"Total broken links: {len(broken_links)}")

finally:
    # Close the browser
    driver.quit()