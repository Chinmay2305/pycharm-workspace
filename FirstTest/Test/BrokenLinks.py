from seleniumbase import BaseCase
import requests

class BrokenLinksTest(BaseCase):
    def test_find_broken_links(self):
        # Replace with the URL you want to test
        url = "http://www.thefreelibrary.com"
        self.open(url)

        # Find all links on the page
        links = self.find_elements("a")

        broken_links = []

        for link in links:
            href = link.get_attribute("href")
            if href:
                # Check the link's status
                response = requests.head(href, allow_redirects=True)
                if response.status_code != 200:
                    broken_links.append((href, response.status_code))

        # Output broken links
        if broken_links:
            print("Broken Links:")
            for href, status in broken_links:
                print(f"{href} - Status Code: {status}")
        else:
            print("No broken links found.")

# Run the test
if __name__ == "__main__":
    import unittest
    unittest.main()