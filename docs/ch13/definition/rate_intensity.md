# Rate Parameter and Intensity

The rate $\lambda$ controls the expected number of events per unit time — the single parameter that fully characterizes a homogeneous Poisson process.

## Definition

The **rate** (or **intensity**) $\lambda$ of a Poisson process satisfies:

$$
E[N(t)] = \lambda t, \qquad \text{Var}(N(t)) = \lambda t
$$

Equivalently, $\lambda = E[N(1)]$ is the expected number of events per unit time.

For a **non-homogeneous** Poisson process with time-varying rate $\lambda(t)$:

$$
N(s, t) \sim \text{Pois}\!\left(\int_s^t \lambda(u)\,du\right)
$$

## Explanation

### Interpreting $\lambda$

- $\lambda = 5$ per hour means about 5 events per hour on average
- In any interval of length $h$: expected count = $\lambda h$
- Mean interarrival time = $1/\lambda$

### Estimation

Given observed arrival times $0 < s_1 < s_2 < \cdots < s_n$ in $[0, T]$:

$$
\hat{\lambda} = \frac{n}{T}
$$

This is the maximum likelihood estimator.

### Non-Homogeneous Extension

When the rate varies over time (e.g., rush-hour traffic), replace $\lambda t$ with $\Lambda(s,t) = \int_s^t \lambda(u)\,du$. Events in disjoint intervals remain independent, but the count distribution depends on the interval's position.

## Examples

**Example.** Emails arrive at rate $\lambda = 12$ per hour. Expected count in 30 minutes: $12 \times 0.5 = 6$. Mean time between emails: $1/12$ hour = 5 minutes.

```python
import numpy as np

np.random.seed(42)
lam = 12  # per hour
T = 10    # observe for 10 hours

# Simulate arrival times
arrivals = []
t = 0
while True:
    t += np.random.exponential(1/lam)
    if t > T:
        break
    arrivals.append(t)

n = len(arrivals)
lam_hat = n / T
print(f"Observed {n} arrivals in {T} hours")
print(f"Rate estimate: {lam_hat:.2f}  (true: {lam})")
print(f"Mean interarrival: {np.mean(np.diff(arrivals))*60:.2f} min  (theory: {60/lam:.2f} min)")
```
