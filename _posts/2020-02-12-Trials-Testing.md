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

* Start time: 2020-07-29 19:00Z
* End time: 2020-07-31 19:00Z
* Observations:
  * All Surfrad GHI:
    * [Bondville IL ghi](https://dashboard.solarforecastarbiter.org/observations/9de039e6-7e49-11e9-b002-0a580a8003e9)
    * [Table Mountain Boulder CO ghi](https://dashboard.solarforecastarbiter.org/observations/9dfe124a-7e49-11e9-98c3-0a580a8003e9)
    * [Desert Rock NV ghi](https://dashboard.solarforecastarbiter.org/observations/9e1c23da-7e49-11e9-9ec0-0a580a8003e9)
    * [Fort Peck MT ghi](https://dashboard.solarforecastarbiter.org/observations/9e35e3e6-7e49-11e9-af11-0a580a8003e9)
    * [Goodwin Creek MS ghi](https://dashboard.solarforecastarbiter.org/observations/9e51ae1c-7e49-11e9-acbe-0a580a8003e9)
    * [Penn State Univ PA ghi](https://dashboard.solarforecastarbiter.org/observations/9e6d4c1e-7e49-11e9-9174-0a580a8003e9)
    * [Sioux Falls SD ghi](https://dashboard.solarforecastarbiter.org/observations/9e8c0f8c-7e49-11e9-91e1-0a580a8003e9)
* Forecasts:
  * 60 minutes ahead of the hour, 60 minute intervals:
    * Issue time: 00:00
    * Lead time to start: 60 minutes
    * Interval length: 60 minutes
    * Interval value type: mean
    * Run length: 60 minutes
    * Interval label: beginning
  * Benchmark:
    * Hour ahead persistence e.g. [Table Mountain Boulder CO Hour Ahead Persistence ghi](https://dashboard.solarforecastarbiter.org/forecasts/single/d692a2b4-a675-11ea-a9c4-0a580a80039b)
* Metrics:
  * MAE, MBE, RMSE, KSI, Skill
* Categories:
  * Total, daily, hour of day
* Quality flags to exclude:
  * User flagged
  * Nighttime
* Missing forecasts:
  * Filled with 0

Given the forecast parameters, the first forecast would be uploaded by 2020-07-29 18:00Z with an hourly timerange of [2020-07-29 19:00Z, 2020-07-29 20:00Z). The second forecast would be uploaded by 2020-07-29 19:00Z covering the time range [2020-07-29 20:00Z, 2020-07-29 21:00Z). And so on through the final forecast issue time of 2020-07-31 17:00Z. The API will restrict forecast uploads to be valid forecasts given the parameters, meaning it will not allow forecasts to be POSTed after each issue time. Please make sure to take this into account by, for example, scheduling the forecast job to run at 18:50Z. Analysis reports will be recomputed at 3Z each day of the trial and may not reflect the latest forecasts until the latest observation data is available in the Arbiter.

**Trial 3:**

Test Trial 3 will test day ahead and hour ahead forecasts for AC power, mean SURFRAD GHI, and two probabilistic forecasts of GHI. This trial will run on Solar Forecast Arbiter version 1.0rc4.

The following forecast start, end, and timing parameters are the same for all forecasts:

* Start time: 2020-11-10 19:00Z
* End time: 2020-11-12 19:00Z
* Forecast parameters:
  * 60 minutes ahead of the hour, 60 minute intervals:
    * Issue time: 00:00
    * Lead time to start: 60 minutes
    * Interval length: 60 minutes
    * Interval value type: mean
    * Run length: 60 minutes
    * Interval label: ending
  * Day ahead:
    * Issue time: 19Z
    * Lead time to start: 24 hours
    * Interval length: 1 hour
    * Interval value type: mean
    * Interval label: ending
    * Run length: 24 hours

The following 4 sets of metadata describe the observations, metrics, categories, quality flags, missing forecast policy, and reference forecasts:

* Observation:
  * [UO SRML Bend OR PV AC Power](https://dashboard.solarforecastarbiter.org/observations/c8d69834-a5ec-11ea-a9ae-0a580a820181)
* Metrics:
  * MAE, MBE, RMSE, Skill
* Categories:
  * Total, daily, hour of day
* Quality flags to exclude:
  * None
* Missing forecasts:
  * Filled with 0
* Reference forecast:
  * Hour ahead: Persistence of clear sky index
  * Day ahead: GFS

* Observation:
  * Average of all SURFRAD GHI
* Metrics:
  * MAE, MBE, RMSE
* Categories:
  * Total, daily, hour of day
* Quality flags to exclude:
  * None
* Missing forecasts:
  * Filled with 0
* Reference forecast:
  * None

* Observation:
  * [Table Mountain Boulder CO ghi](https://dashboard.solarforecastarbiter.org/observations/9dfe124a-7e49-11e9-98c3-0a580a8003e9)
* Probabilistic Forecast Thresholds:
  * Prob(obs < 50 W/m^2)
  * Prob(obs < 500 W/m^2)
* Metrics:
  * BS, REL, RES, UNC
* Categories:
  * Total, daily, hour of day
* Quality flags to exclude:
  * Nighttime
* Missing forecasts:
  * Filled with 0
* Reference forecast:
  * None

* Observation:
  * [Table Mountain Boulder CO ghi](https://dashboard.solarforecastarbiter.org/observations/9dfe124a-7e49-11e9-98c3-0a580a8003e9)
* Probabilistic Forecast Percentiles:
  * Prob(obs < fx) = 2%
  * Prob(obs < fx) = 10%
  * Prob(obs < fx) = 50%
  * Prob(obs < fx) = 90%
  * Prob(obs < fx) = 98%
* Metrics:
  * BS, QS
* Categories:
  * Total, daily, hour of day
* Quality flags to exclude:
  * Nighttime
* Missing forecasts:
  * Filled with 0
* Reference forecast:
  * Hour ahead: Persistence ensemble
  * Day ahead: GEFS


Please contact Will Holmgren at
[holmgren@email.arizona.edu](mailto:holmgren@email.arizona.edu) with
comments, questions, or to sign up for the trials testing.
