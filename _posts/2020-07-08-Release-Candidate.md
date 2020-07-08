---
layout: blog
author: Will Holmgren
---

The Solar Forecast Arbiter is out of beta and onto the "release candidate" phase!
This means that all of the important platform features are implemented and all known critical bugs are eliminated.
A 1.0 final version will follow in the next few months.
If you plan to use 1.0 final then you should start using 1.0-rc1 now to ensure that there are no issues when it really counts.

The new 1.0-rc1 version includes:

* Analysis reports can be created for probabilistic forecasts, including forecasts of distributions, quantiles, and thresholds.
* Cost metric support, including a constant cost factor, a time-of-day varying factor, a date-time varying factor, and a cost that depends on the magnitude of the error. A banded cost allows one to specify a cost similar to charges from a generator imbalance service as described in [FERC OATT](https://www.ferc.gov/industries-data/electric/power-sales-and-markets/open-access-transmission-tariff-oatt-reform).
* Missing forecast values may be filled using a fixed value or the last valid value. This is especially important in the context of an operational trial.
* Probabilistic reference forecasts using the persistence ensemble method.
* Net load observations and reference forecasts for the US ISO/RTOs: CAISO, ERCOT, ISO-NE, MISO, NYISO, PJM, and SPP.
* Climate zones integrated into the dashboard.
* Expanded and revised documentation.

As an example of a probabilistic forecast analysis, the figure below shows the continuous ranked probability score for the Arbiter's day ahead reference probabilistic GHI forecasts for SURFRAD, SOLRAD, and MIDC GHI observations in Climate Region 3: Desert Southwest and Southern US Rockies.
The analysis period is January 2020 - June 2020.
These reference forecasts are based on straightforward processing of the NOAA GEFS cloud cover.
Links to [html report](/assets/zone3crps/Zone_3_CRPS_html.zip), [pdf report](/assets/zone3crps/Zone_3_CRPS_pdf.zip), [metrics csv](/assets/zone3crps/Zone_3_CRPS_metrics.csv).

![crps](/assets/zone3crps/crps.png)

See the full [changelog here](https://solarforecastarbiter.org/changelog/) and visit [dashboard.solarforecastarbiter.org](https://dashboard.solarforecastarbiter.org) to get started.

We successfully ran our first test anonymous operational forecast trial June 4 - 6.
Two more test trials will occur in July.
Additional participants are welcome! Email [admin@solarforecastarbiter.org](mailto:admin@solarforecastarbiter.org) for more information on joining these trials.

We recorded a presentation on the Solar Forecast Arbiter for the June IEA Wind Forecasting Task 36 virtual conference. Click here to view it on YouTube.

**Reminder**: Your organization must sign the Data Use Agreement to access the full functionality of the Arbiter.
The DUA has been signed by private forecasters, utilities, national labs, and universities.
Signing the DUA allows your organization to:

* Create forecast analysis reports
* Upload private observation data
* Upload private forecast data
* Share observation or forecast data with other users
* Participate in forecast trials

Signed DUAs may be returned to [admin@solarforecastarbiter.org](mailto:admin@solarforecastarbiter.org)
