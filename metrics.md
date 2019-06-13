---
layout: base
mathjax: true
permalink: /metrics/
---

# Metrics


## Metrics for Deterministic Forecasts

The following metrics provide measures of the performance of deterministic forecasts. Each metric is computed from a set of $$ n $$ forecasts ($$ F_1, F_2, \dots, F_n $$) and $$ n $$ observations ($$ O_1, O_2, \dots, O_n $$).


- mean absolute error (MAE):

$$ \text{MAE} = \frac{1}{n} \sum_{i=1}^n  \lvert F_i - O_i \rvert $$


- mean bias error (MBE):

$$ \text{MBE} = \frac{1}{n} \sum_{i=1}^n (F_i - O_i) $$


- root mean square error (RMSE):

$$ \text{RMSE} = \sqrt{ \frac{1}{n} \sum_{i=1}^n (F_i - O_i)^2 } $$


- normalized root mean square error (NRMSE):

$$ \text{RMSE} = \frac{100\%}{\text{norm}} \sqrt{ \frac{1}{n} \sum_{i=1}^n (F_i - O_i)^2 } $$


- forecast skill (s):

$$ s = 1 - \frac{\text{RMSE}}{\text{RMSE}_p}$$


## Metrics for Probablistic Forecasts

- Brier Score (BS)

$$ BS = \frac{1}{n} \sum_{i=1}^n (F_i - O_i)^2
