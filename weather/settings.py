import os
import sys
import configparser
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Settings:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Access the values from the config file
        self.lat = config.get('coordinates', 'latitude')
        self.long = config.get('coordinates', 'longitude')
        # self.timestamp = config.get('formatting', 'timestamp')