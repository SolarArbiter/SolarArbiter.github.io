---
layout: base
mathjax: true
permalink: /metrics/
sidebar: metrics_sidebar.html
title: Metrics
---

# Metrics
{: .anchor }
The Solar Forecast Arbiter evaluation framework provides a suite of metrics for evaluating deterministic and probablistic solar forecasts. These metrics are used for different purposes, e.g., comparing the forecast and the measurement, comparing the performance of multiple forecasts, and evaluating an event forecast.


## Metrics for Deterministic Forecasts
{: .anchor }
The following metrics provide measures of the performance of deterministic forecasts. Each metric is computed from a set of $$ n $$ forecasts $$ (F_1, F_2, \dots, F_n) $$ and corresponding observations $$ (O_1, O_2, \dots, O_n) $$.

In the metrics below, we adopt the following nomenclature:
- $$ n : $$ number of samples
- $$ F : $$ forecasted value
- $$ O : $$ observed (actual) value
- $$ \text{norm} : $$ normalizing factor (with the same units as the forecasted and observed values)
- $$ \bar{F}, \, \bar{O} : $$ the mean of the forecasted and observed values, respectively

For more information on these metrics and others, see [Zhang15](#ref-zhang15), [Wilks11](#ref-wilks11) and the references listed below.


### Mean Absolute Error (MAE) {#mae}
{: .anchor }
The absolute error is the absolute value of the difference between the forecasted and observed values. The MAE is defined as:

$$ \text{MAE} = \frac{1}{n} \sum_{i=1}^n  \lvert F_i - O_i \rvert $$


### Mean Bias Error (MBE) {#mbe}
{: .anchor }
The bias is the difference between the forecasted and observed values. The MBE is defined as:

$$ \text{MBE} = \frac{1}{n} \sum_{i=1}^n (F_i - O_i) $$


### Root Mean Square Error (RMSE) {#rmse}
{: .anchor }
The RMSE is the square root of the averaged of the squared differences between the forecasted and observed values, and is defined as:

$$ \text{RMSE} = \sqrt{ \frac{1}{n} \sum_{i=1}^n (F_i - O_i)^2 } $$

RMSE is a frequently used measure for evaluating forecast accuracy. Since the errors are squared before being averaged, the RMSE gives higher weight to large errors.


### Forecast Skill ($$ s $$) {#s}
{: .anchor }
The forecast skill measures the performance of a forecast relative to a reference forecast ([Marquez12](#ref-marquez12)). The Solar Forecast Arbiter uses the definition of forecast skill based on RMSE:

$$ s = 1 - \frac{\text{RMSE}_f}{\text{RMSE}_{\text{ref}}} $$

where $$ \text{RMSE}_f $$ is the RMSE of the forecast of interest, and $$ \text{RMSE}_{\text{ref}} $$ is the RMSE of the reference forecast, e.g., persistence.


### Mean Absolute Percentage Error (MAPE) {#mape}
{: .anchor }
The absolute percentage error is the absolute value of the difference between the forecasted and observed values,

$$ \text{MAPE} = 100\% \cdot \frac{1}{n} \sum_{i=1}^n | \frac{F_i - O_i}{O_i} | $$


### Normalized Root Mean Square Error (NRMSE) {#nrmse}
{: .anchor }
The NRMSE [%] is the normalized form of the RMSE and is defined as:

$$ \text{RMSE} = \frac{100\%}{\text{norm}} \cdot \sqrt{ \frac{1}{n} \sum_{i=1}^n (F_i - O_i)^2 } $$


### Centered (unbiased) Root Mean Square Error (CRMSE) {#crmse}
{: .anchor }
The CRMSE describes the variation in errors around the mean and is defined as:

$$ \text{CRMSE} = \sqrt{ \frac{1}{n} \sum_{i=1}^n \left( (F_i - \bar{F}) - (O_i - \bar{O}) \right)^2 } $$

The CRMSE is related to the RMSE and MBE through $$ \text{RMSE}^2 = \text{CRMSE}^2 + \text{MBE}^2 $$, and can be decomposed into components related to the standard deviation and correlation coefficient:

$$ \text{CRMSE}^2 = \sigma_F^2 + \sigma_O^2 - 2 \sigma_F \sigma_O r $$

where $$ \sigma_F $$ and $$ \sigma_O $$ are the standard deviations of the forecast and observation, respectively, and $$ r $$ is the correlation coefficient.


### Pearson Correlation Coefficient ($$ r $$) {#r}
{: .anchor }
Correlation indicates the strength and direction of a linear relationship between two variables. The Pearson correlation coefficient, aka, the sample correlation coefficient, measures the linear dependency between the forecasted and observed values, and is defined as the ratio of the covariance of the variables to the product of their standard deviation:

$$ r = \frac{ \sum_{i=1}^n (F_i - \bar{F}) (O_i - \bar{O}) }{
\sqrt{ \sum_{i=1}^n (F_i - \bar{F})^2} \times \sqrt{ \sum_{i=1}^n (O_i - \bar{O})^2 } } $$


### Coefficient of Determination ($$ R^2 $$) {#r2}
{: .anchor }
The coefficient of determination measures the extent that the variability in the forecast errors is explained by variability in the observed values, and is defined as:

$$ R^2 = 1 - \frac{ \sum_{i=1}^n (O_i - F_i)^2 }{ \sum_{i=1}^n (O_i - \bar{O})^2 } $$

By this definition, a perfect forecast has a $$ R^2 $$ value of 1.


### Kolmogorov-Smirnov Test Integral (KSI) {#ksi}
{: .anchor }
The KSI quantifies the level of agreement between the cumulative distribution function (CDFs) of the forecasted and observed values ([Espinar09](#ref-espinar09)), and is defined as:

$$ \text{KSI} = \int_{p_{\text{min}}}^{p_{\text{max}}} D_n(p) dp $$

where $$ p_{\text{min}} $$ and $$ p_{\text{max}} $$ are the minimum and maximum values of the union of forecast and observed values, and $$ D_n(p) $$ is the absolute difference between the two empirical CDFs:

$$ D_n(p) = \text{max}( | \text{CDF}_O(p) - \text{CDF}_F(p) | )$$

A KSI value of zero implies that the CDFs of the forecast and observed values are equal.

KSI can be normalized as:

$$ KSI (\%) = \frac{100}{a_{\text{critical}}} KSI $$

where $$ a_{\text{critical}} = V_c (p_{\text{max}} - p_{\text{min}}) $$ and $$ V_c = 1.63 / \sqrt{n} $$. When $$ n \geq 35 , $$ the normalized KSI can be interpreted as a statistic that tests the hypothesis that the two empirical CDFs represent samples drawn from the same population.


### OVER
{: .anchor }
Conceptually, the OVER metric modifies the KSI to quantify the difference between the two CDFs, but only where the CDFs differ by more than a critical limit $$ V_c $$ ([Espinar09](#ref-espinar09)). The OVER metric is calculated as:

$$ OVER = \int_{p_{\text{min}}}^{p_{\text{max}}} D_n^* dp $$

where

$$ D_n^* = \begin{cases}
    \displaystyle D_n - V_c & \text{if} & D_n > V_c \\
    \displaystyle 0 & \text{if} & D_n \leq V_c
\end{cases} $$

The OVER metric can be normalized using the same approach as for KSI.


### Combined Performance Index (CPI) {#cpi}
{: .anchor }
The CPI provides a measure of the agreement between the distributions of forecasted and observed values, and the overall error by combining KSI, OVER and RMSE ([Gueymard12](#ref-gueymard12)):

$$ \text{CPI} = \frac{1}{4} ( \text{KSI} + \text{OVER} + 2 \times \text{RMSE} ) $$


## Metrics for Deterministic Event Forecasts
{: .anchor }
An event is defined by values that exceed or fall below a threshold. A typical event is the ramp in power of solar generation, which is determine by:

$$ | P(t + \Delta t) - P(t) | > \text{Ramp Forecasting Threshold} $$

where $$ P(t) $$ is the solar power output at time $$ t $$ and $$ \Delta t $$ is the duration of the ramp event.

Based on the predefined threshold, all observations or forecasts can be evaluated by placing them in either the "event occurred" (Positive) or "event did not occur" (Negative) categories. Then individual pairs of forecasts and observations can be placed into one of four groups based on whether the event forecast agrees (or disagrees) with the event observed value:

- True Positive (TP): Forecast = Event, Observed = Event
- False Positive (FP): Forecast = Event, Observed = No Event
- True Negative (TN): Forecast = No Event, Observed = No Event
- False Negative (FN): Forecast = No Event, Observed = Event

By then counting the the number of TP, FP, TN and FN values, the following metrics can be computed:


### Probability of Detection (POD)
{: .anchor }
The POD is the fraction of observed events correctly forecasted as events:

$$ POD = \frac{TP}{TP + FN} $$


### False Alarm Ratio (FAR)
{: .anchor }
The FAR is the fraction of forecasted events that did not occur:

$$ FAR = \frac{FP}{TP + FP} $$


### Probability of False Detection (POFD)
{: .anchor }
The POFD is the fraction of observed non-events that were forecasted as events:

$$ POFD = \frac{FP}{FP + TN} $$


### Critical Success Index (CSI)
{: .anchor }
The CSI evaluates how well an event forecast predicts observed events, e.g., ramps in irradiance or power. THe CSI is the relative frequency of hits, i.e., how well predicted "yes" events correspond to observed "yes" events:

$$ CSI = \frac{TP}{TP + FP + FN} $$


### Event Bias (EBIAS)
{: .anchor }
The EBIAS is the ratio of counts of forecast and observed events:

$$ EBIAS = \frac{TP + FP}{TP + FN} $$


### Event Accuracy (EA)
{: .anchor }
The EA is the fraction of events that were forecasted correctly, i.e., forecast = "yes" and observed = "yes" or forecast = "no" and observed = "no":

$$ EA = \frac{TP + TN}{TP + FP + TN + FN} = \frac{TP + TN}{n} $$

where $$ n $$ is the number of samples.


## Metrics for Probablistic Forecasts
{: .anchor }
Probablistic forecasts represent uncertainty in the forecast quantity by providing a probability distribution or a prediction interval, rather than a single value.

In the metrics below, we adopt the following nomenclature:

- $$ F(t_k) : $$ probability forecast for an event $$ o $$ at each time $$ t_k $$
- $$ f_i : $$ discrete values that appear in the probability forecast $$ F $$
- $$ o(t_k) : $$ indicator for event $$ o $$: $$ o(t_k) = 1 $$ if an event occurs at time $$ t_k $$ and $$ o(t_k) = 0 $$ otherwise
- $$ N_i : $$ the number of times each forecast value $$ f_i $$ appears in the forecast $$ F $$
- $$ n = \sum_{i=1}^I N_i : $$ number of forecast events
- $$ p(f_i) = \frac{N_i}{n} : $$ the relative frequency of each forecast value $$ f_i $$ in the forecast $$ F $$
- $$ \bar{o}_i = p(o_i \| f_i ) = \frac{1}{N_i} \sum_{k \in N_i} o_k : $$ the average of $$ o(t_k) $$ at the $$ N_i $$ times $$ t_k $$ when $$ F(t_k) = f_i $$

- $$ \bar{o} = \frac{1}{n} \sum_{k=1}^n o(t_k) = \frac{1}{n} \sum_{i=1}^I N_i \bar{o}_i : $$ the average of $$ o(t_k) $$ for all times $$ t_k $$


### Brier Score (BS) {#bs}
{: .anchor }
The BS measures the accuracy of forecast probability for one or more events ([Brier50](#ref-brier50)). For events with binary outcomes, BS is defined as:

$$ \text{BS} = \frac{1}{n} \sum_{i=1}^n (f_i - o_i)^2  $$

Smaller values of BS indicate better agreement between forecasts and observations. Note that while BS can be generalized to events with more than two outcomes, the Solar Forecast Arbiter only includes built-in support for the (more commonly used) binary events definition. For more info, see Section 7.4.2. of [Wilks11](#ref-wilks11).

When the probability forecast takes on a finite number of values (e.g. 0.0, 0.1, ..., 0.9, 1.0), the BS can be decomposed into a sum of three metrics that give additional insight into a probability forecast ([Murphy73](#ref-murphy73)):

$$ \text{BS} = \text{REL} - \text{RES} + \text{UNC} $$

where REL is the reliability, RES is the resolution and UNC is the uncertatinty, as defined below.


### Reliability (REL) {#rel}
{: .anchor }
The REL is given by:

$$ \text{REL} = \frac{1}{n} \sum_{i=1}^I N_i (f_i - \bar{o}_i)^2 $$

Reliability is the weighted averaged of the squared differences between the forecast probabilities $$ f_i $$ and the relative frequencies of the observed event in the forecast subsample of times where $$ F(t_k) = f_i $$. A forecast is perfectly reliably if $$ \text{REL} = 0 $$. This occurs when the relative event frequency in each subsample is equal to the forecast probability for the subsample.


### Resolution (RES) {#res}
{: .anchor }
The RES is given by:

$$ \text{RES} = \frac{1}{n} \sum_{i=1}^I N_i (\bar{o}_i - \bar{o})^2 $$

Resolution is the weighted averaged of the squared differences between the relative event frequency for each forecast subsample and the overall event frequency. Resolution measures the forecast's ability to produce subsample forecast periods where the event frequency is different. Higher values of RES are desirable.


### Uncertainty (UNC) {#unc}
{: .anchor }
The UNC is given by:

$$ \text{UNC} = \bar{o} (1 - \bar{o})$$

Uncertainty is the variance of the event indicator $$ o(t) $$. Low values of UNC indicate that the event being forecasted occurs only rarely.


### Brier Skill Score (BSS) {#bss}
{: .anchor }
The BSS is based on the BS and measures the performance of a probability forecast relative to a reference forecast:

$$ BSS = 1 - \frac{\text{BS}_f}{\text{BS}_{\text{ref}}} $$

where $$ \text{BS}_f $$ is the BS of the forecast of interest, and $$ \text{BS}_{\text{ref}} $$ is the BS of the reference forecast. BSS greater than zero indicates the forecast performed better than the reference and vice versa for BSS less than zero, while BSS equal to zero indicates the forecast is no better (or worse) than the reference.


### Sharpness (SH) {#sh}
{: .anchor }
The SH represents the degree of "concentration" of a forecast comprising a prediction interval of the form $$ [ f_l, f_u ] $$ within which the forecast quantity is expected to fall with probability $$ 1 - \beta $$. A good forecast should have a low sharpness value. The prediction interval endpoints are associated with quantiles $$ \alpha_l $$ and $$ \alpha_u $$, where $$ \alpha_u - \alpha_l = 1 - \beta $$. For a single prediction interval, the SH is:

$$ \text{SH} = f_u - f_l $$

and for a timeseries of prediction intervals, the SH is given by the average:

$$ \text{SH} = \frac{1}{n} \sum_{i=1}^n f_{u,i} - f_{l, i} $$


### Continuous Ranked Probability Score (CRPS) {#crps}
{: .anchor }
The CRPS is a score that is a designed to measure both the reliability and sharpness of a probablistic forecast ([Matheson76](#ref-matheson76)). For a timeseries of forecasts comprising a CDF at each time point, the CRPS is:

$$ \text{CRPS} = \frac{1}{n} \sum_{i=1}^n \int ( F_i(x) - O_i(x) )^2 dx $$

where $$ F_i(x) $$ is the CDF of the forecast quantity $$ x $$ at time point $$ i $$, and $$ O_i(x) $$ is the CDF associated with the observed value $$ x_i $$:

$$ O_i = \begin{cases}
    \displaystyle 0 & x < x_i \\
    \displaystyle 1 & x \geq x_i
\end{cases} $$

The CRPS reduces to the mean absolute error (MAE) if the forecast is deterministic.


## Value Metrics
{: .anchor }
Forecasts can provide economic value in a number of different ways. At a system operator (balancing authority) level they improve scheduling of the system by more effectively committing and dispatching resources to balance supply and demand. This can result in reduced start-up of quick start units, more effective use of cheaper generation resources and better use of storage to manage variability. Forecasts can also provide financial benefits to plant owners, traders, and other market participants by allowing them to improve bidding strategies or otherwise reduce risks.

There are two main approaches to assessing cost-related impacts of forecasts: 1) as a function of forecast error (e.g. $/MW of RMSE) and 2) simulations using a production cost model (PCM). Both approaches focus on the value from decisions made based on the forecasts and do not include secondary costs, e.g., the cost to develop and deploy the forecast models. The Solar Forecast Arbiter will only include built-in support for evaluating value as a function of error, but we provide a brief introduction to production cost modeling (see below) for users interested in more accurate assessments.


### Value as a Function of Error
{: .anchor }
Let $$ \text{cost} $$ be the cost incurred due to forecast error when, say, operating a system or participating in a market. This cost can be written as:

$$ \text{cost} = \sum_{i=1}^n C_i(S(F_i, O_i)) , $$

where $$ S(\cdot) $$ is a measure of the error between the forecast ($$ F_i $$) and observation ($$ O_i $$), and $$ C_i(\cdot) $$ are functions that map the forecast error to a cost. In the simplest case, all the $$ C_i(\cdot)$$ are identical and defined as a constant cost per error value (e.g. [$/MW of RMSE]):


$$ \text{cost} = C \cdot S(F, O) . $$

However, the $$ C_i(\cdot)$$ can be defined such that the cost per error varies as a function of time (e.g. on-peak vs off-peak or weekday vs weekend) or as a function of error magnitude (e.g. costs increasing in tiers, with larger errors costing more than smaller errors). For example, a on-peak/off-peak cost could be defined as:

$$ C_i = \begin{cases}
    \displaystyle C_1 & \text{4pm} \leq \text{time} \leq \text{8pm} \\
    \displaystyle C_2 & \text{otherwise}
\end{cases} $$

where $$ C_1 \gg C_2 $$, i.e., the cost of misforecasts during on-peak periods is greater than during off-peak. Similarly, the cost could be defined in tiers based on the error magnitude:

$$ C_i = \begin{cases}
    \displaystyle C_1 & \text{error} \leq 20\% \\
    \displaystyle C_2 & 20 < \text{error} \leq 50\% \\
    \displaystyle C_3 & \text{error} > 50\%
\end{cases} $$

where $$ C_1 < C_2 < C_3 $$.

While this approach is straightforward to interpret, a key challenge is how to determine the $$ C_i(\cdot) $$. The $$ C_i(\cdot) $$ could be based on analysis of historical data such as real-time energy prices, differences between day-ahead and real-time prices, reserve prices (where reserve depends on forecast error) or suitable proxies for non-ISO regions. The Solar Forecast Arbiter relies on users to supply the $$ C_i(\cdot) $$ relevant to their forecast application.

The monetary value of an improved forecast ($$ \text{value}_f $$) is then defined as:

$$ \text{value}_f = \text{cost}_{f} - \text{cost}_{\text{ref}}, $$

where $$ \text{cost}_f $$ and $$ \text{cost}_{\text{ref}} $$ refer to the costs of the selected forecast and reference forecast, respectively. Note that the choice of the reference forecast is crucial and should be consistent with current operational practices.


### Production Cost Modeling
{: .anchor }
An alternative approach (not implemented by the Solar Forecast Arbiter) is to perform simulations using a production cost model (PCM) and then compare differences in costs incurred when using different forecasts. In addition to providing a more direct evaluation of the forecasts, simulations can provide insight into future value, e.g., how improved forecasts can improve system operations as solar penetration increases. However, such simulations require additional data dependencies and expertise that may not be readily available to forecasters.

In order to the simulate the system, a PCM should be used to simulate the operations with and without energy storage. A number of key considerations for such simulations include:

- **Use of multi-cycle models:** A multi-cycle model captures operations in at least two decision stages, such as day-ahead and real-time processes, and links the data together. For example a day-ahead decision may be made based on day-ahead forecasts and certain generators committed to provide the forecasted energy needs, plus any reserves. Then, the model updates to real time actuals and the system is redispatched, recognizing limitations on the ability to commit additional generation in response to errors. If such a model is used, the ability of an improved forecast to reduce startup of quick start units or reduce solar curtailment can be captured. An example of such a model is included in [Ela13](#ref-ela13) and [Martinez-Anido16](#ref-martinez-anido16).
- **Use of dynamic reserves that reflect forecast errors:** As solar penetration increases, it is likely to impact reserves associated with balancing, such as regulation or ramping reserves. A number of ISOs and utilities are moving towards dynamically setting those reserves based on analysis of historical forecast error. Therefore, reducing forecast errors can result in reduced reserve requirements, which should also be included in simulations.

Models that include the above can be used to assess value of forecasts, and have been exercised in previous studies, such as by NREL and others ([Zhang15](#ref-zhang15), [Wang16a](#ref-wang16a), [Wang16b](#ref-wang16b), [Wang17](#ref-wang17)). Such an approach provides a more extensive estimate of the value of improved forecasts. At the same time, they are still limited by simplifications made in any model, and are best used for order of magnitude or relative studies. For example, a PCM may say that reducing forecast MAPE by 10% reduces costs in a given system by 1.5%. However, the 1.5% result should be interpreted as meaning reducing the MAPE by 10% is likely to reduce the costs in the range of 0-10%, rather that stating that the cost reduction will be exactly 1.5%.


## References
{: .anchor}
- [<a name="brier50">Brier50</a>] G. W. Brier, "Verification of Forecasts Expressed in Terms of Probability", Mon. Wea. Rev., vol. 78, pp. 1-3, 1950. DOI: [10.1175/1520-0493(1950)078<0001:VOFEIT>2.0.CO;2](https://doi.org/10.1175/1520-0493(1950)078%3C0001:VOFEIT%3E2.0.CO;2)
- [<a name="ref-ela13">Ela13</a>] E. Ela, V. Diakov, E. Ibanez, and M. Heaney, "Impacts of variability and uncertainty in solar photovoltaic generation at multiple timescales", Technical Report, NREL/TP-5500-58274, Golden, CO, May 2013
- [<a name="ref-espinar09">Espinar09</a>] B. Espinar, L. Ramírez, A. Drews, H. G. Beyer, L. F. Zarzalejo, J. Polo, and L. Martín, "Analysis of different comparison parameters applied to solar radiation data from satellite and German radiometric stations", Solar Energy, vol. 83, issue 1, pp. 118-125, 2009. DOI: [10.1016/j.solener.2008.07.009](https://doi.org/10.1016/j.solener.2008.07.009)
- [<a name="ref-gueymard12">Gueymard12</a>] C. A. Gueymard, "Clear-sky irradiance predictions for solar resource mapping and large-scale applications: improved validation methodology and detailed performance analysis of 18 broadband radiative models", Solar Energy, vol. 86, pp. 2145-2169, 2012. DOI: [10.1016/j.solener.2011.11.011](https://doi.org/10.1016/j.solener.2011.11.011)
- [<a name="ref-martinez-anido16">Martinez-Anido16</a>] C. B. Martinez-Anido, B. Botor, A. R. Florita, C. Draxl, S. Lu, H. F. Hamann, and B. M. Hodge, "The value of day-ahead solar power forecasting improvement", Solar Energy, vol. 129, pp. 192-203, 2016. DOI: [10.1016/j.solener.2016.01.049](https://doi.org/10.1016/j.solener.2016.01.049)
- [<a name="ref-marquez12">Marquez12</a>] R. Marquez and C. F. M. Coimbra, "Proposed Metric for Evaluation of Solar Forecasting Models", 2012
- [<a name="matheson76">Matheson76</a>] J. E. Matheson and R. L. Winkler, "Scoring Rules for Continuous Probability Distributions", Management Science, vol. 22, no. 10, pp. 1087-1096, 1976. DOI: [10.1287/mnsc.22.10.1087](https://doi.org/10.1287/mnsc.22.10.1087)
- [<a name="ref-murphy73">Murphy73</a>] A. H. Murphy, "A New Vector Partition of the Probability Score", J. Appl. Meteor., vol. 12, pp. 595-600, 1973. DOI: [10.1175/1520-0450(1973)012%3C0595:ANVPOT%3E2.0.CO;2](https://doi.org/10.1175/1520-0450(1973)012%3C0595:ANVPOT%3E2.0.CO;2)
- [<a name="ref-wang16a">Wang16a</a>] Q. Wang, H. Wu, A. R. Florita, C. B. Martinez-Anido, and B. M. Hodge, "The value of improved wind power forecasting: Grid flexibility quantification, ramp capability analysis, and impacts of electricity market operation timescales", Applied Energy, 184, pp. 696-713, 2016. DOI: [10.1016/j.apenergy.2016.11.016](https://doi.org/10.1016/j.apenergy.2016.11.016)
- [<a name="ref-wang16b">Wang16b</a>] Q. Wang, C. Brancucci, H. Wu, A. R. Florita, and B. M. Hodge, "Quantifying the Economic and Grid Reliability Impacts of Improved Wind Power Forecasting", IEEE Transactions on Sustainable Energy, vol. 7, no. 4, pp. 1525-1537, 2016. DOI: [10.1109/TSTE.2016.2560628](https://doi.org/10.1109/TSTE.2016.2560628)
- [<a name="ref-wang17">Wang17</a>] Q. Wang, and B. M. Hodge, "Enhancing Power System Operational Flexibility with Flexible Ramping Products: A Review", IEEE Transactions on Industrial Informatics, vol. 13, no. 4, pp. 1652-1664, 2017. DOI: [10.1109/TII.2016.2637879](https://doi.org/10.1109/TII.2016.2637879)
- [<a name="ref-wilks11">Wilks11</a>] D. S. Wilks, "Statistical Methods in the Atmospheric Sciences", 3rd ed. Oxford; Waltham, MA; Academic Press, 2011.
- [<a name="ref-zhang15">Zhang15</a>] J. Zhang, A. Florita, B. M. Hodge, S. Lu, H. F. Hamann, V. Banunarayanan, A. Brockway,  "A suite of metrics for assessing the performance of solar power forecasting", Solar Energy, vol. 111, pp. 157-175, 2015. DOI: [10.1016/j.solener.2014.10.016](https://doi.org/10.1016/j.solener.2014.10.016)
