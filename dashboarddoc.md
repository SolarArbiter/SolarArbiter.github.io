---
layout: dashboard
permalink: /dashboarddoc/
---

User Dashboard Interaction
==========================
{: .anchor}

This document illustrates how a Solar Forecast Arbiter user may use the
Dashboard to complete the following actions:

-   [Create a new Site](#create-a-site).

-   [Create a new Observation or Forecast](#create-an-observation-or-forecast).

-   [Upload Data to an Observation or Forecast](#upload-data).


Create a Site
-------------
{: .anchor}

1. Navigate to sites listing page using ‘Sites’ link in the left
   sidebar. At the top of the Site listing click ‘Create new Site’.
<img class="my-3" src="/images/SitesListing.png"/>

2. Enter the metadata for your Site. Tooltips describing the
   information a user should enter are shown when the field’s
   name or options are not descriptive enough alone. An
   example of these tooltips is shown below.


   <img class="my-3" src="/images/TooltipDetail.png" class="figure"/>


- *Weather Station*
<img class="my-3" src="/images/SiteForm.png"/>
   Selecting a site type of 'Power Plant' will prompt you for additional
   fields as shown below.

- *Power Plant*
<img class="my-3" src="/images/plant_site_form.png"/>
   After submission, you will be redirected to a Site
   page which displays the new Site’s metadata and allows you
   to create associated Observations and Forecasts. See
   [Create an Observation or Forecast](#create-an-observation-or-forecast).


Create an Observation or Forecast
---------------------------------
{: .anchor}

To create an Observation or Forecast, an associated site must already exist.
See [Create a Site](#create-a-site) for instructions.

1.  Navigate to the Site listing page using the ‘Sites’ link in the left
	sidebar. Select the site for which you are adding an Observation or Forecast.

2.  You may use the “Create new Observation” button on the Site page or
	on the Site’s Observations listing page.
- Site Page<br/>
  *Weather Station Site*
  <img class="my-3" src="/images/weather_site.png"/>
  *Power Plant Site*
  <img class="my-3" src="/images/plant_site.png"/>
- Site’s Observations listing
<img class="my-3" src="/images/SiteObsListing.png"/>

3.  Enter metadata for your Observation. On submission, you will be redirected
    to an Observation page which displays the new Observation metadata and a
    link to add Observation data. See [Upload Data](#upload-data).
<img class="my-3" src="/images/weather_obs.png"/>

Upload data
-----------
{: .anchor}

To upload data, an associated Site and Observation or Forecast object
must already exist. See [Create a Site](#create-a-site) or
[Create an Observation or Forecast](#create-an-observation-or-forecast)
for instructions. The instructions here will describe the process of
uploading observation data. The process for uploading Forecasts is
similar, however, the required fields will be different. A list of
required fields by data type can be found in the [Data Model](/datamodel/).

1.  From Sites listing page, click on a site.

2.  Click ‘Observations’ to find the Observations listing for that site.

3.  Select an Observation. Click ‘Upload Data’ on the Observation page.
<img class="my-3" src="/images/observation.png"/>

4.  Select the file type, this will display an example of the expected file
format. Click ‘Choose File’ and select the data file to upload.

	-  CSV format
	<img class="my-3" src="/images/csv_upload.png"/>
	- JSON format
	<img class="my-3" src="/images/json_upload.png"/>
