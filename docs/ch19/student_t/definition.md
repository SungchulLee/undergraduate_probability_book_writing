# Student's t Distribution

The Student's $t$ distribution arises when a standard normal is divided by the square root of an independent chi-squared divided by its degrees of freedom. It governs inference about the mean of a normal population when the variance is unknown.

## Definition

If $Z \sim N(0,1)$ and $V \sim \chi^2_d$ are independent, then:

$$
T = \frac{Z}{\sqrt{V/d}} \sim t_d
$$

The PDF is:

$$
f_T(t) = \frac{1}{\sqrt{d}\; B(1/2,\; d/2)} \left(1 + \frac{t^2}{d}\right)^{-(d+1)/2}, \quad -\infty < t < \infty
$$

where $B(a,b) = \Gamma(a)\Gamma(b)/\Gamma(a+b)$.

## Explanation

### Derivation of the PDF

Let $T = Z/\sqrt{V/d}$ and $U = V$ with Jacobian $|\partial(z,v)/\partial(t,u)| = \sqrt{u/d}$. The joint density of $(T,U)$ is:

$$
f_{T,U}(t,u) = f_Z(t\sqrt{u/d})\; f_V(u)\; \sqrt{u/d}
$$

Setting $\lambda = (1 + t^2/d)/2$, the $u$-dependence factors into a $\operatorname{Gamma}((d+1)/2,\, \lambda)$ density. Integrating out $u$ leaves the marginal PDF of $T$.

### Shape of the distribution

The $t_d$ density is symmetric about zero and bell-shaped, but has heavier tails than the standard normal. The tails decay polynomially as $|t|^{-(d+1)}$ rather than exponentially. As $d$ increases, the distribution approaches $N(0,1)$.

## Examples

**Example 1.** Construct $t_5$ samples from the definition and verify against scipy.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
d = 5
n_sim = 200_000

z = np.random.standard_normal(n_sim)
v = np.random.chisquare(d, n_sim)
t_samples = z / np.sqrt(v / d)

print(f"Mean: {t_samples.mean():.4f}  (theory: 0)")
print(f"Var:  {t_samples.var():.4f}  (theory: {d/(d-2):.4f})")

stat, pval = stats.kstest(t_samples, 't', args=(d,))
print(f"KS test p-value: {pval:.4f}")
```
