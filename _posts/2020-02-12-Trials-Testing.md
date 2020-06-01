---
layout: blog
author: Will Holmgren
---

*This post may be updated based on stakeholder feedback.*

The Solar Forecast Arbiter now supports anonymous operational forecast trials. The team has run a series of internal tests of this feature. Because of the importance of this feature, we’re requesting that forecast users and forecast vendors help us test the feature to ensure that it operates smoothly and meets their needs.

We propose a series of short forecast trials described below. We expect that trials may need to be rerun to accommodate errors on our side or unexpected difficulties for users.

We ask that users not upload real forecasts for these initial beta-tests of the trial system. Rather, users should upload non-proprietary, random, constant, or other types of forecast that can be made public. This will allow all of parties to the testing to trace and debug errors without security concerns. To the extent that it’s feasible to program within your systems, we recommend running your systems as if you were making a real forecast but then replacing the final data with fake data before posting it to the Arbiter’s API.


Before starting a trial, users should be familiar with posting forecast
data to the Arbiter’s API. We expect the API to be relatively
straightforward to program against. The API documentation is available
at [https://api.solarforecastarbiter.org/](https://api.solarforecastarbiter.org/).  The development team has also created a [script and accompanying blog post](https://solarforecastarbiter.org/2020/05/18/First-Trial-Data-Uploads.html) to help testers spin up as quickly as possible.

It is worth noting that work done in this testing phase can be reused in the future for a real trial and thus has benefit to stakeholders too. In recognition of your help in this critical beta-testing, we will provide any support needed.

**Trial 1:**

* Start time: 2020-06-04 19:00Z
* End time: 2020-06-06 19:00Z
* Observations:
  * Table Mountain GHI
* Forecasts:
  * Day ahead:
    * Issue time: 19Z
    * Lead time to start: 24 hours
    * Interval length: 1 hour
    * Interval value type: mean
    * Interval label: beginning
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

Given the forecast parameters, one forecast would be uploaded by 2020-06-03 19:00Z with an hourly timerange of [2020-06-04 19:00Z, 2020-06-05 19:00Z). The second (and final) forecast would be uploaded at 2020-06-04 19:00Z covering the time range [2020-06-04 19:00Z, 2020-06-06 19:00Z). The API will restrict forecast uploads to be valid forecasts given the parameters, meaning it will not allow forecasts to be POSTed after each issue time. Please make sure to take this into account by, for example, scheduling the forecast job to run at 18:50Z.


**Trial 2:**

* Start time: 2020-06-09 19:00Z
* End time: 2020-06-11 19:00Z
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

* Start time: 2020-06-23 19:00Z
* End time: 2020-06-25 19:00Z
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
