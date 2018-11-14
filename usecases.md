---
layout: base
permalink: /usecases/
---
# Use Cases


{% include to_top.html %}
## Purpose and Summary {#purpose}
{: .anchor }
This document describes Solar Forecast Arbiter use cases and their associated requirements, and Solar Forecast Arbiter framework functional capabilities.

Use cases are grouped into two categories:

1. [Evaluate forecasts](#evaulatefx). These use cases anticipate a framework user whose primary interest is comparing one or more forecasts to data. Forecast quantities can include irradiance, power or load, and can vary in lead time, interval and horizon. The framework can evaluate deterministic forecasts, event forecasts and probabilistic forecasts.
2. [Analyze forecasts](#analyzefx). These use cases anticipate a framework user whose primary interest is investigating correlations between forecasts, forecast errors and other quantities.

Framework functional capabilities are grouped into three categories:

1. [Perform forecast evaluation in a standard manner](#evaluation)
2. [Administer the framework](#administer)
3. [Archive data and forecasts](#archive)

Additional documents will be created to refine topics including metrics, benchmark forecasts, data formats, data sharing, and legal considerations through continued stakeholder engagement.

## Contents  {#contents}
<div>
<ul>
  <li><a href="#definitions">Definitions</a></li>
    <ol>
      <li><a href="#forecastdef">Forecast and Forecast runs</a></li>
      <li><a href="#forecastparams">Forecast parameters</a></li>
      <li><a href="#users">Framework User and Framework Administrator</a></li>
    </ol>
  <li><a href="#usecases">Use Cases</a></li>
    <ol>
      <li><a href="#evaluatefx">Evaluate forecasts</a></li>
        <ol type="A">
          <li><a href="#uc1A">Compare a forecast to measurements</a></li>
          <li><a href="#uc1B">Compare a probabilistic forecast to measurements</a></li>
          <li><a href="#uc1C">Compare multiple forecasts to measurements</a></li>
          <li><a href="#uc1D">Compare forecasts to measurements for sites and aggregates</a></li>
          <li><a href="#uc1E">Evaluate an event forecast</a></li>
          <li><a href="#uc1F">Conduct forecast trial</a></li>
          <li><a href="#uc1G">Compare multiple forecast runs to measurements (stretch)</a></li>
        </ol>
      <li><a href="#analyzefx">Analyze forecasts</a></li>
        <ol type="A">
          <li><a href="#uc2A">Select subsets of forecasts and data</a></li>
          <li><a href="#uc2A">Identify events</a></li>
          <li><a href="#uc2A">Find forecasts errors with large impacts (stretch)</a></li>
        </ol>
      </ol>
  <li><a href="#capabilities">Framework functional capabilities</a></li>
    <ol start="3">
      <li><a href="#evaluation">Perform forecast evaluation in a standard manner</a></li>
        <ol type="A">
          <li><a href="#uc3A">Calculate forecast error metrics</a></li>
          <li><a href="#uc3B">Calculate forecast impacts (stretch)</a></li>
          <li><a href="#uc3C">Communicate probabilistic forecasts</a></li>
          <li><a href="#uc3D">Facilitate communication of forecasts and forecast metrics</a></li>
        </ol>
      <li><a href="#administer">Administer the framework</a></li>
        <ol type="A">
          <li><a href="#uc4A">Manage users and organizations</a></li>
          <li><a href="#uc4B">Manage data</a></li>
          <li><a href="#uc4C">Provide the framework API</a></li>
          <li><a href="#uc4D">Provide reference forecasts</a></li>
          <li><a href="#uc4E">Provide reference data</a></li>
          <li><a href="#uc4F">Protect forecasts and data</a></li>
          <li><a href="#uc4G">Perform data quality checks</a></li>
        </ol>
      <li><a href="#archive">Archive data and forecasts</a></li>
        <ol type="A">
          <li><a href="#uc5A">Provide historical data, forecasts and forecast errors</a></li>
        </ol>
    </ol>
</ul>
</div>

## Definitions  {#definitions}
{: .anchor}

### Forecast and Forecast runs {#forecastdef}
{: .anchor}

**Forecast run**. A _forecast run_ is a sequence of one or more (_Time_, _Value_) pairs issued at a particular time. _Time_ can label a moment in time or an interval of time, e.g., a _Time_ of 17:00 can label the hour-long interval from 17:00 to 18:00. _Value_ has a unit (e.g., MW) and a type (e.g., mean, 95th percentile) determined by the corresponding observation. An example forecast run for the average hourly power issued at 16:00 for the next three hours could be {(17:00, 5MW), (18:00, 10MW), (19:00, 7 MW)}. A forecast run is defined by the following parameters, illustrated by the example forecast run:

1. Start time (17:00)
2. Lead time to start of forecast (1 hour)
3. Interval duration (1 hour)
4. Number of intervals per submission (3)
5. Forecast issue frequency (once)
6. Value type (mean)
7. Interval label (start)

**Forecast**. A _forecast_ is a serially complete time series of (Time, Value) pairs spanning from a _start time_ to an _end time_. A single forecast run is a forecast. A forecast can also comprise the concatenation of a series of identically specified forecast runs with different issue times, as shown in the figures below. For example, three forecast runs (green) could be:

- {(13:00, 10MW)} issued at 12:00, and
- {(14:00, 7MW)} issued at 13:00, and
- {(15:00, 5MW)} issued at 14:00.

From these three runs, the user could upload an hour ahead, hour interval forecast of:

- {(13:00, 10MW), (14:00, 7MW), (15:00, 5MW)}

 ![timeline_concat_1h](/images/timeline_concat_1h.svg){: .usecase-figure}

The framework also supports the concatenation of submissions with more than one interval, so long as the intervals do not overlap. The example below shows how three different hour ahead, 15 minute interval, 1 hour duration forecast runs may be concatenated into a single forecast for evaluation.

 ![timeline_concat](/images/timeline_concat.svg){: .usecase-figure}

This concept also applies to the evaluation of day-ahead forecasts issued at a particular time of day. For example, hour average forecasts for next day as of 16:00 previous day can be represented by a concatenation of forecasts with start time of midnight, 8 hour lead time to start, 1 hour interval, 24 intervals per submission, and 1 day frequency.

For most use cases ([1.A](#uc1A)-[1.E](#uc1E)), the framework expects forecast providers to upload a _forecast_. For the Forecast Trial use case ([1.F](#uc1F)), the framework expects forecast providers to upload a series of _forecast runs_ that the framework can concatenate into a _forecast_ for evaluation.

A stretch goal is to support the use case of analyzing multiple forecast runs with the same valid times ([1.G](#uc1G)). For example, the user could upload each of the forecast runs specified above, and then use the framework to merge the forecast runs into a 0, 1, or 2 hour ahead forecast for evaluation. The figure below shows three forecasts runs (green) merged into two different evaluation forecasts (blue, red).

 ![timeline_merge](/images/timeline_merged.svg){: .usecase-figure}


### Forecast parameters {#forecastparams}
{: .anchor}

A _forecast_ is a piecewise-continuous time series of values parameterized by:

1. Start time
2. Lead time to start of forecast
3. Interval duration
4. Intervals per submission
5. Forecast issue frequency
6. Value type (e.g. mean, max, 95th percentile, instantaneous)
7. Interval label (start or end)

See the [Forecast and Forecast runs](#forecastdef) section above for examples.

### Framework User and Framework Administrator {#users}
{: .anchor}

A _framework user_ is an individual or organization that uses the capabilities of Solar Forecast Arbiter to evaluate and analyze forecasts. A framework user can be a _forecast provider_ (one who creates a forecast), a _forecast user_ (one using a forecast for a defined purpose), researchers, and others.

The _framework administrator_ operates Solar Forecast Arbiter, ensures data security and anonymity, establishes standards for forecast evaluation, and provides benchmark forecasts.



## Use cases  {#usecases}
{: .anchor}

A use case describes a sequence of actions taken by a framework user to achieve a goal. Use cases are grouped into two categories: Evaluate forecasts, and Analyze forecasts. From each use case a list of framework requirements is developed. A use case may adopt, expand, or modify the requirements of another use case.

### 1. Evaluate forecasts  {#evaulatefx}
{: .anchor}

#### 1.A. Compare a forecast to measurements {#uc1A}
{: .anchor}

**Use case narrative** : A framework user uploads a forecast or selects a benchmark forecast, uploads corresponding measured data or selects reference data, specifies filters, specifies temporal averaging, and selects metrics. The framework calculates metrics, provides a visual display of forecast performance and an evaluation report for download.

**Requirements** :

- User can upload measured data, select from previously uploaded measured data, or select a location/period with reference data ([4.E](#uc4E)).
  - If uploading data, user must define relevant metadata including location, data type, and units.
  - Data type can be irradiance, power, or net-load.
- User can upload a corresponding [forecast](#forecastdef) ([4.C](#uc4C)) or select corresponding benchmark forecast ([4.D](#uc4D)). The forecast value type must be deterministic.
- Framework applies data quality checks to uploaded data and forecasts ([4.G](#uc4G)).
- User can specify filters to exclude forecast or data points (a subset of (time, value) pairs), by time or by value ([2.A](#uc2A)).
- User can select among forecast performance metrics ([3.A](#uc3A)).
- Framework provides metric values and visuals of forecast performance ([3.A](#uc3A)).
- Framework provides a report for download ([3.D](#uc3D)).
- Framework protects forecasts and uploaded data as user-owned: user can specify other users and/or groups who can see/use the uploaded forecasts, data, or summary error statistics ([4.F](#uc4F)).

#### 1.B. Compare a probabilistic forecast to measurements {#uc1B}
{: .anchor}

**Use case narrative** : A framework user uploads a probabilistic forecast, uploads corresponding data or selects reference data, specifies filters, and selects metrics. The framework calculates probabilistic metrics and provides a visual display of probabilistic forecast performance.

**Requirements** :

- All requirements as listed for Use Case [1.A](#uc1A) with the following modifications.
- A forecast value must be an empirical probability distribution at each time point (a sequence of {quantile, value} or {Prob(X), X} pairs).
- User can select among probabilistic forecast performance metrics ([3.A](#uc3A)).
- Framework provides probabilistic metric values for comparison among forecasts ([3.A](#uc3A)), visual displays of probabilistic forecast performance, and a report for download ([3.D](#uc3D)).

#### 1.C. Compare multiple forecasts to measurements {#uc1C}
{: .anchor}

**Use case narrative** : Framework users upload forecasts, select benchmark forecasts, or invite other users to share forecasts. Framework users upload corresponding data or select reference data, specify data filters, specify temporal averaging, and select metrics. The framework calculates metrics and provides a visual display of forecast performance and forecast errors for download, and a visual display comparing the forecasts. The framework user can share results with other users.

**Requirements** :

- All requirements as listed for Use Case [1.A](#uc1A) or [1.B](#uc1B) for each forecast in the comparison.
- User can share forecast specifications (e.g., quantity, interval, horizon, averaging, lead times) with other framework users and invite other framework users to share forecasts for the comparison ([4.F](#uc4F)).
- Framework supports anonymous forecast comparison.
- Framework protects forecasts as specified by each forecast owner ([4.F](#uc4F)).
- Framework provides metric values for the comparison among forecasts ([3.A](#uc3A)), a visual display of comparison results, and a report for download ([3.D](#uc3D)).

#### 1.D. Compare forecasts to measurements for sites and aggregates {#uc1D}
{: .anchor}

**Use case narrative** : A framework administrator defines an aggregate of locations. A framework user uploads forecasts for locations in the aggregate and a forecast for the aggregation of locations. A framework user uploads corresponding data or selects reference data, specifies filters, specifies temporal averaging, and selects metrics. The forecasts and data may represent individual point sensors, power plants, or aggregated quantities. The framework calculates metrics and provides a visual display comparing the forecasts across scales.

**Requirements** :

- All requirements as listed for Use Case [1.A](#uc1A), [1.B](#uc1B), or [1.C](#uc1C), as appropriate.
- User uploads an aggregation of forecasts with weights specified by the framework ([4.C](#uc4C)).
- Framework computes observations, as specified.
- Framework provides metric values for the comparison among forecasts ([3.A](#uc3A)), a visual display of comparison results, and a report for download ([3.D](#uc3D)).

#### 1.E. Evaluate an event forecast {#uc1E}
{: .anchor}

**Use case narrative** : A framework user can analyze an event forecast.

**Requirements** :

- All requirements as listed by Use Case [1.A](#uc1A), [1.B](#uc1B), or [1.C](#uc1C), as appropriate.
- User can upload an event forecast, e.g., a time series of true/false values, or a time series of event occurrence likelihood ([4.C](#uc4C)).
- User can upload corresponding event data or connect to a saved event time series ([2.B](#uc2B)).
- User can select among event forecast performance metrics ([3.A](#uc3A)).
- Framework provides metric values and visuals of event forecast performance ([3.A](#uc3A)).
- Framework provides a report for user download ([3.D](#uc3D)).

#### 1.F. Conduct forecast trial {#uc1F}
{: .anchor}

**Use case narrative** : The framework administrator, in consultation with trial participants, defines trial period, locations, forecast quantities, time horizons, time resolutions, etc. of a forecast trial. The trial may be either retrospective or live, and may involve a test period followed by an evaluation period. Separate trials may be administered for multiple forecast parameters (e.g. hour ahead and day ahead forecast evaluations for the same set of locations).

**Requirements** :

- All requirements as listed for Use Case [1.C](#uc1C).
- Administrator, in consultation with trial participants, defines data sources, forecast run intervals/horizons, trial period, metrics, filters ([4.C](#uc4C)).
- Framework concatenates regularly posted forecast runs into a continuous forecast ([4.C](#uc4C)).
- Framework accepts and allows for download of streaming data ([4.C](#uc4C)).
- Framework generates intermediate reports during the trial ([3.D](#uc3D)).

#### 1.G. Compare multiple forecast runs to measurements (stretch) {#uc1G}
{: .anchor}

**Use case narrative** : A framework user uploads a sequence of forecast runs at a regular interval, uploads corresponding data or selects reference data, specifies filters, specifies temporal averaging, and selects metrics. The framework calculates metrics, provides a visual display of forecast performance and an evaluation report for download.

**Requirements** :

- All requirements as listed for Use Case [1.A](#uc1A), for each forecast run.
- Each [forecast run](#forecastdef) must be identically specified.
- Forecast runs are issued at a regular interval (e.g., every 6 hours).
- User can upload multiple forecast runs. Each forecast run must be:
  - A time series of uniform forecast intervals, duration, and value type (e.g. 5 minute interval, interval average forecasts through 24 hours from the start time)
- User can define forecast evaluation intervals, horizons, and temporal averaging.



### 2. Analyze forecasts {#analyzefx}
{: .anchor}

#### 2.A. Select subsets of forecasts and data {#uc2A}
{: .anchor}

**Use case narrative** : A framework user selects a subset of an uploaded forecast, and the corresponding data, based on one or more conditions, for detailed analysis.  The framework calculates metrics and provides a visual display of forecast performance.

**Requirements** :

- User can select a subset of points in a forecast or its corresponding data based on one or more conditions: forecast error (bias), forecast lead time, time of day, weather (irradiance, temperature, wind). Framework returns selected subsets from the forecast and corresponding data.
- User can select among forecast performance metrics ([3.A](#uc3A)).
- Framework applies data quality checks to uploaded data ([4.E](#uc4E)).
- Framework provides metric values and visuals of forecast performance ([3.A](#uc3A)).
- Framework provides a report for user download ([3.D](#uc3D)).

#### 2.B. Identify events {#uc2B}
{: .anchor}

**Use case narrative** : The framework assists a user to identify events in a forecast or in data.

**Requirements** :

- User can upload a forecast ([4.C](#uc4C)).
- User can upload data ([4.C](#uc4C)).
- Framework applies data quality checks to uploaded data ([4.E](#uc4E)).
- User can specify conditions (e.g., ramp rates) used to identify events occurring in a forecast or in data.
- Framework provides visual display of identified events ([3.D](#uc3D)).
- Framework provides a report for user download ([3.D](#uc3D)).
- User can save event data, i.e., a time series of true/false values.

#### 2.C. Find forecasts errors with large impacts (stretch) {#uc2C}
{: .anchor}

**Use case narrative** : A framework user can associate forecast errors with system impact, and can filter forecasts based on system impact.

**Requirements** :

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

**Use case narrative** : The framework provides a set of well-documented metrics which can be selected by a framework user for evaluating or analyzing forecasts. Metrics include, for example, statistics for forecast error, and cost estimated by a user-supplied $/MW-error.

**Requirements** :

- Metrics are documented on the framework website.
- Metrics are coded in the framework.
- Metrics can be selected by a framework user.
- Metrics are available for probabilistic forecasts.

#### 3.B. Calculate forecast error impacts (stretch) {#uc3B}
{: .anchor}

**Use case narrative** : The framework provides a set of well-documented functions to associate forecast error with system impact. System impact may include, for example, increase or decrease in reserve requirements.

**Requirements** :

- Functions for estimating system impact are documented on the framework website.
- Functions are coded in the framework.
- Function parameters can be selected by a framework user.

#### 3.C. Communicate probabilistic forecasts {#uc3C}
{: .anchor}

**Use case narrative** : The framework communicates probabilistic forecast information in a meaningful, well-documented manner.

**Requirements** :

- Quantities and terms used to describe and present probabilistic forecasts are documented on the framework website.
- Framework presents visuals for probabilistic forecasts.

#### 3.D. Facilitate communication of forecasts and forecast metrics {#uc3D}
{: .anchor}

**Use case narrative** : The framework aids a forecast provider to communicate forecast performance.

**Requirements** :

- The framework produces reports of forecast evaluation and analysis for user download.
- The framework website includes pages that aid in explaining forecasts and their use.
- Framework users can share forecasts, forecast evaluation reports, and data with other framework users.
- Framework protects forecasts and uploaded data as specified by the user.



### 4. Administer the framework {#administer}
{: .anchor}

#### 4.A. Manage users and organizations {#uc4A}
{: .anchor}

**Use case narrative** : The framework administrator can manage users and organizations.

**Requirements** :

- Administrator can associate or disassociate users with organizations.
- Administrator can enable data upload privileges based on email communication.
- Administrator can reset user passwords.

#### 4.B. Manage data {#uc4B}
{: .anchor}

**Use case narrative** : The framework administrator can manage data storage, and can delete data upon request or at the end of the DOE funding period.

**Requirements** :

- Framework administrator can assign data storage limits.
- Framework administrator can delete stored data.
- Users can delete user-owned data.

#### 4.C. Provide the framework API {#uc4C}
{: .anchor}

**Use case narrative** : The framework provides a documented API and appropriate services for client users.

**Requirements** :

- The framework's API is documented on the framework website.
- Users can interact with the framework via url requests.
- Users can request forecast evaluations via script (stretch).

#### 4.D. Provide reference forecasts {#uc4D}
{: .anchor}

**Use case narrative** : The framework provides a set of documented reference forecasts for irradiance and power, for various locations, at various intervals and horizons.

**Requirements** :

- The framework provides a reference irradiance forecast at hourly intervals out to 60 hours for CONUS.
- The framework provides a reference irradiance forecast at user-selected intervals (5 to 60 minutes) out to 24 hours, using smart persistence of user-uploaded data.
- The framework provides a reference forecast for air temperature and wind speed to accompany the reference irradiance forecasts.
- The framework provides a reference model for translating irradiance to power.
- The framework provides a reference forecast for power, using user-uploaded power and a persistence method.
- The framework can provide load and net load forecasts from user-uploaded data using persistence (stretch).
- Reference forecasts and forecast methods are documented on the framework website.

#### 4.E. Provide reference data {#uc4E}
{: .anchor}

**Use case narrative** : The framework provides reference weather and power data at selected locations.

**Requirements** :

- The framework provides reference irradiance data from a selection of stations e.g. SURFRAD stations.
- The framework provides reference power data from a selection of PV systems.
- The framework provides metadata for reference PV systems.

#### 4.F. Protect forecasts and data {#uc4F}
{: .anchor}

**Use case narrative** : The framework protects data and forecasts according to user-selected conditions.

**Requirements** :

- The data sharing agreement terms are posted on the framework website.
- The framework provides user identification services (account management, password services).
- The framework records an owner for uploaded forecasts and data.
- Data owners can set permissions on data for viewing and downloading.
- Forecast owners can set permission on forecasts for viewing, downloading and attribution.

#### 4.G. Perform data quality checks {#uc4G}
{: .anchor}

**Use case narrative** : The framework applies data quality checks when a user uploads data, provides visuals and text reports of data quality check results, and offers download of user data with data quality flags.

**Requirements** :

- Time stamps are checked for timezone consistency, increasing order, gaps.
- Irradiance data are checked for missing values, non-physical values, periods of constant values, consistency of irdiance components.
- Power data are checked for missing values, non-physical values, periods of curtailment, periods of inverter clipping, miligned trackers, incorrect system metadata.
- Data quality algorithms are coded and documented on the framework.



### 5. Archive data and forecasts {#archive}
{: .anchor}

#### 5.A. Provide historical data, forecasts and forecast errors {#uc5A}
{: .anchor}

**Use case narrative** : The framework provides archive service for data and forecasts.

**Requirements** :

- The framework provides an archive of reference irradiance and power data.
- The framework provides an archive of reference forecasts and forecast errors.
- Framework users can store forecasts and associated metadata on the framework up to account data limits.
- Framework users can store measurements and associated metadata on the framework up to account data limits.
- Framework users can share stored forecasts and data.
