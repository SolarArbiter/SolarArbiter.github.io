---
layout: base
mathjax: true
permalink: /metrics/
---

# Metrics
The Solar Forecast Arbiter evaluation framework provides a suite of metrics for evaluating deterministic and probablistic solar forecasts. These metrics are used for different purposes, e.g., comparing the forecast and the measurement, comparing the performance of multiple forecasts, and evaluating an event forecast.

In the metrics below, we adopt the following nomenclature:
- $$ n : $$ number of samples
- $$ F : $$ forecasted value
- $$ O : $$ observed (actual) value
- $$ \text{norm} : $$ normalizing factor (with the same units as the forecasted and observed values)
- $$ \bar{F}, \, \bar{O} : $$ the mean of the forecasted and observed values, respectively


## Metrics for Deterministic Forecasts
The following metrics provide measures of the performance of deterministic forecasts. Each metric is computed from a set of $$ n $$ forecasts $$ (F_1, F_2, \dots, F_n) $$ and corresponding observations $$ (O_1, O_2, \dots, O_n) $$.


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

$$ s = 1 - \frac{\text{RMSE}_F}{\text{RMSE}_{\text{ref}}} $$

where $$ \text{RMSE}_F $$ is the RMSE of the forecast of interest, and $$ \text{RMSE}_{\text{ref}} $$ is the RMSE of the reference forecast, e.g., persistence.


### Mean Absolute Percentage Error (MAPE)
The absolute percentage error is the absolute value of the difference between the forecasted and observed values,

$$ \text{MAPE} = $$


### Normalized Root Mean Square Error (NRMSE):
The NRMSE [%] is the normalized form of the RMSE and is defined as:

$$ \text{RMSE} = \frac{100\%}{\text{norm}} \sqrt{ \frac{1}{n} \sum_{i=1}^n (F_i - O_i)^2 } $$


### Centered (unbiased) Root Mean Square Error (CRMSE)
The CRMSE describes the variation in errors around the mean and is defined as:

$$ \text{CRMSE} = \sqrt{ \frac{1}{n} \sum_{i=1}^n \left( (F_i - \hat{F}) - (O_i - \hat{O}) \right)^2 } $$


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

$$ D_n(p) = \text{max}( | \text{CDF}_O(p) - \text{CDF}_F(p) | ) \text{for}$$

where $$ p_k $$ is defined



## Metrics for Probablistic Forecasts

The following metrics provide measures of the performance of probablistic forecasts. Each metric is computer

### Brier Score (BS)
The BS

$$ BS = \frac{1}{n} \sum_{i=1}^n (F_i - O_i)^2  $$


