---
layout: blog
author: Tony Lorenzo
---

This post describes the first test trial of the Solar Forecast Arbiter
framework, and a script that participants can uses to generate and post
random forecasts for the trial. Read about the full testing plans in the
[Trials Testing blog post](https://solarforecastarbiter.org/2020/02/12/Trials-Testing.html).

To set up a trial, the framework administrators perform the following steps:

1. Work with stakeholders to define trial parameters
2. Create anonymous users
3. Create [Site metadata](https://solarforecastarbiter.org/datamodel/#site) and [Observation metadata](https://solarforecastarbiter.org/datamodel/#observations) (as required)
4. For each anonymous user, create the [Forecast objects](https://solarforecastarbiter.org/datamodel/#forecasts)
5. Create daily and final Reports of how the forecasts perform

Trial participants will receive an email with their unique, anonymous
username to use specifically for the trial along with a link to set a
password.  Participants then use this trial username and password to
upload forecast values for each forecast object assigned to them.  In
most cases, the framework will restrict uploads so only those made
before the forecast issue time of day are valid.

**Example Script**

An example script to upload random forecast values for each of the user's
forecast objects in a trial can be found at the end of this post and
[in this gist](https://gist.github.com/alorenzo175/93ce302e23821bc6f6a78124f135aebc).

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
found at
[https://solarforecastarbiter-core.readthedocs.io/en/latest/](https://solarforecastarbiter-core.readthedocs.io/en/latest/).


<script src="https://gist.github.com/alorenzo175/93ce302e23821bc6f6a78124f135aebc.js"></script>
