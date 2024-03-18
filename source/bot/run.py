from source.dependency.driver import get_container
from source.bot.booking.kufar import get_booking

from config import get_config

import logging
import time
if __name__ == "__main__":

    logger = logging.getLogger('bot')
    logger.setLevel("INFO")
    handler = logging.StreamHandler()  # Console handler
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    driver = get_container().driver
    config = get_config()
    booking_service = get_booking(driver)
    with booking_service as bot:
        parent_window = bot.land_first_page(config.base_url)
        print(parent_window)
        bot.is_closed_popup()
        bot.find('Гитары')

        bot.click_search()
        time.sleep(1)

        prices = bot.find_prices()

        for price in prices:
            print(price.text)

        time.sleep(1000)



