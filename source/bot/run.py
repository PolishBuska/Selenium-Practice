from source.dependency.driver import get_container
from source.bot.booking.booking import get_booking

from config import get_config


if __name__ == "__main__":
    driver = get_container().driver
    with driver as driver:
        config = get_config()
        booking_service = get_booking(driver)
        booking_service.land_first_page(config.base_url)

