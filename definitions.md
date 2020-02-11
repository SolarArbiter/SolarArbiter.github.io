---
layout: base
permalink: /definitions/
sidebar: definition_sidebar.html
title: Forecast Definitions
---

# Definitions  {#definitions}
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


## Forecast data point {#forecastdatapoint}
{: .anchor}

A *forecast data point* is a single (*time*, *value*) data pair. Time can label a moment in time or an interval of time, as defined by the *interval label*. For example, a time of 17:00 can label the 1-hour *interval length* period from 17:00 to 18:00 (*beginning* label), 16:00 to 17:00 (*ending* label) or instantaneously at 17:00 (*instantaneous* label). Value has a *interval value type* (e.g., mean, minimum) and *variable* (e.g. power, GHI). The variable defines the unit.


## Forecast run {#forecastrun}
{: .anchor}

A _forecast run_ is a sequence of one or more *forecast data points* issued at the same *issue time*. The time between the issue time and the first forecast data point time is the *lead time to start*. The *run length* is the time between the first forecast data point and the last forecast data point.

Most forecast runs in the Solar Forecast Arbiter are only as long as the predetermined evaluation scenario requires. For example, evaluations of forecasts with 15-minute interval, 1-hour length require a series of forecast runs that each contain only 4 forecast data points. Forecast providers often create runs that are longer than a particular Solar Forecast Arbiter evaluation scenario requires. Typically, forecast providers must parse these forecast runs into a *forecast evaluation time series* (discussed next).

