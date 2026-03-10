# Chi-Squared Distribution

The chi-squared distribution with $d$ degrees of freedom is the distribution of a sum of $d$ independent squared standard normals. It is the fundamental building block for inference about variance in normal populations.

## Definition

If $Z_1, Z_2, \ldots, Z_d$ are iid $N(0,1)$, then:

$$
\chi^2_d = \sum_{i=1}^d Z_i^2
$$

Equivalently, since $Z^2 \sim \operatorname{Gamma}(1/2, 1/2)$ and the Gamma family is closed under convolution with a common rate:

$$
\chi^2_d \sim \operatorname{Gamma}\!\left(\frac{d}{2},\; \frac{1}{2}\right)
$$

## Explanation

### Why a squared normal is Gamma(1/2, 1/2)

For $x > 0$, the CDF of $Z^2$ is:

$$
P(Z^2 \le x) = P(-\sqrt{x} \le Z \le \sqrt{x}) = 2\int_0^{\sqrt{x}} \frac{1}{\sqrt{2\pi}} e^{-s^2/2}\, ds
$$

Differentiating with respect to $x$ gives the Gamma$(1/2, 1/2)$ density:

$$
f_{Z^2}(x) = \frac{(1/2)^{1/2}}{\Gamma(1/2)}\, x^{-1/2}\, e^{-x/2}
$$

### From one to d degrees of freedom

By additivity of the Gamma distribution with common rate parameter:

$$
\chi^2_d = \underbrace{\operatorname{Gamma}(1/2,\,1/2) * \cdots * \operatorname{Gamma}(1/2,\,1/2)}_{d} = \operatorname{Gamma}(d/2,\,1/2)
$$

### PDF

From the Gamma PDF with shape $d/2$ and rate $1/2$:

$$
f_{\chi^2_d}(x) = \frac{(1/2)^{d/2}}{\Gamma(d/2)}\, x^{d/2-1}\, e^{-x/2}, \quad x > 0
$$

## Examples

**Example 1.** Verify that simulated sums of squared normals match the $\chi^2_d$ distribution.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
d = 7
n_sim = 200_000

# Sum of d squared standard normals
z = np.random.standard_normal((n_sim, d))
chi2_sim = np.sum(z**2, axis=1)

print(f"Simulated mean: {chi2_sim.mean():.3f}  (theory: {d})")
print(f"Simulated var:  {chi2_sim.var():.3f}  (theory: {2*d})")

stat, pval = stats.kstest(chi2_sim, 'chi2', args=(d,))
print(f"KS test p-value: {pval:.4f}")
```
