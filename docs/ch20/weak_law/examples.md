# WLLN Examples and Extensions

The weak law applies to any iid sequence with finite mean — from exponential waiting times to Monte Carlo estimation of integrals.

## Definition

The WLLN: for iid $X_i$ with $E[\lvert X_i \rvert] < \infty$:

$$
\bar{X}_n \xrightarrow{p} \mu
$$

The Chebyshev-based convergence rate (when $\sigma^2 < \infty$): $P(\lvert \bar{X}_n - \mu \rvert \ge \varepsilon) \le \frac{\sigma^2}{n\varepsilon^2}$.

## Explanation

### Chebyshev vs CLT Rates

Chebyshev gives polynomial decay: $O(1/n)$. The CLT gives sharper asymptotic behavior:

$$
P(|\bar{X}_n - \mu| \ge \varepsilon) \approx 2\!\left(1 - \Phi\!\left(\frac{\varepsilon\sqrt{n}}{\sigma}\right)\right)
$$

which decays exponentially in $n$.

### When WLLN Fails

If $E[\lvert X \rvert] = \infty$, the WLLN may fail. For iid Cauchy random variables, $\bar{X}_n$ has the **same** Cauchy distribution for every $n$ — no convergence occurs.

### Estimating pi via Monte Carlo

Generate $(U_i, V_i) \sim U([0,1]^2)$ iid, let $X_i = \mathbf{1}(U_i^2 + V_i^2 \le 1)$. Then $E[X_i] = \pi/4$ and:

$$
\hat{\pi}_n = 4\bar{X}_n \xrightarrow{p} \pi
$$

## Examples

**Example.** Convergence rates and Cauchy failure.

```python
import numpy as np

np.random.seed(42)
n = 10_000

# WLLN works: Exp(1)
exp_means = np.cumsum(np.random.exponential(1.0, n)) / np.arange(1, n + 1)
print(f"Exp(1) sample mean at n={n}: {exp_means[-1]:.4f} (theory: 1.0)")

# WLLN fails: Cauchy
cauchy_means = np.cumsum(np.random.standard_cauchy(n)) / np.arange(1, n + 1)
print(f"Cauchy sample mean at n={n}: {cauchy_means[-1]:.4f} (no convergence)")

# Monte Carlo pi
U = np.random.uniform(0, 1, (n, 2))
pi_hat = 4 * np.mean(U[:, 0]**2 + U[:, 1]**2 <= 1)
print(f"Monte Carlo π estimate: {pi_hat:.4f} (true: {np.pi:.4f})")
```
