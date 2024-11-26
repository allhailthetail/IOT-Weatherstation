import sys
import json
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
        

    def _get_weekly(self):
        '''
        Returns a dictionary of 12 hour forecast values for the week (inclusive of today)
        '''
        weekly_forecast_url = self.base_info['properties']['forecast']
        response = requests.get(weekly_forecast_url).json()

        self.weekly_forecast = response['properties']['periods']

    def _get_hourly(self):
            '''
            Returns an hourly forecast.
            '''
            hourly_forecast_url = self.base_info['properties']['forecastHourly']
            response = requests.get(hourly_forecast_url).json()

            self.hourly_forecast = response['properties']['periods']

    def tearse_weekly_to_file(self):
        '''
        Writes tearse weekly forecast to file in reports
        '''

        self.tearse_weekly_forecast = []
        for day in self.weekly_forecast:
            self.tearse_weekly_forecast.append({
                'name': day['name'],
                'temperature': day['temperature'],
                'temperatureUnit': day['temperatureUnit'],
                'windSpeed': day['windSpeed'],
                'detailedForecast': day['detailedForecast']
            })
        
        with open(f'reports/tearse_weekly_forecast.json', 'w') as file:
            file.writelines(json.dumps(self.tearse_weekly_forecast))
        file.close()

    def tearse_hourly_to_file(self):
        '''
        Writes tearse hourly forecast to file in reports
        '''
        self.tearse_hourly_forecast = []
        for day in self.hourly_forecast:
            self.tearse_hourly_forecast.append({
                'startTime': day['startTime'],
                'endTime': day['endTime'],
                'temperature': day['temperature'],
                'temperatureUnit': day['temperatureUnit'],
                'windSpeed': day['windSpeed'],
            })
        
        with open(f'reports/tearse_hourly_forecast.json', 'w') as file:
            file.writelines(json.dumps(self.tearse_hourly_forecast))
        file.close()

    def raw_weekly_to_file(self):
        '''
        Writes weekly forecast to file in reports.
        '''
        if self.weekly_forecast is not None:
            with open(f'reports/weekly_forecast.json', 'w') as file:
                file.writelines(json.dumps(self.weekly_forecast))
            file.close()

    def raw_hourly_to_file(self):
        '''
        Writes hourly forecast to file in reports.
        '''
        if self.hourly_forecast is not None:
            with open(f'reports/hourly_forecast.json', 'w') as file:
                    file.writelines(json.dumps(self.hourly_forecast))
            file.close()