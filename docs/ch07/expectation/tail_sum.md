# Tail Sum Formula

The tail sum formula expresses the expectation as a sum (or integral) of survival probabilities — often the simplest way to compute $E[X]$ for non-negative variables.

## Definition

**Discrete** (non-negative integer-valued $X$):

$$
E[X] = \sum_{k=1}^{\infty} P(X \ge k) = \sum_{k=0}^{\infty} P(X > k)
$$

**Continuous** (non-negative $X$):

$$
E[X] = \int_0^{\infty} P(X > t)\,dt = \int_0^{\infty} [1 - F_X(t)]\,dt
$$

## Explanation

### Proof (Discrete)

$$
\sum_{k=1}^{\infty} P(X \ge k) = \sum_{k=1}^{\infty}\sum_{j=k}^{\infty} P(X=j) = \sum_{j=1}^{\infty}\sum_{k=1}^{j} P(X=j) = \sum_{j=1}^{\infty} j\,P(X=j) = E[X]
$$

The swap of summation order shows each $P(X=j)$ is counted exactly $j$ times.

### Proof (Continuous)

$$
\int_0^{\infty} P(X > t)\,dt = \int_0^{\infty}\!\int_t^{\infty} f(x)\,dx\,dt = \int_0^{\infty}\!\int_0^{x} dt\,f(x)\,dx = \int_0^{\infty} x\,f(x)\,dx = E[X]
$$

### General Version

For any random variable (not necessarily non-negative):

$$
E[X] = \int_0^{\infty} P(X > t)\,dt - \int_0^{\infty} P(X < -t)\,dt
$$

## Examples

**Example 1.** $X \sim \text{Geo}(p)$: $P(X \ge k) = (1-p)^{k-1}$.

$$
E[X] = \sum_{k=1}^{\infty}(1-p)^{k-1} = \frac{1}{p}
$$

**Example 2.** $X \sim \text{Exp}(\lambda)$: $P(X > t) = e^{-\lambda t}$.

$$
E[X] = \int_0^{\infty} e^{-\lambda t}\,dt = \frac{1}{\lambda}
$$

```python
import numpy as np

# Geometric(0.3): tail sum vs exact
p = 0.3
E_tail = sum((1-p)**(k-1) for k in range(1, 1000))
print(f"E[Geo({p})]: tail sum = {E_tail:.4f}, exact = {1/p:.4f}")

# Exponential(2): tail sum vs exact
from scipy import integrate
lam = 2.0
E_tail_exp, _ = integrate.quad(lambda t: np.exp(-lam*t), 0, np.inf)
print(f"E[Exp({lam})]: tail sum = {E_tail_exp:.4f}, exact = {1/lam:.4f}")
```
