---
layout: base
permalink: /documentation/dashboard/trials/
sidebar: dashboard_trial_sidebar.html
title: Trials
---

Trials
======
{: .anchor}

The Solar Forecast Arbiter supports operational forecast trials, including features such as:

* Multiple anonymous vendors
* Built-in benchmark forecasts
* Penalties for missing forecasts
* Rejection of late forecasts
* Daily reanalysis of forecast performance

The Solar Forecast Arbiter does not declare trial winners nor declare that one
forecast is superior to another. It simply provides an impartial calculation of
metrics following clearly defined data processing and forecast specifications.

In addition to the material on this page that is specific to the Solar Forecast Arbiter,
we recommend that users review the [IEA Wind Task 36 Work Packages](https://www.ieawindforecasting.dk/work-packages) for information on weather forecasts, benchmarking, and optimal use of
forecasting solutions. The vast majority of the material applies to both solar
and wind forecasts and will aid users in defining their forecast requirements.

All participating organizations must sign the [Data Use Agreement](https://solarforecastarbiter.org/assets/45864%20Approved_Final%20version%201.1.pdf)
before a trial can begin.


Initiating a trial
------------------
{: .anchor}

Forecast users may contact [admin@solarforecastarbiter.org](mailto:admin@solarforecastarbiter.org)
with a request to initiate a trial. While the trial does not need to be
fully-specified when contacting us, it will be most effecient if your request
includes information about:

* Sites and variables
* Start and end dates
* Forecast lead time to start
* Forecast interval length
* Forecast issue time of day
* [Metrics](/metrics) (MAE, MBE, RMSE, Skill, etc.)
* Time categories (total, day, hour, etc.)
* Reference forecasts
* Data quality flags to exclude
* Rule for missing forecasts (exclude, fill with 0, fill with last valid value)
* Anticipated outcome at trial conclusion (e.g. award contract to vendor)

See [Forecast Definitions](/definitions/) for an explanation of how the Solar
Forecast Arbiter defines forecast parameters. Multiple sites and forecasts
(e.g. hour ahead and day ahead) may be analyzed in a single trial.

The Solar Forecast Arbiter administrators will help you refine your requirements
if needed.


Design iteration
----------------
{: .anchor}

Next, the Solar Forecast Arbiter administrators will email the proposed requirements to
our participating [forecast vendor list](#forecast-vendor-list).
Forecast vendors will be given an opportunity to provide feedback on the trial
design to the end users. After some iteration, the Solar Forecast Arbiter
administrators will finalize the trial requirements and present them to vendors
to opt in.


Vendor opt in
-------------
{: .anchor}

The Solar Forecast Arbiter administrators will email a final set of trial
specifications to forecast vendors. The specifications will include:

* Start and end datetimes.
* All metadata needed instantiate the relevant Site, Observation, and Forecast
  objects in the Solar Forecast Arbiter or links to existing metadata. This
  fully defines the forecast specifications.
* All metadata needed to instantiate reference forecast objects or links to
  existing reference forecasts.
* All metrics to be computed.
* All time categories over which metrics will be calculated.
* Observation data quality flags that will be excluded from analysis.
* Rule for missing forecasts (exclude, fill with 0, fill with last valid value).
* Rules for visibility of forecast time series with other anonymous vendors:
  1. during the trial and
  2. in the final report.

The specification will also include the forecast user's anticipated outcome at
the trial conclusion, but we emphasize that the Solar Forecast Arbiter team will
play no role in facilitating that outcome.

Forecast vendors respond with an indication that they would like to participate
in the trial or decline to respond.


Anonymous accounts
------------------
{: .anchor}

The Solar Forecast Arbiter will create a new anonymous user account for each
vendor for each trial. The mapping between the trial participants and the
anonymized names is created automatically so that the administrators do not know
the true identities. An automated email will be sent to each trial participant with
the anonymous username, a password reset link, and a securely signed text file.
This text file can be used to verify that a trial participant was assigned a
particular anonymous user account. It should be kept in a safe location.

The Solar Forecast Arbiter will automatically create all required
[forecast metadata](/documentation/dashboard/working-with-data/#create-new-forecast)
for each forecast vendor. This also defines the API endpoints that forecasters
will use to [upload data](#data-upload) during a trial.

Forecast vendors use the anonymous accounts to log in to the dashboard and to
obtain tokens for use with the API. When logging into the dashboard with the
anonymous account, users will only see the metadata and data objects that are
relevant to this trial. All other user-supplied data and reference data is not
accessible by an anonymous trial account, but is of course still accessible
with a standard user account.


Data upload
-----------
{: .anchor}

Once the trial begins, forecast users and vendors upload their data using the
Solar Forecast Arbiter's RESTful HTTP [API](https://api.solarforecastarbiter.org/).
Users upload their observation data using the
[Add Observation Data endpoints](https://api.solarforecastarbiter.org/#tag/Observations/paths/~1observations~1{observation_id}~1values/post)
and vendors upload their forecast data using the
[Add Forecast Data endpoints](https://api.solarforecastarbiter.org/#tag/Forecasts/paths/~1forecasts~1single~1{forecast_id}~1values/post) or
[Add Probabilistic Forecast Data endpoints](https://api.solarforecastarbiter.org/#tag/Probabilistic-Forecasts/paths/~1forecasts~1cdf~1single~1{forecast_id}~1values/post). The endpoints are
unique to each forecast for each vendor. The Solar Forecast Arbiter's data
administration rules prevent other users from uploading data to each vendor's
forecasts. Depending on the trial design, other vendors may or may not be able
to view the data.

Forecast vendors must upload their forecasts before the closing time of any
forecast run. Forecasts that are not uploaded are handled according to the
trial specification agreed to in [vendor opt in](#vendor-opt-in).

Forecast vendors may upload data for intervals beyond what is required at any
given time. The data may be overwritten until the closing time of the forecast
run. Consider a 1 hour lead time, 1 hour interval forecast with
hour-beginning interval labels. In this example, a forecast vendor need only
upload a single value each at each hour of the trial.
For instance, before (or precisely at) ``2020-01-01T00:00:00Z`` a vendor may
upload the forecast

```
# valid upload at any time until 2020-01-01T00:00:01Z
timestamp,value
2020-01-01T01:00Z,10
```

The vendor could choose to upload additional forecast values such as

```
# valid upload at any time until 2020-01-01T00:00:01Z
timestamp,value
2020-01-01T01:00Z,10
2020-01-01T02:00Z,20
2020-01-01T03:00Z,30
```

Now imagine we advance in time to the next forecast interval.
From ``2020-01-01T00:00:00Z`` to ``2020-01-01T01:00:00Z`` (inclusive)
the vendor may change the value of all forecasts starting from ``2020-01-01T02:00:00Z``.
A valid upload could be

```
# valid upload at any time until 2020-01-01T01:00:01Z
timestamp,value
2020-01-01T02:00Z,25
2020-01-01T03:00Z,35
2020-01-01T04:00Z,45
```

The API will reject an upload that contains a time that should have already
been issued. For example, during this interval, the upload would be rejected
if it contains any times before ``2020-01-01T02:00:00Z``.

```
# invalid upload after 2020-01-01T00:00Z
timestamp,value
2020-01-01T01:00Z,15
2020-01-01T02:00Z,25
2020-01-01T03:00Z,35
2020-01-01T04:00Z,45
```

Assuming no additional uploads, the time series used for evaluation would be

```
# forecast evaluation time series
timestamp,value
2020-01-01T01:00Z,10
2020-01-01T02:00Z,25
2020-01-01T03:00Z,35
2020-01-01T04:00Z,45
```

See the [Example script](#example-script) section below for an example of how
to program against the API for a trial.


Intermediate reports
----------------
{: .anchor}

During a trial, the Solar Forecast Arbiter will automatically compute error
statistics at a predetermined frequency, typically once per day. The results will
be available in a standard Solar Forecast Arbiter report listed under the
Dashboard's [Reports](https://dashboard.solarforecastarbiter.org/reports/)
section. The reports will compute all metrics for all categories for all forecasts as
specified in the trial design. The results are overwritten each time the reports
are recomputed.


Trial conclusion
----------------
{: .anchor}

At the conclusion of a trial, the Solar Forecast Arbiter administrators will
email all participants to let them know that the final analysis report has been
generated.

We urge users to download html and pdf copies of the report. These downloads
contain a [PGP signature](https://en.wikipedia.org/wiki/Pretty_Good_Privacy)
that may be used to verify the authenticity of the report. The Solar Forecast
Arbiter is not a long-term data repository and we make no guarantees about the
length of time we will store trial results.

Forecast vendors may or may not choose to directly contact the forecast vendor
and reveal their identities (identity may be proven using the signed text file
provided when the anonymous account was created). The forecast user may or may
not decide to pursue the recorded anticipated outcome.
The Solar Forecst Arbiter plays no role in these processes.


Forecast vendor list
--------------------
{: .anchor}

All forecast vendors are encouraged to register with the forecast vendor list
by contacting [admin@solarforecastarbiter.org](mailto:admin@solarforecastarbiter.org).
Please include a link to your vendor website so that we may confirm that you
represent a legitmate forecast vendor. We accept requests for individuals
(e.g. ``name@fxvendor.com``) and lists (e.g. ``info@fxvendor.com``).

Signing the [Data Use Agreement](https://solarforecastarbiter.org/assets/45864%20Approved_Final%20version%201.1.pdf)
is not required for addition to the vendor list, but you will not be able to participate
in trials until the DUA is signed.


Example script
--------------
{: .anchor}

We urge vendors to practice using the API with test forecasts before a trial
starts. An example script to upload forecast values for each of the user's
forecast objects in a trial can be found below and
[in this gist](https://gist.github.com/alorenzo175/93ce302e23821bc6f6a78124f135aebc).
We do not guarantee the reliability of this script for operational forecast
trials - it is only an example to help you get started with the API.

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
[solarforecastarbiter-core Docker image](https://quay.io/repository/solararbiter/solarforecastarbiter-core)
which includes a Python installation and all requirements. Otherwise,
the solarforecastarbiter-core Python package can be installed from the
[Github repository](https://github.com/solararbiter/solarforecastarbiter-core)
or via pip with the command

```
pip install git+https://github.com/solararbiter/solarforecastarbiter-core.git
```

The script should be run periodically to generate new forecasts, either using
cron jobs or a cron Python framework like
[schedule](https://schedule.readthedocs.io/en/stable/). Further
documentation for the solarforecastarbiter-core Python package can be
found at
[https://solarforecastarbiter-core.readthedocs.io/en/latest/](https://solarforecastarbiter-core.readthedocs.io/en/latest/).

<script src="https://gist.github.com/alorenzo175/d25293c4e47bec307ede7cd70022582c.js"></script>
