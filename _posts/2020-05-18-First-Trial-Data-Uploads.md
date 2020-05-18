---
layout: blog
author: Tony Lorenzo
---

This post describes the first test trial of the Solar Forecast Arbiter
framework, and a script that participants can uses to generate and post
random forecasts for the trial.

To set up a trial, the framework administrators perform the following steps:

1. Work with stakeholders to define trial parameters
2. Create anonymous users
3. Create Sites and Observations (as required)
4. For each anonymous user, create the Forecast objects
5. Create periodic and final Reports of how the forecasts performed

Trial participants will receive an email with their unique, anonymous
username to use specifically for the trial along with a link to set a
password.  Participants then use this trial username and password to
upload forecast values for each forecast object assigned to them.  In
most cases, the framework will restrict uploads so only those made
before the forecast issue time of day are valid.

**Example Script**

An example script to upload random forecast values for each of the user's
forecast objects in a trial can be found
[here](https://solarforecastarbiter.org/assets/test_trial_1_random_forecast_upload.py).

This script uses the
[solarforecastarbiter-core](https://github.com/solararbiter/solarforecastarbiter-core)
library to interact with the Solar Forecast Arbiter
[API](https://api.solarforecastarbiter.org).  First, a token for API
access is requested using the username and password for the anonymous
trial user. The script expects a path to a file with the username and password
of this user seperated by a new line like
```
username
password
```

A list of forecasts is then retrieved from the API and filtered for
those forecasts relevant to the Trial. For each of these forecasts, a
check is performed to determine if the current time is within 10
minutes of the next issue time of the forecast. If it is, a random set
of values is uploaded to the API for the expected forecast time
range. Otherwise, the script moves on to trying the next forecast in
the list.

To run the script, users can make use of the
[solarforecastarbiter-core Docker
image](https://quay.io/repository/solararbiter/solarforecastarbiter-core)
which includes a Python installation and all requirements. Otherwise,
the solarforecastarbiter-core Python package can be installed from the
[Github
repository](https://github.com/solararbiter/solarforecastarbiter-core)
or via pip with the command ``pip install
git+https://github.com/solarforecastarbiter-core.git``. The script
should be run periodically to generate new forecasts, either using
cron jobs or a cron Python framework like
[schedule](https://schedule.readthedocs.io/en/stable/). Further
documentation for the solarforecastarbiter-core Python package can be
found at https://solarforecastarbiter-core.readthedocs.io/en/latest/.
