import string

from driver import get_container

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

import time
import random

if __name__ == "__main__":

    container = get_container()
    driver = container.driver
    driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
    driver.implicitly_wait(5)
    sum_1 = driver.find_element(By.ID, value='value1')
    sum_2 = driver.find_element(By.ID, value='value2')
    sum_1.send_keys(2)
    sum_2.send_keys(2)
    total = driver.find_element(By.CSS_SELECTOR, value="button[onclick='return total()']")
    total.click()
    res = driver.find_element(By.ID, value='displayvalue')
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element(
            (By.ID, "displayvalue"),
            '4'
        )
    )
    rand = ""
    single_field = driver.find_element(By.ID, value='user-message')
    single_field.send_keys(rand.join(random.choice(string.ascii_lowercase) for _ in range(100)))

    single_field_button = driver.find_element(By.CSS_SELECTOR, value="button[onclick='showInput();']")
    single_field_button.click()

    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element(
            (By.ID, 'display'),
            "My message"
        )
    )
    time.sleep(10)
