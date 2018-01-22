import logging

import settings
from forever_homes.home import Home


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    # Iterate through each home to find the Google Maps Distance.
    for address in settings.FOREVER_HOMES:
        home = Home(address)
        logging.info("Address: %s", home.address)
        logging.info("Distance: %s", home.distance)
        logging.info("Duration: %s", home.duration)
        logging.info("Bedrooms: %s", home.bedrooms)
        logging.info("Bathrooms: %s", home.bathrooms)
        logging.info("Lot Size: %.2f acres", home.lot_size)
        logging.info("")
