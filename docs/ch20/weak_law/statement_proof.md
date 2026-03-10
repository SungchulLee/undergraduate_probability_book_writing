# Weak Law of Large Numbers

The sample mean converges in probability to the population mean — proved in one line from Chebyshev's inequality.

## Definition

Let $X_1, X_2, \ldots$ be iid with $E[X_i] = \mu$ and $\operatorname{Var}(X_i) = \sigma^2 < \infty$. Then:

$$
\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i \xrightarrow{p} \mu
$$

More generally, if $E[\lvert g(X) \rvert] < \infty$, then $\frac{1}{n}\sum_{i=1}^n g(X_i) \xrightarrow{p} E[g(X)]$.

## Explanation

### Proof (Finite Variance)

**Step 1.** $E[\bar{X}_n] = \mu$ and $\operatorname{Var}(\bar{X}_n) = \sigma^2/n$.

**Step 2.** By Chebyshev:

$$
P(|\bar{X}_n - \mu| > \varepsilon) \le \frac{\sigma^2}{n\varepsilon^2} \to 0
$$

Therefore $\bar{X}_n \xrightarrow{p} \mu$. $\square$

### Without Finite Variance

The WLLN holds under the weaker condition $E[\lvert X \rvert] < \infty$ alone. The proof uses **truncation**: define $Y_i = X_i \cdot \mathbf{1}(\lvert X_i \rvert \le n)$, apply Chebyshev to $\bar{Y}_n$, and show $P(\bar{X}_n \ne \bar{Y}_n) \to 0$.

### Interpretation

For large $n$, $\bar{X}_n$ is **unlikely** to be far from $\mu$. This does not guarantee that $\bar{X}_n$ stays close forever — that is the Strong Law.

## Examples

**Example.** Chebyshev bound vs actual deviation probability for $\operatorname{Exp}(1)$ ($\mu = 1$, $\sigma^2 = 1$).

```python
import numpy as np

np.random.seed(42)
n_sim = 100_000
eps = 0.1

for n in [100, 1000, 10000]:
    means = np.random.exponential(1.0, (n_sim, n)).mean(axis=1)
    actual = np.mean(np.abs(means - 1.0) > eps)
    chebyshev = 1.0 / (n * eps**2)
    print(f"n={n:5d}: actual={actual:.4f}, Chebyshev bound={chebyshev:.4f}")
```
