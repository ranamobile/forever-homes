import logging

import settings
from forever_homes.utils import GOOGLE
from forever_homes.utils import ZILLOW


class Home(object):

    def __init__(self, address):
        self._address = address
        self._google = GOOGLE.load(address)
        self._zillow = ZILLOW.load(address)

    @property
    def address(self):
        return self._address

    @property
    def distance(self):
        return self._google[0]["legs"][0]["distance"]["text"]

    @property
    def duration(self):
        return self._google[0]["legs"][0]["duration"]["text"]

    @property
    def bedrooms(self):
        return self._zillow["extended_data"]["bedrooms"]

    @property
    def bathrooms(self):
        return self._zillow["extended_data"]["bathrooms"]

    @property
    def lot_size(self):
        return float(self._zillow["extended_data"]["lot_size_sqft"]) / 43560
