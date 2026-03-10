# Erlang Distribution

The Erlang distribution is the Gamma distribution with an integer shape parameter -- it models the sum of independent identical exponential waiting times.

## Definition

The **Erlang distribution** with shape parameter $k$ (a positive integer) and rate $\lambda > 0$ is

$$
\text{Erlang}(k, \lambda) = \Gamma(k, \lambda)
$$

Its PDF is

$$
f(x) = \frac{\lambda(\lambda x)^{k-1} e^{-\lambda x}}{(k-1)!}, \quad x > 0
$$

where we use $\Gamma(k) = (k-1)!$ for positive integers $k$.

**CDF (closed form):**

$$
F(x) = 1 - \sum_{j=0}^{k-1} \frac{(\lambda x)^j}{j!} e^{-\lambda x}, \quad x \geq 0
$$

**Moments:**

$$
E[X] = \frac{k}{\lambda}, \qquad \text{Var}(X) = \frac{k}{\lambda^2}
$$

## Explanation

### Construction as a Sum of Exponentials

If $T_1, T_2, \ldots, T_k$ are iid $\text{Exp}(\lambda)$, then their sum follows the Erlang distribution:

$$
S_k = T_1 + T_2 + \cdots + T_k \sim \text{Erlang}(k, \lambda) = \Gamma(k, \lambda)
$$

This is the defining interpretation: the Erlang distribution arises when you wait for $k$ events in a Poisson process.

| Sum | Distribution |
|:---:|:---:|
| $T_1$ | $\text{Exp}(\lambda) = \text{Erlang}(1, \lambda)$ |
| $T_1 + T_2$ | $\text{Erlang}(2, \lambda)$ |
| $T_1 + T_2 + T_3$ | $\text{Erlang}(3, \lambda)$ |
| $T_1 + \cdots + T_k$ | $\text{Erlang}(k, \lambda)$ |

### Why a Separate Name

The Erlang distribution is named after A.K. Erlang, who introduced it in the early 20th century to model telephone call waiting times. While it is mathematically just a special case of the Gamma distribution, it has its own identity because:

- It predates the general Gamma distribution in applications
- Its integer shape parameter gives it a concrete interpretation as a sum of iid Exponentials
- Its CDF has a **closed-form** expression involving a finite sum, unlike the general Gamma which requires the incomplete gamma function

### Closed-Form CDF via the Poisson Connection

The CDF formula comes from a beautiful duality. The event "the $k$-th arrival occurs by time $x$" is the same as "at least $k$ arrivals occur by time $x$":

$$
P(S_k \leq x) = P(N(x) \geq k) = 1 - P(N(x) \leq k - 1) = 1 - \sum_{j=0}^{k-1} \frac{(\lambda x)^j}{j!} e^{-\lambda x}
$$

where $N(x) \sim \text{Po}(\lambda x)$. This links the **Erlang CDF** to the **Poisson tail probability**.

### Shape of the PDF

As $k$ increases, the Erlang PDF becomes more bell-shaped and concentrated around the mean $k/\lambda$:

- $k = 1$: purely decreasing (Exponential)
- $k = 2$: rises from zero, peaks at $1/\lambda$, then decays
- $k \geq 3$: increasingly symmetric and normal-looking

The mode is at $x = (k - 1)/\lambda$ for $k \geq 1$, and the distribution approaches a Normal distribution as $k \to \infty$ (by the Central Limit Theorem, since it is a sum of iid random variables).

## Examples

**Example 1.** Customers arrive at a bank at rate $\lambda = 6$ per hour (Poisson process). You are third in line. Find the distribution, mean, and standard deviation of the time until you reach the counter.

You must wait for 3 services, so your wait is $S_3 \sim \text{Erlang}(3, 6)$. Then $E[S_3] = 3/6 = 0.5$ hours (30 minutes) and $\text{SD}(S_3) = \sqrt{3}/6 \approx 0.289$ hours (17.3 minutes).

**Example 2.** Verify that the sum of $k$ iid Exponentials matches the Erlang distribution.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
lam = 2.0
n_sim = 200_000

print("=== Sum of k iid Exp(lam) vs Erlang(k, lam) ===")
print(f"{'k':>3} | {'Mean sim':>9} {'Mean thy':>9} | "
      f"{'Var sim':>9} {'Var thy':>9}")
print("-" * 50)

for k in [1, 2, 3, 5, 10]:
    # Sum of k exponentials
    exp_samples = np.random.exponential(1/lam, size=(n_sim, k))
    sums = exp_samples.sum(axis=1)

    mean_thy = k / lam
    var_thy = k / lam**2

    print(f"{k:3d} | {np.mean(sums):9.4f} {mean_thy:9.4f} | "
          f"{np.var(sums):9.4f} {var_thy:9.4f}")

# Verify closed-form CDF: P(S_k <= x) = 1 - sum Poisson terms
k, x_val = 3, 1.5
erlang_cdf = stats.gamma.cdf(x_val, a=k, scale=1/lam)
poisson_tail = 1 - sum(
    (lam * x_val)**j / np.math.factorial(j) * np.exp(-lam * x_val)
    for j in range(k)
)
print(f"\nCDF check: Erlang({k},{lam}) at x={x_val}")
print(f"  scipy CDF:       {erlang_cdf:.6f}")
print(f"  Poisson formula:  {poisson_tail:.6f}")
```
