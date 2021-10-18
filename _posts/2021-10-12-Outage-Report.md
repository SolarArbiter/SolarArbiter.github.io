---
layout: blog
author: Will Holmgren
---

**Updated Oct 18, 2021**

The Solar Forecast Arbiter dashboard and API were not available from
approximately 2021-10-12 02 UTC to 2021-10-16 18 UTC.

From 2021-10-16 18 UTC through 2021-10-17 18 UTC several features remained
unavailable, specifically validation of observation data and report computation.
During this time uploads of observation data successfully inserted data into the
Arbiter's database, but still returned a failed status because the data
validation could not be scheduled.

The operational forecast evaluations will exclude the forecast
submissions that were scheduled to occur from 2021-10-12 02 UTC to 2021-10-17 18
UTC.

The downtime was due to a traffic routing issue that arose after addressing
expiring certificates used to secure traffic within the OpenShift Origin cluster
that the Solar Forecast Arbiter runs on. We will write a longer post-mortem over
the next few weeks.
