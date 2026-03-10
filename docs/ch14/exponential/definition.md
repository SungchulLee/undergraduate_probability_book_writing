# Exponential Distribution Definition

The Exponential distribution models the waiting time between events in a Poisson process -- the continuous counterpart of the Geometric distribution.

## Definition

A continuous random variable $X$ has the **Exponential distribution** with rate parameter $\lambda > 0$, written $X \sim \text{Exp}(\lambda)$, if its PDF is

$$
f(x) = \lambda e^{-\lambda x}, \quad x \geq 0
$$

**CDF:**

$$
F(x) = P(X \leq x) = 1 - e^{-\lambda x}, \quad x \geq 0
$$

**Survival function (tail probability):**

$$
\bar{F}(x) = P(X > x) = e^{-\lambda x}, \quad x \geq 0
$$

**Moments:**

$$
E[X] = \frac{1}{\lambda}, \qquad \text{Var}(X) = \frac{1}{\lambda^2}
$$

**MGF:**

$$
M_X(t) = \frac{\lambda}{\lambda - t}, \quad t < \lambda
$$

**Parameterization note.** Some texts parameterize by the *scale* $\beta = 1/\lambda$ (the mean) rather than the rate $\lambda$. In the scale parameterization, the PDF is $f(x) = \frac{1}{\beta} e^{-x/\beta}$. We use the rate parameterization throughout this book because it keeps the Poisson process connection transparent: rate $\lambda$ in the process equals rate $\lambda$ in the distribution.

## Explanation

### Connection to the Poisson Process

In a Poisson process with rate $\lambda$, events arrive randomly along the time axis. Let $T_1$ be the time of the first arrival after time $0$. Then

$$
P(T_1 > t) = P(\text{no arrivals in } [0, t]) = e^{-\lambda t}
$$

since the number of arrivals in $[0, t]$ follows $\text{Po}(\lambda t)$, and $P(N(t) = 0) = e^{-\lambda t}$. This shows $T_1 \sim \text{Exp}(\lambda)$.

More generally, the interarrival times $T_1, T_2, T_3, \ldots$ between consecutive events are **independent and identically distributed** $\text{Exp}(\lambda)$. This is the fundamental link between the Poisson process (counting events) and the Exponential distribution (measuring waiting times).

### Relationship to the Geometric Distribution

The Exponential distribution is the **continuous analog** of the Geometric distribution:

| Property | Geometric | Exponential |
|----------|-----------|-------------|
| Domain | Discrete ($1, 2, 3, \ldots$) | Continuous ($[0, \infty)$) |
| Memoryless | Yes | Yes |
| Interpretation | Trials until first success | Time until first event |
| Parameter | $p$ (success probability) | $\lambda$ (rate) |
| Mean | $1/p$ | $1/\lambda$ |
| Variance | $q/p^2$ | $1/\lambda^2$ |

### Relationship to the Gamma Distribution

The Exponential distribution is a special case of the Gamma distribution:

$$
\text{Exp}(\lambda) \stackrel{d}{=} \Gamma(1, \lambda)
$$

Setting $\alpha = 1$ in the Gamma PDF gives

$$
\frac{\lambda(\lambda x)^{1-1} e^{-\lambda x}}{\Gamma(1)} = \lambda e^{-\lambda x}
$$

since $\Gamma(1) = 1$ and $(\lambda x)^0 = 1$, recovering the Exponential PDF.

### Simulation via Inverse CDF

To simulate $X \sim \text{Exp}(\lambda)$ from a uniform random variable $U \sim U(0,1)$, use the inverse CDF method. Solving $u = 1 - e^{-\lambda x}$ for $x$ gives

$$
X = F^{-1}(U) = -\frac{1}{\lambda} \ln(1 - U)
$$

Since $1 - U \sim U(0,1)$ when $U \sim U(0,1)$, this simplifies to

$$
X = -\frac{1}{\lambda} \ln(U) \sim \text{Exp}(\lambda)
$$

## Examples

**Example 1.** Let $X \sim \text{Exp}(2)$. Compute $P(X > 1)$, $P(0.5 < X < 2)$, and the median.

Using the survival function: $P(X > 1) = e^{-2 \cdot 1} = e^{-2} \approx 0.1353$.

Using the CDF: $P(0.5 < X < 2) = F(2) - F(0.5) = (1 - e^{-4}) - (1 - e^{-1}) = e^{-1} - e^{-4} \approx 0.3496$.

The median $m$ satisfies $F(m) = 1/2$, so $1 - e^{-2m} = 1/2$ and $m = \frac{\ln 2}{2} \approx 0.3466$.

**Example 2.** Simulate $\text{Exp}(2)$ using the inverse CDF method and verify the PDF, CDF, and moments.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
lam = 2.0
n_sim = 200_000

# Simulate via inverse CDF
U = np.random.uniform(0, 1, n_sim)
X_sim = -np.log(U) / lam

# Verify moments
print(f"Theoretical mean: {1/lam:.4f}")
print(f"Simulated mean:   {np.mean(X_sim):.4f}")
print(f"Theoretical var:  {1/lam**2:.4f}")
print(f"Simulated var:    {np.var(X_sim):.4f}")

# Verify probabilities from Example 1
print(f"\nP(X > 1):  theory={np.exp(-2):.4f}, sim={np.mean(X_sim > 1):.4f}")
p_interval = np.exp(-1) - np.exp(-4)
print(f"P(0.5<X<2): theory={p_interval:.4f}, "
      f"sim={np.mean((X_sim > 0.5) & (X_sim < 2)):.4f}")
median_theory = np.log(2) / lam
print(f"Median: theory={median_theory:.4f}, sim={np.median(X_sim):.4f}")

# Compare with scipy
X_scipy = stats.expon(scale=1/lam)
print(f"\nScipy CDF at x=1: {X_scipy.cdf(1):.4f}")
print(f"Scipy median:     {X_scipy.median():.4f}")
```
