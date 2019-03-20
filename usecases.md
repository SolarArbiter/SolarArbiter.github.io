---
layout: usecases
permalink: /usecases/
---

# Use Cases


{% include to_top.html %}
## Purpose and Summary {#purpose}
{: .anchor }
This document describes Solar Forecast Arbiter use cases and their associated requirements, and Solar Forecast Arbiter framework functional capabilities.

The Solar Forecast Arbiter is primarily designed to support the evaluation of solar forecasts that are useful for solar forecast users. It is not a general-purpose weather forecast analysis tool, though it may eventually be extended to incorporate wind power and load forecast analysis.

Use cases are grouped into two categories:

1. [Evaluate forecasts](#evaluatefx). These use cases anticipate a framework user whose primary interest is comparing one or more forecasts to observation data. Forecast quantities can include irradiance, power or net load, and can vary in lead time, interval and horizon. The framework can evaluate deterministic forecasts, event forecasts, and probabilistic forecasts.
2. [Analyze forecasts](#analyzefx). These use cases anticipate a framework user whose primary interest is investigating relationships between forecasts, forecast errors, and other quantities. Examples might include the spread between probabilistic forecasts, the standard deviation of a forecast, or the hit rate of forecasting a specific event (like a large change in power).

Framework functional capabilities are grouped into three additional categories:

{:start="3"}
1. [Perform forecast evaluation in a standard manner](#evaluation)
1. [Administer the framework](#administer)
1. [Archive data and forecasts](#archive)

Metrics, benchmark forecasts, data formats, data sharing policies, and legal considerations will be detailed in other documents.


## Definitions  {#definitions}
{: .anchor}

The precise definition of a *forecast* is often a source of confusion in the forecasting industry. Consider these statements that use the term *forecast*:

<ol type="A">
  <li>"The forecast for the next 48 hours is 5 MW, 10 MW, 7 MW..."</li>
  <li>"The hour ahead forecast this morning was 5 MW, 10 MW, 7 MW..."</li>
</ol>

In Statement A, the user refers to a series of expected values issued from a single forecast. In Statement B, the user refers to a series of expected values with the **same** look-ahead time that are issued from **different** forecasts.

An evaluation challenge arises if Statement A is extended to include a new 48-hour duration forecast every hour. In this scenario, many forecasts exist at each evaluation time. More information is needed to focus the analysis to a particular application.

Statement B suggests an alternative strategy: the forecast user or the forecast provider parses forecast data into a time series for evaluation according to her **application**. For example, from many 48-hour length forecasts, a time series of forecast values with lead times of 1-hour ahead could be compiled to evaluate forecasts that support participation in a particular market. Or, a time series of forecast values for each hour of the day ahead could be compiled from forecasts issued at the same time each day to evaluate forecasts input to a production cost model. In each case, the forecast under evaluation is a continuous, non-overlapping time series that can be compared to observations.

The Solar Forecast Arbiter is designed to analyze these user-supplied, continuous, non-overlapping time series. We refer to this as a *forecast evaluation time series*.

The Solar Forecast Arbiter provides a taxonomy to allow forecast users and forecast providers to clearly and completely describe each forecast evaluation time series. For most use cases, the user is required to consider the forecast application, parse the forecast data into a continuous, non-overlapping time series for evaluation, and provide the parsed data to the Solar Forecast Arbiter for analysis – not the individual forecast runs that went into the parsed forecast.

The sections below define and illustrate the key concepts (forecast data points, runs, and evaluation time series) and the attributes that describe forecasts.


### Forecast data point {#forecastdatapoint}
{: .anchor}

A *forecast data point* is a single (*time*, *value*) data pair. Time can label a moment in time or an interval of time, as defined by the *interval label*. For example, a time of 17:00 can label the 1-hour *interval length* period from 17:00 to 18:00 (*beginning* label), 16:00 to 17:00 (*ending* label) or instantaneously at 17:00 (*instantaneous* label). Value has a *value type* (e.g., mean, 95th percentile) and *variable* (e.g. power, GHI). The variable defines the unit.


### Forecast run {#forecastrun}
{: .anchor}

A _forecast run_ is a sequence of one or more *forecast data points* issued at the same *issue time*. The time between the issue time and the first forecast data point time is the *lead time to start*. The *run length* is the time between the first forecast data point and the last forecast data point.

Most forecast runs in the Solar Forecast Arbiter are only as long as the predetermined evaluation scenario requires. For example, evaluations of forecasts with 15-minute interval, 1-hour length require a series of forecast runs that each contain only 4 forecast data points. Forecast providers often create runs that are longer than a particular Solar Forecast Arbiter evaluation scenario requires. Typically, forecast providers must parse these forecast runs into a *forecast evaluation time series* (discussed next).

Individual forecast runs are not archived or searchable except under the stretch goal [1.G. Compare multiple overlapping forecast runs to measurements](#uc1G).


### Forecast evaluation time series {#forecastevalts}
{: .anchor}

A _forecast evaluation time series_ is the concatenation of a series of non-overlapping forecast runs with sequential issue times, as shown in Figure 1 below. Each forecast run has the same attributes, except for the issue time. For example, three forecast runs (shown in green in Figure 1) could be:

- {(13:00, 10MW)} issued at 12:00, and
- {(14:00, 7MW)} issued at 13:00, and
- {(15:00, 5MW)} issued at 14:00.

From these three runs, the user could upload an hour-ahead, hour-interval forecast evaluation time series of:

- {(13:00, 10MW), (14:00, 7MW), (15:00, 5MW)}

These three runs have a 1-hour *run length / issue frequency*. The runs must have the same run length and issue frequency to create a continuous, non-overlapping forecast evaluation time series.

<img src="/images/timeline_concat_1h.svg" alt="timeline_concat_1h" class="figure">
<figcaption class="figure">Figure 1. Forecast runs with 1-hour intervals concatenated into a forecast evaluation time series.</figcaption>
<br>
The framework also supports forecast evaluation time series that are the concatenation of forecast runs with more than one interval, so long as the intervals do not overlap. Figure 2 shows how three different 75-minute-ahead, 15-minute interval, 1-hour length forecast runs may be parsed and concatenated into a single forecast evaluation time series.

<img src="/images/timeline_concat.svg" alt="timeline_concat" class="figure">
<figcaption class="figure">Figure 2. Forecast runs with 15-minute intervals concatenated into a forecast evaluation time series.</figcaption>
<br>
In most cases, the original forecast interval is retained, (e.g., 15-minutes in Figure 2) or intervals are combined to a longer interval (e.g., 15-minute values averaged to hourly values).

The *issue time of day* attribute describes the time of day at which a forecast is issued. For example, a user may require a day ahead forecast to be issued by 16:00 each day. As shown in Figures 1 and 2, a forecast evaluation time series is often constructed of forecast runs that are issued multiple times within a single day. In this case, the *issue time of day* describes the first time of day that the forecast is issued. Subsequent issue times are uniquely determined by the first issue time and the *run length / issue frequency*. This approach allows users to succinctly describe both intraday and longer forecast applications using a common set of attributes. See [Forecast evaluation time series attributes](#forecastattrs) for more examples.

For most use cases ([1.A](#uc1A)-[1.E](#uc1E)), the Solar Forecast Arbiter expects forecast providers to upload a *forecast evaluation time series*. For the Forecast Trial use case ([1.F](#uc1F)), the Solar Forecast Arbiter expects forecast providers to regularly upload a _forecast run_ that the Solar Forecast Arbiter can append to a *forecast evaluation time series*. For some forecast trials, the Solar Forecast Arbiter will allow the upload of a forecast run that is longer than the *run length / issue frequency* attribute. This behavior is analogous to a forecast user falling back on an older forecast if a new forecast is not submitted on time. Some applications may not support this flexibility (e.g. a market with strict data formats) and therefore the Solar Forecast Arbiter will reject forecast runs that are longer than *run length / issue frequency*. The setting is determined before the trial starts.

A stretch goal is to support the use case of uploading and analyzing multiple forecast runs, optionally with the same valid times ([1.G](#uc1G)). For example, the user could upload a new 24-hour length forecast that is issued each hour of the day. Later, the user could then use the framework to merge the forecast runs into a 0-, 1-, or 2-hour ahead forecast for evaluation. Figure 3 shows three forecasts runs (green) merged into two different evaluation forecasts (blue, red).

<img src="/images/timeline_merged.svg" alt="timeline_merged" class="figure">
<figcaption class="figure">Figure 3. Forecast runs merged to create two distinct forecast evaluation time series. The blue forecast evaluation time series retains the 15-minute intervals of the forecast runs. The red forecast evaluate time series is created by averaging the 15-minute values to hourly values within each forecast run.</figcaption>


### Forecast evaluation time series attributes {#forecastattrs}
{: .anchor}

The Solar Forecast Arbiter uses the set of attributes defined below to describe the characteristics of a forecast evaluation time series. This structure allows any type of forecast typically utilized in the solar energy field to be evaluated.

A *forecast evaluation time series* is described by the following attributes:

1. *Issue time of day* - The time of day that a forecast run is issued, e.g. 00:30. For forecast runs issued multiple times within one day (e.g. hourly), this specifies the first issue time of day. Additional issue times are uniquely determined by the first issue time and the *run length / issue frequency* attribute.
2. *Lead time to start* - The difference between the issue time and the start of the first forecast interval, e.g. 1 hour.
3. *Interval length* - The length of time that each data point represents, e.g. 5 minutes, 1 hour.
4. *Run length / issue frequency* - The total length of a single issued forecast run, e.g. 1 hour. To enforce a continuous, non-overlapping sequence, this is equal to the forecast run issue frequency.
5. *Interval label* - Indicates if a time labels the beginning or the ending of an interval average, or indicates an instantaneous value, e.g. beginning, ending, instant
6. *Value type* - The type of the data in the forecast, e.g. mean, max, 95th percentile.
7. *Variable* - The variable in the forecast, e.g. power, GHI, DNI. Each variable is associated with a standard unit.
8. *Site* - The predefined site that the forecast is for, e.g. Power Plant X or Aggregate Y.

A forecast must be associated with a pre-defined site. The site, not the forecast, defines geographic location and time zone. The variable determines the content of the forecast evaluation time series.

The table below shows the attributes for three different examples. We assume all intervals are labeled with the interval beginning time in these examples.

* Forecast User A requires hourly forecasts of average GHI at Sensor X located in the America/Denver time zone. The forecasts are to have 5-minute intervals and be updated 75-minute ahead of the hour.

* Forecast User B requires day ahead forecasts of hourly average power at Power Plant Y issued at 13:00 each day in the Etc/GMT+7 time zone.

* Forecast User C requires intraday forecasts for 5th percentile of power for Aggregate Z specified in the America/Phoenix time zone. The forecasts are to be issued every 3 hours with 15-minute interval length and 3-hour forecast length.

| Attribute | User A | User B | User C |
|-----------|:------:|:------:|:------:|
| Issue time of day | 00:45 | 13:00 | 00:00 |
| Lead time to start | 75 minutes | 11 hours | 0 minutes |
| Interval length | 5 minutes | 1 hour | 15 minutes |
| Run length / issue freq. | 1 hour | 24 hours | 3 hours |
| Interval label | Beginning | Beginning | Beginning |
| Value type | Mean | Mean | 5th Percentile |
| Variable | GHI (W/m2) | Power (MW) | Power (MW) |
| Site | Sensor X (America/Denver) | Power Plant Y (Etc/GMT+7) | Aggregate Z (America/Phoenix) |


### Probabilistic forecasts {#probforecastdef}
{: .anchor}

The Solar Forecast Arbiter uses cumulative distribution functions (CDF) to
quantify probabilistic forecasts. A CDF is represented here as a sequence of
(*variable value*, *percentile*) pairs, where percentiles range from 0 to 100.

Each [forecast data point](#forecastdatapoint) describes one (variable value, percentile)
point of a CDF at one point in time. Therefore, each [forecast evaluation time
series](#forecastattrs) describes (variable value, percentile) points at multiple times
while holding either value or percentile constant.

Consider a few simple examples. A probabilistic forecast may be the probability
that generation is less than 10 MW at each point in time. This probabilistic
forecast is a single number (the probability) at each [forecast data
point](#forecastdatapoint). Another probabilistic forecast may quantify the
generation that corresponds to the 50th percentile of a CDF, i.e., the median
generation value. Here, too, the probabilistic forecast is a single number (the
generation) at each [forecast data point](#forecastdatapoint). These two types
of probabilistic forecasts can be summarized as:

| Case | Constant value | Forecast type |
|------|:--------------:|:-------------:|
| Prob(Power < 10 MW) | Variable (Power) = 10 MW | Percentile |
| p50 Power | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Percentile = 50 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Variable (Power) |

Probabilistic forecasts can also be a grouping of [forecast evaluation time
series](#forecastattrs) that describe more of the probability distribution. For
example, a user may be interested in the probability that power is less than
each of a range of power levels. In this case, the *constant values* are
specified along the *x* axis of the CDF and the forecasts are percentiles:

| Case | Constant value | Forecast type |
|------|:--------------:|:-------------:|
| Prob(Power < 1 MW) | Variable (Power) = 1 MW | Percentile |
| Prob(Power < 10 MW) | Variable (Power) = 10 MW | Percentile |
| Prob(Power < 20 MW) | Variable (Power) = 20 MW | Percentile |
| Prob(Power < 30 MW) | Variable (Power) = 30 MW | Percentile |
| Prob(Power < 40 MW) | Variable (Power) = 40 MW | Percentile |
| Prob(Power < 50 MW) | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Variable (Power) = 50 MW&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Percentile |

Or, a user may be interested in the power at a number of percentiles. In this
case, the *constant values* are specified along the *y* axis of the CDF and the
forecasts are powers:

| Case | Constant value | Forecast type |
|------|:--------------:|:-------------:|
| p0 Power | Percentile = 0 | Variable (Power) |
| p5 Power | Percentile = 5 | Variable (Power) |
| p10 Power | Percentile = 10 | Variable (Power) |
| p30 Power | Percentile = 30 | Variable (Power) |
| p50 Power | Percentile = 50 | Variable (Power) |
| p70 Power | Percentile = 70 | Variable (Power) |
| p90 Power | Percentile = 90 | Variable (Power) |
| p95 Power | Percentile = 95 | Variable (Power) |
| p100 Power | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Percentile = 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Variable (Power) |

Or the user may only be interested in points that correspond to a central
credible interval:

| Case | Constant value | Forecast type |
|------|:--------------:|:-------------:|
| p10 Power | Percentile = 10 | Variable (Power) |
| p90 Power | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Percentile = 90&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Variable (Power) |

Users may specify as many percentile or variable *constant values* as is needed to
accurately communicate a probabilistic forecast.


### Probabilistic forecast attributes {#probforecastattrs}
{: .anchor}

The metadata for a probabilistic forecast is the same as for a [forecast
evaluation time series](#forecastattrs) with the addition of two attributes:

-   *Axis* - The axis on which the constant values of the CDF is specified. The
    axis can be either *x* (constant variable values) or *y* (constant
    percentiles). The axis is fixed and the same for all [forecast evaluation
    time series](#forecastattrs) in the probabilistic forecast.
-   *Constant values* - The variable values or percentiles for the set
    of [forecast evaluation time series](#forecastattrs) in the probabilistic
    forecast.


### Framework user and framework administrator {#users}
{: .anchor}

A _framework user_ is an individual or organization that uses the capabilities of Solar Forecast Arbiter to evaluate and analyze forecasts. A framework user can be a _forecast provider_ (one who creates a forecast), a _forecast user_ (one using a forecast for a defined purpose), researchers, and others.

The _framework administrator_ operates Solar Forecast Arbiter, ensures data security and anonymity, establishes standards for forecast evaluation, supports observational and forecast data exchange among users, and provides benchmark forecasts.



## Use cases  {#usecases}
{: .anchor}

A use case describes a sequence of actions to achieve a goal. Use cases are grouped into two categories: [Evaluate forecasts](#evaluatefx), and [Analyze forecasts](#analyzefx). From each use case a list of framework requirements is developed. To reduce repeating requirements, a use case may adopt, expand, or modify the requirements of another use case.

**In this section, for brevity, a *forecast* refers to the *[forecast evaluation time series](#forecastevalts)* defined in the [Definitions section](#definitions).**

### 1. Evaluate forecasts  {#evaluatefx}
{: .anchor}

#### 1.A. Compare a forecast to measurements {#uc1A}
{: .anchor}

**Use case narrative**: A framework user uploads a forecast or selects a benchmark forecast for a single location, uploads corresponding measured data or selects reference data, specifies filters, specifies temporal averaging, and selects metrics. The framework calculates metrics, provides a visual display of forecast performance and an evaluation report for download.

**Requirements**:

- User can upload measured data, select from previously uploaded measured data, or select a location/period with reference data ([4.E](#uc4E)).
  - If uploading data, user must define relevant metadata including location, data type, and units.
- User can upload a corresponding [forecast](#forecastdef) ([4.C](#uc4C)) or select corresponding benchmark forecast ([4.D](#uc4D)). The forecast must be single-valued (e.g. mean or 95th percentile) at each time.
- Framework applies data quality checks to uploaded data and forecasts ([4.G](#uc4G)).
- User can specify filters to exclude forecast or data points (a subset of (time, value) pairs), by time or by value ([2.A](#uc2A)).
- User can select among forecast performance metrics ([3.A](#uc3A)).
- Framework provides metric values and visuals of forecast performance ([3.A](#uc3A)).
- Framework provides a report for download ([3.D](#uc3D)).
- Framework protects forecasts and uploaded data as user-owned: user can specify other users and/or groups who can see/use the uploaded forecasts, data, or summary error statistics ([4.F](#uc4F)).

#### 1.B. Compare a probabilistic forecast to measurements {#uc1B}
{: .anchor}

**Use case narrative**: A framework user uploads a probabilistic forecast for a single location, uploads corresponding data or selects reference data, specifies filters, and selects metrics. The framework calculates probabilistic metrics and provides a visual display of probabilistic forecast performance.

**Requirements**:

- All requirements as listed for Use Case [1.A](#uc1A) with the following modifications.
- The probabilistic forecast must describe one or more points of a cumulative distribution function.
- User can select among probabilistic forecast performance metrics ([3.A](#uc3A)).
- Framework provides probabilistic metric values for comparison among forecasts ([3.A](#uc3A)), visual displays of probabilistic forecast performance, and a report for download ([3.D](#uc3D)).

#### 1.C. Compare multiple forecasts to measurements {#uc1C}
{: .anchor}

**Use case narrative**: Framework users upload forecasts, select benchmark forecasts, or invite other users to share forecasts for a single location. Framework users upload corresponding data or select reference data, specify data filters, specify temporal averaging, and select metrics. The framework calculates metrics and provides a visual display of forecast performance and forecast errors for download, and a visual display comparing the forecasts. The framework user can share results with other users.

**Requirements**:

- All requirements as listed for Use Case [1.A](#uc1A) or [1.B](#uc1B) for each forecast in the comparison.
- User can share forecast specifications (e.g., quantity, interval, horizon, averaging, lead times) with other framework users and invite other framework users to share forecasts for the comparison ([4.F](#uc4F)).
- Framework supports anonymous forecast comparison ([4.F](#uc4F)).
- Framework protects forecasts as specified by each forecast owner ([4.F](#uc4F)).
- Framework provides metric values for the comparison among forecasts ([3.A](#uc3A)), a visual display of comparison results, and a report for download ([3.D](#uc3D)).

#### 1.D. Compare forecasts to measurements for sites and aggregates {#uc1D}
{: .anchor}

**Use case narrative**: A framework administrator defines an aggregate of locations. A framework user uploads forecasts for each location in the aggregate and a forecast for the aggregation of locations. A framework user uploads corresponding data or selects reference data, specifies filters, specifies temporal averaging, and selects metrics. The forecasts and data may represent individual point sensors, power plants, or aggregated quantities. The framework calculates metrics and provides a visual display comparing the forecasts across scales.

**Requirements**:

- All requirements as listed for Use Case [1.A](#uc1A), [1.B](#uc1B), or [1.C](#uc1C), as appropriate.
- User uploads of individual sites and the aggregate ([4.C](#uc4C)).
- Framework computes observations, as specified by the framework's aggregate definition weights ([3.E](#uc3E)).
- Framework provides metric values for the comparison among forecasts, including sites vs. aggregate ([3.A](#uc3A)), a visual display of comparison results, and a report for download ([3.D](#uc3D)).

#### 1.E. Evaluate an event forecast {#uc1E}
{: .anchor}

**Use case narrative**: A framework user can analyze an event forecast for a single location.

**Requirements**:

- All requirements as listed by Use Case [1.A](#uc1A), [1.B](#uc1B), or [1.C](#uc1C), as appropriate.
- User can upload an event forecast, e.g., a time series of true/false values, or a time series of event occurrence likelihood ([4.C](#uc4C)).
- User can upload observed event data or select a saved event time series ([2.B](#uc2B)). The observed event data must be the same variable type and units as the event forecast.
- User can select among event forecast performance metrics ([3.A](#uc3A)).
- Framework provides metric values and visuals of event forecast performance ([3.A](#uc3A)).
- Framework provides a report for user download ([3.D](#uc3D)).

#### 1.F. Conduct forecast trial {#uc1F}
{: .anchor}

**Use case narrative**: The framework administrator, in consultation with trial participants, defines trial period, metrics, locations, forecast quantities, time horizons, time resolutions, etc. of a forecast trial. The trial may be retrospective or live, and may involve a debugging period followed by an evaluation period. Separate trials may be administered for multiple forecast parameters (e.g. hour ahead and day ahead forecast evaluations for the same set of locations).

**Example 1**: Forecast User 1 would like to evaluate the operational performance of many forecast providers. Forecast User 1 and the Framework Administrator announce the opportunity to Forecast Providers A-F. User 1 may announce its intention to contract with one or more Providers at the conclusion of the trial, but this is outside the scope of the Solar Forecast Arbiter.

The User, Administrator, and Providers discuss the many possible forecasts that could be evaluated and determine that two trials will be conducted to support particular business needs. Trial 1 is a 1-hour ahead, 1-hour interval average trial and Trial 2 is day ahead as of 13:00, 1-hour interval trial. The full forecast evaluation time series attributes are defined for each trial. For both trials, the start date is Jan 1, 2020, the end date is March 31, 2020, the evaluation metrics are average hourly MAE and RMSE, and missing forecasts will be assumed to be 0. Trial 1 will include a persistence benchmark, and Trial 2 will include a benchmark based on transparent processing of the NOAA NAM model.

Forecast User 1 creates the Sites, Observations, and Aggregate, uploads 12 months of training data, and shares the data with Forecast Providers A-F. Forecast Providers A-F download the training data and create their models. An anonymous user is automatically generated for each Provider and the Framework Administrator does not keep a record of the user mapping. Separately for each trial, Forecast Providers upload their forecast runs during the debugging period, fix any issues, and continue to regularly upload runs during the evaluation period. Forecasters that fail to submit a forecast run are penalized according to predefined rules. At the conclusion of the trials, reports are automatically generated for all participants.


**Requirements**:

- All requirements as listed for Use Case [1.C](#uc1C).
- Administrator, in consultation with trial participants, defines data sources, forecast run intervals/horizons, trial period, metrics, filters ([4.C](#uc4C)).
- Framework concatenates regularly posted forecast runs into a continuous forecast evaluation time series([4.C](#uc4C)).
- Framework accepts uploads of regularly updated data and allows for download of regularly updated data ([4.C](#uc4C)).
- Framework generates intermediate reports during the trial ([3.D](#uc3D)).

#### 1.G. Compare multiple overlapping forecast runs to measurements (stretch) {#uc1G}
{: .anchor}

**Use case narrative**: A framework user uploads a sequence of overlapping forecast runs issued at a regular interval for a single site or aggregate, uploads corresponding data or selects reference data, specifies filters, specifies temporal averaging, and selects metrics. The framework calculates metrics, provides a visual display of forecast performance and an evaluation report for download.

**Example 1**: Forecast Provider A creates a new 24-hour length forecast run at each hour of the day. Forecast User 1 would like to analyze the accuracy of points in these forecasts as a function of lead time. Forecast Provider A uploads all forecasts to the framework and shares them with Forecast User 1. Forecast User 1 uses the framework to analyze forecast performance across lead times.

**Requirements**:

- All requirements as listed for Use Case [1.A](#uc1A), for each forecast run.
- Each [forecast run](#forecastdef) must be identically specified.
- Forecast runs are issued at a regular interval (e.g., every 6 hours).
- User can upload multiple overlapping forecast runs. Each forecast run can have a different issue time, but must have the same forecast interval (duration and label), forecast length and value type (e.g. 5-minute interval, 5-minute interval-ending label, 24 hours in length, average power forecast).
- User can define forecast evaluation intervals, lead times, and temporal averaging.

#### 1.H. Establish a long-term performance baseline of state-of-the-art operational forecasts (stretch) {#uc1H}
{: .anchor}

**Use case narrative**: The framework administrator, in consultation with providers of operational forecasts, defines metrics, locations, forecast quantities, time horizons, time resolutions, etc. for a long-term, open-ended forecast evaluation. Separate evaluations may be administered for multiple forecast parameters (e.g. hour ahead and day ahead forecast evaluations for the same set of locations). Forecast performance is used to establish a long-term performance baseline of state-of-the-art operational forecasts.

**Example 1**: Forecast Providers A-F anonymously submit operational forecasts to the framework for all SURFRAD sites and handful of PV power plants across the country. Forecasts include 24-hour lead time, hourly interval and 1-hour lead time, 5-minute interval. Analysis of forecasts during the trial provide a baseline of operational forecast performance. Later, an organization funds a research effort to improve forecasts. In a retrospective or live trial scenario, the research effort submits its new forecasts to the framework for comparison against the operational forecast baseline.

**Requirements**:

- All requirements as listed for Use Case [1.F](#uc1F).
- Framework tracks and reports forecast metrics over time.
- Framework allows summary statistics from long-term trials to be used as a point of reference in reports generated for other use cases.
- Framework archives forecasts and observation data for extended periods [5.A](#uc5A).
- Framework protects anonymity of forecast providers over a multi-year period.


### 2. Analyze forecasts {#analyzefx}
{: .anchor}

#### 2.A. Analyze subsets of forecasts and data {#uc2A}
{: .anchor}

**Use case narrative**: A framework user selects a subset of an uploaded forecast, and the corresponding data, based on one or more conditions, for detailed analysis. The framework calculates metrics and provides a visual display of forecast performance.

**Requirements**:

- User can select a subset of points in a forecast or its corresponding data based on one or more conditions: forecast error (bias), forecast lead time, time of day, time of year, weather (irradiance, temperature, wind), presence or absence of data flags. Framework returns selected subsets from the forecast and corresponding data.
- User can select among forecast performance metrics ([3.A](#uc3A)).
- Framework applies data quality checks to uploaded data ([4.E](#uc4E)).
- Framework provides metric values and visuals of forecast performance ([3.A](#uc3A)).
- Framework provides a report for user download ([3.D](#uc3D)).

#### 2.B. Identify events {#uc2B}
{: .anchor}

**Use case narrative**: The framework assists a user to identify events in a forecast or in data.

**Requirements**:

- User can upload a forecast ([4.C](#uc4C)).
- User can upload data ([4.C](#uc4C)).
- Framework applies data quality checks to uploaded data ([4.E](#uc4E)).
- User can specify conditions (e.g., ramp rates, clear-sky threshold) used to identify events occurring in a forecast or in data.
- Framework provides visual display of identified events ([3.D](#uc3D)).
- Framework provides a report for user download ([3.D](#uc3D)).
- User can save event data, i.e., a time series of true/false values.

#### 2.C. Find forecasts errors with large impacts (stretch) {#uc2C}
{: .anchor}

**Use case narrative**: A framework user can associate forecast errors with system impact and can filter forecasts based on system impact.

**Requirements**:

- All requirements associated with Use Case [1.A](#uc1A).
- User can select conditions to associate forecast error with system impact ([3.B](#uc3B)).
- Framework uses user-selected conditions to calculate system impact ([3.B](#uc3B)).
- Framework finds subset of forecast times corresponding to user-defined "large" system impacts.
- Framework provides a report for user download ([3.D](#uc3D)).



## Framework functional capabilities {#capabilities}
{: .anchor}

Functional requirements are capabilities not specific to a use case but which the framework requires in order to satisfy the use cases. Functional requirements are grouped into three categories:

- [Perform forecast evaluation in a standard manner](#evaluation)
- [Administer the framework](#administer)
- [Archive data and forecasts](#archive)

### 3. Perform forecast evaluation in a standard manner {#evaluation}
{: .anchor}

#### 3.A. Calculate forecast error metrics {#uc3A}
{: .anchor}

**Use case narrative**: The framework provides a set of well-documented metrics which can be selected by a framework user for evaluating or analyzing forecasts. Metrics include, for example, statistics for forecast error, and cost estimated by a user-supplied $/MW-error.

**Requirements**:

- Metrics are documented on the framework website.
- Metrics are coded in the framework.
- Metrics can be selected by a framework user.
- Metrics are available for probabilistic forecasts.

#### 3.B. Calculate forecast error impacts (stretch) {#uc3B}
{: .anchor}

**Use case narrative**: The framework provides a set of well-documented functions to associate forecast error with system impact. System impact may include, for example, increase or decrease in reserve requirements.

**Requirements**:

- Functions for estimating system impact are documented on the framework website.
- Functions are coded in the framework.
- Function parameters can be selected by a framework user.

#### 3.C. Communicate probabilistic forecasts {#uc3C}
{: .anchor}

**Use case narrative**: The framework communicates probabilistic forecast information in a meaningful, well-documented manner.

**Requirements**:

- Quantities and terms used to describe and present probabilistic forecasts are documented on the framework website.
- Framework presents visuals for probabilistic forecasts.

#### 3.D. Facilitate communication of forecasts and forecast metrics {#uc3D}
{: .anchor}

**Use case narrative**: The framework aids a forecast provider to communicate forecast performance.

**Requirements**:

- The framework produces reports of forecast evaluation and analysis for user download.
- The framework website includes pages that aid in explaining forecasts and their use.
- Framework users can share forecasts, forecast evaluation reports, and data with other framework users.
- Framework protects forecasts and uploaded data as specified by the user.

#### 3.E. Compute aggregate observations {#uc3E}
{: .anchor}

**Use case narrative**: The framework computes aggregates of observational data, accounting for missing data and flagged data, in a well-documented manner.

**Requirements**:

- Aggregation functions are coded in the framework.
- Aggregation functions are documented on the framework website.



### 4. Administer the framework {#administer}
{: .anchor}

#### 4.A. Manage users and organizations {#uc4A}
{: .anchor}

**Use case narrative**: The framework administrator can manage users and organizations.

**Requirements**:

- Administrator can associate or disassociate users with organizations.
- Administrator can enable data upload privileges based on email communication.
- Administrator can reset user passwords.

#### 4.B. Manage data {#uc4B}
{: .anchor}

**Use case narrative**: The framework administrator can manage data storage, and can delete data upon request or at the end of the DOE funding period.

**Requirements**:

- Framework administrator can assign data storage limits.
- Framework administrator can delete stored data.
- Users can delete user-owned data.

#### 4.C. Provide the framework API {#uc4C}
{: .anchor}

**Use case narrative**: The framework provides a documented API and appropriate services for client users.

**Requirements**:

- The framework's API is documented on the framework website.
- Users can interact with the framework via HTTP requests.
- Users can request forecast evaluations via script (stretch).

#### 4.D. Provide reference forecasts {#uc4D}
{: .anchor}

**Use case narrative**: The framework provides a set of documented reference forecasts for irradiance and power, for various locations, at various intervals and horizons.

**Requirements**:

- The framework provides a reference irradiance forecast at hourly intervals for at least 72 hours for CONUS.
- The framework provides a reference irradiance forecast at user-selected intervals (5 to 60 minutes) out to 24 hours, using persistence of measured values, persistence of clearsky index, or persistence of clearness index of user-uploaded data.
- The framework provides a reference forecast for air temperature and wind speed to accompany the reference irradiance forecasts.
- The framework uses and makes available a reference model for translating irradiance and weather variables to power.
- The framework provides a reference forecast for power, using user-uploaded power and a persistence method.
- The framework can provide load and net load forecasts from user-uploaded data using persistence (stretch).
- Reference forecasts and forecast methods are documented on the framework website.

#### 4.E. Provide reference data {#uc4E}
{: .anchor}

**Use case narrative**: The framework provides reference weather and power data at selected locations.

**Requirements**:

- The framework provides reference irradiance and other weather data from a selection of stations e.g. SURFRAD stations.
- The framework provides reference power data from a selection of PV systems.
- The framework provides metadata for reference PV systems.
- The framework provides availability and status for reference PV systems.

#### 4.F. Protect forecasts and data {#uc4F}
{: .anchor}

**Use case narrative**: The framework protects data and forecasts according to user-selected conditions.

**Requirements**:

- The data sharing agreement terms are posted on the framework website.
- The framework provides user identification services (account management, password services).
- The framework records an owner, optionally under an anonymous pseudonym, for uploaded forecasts and data.
- Data owners can set permissions on data for viewing and downloading.
- Forecast owners can set permission on forecasts for viewing, downloading and attribution.

#### 4.G. Perform data quality checks {#uc4G}
{: .anchor}

**Use case narrative**: The framework applies data quality checks when a user uploads data, provides visuals and text reports of data quality check results, and offers download of user data with data quality flags.

**Requirements**:

- Time stamps are checked for time zone consistency, increasing order, gaps.
- Irradiance data are checked for missing values, non-physical values, periods of constant values, consistency of irradiance components.
- Power data are checked for missing values, non-physical values, periods of curtailment, periods of inverter clipping, misaligned trackers, incorrect system metadata.
- Data quality algorithms are coded and documented on the framework.



### 5. Archive data and forecasts {#archive}
{: .anchor}

#### 5.A. Provide historical data, forecasts and forecast errors {#uc5A}
{: .anchor}

**Use case narrative**: The framework provides archive service for data and forecasts.

**Requirements**:

- The framework provides an archive of reference irradiance and power data.
- The framework provides an archive of reference forecasts and forecast errors.
- Framework users can store forecasts and associated metadata on the framework up to account data limits.
- Framework users can store measurements and associated metadata on the framework up to account data limits.
- Framework users can share stored forecasts and data.
