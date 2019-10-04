---
layout: dashboard
permalink: /documentation/dashboard/
---

Dashboard Documentation
=======================
{: .anchor}

The Solar Forecast Arbiter Dashboard is a web interface for managing solar
observation and forecast data and for evaluating solar forecast accuracy.
This documentation provides step-by-step examples of how to perform
common activities on the Solar Forecast Arbiter dashboard. Use the Contents menu
to navigate between each activity. Each section includes instructions and screenshots.

Be sure to read the [Getting Started](#getting-started) section for instructions
on how to access the current version of the dashboard.
Please see the [data model documentation](/datamodel/) for more details on
how the Solar Forecast Arbiter organizes metadata (Sites, Observations, and Forecasts)
and time series data.
Additional training materials are available in our
[workshop repository](https://github.com/SolarArbiter/workshop).


Getting Started
---------------
{: .anchor}

To register an account in the Solar Forecast Arbiter, navigate to
[dashboard.solarforecastarbiter.org](https://dashboard.solarforecastarbiter.org)
and click on the login link. You will be prompted with an Auth0 login
window. Click the sign up tab and enter your information. Auth0 is a
secure authentication service that has numereous security credentials
and undergoes routine audits.

You will receive an email from Auth0 to verify your email address. You are
required to verify your email before accessing the Solar Forecast Arbiter.

In order to upload data to the Arbiter, generate reports, or receive
data from other users, you will first need to associate your user
account with an *organization* account. To establish a new organization
or to join an existing organization, contact
[help@solarforecastarbiter.org](mailto:help@solarforecastarbiter.org)


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

1.  Navigate to the Site listing page using the **Sites** link in the left
	sidebar. Select the site for which you are adding a Forecast.

2.  Click the **Create new Forecast** button on the Site page.
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
    Add pairs of Observations and Forecasts to compare by clicking the
    **Add Forecast, Observation pair** button. Check the boxes for
    metrics to calculate in the report.

     <img class="my-3" src="/images/report_form.png"/>

    After clicking submit, you will be returned to the report listing page where
    you will see the newly created report with a status of **pending**. The Arbiter
    will process the report and then set its status to **complete**. You may then
    view the web version of the report.

## Permission/Role management
{: .anchor}

This section describes the user interface for managing data acces through
roles and permissions. An accompanying workflow description can be found in the
[Data Access Workflow Document](/data-access-workflow/).

User, permission and role administation can be accessed by clicking the **User
Administration** link in the Account menu in the top right corner of the site.
    <img class="my-3" src="/images/admin_menu.png"/>



Note that these menus are meant to assist organization administrators in viewing
and managing permissions, and users without admin privileges may not see anything
on these pages.



### Users
{: .anchor}
-   The Users tab will list the Users you have access to administer or view.
	<img class="my-3" src="/images/users.png"/>


-	Clicking on an individual user will list information about the user and their
    roles.
    <img class="my-3" src="/images/user.png"/>


### Roles
{: .anchor}
-	The Roles tab will list all of the Roles you have access to administer or view.
    <img class="my-3" src="/images/roles.png"/>

-	Clicking on an individual Role will list information about it and the permissions
    associated with it.
    <img class="my-3" src="/images/role.png"/>


### Permissions
{: .anchor}
-	The Permissions tab will list all of the Permissions you have access to administer
    or view.
    <img class="my-3" src="/images/permissions.png"/>

-	Clicking on an individual Permission will list information about it and the objects
    it applies to.
    <img class="my-3" src="/images/permission.png"/>
