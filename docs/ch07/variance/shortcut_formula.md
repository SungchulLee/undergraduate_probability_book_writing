# Var(X) = E[X²] − (E[X])² Formula

## The Shortcut Formula

$$

\text{Var}(X) = E[X^2] - (E[X])^2

$$

This is often easier to compute than the definition $E[(X - \mu)^2]$ because it avoids subtracting the mean inside the squared term.

---

## Proof

$$

\text{Var}(X) = E[(X - \mu)^2] = E[X^2 - 2\mu X + \mu^2] = E[X^2] - 2\mu E[X] + \mu^2 = E[X^2] - \mu^2

$$

---

## Examples

### Bernoulli

$E[X] = p$, $E[X^2] = 0^2(1-p) + 1^2 p = p$

$$

\text{Var}(X) = p - p^2 = p(1-p) = pq

$$

### Geometric

If $X \sim \text{Geo}(p)$, we can show $E[X] = 1/p$ and $E[X^2] = (2-p)/p^2$, giving

$$

\text{Var}(X) = \frac{2-p}{p^2} - \frac{1}{p^2} = \frac{1-p}{p^2} = \frac{q}{p^2}

$$

### Poisson

If $X \sim \text{Poisson}(\lambda)$, then $E[X] = \lambda$ and $E[X(X-1)] = \lambda^2$, so $E[X^2] = \lambda^2 + \lambda$, giving

$$

\text{Var}(X) = \lambda^2 + \lambda - \lambda^2 = \lambda

$$

---

## Important Warning

!!! warning "Numerical Instability"
    While $E[X^2] - (E[X])^2$ is algebraically convenient, it can suffer from **catastrophic cancellation** in numerical computations when $E[X^2]$ and $(E[X])^2$ are both large and close in value. For numerical computation, use the definition form or a numerically stable algorithm.

---

## Python Implementation

```python
import numpy as np

# Shortcut formula for fair die
values = np.arange(1, 7)
probs = np.ones(6) / 6

E_X = np.sum(values * probs)
E_X2 = np.sum(values**2 * probs)
var_shortcut = E_X2 - E_X**2

print(f"E[X] = {E_X}")
print(f"E[X²] = {E_X2:.4f}")
print(f"Var(X) = E[X²] - (E[X])² = {E_X2:.4f} - {E_X**2:.4f} = {var_shortcut:.4f}")

# Verify with definition
var_def = np.sum((values - E_X)**2 * probs)
print(f"Var(X) via definition = {var_def:.4f}")

# Poisson example
lam = 5.0
np.random.seed(42)
samples = np.random.poisson(lam, 1_000_000)
print(f"\nPoisson(λ={lam}):")
print(f"Theoretical Var = {lam}")
print(f"MC Var = {np.var(samples):.4f}")
```
