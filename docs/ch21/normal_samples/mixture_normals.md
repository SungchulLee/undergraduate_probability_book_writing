# Mixture of Normals

Combining samples from different normal distributions produces a mixture distribution — a weighted sum of densities that can model multimodal data.

## Definition

A **mixture of two normals** has density:

$$
f(x) = w_1 \, \phi(x; \mu_1, \sigma_1^2) + w_2 \, \phi(x; \mu_2, \sigma_2^2)
$$

where $w_1 + w_2 = 1$, $w_i > 0$, and $\phi(x; \mu, \sigma^2)$ is the normal density.

## Explanation

### Simulation

To sample from a mixture: with probability $w_1$ draw from $N(\mu_1, \sigma_1^2)$, otherwise from $N(\mu_2, \sigma_2^2)$. This is equivalent to generating $n_1 = w_1 n$ samples from the first component and $n_2 = w_2 n$ from the second.

### Moments

$$
E[X] = w_1 \mu_1 + w_2 \mu_2
$$

$$
\operatorname{Var}(X) = w_1(\sigma_1^2 + \mu_1^2) + w_2(\sigma_2^2 + \mu_2^2) - (w_1\mu_1 + w_2\mu_2)^2
$$

### Bimodality

The mixture is bimodal when the component means are sufficiently separated relative to their standard deviations: roughly $\lvert \mu_1 - \mu_2 \rvert > 2\max(\sigma_1, \sigma_2)$.

## Examples

**Example.** 60% from $N(1, 1)$ and 40% from $N(4, 1)$.

```python
import numpy as np

np.random.seed(42)

w1, mu1, sig1 = 0.6, 1.0, 1.0
w2, mu2, sig2 = 0.4, 4.0, 1.0
n = 10_000

n1 = int(w1 * n)
n2 = n - n1
X = np.concatenate([np.random.normal(mu1, sig1, n1),
                    np.random.normal(mu2, sig2, n2)])

E_theory = w1 * mu1 + w2 * mu2
print(f"Sample mean: {X.mean():.4f} (theory: {E_theory})")
print(f"Sample var:  {X.var():.4f}")
print(f"Min={X.min():.2f}, Max={X.max():.2f}")
```
