---
layout: base
permalink: /documentation/framework/
title: Framework Documentation
---

Solar Forecast Arbiter Design
=============================

The Solar Forecast Arbiter is an open source framework for the evaluation of solar irradiance, solar power and net-load forecasts. It is comprised of three software components: The API, Dashboard and Core library.
## Components

### Solar Forecast Arbiter Dashboard
The Dashboard is a website providing a graphical user interface for the Solar Forecast Arbiter framework. It provides webforms for exchanging data with the API and requesting analysis. It leverages the Core library to create visualizations for uploaded data and reports. The Dashboard is a Python Flask application that makes extensive use of Jinja2 templates.

**Alpha Version:**  [https://dashboard.solarforecastarbiter.org/](https://dashboard.solarforecastarbiter.org/)


**Documentation:** [https://solarforecastarbiter.org/documentation/dashboard/](https://solarforecastarbiter.org/documentation/dashboard/)

**Code:** [https://github.com/SolarArbiter/solarforecastarbiter_dashboard](https://github.com/SolarArbiter/solarforecastarbiter_dashboard)

### Solar Forecast Arbiter Core:
The Core library contains definitions for the data structures used throughout the framework. It also contains all of the data acquisition, data processing, analysis, and visualization code to be used by the other components of the framework. The core library is written in Python and makes extensive use of libraries such as pvlib python, pandas, xarray, and bokeh.

**Code:** [https://github.com/SolarArbiter/solarforecastarbiter-core](https://github.com/SolarArbiter/solarforecastarbiter-core)

**Documentation:** [https://solarforecastarbiter-core.readthedocs.io](https://solarforecastarbiter-core.readthedocs.io)

### Solar Forecast Arbiter API
The API is a HTTP REST API for programatically exchanging data with the Solar Forecast Arbiter. The API handles all user authentication and database interaction. To handle requests, the API adds to a queue of tasks to be performed by worker processes. Because the API is closely tied to the Database and Queue, it contains code for initializing these services. The API is a Python Flask application that makes extensive use of sqlalchemy, rq(Redis Queue), and marshmallow.

**Alpha Version/Documentation:** [https://api.solarforecastarbiter.org/](https://api.solarforecastarbiter.org/)

**Code:** [https://github.com/SolarArbiter/solarforecastarbiter-api](https://github.com/SolarArbiter/solarforecastarbiter-api)

## Architecture

<img class="figure" src="/images/architecture_chart.png"/>

<figcaption class="figure">Diagram depicting data flow between components of the Solar Forecast Arbiter. Users may choose to interact with the API directly, or through Dashboard. The API stores and retrieves data with the Database. The API queues analyses to be processed by workers that send their results to the API for storage in the API.</figcaption>

<br/>
The alpha release of the Solar Forecast Arbiter is hosted on a server running CentOS at a datacenter at the University of Arizona. The components are run on an OKD (Origin Kubernetes Distribution) cluster and depend on a separate MYSQL server for data storage. The infrastructure of the Solar Forecast Arbiter is documented in detail in our Systems Layer Setup document.
