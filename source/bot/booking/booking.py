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

    def land_first_page(self, link):
        self._driver.get(link)

    def is_closed_popup(self, element='//button[@aria-label="Close"]'):
        try:

            close_button = self._driver.find_element(By.XPATH, element)
            close_button.click()
            return True
        except NoSuchElementException:
            self._driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)

    def select_currency(self, currency: str) -> ChangeCurrencyResponse:
        try:
            self.is_closed_popup()
            btn = self._driver.find_element(
                By.CSS_SELECTOR,
                'button[data-testid="header-currency-picker-trigger"]'
            )
            btn.click()

            self._driver.implicitly_wait(15)

            current_currency = self._driver.find_element(
                By.XPATH,
                f'//span/div[contains(text(), "{currency}")]/ancestor::button'
            )

            current_currency.click()
            return ChangeCurrencyResponse(status=True, message=f"Changed currency to {currency}")
        except Exception as e:
            raise BookingBotError(f"Currency changing event failed. Original error {str(e)}") from e

    def select_location(self, location):
        self.is_closed_popup()

        form = self._driver.find_element(By.NAME, "ss")

        form.clear()
        form.send_keys(location)
        res = self._driver.find_element(By.ID,
                                        'autocomplete-result-0')
        res.click()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._driver.quit()


def get_booking(driver) -> Booking:
    return Booking(driver)
