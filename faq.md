---
layout: base
permalink: /faq/
sidebar: faq_sidebar.html
title: FAQ
---
<link href="/css/faq.css" type="text/css" rel="stylesheet">

# Frequently Asked Questions
{: .anchor }

## General
{: .anchor }
---

- Q. Can I use the Solar Forecast Arbiter to analyze wind power forecasts?

  A. Yes! When creating a new Site, select Power Power and simply ignore the
  solar-specific information such as surface tilt. Then proceed to use the
  Arbiter as normal. We are exploring what would need to be done to better
  support wind forecasts in [this
  issue](https://github.com/SolarArbiter/solarforecastarbiter-core/issues/491).

- Q. Can I hide the identity of a power plant?

  A. Sort of. See our [Anonymous Data blog
  post](https://solarforecastarbiter.org/2019/09/30/Anonymous-Data.html) for a
  full explanation.

- Q. Who do I contact if I have a suggestion or I found a bug?

  A. We encourage you to create an issue on our GitHub repositories. We manage a
  few repositories but the [`solarforecastarbiter-core` issue
  tracker](https://github.com/SolarArbiter/solarforecastarbiter-core/issues) is
  likely where you want to report. If don't want to report the issue on GitHub
  then please email us at
  [admin@solarforecastarbiter.org](mailto:admin@solarforecastarbiter.org).

- Q. I'm having trouble accessing `solarforecastarbiter.org` or
  `dashboard.solarforecastarbiter.org`. Any ideas?

  A. Some users at utilities have reported similar problems. The best course of
  action is to ask your IT department as there is not a single solution that we
  are aware of.

- Q. What's the meaning of the parameter *issue time of day* for a forecast that
  is issued multiple times per day?

  A. *Issue time of day* is defined only once even for forecasts that are issued
  multiple times per day. That situation, it defines a single issue time of day,
  then the ``run length`` defines all subsequent issue times. So it doesn’t
  really matter if you specify, say, 1 or 2 or 11 am for a forecast that is
  issued on the hour. But you could also do things like issue time of day =
  0045, lead time to start = 75 minutes to represent the start of the CAISO real
  time market window. The flexibility is powerful but a bit confusing.

## Dashboard
{: .anchor }
---

- Q. Can I instruct the Arbiter to create reference forecasts using NWP
  data or persistence models for my own sites?

  A. Not currently, but we hope to add this feature for historical data. You can
  install
  [`solarforecastarbiter-core`](https://solarforecastarbiter-core.readthedocs.io/en/latest/installation.html)
  to run these models on your local machine and obtain true forecasts. We can
  also run custom reference forecasts in a
  [trial](/documentation/dashboard/trials/).


## API
{: .anchor }
---

- Q. Is there a limit to the number of requests per hour that I can make?

  A. The Arbiter API does not currently impose a limit. For requests of
  reasonable size (i.e. response time is much less than request frequency) you
  can hit the server as often as you want. However, the Auth0 API does impose a
  limit, so if you are obtaining a new token with every request then you may be
  limited by Auth0.

- Q. Should I obtain a new token with every request?

  A. Generally you should only obtain a new token when your current token is
  nearing or past its expiration. Obtaining a token more frequently than is
  necessary runs the risk of hitting Auth0's rate limit.

- Q. Can I upload data to multiple forecasts or observations at once?

  A. No. A separate POST request must be made to each forecast or observation
  endpoint. The benefit is that the format is exactly the same for all uploads,
  so there is no need to worry about any nuance in file names, csv column names,
  or json keys.

- Q. How do I associate my data with UUIDs?

  A. A brute force answer is a hardcoded dictionary or other mapping with keys
  that are your e.g. PI names and values that are the SFA UUIDs. Another option
  is to record your own resource name in the SFA’s observation metadata extra
  parameters field, then search/filter the observations for the right one/ones,
  then pull the UUID from the found object.

- Q. Do you have any examples?

  A. The [API documentation](https://api.solarforecastarbiter.org/) contains a
  number of request and response examples. For examples using the Python API
  wrapper, please see the [data_upload_download
  notebook](https://github.com/SolarArbiter/workshop/blob/master/data_upload_download.ipynb)
  in our [workshop repository](https://github.com/SolarArbiter/workshop). You
  can actually run that notebook using
  [MyBinder](https://mybinder.org/v2/gh/SolarArbiter/workshop/master) if you
  want a very quick start.

- Q. I can access the dashboard using my credentials but not the API. Why not?

  A. If you're behind a firewall, there is a good chance that is causing
  problems with reaching our identity provider, Auth0. If you're using the SFA
  core library or the python ``requests`` library, you can get around this by
  copying the PEM chain certificate for
  https://solarforecastarbiter.auth0.com/oauth/token to your machine and setting
  the ``REQUESTS_CA_BUNDLE`` environment variable to the path to the
  certificate.

- Q. Any tips for trying to get data streaming from PI and into the Arbiter?

  A. If you're able to use Python, we've heard good things about
  [PIConnect](https://pypi.org/project/PIconnect/). Combine that with our Python
  wrapper of the API and hopefully you'll be able to establish data feeds
  relatively quickly.

## Core
{: .anchor }
---

- Q. How do I install the core framework?

  A. Please see the [installation instructions](https://solarforecastarbiter-core.readthedocs.io/en/latest/installation.html).

- Q. I'd like to create reference forecasts on my own machine. Do you have any
  recommendations for how to make that work?

  A. If you're only using persistence forecasts then it's relatively
  straightforward. If you want to use NWP data then it's much more complicated
  due primarily to the dependency on ``wgrib``. The most reliable solution is to
  run the NWP data fetch in the [Arbiter docker
  image](https://quay.io/repository/solararbiter/solarforecastarbiter-core?tab=tags).
  Please see [docker](https://docs.docker.com/), the [core cli
  documentation](https://solarforecastarbiter-core.readthedocs.io/en/latest/cli.html),
  and run ``solararbiter fetchnwp -h`` for help. Once the data is available
  locally you can process it into irradiance or power forecasts using a
  ``solarforecastarbiter-core`` installation in your native OS.

## Trials
{: .anchor }
---

- Q. I'm interested in conducting a forecast trial using the Solar
  Forecast Arbiter. What do I need to get started?

  A. There are a few steps to organizing a trial on the Solar Forecast Arbiter.
    1. See the [Trials Documentation](/documentation/dashboard/trials/)
       and consider the specifications of the trial and contact
       [admin@solarforecastarbiter.org](mailto:admin@solarforecastarbiter.org)
       when ready. The administrators can help design the trial and
       reach out to vendors.
    2. If you're planning to provide measurements to forecast vendors (this is
       preferred), see the notes on [Data
       Upload](/documentation/dashboard/trials/#data-upload) and consider the IT
       requirements of providing data when considering the timeframe of the
       trial.
    3. Send a signed [Data Use Agreement](/assets/45864 Approved_Final version
       1.1.pdf) to
       [admin@solarforecastarbiter.org](mailto:admin@solarforecastarbiter.org)
       if your company has not signed it.

- Q. The metadata is inconsistent with other records and/or with observed data.
  What should we do?

  A. Please let the trial administrators know of the inconsistency, but note
  that trials are always evaluated against the observed data regardless of the
  accuracy of the metadata.

- Q. Can I access the trial data using my own account or must I use the
  anonymous account created for me for the trial?

  A. You must log in with your anonymous account. We do it this way so that we
  do not need to retain any record of who’s who in our system, thus minimizing
  the amount of trust you must place in us as the administrators. You are the
  only person that knows which anonymous account is yours and only you can
  choose to reveal that to someone. If we instead extend the read/write
  permissions to your personal account then in principal we could retrieve the
  association by inspecting the permissions in the database (we would never do
  that!).
