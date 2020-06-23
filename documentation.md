---
layout: base
permalink: /documentation/
title: Documentation
---

Solar Forecast Arbiter Documentation
====================================

The Solar Forecast Arbiter is an open source framework for the evaluation of
solar irradiance, solar power, and net-load forecasts. It is comprised of
three software components: the API, Dashboard and Core library.


<div class="row my-5">
<div class="col-md-7 col-xs-12">
<h2 id="solar-forecast-arbiter-dashboard">Solar Forecast Arbiter Dashboard</h2>
<p>
The Dashboard is a website providing a graphical user interface for the Solar
Forecast Arbiter framework. It provides web forms for exchanging data with the
API and requesting analyses. It leverages the Core library to create
visualizations for uploaded data and reports. The Dashboard is a Python Flask
application that makes extensive use of Jinja2 templates.
</p>

<a href="https://dashboard.solarforecastarbiter.org/">https://dashboard.solarforecastarbiter.org/</a><br/>

<b>Documentation:</b> <a href="https://solarforecastarbiter.org/documentation/dashboard/">https://solarforecastarbiter.org/documentation/dashboard/</a><br/>

<b>Code:</b> <a href="https://github.com/SolarArbiter/solarforecastarbiter_dashboard">https://github.com/SolarArbiter/solarforecastarbiter_dashboard</a>
</div>
<div class="col-md-5 col-xs-12">
<img class="shadow" src="/images/dashboard_screenshot.png"/>
</div>
</div>

<div class="row my-5">
<div class="col-md-7 col-xs-12">
<h2>Solar Forecast Arbiter API</h2>
<p>
The API is a HTTP REST API for programatically exchanging data with the Solar
Forecast Arbiter. The API handles all user authentication and database
interaction. To handle requests, the API adds to a queue of tasks to be
performed by worker processes. Because the API is closely tied to the Database
and Queue, it contains code for initializing these services. The API is
a Python Flask application that makes extensive use of sqlalchemy,
rq(Redis Queue), and marshmallow.
</p>

<b>Documentation:</b> <a href="https://api.solarforecastarbiter.org/">https://api.solarforecastarbiter.org/</a><br/>
<b>Code:</b> <a href="https://github.com/SolarArbiter/solarforecastarbiter-api">https://github.com/SolarArbiter/solarforecastarbiter-api</a><br/>
</div>
<div class="col-md-5 col-xs-12">
<img class="shadow" src="/images/api_screenshot.png"/>
</div>
</div>

<div class="row my-5">
<div class="col-md-7 col-xs-12">
<h2>Solar Forecast Arbiter Core</h2>
<p>
The Core library contains definitions for the data structures used throughout
the framework. It also contains all of the data acquisition, data processing,
analysis, and visualization code to be used by the other components of the
framework. The core library is written in Python and makes extensive use of
libraries such as pvlib python, pandas, xarray, bokeh, and plotly.
</p>
<b>Code:</b> <a href="https://github.com/SolarArbiter/solarforecastarbiter-core">https://github.com/SolarArbiter/solarforecastarbiter-core</a><br/>

<b>Documentation:</b> <a href="https://solarforecastarbiter-core.readthedocs.io">https://solarforecastarbiter-core.readthedocs.io</a><br/>
</div>
<div class="col-md-5 col-xs-12">
<div class="d-flex h-100 shadow">
<img class="align-self-center" src="/images/python-logo-master-v3-TM.png">
</div>
</div>
</div>

## Architecture

<img class="figure" src="/images/architecture_chart.png"/>

<figcaption class="figure">
Diagram depicting data flow between components of the Solar Forecast Arbiter.
Most users will use the Dashboard to interact with the API. Some users may
choose to use a local installation of the Core library to perform their
analyses and interact with the API. Other users may choose to interact
directly with the API for scripting purposes (not shown). The API stores and
retrieves data with the Database. The API also queues analyses to be processed
by workers running the Core library. The works then send their results to the
API for storage in the database.</figcaption>

<br/>
The Solar Forecast Arbiter is hosted on a server running CentOS at a datacenter
at the University of Arizona. The components are run on an OKD (Origin
Kubernetes Distribution) cluster and depend on a separate MYSQL server for
data storage. The infrastructure of the Solar Forecast Arbiter is documented
in detail in a Systems Layer Setup document (available on request).
