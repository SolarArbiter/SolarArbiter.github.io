---
layout: dashboard
permalink: /dashboarddoc/
---

User Dashboard Interaction
==========================
{: .anchor}

This document illustrates how a Solar Forecast Arbiter user may use the
Dashboard to complete the following actions:

-   [Creating a new Site](#creating-a-site).

-   [Creating a new Observation or Forecast](#creating-an-observation-or-forecast).

-   [Uploading Data to an Observation or Forecast](#uploading-data).

When a user is filling out a form, a tooltip describing the information
a user should enter is shown when the field’s name or options are not
descriptive enough alone. An example of these tooltips is shown below.

<img class="my-3" src="/images/TooltipDetail.png" class="figure"/>

Creating a Site
---------------
{: .anchor}

1. Navigate to sites listing page using ‘Sites’ link in the left sidebar. At the top of the Site listing click ‘Create new Site’.
<img class="my-3" src="/images/SitesListing.png"/>

2. Enter the metadata for your Site. Selecting a site type of 'Power Plant' will prompt you for additional fields as shown below. Sites that are power plants will require  After submission, you will be redirected to a Site page which displays the new Site’s metadata. The Site page will also display links to pages listing its associated Observations and Forecasts. See [Creating an Observation or Forecast](#creating-an-observation-or-forecast).
- Weather Station
<img class="my-3" src="/images/SiteForm.png"/>
- Power Plant
<img class="my-3" src="/images/plant_site_form.png"/>


Creating an Observation or Forecast
-----------------------------------
{: .anchor}

To create an Observation or Forecast, an associated site must already exist. See [Creating a Site](#creating-a-site) for instructions.

1.  Navigate to the Site listing page using the ‘Sites’ link in the left sidebar. Select the site for which you are adding an Observation or Forecast.

2.  You may use the “Create new Observation” button on the Site page or on the Site’s Observations listing page.
- Site Page<br/>
  <i>Weather Station Site</i>
  <img class="my-3" src="/images/weather_site.png"/>
  <i>Power Plant Site</i>
  <img class="my-3" src="/images/plant_site.png"/>
- Site’s Observations listing
<img class="my-3" src="/images/SiteObsListing.png"/>

3.  Enter metadata for your Observation. On submission, you will be redirected to an Observation page which displays the new Observation metadata and a link to add Observation data. See [Uploading Data](#uploading-data).
<img class="my-3" src="/images/weather_obs.png"/>

Uploading data
--------------
{: .anchor}

To upload data, an associated Site and Observation or Forecast object must already exist. See [Creating a Site](#creating-a-site) or [Creating an Observation or Forecast](#creating-an-observation-or-forecast) for instructions. To upload Forecast data, replace “Observations” with “Forecasts” in the instructions below.

1.  From Sites listing page, click on a site.

2.  Click ‘Observations’ to find the Observations listing for that site.

3.  Select an Observation. Click ‘Upload Data’ on the Observation page.
<img class="my-3" src="/images/observation.png"/>

4.  Select the file type, this will display an example of the expected file format. Click ‘Choose File’ and select the data file to upload.

	-  CSV format
	<img class="my-3" src="/images/csv_upload.png"/>
	- JSON format
	<img class="my-3" src="/images/json_upload.png"/>
