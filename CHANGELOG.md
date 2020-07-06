# Changelog

All notable changes to the Solar Forecast Arbiter Framework will be documented
in this file.

Detailed changes to the Solar Forecast Arbiter Core python library can be found
in the core documentation's [what's new](https://solarforecastarbiter-core.readthedocs.io/en/latest/whatsnew/index.html) series.

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
