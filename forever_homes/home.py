import json
import logging
import os

import googlemaps

import settings


class Home(object):

    def __init__(self, address):
        self._address = address
        self._googlemaps = Home.load_maps(address)

    @staticmethod
    def load_maps(address):
        map_results = os.path.join(settings.GOOGLE_DIRECTORY, address + ".json")

        # Load a previously requested maps data to save time and lower number of Google Maps
        # requests, because I only have the free tier.
        if map_results:
            logging.info("Loading distance data: %s", address)
            with open(map_results, "r") as handler:
                home_results = json.load(handler)

        # Send a request to Google Maps API to retrieve the distance data.
        else:
            logging.info("Connecting to the Google Maps API")
            gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)

            logging.info("Requesting distance data: %s", address)
            home_results = gmaps.directions(address, settings.FOREVER_WORK)
            with open(map_results, "w") as handler:
                json.dump(home_results, handler, indent=4)

        return home_results

    @property
    def address(self):
        return self._address

    @property
    def distance(self):
        return self._googlemaps[0]["legs"][0]["distance"]["text"]

    @property
    def duration(self):
        return self._googlemaps[0]["legs"][0]["duration"]["text"]
