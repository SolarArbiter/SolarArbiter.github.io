---
layout: dashboard
permalink: /dashboarddoc/
---

User Dashboard Interaction
==========================
{: .anchor}

This document illustrates how a Solar Forecast Arbiter user may use the
Dashboard to complete the following actions:

-   [Create New Site](#create-new-site)

-   [Create New Observation or Forecast](#create-new-observation-or-forecast)

-   [Upload Data to an Observation or Forecast](#upload-data)

### User Guidance Considerations
To assist in the user in providing the correct information and
navigating the dashboard's interface, we've adopted the following
features not otherwise illustrated in this guide.

-  To reduce clutter, the dashboard will utilize *progressive
   disclosure* to hide unnecessary fields from view e.g. the
   Site form will not display the *PV Modeling Paremeters* fields
   unless a *Site Type* of *Power Plant* is selected.

-  Descriptive tooltips will be displayed when a user selects a field.
   <img class="my-3" src="/images/TooltipDetail.png" class="figure"/>
   <figcaption class="figure pb-2">The latitude field is selected and displays
   a tooltip describing the data a user should enter.</figcaption>

-  Basic validation will be performed on the entered data to provide
   immediate feedback to the user. There are two possible sources of
   error in dashboard interaction:

   1.  Invalid Input

       For example, a user entering a non-numeric value into numeric
       field. In this case, the user will be prompted with meaningful
       error messages and required to correct their data before submission. 

   2.  Insufficient Input

	   All fields will be required unless otherwise indicated. Users will
	   not be able to submit data until they have provided valid data
	   for all required fields.

Create New Site
-------------
{: .anchor}

1. Navigate to sites listing page using ‘Sites’ link in the left
   sidebar. At the top of the Site listing click ‘Create new Site’.
<img class="my-3" src="/images/SitesListing.png"/>

2. Enter the metadata for your Site. Selecting a site type of 
   'Power Plant' will prompt you for additional fields. 

   
   - *Weather station site creation form*
   <img class="my-3" src="/images/SiteForm.png"/>

   - *Power plant site creation form*
   <img class="my-3" src="/images/plant_site_form.png"/>

3. After submission, you will be redirected to a Site
   page which displays the new Site’s metadata and allows you
   to create associated Observations and Forecasts (see
   [Create New Observation or Forecast](#create-new-observation-or-forecast)).

   *Power Plant Site Page*
   <img class="my-3" src="/images/plant_site.png"/>


Create New Observation or Forecast
---------------------------------
{: .anchor}

To create an Observation or Forecast, an associated site must already exist (see [Create New Site](#create-new-site)).

### Create New Observation
{: anchor} 

1.  Navigate to the Site listing page using the ‘Sites’ link in the left
	sidebar. Select the site for which you are adding an Observation.

2.  Click the “Create new Observation” button on the Site page.
  <img class="my-3" src="/images/weather_site.png"/>

3.  Enter metadata for your Observation. On submission, you will be redirected
    to an Observation page which displays the new Observation metadata and a
    link to add Observation data (see [Upload Data](#upload-observation-data)).
- *Observation form*
<img class="my-3" src="/images/weather_obs.png"/>
- *Created Observation page*
<img class="my-3" src="/images/observation.png"/>

### Create New Forecast
{: anchor}

1.  Navigate to the Site listing page using the ‘Sites’ link in the left
	sidebar. Select the site for which you are adding a Forecast.

2.   Click the “Create new Forecast” button on the Site page.
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
[https://dev-api.solarforecastarbiter.org/](https://dev-api.solarforecastarbiter.org/)
for detailed documentation.

### Upload Observation Data
{: anchor}

1.  From Sites listing page, click on a site.

2.  Click ‘Observations’ to find the Observations listing for that site.

3.  Select an Observation. Click ‘Upload Data’ on the Observation page.
<img class="my-3" src="/images/observation.png"/>

4.  Select the file type, this will display an example of the expected file
format. Click ‘Choose File’ and select the data file to upload.

	-  CSV format
	<img class="my-3" src="/images/obs_csv_upload.png"/>
	- JSON format
	<img class="my-3" src="/images/obs_json_upload.png"/>

### Upload Forecast Data
{: anchor}

1.  From Sites listing page, click on a site.

2.  Click ‘Forecast’ to find the Forecasts listing for that site.

3.  Select a Forecast. Click ‘Upload Data’ on the Forecast page.
<img class="my-3" src="/images/forecast.png"/>

4.  Select the file type, this will display an example of the expected file
format. Click ‘Choose File’ and select the data file to upload.

	- CSV format
	<img class="my-3" src="/images/fx_csv_upload.png"/>
	- JSON format
	<img class="my-3" src="/images/fx_json_upload.png"/>


Download Data
-------------
The dashboard will include tools to allow users to download data from
an Observation or Forecast page. Users will be able to select the time
period for which to download data. The format and field names in
the downloaded data will be the same as for data uploads. 

Users may also utilize the API to download data. See the
[API documentation](https://dev-api.solarforecastarbiter.org/)
for details.


<div class="my-3"></div>
