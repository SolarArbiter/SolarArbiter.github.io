"""
An example script to generate random forecasts for participants
in the first test trial of the Solar Forecast Arbiter.
This script should be run as cronjob or via another scheduling
mechanism at an appropriate interval that will be determined by
the trial/forecast parameters.
"""
import logging
import sys


import numpy as np
import pandas as pd


from solarforecastarbiter.io import api
from solarforecastarbiter.reference_forecasts import utils


API_URL = 'https://api.solarforecastarbiter.org'
FORECAST_IDS = [
    # the UUIDs of the relevant forecasts go here
]
logging.basicConfig(level='INFO')

# here, we read the file provided as an argument to the script
# to get the username and password (separated by a new line).
# Alternatives include using environment variables or hardcoding the values
with open(sys.argv[1], 'r') as f:
    username, password = f.read().split('\n')[:2]

# Setup an APISession to communicate with the solararbiter API
token = api.request_cli_access_token(username, password)
session = api.APISession(token, base_url=API_URL)


def list_forecasts_for_the_trial(session, string_in_extra_params):
    """Function that could be used to examine the all forecasts
    and select the relevant forecasts based on the forecast
    extra_parameters."""
    # Get information about the current user
    user_info = session.get_user_info()

    # Retrive all forecasts the user has access to
    all_forecasts = session.list_forecasts()

    # Filter out the forecasts not in the trial
    # for the purposes of this trial, the trial name will
    # appear in the extra_parameters section of the Forecast
    trial_forecasts = filter(
        lambda x: (
            string_in_extra_params in x.extra_parameters
        ) and (
            x.provider == user_info['organization']
        ),
        all_forecasts
    )
    return trial_forecasts


# go through each of our forecasts in the trial,
# generate random data, and upload to the API
for forecast_id in FORECAST_IDS:
    forecast = session.get_forecast(forecast_id)
    logging.info('Check if a forecast should be generated for %s',
                 forecast.name)
    # set the run_time as now
    run_time = pd.Timestamp.now(tz='UTC')
    # From the forecast metadata, determine the next time
    # the forecasts should be issued
    issue_time = utils.get_next_issue_time(
        forecast, run_time)
    # if the next issue_time is not within 10 minutes of the
    # current time, skip and move on to the next forecast
    if (issue_time - run_time) > pd.Timedelta('10min'):
        logging.info('Not yet time to generate forecast for %s. '
                     'Next issue time is %s.',
                     forecast.name, issue_time)
        continue

    # Get the time range that we are expected to generate a
    # forecast for. This includes an adjustment for the lead time
    # before a forecast is valid.
    start, end = utils.get_forecast_start_end(
        forecast, issue_time, adjust_for_interval_label=True)
    logging.info('Generating forecast for %s from %s to %s',
                 forecast.name, start, end)

    # make the forecast, in this case just random numbers
    # between 0 and 100
    # first, make the index
    index = pd.date_range(start=start, end=end, freq=forecast.interval_length)
    # now make the random series
    forecast_series = pd.Series(np.random.randint(0, 100, len(index)),
                                index=index)
    # upload the forecast to the API
    # catch and log errors so we can try uplloading the other forecasts
    try:
        session.post_forecast_values(forecast.forecast_id, forecast_series)
    except Exception:
        logging.exception('Failed to upload forecast for %s', forecast.name)
        continue
