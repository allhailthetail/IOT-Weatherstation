import os
import sys
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


from weather import forecast

# Begin by importing the settings from the config file:

# Initialize a new Forecast for Little Rock, AR (for testing purposes):
f = forecast.Forecast('34.7490', '-92.2824')

# Begin tests:

f._get_weekly()
f._get_hourly()

with open('tests/output.txt', 'w') as file:
    weekly_forecast = json.dumps(f.weekly_forecast, sort_keys=False, indent=4)
    file.writelines('Testing Weekly Forecast:\n\n')
    for line in weekly_forecast:
        file.writelines(line)
    file.writelines('\n\n---------------------------\n\n')
    
    hourly_forecast = json.dumps(f.hourly_forecast, sort_keys=False, indent=4)
    file.writelines('Testing Hourly Forecast:\n\n')
    for line in hourly_forecast:
        file.writelines(line)
    file.writelines('\n\n---------------------------\n\n')

file.close()