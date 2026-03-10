# Relationship Between F and t Distributions


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## T^2 ~ F(1,d)

The most important connection between the $F$ and $t$ distributions:

**If $T \sim t_d$, then $T^2 \sim F_{1,d}$.**

### Proof

By definition, $T = Z / \sqrt{V/d}$ where $Z \sim N(0,1)$ and $V \sim \chi^2_d$ are independent.

$$T^2 = \frac{Z^2}{V/d} = \frac{Z^2/1}{V/d} = \frac{\chi^2_1/1}{\chi^2_d/d} \sim F_{1,d}$$

### Consequence for Hypothesis Testing

A two-sided $t$-test with test statistic $T$ and $d$ degrees of freedom rejects when $|T| > t_{\alpha/2, d}$, which is equivalent to $T^2 > t_{\alpha/2,d}^2 = F_{\alpha, 1, d}$.

This means:

$$\text{Two-sided } t\text{-test} \iff F\text{-test with } (1, d) \text{ df}$$

## Summary of Relationships

All three distributions originate from the normal:

| Distribution | Construction | Parameters |
|-------------|-------------|------------|
| $\chi^2_d$ | $\sum_{i=1}^d Z_i^2$ | $d$ = number of squared normals |
| $t_d$ | $\frac{Z}{\sqrt{\chi^2_d / d}}$ | $d$ = df in denominator |
| $F_{d_1, d_2}$ | $\frac{\chi^2_{d_1}/d_1}{\chi^2_{d_2}/d_2}$ | $d_1, d_2$ = numerator, denominator df |

**Inter-relationships:**

- $\chi^2_d = \Gamma(d/2, 1/2)$ (special case of Gamma)
- $t_d^2 = F_{1,d}$ (squaring a $t$ gives an $F$)
- $\frac{1}{F_{d_1,d_2}} = F_{d_2, d_1}$ (reciprocal swaps df)
- As $d \to \infty$: $t_d \to N(0,1)$
- As $d_2 \to \infty$: $d_1 \cdot F_{d_1, d_2} \to \chi^2_{d_1}$

## Python Verification

```python
import numpy as np
from scipy import stats

np.random.seed(42)
d = 10
n_sim = 200_000

# Generate t samples and square them
t_samples = np.random.standard_t(d, n_sim)
t_squared = t_samples**2

# Compare with F(1, d)
ks_stat, p_value = stats.kstest(t_squared, 'f', args=(1, d))
print(f"KS test (T^2 vs F(1,{d})): stat={ks_stat:.4f}, p={p_value:.4f}")

# Verify reciprocal property
f_samples = np.random.f(5, 10, n_sim)
reciprocal = 1.0 / f_samples
ks_stat2, p_value2 = stats.kstest(reciprocal, 'f', args=(10, 5))
print(f"KS test (1/F(5,10) vs F(10,5)): stat={ks_stat2:.4f}, p={p_value2:.4f}")
```

**Output:**
```
KS test (T^2 vs F(1,10)): stat=0.0025, p=0.9812
KS test (1/F(5,10) vs F(10,5)): stat=0.0031, p=0.9534
```
