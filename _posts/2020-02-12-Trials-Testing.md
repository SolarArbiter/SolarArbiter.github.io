---
layout: blog
author: Will Holmgren
---

*This post may be updated based on stakeholder feedback.*

The Solar Forecast Arbiter now supports anonymous operational forecast
trials. The team has run a series of internal tests of this feature.
Because of the importance of this feature, we’re requesting that a
handful of forecast users and forecast vendors help us test the feature
to ensure that it operates smoothly and meets their needs.

We propose a series of short forecast trials described below. We expect
that trials may need to be rerun to accommodate errors on our side or
unexpected difficulties for users.

We ask that users do not upload real forecasts for these initial test
trials. Rather, users should upload non-proprietary, random, constant,
or other types of forecast that could be made publicly available without
concern. This will allow all of us to debug systems more easily if/when
issues arise. To the extent that it’s feasible to program within your
systems, we recommend running your systems as if you were making a real
forecast but then replacing the final data with fake data before posting
it to the Arbiter’s API.

Before starting a trial, users should be familiar with posting forecast
data to the Arbiter’s API. We expect the API to be relatively
straightforward to program against. The API documentation is available
at [https://api.solarforecastarbiter.org/](https://api.solarforecastarbiter.org/)

**Trial 1:**

* Start time: 2020-04-21 19:00Z
* End time: 2020-04-23 19:00Z
* Observations:
  * Table Mountain GHI
* Forecasts:
  * Day ahead:
    * Issue time: 7Z (local midnight)
    * Lead time to start: 24 hours
    * Interval length: 1 hour
    * Interval value type: mean
    * Run length: 24 hours
  * Benchmark:
    * Day ahead GFS
* Metrics:
  * MAE, MBE, RMSE, KSI
* Categories:
  * Total, daily, hour of day
* Quality flags to exclude:
  * Nighttime
  * User flagged

**Trial 2:**

* Start time: 2020-05-05 19:00Z
* End time: 2020-05-07 19:00Z
* Observations:
  * All DOE RTC AC Power
* Forecasts:
  * 75 minutes ahead of the hour, 5 minute intervals:
    * Issue time: 00:45
    * Lead time to start: 75 minutes
    * Interval length: 5 minutes
    * Interval value type: mean
    * Run length: 1 hour
  * Benchmark:
    * Intraday HRRR
* Metrics:
  * MAE, MBE, RMSE, KSI
* Categories:
  * Total, daily, hour of day
* Quality flags to exclude:
  * User flagged

**Trial 3:**

* Start time: 2020-05-19 19:00Z
* End time: 2020-05-21 19:00Z
* Observations:
  * Supplied by TBD forecast user
* Forecasts:
  * Relevant to TBD forecast user
  * Benchmark TBD forecast user
* Metrics:
  * TBD forecast user
* Categories:
  * TBD
* Quality flags to exclude:
  * TBD

Please contact Will Holmgren at
[holmgren@email.arizona.edu](mailto:holmgren@email.arizona.edu) with
comments, questions, or to sign up for the trials testing.
