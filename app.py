# import os
# import sys
# import json
import argparse
import time
from weather import forecast
from weather import settings

# Import settings defaults:
settings = settings.Settings()

# Initialize argument parser:
parser=argparse.ArgumentParser()

# Grab timestring in case it's needed later:
timestr = time.strftime("%Y%m%d-%H%M%S")

# Parser args for the program:
parser.add_argument('--weekly-text', 
    help = 'Print text-based weekly forecast to file',
    action='store_true')
parser.add_argument('--hourly-text',
    help='Print text-based hourly forecast to file',
    action='store_true')
parser.add_argument('--raw', help='Output raw JSON data', 
    action='store_true')

args = parser.parse_args()

# Program flow:

fcast = forecast.Forecast(settings.lat,settings.long)

if args.weekly_text and args.raw:
    # If True, fetch weekly forecast
    fcast.get_weekly()
    fcast.raw_weekly_to_file(timestr)

if args.hourly_text and args.raw:
    # If True, fetch hourly forecast
    fcast.get_weekly()
    fcast.raw_hourly_to_file(timestr)

if args.weekly_text:
    # I can see doing something nifty here with a Jupyter Notebook or something?
    pass

if args.hourly_text:
    # I can see doing something nifty here with a Jupyter Notebook or something?
    pass


# print('DEBUG: ',settings.timestamp)