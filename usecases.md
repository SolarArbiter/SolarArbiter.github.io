---
layout: base
permalink: /usecases/
---
# Use Cases

*We are currently asking stakeholders to provide feedback on the Solar Forecast Arbiter use cases. Please take just a couple of minutes to provide simple feedback using this [form](https://goo.gl/forms/F1qq08JppsKBMUtj2). Stakeholders may also markup this [word document](https://drive.google.com/open?id=18cL-sZnStsZzOzbeSV0hWmh06G3ESEpN) and email it to a team member or [info@solarforecastarbiter.org](mailto:info@solarforecastarbiter.org).*

{% include to_top.html %}
## Purpose and Summary {#purpose}
{: .anchor }
This document describes Solar Forecast Arbiter use cases and their associated requirements, and Solar Forecast Arbiter framework functional capabilities.

The Solar Forecast Arbiter is primarily designed to support the evaluation of solar forecasts that are useful for solar forecast users. It is not a general-purpose weather forecast analysis tool, though it may eventually be extended to incorporate wind power and load forecast analysis.

Use cases are grouped into two categories:

1. [Evaluate forecasts](#evaluatefx). These use cases anticipate a framework user whose primary interest is comparing one or more forecasts to data. Forecast quantities can include irradiance, power or net load, and can vary in lead time, interval and horizon. The framework can evaluate deterministic forecasts, event forecasts, and probabilistic forecasts.
2. [Analyze forecasts](#analyzefx). These use cases anticipate a framework user whose primary interest is investigating correlations between forecasts, forecast errors, and other quantities.

Framework functional capabilities are grouped into three categories:

1. [Perform forecast evaluation in a standard manner](#evaluation)
2. [Administer the framework](#administer)
3. [Archive data and forecasts](#archive)

Metrics, benchmark forecasts, data formats, data sharing policies, and legal considerations will be detailed in other documents.

## Contents  {#contents}
<div>
<ul>
  <li><a href="#definitions">Definitions</a></li>
    <ol>
      <li><a href="#forecastdef">Forecast evaluation timeseries, forecast runs, and forecast datapoints</a></li>
      <li><a href="#forecastattrs">Forecast evaluation timeseries attributes</a></li>
      <li><a href="#users">Framework user and framework administrator</a></li>
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
          <li><a href="#uc3E">Compute aggregate observations</a></li>
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

The precise definition of a *forecast* is often a source of confusion in the forecasting industry. Consider these statements that use the term *forecast*:

<ol type="A">
  <li>"The forecast for the next 48 hours is 5 MW, 10 MW, 7 MW..."</li>
  <li>"The hour ahead forecast this morning was 5 MW, 10 MW, 7 MW..."</li>
</ol>

In Statement A, the user refers to a series of expected values issued at a **single** point in time. In Statement B, the user refers to a series of expected values with the **same** lead time that are issued at **different** points in time.

An evaluation challenge arises if Statement A is extended to include a new 48 hour duration forecast every hour. In this scenario, many forecasts exist at each evaluation time. More information is needed to focus the analysis to a particular application.

Statement B suggests an alternative strategy: the forecast user or the forecast provider parses forecast data into a timeseries for evaluation according to her **application**. For example, from many 48 hour length forecasts, a timeseries of forecast values with lead times of 1 hour ahead could be compiled to evaluate forecasts that support participation in a particular market. Or, a timeseries of forecast values for each hour of the day ahead could be compiled from forecasts issued at the same time each day to evaluate forecasts input to a production cost model. In each case, the forecast under evaluation is a continuous, non-overlapping timeseries that can be compared to observations.

The Solar Forecast Arbiter is designed to analyze these user-supplied, continuous, non-overlapping timeseries. We refer to this as a *forecast evaluation timeseries*.

The Solar Forecast Arbiter provides a taxonomy to allow forecast users and forecast providers to clearly and completely describe each forecast evaluation timeseries. For most use cases, the user is required to consider the forecast application, parse the forecast data into a continuous, non-overlapping timeseries for evaluation, and provide the parsed data to the Solar Forecast Arbiter for analysis – not the individual forecast runs that went into the parsed forecast.

The sections below define and illustrate the key terms and concepts.


### Forecast evaluation timeseries, forecast runs, and forecast datapoints {#forecastdef}
{: .anchor}

**Forecast datapoint**. A *forecast datapoint* is a single (*Time*, *Value*) data pair. Time can label a moment in time or an interval of time, as defined by the interval type label. For example, a Time of 17:00 can label the hour-long interval beginning from 17:00 to 18:00 (period beginning label), 16:00 to 17:00 (period ending label) or instantaneously at 17:00 (instantaneous label). Value has a *quantity* (e.g., mean, 95th percentile) and *type* (e.g. power, GHI). The type defines the unit.

**Forecast run**. A _forecast run_ is a sequence of one or more *forecast datapoints* issued at the same time.  An example forecast run for the average hourly power at Power Plant X, issued at 16:00 for the next three hours, could be {(17:00, 5 MW), (18:00, 10 MW), (19:00, 7 MW)}. A forecast run is described by the following attributes (with the values relevant to this example in parentheses):

1.	Issue time (16:00)
2.	Lead time to start (1 hour)
3.	Interval duration (1 hour)
4.	Number of intervals per submission (3)
5.	Forecast issue frequency (3 hr)
6.	Interval label (start)
7.	Value type (mean)
8.	Variable (power)
9.	Site (Power Plant X)

**Forecast evaluation timeseries**. A _forecast evaluation timeseries_ is a complete series of (*forecast datapoints*) spanning from a _start time_ to an _end time_. For example, a single *forecast run* is a *forecast evaluation timeseries*. Typically, a *forecast evaluation timeseries* is the concatenation of a series of identically specified forecast runs with sequential issue times, as shown in the figure below. For example, three forecast runs (green) could be:

- {(13:00, 10MW)} issued at 12:00, and
- {(14:00, 7MW)} issued at 13:00, and
- {(15:00, 5MW)} issued at 14:00.

From these three runs, the user could upload an hour ahead, hour interval forecast of:

- {(13:00, 10MW), (14:00, 7MW), (15:00, 5MW)}

 ![timeline_concat_1h](/images/timeline_concat_1h.svg){: .usecase-figure}

The framework also supports *forecast evaluation timeseries* that are the concatenation of *forecast runs* with more than one interval, so long as the intervals do not overlap. The example below shows how three different hour-ahead, 15-minute interval, 1-hour duration *forecast runs* may be parsed and concatenated into a single forecast evaluation timeseries.

 ![timeline_concat](/images/timeline_concat.svg){: .usecase-figure}

This concept also applies to the evaluation of day-ahead forecasts issued at a particular time of day. For example, hour average forecasts for next day as of 16:00 previous day can be represented by a concatenation of forecasts with start time of midnight, 8-hour lead time to start, 1-hour interval, 24 intervals per submission, and 1 day frequency.

For most use cases ([1.A](#uc1A)-[1.E](#uc1E)), the framework expects forecast providers to upload a *forecast evaluation timeseries*. For the Forecast Trial use case ([1.F](#uc1F)), the Solar Forecast Arbiter expects forecast providers to regularly upload a _forecast runs_ that the Solar Forecast Arbiter can concatenate into a *forecast evaluation timeseries*.

A stretch goal is to support the use case of uploading and analyzing multiple forecast runs with the same valid times ([1.G](#uc1G)). For example, the user could upload each of the forecast runs specified above, and then use the framework to merge the forecast runs into a 0, 1, or 2 hour ahead forecast for evaluation. The figure below shows three forecasts runs (green) merged into two different evaluation forecasts (blue, red).

 ![timeline_merge](/images/timeline_merged.svg){: .usecase-figure}


### Forecast evaluation timeseries attributes {#forecastattrs}
{: .anchor}

The Solar Forecast Arbiter uses the set of attributes defined below to describe the characteristics of a forecast evaluation timeseries. This structure allows any type of forecast typically utilized in the solar energy field to be evaluated.

A *forecast evaluation timeseries* is a serially complete time series of values with the following attributes:

1.	Issue time - The time of day that a forecast is issued, e.g. 13:00. Multiple issue times are uniquely determined by any one issue time and forecast issue frequency.
2.	Lead time to start - The difference between each issue time and the start of the first forecast interval, e.g. 1 hour.
3.	Interval duration - The length of time that each data point represents, e.g. 5 minutes, 1 hour.
4.	Intervals per submission - The number of intervals in each forecast submission, e.g. 12.
5.	Forecast issue frequency - The frequency at which new forecasts are issued, e.g. 1 hour, 6 hours, 1 day.
6.	Interval label - Indicates if a time labels the start or the end of an interval, or indicates an instantaneous value.
7.	Value type - The type of the data in the forecast, e.g. mean, max, 95th percentile.
8.	Variable - The variable in the forecast, e.g. power, GHI, DNI. Each variable is associated with a standard unit.
9.	Site - The predefined site that the forecast is for, e.g. Power Plant X or Aggregate Y.

A forecast must be associated with a pre-defined site. The site, not the forecast, defines geographic location and the variable determines the units.


### Framework user and framework administrator {#users}
{: .anchor}

A _framework user_ is an individual or organization that uses the capabilities of Solar Forecast Arbiter to evaluate and analyze forecasts. A framework user can be a _forecast provider_ (one who creates a forecast), a _forecast user_ (one using a forecast for a defined purpose), researchers, and others.

The _framework administrator_ operates Solar Forecast Arbiter, ensures data security and anonymity, establishes standards for forecast evaluation, and provides benchmark forecasts.



## Use cases  {#usecases}
{: .anchor}

A use case describes a sequence of actions to achieve a goal. Use cases are grouped into two categories: [Evaluate forecasts](#evaluatefx), and [Analyze forecasts](#analyzefx). From each use case a list of framework requirements is developed. To reduce repeating requirements, a use case may adopt, expand, or modify the requirements of another use case.

**In this section, for brevity, a *forecast* refers to the *[forecast evaluation timeseries](#forecastdef)* defined above.**

### 1. Evaluate forecasts  {#evaluatefx}
{: .anchor}

#### 1.A. Compare a forecast to measurements {#uc1A}
{: .anchor}

**Use case narrative**: A framework user uploads a forecast or selects a benchmark forecast, uploads corresponding measured data or selects reference data, specifies filters, specifies temporal averaging, and selects metrics. The framework calculates metrics, provides a visual display of forecast performance and an evaluation report for download.

**Requirements**:

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

**Use case narrative**: A framework user uploads a probabilistic forecast, uploads corresponding data or selects reference data, specifies filters, and selects metrics. The framework calculates probabilistic metrics and provides a visual display of probabilistic forecast performance.

**Requirements**:

- All requirements as listed for Use Case [1.A](#uc1A) with the following modifications.
- A forecast value must be an empirical probability distribution at each time point (a sequence of {quantile, value} or {Prob(X), X} pairs).
- User can select among probabilistic forecast performance metrics ([3.A](#uc3A)).
- Framework provides probabilistic metric values for comparison among forecasts ([3.A](#uc3A)), visual displays of probabilistic forecast performance, and a report for download ([3.D](#uc3D)).

#### 1.C. Compare multiple forecasts to measurements {#uc1C}
{: .anchor}

**Use case narrative**: Framework users upload forecasts, select benchmark forecasts, or invite other users to share forecasts. Framework users upload corresponding data or select reference data, specify data filters, specify temporal averaging, and select metrics. The framework calculates metrics and provides a visual display of forecast performance and forecast errors for download, and a visual display comparing the forecasts. The framework user can share results with other users.

**Requirements**:

- All requirements as listed for Use Case [1.A](#uc1A) or [1.B](#uc1B) for each forecast in the comparison.
- User can share forecast specifications (e.g., quantity, interval, horizon, averaging, lead times) with other framework users and invite other framework users to share forecasts for the comparison ([4.F](#uc4F)).
- Framework supports anonymous forecast comparison ([4.F](#uc4F)).
- Framework protects forecasts as specified by each forecast owner ([4.F](#uc4F)).
- Framework provides metric values for the comparison among forecasts ([3.A](#uc3A)), a visual display of comparison results, and a report for download ([3.D](#uc3D)).

#### 1.D. Compare forecasts to measurements for sites and aggregates {#uc1D}
{: .anchor}

**Use case narrative**: A framework administrator defines an aggregate of locations. A framework user uploads forecasts for locations in the aggregate and a forecast for the aggregation of locations. A framework user uploads corresponding data or selects reference data, specifies filters, specifies temporal averaging, and selects metrics. The forecasts and data may represent individual point sensors, power plants, or aggregated quantities. The framework calculates metrics and provides a visual display comparing the forecasts across scales.

**Requirements**:

- All requirements as listed for Use Case [1.A](#uc1A), [1.B](#uc1B), or [1.C](#uc1C), as appropriate.
- User uploads an aggregation of forecasts with weights specified by the framework ([4.C](#uc4C)).
- Framework computes observations, as specified ([3.E](#uc3E)).
- Framework provides metric values for the comparison among forecasts ([3.A](#uc3A)), a visual display of comparison results, and a report for download ([3.D](#uc3D)).

#### 1.E. Evaluate an event forecast {#uc1E}
{: .anchor}

**Use case narrative**: A framework user can analyze an event forecast.

**Requirements**:

- All requirements as listed by Use Case [1.A](#uc1A), [1.B](#uc1B), or [1.C](#uc1C), as appropriate.
- User can upload an event forecast, e.g., a time series of true/false values, or a time series of event occurrence likelihood ([4.C](#uc4C)).
- User can upload corresponding event data or connect to a saved event time series ([2.B](#uc2B)).
- User can select among event forecast performance metrics ([3.A](#uc3A)).
- Framework provides metric values and visuals of event forecast performance ([3.A](#uc3A)).
- Framework provides a report for user download ([3.D](#uc3D)).

#### 1.F. Conduct forecast trial {#uc1F}
{: .anchor}

**Use case narrative**: The framework administrator, in consultation with trial participants, defines trial period, locations, forecast quantities, time horizons, time resolutions, etc. of a forecast trial. The trial may be either retrospective or live, and may involve a test period followed by an evaluation period. Separate trials may be administered for multiple forecast parameters (e.g. hour ahead and day ahead forecast evaluations for the same set of locations).

**Requirements**:

- All requirements as listed for Use Case [1.C](#uc1C).
- Administrator, in consultation with trial participants, defines data sources, forecast run intervals/horizons, trial period, metrics, filters ([4.C](#uc4C)).
- Framework concatenates regularly posted forecast runs into a continuous forecast ([4.C](#uc4C)).
- Framework accepts and allows for download of streaming data ([4.C](#uc4C)).
- Framework generates intermediate reports during the trial ([3.D](#uc3D)).

#### 1.G. Compare multiple forecast runs to measurements (stretch) {#uc1G}
{: .anchor}

**Use case narrative**: A framework user uploads a sequence of forecast runs at a regular interval, uploads corresponding data or selects reference data, specifies filters, specifies temporal averaging, and selects metrics. The framework calculates metrics, provides a visual display of forecast performance and an evaluation report for download.

**Requirements**:

- All requirements as listed for Use Case [1.A](#uc1A), for each forecast run.
- Each [forecast run](#forecastdef) must be identically specified.
- Forecast runs are issued at a regular interval (e.g., every 6 hours).
- User can upload multiple forecast runs. Each forecast run must be:
  - A time series of uniform forecast intervals, duration, and value type (e.g. 5 minute interval, interval average forecasts through 24 hours from the start time)
- User can define forecast evaluation intervals, horizons, and temporal averaging.



### 2. Analyze forecasts {#analyzefx}
{: .anchor}

#### 2.A. Analyze subsets of forecasts and data {#uc2A}
{: .anchor}

**Use case narrative**: A framework user selects a subset of an uploaded forecast, and the corresponding data, based on one or more conditions, for detailed analysis. The framework calculates metrics and provides a visual display of forecast performance.

**Requirements**:

- User can select a subset of points in a forecast or its corresponding data based on one or more conditions: forecast error (bias), forecast lead time, time of day, weather (irradiance, temperature, wind). Framework returns selected subsets from the forecast and corresponding data.
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
- User can specify conditions (e.g., ramp rates) used to identify events occurring in a forecast or in data.
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
- Users can interact with the framework via url requests.
- Users can request forecast evaluations via script (stretch).

#### 4.D. Provide reference forecasts {#uc4D}
{: .anchor}

**Use case narrative**: The framework provides a set of documented reference forecasts for irradiance and power, for various locations, at various intervals and horizons.

**Requirements**:

- The framework provides a reference irradiance forecast at hourly intervals out to 60 hours for CONUS.
- The framework provides a reference irradiance forecast at user-selected intervals (5 to 60 minutes) out to 24 hours, using smart persistence of user-uploaded data.
- The framework provides a reference forecast for air temperature and wind speed to accompany the reference irradiance forecasts.
- The framework provides a reference model for translating irradiance to power.
- The framework provides a reference forecast for power, using user-uploaded power and a persistence method.
- The framework can provide load and net load forecasts from user-uploaded data using persistence (stretch).
- Reference forecasts and forecast methods are documented on the framework website.

#### 4.E. Provide reference data {#uc4E}
{: .anchor}

**Use case narrative**: The framework provides reference weather and power data at selected locations.

**Requirements**:

- The framework provides reference irradiance data from a selection of stations e.g. SURFRAD stations.
- The framework provides reference power data from a selection of PV systems.
- The framework provides metadata for reference PV systems.

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

- Time stamps are checked for timezone consistency, increasing order, gaps.
- Irradiance data are checked for missing values, non-physical values, periods of constant values, consistency of irdiance components.
- Power data are checked for missing values, non-physical values, periods of curtailment, periods of inverter clipping, miligned trackers, incorrect system metadata.
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
