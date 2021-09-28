---
layout: blog
author: Leland Boeman
---

The Solar Forecast Arbiter platform recently experienced two outages over the last week.
All systems were down and 

- September 17, 2021 19:00 - September 19, 2021 00:00

- September 27, 2021 01:00 - 12:40 UTC

During these periods the Solar Forecast Arbiter dashboard and api were inaccessible.

These outages were due to infrastructure failures that resulted in a loss of network
connectivity to applications hosted in our kubernetes cluster. We were unable to
definitively determine the cause of these infrastructure failures, but we were able
to identify repeated failures of non-essential processes that eventually caused an
imbalance in workload between worker nodes. The failures identified have been
fixed, and workload has been rebalanced between nodes. We also identified and
corrected issues with error reporting and monitoring of our infrastructure.

We will continue to monitor the situation to minimize the possibility of downtime.
