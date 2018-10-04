---
layout: base
permalink: /metrics/
---

## Metrics -- DRAFT

*Metric: a standard of measurement* -- [Merriam-Webster](https://www.merriam-webster.com/dictionary/metric)

This page contains summaries of the metrics that the Arbiter uses to
assess forecasts. Check back soon for more information.

Please send feedback to Will Holmgren at <a href="mailto:holmgren@email.arizona.edu">holmgren@email.arizona.edu</a>


Deterministic
-------------

* forecast and observation means
* forecast and observation variance/standard deviation
* MAE: Mean absolute error
* MAPE: Mean absolute percentage error
* MBE: Mean bias error
* RMSE: Root mean squared error
* NRMSE: Normalized root mean squared error
* CRMSE: Centered (unbiased) root mean squared error
* r: Pearson correlation coefficient
* KSI: Kolmogorov-Smirnov Integral
* FS: Forecast skill scores (typically based on RMSE of one or more benchmark forecasts)
* CSI: Critical success index
* Ramp metrics: to be determined.

Deterministic metrics must be understood within the context of the forecast
and observation mean and standard deviation.


Probabilistic
-------------

* REL: Reliability
* RES: Resolution
* Uncertainty
* BS: Brier score (and reliability, resolution, uncertainty decomposition)
* BSS: Brier skill score
* RPS: Ranked probability score
* RPSS: Ranked probability skill score
* CRPS: Continuous ranked probability score


Cost
----

Accurately determining economic loss or savings from forecasts is a
complicated problem that is unique to each forecast user. The Arbiter
will provide features to help users estimate the cost of forecast errors
and potential savings from improved forecasts. To do so, the Arbiter
relies on users to supply some amount of $/MW information:

* User supplied fixed $/MW (1 number)
* User supplied time of day $/MW (max 1440 numbers)
* User supplied time series of $/MW (N numbers)
* User supplied time series of $/MW for predefined MW error bins (NxM numbers)

The input data could be informed by the typical marginal cost of
generation, optionally as a function of time of day or year. More
complicated analyses can use the binned error approach to support an
approximation of a stack of resources that may be called upon depending
on the magnitude and direction of forecast error.


Graphics
--------

* Time series
* Forecast vs. observed scatter
* Histograms
* Taylor diagrams
* Reliability diagrams
* QQ diagrams


Customization
-------------

Framework adminstrators and users will be able to customize the
reporting of metrics. Options may include:

* Choice of metrics and graphics
* Time of year
* Time of day
* Solar position
* Forecast lead time
* Magnitude and direction of error


Concepts
--------

* Dimensionality
* Propriety


Examples
--------

This section will include examples of forecast errors. The examples will
show how bulk error statistics can illuminate and mislead.



References
----------

Here we list a handful of key references for solar forecast verification.

Jensen 2016: Metrics for evaluation of solar energy forecasts. NCAR Technical Note. NCAR/TN-527+STR [doi](http://dx.doi.org/10.5065/D6RX99GG)

Murphy 1993: What is a Good Forecast? An Essay on the Nature of Goodness in Weather Forecasting. [doi](http://dx.doi.org/10.1175/1520-0434(1993)008<0281:WIAGFA>2.0.CO;2)

Wilks 2011: Statistical Methods in the Atmospheric Sciences, Third Edition.

Zhang 2015: A suite of metrics for assessing the performance of solar power forecasting. Solar Energy 111, 157. [doi](http://dx.doi.org/10.1016/j.solener.2014.10.016)

[Model Evaluation Toolkit](https://dtcenter.org/met/users/index.php)