Individual forecast runs are not archived or searchable except under the stretch goal [1.G. Compare multiple overlapping forecast runs to measurements](/usecases/#uc1G).


## Forecast evaluation time series {#forecastevalts}
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

For most use cases ([1.A](/usecases/#uc1A)-[1.E](/usecases/#uc1E)), the Solar Forecast Arbiter expects forecast providers to upload a *forecast evaluation time series*. For the Forecast Trial use case ([1.F](/usecases/#uc1F)), the Solar Forecast Arbiter expects forecast providers to regularly upload a _forecast run_ that the Solar Forecast Arbiter can append to a *forecast evaluation time series*. For some forecast trials, the Solar Forecast Arbiter will allow the upload of a forecast run that is longer than the *run length / issue frequency* attribute. This behavior is analogous to a forecast user falling back on an older forecast if a new forecast is not submitted on time. Some applications may not support this flexibility (e.g. a market with strict data formats) and therefore the Solar Forecast Arbiter will reject forecast runs that are longer than *run length / issue frequency*. The setting is determined before the trial starts.

A stretch goal is to support the use case of uploading and analyzing multiple forecast runs, optionally with the same valid times ([1.G](/usecases/#uc1G)). For example, the user could upload a new 24-hour length forecast that is issued each hour of the day. Later, the user could then use the framework to merge the forecast runs into a 0-, 1-, or 2-hour ahead forecast for evaluation. Figure 3 shows three forecasts runs (green) merged into two different evaluation forecasts (blue, red).

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
6. *Interval value type* - The type of the data in each interval of the forecast, e.g. mean, maximum, median.
7. *Variable* - The variable in the forecast, e.g. power, GHI, DNI. Each variable is associated with a standard unit.
8. *Site* - The predefined site that the forecast is for, e.g. Power Plant X or Aggregate Y.

A forecast must be associated with a pre-defined site. The site, not the forecast, defines geographic location and time zone. The variable determines the content of the forecast evaluation time series.

The table below shows the attributes for three different examples. We assume all intervals are labeled with the interval beginning time in these examples.

* Forecast User A requires hourly forecasts of average GHI at Sensor X located in the America/Denver time zone. The forecasts are to have 5-minute intervals and be updated 75-minute ahead of the hour.

* Forecast User B requires day ahead forecasts of hourly average power at Power Plant Y issued at 13:00 each day in the Etc/GMT+7 time zone.

* Forecast User C requires intraday forecasts for the minimum power in each forecast interval for Aggregate Z specified in the America/Phoenix time zone. The forecasts are to be issued every 3 hours with 15-minute interval length and 3-hour forecast length.

| Attribute | User A | User B | User C |
|-----------|:------:|:------:|:------:|
| Issue time of day | 00:45 | 13:00 | 00:00 |
| Lead time to start | 75 minutes | 11 hours | 0 minutes |
| Interval length | 5 minutes | 1 hour | 15 minutes |
| Run length / issue freq. | 1 hour | 24 hours | 3 hours |
| Interval label | Beginning | Beginning | Beginning |
| Interval value type | Mean | Mean | Minimum |
| Variable | GHI (W/m2) | Power (MW) | Power (MW) |
| Site | Sensor X (America/Denver) | Power Plant Y (Etc/GMT+7) | Aggregate Z (America/Phoenix) |


### Probabilistic forecasts {#probforecastdef}
{: .anchor}

The Solar Forecast Arbiter quantifies probabilistic forecasts using cumulative
distribution functions (CDFs). A CDF is represented here as a sequence of
(*variable value*, *percentile*) pairs, where percentiles range from 0 to 100.

A probabilistic forecast is defined by fixing a set of values for either the
variable being forecast, or the percentiles being forecast. For each value in
the set, a separate [forecast evaluation time series](#forecastattrs) is
uploaded, each [forecast data point](#forecastdatapoint) of which comprises one
(variable value, percentile) pair of the CDF at that point in time. Therefore,
each [forecast evaluation time series](#forecastattrs) describes (variable
value, percentile) points at multiple times while holding either value or
percentile constant.  At a point in time the CDF is represented by the
collection of (variable value, percentile) pairs across the set of [forecast
evaluation time series](#forecastattrs).

Consider a few simple examples. A probabilistic forecast may be the probability
that generation is less than 10 MW at each point in time. This probabilistic
forecast consists of a single [forecast evaluation time series](#forecastattrs),
which in turn contains a single number (the probability) at each [forecast data
point](#forecastdatapoint). Another probabilistic forecast may quantify the
generation that corresponds to the 50th percentile of a CDF, i.e., the median
generation value. Here, too, the probabilistic forecast is a single [forecast
evaluation time series](#forecastattrs) containing one number (the generation)
at each [forecast data point](#forecastdatapoint). These two probabilistic
forecasts can be summarized as:

| Case | Constant value | Forecast type |
|------|:--------------:|:-------------:|
| Prob(Power < 10 MW) | Variable (Power) = 10 MW | Percentile |
| p50 Power | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Percentile = 50 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Variable (Power) |

Probabilistic forecasts can also be a group of [forecast evaluation time
series](#forecastattrs) each describing a different point on the CDF. For
example, a user may be interested in the probability that power is less than
each of a range of power levels. In this case, one [forecast evaluation time
series](#forecastattrs) is made for each power level. The group of [forecast
evaluation time series](#forecastattrs) is specified by fixing *constant values*
along the *x* axis of the CDF and the forecasts are percentiles:

| Case | Constant value | Forecast type |
|------|:--------------:|:-------------:|
| Prob(Power < 1 MW) | Variable (Power) = 1 MW | Percentile |
| Prob(Power < 10 MW) | Variable (Power) = 10 MW | Percentile |
| Prob(Power < 20 MW) | Variable (Power) = 20 MW | Percentile |
| Prob(Power < 30 MW) | Variable (Power) = 30 MW | Percentile |
| Prob(Power < 40 MW) | Variable (Power) = 40 MW | Percentile |
| Prob(Power < 50 MW) | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Variable (Power) = 50 MW&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Percentile |

Or, a user may be interested in the power at a number of percentiles. In this
case, the group of [forecast evaluation time series](#forecastattrs) is specified
by *constant values* along the *y* axis of the CDF and the forecasts are powers:

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
