import json
import logging
import os
import re

import zillow

import settings


class Zillow(object):

    def __init__(self):
        self._api = zillow.ValuationApi()

    def load(self, address):
        zillow_results = os.path.join(settings.ZILLOW_DIRECTORY, address + ".json")

        # Load a previously requested maps data to save time and lower number of Google Maps
        # requests, because I only have the free tier.
        if os.path.exists(zillow_results):
            logging.info("Loading property data: %s", address)
            with open(zillow_results, "r") as handler:
                home_results = json.load(handler)

        # Send a request to Google Maps API to retrieve the distance data.
        else:
            match = re.search(r'(?P<address>.*?) (?P<zip>\d{5})$', address, re.DOTALL)
            if match:
                logging.info("Requesting property data: %s", address)
                response = self._api.GetDeepSearchResults(
                    settings.ZILLOW_API_KEY, match.group("address"), match.group("zip"))
                home_results = response.get_dict()

                with open(zillow_results, "w") as handler:
                    json.dump(home_results, handler, indent=4)
            else:
                raise ValueError("Failed to detect address and zip code")

        return home_results
