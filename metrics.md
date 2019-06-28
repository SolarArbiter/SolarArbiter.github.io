---
layout: base
mathjax: true
permalink: /metrics/
---

# Metrics
The Solar Forecast Arbiter evaluation framework provides a suite of metrics for evaluating deterministic and probablistic solar forecasts. These metrics are used for different purposes, e.g., comparing the forecast and the measurement, comparing the performance of multiple forecasts, and evaluating an event forecast.


## Metrics for Deterministic Forecasts
The following metrics provide measures of the performance of deterministic forecasts. Each metric is computed from a set of $$ n $$ forecasts $$ (F_1, F_2, \dots, F_n) $$ and corresponding observations $$ (O_1, O_2, \dots, O_n) $$.

In the metrics below, we adopt the following nomenclature:
- $$ n : $$ number of samples
- $$ F : $$ forecasted value
- $$ O : $$ observed (actual) value
- $$ \text{norm} : $$ normalizing factor (with the same units as the forecasted and observed values)
- $$ \bar{F}, \, \bar{O} : $$ the mean of the forecasted and observed values, respectively


### Mean Absolute Error (MAE)
The absolute error is the absolute value of the difference between the forecasted and observed values. The MAE is defined as:

$$ \text{MAE} = \frac{1}{n} \sum_{i=1}^n  \lvert F_i - O_i \rvert $$


### Mean Bias Error (MBE)
The bias is the difference between the forecasted and observed values. The MBE is defined as:

$$ \text{MBE} = \frac{1}{n} \sum_{i=1}^n (F_i - O_i) $$


### Root Mean Square Error (RMSE)
The RMSE is the square root of the averaged of the squared differences between the forecasted and observed values, and is defined as:

$$ \text{RMSE} = \sqrt{ \frac{1}{n} \sum_{i=1}^n (F_i - O_i)^2 } $$

RMSE is a frequently used measured for evaluating forecast accuracy. It can be interprest


### Forecast Skill ($$ s $$)
The forecast skill measures the performance of a forecast relative to a reference forecast. The Solar Forecast Arbiter uses the definition of forecast skill based on RMSE:

$$ s = 1 - \frac{\text{RMSE}_f}{\text{RMSE}_{\text{ref}}} $$

where $$ \text{RMSE}_f $$ is the RMSE of the forecast of interest, and $$ \text{RMSE}_{\text{ref}} $$ is the RMSE of the reference forecast, e.g., persistence.


### Mean Absolute Percentage Error (MAPE)
The absolute percentage error is the absolute value of the difference between the forecasted and observed values,

$$ \text{MAPE} = 100\% \cdot \frac{1}{n} \sum_{i=1}^n | \frac{F_i - O_i}{O_i} | $$


### Normalized Root Mean Square Error (NRMSE):
The NRMSE [%] is the normalized form of the RMSE and is defined as:

$$ \text{RMSE} = \frac{100\%}{\text{norm}} \cdot \sqrt{ \frac{1}{n} \sum_{i=1}^n (F_i - O_i)^2 } $$


### Centered (unbiased) Root Mean Square Error (CRMSE)
The CRMSE describes the variation in errors around the mean and is defined as:

$$ \text{CRMSE} = \sqrt{ \frac{1}{n} \sum_{i=1}^n \left( (F_i - \bar{F}) - (O_i - \bar{O}) \right)^2 } $$

The CRMSE is related to the RMSE and MBE through $$ \text{RMSE}^2 = \text{CRMSE}^2 + \text{MBE}^2 $$, and can be decomposed into components related to the standard deviation and correlation coefficient:

$$ \text{CRMSE}^2 = \sigma_F^2 + \sigma_O^2 - 2 \sigma_F \sigma_O r $$

where $$ \sigma_F $$ and $$ \sigma_O $$ are the standard deviations of the forecast and observation, respectively, and $$ r $$ is the correlation coefficient.


### Pearson Correlation Coefficient ($$ r $$)
Correlation indicates the strength and direction of a linear relationship between two variables. The Pearson correlation coefficient, aka, the sample correlation coefficient, measures the linear dependency between the forecasted and observed values, and is defined as the ratio of the covariance of the variables to the product of their standard deviation:

