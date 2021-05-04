---
layout: base
permalink: /benchmarks/
title: Benchmark Forecasts
---

# Benchmark Forecasts

The forecasting community has long recognized the importance of comparing
a forecast to some kind of reference forecast. The choice of reference forecast
is critical for a fair comparison. Fair comparisons of test forecasts
against reference forecasts can help forecast users and developers
understand the relative merits of models. The most appropriate reference
will depend on the use case and forecast horizon.

The Arbiter provides a selection of built-in benchmark forecasts for publicly
available reference data, but it ultimately leaves the selection of reference
forecasts to the user.

## Built-in benchmark forecasts

To guide our selection of the built-in benchmark forecasts, we first identified
the following desirable attributes of a benchmark forecast:

* Available throughout the US
* Freely available or easily implemented
* Provide quantities of interest to both forecast users and providers
* Stakeholder buy-in

The Arbiter includes the capability to create and evaluate benchmark
irradiance, power, and net load forecasts.

The Arbiter provides built-in support for the following benchmark
options. Additional implementation details are available in the
``solarforecastarbiter-core``
[documentation](https://solarforecastarbiter-core.readthedocs.io/en/latest/reference-forecasts.html).

### Persistence

* Persistence
* Persistence of clear sky index

The Arbiter provides reference implementations of persistence
algorithms. The averaging window of the Arbiter's benchmark persistence
forecasts are fixed to be equal to a forecast's run length, but no
longer than 1 hour. For example, a benchmark forecast for a 15 minute
interval will use the most recent 15 minutes of data to compute the
quantity to persist (irradiance, power, or clear sky index). Persistence
of clear sky index accounts for the average clear sky index during an
interval rather than simply using the interval start or end time.

A week-ahead persistence forecast may also be configured for net load
applications (e.g. net load of the next Sunday will be equal to the last
Sunday).

### NWP

* HRRR subhourly irradiance
* RAP cloud cover to irradiance
* NAM cloud cover to irradiance
* GFS cloud cover to irradiance

With the exception of the HRRR, the Arbiter derives irradiance and power
forecasts from NWP cloud cover forecasts to accurately account for solar
position, inverval labels (beginning or ending), and interval averaging.
For these models, the process is:

1. Load hourly (or longer) interval data from the NWP grib files.
   * For GFS cloud cover, unmix the mixed-intervals average data.
2. Resample data to 5 minute intervals.
   * For GFS cloud cover, backfill the data.
   * For all other NWP data, interpolate the data.
3. Convert cloud cover to irradiance following Larson et. al. (2016).
4. If desired, use site metadata to compute AC power using
   [pvlib-python](https://pvlib-python.readthedocs.io/en/latest/)
   functions.
5. Compute hourly averages with desired interval labels.

NWP-derived forecasts are not currently available for net load.

### Probabilistic

* GEFS cloud cover to ranked irradiance or power ensemble
* Persistence ensemble (irradiance, power, net load)

### Automated generation

The Arbiter automatically produces benchmark forecasts for every reference
forecast site in the Arbiter's database. Built-in benchmark forecasts are
currently restricted to the public dataset, though we hope to add support for
user-specifed sites in the future.

The Arbiter creates persistence forecasts with 5, 15, 60, and 1 day lead times.
These forecasts are created for each variable that has a corresponding
observation at a site. The Arbiter also creates week-ahead persistence forecasts
for net load[^1].

For intraday and day ahead lead times, we chose to define [forecast
attributes](/definitions/#forecastattrs) for a *GFS Day Ahead*, *NAM Current
Day*, *HRRR Intraday*, and *RAP intraday* forecast in the local timezones of the
sites (Daylight Saving Time not considered). For example, for the Table Mountain
SURFRAD site, the following parameters apply (interval label is ending and
interval length is 1 hour for all):

| Model | Issue time of day &nbsp;&nbsp;&nbsp;| Run length / Issue frequency &nbsp;&nbsp;&nbsp;| Lead time to start &nbsp;&nbsp;&nbsp;|
|-------|:-----------------:|:----------:|:------------------:|
| GFS day ahead | 7Z | 1 day | 1 day |
| NAM current day | 6Z | 1 day | 1 hour |
| HRRR intraday | 0Z | 6 hours | 1 hour |
| RAP intraday | 0Z | 6 hours | 1 hour |

Note that, as described in [forecast attributes](/definitions/#forecastattrs),
the combination of *issue time of day* and *run length/issue frequency*
may describe more than one forecast run per day. Here, the HRRR and RAP
forecasts are issued at 0Z, 6Z, 12Z, and 18Z. The Arbiter creates irradiance
forecasts at every reference site and also creates power forecasts at the
reference power plants.

The Arbiter also creates benchmark probabilistic forecasts. The GEFS drives
a day ahead forecast and a persistence ensemble is used for an hour ahead
forecast.

## User-supplied reference forecasts

Some evalulation applications may require users to provide their own
reference forecasts. For example, some Solar Forecasting 2, Topic Area 2
teams will run an earlier version of WRF Solar and then upload
its forecasts for existing or new evaluation sites. Or a forecast user may
choose to use its existing forecast vendor as a reference. Users may then
identify the forecast as a reference when creating a forecast
evaluation [report](/documentation/dashboard/#create-new-report) so that
forecast skill metrics will be calculated with respect to the reference.

Users are encouraged to track metadata about the forecast using the *extra
parameters* field of the forecast creation
[form](documentation/dashboard/#create-new-forecast). Key modeling details such
as grid spacing and schemes, or your internal version of a namelist, may be
included in the extra parameters field. As explained in the [Data
Model](/datamodel/), the Arbiter will accept uploaded forecasts for predefined
evaluation sites or aggregates. The Arbiter will not accept gridded datasets.

## Trial-specific benchmark forecasts

The Arbiter's [operational forecast trials](/documentation/dashboard/trials/)
allow for any configuration of the built-in benchmark forecasts or user-supplied
reference forecasts. The Arbiter administrators can help prospective trial users
determine the most appropriate reference for their application. Contact
[admin@solarforecastarbiter.org](mailto:admin@solarforecastarbiter.org) for
more information on trials.

## Footnotes

[^1]: Net load is defined here as true system load minus behind the meter PV.
      Net load is the load that must be served with utility scale resources,
      regardless of whether or not they are dispatchable, conventional, or
      renewable. We make no allowance for wind power or utility scale solar
      power. Therefore, net load is *not equal* to the load that must be
      served with conventional generation.
