# Convergence in Distribution

The weakest mode of convergence — CDFs converge pointwise — is all the CLT provides, yet it suffices for normal approximation.

## Definition

$X_n \xrightarrow{d} X$ if:

$$
\lim_{n \to \infty} F_{X_n}(x) = F_X(x)
$$

at every $x$ where $F_X$ is continuous.

## Explanation

### What It Says

The histograms of $X_n$ approach the density of $X$. This makes no claim about the random variables being on the same probability space — only the **distributions** must match.

### CLT as the Key Example

$$
\frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} N(0,1)
$$

This tells us the shape of the distribution approaches the standard normal, but does not say the sample mean itself converges to any single value. That requires the LLN.

### MGF Characterization

If $M_{X_n}(t) \to M_X(t)$ for all $t$ in a neighborhood of 0, then $X_n \xrightarrow{d} X$ (continuity theorem).

## Examples

**Example.** Uniform on $\{1/n, 2/n, \ldots, 1\}$ converges in distribution to $U(0,1)$.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n_sim = 100_000

for n in [10, 100, 1000]:
    X = np.random.choice(np.arange(1, n+1) / n, n_sim)
    ks_stat, p_val = stats.kstest(X, 'uniform')
    print(f"n={n:5d}: KS stat={ks_stat:.4f}, p-value={p_val:.4f}")
```
