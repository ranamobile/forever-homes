import os

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
GOOGLE_DIRECTORY = os.path.join(CURRENT_DIRECTORY, "google")
ZILLOW_DIRECTORY = os.path.join(CURRENT_DIRECTORY, "zillow")

GOOGLE_API_KEY = "<insert google api key here>"
ZILLOW_API_KEY = "<insert zillow api key here>"

FOREVER_WORK = "123 Work Ave, Awesomeville, AA 00000"
FOREVER_HOMES = [
    "456 New Home Ave, Superville, AA 00000",
]
