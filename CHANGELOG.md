# Changelog

All notable changes to the Solar Forecast Arbiter Framework will be documented
in this file.

Detailed changes to the Solar Forecast Arbiter Core python library can be found
in the core documentation's [what's new](https://solarforecastarbiter-core.readthedocs.io/en/latest/whatsnew/index.html) series.


## [1.0beta5] - 2020-04-23

### Added

- Added support for event forecasts and associated reports. A list of supported
  metrics can be found on the [metrics page](https://solarforecastarbiter.org/metrics/#metrics-for-deterministic-event-forecasts).

- Reports now support normalized metrics such as NMAE. Normalization is
  automatically determined based on Observation type. AC power observations
  are normalized by AC capacity; DC power by DC capacity. Normalized metrics
  set to nan for all other variables.

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
  insufficient permissions.

- Improved the speed of reading aggregate values from the API.

- Improved the speed of storing timeseries values at the API.

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
