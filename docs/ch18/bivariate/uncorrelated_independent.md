# Uncorrelated Implies Independent (Normal Case)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Overview

In general, zero correlation does **not** imply independence. However, for the bivariate normal distribution, zero correlation **does** imply independence. This is a special and important property. Understanding when this implication holds — and when it fails — is essential for applied statistics.

---

## The General Picture

$$
\text{Independence} \implies \text{Cov}(X, Y) = 0 \qquad \text{(always true)}
$$

$$
\text{Cov}(X, Y) = 0 \;\not\!\!\!\implies \text{Independence} \qquad \text{(in general)}
$$

$$
(X, Y)^T \text{ bivariate normal},\; \text{Cov}(X, Y) = 0 \implies \text{Independence} \qquad \text{(special case!)}
$$

---

## Why It Works for the Bivariate Normal

When $\rho = 0$, the bivariate normal PDF factors:

$$
f(x, y) = \frac{1}{2\pi\sigma_X\sigma_Y} \exp\left(-\frac{\tilde{x}^2 + \tilde{y}^2}{2}\right) = f_X(x) \cdot f_Y(y)
$$

Factorization of the joint PDF into marginals is the **definition** of independence. The key is that the exponent contains no cross term $\tilde{x}\tilde{y}$ when $\rho = 0$.

---

## Common Misconception

A statement that is **wrong**:

> "$X$ and $Y$ are normal and $\text{Cov}(X, Y) = 0$, therefore $X$ and $Y$ are independent."

This is incorrect because $X$ and $Y$ being individually normal does not mean $(X, Y)^T$ is bivariate normal. The correct statement requires that $X$ and $Y$ are **jointly** bivariate normal.

---

## Counterexample: Marginally Normal but Not Jointly Normal

This classic counterexample demonstrates that two marginally normal, uncorrelated random variables can still be dependent.

**Construction.** Let $X \sim N(0, 1)$. Independently of $X$, flip a fair coin and record the outcome $S$ as $+1$ (heads) or $-1$ (tails). Define:

$$
Y = S \cdot X
$$

**Claim 1: $Y$ is standard normal.**

$$
P(Y \leq y) = P(S = 1)P(X \leq y) + P(S = -1)P(X \geq -y)
$$

$$
= \frac{1}{2}\int_{-\infty}^y \frac{1}{\sqrt{2\pi}} e^{-s^2/2}\,ds + \frac{1}{2}\int_{-y}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-s^2/2}\,ds
$$

By symmetry of the standard normal, $P(X \geq -y) = P(X \leq y)$, so:

$$
P(Y \leq y) = P(X \leq y)
$$

Therefore $Y \sim N(0, 1)$.

**Claim 2: $\text{Cov}(X, Y) = 0$.**

$$
E[XY] = P(S = 1) \cdot E[XY \mid S = 1] + P(S = -1) \cdot E[XY \mid S = -1]
$$

$$
= \frac{1}{2}E[X^2] + \frac{1}{2}E[-X^2] = \frac{1}{2}(1) - \frac{1}{2}(1) = 0
$$

Since $E[X] = E[Y] = 0$:

$$
\text{Cov}(X, Y) = E[XY] - E[X]E[Y] = 0 - 0 = 0
$$

**Claim 3: $X$ and $Y$ are NOT independent.**

By construction, if $X = 2$, then $Y$ is either $2$ or $-2$. In particular:

$$
P(|Y| = |X|) = 1
$$

If $X$ and $Y$ were independent, $P(|Y| = |X|) = 0$ (since both are continuous). Therefore $X$ and $Y$ are dependent.

**Why this doesn't contradict the theorem.** Although $X$ and $Y$ are each marginally $N(0, 1)$, the vector $(X, Y)^T$ is **not** bivariate normal. The joint distribution places all mass on the two lines $y = x$ and $y = -x$ (each with probability $1/2$), which is not a bivariate normal distribution.

---

## Python: Demonstrating the Counterexample

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n = 10_000

# Generate the counterexample
X = np.random.randn(n)
S = np.random.choice([-1, 1], size=n)
Y = S * X

# Verify properties
print(f"Correlation(X, Y) = {np.corrcoef(X, Y)[0, 1]:.6f}")
print(f"E[X] = {X.mean():.4f}, E[Y] = {Y.mean():.4f}")
print(f"Var(X) = {X.var():.4f}, Var(Y) = {Y.var():.4f}")
print(f"P(|Y| = |X|) = {np.mean(np.abs(Y - np.abs(X)) < 1e-10):.4f}")

# Independence test: P(X > 0, Y > 0) vs P(X > 0) * P(Y > 0)
p_joint = np.mean((X > 0) & (Y > 0))
p_x = np.mean(X > 0)
p_y = np.mean(Y > 0)
print(f"\nP(X>0, Y>0) = {p_joint:.4f}")
print(f"P(X>0) * P(Y>0) = {p_x * p_y:.4f}")
print(f"If independent these should be equal — they're not!")

# Visualization
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Scatter plot
axes[0].scatter(X[:2000], Y[:2000], s=2, alpha=0.3)
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')
axes[0].set_title(f'X vs Y (ρ = {np.corrcoef(X, Y)[0, 1]:.3f})')
axes[0].set_aspect('equal')

# Marginal of X
axes[1].hist(X, bins=60, density=True, alpha=0.6, label='X')
axes[1].hist(Y, bins=60, density=True, alpha=0.6, label='Y')
x_grid = np.linspace(-4, 4, 200)
axes[1].plot(x_grid, 1/np.sqrt(2*np.pi) * np.exp(-x_grid**2/2),
             'k--', label='N(0,1)')
axes[1].set_title('Marginals: Both N(0,1)')
axes[1].legend()

# Evidence of dependence: |Y| vs |X|
axes[2].scatter(np.abs(X[:2000]), np.abs(Y[:2000]), s=2, alpha=0.3)
axes[2].plot([0, 4], [0, 4], 'r--', linewidth=2, label='|Y| = |X|')
axes[2].set_xlabel('|X|')
axes[2].set_ylabel('|Y|')
axes[2].set_title('Dependence: |Y| = |X| always')
axes[2].legend()

plt.tight_layout()
plt.show()
```

---

## Summary Table

| Condition | Independence? |
|:---|:---:|
| $X \perp Y$ | Always $\implies \text{Cov}(X, Y) = 0$ |
| $\text{Cov}(X, Y) = 0$ | Not sufficient in general |
| $X, Y$ both normal, $\text{Cov}(X, Y) = 0$ | **Not sufficient** |
| $(X, Y)^T$ bivariate normal, $\text{Cov}(X, Y) = 0$ | **Sufficient** ✓ |

---

## Key Takeaways

- For the bivariate normal, uncorrelated $\iff$ independent. This is a special property not shared by most distributions.
- The critical requirement is that $(X, Y)^T$ is **jointly** bivariate normal, not merely that $X$ and $Y$ are each marginally normal.
- The classic counterexample ($Y = SX$ with random sign $S$) shows that two standard normal variables can be uncorrelated yet completely dependent.
- In practice, always verify joint normality before concluding that zero correlation implies independence.
