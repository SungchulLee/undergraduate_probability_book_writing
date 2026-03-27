# PGF of Common Discrete Distributions

## Bernoulli$(p)$

If $X \sim \text{Bernoulli}(p)$:

$$G_X(s) = E[s^X] = s^0(1-p) + s^1 \cdot p = 1 - p + ps$$

**Moments:** $G'(s) = p$, so $E[X] = G'(1) = p$. Since $G''(s) = 0$, $\text{Var}(X) = 0 + p - p^2 = p(1-p)$.

## Binomial$(n, p)$

If $X \sim B(n, p)$, then $X = \sum_{i=1}^n X_i$ with $X_i \stackrel{\text{iid}}{\sim} \text{Bernoulli}(p)$. By the product rule:

$$G_X(s) = [G_{X_1}(s)]^n = (1 - p + ps)^n$$

**Moments:** $G'(s) = np(1-p+ps)^{n-1}$, so $E[X] = np$.

$$G''(s) = n(n-1)p^2(1-p+ps)^{n-2} \implies G''(1) = n(n-1)p^2$$

$$\text{Var}(X) = n(n-1)p^2 + np - n^2p^2 = np(1-p)$$

## Geometric$(p)$

If $X \sim \text{Geo}(p)$ with $P(X = k) = (1-p)^{k-1}p$ for $k = 1, 2, \ldots$

$$G_X(s) = \sum_{k=1}^{\infty} (1-p)^{k-1}p\,s^k = ps \sum_{j=0}^{\infty} [(1-p)s]^j = \frac{ps}{1 - (1-p)s}$$

for $|s| < \frac{1}{1-p}$.

**Moments:** Let $q = 1-p$. Then $G'(s) = \frac{p}{(1 - qs)^2}$, so $E[X] = G'(1) = \frac{1}{p}$.

$$G''(s) = \frac{2pq}{(1-qs)^3} \implies G''(1) = \frac{2q}{p^2}$$

$$\text{Var}(X) = \frac{2q}{p^2} + \frac{1}{p} - \frac{1}{p^2} = \frac{q}{p^2}$$

## Negative Binomial$(r, p)$

If $X \sim \text{NB}(r, p)$ is the sum of $r$ iid $\text{Geo}(p)$ random variables:

$$G_X(s) = \left[\frac{ps}{1 - (1-p)s}\right]^r$$

**Moments:** $E[X] = \frac{r}{p}$ and $\text{Var}(X) = \frac{r(1-p)}{p^2}$.

## Poisson$(\lambda)$

If $X \sim \text{Po}(\lambda)$:

$$G_X(s) = \sum_{k=0}^{\infty} \frac{\lambda^k}{k!}e^{-\lambda}\,s^k = e^{-\lambda}\sum_{k=0}^{\infty}\frac{(\lambda s)^k}{k!} = e^{-\lambda} \cdot e^{\lambda s} = e^{\lambda(s-1)}$$

**Moments:** $G'(s) = \lambda e^{\lambda(s-1)}$, so $E[X] = \lambda$.

$$G''(s) = \lambda^2 e^{\lambda(s-1)} \implies G''(1) = \lambda^2$$

$$\text{Var}(X) = \lambda^2 + \lambda - \lambda^2 = \lambda$$

## Summary Table

| Distribution | PGF $G_X(s)$ | $E[X]$ | $\text{Var}(X)$ |
|:---|:---:|:---:|:---:|
| $\text{Bernoulli}(p)$ | $1 - p + ps$ | $p$ | $p(1-p)$ |
| $B(n, p)$ | $(1-p+ps)^n$ | $np$ | $np(1-p)$ |
| $\text{Geo}(p)$ | $\frac{ps}{1-(1-p)s}$ | $\frac{1}{p}$ | $\frac{1-p}{p^2}$ |
| $\text{NB}(r, p)$ | $\left[\frac{ps}{1-(1-p)s}\right]^r$ | $\frac{r}{p}$ | $\frac{r(1-p)}{p^2}$ |
| $\text{Po}(\lambda)$ | $e^{\lambda(s-1)}$ | $\lambda$ | $\lambda$ |

## Python Verification

```python
import numpy as np
from scipy.misc import derivative

pgfs = {
    "Bernoulli(0.4)": lambda s: 0.6 + 0.4 * s,
    "B(10, 0.4)":     lambda s: (0.6 + 0.4 * s)**10,
    "Geo(0.3)":       lambda s: 0.3 * s / (1 - 0.7 * s),
    "Po(5)":          lambda s: np.exp(5 * (s - 1)),
}

exact = {
    "Bernoulli(0.4)": (0.4, 0.24),
    "B(10, 0.4)":     (4.0, 2.4),
    "Geo(0.3)":       (10/3, 70/9),
    "Po(5)":          (5.0, 5.0),
}

for name, G in pgfs.items():
    EX = derivative(G, 1, n=1, dx=1e-6)
    EXX1 = derivative(G, 1, n=2, dx=1e-6)
    VarX = EXX1 + EX - EX**2
    mu, var = exact[name]
    print(f"{name}:  E[X]={EX:.4f} (exact {mu:.4f}),  Var={VarX:.4f} (exact {var:.4f})")
```
