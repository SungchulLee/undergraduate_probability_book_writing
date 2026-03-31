# Rate Parameter and Intensity
<<<<<<< Updated upstream

## The Rate Parameter

The constant $\lambda > 0$ in the Poisson process definition is called the **rate parameter** (or **intensity**). It controls how frequently events occur.

!!! info "Interpreting the Rate"
    For a Poisson process with rate $\lambda$:

    - $\lambda$ is the **expected number of events per unit time**
    - In an interval of length $t$, the expected number of events is $\lambda t$
    - The probability of an event in a tiny interval $(t, t+h]$ is approximately $\lambda h$

---

## Mean and Variance

Since $N(t) \sim \text{Po}(\lambda t)$, the mean and variance follow immediately from the properties of the Poisson distribution:

$$
E[N(t)] = \lambda t
$$

$$
\text{Var}(N(t)) = \lambda t
$$

The expected count grows linearly with time, and so does the variance. This means the **standard deviation** grows as $\sqrt{\lambda t}$, so the relative fluctuation $\text{SD}(N(t))/E[N(t)] = 1/\sqrt{\lambda t}$ decreases over longer observation windows.

---

## Recovering the Rate from Data

Given observed data, the rate can be estimated as:

$$
\hat{\lambda} = \frac{\text{total number of events}}{\text{total observation time}} = \frac{N(t)}{t}
$$

By the law of large numbers, this estimator converges to the true $\lambda$ as the observation time grows.

---

## Units and Dimensional Analysis

The rate $\lambda$ always has units of **events per unit time**. The unit of time must be specified and used consistently.

| Context | Rate $\lambda$ | Unit |
|:---|:---|:---|
| Phone calls to a call center | 12 | calls per hour |
| Radioactive decay | 0.693 | decays per second |
| Customer arrivals at a shop | 2.5 | customers per minute |
| Earthquakes in a region | 0.3 | quakes per year |
| Typos on a printed page | 1.2 | errors per page |

??? example "Unit Conversion"
    A call center receives calls at rate $\lambda = 12$ calls per hour. Expressing this in different units:

    - Per minute: $\lambda = 12/60 = 0.2$ calls per minute
    - Per 8-hour shift: $\lambda \cdot 8 = 96$ expected calls per shift

    The number of calls in a 15-minute window is $N(0.25) \sim \text{Po}(12 \times 0.25) = \text{Po}(3)$.

---

## Intensity Function (Non-Homogeneous Case)

The standard Poisson process has a constant rate $\lambda$, meaning events are equally likely at any moment. In practice, many phenomena have rates that vary over time.

A **non-homogeneous Poisson process** replaces the constant $\lambda$ with a time-varying **intensity function** $\lambda(t)$. In this case, the number of events in $(s, s+t]$ follows

$$
N(s, s+t) \sim \text{Po}\!\left(\int_s^{s+t} \lambda(u)\, du\right)
$$

The increments remain independent but are no longer stationary, since the distribution depends on when the interval starts. This chapter focuses on the homogeneous case ($\lambda$ constant); the non-homogeneous extension is mentioned for completeness and appears in more advanced courses.

---

## Summary

The rate parameter $\lambda$ is the single parameter that governs the entire Poisson process. It determines the expected event count ($\lambda t$), the variance ($\lambda t$), the mean waiting time between events ($1/\lambda$, as we will see in Chapter 14), and the probability of events in any interval. Always check that $\lambda$ and the time variable share consistent units.
=======
>>>>>>> Stashed changes
