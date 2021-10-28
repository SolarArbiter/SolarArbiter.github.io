# Changelog

All notable changes to the Solar Forecast Arbiter Framework will be documented
in this file.

Detailed changes to the Solar Forecast Arbiter Core python library can be found
in the core documentation's [what's new](https://solarforecastarbiter-core.readthedocs.io/en/latest/whatsnew/index.html) series.

## [1.0.7] - 2021-10-28
{: .anchor}

### Changed

- Improved dashboard code which estimates the total data points used in a report. This code is used to determine whether or
  not to attempt to display timeseries plots on a rendered report. The estimate had not correctly accounted for probabilistic
  forecasts and resulted in large reports being inaccessible via the dashboard.


## [1.0.6] - 2021-10-08
{: .anchor}

### Added

- Added missing [documentation](https://solarforecastarbiter-core.readthedocs.io/en/latest/reference-forecasts.html#persistence) for probabilistic reference forecasts.

### Changed

- Cleaned up dashboard navigation and appearance. Moved sidebar navigation into header, reduced height of header, reduced font size, and increased horizontal span. 

- Put many Report sections into expandable containers to reduce scrolling
  and to highlight the most relevant information for most users.

## [1.0.5] - 2021-09-22
{: .anchor}

### Added

- Added dashboard interface for quality flag filters instead of just selecting
  quality flags to exclude. See [Quality flag filters documentation](/documentation/dashboard/working-with-data/#quality-flag-filters)
  for details.

- Forecast creation forms on the dashboard now link to the [forecast definition](https://solarforecastarbiter.org/definitions/).

### Changed

- Quality flag filters will now exclude intervals where the percentage of flagged
  points within the interval is greater than *or equal* to the resample threshold
  percentage of the filter. Previously the comparison was strictly greater than. A resample percentage threshold of 0 is treated as a
  special value that will exclude intervals if *any* flagged points are found in
  the interval.

- Removed development and test urls from API documentation. These URLS were intended
  for use by platform maintainers and their inclusion in documentation was confusing
  to end users.

### Fixed

- Corrected the error message when an invalid report name is supplied on the
  dashboard report form.

- Corrected misaligned data in report csv downloads. Each forecast or observation
  is now provided in a separate csv file. Also removed stray `<br>` tags from column names.

- Corrected power model by projecting DNI into plane of the array when computing
  POA irradiance.

- Corrected order of seasons on metric plots with season categories.

- Fixed broken time range inputs on dashboard probabilistic forecast pages.

## [1.0.4] - 2021-08-18
{: .anchor}

### Added

- [Frequently Asked Questions](/faq/) help page.

- Added buttons to dashboard to clone metadata of Sites, Observations, Forecasts,
  and Probabilistic Forecasts.

### Changed

- Updated API documentation to clarify authentication token process. Also
  included script using commonly available commands as alternative to *jq*.

- Corrected API documentation for Site *temperature coefficient* field. Field
  was erroneously listed as having units of 1/C and was corrected to units of
  %/C.

### Fixed

- When observations and forecasts had a different interval label convention
  (ending/beginning and beginning/ending), observations were not correctly
  resampled. Fixing this substantially alters the metrics for some forecasts.
  Report owners must recompute the report to recalculate the correct metrics. If
  reading a report with mismatched observation and forecast interval labels,
  ensure that the report was created with ``solarforecastarbiter-core >=
  1.0.4``.

- Fixed plotting of observations when multiple values exist at the same time
  index. Bug was introduced in 1.0.3 when addressing a failure to plot
  observations when one of many forecasts was missing.

## [1.0.3] - 2021-08-03
{: .anchor}

### Added

- Instructions to the Create Site page for how to reasonably specify
  metadata for a wind power plant or load.

- Reports for event forecasts may now exclude user flagged and nighttime
  periods.

### Fixed

- Fixed report summary statistics table always displaying event statistics.

- Improper accounting for observation and forecast interval labels in
  probabilistic persistence time of day reference forecasts.

- Differentiated observations in report timeseries plot legend by adding
  interval length and interval label of the resampled observation.

- Typos and minor layout issues in role based access control dashboard
  pages.

- Incorrect help text for single axis tracker ground coverage ratio.

## [1.0.2] - 2021-07-22
{: .anchor}

### Added

- Report timezone may now be explicitly set. Previous behavior was to
  use the timezone of the first site specified in the report.

- `solarforecastarbiter` python package now available through `conda-forge`:
  ``conda install -c conda-forge solarforecastarbiter``

- Function to parse BSRN station-to-archive formatted data (modified
  version of a pvlib python function).

### Changed

- Removed the word **solar** from the reports as a first step in making
  the platform more suitable for wind and load.

- Datetime input fields are improved and now consistent throughout the
  dashboard.

- Report links to observations and forecasts now go to the specific
  date range of the report.

### Fixed

- SRML and PVDAQ reference PV sites had positive temperature coefficients.

- Minor changes to python packing including requirements specifications
  and classifiers.

- If total metrics category was not selected, reports now display a
  warning instead of a confusing empty table.

- Removed the BSRN Granite Island MI site from reference database. This
  site was added without realizing 2020 and newer data is not readily
  available from the NASA web pages.

- Reports could not be created for event forecasts due to an issue with
  validating event forecast data.

- Changed GFS fetch directory for compatibility with March 22, 2021, 12Z
  model upgrade.

- Fixed issue with processed observations failing to be plotted due to a
  missing forecast. Processed observations are now plotted for all
  points for which there is a forecast.

- Fixed probabilistic persistence ensemble forecasts to use the last 30
  days of data and probabilistic persistence time of day algorithm
  rather than the last hour of data with standard probabilistic
  persistence. Hour ahead reference forecasts are replaced with day
  ahead reference forecasts.

- Clarified that automated generation of reference forecasts is
  currently limited to privileged accounts run by SFA itself.

- Fixed reference forecast links in report tables.


## [1.0.1] - 2020-11-18
{: .anchor}

### Fixed

- Issue with text encoding for dashboard data uploads.

- Removed report intro sentence about creating issues on GitHub.

- Clarified report summary statistics table only contains statistics for
  the resampled observations and deterministic forecasts.

- Added missing permissions to read reference aggregates.

## [1.0.0] - 2020-11-17
{: .anchor}

This 1.0 version is the culmination of more than 2 years of work, but this
section of the changelog only highlights the differences with the most recent
release (1.0rc4). Please see the release notes for each of the rc, beta, and
alpha versions below for a complete history of changes. Please see the
[documentation](https://solarforecastarbiter.org/documentation/) for the
dashboard, API, or core framework for a complete description of features.

### Added

- Backfilled all missing data from SURFRAD, SOLRAD, RTC, and ARM data for 2017
  through October 2020.

- Predefined reference aggregates for mean of SURFRAD GHI, mean of SURFRAD DNI,
  and the total PV power of several small systems in the UO SRML network in
  Portland, OR. See [dashboard.solarforecastarbiter.org/aggregates](https://dashboard.solarforecastarbiter.org/aggregates/).

- Ability to download site, observation, and forecast metadata from the
  dashboard. Click the "Download Metadata" link in the upper right corner of
  any metadata description box.

- "Copy UUID" button to the metadata of a site, observation, or forecast. This
  allows dashboard users to more easily copy identifier data into scripts that
  interact with the API.

### Changed

- Improved documentation of
  [data upload](https://api.solarforecastarbiter.org/#section/Introduction/Interaction-for-Observational-Data-Providers)
  and
  [authentication](https://api.solarforecastarbiter.org/#section/Authentication)
  procedures when using the REST API.

- Improved text description on [dashboard.solarforecastarbiter.org](https://dashboard.solarforecastarbiter.org)
  landing page.

- Moved the dashboard's observation/forecast data upload controls from a
  separate page to below the time series graph.

### Fixed

- Plots of metrics for total analysis period could contain mislabeled bars.

- JSON metadata downloads in reports could fail due to special characters in
  site, observation, or forecast extra parameters fields.

- Typo in time series plot labels for probabilistic forecasts of thresholds.

- API error when uploading empty forecast data.

- Bug causing report values to be duplicated on recompute, causing slow down
  and API failures. Now only the most recent computed values are stored.


## [1.0rc4] - 2020-10-29

### Added

- Added Seasons to the available report categories.

- Added summary statistics of resampled observations, forecasts, and reference
  forecasts to reports.

- All validated, aligned, and resampled data, report object metadata, and summary
  statistics are now available to download directly from reports.

- Added Continuous Ranked Probability Skill Score metric to probabilisitic
  report metric options.

- Added ability to update metadata fields for name, PV power plant modeling
  parameters, timezone, observation uncertainty, and extra parameters. Updates
  can be performed through the API or by following the 'Update Metdata' buttons
  on the dashboard.

- Added validation for event data on upload.

### Changed

- Intervals are now marked as day/night depending on the fraction of day/night
  minutes within the interval, rather than the day/night status at the moment
  of the interval label.

- Data validation filters may now be applied before resampling observations to
  match forecasts or after the resampling. By default, filters associated with
  erroneous data (e.g. limits exceeded) will be applied before resampling to
  prevent bad values from contaminating the observation. Filters
  associated with good data (e.g. day/night, clear/cloudy) will be applied after
  resampling to remove resampled intervals with too few qualifying points.
  Rewrote the report data prepreprocessing section to more clearly describe how
  the data is handled.

- Observations *uncertainty* field is now optional.

- Users with limited permissions on a report will now be able to view a partial
  report with timeseries and scatter plots that only containing data they have
  access to.

- Observations may be deleted from an aggregate. This will remove all
  *effective from* and *effective until* values for the observation.

- API Reports endpoint now validates object pairs on report submission. The
  API previously accepted invalid object pairs which resulted in report
  computation failures.

### Fixed

- Improved upon API's OpenAPI specification, with more complete parameter
  descriptions and correct response codes. The specification is available at
  the `/openapi.json` and `/openapi.yaml` endpoints.

- Fixed a bug where aggregation failed with a missing observation error after
  an observation's *effective_until* had been set.

- Adjusted report metrics and validation result tables to be scrollable when
  they contain many results. Previously, columns would become crowded and
  overlap.

- Adjusted Report metrics plots to avoid x axis labels running off the plot or
  overlapping eachother.

- Utilized [loky](https://loky.readthedocs.io/en/stable/) to improve failure
  tolerance of reference NWP code.

- Fixed a bug where aggregate computation reported a missing observation outside
  the observation's *effective_from* and *effective_until*.

## [1.0rc3] - 2020-09-16

### Added

- A package for solarforecastarbiter-core to PyPI
  [https://pypi.org/project/solarforecastarbiter/](https://pypi.org/project/solarforecastarbiter/)
  Install in a python environment with ``pip install solarforecastarbiter --pre``

- Additional irradiance data has been added to DOE ARM sites.

- Relative euclidean distance, quantile score, and quantile skill
  score metrics.

- API endpoints /users/can-create and /users/actions-on-type/<object-type>.

- Plots for probabilistic forecast groups on the dashboard.

- Option to include a reference forecast as a standard forecast, rather
  than simply being used for skill score, when creating a report.

### Changed

- Reduced the opacity of report scatter plot points to improve visibility of many points.

- Site creation form now always includes PV power plant parameter fields that
  are initially set to disabled. Selecting Power Plant enables the fields.

- Buttons to create metadata, delete reports, and add roles are now hidden if
  the user does not have permission to take the action on the object.

### Fixed

- NOAA USCRN reference site elevation was incorrectly specified in units of
  feet instead of meters.

- Ordering and color of forecasts in report time-series and scatter plots
  is now consistent.

- Fix some UO SRML reference site names and fix the data fetch routine to
  avoid data gaps.

- Fixed bad text wrapping in report metadata table.

- Added several missing PVDAQ sites and fixed several PVDAQ time zones


## [1.0rc2] - 2020-07-21

### Added

- [Documentation](https://solarforecastarbiter.org/documentation/dashboard/trials/)
  of the Solar Forecast Arbiter's procedures for initiating, configuring, and
  conducting forecast trials.

### Changed

- Plots of probabilistic forecast distributions in reports are now shaded by
  their percentile values.

- Observations and forecasts of power may only be created at "Power Plant"
  sites and are no longer allowed at "Weather Station" sites. The plant
  metadata (e.g. AC/DC capacity) is required to validate data uploads and run
  analysis reports, leading to run-time errors when users attempted to do so at
  "Weather Station" sites. The Site creation form now indicates this
  requirement.

### Fixed

- Filtering by climate zone.

- Several bugs in the dashboard user interface for creating permissions,
  adding permissions to roles, and granting roles to another user. These bugs
  were cosmetic and did not jeopardize any user data.

- Bug related to variable/unit consistency in the report form's forecast
  and observation selection interface.

- Reference persistence forecasts for GHI at PV power plants were incorrectly
  clipped to the power plant's AC capacity value.


## [1.0rc1] - 2020-07-06

### Added

- Support for probabilistic forecast reports, including forecasts of
  distributions, quantiles, and thresholds.

- Deterministic cost metrics in reports, including a constant cost factor,
  a time-of-day varying factor, a datetime varying factor, and a cost that
  depends on the magnitude of the error. Read more
  [here](https://solarforecastarbiter-core.readthedocs.io/en/latest/cost.html).

- Missing forecast values may be filled using a fixed value or the last valid
  value. This is especially important in the context of an operational
  forecast trial.

- Functions to compute persistence ensemble (PeEn) forecasts from observation
  data.

- Reference persistence ensemble forecasts at reference sites.

- Net load observation data and reference net load forecasts for the
  US ISO/RTOs: CAISO, ERCOT, ISO-NE, MISO, NYISO, PJM, and SPP.

- Climate zones and associated endpoints now available in the API.

- Dashboard users can create a copy of an existing report using the "Clone report
  parameters" button. Users will have an opportunity to adjust any parameters
  before the report is created.

- Added API endpoint to locate gaps in timeseries data. This endpoint is available
  for observations, forecasts, and probabilistic forecasts.

- Added API endpoint to locate days where observation data does not contain a
  given quality flag.

### Changed

- Site listing page now shows the climate zones that each site belongs to,
  rather than the latitude and longitude. Metadata display for each site
  also now includes the climate zones.

- Expanded and revised dashboard documentation.
  [solarforecastarbiter.org/documentation](https://solarforecastarbiter.org/documentation/)
  provides links to documentation for each component of the project (dashboard,
  API, and core). Simplified
  [Getting Started](https://solarforecastarbiter.org/documentation/dashboard/getting-started/).
  [Working with Data](https://solarforecastarbiter.org/documentation/dashboard/working-with-data/)
  now contains sections on [Reports](https://solarforecastarbiter.org/documentation/dashboard/working-with-data/#create-new-report)
  and
  [Data Validation](https://solarforecastarbiter.org/documentation/dashboard/working-with-data/#data-validation).

- Documentation style is now consistent with dashboard style.

### Fixed

- Reports for event forecasts could not be generated due to a bug.

- Observation data validation is now reapplied if needed when computing a report.

- Adjusted forecast timeseries plots to include any future data by default.

## [1.0beta6] - 2020-06-02

### Added

- Reports may now be downloaded in PDF format, although reports that currently exist must first be recomputed.

- Incorporated PV power data from University of Oregon SRML network into the
  Solar Forecast Arbiter's reference observation dataset.

- Automatically generated persistence forecasts were added to the Solar
  Forecast Arbiter reference dataset.

- Added support for derived quality flags 'DAYTIME', 'DAYTIME STALE
  VALUES' and 'DAYTIME INTERPOLATED VALUES'.

- AC and DC power limits were added to the validation package. Values are
  marked with the `LIMITS EXCEEDED` flag.

- Added limits to API requests to avoid timeouts when transferring or
  processing data. The limit for retrieving timeseries data is 1 year. The
  limit for uploading data is 200,000 datapoints or 16 MB, whichever limit is
  reached first. The dashboard and API will respond with error messages
  informing users of these new limits.

- Dashboard now displays the timerange of available timeseries data, and will
  plot the most recent three days of data by default.

- Report listings have a metadata button for viewing report metadata in a pop
  out before viewing.

- Dashboard now displays option to recompute a report to users with update
  permissions on that report.

- Extra parameters field are now accessible on the dashboard.

- Improved upon error messages when users enter invalid characters into a name
  field on the dashboard.

### Changed

- Temperature coefficients are now recorded in units of %/C.

### Fixed

- Report metric plots now display months and weekdays in the correct order.

- Fixed incorrect timezones of DOE RTC sites.

- Fixed multiple instances where the dashboard did not handle error responses
  from the API as expected, causing crashes.

## [1.0beta5] - 2020-04-27

### Added

- Added support for event forecasts and associated reports. A list of supported
  metrics can be found on the [metrics page](https://solarforecastarbiter.org/metrics/#metrics-for-deterministic-event-forecasts).

- Reports now support normalized metrics such as NMAE. Normalization is
  automatically determined based on Observation type. AC power observations
  are normalized by AC capacity; DC power by DC capacity. Normalized metrics
  are set to nan for all other variables.

- Users may now select a reference forecast to use in computing
  [forecast skill](https://solarforecastarbiter.org/metrics/#s).

- Many deterministic metrics may now include a deadband to account for
  uncertainty. The deadband is specified as a percentage of the observations.
  The error forecast - observation is set to 0 within the deadband. Users may
  control the deadband using the report creation form.

- Reports of GHI observations and forecasts may now filter out periods of
  clear sky. Users must generate two reports if they desire metrics for both
  all sky and cloudy sky.

- All report plots are now created with Plotly instead of Bokeh. Plotly's JSON
  specification and more mature javascript library makes it easier to optimize
  reports for display in web browsers.

- Added API endpoint to recompute report at `/reports/<report_id>/recompute`.
  API users can access this endpoint now, and a button will be added to the
  dashboard in a future release.

- Added API endpoint to get the actions the current user is allowed to take on
  an object at `/users/actions-on/<object_id>`.

- Added API endpoints to query for latest available data or a timerange of
  available data. These endpoints are found by appending `/latest` or
  `/timerange` to the end of a values endpoint.

- Added DOE ARM sites to reference database.

### Changed

- Individual forecasts or observations can be singled out by double-clicking
  the legend of a report timeseries or scatter plot.

- Dashboard hides buttons for actions that a users cannot take due to
  insufficient permissions. This feature has been implemented on individual
  site, forecast, probabilistic forecast, aggregate, observation, role, and
  permission pages. This feature will be extended to hide the "Create" button
  and other actions from tabulated listing pages in a future release.

- Improved the speed of reading aggregate values from the API.

- Improved the speed of storing timeseries values at the API.

- Clarified data validation and data resampling/alignment sections of reports.

### Fixed

- Lazily render report plots to avoid browser freezing or crashing when many
  (~100) plots exist.

- Report timeseries figures no longer draw a line over periods of missing data.

- Improved data fetch of reference observations to avoid periods of missing
  data due to delays in data reporting.

- All data validation now includes the generation of the NIGHTTIME flag.

## [1.0beta4] - 2020-02-07

### Added

- Daily updating precomputed reports for select reference data.

- Reports now contain a summary of data affected by the data resampling and
  alignment process. The summary includes the number of data points removed by
  each phase of validation.

- Reports now contain a table of all included metrics over the entire selected
  period.

- Reports may be configured to filter data by quality flag. Currently allows
  filtering of *user flagged* and *nighttime* values.

- The dashboard report view now allows users to search metric plots by
  forecast and to sort metric plots by metric, category and forecast.

- Dashboard users can now download report metrics as a csv using a link in the
  *Metrics* section of the report.

- Reports in the *pending* and *failed* state now display a message to the user
  about their status. For failed reports, this is a list of errors encountered
  while processing the report.

### Changed

- The API's report response's `raw_report` attribute was updated to reflect the
  set of processed report data needed for rendering a final report. The
  `raw_report` attribute was previously presented as a serialized version of
  the final rendered report.

- The core library's Report received a major refactoring. See the core
  [what's new](https://solarforecastarbiter-core.readthedocs.io/en/latest/whatsnew/1.0.0b4.html)
  for details.

- The button for downloading timeseries data from the dashboard has moved to
  below the plots on any Forecast, Observation or Probabilistic Forecast's
  page. The same start and end times are used for downloading data and creating
  plots.

- The start and end time values for the dashboard's timeseries plots are now
  prefilled with time range requested. By default, this will display the last
  three days of data.

### Fixed

- Corrected handling of empty observation timeseries during metrics
  preprocessing which was causing report processing to fail.

- Corrected handling of `interval_label` == `ending` when computing metrics
  for a report containing mixed `interval_label`s.

## [1.0beta3] - 2019-12-16

### Added

- Dashboard report form now includes all deterministic metrics options
  identified by stakeholders.

- Dashboard report form now includes options to calculate metrics by categories
  Total, Year, Month, Date, and Hour of Day.

- Ability to analyze forecasts of aggregated observations in reports.

- Reports may be downloaded in HTML format from the dashboard at
  `/reports/<report_id>/downloads/html`.

- The API report schema's `object_pair` json objects have been updated to
  support pairing forecasts with either observations or aggregates. See the
  [api documentation](https://api.solarforecastarbiter.org/#tag/Reports/paths/~1reports~1{report_id}/get) for details.

- Dashboard report downloads contain a GPG signed report as well as md5, sha1
  and sha256 checksums for validation.

- CHANGELOG.md (this file) for tracking and communicating changes.

- Dashboard tables now allow for filtering on multiple columns. e.g. Variable,
  Provider and Site for Observation and Forecast tables.

### Fixed

- Permissions acting on aggregates are now accessible on the dashboard via a
  Role's permission listing.

- Removed dashboard functionality to create ineffectual permissions granting
  `update` action on forecasts, sites, observations and probabilistic
  forecasts.

- Removed permissions listing from the dashboard role creation form. Users
  will now add permissions after the Role has been created.

- Updated dashboard role and permission forms to retain checklist selections
  in the event of an error.

## [1.0beta2] - 2019-11-18

### Added

- Aggregates can be created through the dashboard. See  [Aggregate Documentation](https://solarforecastarbiter.org/documentation/dashboard/working-with-data/#create-new-aggregate)

- Day-ahead probabilistic reference forecasts based on the GEFS are available for DOE RTC, NOAA SURFRAD, NOAA SOLRAD, and NREL MIDC networks.

### Fixed

- Issues with report plots and tables including inconsistent forecast ordering
  and coloring in report bar charts, limitations on number of forecasts than
  can be plotted, limitations on number of metrics in a table.

## [1.0beta] - 2019-10-4

### Added

- User management controls for organization admin. See [Dashboard Administration Documentation](https://solarforecastarbiter.org/documentation/dashboard/administration/)

- Start/End selection for plots on Forecast, Probabilistic Forecasts and
  Observation Pages.

## Fixed

- Reports now calculate monthly, daily, hourly metrics in the timezone
  specified by the site metadata instead of UTC.

- Reference NWP forecasts now properly account for `interval_label`.

## [1.0alpha] - 2019-06-28

Initial Solar Forecast Arbiter Dashboard release. Includes site, forecast,
probabilistic forecast, and basic report functionality.
