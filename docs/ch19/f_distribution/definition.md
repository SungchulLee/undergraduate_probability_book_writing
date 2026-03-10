# F Distribution

The $F$ distribution is the distribution of the ratio of two independent chi-squared random variables, each divided by their degrees of freedom. It arises in comparing variances from two normal populations and in the analysis of variance.

## Definition

If $V_1 \sim \chi^2_{d_1}$ and $V_2 \sim \chi^2_{d_2}$ are independent, then:

$$
F = \frac{V_1/d_1}{V_2/d_2} \sim F_{d_1, d_2}
$$

The PDF is:

$$
f_F(f) = \frac{1}{B(d_1/2,\; d_2/2)\; f}\;\sqrt{\frac{(d_1 f)^{d_1}\; d_2^{d_2}}{(d_1 f + d_2)^{d_1+d_2}}}, \quad f > 0
$$

## Explanation

### PDF derivation sketch

Set $F = (X/d_1)/(Y/d_2)$ and $W = Y$ where $X \sim \chi^2_{d_1}$, $Y \sim \chi^2_{d_2}$ are independent. The Jacobian of the inverse transformation is $|d_1 w/d_2|$. After substituting and recognizing that the $w$-dependence factors into a Gamma density, integrating out $w$ yields the marginal PDF above.

### Support and shape

The $F$ distribution is supported on $(0, \infty)$ and is right-skewed, with skewness decreasing as both $d_1$ and $d_2$ increase.

## Examples

**Example 1.** Verify the $F$ distribution by constructing it from chi-squared samples.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
d1, d2, n_sim = 5, 10, 200_000

v1 = np.random.chisquare(d1, n_sim)
v2 = np.random.chisquare(d2, n_sim)
f_samples = (v1 / d1) / (v2 / d2)

theory_mean = d2 / (d2 - 2)
print(f"Mean: {f_samples.mean():.4f}  (theory: {theory_mean:.4f})")

stat, pval = stats.kstest(f_samples, 'f', args=(d1, d2))
print(f"KS test p-value: {pval:.4f}")
```
