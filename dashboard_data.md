---
layout: dashboard_data
permalink: /documentation/dashboard/working-with-data
---

Working With Data
=================
{: .anchor}

Please see the [data model documentation](/datamodel/) for more details on how
the Solar Forecast Arbiter organizes metadata (Sites, Observations, and
Forecasts) and time series data.

Create New Site
---------------
{: .anchor}

1. Navigate to sites listing page using **Sites** link in the left
   sidebar. At the top of the Site listing click **Create new Site**.
<img class="my-3" src="/images/SitesListing.png"/>

2. Enter the metadata for your Site. Selecting a site type of
   **Power Plant** will prompt you for additional fields.

   - *Weather station site creation form*
   <img class="my-3" src="/images/SiteForm.png"/>

   - *Power plant site creation form*
   <img class="my-3" src="/images/plant_site_form.png"/>

3. After submission, you will be redirected to a Site
   page which displays the new Site's metadata and allows you
   to create associated Observations and Forecasts (see
   [Create New Observation or Forecast](#create-new-observation-or-forecast)).

   *Power Plant Site Page*
   <img class="my-3" src="/images/plant_site.png"/>


Create New Aggregate
--------------------
{: .anchor}

Aggregates are created by first defining metadata for the aggregate, then
associating existing observations with it. The aggregate metadata determines
how aggregation will be performed and the characteristics of the resulting
timeseries data.


1. Navigate to the aggregates listing page using the **Aggregates** link in
   the left sidebar. At the top of the listing, click **Create new Aggregate**.

   <img class="my-3" src="/images/aggregate_listing.png"/>

2. Enter the metadata for your Aggregate. Observations added to the aggregate
   must have the same variable as the aggregate and an interval length less
   than or equal to that of the aggregate.

   <img class="my-3" src="/images/aggregate_form.png"/>

3. After submission, you will be redirected to an Aggregate page which displays
   the observations that make up the aggregate (see 
   [Add Observations to an Aggregate](#add-observations-to-an-aggregate)).

   <img class="my-3" src="/images/aggregate_page_no_obs.png"/>


### Add Observations to an Aggregate
{: .anchor}

Observations are included in an aggregate between an *Effective From* and
an *Effective Until* date defined by the user. Note that observations are
expected to contain all values in their effective range. Any values missing
from an observation during computation will cause a failure. To avoid this
failure, users should submit `NaN`s where data is missing for their
observations.

Observations may be added to an Aggregate by following the steps below.
Observations must be defined before they can be added to an aggregate (see 
[Create New Observation](#create-new-observation)). 

1. Navigate to the Aggregate listing page using the **Aggregates** link in
   the left sidebar. Select the Aggregate to add observations to. Click the
   **Add Observation** button.

2. Enter an *Effective From* date. This will determine the start of the period
   for which the observations should be considered part of the aggregate. Check
   the boxes for each observation to be included in the aggregate. Note that to
   add observations for different time periods, you will need to repeat this
   process with a different *Effective From* date.
   

   <img class="my-3" src="/images/aggregate_observation_form.png"/>


### Remove an Observation from an Aggregate
{: .anchor}

Observations are removed from an aggregate by setting their *Effective Until* date.
Aggregate values will only contain data from constituent observations between
their *Effective From* and *Effective Until* dates.

1. Navigate to the Aggregate listing page using the **Aggregates** link in
   the left sidebar. Select the Aggregate to remove observations from.

2. On the aggregate page, locate the observation to remove in the observations table.
   Click on the **Set Effective Until** link for the observation to remove.

   <img class="my-3" src="/images/aggregate_page_with_obs.png"/>

3. Enter the *Effective Until* date for the observation. This will determine the end
   of the period for which the observations should be considered part of the aggregate.
   To remove it entirely, set an *Effective until* earlier than the *Effective from*.

   <img class="my-3" src="/images/aggregate_observation_effective_until_form.png"/>



Create New Observation or Forecast
----------------------------------
{: .anchor}

To create an Observation or Forecast, an associated site must already exist (see [Create New Site](#create-new-site)).

### Create New Observation
{: .anchor}

1.  Navigate to the Site listing page using the **Sites** link in the left
	sidebar. Select the site for which you are adding an Observation.

2.  Click the **Create new Observation** button on the Site page.
  <img class="my-3" src="/images/weather_site.png"/>

3.  Enter metadata for your Observation. On submission, you will be redirected
    to an Observation page which displays the new Observation metadata and a
    link to add Observation data (see [Upload Data](#upload-observation-data)).
- *Observation form*
<img class="my-3" src="/images/weather_obs.png"/>
- *Created Observation page*
<img class="my-3" src="/images/observation.png"/>

### Create New Forecast
{: .anchor}

Forecasts can be created for either a Site or an Aggregate.

1.  Navigate to the sites or aggregates page using the sidebar, then select the
    site or aggregate for which you are adding a Forecast.

2.  On the site or aggregate page, click the **Create new Forecast** button.
    <img class="my-3" src="/images/plant_site.png"/>

3.  Enter metadata for your Forecast. On submission, you will be redirected
    to a Forecast page which displays the new Forecast metadata and a
    link to add Forecast data (see [Upload Data](#upload-forecast-data)).
- *Forecast form*
<img class="my-3" src="/images/forecast_form.png"/>
- *Created Forecast page*
<img class="my-e" src="/images/forecast.png"/>


Upload data
-----------
{: .anchor}

To upload data, an associated Site and Observation or Forecast object
must already exist (see [Create New Site](#create-New-site) or
[Create New Observation or Forecast](#create-new-observation-or-forecast)).
The instructions here will describe the process of
uploading data using the dashboard.
Uploading data may be automated using the API, see
[https://api.solarforecastarbiter.org/](https://api.solarforecastarbiter.org/)
for detailed documentation.

### Upload Observation Data
{: .anchor}

1.  From Sites listing page, click on a site.

2.  Click **Observations** to find the Observations listing for that site.

3.  Select an Observation. Click **Upload Data** on the Observation page.
<img class="my-3" src="/images/observation.png"/>

4.  Select the file type, this will display an example of the expected file
format. Click **Choose File** and select the data file to upload.

	-  CSV format
	<img class="my-3" src="/images/obs_csv_upload.png"/>
	- JSON format
	<img class="my-3" src="/images/obs_json_upload.png"/>

### Upload Forecast Data
{: .anchor}

1.  From Sites listing page, click on a site.

2.  Click **Forecast** to find the Forecasts listing for that site.

3.  Select a Forecast. Click **Upload Data** on the Forecast page.
<img class="my-3" src="/images/forecast.png"/>

4.  Select the file type, this will display an example of the expected file
format. Click **Choose File** and select the data file to upload.

	- CSV format
	<img class="my-3" src="/images/fx_csv_upload.png"/>
	- JSON format
	<img class="my-3" src="/images/fx_json_upload.png"/>


Download Data
-------------
{: .anchor}

The instructions here will describe the process of
downloading data using the dashboard.
Users may also utilize the API to download data. See the
[API documentation](https://api.solarforecastarbiter.org/)
for details.

### Download Observation data
{: .anchor}

1.  From Sites listing page, click on a site.

2.  Click **Observations** to find the Observations listing for that site.

3.  Select an Observation. Click **Download Data** on the Observation page.
    <img class="my-3" src="/images/observation.png"/>

4.  Specify a date range, timezone and format, and click download.

	<img class="my-3" src="/images/obs_download.png">

### Download Forecast data
{: .anchor}

1.  From Sites listing page, click on a site.

2.  Click **Forecasts** to find the Observations listing for that site.

3.  Select a Forecast. Click **Download Data** on the Forecast page.
	<img class="my-3" src="/images/forecast.png"/>

4.  Specify a date range, timezone and format, and click download.

	<img class="my-3" src="/images/fx_download.png">

<div class="my-3"></div>

### Create New Report
{: .anchor}

1.  Use the **Reports** link on the left sidebar to view the reports listing page.
    Click the **Create new Report** link.
    <img class="my-3" src="/images/reports.png"/>

2.  Enter the report name and a start and end for the period to analyze.
    To pairs of Observations and Forecasts, start by selecting a Site. The forecast
    field will populate with a list of forecasts located at the site. Selecting a
    forecast will populate the observation field with observations field with
    observations that match the forecast's site and variable. Click the 
    **Add Forecast, Observation pair** button. Multiple Pairs can be added by repeating
    this process. Pairs can be removed by clicking the 'x' on the right side of the
    forecast & observation table.

     <img class="my-3" src="/images/report_form.png"/>

    After clicking submit, you will be returned to the report listing page where
    you will see the newly created report with a status of **pending**. The Arbiter
    will process the report and then set its status to **complete**. You may then
    view the web version of the report.
