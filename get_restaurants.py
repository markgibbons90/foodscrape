import googlemaps
import ConfigParser
from datetime import datetime

class RestaurantGetter(object):
    """
    Class with methods for getting a list of restaurants based on entered criteria
    """

    def __init__(self):
        # Set the API key
        self.api_key = self.get_api_key()
        # Set the gmaps object
        self.gmaps = googlemaps.Client(key=self.api_key)

    def get_api_key():
        """
        Fetch the api key from settings.ini
        """
        config = ConfigParser.ConfigParser()
        config.read('settings.ini')
        return config.get('Google API', 'google_api_key')

    def get_by_coords(self, lat, lng, radius):
        """
        Fetch a list of restaurants based on coordinates, within a given distance
        """
        self.gmaps.places((lat, lng), radius=radius, type='restaurant')
