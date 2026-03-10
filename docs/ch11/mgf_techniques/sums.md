# MGF of Sums of Independent Random Variables

The MGF of a sum of independent variables is the product of their MGFs — the key property that makes MGFs a powerful tool for distribution theory.

## Definition

If $X_1, \ldots, X_n$ are **independent**, then

$$
M_{X_1 + \cdots + X_n}(t) = \prod_{i=1}^n M_{X_i}(t)
$$

For **iid** variables: $M_{\sum X_i}(t) = (M_{X_1}(t))^n$.

## Explanation

### Proof

$$
M_{X+Y}(t) = E[e^{t(X+Y)}] = E[e^{tX}\,e^{tY}] = E[e^{tX}]\,E[e^{tY}] = M_X(t)\,M_Y(t)
$$

The factorization $E[e^{tX}\,e^{tY}] = E[e^{tX}]\,E[e^{tY}]$ uses independence. The proof extends to $n$ variables by induction.

### Closure Results

This multiplicative property yields all the standard closure results:

| Independent sum | Result |
|:----------------|:-------|
| $\text{Bin}(n, p) + \text{Bin}(m, p)$ | $\text{Bin}(n+m, p)$ |
| $\text{Pois}(\lambda_1) + \text{Pois}(\lambda_2)$ | $\text{Pois}(\lambda_1+\lambda_2)$ |
| $N(\mu_1, \sigma_1^2) + N(\mu_2, \sigma_2^2)$ | $N(\mu_1+\mu_2, \sigma_1^2+\sigma_2^2)$ |
| $\text{Gamma}(\alpha_1, \lambda) + \text{Gamma}(\alpha_2, \lambda)$ | $\text{Gamma}(\alpha_1+\alpha_2, \lambda)$ |
| $\text{NB}(r_1, p) + \text{NB}(r_2, p)$ | $\text{NB}(r_1+r_2, p)$ |

### Warning: Same Family Required

The sum of $\text{Gamma}(\alpha_1, \lambda_1) + \text{Gamma}(\alpha_2, \lambda_2)$ with $\lambda_1 \ne \lambda_2$ is **not** gamma. The rate parameters must match.

## Examples

**Example.** $X_1, \ldots, X_{10} \stackrel{\text{iid}}{\sim} \text{Exp}(2)$. Then $S \sim \text{Gamma}(10, 2)$.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n_sim = 200_000

S = np.random.exponential(0.5, (n_sim, 10)).sum(axis=1)
print(f"Sum of 10 Exp(2): mean={S.mean():.3f} (theory: 5)")
print(f"                  var={S.var():.3f} (theory: 2.5)")

# KS test against Gamma(10, scale=0.5)
stat, pval = stats.kstest(S, 'gamma', args=(10, 0, 0.5))
print(f"KS test p-value: {pval:.4f} (should be large)")
```
