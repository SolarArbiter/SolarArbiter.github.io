---
layout: base
permalink: /usecases/
sidebar: usecase_sidebar.html
title: Use Cases
---

# Use Cases
{: .anchor }


{% include to_top.html %}
## Purpose and Summary {#purpose}
{: .anchor }
This document describes Solar Forecast Arbiter use cases and their associated requirements, and Solar Forecast Arbiter framework functional capabilities. A use case describes a sequence of actions to achieve a goal. To reduce repeating requirements, a use case may adopt, expand, or modify the requirements of another use case.

Use cases are grouped into two categories:

1. [Evaluate forecasts](#evaluatefx). These use cases anticipate a framework user whose primary interest is comparing one or more forecasts to observation data. Forecast quantities can include irradiance, power or net load, and can vary in lead time, interval and horizon. The framework can evaluate deterministic forecasts, event forecasts, and probabilistic forecasts.
2. [Analyze forecasts](#analyzefx). These use cases anticipate a framework user whose primary interest is investigating relationships between forecasts, forecast errors, and other quantities. Examples might include the spread between probabilistic forecasts, the standard deviation of a forecast, or the hit rate of forecasting a specific event (like a large change in power).

Framework functional capabilities are grouped into three additional categories:

{:start="3"}
1. [Perform forecast evaluation in a standard manner](#evaluation)
1. [Administer the framework](#administer)
1. [Archive data and forecasts](#archive)

**For brevity, a *forecast* refers to the *[forecast evaluation time series](/definitions/#forecastevalts)* defined in the [Definitions section](/definitions/).**

Metrics, benchmark forecasts, data formats, data sharing policies, and legal considerations will be detailed in other documents.

The Solar Forecast Arbiter is primarily designed to support the evaluation of solar forecasts that are useful for solar forecast users. It is not a general-purpose weather forecast analysis tool, though it may eventually be extended to incorporate wind power and load forecast analysis.

## Use cases  {#usecases}

### 1. Evaluate forecasts  {#evaluatefx}
{: .anchor}

#### 1.A. Compare a forecast to measurements {#uc1A}
{: .anchor}

**Use case narrative**: A framework user uploads a forecast or selects a benchmark forecast for a single location, uploads corresponding measured data or selects reference data, specifies filters, specifies temporal averaging, and selects metrics. The framework calculates metrics, provides a visual display of forecast performance and an evaluation report for download.

**Requirements**:

- User can upload measured data, select from previously uploaded measured data, or select a location/period with reference data ([4.E](#uc4E)).
  - If uploading data, user must define relevant metadata including location, data type, and units.
- User can upload a corresponding [forecast](/definitions/#forecastrun) ([4.C](#uc4C)) or select corresponding benchmark forecast ([4.D](#uc4D)). The forecast must be single-valued (e.g. mean or 95th percentile) at each time.
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

**Example 1**: An electric utility (the Utility) uses an in-house forecast model to predict the power generation of its fleet of solar photovoltaic (PV) power plants. The Utility is interested in replacing or supplementing its in-house forecast model with a commercially-available forecast, and therefore would like to evaluate the operational performance of commercial forecast providers. The Utility and the Framework Administrator announce the opportunity to Forecast Providers A-F. The Utility may announce its intention to contract with one or more Forecast Providers at the conclusion of the trial, but this is outside the scope of the Solar Forecast Arbiter.

The Utility, Administrator, and Providers discuss the many possible forecasts that could be evaluated and determine that two trials will be conducted to support particular business needs. Both trials will evaluate deterministic forecasts of power generated from the Utility's PV plants. Trial 1 will evaluate 1-hour ahead, 1-hour interval average forecasts that needs to be submitted at the prior hour. Trial 2 will evaluate day-ahead, 1-hour interval average forecasts that are issued once per day by 10:00 on the prior day and forecast for 00:00 to 23:00 for the next day (a lead time of 14 hours). The full forecast evaluation time series attributes are defined for each trial. For both trials, the start date is Jan 1, 2020, the end date is March 31, 2020, the evaluation metrics are average hourly MAE and RMSE, and missing forecasts will be assumed to be 0. Trial 1 will include a persistence benchmark, and Trial 2 will include a benchmark based on transparent processing of the NOAA NAM model, with solar irradiance from the NAM model transformed to power using pvlib.

Quality of the observation data provided by the Utility are also discussed and it is agreed that if nighttime hours will be ignored, which the Administrator will set the when performing the reporting on the metrics. In addition, if the observation data is identified to have quality issues for any periods, those values will be flagged in the data either on upload using the quality flag input or by the Administrator and any metric reports will be recalculated.

The Utility creates the Sites and Observations for the chosen PV plants, uploads 12 months of training data, and shares the data with Providers A-F. Providers A-F download the training data and create their models. An anonymous user is created for each Provider by the Administrator, which helps ensure an unbiased evaluation of the forecasts by masking the identity of the Providers from the Utility and each other. The Providers are granted a debugging period prior to the official start of the trial, where they can test that their forecast generation and submission processes are working properly. Then the trial starts officially and the Providers submit forecasts separately to the two trials for the duration of the evaluation period. Missing forecasts are penalized according to predefined rules. At the conclusion of the trials, reports are automatically generated for all participants.

Based on the results of the trial, the Utility can request discussions with all or a subset of the anonymized Forecast Providers. The Administrator notifies the selected Providers to contact the Utility for follow-on discussions.

**Example 2**: Similar to Example 1, except the Utility wishes to evaluate probabilistic forecasts instead of deterministic. The same general process applies, with the key differences being (1) the Forecast Providers submit probabilistic forecasts for predefined probabilities, e.g., 5th, 10th, ..., 95th percentiles, and (2) the forecasts are evaluated using probabilistic forecast error metrics, e.g., CRPS.

**Example 3**: Similar to Example 1, except the Utility wishes to evaluate sub-hourly time resolution forecasts, e.g., 1-hour ahead, 15-minute interval average forecasts instead of 1-hour ahead, 1-hour interval average forecasts. The same general process applies, with the key differences being (1) the Utility providers Observation data as 15-minute interval averages instead of 1-hour and (2) the Forecast Providers submit four 15-minute interval forecast values per hour instead of one 1-hour interval. Note that the Solar Forecast Arbiter can handle resampling Observation data and therefore the Utility could provide, e.g., 1-minute interval averages, with the Solar Forecast Arbiter then automatically resampling the 1-minute data to 15-minute when evaluating the forecasts.


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
- Each [forecast run](/definitions/#forecastrun) must be identically specified.
- Forecast runs are issued at a regular interval (e.g., every 6 hours).
- User can upload multiple overlapping forecast runs. Each forecast run can have a different issue time, but must have the same forecast interval (duration and label), forecast length and interval value type (e.g. 5-minute interval, 5-minute interval-ending label, 24 hours in length, interval average power forecast).
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
