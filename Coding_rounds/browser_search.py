from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def setup():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()

    # Open Google homepage
    driver.get("https://www.google.com")
    driver.maximize_window()

    # Find search bar and enter the search term
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys("Selenium WebDriver")
    search_box.send_keys(Keys.RETURN)  # Simulates pressing Enter

    # Wait for search results to load
    time.sleep(2)

    # Fetch the titles of the first 5 search results
    search_results = driver.find_elements(By.XPATH, "//h3")  # H3 tags are usually used for titles
    count = 0
    for result in search_results:
        print(result.text)
        count += 1
        if count == 5:
            break

    # Close the browser
    driver.quit()


setup()
