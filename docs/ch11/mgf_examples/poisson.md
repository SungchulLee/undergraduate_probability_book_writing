# MGF of Poisson

The Poisson MGF confirms that mean equals variance and provides an elegant proof of the Poisson limit theorem.

## Definition

If $X \sim \text{Pois}(\lambda)$:

$$
M_X(t) = e^{\lambda(e^t - 1)}
$$

This exists for all $t \in \mathbb{R}$.

## Explanation

### Derivation

$$
M_X(t) = \sum_{k=0}^{\infty}e^{tk}\frac{\lambda^k}{k!}e^{-\lambda} = e^{-\lambda}\sum_{k=0}^{\infty}\frac{(\lambda e^t)^k}{k!} = e^{-\lambda}\,e^{\lambda e^t} = e^{\lambda(e^t - 1)}
$$

### Moments

$M_X'(t) = \lambda e^t\,e^{\lambda(e^t-1)}$, so $E[X] = \lambda$.

$M_X''(0) = \lambda^2 + \lambda$, so $\text{Var}(X) = \lambda^2 + \lambda - \lambda^2 = \lambda$.

This confirms the Poisson's defining property: $E[X] = \text{Var}(X) = \lambda$.

### Poisson Limit Theorem via MGF

For $X_n \sim \text{Bin}(n, \lambda/n)$:

$$
M_{X_n}(t) = \left(1 + \frac{\lambda}{n}(e^t - 1)\right)^n \to e^{\lambda(e^t - 1)} = M_{\text{Pois}(\lambda)}(t)
$$

By the convergence theorem, $\text{Bin}(n, \lambda/n) \xrightarrow{d} \text{Pois}(\lambda)$.

### Sum Property

$\text{Pois}(\lambda_1) + \text{Pois}(\lambda_2) \sim \text{Pois}(\lambda_1 + \lambda_2)$ for independent summands.

## Examples

**Example.** $X \sim \text{Pois}(5)$: $E[X] = \text{Var}(X) = 5$.

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

X = np.random.poisson(5, n_sim)
print(f"E[X] = {X.mean():.4f}  (theory: 5)")
print(f"Var(X) = {X.var():.4f}  (theory: 5)")

# Poisson limit: Bin(1000, 0.005) ≈ Pois(5)
Y = np.random.binomial(1000, 0.005, n_sim)
print(f"\nBin(1000, 0.005): E={Y.mean():.4f}, Var={Y.var():.4f}")
```
