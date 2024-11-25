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

    def tearse_weekly_to_file(self,timestr):
        '''
        Writes tearse weekly forecast to file in reports
        '''
        pass

    def tearse_weekly_to_file(self,timestr):
        '''
        Writes tearse weekly forecast to file in reports
        '''
        pass

    def raw_weekly_to_file(self, timestr):
        '''
        Writes weekly forecast to file in reports.
        '''
        if self.weekly_forecast is not None:
            with open(f'reports/weekly_forecast-{timestr}.txt', 'w') as file:
                file.writelines('''
                    -------------------------------------------------
                    -------------------------------------------------
                                Begin Weekly Forecast:\n\n''')
                text = json.dumps(self.weekly_forecast, sort_keys=False, indent=4)
                file.writelines(f'Weekly Forecast for ({self.lat},{self.lon}):\n\n')
                for line in text:
                    file.writelines(line)
                file.writelines('''
                                 End of Weekly Forecast

                    -------------------------------------------------
                    -------------------------------------------------
                    ''')
            file.close()

    def raw_hourly_to_file(self, timestr):
        '''
        Writes hourly forecast to file in reports.
        '''
        if self.hourly_forecast is not None:
            with open(f'reports/hourly_forecast-{timestr}.txt', 'w') as file:
                file.writelines('''
                    -------------------------------------------------
                    -------------------------------------------------
                                Begin Hourly Forecast:\n\n''')
                text = json.dumps(self.hourly_forecast, sort_keys=False, indent=4)
                file.writelines(f'Hourly Forecast for ({self.lat},{self.lon}):\n\n')
                for line in text:
                    file.writelines(line)
                file.writelines('''
                                 End of Hourly Forecast
                                 
                    -------------------------------------------------
                    -------------------------------------------------
                    ''')
            file.close()