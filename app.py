import argparse
import subprocess
import papermill as pm
from weather import forecast

# Initialize argument parser:
parser=argparse.ArgumentParser()

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
parser.add_argument('--raw', help='Full/Raw JSON Output', 
    action='store_true')
parser.add_argument('--weekly-graphical', help='Output weekly data via Juptyer Notebook and PDF', 
    action='store_true')
parser.add_argument('--hourly-graphical', help='Output hourly data via Juptyer Notebook and PDF', 
    action='store_true')

args = parser.parse_args()

# Initialize a new forecast:
fcast = forecast.Forecast(args.latitude,args.longitude)

# Program Flow:
# For testing: (Little Rock Coords) python app.py 34.7490 -92.2824 --weekly-text --hourly-text --raw
# For graphical testing: python app.py 38.8313 -104.8038 --weekly-graphical
# jupyter nbconvert --to html --no-input 'reports/weekly_report.ipynb' --output='weekly_report.html' &> /dev/null

if args.weekly_text:
    # If True, fetch weekly forecast
    fcast._get_weekly()
    fcast.tearse_weekly_to_file()

if args.hourly_text:
    # If True, fetch hourly forecast
    fcast._get_hourly()
    fcast.tearse_hourly_to_file()

if args.weekly_text and args.raw:
    # If True, fetch weekly forecast
    fcast._get_weekly()
    fcast.raw_weekly_to_file()

if args.hourly_text and args.raw:
    # If True, fetch hourly forecast
    fcast._get_hourly()
    fcast.raw_hourly_to_file()

if args.weekly_graphical:
    # Queue Jupyter Notebook 'notebooks/weekly_template.ipynb'
    pm.execute_notebook(
        'notebooks/weekly_template.ipynb',
        'reports/weekly_report.ipynb',
        parameters=dict(latitude=args.latitude, longitude=args.longitude))

    # Process into HTML:
    # jupyter nbconvert --to html --no-input 'reports/weekly_report.ipynb' --output='weekly_report.html'
    subprocess.Popen("jupyter nbconvert --to html --no-input 'reports/weekly_report.ipynb' --output='weekly_report.html'", 
        shell=True, 
        stdout=subprocess.PIPE).stdout.read()

if args.hourly_graphical:
    # ToDo Develop this
    pass