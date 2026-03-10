# MGF of Exponential and Gamma

The gamma MGF is a power of the exponential MGF, reflecting the sum-of-exponentials decomposition.

## Definition

**Exponential:** If $X \sim \text{Exp}(\lambda)$:

$$
M_X(t) = \frac{\lambda}{\lambda - t}, \qquad t < \lambda
$$

**Gamma:** If $X \sim \text{Gamma}(\alpha, \lambda)$:

$$
M_X(t) = \left(\frac{\lambda}{\lambda - t}\right)^\alpha, \qquad t < \lambda
$$

## Explanation

### Derivation

$$
M_X(t) = \int_0^{\infty} e^{tx}\,\lambda e^{-\lambda x}\,dx = \frac{\lambda}{\lambda - t}
$$

Convergence requires $t < \lambda$.

### Moments

Exponential: $E[X] = 1/\lambda$, $\text{Var}(X) = 1/\lambda^2$.

Gamma: $E[X] = \alpha/\lambda$, $\text{Var}(X) = \alpha/\lambda^2$.

### Sum Property

$\sum_{i=1}^n \text{Exp}(\lambda) \sim \text{Gamma}(n, \lambda)$, since $(\lambda/(\lambda-t))^n$ is the gamma MGF. More generally, $\text{Gamma}(\alpha_1, \lambda) + \text{Gamma}(\alpha_2, \lambda) \sim \text{Gamma}(\alpha_1 + \alpha_2, \lambda)$ (same rate required).

## Examples

**Example.** $X_1, \ldots, X_5 \stackrel{\text{iid}}{\sim} \text{Exp}(2)$: $S \sim \text{Gamma}(5, 2)$, $E[S] = 5/2$, $\text{Var}(S) = 5/4$.

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

X = np.random.exponential(1/2, (n_sim, 5))  # rate 2, scale 1/2
S = X.sum(axis=1)

print(f"E[S] = {S.mean():.4f}  (theory: {5/2})")
print(f"Var(S) = {S.var():.4f}  (theory: {5/4})")
```