$$ r = \frac{ \sum_{i=1}^n (F_i - \bar{F}) (O_i - \bar{O}) }{
\sqrt{ \sum_{i=1}^n (F_i - \bar{F})^2} \times \sqrt{ \sum_{i=1}^n (O_i - \bar{O})^2 } } $$


### Coefficient of Determination ($$ R^2 $$)
The coefficient of determination measures the extent that the variability in the forecast errors is explained by variability in the observed values, and is defined as:

$$ R^2 = 1 - \frac{ \sum_{i=1}^n (O_i - F_i)^2 }{ \sum_{i=1}^n (O_i - \bar{O})^2 } $$

By this definition, a perfect forecast has a $$ R^2 $$ value of 1.


### Kolmogorov-Smirnov Test Integral (KSI)
The KSI quantifies the level of agreement between the cumulative distribution function (CDFs) of the forecasted and observed values, and is defined as:

$$ \text{KSI} = \int_{p_{\text{min}}}^{p_{\text{max}}} D_n(p) dp $$

where $$ p_{\text{min}} $$ and $$ p_{\text{max}} $$ are the minimum and maximum values of the observations, and $$ D_n(p) $$ is the absolute difference between the two empirical CDFs:

$$ D_n(p) = \text{max}( | \text{CDF}_O(p) - \text{CDF}_F(p) | ) \enspace \text{for} \enspace p \in [ p_k, p_{k+1} ] $$

where $$ p_k $$ is defined as $$ p_k = p_{\text{min}} + kd $$ for $$k = 0, 1, \dots, K $$ and $$ d = (p_{\text{max}} - p_{\text{min}}) / K $$.

In practice, $$ K = 100 $$ is typical. A KSI value of zero implies that the CDFs of the forecast and observed values are equal.

KSI can be normalized as:

$$ KSI (\%) = \frac{100}{a_{\text{critical}}} KSI $$

where $$ a_{\text{critical}} = V_c (p_{\text{max}} - p_{\text{min}}) $$ and $$ V_c = 1.63 / \sqrt{n} $$. When $$ n \geq 35 , $$ the normalized KSI can be interpreted as a stastical that tests the hypothesis that the two empirical CDFs represent samples drawn from the same population.


### OVER
Conceptually, the OVER metric modifies the KSI to quantify the difference between the two CDFs, but only where the CDFs differ by more than a critical limit $$ V_c $$. The OVER is calculated as:

$$ OVER = \int_{p_{\text{min}}}^{p_{\text{max}}} D_n^* dp $$

where

$$ D_n^* \begin{cases}
    \displaystyle D_n - V & \text{if} & D_n > V_c \\
    \displaystyle 0 & \text{if} & D_n \leq V_c
\end{cases} $$

The OVER metric can be normalized using the same approach as for KSI.


### Combined Performance Index (CPI)
The CPI can be thought of as a combination of KSI, OVER, and RMSE:

$$ \text{CPI} = \frac{1}{4} ( \text{KSI} + \text{OVER} + 2 \times \text{RMSE} ) $$


## Metrics for Deterministic Event Forecasts
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
The POD is the fraction of observed events correctly forecasted as events:

$$ POD = \frac{TP}{TP + FN} $$


### False Alarm Ratio (FAR)
The FAR is the fraction of forecasted events that did not occur:

$$ FAR = \frac{FP}{TP + FP} $$


### Probability of False Detection (POFD)
The POFD is the fraction of observed non-events that were forecasted as events:

$$ POFD = \frac{FP}{FP + TN} $$


### Critical Success Index (CSI)
The CSI evaluates how well an event forecast predicts observed events, e.g., ramps in irradiance or power. THe CSI is the relative frequency of hits, i.e., how well predicted "yes" events correspond to observed "yes" events:

$$ CSI = \frac{TP}{TP + FP + FN} $$


### Event Bias (EBIAS)
The EBIAS is the ratio of counts of forecast and observed events:

$$ EBIAS = \frac{TP + FP}{TP + FN} $$


