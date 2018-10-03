---
layout: base
permalink: /benchmarks/
---

## Benchmark Forecasts -- DRAFT

The Arbiter will include a capability to evaluate and create benchmark
irradiance, power, and net load forecasts. Comparisons of test forecasts
against benchmark forecasts can help forecast users and developers to
understand the relative merits of models. The most appropriate benchmark
will depend on the use case and forecast horizon. We believe that the
following benchmark forecast attributes are appropriate for most use
cases:

* Available throughout the US
* Freely available or easily implemented
* Provide quantities of interest to both forecast users and providers
* Stakeholder buy-in

Additional information on the Arbiter's benchmark forecast capabilities
will be available in January, 2019.

If you're attending AMS 2019, please visit our Benchmark Solar Power
Forecasts
[poster](https://ams.confex.com/ams/2019Annual/meetingapp.cgi/Paper/354730)
on Monday, January 7 from 4:00 - 6:00 PM.


Built-in benchmark forecasts
============================

The Arbiter will provide built-in support for the following benchmark options.

Intrahour horizons
------------------

* Persistence
* Persistence of clear sky index
* ARIMA


Intraday and longer horizons
----------------------------

* HRRR irradiance
* RAP irradiance
* NAM cloud cover to irradiance
* GFS cloud cover to irradiance

The Arbiter derives irradiance forecasts from NAM and GFS cloud cover
forecasts to properly account for the solar position and time averaging. The
Arbiter will include options for bias-corrected NWP-based benchmark forecasts.


Probabilistic
-------------

* HRRRE

Calibration of probabilistic benchmark forecasts is a topic of discussion.


User-supplied benchmark forecasts
=================================

Some evalulation applications may require users to provide their own
benchmark forecasts. For example, Solar Forecasting 2, Topic Area 2
teams may choose to run an earlier version of WRF Solar and then upload
its forecasts for particular evaluation points. Benchmark models should
be run in consultation with the framework administrators. The framework
will accept uploaded forecasts for predefined evaluation point or
area-average values. The framework will not accept gridded datasets.


PV power forecasts
==================

The Arbiter will include functionality for converting benchmark solar
irradiance forecasts into benchmark solar power forecasts in simple,
auditable manner. The Arbiter will use solar power modeling functions
from the [pvlib-python](https://pvlib-python.readthedocs.io/en/latest/)
library.


Net load forecasts
==================

Net load is defined here as true system load minus behind the meter PV.
That is it. We make no allowance for wind power or utility scale solar power.
Net load is the load that must be served with utility scale resources,
regardless of whether or not they are dispatchable, conventional, or renewable.
Therefore, net load is *not equal* to the load that must be served with
conventional generation.

The Arbiter will include the capability to create benchmark net load
forecasts as defined above. This requires the development of a simple
benchmark load model.