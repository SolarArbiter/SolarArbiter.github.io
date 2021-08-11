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
<hr>

- Q. Can I use the Solar Forecast Arbiter to analyze wind power forecasts?

  A. Yes! When creating a new Site, select Power Power and simply ignore
the solar-specific information such as surface tilt. Then proceed to use
the Arbiter as normal. We are exploring what would need to be done to
better support wind forecasts in [this
issue](https://github.com/SolarArbiter/solarforecastarbiter-core/issues/491).

- Q. Can I hide the identity of a power plant?

  A. Sort of. See our [Anonymous Data blog
post](https://solarforecastarbiter.org/2019/09/30/Anonymous-Data.html)
for a full explanation.

- Q. Who do I contact if I have a suggestion or I found a bug?

  A. We encourage you to create an issue on our GitHub repositories. We
manage a few repositories but the [`solarforecastarbiter-core` issue
tracker](https://github.com/SolarArbiter/solarforecastarbiter-core/issues)
is likely where you want to report. If don't want to report the issue on
GitHub then please email us at
[admin@solarforecastarbiter.org](mailto:admin@solarforecastarbiter.org).

## Dashboard
{: .anchor }
<hr/>

- Q. Can I instruct the Arbiter to create reference forecasts using NWP data or persistence models?

  A. Not currently, but we hope to add this feature in the future. You can
install
[`solarforecastarbiter-core`](https://solarforecastarbiter-core.readthedocs.io/en/latest/installation.html)
to run these models on your local machine.


## API
{: .anchor }
<hr/>

- Q. Is there a limit to the number of requests per hour that I can make?

  A. The Arbiter API does not currently impose a limit. For requests of reasonable
size (i.e. response time is much less than request frequency) you can hit the
server as often as you want. However, the Auth0 API does impose a limit, so if
you are obtaining a new token with every request then you may be limited by
Auth0.

- Q. Should I obtain a new token with every request?

  A. Generally you should only obtain a new token when your current token is
nearing or past its expiration. Obtaining a token more frequently than is
necessary runs the risk of hitting Auth0's rate limit.

- Q. Can I upload data to multiple forecasts/observations at once?

  A. No. A separate POST request will need to be made to each forecast or
observations endpoints.

## Core
{: .anchor }
<hr/>

## Trials
{: .anchor }
<hr/>

- Q. I'm interesting in conducting a forecast trial using the Solar Forecast Arbiter.
  What do I need to get started?

  A. There are a few steps to organizing a trial on the Solar Forecast Arbiter.
    1. Send a signed [Data Use Agreement](/assets/45864 Approved_Final version 1.1.pdf) to
       [admin@solarforecastarbiter.org](mailto:admin@solarforecastarbiter.org) if
       you don't already belong to an organization.
    2. See the [Trials Documentation](/documentation/dashboard/trials/) and consider the
       specifications of the trial and contact
       [admin@solarforecastarbiter.org](mailto:admin@solarforecastarbiter.org) when
       ready. If you're planning to provide measurements to forecast vendors, see the notes
       on [Data Upload](/documentation/dashboard/trials/#data-upload) and consider the 
       IT requirements of providing data when considering the timeframe of the trial.