### Event Accuracy (EA)
The EA is the fraction of events that were forecasted correctly, i.e., forecast = "yes" and observed = "yes" or forecast = "no" and observed = "no":

$$ EA = \frac{TP + TN}{TP + FP + TN + FN} = \frac{TP + TN}{n} $$

where $$ n $$ is the number of samples.


## Metrics for Probablistic Forecasts
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


### Brier Score (BS)
The BS measures the accuracy of forecast probability for one or more events:

$$ \text{BS} = \frac{1}{n} \sum_{i=1}^n (f_i - o_i)^2  $$

Smaller values of BS indicate better agreement between forecasts and observations.


### Brier Skill Score (BSS)
The BSS is based on the BS and measures the performance of a probability forecast relative to a reference forecast:

$$ BSS = 1 - \frac{\text{BS}_f}{\text{BS}_{\text{ref}}} $$

where $$ \text{BS}_f $$ is the BS of the forecast of interest, and $$ \text{BS}_{\text{ref}} $$ is the BS of the reference forecast. BSS greater than zero indicates the forecast performed better than the reference and vice versa for BSS less than zero, while BSS equal to zero indicates the forecast is no better (or worse) than the reference.

When the probability forecast takes on a finite number of values (e.g. 0.0, 0.1, ..., 0.9, 1.0), the BS can be decomposed into a sum of three metrics that give additional insight into a probability forecast:

$$ \text{BS} = \text{REL} + \text{RES} + \text{UNC} $$


### Reliability (REL)
The REL is given by:

$$ \text{REL} = \frac{1}{n} \sum_{i=1}^I N_i (f_i - \bar{o}_i)^2 $$

Reliability is the weighted averaged of the squared differences between the forecast probabilities $$ f_i $$ and the relative frequencies of the observed event in the forecast subsample of times where $$ F(t_k) = f_i $$. A forecast is perfectly reliably if $$ \text{REL} = 0 $$. This occurs when the relative event frequency in each subsample is equal to the forecast probability for the subsample.


### Resolution (RES)
The RES is given by:

$$ \text{RES} = \frac{1}{n} \sum_{i=1}^I N_i (\bar{o}_i - \bar{o})^2 $$

Resolution is the weighted averaged of the squared differences between the releative event frequency for each forecast subsample and the overall event frequency. Resolution measures the forecast's ability to produce subsample forecast periods where the event frequency is different. Higher values of RES are desirable.


### Uncertainty (UNC)
The UNC is given by:

$$ \text{UNC} = \bar{o} (1 - \bar{o})$$

Uncertainty is the variance of the event indicator $$ o(t) $$. Low values of UNC indicate that the event being forecasted occurs only rarely.


### Sharpness (SH)
The SH represents the degree of "concentration" of a forecast comprising a prediction interval of the form $$ [ f_l, f_u ] $$ within which the forecast quantity is expected to fall with probability $$ 1 - \beta $$. A good forecast should have a low sharpness value. The prediction interval endpoints are associated with quantiles $$ \alpha_l $$ and $$ \alpha_u $$, where $$ \alpha_u - \alpha_l = 1 - \beta $$. For a single prediction interval, the SH is:

$$ \text{SH} = f_u - f_l $$

and for a timeseries of prediction intervals, the SH is given by the average:

$$ \text{SH} = \frac{1}{n} \sum_{i=1}^n f_{u,i} - f_{l, i} $$


### Continuous Ranked Probability Score (CRPS)
The CRPS is a score that is a designed to measure both the realiability and sharpness of a probablistic forecast. For a timeseries of forecasts comprising a CDF at each time point, the CRPS is:

$$ \text{CRPS} = \frac{1}{n} \sum_{i=1}^n \int | F_i(x) - O_i(x) | dx $$

where $$ F_i(x) $$ is the CDF of the forecast quantity $$ x $$ at time point $$ i $$, and $$ O_i(x) $$ is the CDF associated with the observed value $$ x_i $$:

$$ O_i = \begin{cases}
    \displaystyle 0 & x < x_i \\
    \displaystyle 1 & x \geq x_i
\end{cases} $$

The CRPS reduces to the mean absolute error (MAE) if the forecast is deterministic.
