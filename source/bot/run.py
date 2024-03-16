from source.dependency.driver import get_container
from source.bot.booking.booking import get_booking

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
        bot.land_first_page(config.base_url)
        res = bot.select_currency("USD")
        logger.info(f"{res.status, res.message}")
        bot.is_closed_popup()
        print('about to')
        bot.select_location('Minsk')
        inp = input()
        bot.is_closed_popup()
        print('selected')

