# Chi-Squared Properties

The moment generating function, mean, and variance of the chi-squared distribution all follow directly from its representation as a Gamma distribution.

## Definition

The key properties of $\chi^2_d \sim \operatorname{Gamma}(d/2, 1/2)$ are:

$$
\varphi_{\chi^2_d}(t) = (1-2t)^{-d/2}, \quad E[\chi^2_d] = d, \quad \operatorname{Var}(\chi^2_d) = 2d
$$

## Explanation

### Moment generating function

Computing the MGF by integrating against the Gamma density and recognizing the normalizing constant:

$$
\varphi_{\chi^2_d}(t) = \int_0^\infty e^{tx} \frac{(1/2)^{d/2}}{\Gamma(d/2)} x^{d/2-1} e^{-x/2}\, dx = (1-2t)^{-d/2}, \quad t < \frac{1}{2}
$$

### Mean and variance from the definition

Each $Z_i^2$ has $E[Z_i^2] = 1$ and $\operatorname{Var}(Z_i^2) = E[Z_i^4] - 1 = 3 - 1 = 2$. By linearity and independence:

$$
E[\chi^2_d] = d, \qquad \operatorname{Var}(\chi^2_d) = 2d
$$

### Additional properties

| Property | Value |
|----------|-------|
| Mode | $\max(d-2, 0)$ |
| Skewness | $\sqrt{8/d}$ |

As $d$ increases, the skewness decreases and the distribution approaches normality by the CLT, since $\chi^2_d$ is a sum of $d$ iid random variables.

## Examples

**Example 1.** Verify the MGF numerically by comparing $E[e^{tX}]$ from simulation with the closed form.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
d = 6
samples = np.random.chisquare(d, 300_000)

for t in [0.1, 0.2, 0.3]:
    sim_mgf = np.mean(np.exp(t * samples))
    theory_mgf = (1 - 2*t)**(-d/2)
    print(f"t={t}: simulated={sim_mgf:.4f}, theory={theory_mgf:.4f}")
```
