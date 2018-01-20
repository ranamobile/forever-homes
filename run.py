import json
import logging
import os

import googlemaps

import settings


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    # Connect to the Google Maps API.
    gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)

    # Iterate through each home to find the Google Maps Distance.
    for home in settings.FOREVER_HOMES:
        home_gmap_file = os.path.join("googlemaps", home + ".json")

        # Load a previously requested maps data to save time and lower number of Google Maps
        # requests, because I only have the free tier.
        if os.path.exists(home_gmap_file):
            logging.info("Loading distance data: %s", home)
            with open(home_gmap_file, "r") as handler:
                home_results = json.load(handler)

        # Send a request to Google Maps API to retrieve the distance data.
        else:
            logging.info("Requesting distance data: %s", home)
            home_results = gmaps.directions(home, settings.FOREVER_WORK)
            with open(home_gmap_file, "w") as handler:
                json.dump(home_results, handler, indent=4)

        # Parse the distance and duration from home to work.
        home_distance = home_results[0]["legs"][0]["distance"]["text"]
        home_duration = home_results[0]["legs"][0]["duration"]["text"]
        logging.info("Distance: %s    Duration: %s", home_distance, home_duration)
        logging.info("")
