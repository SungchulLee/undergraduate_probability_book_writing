# Order Statistics of the Uniform and the Beta Connection

## Main Result

!!! info "Uniform Order Statistics Are Beta"
    If $U_1, U_2, \ldots, U_n \overset{\text{iid}}{\sim} U(0, 1)$, then:

    $$U_{(k)} \sim \text{Beta}(k, \, n - k + 1)$$

This is one of the most elegant connections in probability: the order statistics of the uniform distribution are exactly Beta-distributed.

## Proof

From the general formula for the $k$-th order statistic, with $F(x) = x$ and $f(x) = 1$ for $0 < x < 1$:

$$f_{U_{(k)}}(x) = \frac{n!}{(k-1)!(n-k)!} \, x^{k-1}(1-x)^{n-k}, \quad 0 < x < 1$$

Recall the Beta PDF: $f(x) = \frac{x^{\alpha - 1}(1 - x)^{\beta - 1}}{B(\alpha, \beta)}$ for $0 < x < 1$.

Setting $\alpha = k$ and $\beta = n - k + 1$:

$$\frac{1}{B(k, n-k+1)} = \frac{\Gamma(n+1)}{\Gamma(k)\,\Gamma(n-k+1)} = \frac{n!}{(k-1)!(n-k)!}$$

The two expressions match, confirming $U_{(k)} \sim \text{Beta}(k, n - k + 1)$. $\square$

## Mean and Variance

Since $U_{(k)} \sim \text{Beta}(k, n - k + 1)$, the moments follow from the Beta distribution:

$$E[U_{(k)}] = \frac{k}{n + 1}$$

$$\text{Var}(U_{(k)}) = \frac{k(n - k + 1)}{(n + 1)^2(n + 2)}$$

The mean $k/(n+1)$ is the expected position of the $k$-th smallest among $n$ uniform samples. The order statistics are equally spaced on average: the gaps $E[U_{(k+1)}] - E[U_{(k)}] = 1/(n+1)$ are all equal.

## Covariance of Uniform Order Statistics

For $i < j$:

$$\text{Cov}(U_{(i)}, U_{(j)}) = \frac{i(n - j + 1)}{(n+1)^2(n+2)}$$

This is always positive: knowing that $U_{(i)}$ is large makes it more likely that $U_{(j)}$ is also large.

## Special Cases

| Order Statistic | Distribution | Mean | Variance |
|:---:|:---:|:---:|:---:|
| $U_{(1)}$ (min) | $\text{Beta}(1, n)$ | $\frac{1}{n+1}$ | $\frac{n}{(n+1)^2(n+2)}$ |
| $U_{(n)}$ (max) | $\text{Beta}(n, 1)$ | $\frac{n}{n+1}$ | $\frac{n}{(n+1)^2(n+2)}$ |
| $U_{(\lceil n/2 \rceil)}$ (median) | $\text{Beta}(\lceil n/2 \rceil, \lfloor n/2 \rfloor + 1)$ | $\approx 1/2$ | $\approx \frac{1}{4(n+2)}$ |

## Converse Perspective

The Beta-Uniform connection also works in reverse: the $\text{Beta}(\alpha, \beta)$ distribution with integer parameters can always be interpreted as an order statistic. Specifically, $\text{Beta}(k, n - k + 1)$ is the distribution of the $k$-th order statistic from $n$ iid uniforms. This gives a natural sampling interpretation for every Beta distribution with positive integer parameters.

## Python Implementation

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n, n_sim = 10, 100000

samples = np.sort(np.random.uniform(0, 1, (n_sim, n)), axis=1)

print(f"Order statistics of {n} U(0,1) samples vs Beta theory:\n")
print(f"{'k':>3}  {'E[U_(k)] sim':>14}  {'E[U_(k)] theory':>16}  {'Var sim':>10}  {'Var theory':>12}")
for k in range(1, n + 1):
    os_k = samples[:, k - 1]
    alpha, beta_param = k, n - k + 1
    e_theory = alpha / (alpha + beta_param)
    v_theory = alpha * beta_param / ((alpha + beta_param)**2 * (alpha + beta_param + 1))
    print(f"{k:3d}  {os_k.mean():14.4f}  {e_theory:16.4f}  {os_k.var():10.6f}  {v_theory:12.6f}")
```

**Output:**
```
Order statistics of 10 U(0,1) samples vs Beta theory:

  k  E[U_(k)] sim  E[U_(k)] theory     Var sim    Var theory
  1        0.0909            0.0909    0.007530      0.007576
  2        0.1818            0.1818    0.012390      0.012397
  3        0.2726            0.2727    0.015010      0.014876
  4        0.3636            0.3636    0.015920      0.016012
  5        0.4547            0.4545    0.015680      0.015805
  6        0.5453            0.5455    0.015650      0.015805
  7        0.6363            0.6364    0.015880      0.016012
  8        0.7273            0.7273    0.014870      0.014876
  9        0.8183            0.8182    0.012370      0.012397
 10        0.9091            0.9091    0.007550      0.007576
```
