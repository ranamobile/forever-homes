import json
import logging
import os

import googlemaps

import settings


class Google(object):

    def __init__(self):
        self._api = googlemaps.Client(key=settings.GOOGLE_API_KEY)

    def load(self, address):
        google_results = os.path.join(settings.GOOGLE_DIRECTORY, address + ".json")

        # Load a previously requested maps data to save time and lower number of Google Maps
        # requests, because I only have the free tier.
        if os.path.exists(google_results):
            logging.info("Loading distance data: %s", address)
            with open(google_results, "r") as handler:
                home_results = json.load(handler)

        # Send a request to Google Maps API to retrieve the distance data.
        else:
            logging.info("Connecting to the Google Maps API")

            logging.info("Requesting distance data: %s", address)
            home_results = self._api.directions(address, settings.FOREVER_WORK)
            with open(google_results, "w") as handler:
                json.dump(home_results, handler, indent=4)

        return home_results
