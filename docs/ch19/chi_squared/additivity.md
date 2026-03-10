# Additivity of Chi-Squared

Independent chi-squared random variables add: the sum is again chi-squared with degrees of freedom equal to the sum of the individual degrees of freedom. This property is central to the decomposition of sums of squares in ANOVA and regression.

## Definition

If $V_1 \sim \chi^2_{d_1}$ and $V_2 \sim \chi^2_{d_2}$ are independent, then:

$$
V_1 + V_2 \sim \chi^2_{d_1 + d_2}
$$

More generally, for independent $V_i \sim \chi^2_{d_i}$, $i = 1, \ldots, k$:

$$
\sum_{i=1}^k V_i \sim \chi^2_{d_1 + \cdots + d_k}
$$

## Explanation

### Proof via moment generating functions

Using the MGF of the chi-squared and independence:

$$
\varphi_{V_1+V_2}(t) = (1-2t)^{-d_1/2} \cdot (1-2t)^{-d_2/2} = (1-2t)^{-(d_1+d_2)/2}
$$

This is the MGF of $\chi^2_{d_1+d_2}$, so the result follows by uniqueness.

### Proof via Gamma additivity

Since $\chi^2_{d_i} \sim \operatorname{Gamma}(d_i/2, 1/2)$ and independent Gamma random variables with a common rate add in the shape parameter:

$$
V_1 + V_2 \sim \operatorname{Gamma}\!\left(\frac{d_1+d_2}{2},\; \frac{1}{2}\right) = \chi^2_{d_1+d_2}
$$

### Application: Cochran's decomposition

Additivity used in reverse yields the key identity:

$$
\underbrace{\sum_{i=1}^n \left(\frac{X_i - \mu}{\sigma}\right)^2}_{\chi^2_n} = \underbrace{\sum_{i=1}^n \left(\frac{X_i - \bar{X}}{\sigma}\right)^2}_{\chi^2_{n-1}} + \underbrace{\left(\frac{\bar{X} - \mu}{\sigma/\sqrt{n}}\right)^2}_{\chi^2_1}
$$

If the two right-hand terms are independent, the MGF factorization forces the first term to be $\chi^2_{n-1}$.

## Examples

**Example 1.** Verify additivity: generate independent $\chi^2_3$ and $\chi^2_7$ samples and test that their sum is $\chi^2_{10}$.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n_sim = 200_000

v1 = np.random.chisquare(3, n_sim)
v2 = np.random.chisquare(7, n_sim)
total = v1 + v2

print(f"Mean: {total.mean():.3f}  (theory: 10)")
print(f"Var:  {total.var():.3f}  (theory: 20)")

stat, pval = stats.kstest(total, 'chi2', args=(10,))
print(f"KS test p-value: {pval:.4f}")
```
