import sys
import requests

class Forecast:
    '''A class to represent a basic forecast'''

    def __init__(self, lat, lon):
        '''Initialize basic geo info about the forecast'''
        self.lat = lat
        self.lon = lon
        self.weekly_forecast = []
        self.hourly_forecast = []

        try:
            self.base_info = requests.get(f'https://api.weather.gov/points/{lat},{lon}').json()
        except Exception as err:
            print('\nAn error occured:\n\n', err)
            sys.exit()
        
    def get_hourly(self):
        '''
        Returns an hourly forecast... 
        '''
        hourly_forecast_url = self.base_info['properties']['forecastHourly']
        response = requests.get(hourly_forecast_url).json()

        self.hourly_forecast = response['properties']['periods']
    
    def get_weekly(self):
        '''
        Returns a dictionary of 12 hour forecast values for the week (inclusive of today)
        '''
        weekly_forecast_url = self.base_info['properties']['forecast']
        response = requests.get(weekly_forecast_url).json()

        self.weekly_forecast = response['properties']['periods']