# Variance Shortcut Formula

The identity $\text{Var}(X) = E[X^2] - (E[X])^2$ converts a variance computation into two expectation computations, avoiding the need to center first.

## Definition

$$
\text{Var}(X) = E[X^2] - (E[X])^2
$$

Equivalently, $E[X^2] = \text{Var}(X) + (E[X])^2$, which shows that the second moment always exceeds the squared mean (unless $X$ is constant).

## Explanation

### Proof

$$
E[(X-\mu)^2] = E[X^2 - 2\mu X + \mu^2] = E[X^2] - 2\mu\,E[X] + \mu^2 = E[X^2] - \mu^2
$$

### Factorial Moment Trick

For integer-valued variables, the **factorial moment** $E[X(X-1)] = E[X^2] - E[X]$ is often easier to compute. Then:

$$
E[X^2] = E[X(X-1)] + E[X], \qquad \text{Var}(X) = E[X(X-1)] + E[X] - (E[X])^2
$$

## Examples

**Example 1 (Geometric).** $X \sim \text{Geo}(p)$: $E[X] = 1/p$, $E[X^2] = (2-p)/p^2$.

$$
\text{Var}(X) = \frac{2-p}{p^2} - \frac{1}{p^2} = \frac{1-p}{p^2}
$$

**Example 2 (Poisson).** $X \sim \text{Poi}(\lambda)$: $E[X] = \lambda$, $E[X(X-1)] = \lambda^2$.

$$
E[X^2] = \lambda^2 + \lambda, \qquad \text{Var}(X) = \lambda^2 + \lambda - \lambda^2 = \lambda
$$

For Poisson, mean equals variance.

```python
import numpy as np

# Poisson: Var = lambda
lam = 5.0
np.random.seed(42)
samples = np.random.poisson(lam, 1_000_000)
print(f"Poisson({lam}): theory Var={lam}, MC Var={samples.var():.4f}")

# Geometric: Var = (1-p)/p^2
p = 0.3
theory_var = (1 - p) / p**2
samples = np.random.geometric(p, 1_000_000)
print(f"Geo({p}): theory Var={theory_var:.4f}, MC Var={samples.var():.4f}")
```
