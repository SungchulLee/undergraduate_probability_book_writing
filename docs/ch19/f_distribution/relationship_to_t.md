# Relationship Between F and t Distributions

Squaring a $t$ random variable produces an $F$ random variable with 1 numerator degree of freedom. This connects two-sided $t$-tests to $F$-tests.

## Definition

If $T \sim t_d$, then:

$$
T^2 \sim F_{1, d}
$$

## Explanation

### Proof

Write $T = Z/\sqrt{V/d}$ with $Z \sim N(0,1)$ and $V \sim \chi^2_d$ independent. Then:

$$
T^2 = \frac{Z^2}{V/d} = \frac{\chi^2_1/1}{\chi^2_d/d} \sim F_{1,d}
$$

### Equivalence of two-sided t-test and F-test

A two-sided $t$-test rejects when $|T| > t_{\alpha/2,d}$, which is equivalent to $T^2 > t_{\alpha/2,d}^2 = F_{\alpha,1,d}$. Thus a two-sided $t$-test with $d$ degrees of freedom is the same as an $F$-test with $(1, d)$ degrees of freedom.

### Summary of relationships

| Distribution | Construction | Parameters |
|-------------|-------------|------------|
| $\chi^2_d$ | $\sum_{i=1}^d Z_i^2$ | $d$ = number of squared normals |
| $t_d$ | $Z / \sqrt{\chi^2_d/d}$ | $d$ = df in denominator |
| $F_{d_1,d_2}$ | $(\chi^2_{d_1}/d_1)/(\chi^2_{d_2}/d_2)$ | $d_1, d_2$ = numerator, denominator df |

Key inter-relationships: $t_d^2 = F_{1,d}$, $\;1/F_{d_1,d_2} = F_{d_2,d_1}$, $\;\chi^2_d = \operatorname{Gamma}(d/2, 1/2)$, and $t_d \to N(0,1)$ as $d \to \infty$.

## Examples

**Example 1.** Verify that $T^2 \sim F_{1,d}$ by simulation.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
d, n_sim = 10, 200_000

t_samples = np.random.standard_t(d, n_sim)
t_squared = t_samples**2

stat, pval = stats.kstest(t_squared, 'f', args=(1, d))
print(f"KS test T^2 ~ F(1,{d}): stat={stat:.4f}, p={pval:.4f}")

# Verify equivalence of critical values
alpha = 0.05
t_crit = stats.t(d).ppf(1 - alpha/2)
f_crit = stats.f(1, d).ppf(1 - alpha)
print(f"t_crit^2 = {t_crit**2:.4f}, F_crit = {f_crit:.4f}")
```
