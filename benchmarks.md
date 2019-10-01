---
layout: base
permalink: /benchmarks/
---

# Benchmark Forecasts

The Arbiter includes the capability to create and evaluate benchmark
irradiance, power, and net load forecasts. Comparisons of test forecasts
against benchmark forecasts can help forecast users and developers
understand the relative merits of models. The most appropriate benchmark
will depend on the use case and forecast horizon. To guide our selection
of the built-in benchmark forecasts, we first identified the following
desirable attributes of a benchmark forecast:

* Available throughout the US
* Freely available or easily implemented
* Provide quantities of interest to both forecast users and providers
* Stakeholder buy-in

## Built-in benchmark forecasts

The Arbiter provides built-in support for the following benchmark
options. Additional implementation details are available in the
``solarforecastarbiter-core``
[documentation](https://solarforecastarbiter-core.readthedocs.io/en/latest/reference-forecasts.html).

### Intrahour horizons

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

### Intraday and longer horizons

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

### Probabilistic

* GEFS cloud cover to ranked irradiance ensemble
* Climatology (not yet implemented)
* Persistence ensemble (not yet implemented)

### Automated generation

Operational benchmark forecasts are currently produced for every
reference forecast site in the Arbiter's database. Forecasts are currently only produced
using the [intraday and longer horizons](#Intraday-and-longer-horizons)
models described above. For these automated benchmark forecasts, we choose to define
[forecast attributes](/definitions/#forecastattrs) such that new forecasts
would be issued at midnight local time for each site. Daylight Saving Time
is not included when determining the issue time. For example, for the
Table Mountain SURFRAD site, the following parameters apply (interval label
is ending and interval length is 1 hour for all):

| Model | Issue time of day &nbsp;&nbsp;&nbsp;| Run length &nbsp;&nbsp;&nbsp;| Lead time to start &nbsp;&nbsp;&nbsp;|
|-------|:-----------------:|:----------:|:------------------:|
| GFS day ahead | 7Z | 1 day | 1 day |
| NAM current day | 6Z | 1 day | 1 hour |
| HRRR intraday | 0Z | 6 hours | 1 hour |
| RAP intraday | 0Z | 6 hours | 1 hour |

Please contact the framework administrators if you have suggestions for
improvements to the configuration of the automatically generated
benchmarks or if you require a custom benchmark configuration for your
application (e.g. a forecast trial).

## User-supplied benchmark forecasts

Some evalulation applications may require users to provide their own
benchmark forecasts. For example, Solar Forecasting 2, Topic Area 2
teams may choose to run an earlier version of WRF Solar and then upload
its forecasts for existing or new evaluation sites. Users may then
identify the forecast as a benchmark when creating a forecast
evaluation [report](/documentation/dashboard/#create-new-report) so that
forecast skill metrics will be calculated with respect to the benchmark.

Users are encouraged to track metadata about the forecast using the
*extra parameters* field of the forecast creation
[form](documentation/dashboard/#create-new-forecast). Key modeling details
such as grid spacing and schemes, or even a whole WRF namelist, may be
included in the extra parameters field.

As explained in the
[Data Model](https://solarforecastarbiter.org/datamodel/), the Arbiter
will accept uploaded forecasts for predefined evaluation sites or
aggregates. The Arbiter will not accept gridded datasets.

## Net load forecasts

Net load is defined here as true system load minus behind the meter PV.
Net load is the load that must be served with utility scale resources,
regardless of whether or not they are dispatchable, conventional, or
renewable. We make no allowance for wind power or utility scale solar
power. Therefore, net load is *not equal* to the load that must be
served with conventional generation.

The Arbiter will include the capability to create benchmark net load
forecasts as defined above. More information on this topic will be
available soon.
