---
layout: base
permalink: /faq/
title: FAQ
---

# Frequently Asked Questions

## General

Q. Can I use the Solar Forecast Arbiter to analyze wind power forecasts?

A. Yes! When creating a new Site, select Power Power and simply ignore
the solar-specific information such as surface tilt. Then proceed to use
the Arbiter as normal. We are exploring what would need to be done to
better support wind forecasts in [this
issue](https://github.com/SolarArbiter/solarforecastarbiter-core/issues/491).

Q. Can I hide the identity of a power plant?

A. Sort of. See our [Anonymous Data blog
post](https://solarforecastarbiter.org/2019/09/30/Anonymous-Data.html)
for a full explanation.

Q. Who do I contact if I have a suggestion or I found a bug?

A. We encourage you to create an issue on our GitHub repositories. We
manage a few repositories but the [`solarforecastarbiter-core` issue
tracker](https://github.com/SolarArbiter/solarforecastarbiter-core/issues)
is likely where you want to report. If don't want to report the issue on
GitHub then please email us at
[admin@solarforecastarbiter.org](mailto:admin@solarforecastarbiter.org).

## Dashboard

Q. Can I instruct the Arbiter to create reference forecasts using NWP data or persistence models?

A. Not currently, but we hope to add this feature in the future. You can
install
[`solarforecastarbiter-core`](https://solarforecastarbiter-core.readthedocs.io/en/latest/installation.html)
to run these models on your local machine.

## API

Q. Is there a limit to the number of requests per hour that I can make?

A. The Arbiter API does not currently impose a limit. For requests of reasonable
size (i.e. response time is much less than request frequency) you can hit the
server as often as you want. However, the Auth0 API does impose a limit, so if
you are obtaining a new token with every request then you may be limited by
Auth0.

Q. Should I obtain a new token with every request?

A. Generally you should only obtain a new token when your current token is
nearing or past its expiration. Obtaining a token more frequently than is
necessary runs the risk of hitting Auth0's rate limit.

## Core

## Trials
