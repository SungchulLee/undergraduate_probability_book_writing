# Uncorrelated Implies Independent (Normal Case)

For the bivariate normal distribution, zero correlation implies independence -- a property that fails for most other distributions. Understanding when this special implication holds is essential for applied statistics.

## Definition

The relationship between correlation and independence has three levels:

$$
\text{Independence} \implies \text{Cov}(X, Y) = 0 \qquad \text{(always true)}
$$

$$
\text{Cov}(X, Y) = 0 \;\not\!\!\!\implies \text{Independence} \qquad \text{(in general)}
$$

$$
(X, Y)^T \text{ bivariate normal},\; \rho = 0 \implies \text{Independence} \qquad \text{(special case)}
$$

## Explanation

### Why it works for the bivariate normal

When $\rho = 0$, the bivariate normal PDF factors:

$$
f(x, y) = \frac{1}{2\pi\sigma_X\sigma_Y} \exp\!\left(-\frac{\tilde{x}^2 + \tilde{y}^2}{2}\right) = f_X(x) \cdot f_Y(y)
$$

Factorization of the joint PDF into marginals is the definition of independence. The key is that the exponent contains no cross term when $\rho = 0$.

### Common misconception

The statement "$X$ and $Y$ are normal and uncorrelated, therefore independent" is **wrong**. The correct statement requires that $(X, Y)^T$ is **jointly** bivariate normal, not merely that each marginal is normal.

### Classic counterexample

Let $X \sim N(0, 1)$ and let $S$ be an independent fair coin flip taking values $\pm 1$. Define $Y = SX$.

- **Y is standard normal.** By the symmetry of $N(0, 1)$, $P(Y \leq y) = P(X \leq y)$.
- **Cov(X, Y) = 0.** Since $E[XY] = \frac{1}{2}E[X^2] - \frac{1}{2}E[X^2] = 0$.
- **X and Y are dependent.** We have $|Y| = |X|$ with probability 1, which cannot hold for independent continuous variables.

The pair $(X, Y)^T$ is not bivariate normal -- its mass concentrates on the lines $y = x$ and $y = -x$.

## Examples

Simulate the counterexample and verify all three claims.

```python
import numpy as np

np.random.seed(42)
n = 100_000

X = np.random.randn(n)
S = np.random.choice([-1, 1], size=n)
Y = S * X

# Claim 1: Y is standard normal
print("Claim 1: Y ~ N(0,1)")
print(f"  E[Y] = {Y.mean():.4f},  Var(Y) = {Y.var():.4f}")

# Claim 2: Cov(X, Y) = 0
print(f"\nClaim 2: Cov(X, Y) = {np.cov(X, Y)[0, 1]:.4f}")

# Claim 3: X and Y are dependent (|Y| = |X| always)
print(f"\nClaim 3: max | |Y| - |X| | = {np.max(np.abs(np.abs(Y) - np.abs(X))):.1e}")

# Independence test: P(X>0, Y>0) vs P(X>0)*P(Y>0)
p_joint = np.mean((X > 0) & (Y > 0))
p_product = np.mean(X > 0) * np.mean(Y > 0)
print(f"\nP(X>0, Y>0)       = {p_joint:.4f}")
print(f"P(X>0) * P(Y>0)   = {p_product:.4f}")
print(f"These differ because X and Y are dependent.")
```
