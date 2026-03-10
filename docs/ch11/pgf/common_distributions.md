# PGF of Common Discrete Distributions

Each standard discrete distribution has a closed-form PGF that makes moments and sum properties transparent.

## Definition

| Distribution | PGF $G_X(s)$ | $E[X]$ | $\text{Var}(X)$ |
|:-------------|:-------------|:-------|:----------------|
| $\text{Bern}(p)$ | $q + ps$ | $p$ | $pq$ |
| $\text{Bin}(n, p)$ | $(q + ps)^n$ | $np$ | $npq$ |
| $\text{Geo}(p)$ | $ps/(1-qs)$ | $1/p$ | $q/p^2$ |
| $\text{NB}(r, p)$ | $(ps/(1-qs))^r$ | $r/p$ | $rq/p^2$ |
| $\text{Pois}(\lambda)$ | $e^{\lambda(s-1)}$ | $\lambda$ | $\lambda$ |

where $q = 1 - p$ throughout.

## Explanation

### Poisson PGF

$$
G_X(s) = \sum_{k=0}^{\infty}\frac{\lambda^k}{k!}e^{-\lambda}\,s^k = e^{-\lambda}\sum_{k=0}^{\infty}\frac{(\lambda s)^k}{k!} = e^{\lambda(s-1)}
$$

$G_X'(s) = \lambda e^{\lambda(s-1)}$, so $E[X] = \lambda$. $G_X''(1) = \lambda^2$, so $\text{Var}(X) = \lambda^2 + \lambda - \lambda^2 = \lambda$.

### Geometric PGF

$$
G_X(s) = \sum_{k=1}^{\infty}q^{k-1}p\,s^k = ps\sum_{k=0}^{\infty}(qs)^k = \frac{ps}{1-qs}
$$

### Sum Properties from PGFs

$\text{Bin}(n,p) + \text{Bin}(m,p) \sim \text{Bin}(n+m,p)$: $(q+ps)^n(q+ps)^m = (q+ps)^{n+m}$.

$\text{Pois}(\lambda_1) + \text{Pois}(\lambda_2) \sim \text{Pois}(\lambda_1+\lambda_2)$: $e^{\lambda_1(s-1)}e^{\lambda_2(s-1)} = e^{(\lambda_1+\lambda_2)(s-1)}$.

## Examples

**Example.** Verify the Poisson PGF by evaluating at several points.

```python
import numpy as np
from math import factorial

lam = 4.0

# G(s) = exp(lambda*(s-1))
def pgf_pois(s, lam):
    return np.exp(lam * (s - 1))

# Direct computation: sum P(X=k)*s^k
def pgf_direct(s, lam, K=30):
    return sum(np.exp(-lam)*lam**k/factorial(k) * s**k for k in range(K))

for s in [0.0, 0.3, 0.5, 0.8, 1.0]:
    print(f"s={s}: formula={pgf_pois(s, lam):.6f}, "
          f"direct={pgf_direct(s, lam):.6f}")
```
