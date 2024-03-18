import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from source.bot.dto import ChangeCurrencyResponse
from source.bot.exceptions import BookingBotError


class Booking:
    def __init__(self, driver: Chrome):
        self._driver = driver
        self._driver.implicitly_wait(1)
        self._driver.maximize_window()
        self._windows = self._driver.window_handles

    @property
    def windows(self):
        return self._windows

    def land_first_page(self, link):
        self._driver.get(link)
        return self._driver.current_window_handle


    def is_closed_popup(self):
        try:
            btn = WebDriverWait(self._driver, 100).until(EC.element_to_be_clickable(
                (By.XPATH, f"//button[contains(text(), 'Принять')]")
            ))
            btn.click()
            return True
        except NoSuchElementException:
            self._driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ENTER)

    def find(self, item):
        form = self._driver.find_element(
            By.CSS_SELECTOR,
            value='input[data-cy="searchbar-input"]'
        )
        form.send_keys(item)
        form.send_keys(Keys.ENTER)

    def click_search(self):
        # Store the original window handle
        self.original_window = self._driver.current_window_handle

        # Click the search button
        btn = WebDriverWait(self._driver, 4).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[data-cy="searchbar-search-button"]')
        ))
        btn.click()

    def find_prices(self):
        # Now the driver is focused on the new tab
        self._driver.implicitly_wait(4)
        items = self._driver.find_elements(By.CSS_SELECTOR, value='div[data-name="listings"]')
        return items

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._driver.quit()


def get_booking(driver) -> Booking:
    return Booking(driver)
