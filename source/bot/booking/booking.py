from selenium.webdriver import Chrome


class Booking:
    def __init__(self, driver: Chrome):
        self._driver = driver

    def land_first_page(self, link):
        self._driver.get(link)


def get_booking(driver):
    return Booking(driver)
