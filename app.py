# import os
# import sys
# import json
import argparse
import time
from weather import forecast

# Initialize argument parser:
parser=argparse.ArgumentParser()

# Grab timestring in case it's needed later:
timestr = time.strftime("%Y%m%d-%H%M%S")

# Parser args for the program:
#
# Positional Arguments:
parser.add_argument('latitude',
    help='Must Specify US-Based Latitude',
    type=str)
parser.add_argument('longitude',
    help='Must Specify US-Based Longitude',
    type=str)
#
# Optional arguments:
parser.add_argument('--weekly-text', 
    help='Print text-based weekly forecast to file',
    action='store_true')
parser.add_argument('--hourly-text',
    help='Print text-based hourly forecast to file',
    action='store_true')
parser.add_argument('--raw', help='Output raw JSON data', 
    action='store_true')

args = parser.parse_args()

# Program flow:
# For testing: (Little Rock Coords) python app.py 34.7490 -92.2824 --weekly-text --hourly-text --raw
fcast = forecast.Forecast(args.latitude,args.longitude)

if args.weekly_text and args.raw:
    # If True, fetch weekly forecast
    fcast._get_weekly()
    fcast.raw_weekly_to_file(timestr)

if args.hourly_text and args.raw:
    # If True, fetch hourly forecast
    fcast._get_hourly()
    fcast.raw_hourly_to_file(timestr)

if args.weekly_text:
    # I can see doing something nifty here with a Jupyter Notebook or something?
    pass

if args.hourly_text:
    # I can see doing something nifty here with a Jupyter Notebook or something?
    pass


# print('DEBUG: ',settings.timestamp)