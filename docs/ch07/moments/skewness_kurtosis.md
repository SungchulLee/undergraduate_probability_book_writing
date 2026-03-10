# Skewness and Kurtosis

Skewness measures asymmetry; kurtosis measures tail weight. Both are dimensionless, standardized moments.

## Definition

**Skewness** (third standardized moment):

$$
\gamma_1 = E\!\left[\left(\frac{X-\mu}{\sigma}\right)^3\right]
$$

**Kurtosis** (fourth standardized moment):

$$
\kappa_4 = E\!\left[\left(\frac{X-\mu}{\sigma}\right)^4\right]
$$

**Excess kurtosis** $= \kappa_4 - 3$ (normalized so the normal distribution gives 0).

## Explanation

### Skewness Interpretation

| $\gamma_1$ | Shape | Tail |
|:-----------|:------|:-----|
| $< 0$ | Left-skewed | Long left tail |
| $= 0$ | Symmetric | Balanced |
| $> 0$ | Right-skewed | Long right tail |

Any symmetric distribution has $\gamma_1 = 0$. The exponential has $\gamma_1 = 2$.

### Kurtosis Interpretation

| Excess kurtosis | Type | Tails |
|:----------------|:-----|:------|
| $> 0$ | Leptokurtic | Heavier than normal |
| $= 0$ | Mesokurtic | Normal-like |
| $< 0$ | Platykurtic | Lighter than normal |

Kurtosis measures **tail weight**, not peakedness. The $t$-distribution with $\nu > 4$ has excess kurtosis $6/(\nu-4)$. Uniform has excess kurtosis $-6/5$.

## Examples

**Example.** Compare common distributions:

| Distribution | Skewness | Excess Kurtosis |
|:-------------|:--------:|:---------------:|
| $N(0,1)$ | 0 | 0 |
| $\text{Exp}(1)$ | 2 | 6 |
| $\text{Uniform}(0,1)$ | 0 | $-1.2$ |
| $t(5)$ | 0 | 6 |

```python
from scipy import stats

dists = {
    'Normal': stats.norm(),
    'Exp(1)': stats.expon(),
    'Uniform': stats.uniform(),
    't(5)': stats.t(5),
    'Chi2(3)': stats.chi2(3),
}

for name, d in dists.items():
    s, k = float(d.stats('s')), float(d.stats('k'))
    print(f"{name:10s}: skew={s:+.4f}, excess_kurt={k:+.4f}")
```
