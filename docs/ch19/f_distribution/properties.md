# F Distribution Properties

The $F$ distribution has a mean that depends only on the denominator degrees of freedom, and it satisfies a clean reciprocal property: inverting an $F$ swaps the two degree-of-freedom parameters.

## Definition

For $F \sim F_{d_1, d_2}$:

$$
E[F] = \frac{d_2}{d_2 - 2} \;\;(d_2 > 2), \qquad \operatorname{Var}(F) = \frac{2d_2^2(d_1+d_2-2)}{d_1(d_2-2)^2(d_2-4)} \;\;(d_2 > 4)
$$

The reciprocal property states:

$$
\frac{1}{F} \sim F_{d_2, d_1}
$$

## Explanation

### Mean depends only on the denominator

The mean $d_2/(d_2-2)$ is independent of $d_1$. For small $d_2$, the mean is substantially larger than 1. As $d_2 \to \infty$, the mean approaches 1.

### Reciprocal property

By definition, $F = (V_1/d_1)/(V_2/d_2)$, so $1/F = (V_2/d_2)/(V_1/d_1) \sim F_{d_2, d_1}$. Swapping numerator and denominator swaps the degrees of freedom.

### Connection to the Beta distribution

If $F \sim F_{d_1, d_2}$, then:

$$
\frac{d_1 F/d_2}{1 + d_1 F/d_2} \sim \operatorname{Beta}\!\left(\frac{d_1}{2},\; \frac{d_2}{2}\right)
$$

## Examples

**Example 1.** Verify the mean and the reciprocal property by simulation.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
d1, d2, n_sim = 5, 10, 200_000

f_samples = np.random.f(d1, d2, n_sim)
print(f"Mean of F({d1},{d2}): {f_samples.mean():.4f}  (theory: {d2/(d2-2):.4f})")

# Reciprocal property
recip = 1.0 / f_samples
stat, pval = stats.kstest(recip, 'f', args=(d2, d1))
print(f"KS test 1/F({d1},{d2}) ~ F({d2},{d1}): p={pval:.4f}")
```
