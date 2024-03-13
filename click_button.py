
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

from driver import get_container

if __name__ == "__main__":

    driver = get_container().driver
    driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")
    driver.implicitly_wait(2)
    element = driver.find_element(by=By.ID, value='downloadButton')
    element.click()

    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "progress-label"),
            'Complete!'
        )
    )
