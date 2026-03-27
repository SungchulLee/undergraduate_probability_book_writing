# Independence Implies Zero Covariance

## The Forward Direction

!!! info "Theorem"
    If $X$ and $Y$ are independent, then $\text{Cov}(X, Y) = 0$ (equivalently, $\rho(X, Y) = 0$).

**Proof.** Independence implies $E[XY] = E[X]\,E[Y]$ (proved in the next section on products). Therefore:

$$
\text{Cov}(X, Y) = E[XY] - E[X]\,E[Y] = 0
$$

$\blacksquare$

This gives a quick check: if two random variables are independent, you can immediately conclude they are uncorrelated.

---

## The Converse Is False

!!! warning "Uncorrelated Does Not Imply Independent"
    There exist random variables with $\text{Cov}(X, Y) = 0$ that are **not** independent. Zero covariance means no **linear** association, but a nonlinear dependence can still be present.

### Classic Counterexample

Let $X$ be uniform on $\{-1, 0, 1\}$ (each with probability $1/3$), and let $Y = X^2$.

**Step 1.** $Y$ is completely determined by $X$, so $X$ and $Y$ are clearly dependent.

**Step 2.** Compute the covariance:

$$
E[X] = \frac{1}{3}(-1 + 0 + 1) = 0
$$

$$
E[XY] = E[X \cdot X^2] = E[X^3] = \frac{1}{3}\bigl((-1)^3 + 0^3 + 1^3\bigr) = 0
$$

$$
\text{Cov}(X, Y) = E[XY] - E[X]\,E[Y] = 0 - 0 \cdot E[Y] = 0
$$

So $\text{Cov}(X, Y) = 0$ even though $Y$ is a deterministic function of $X$.

**Why does this happen?** The relationship $Y = X^2$ is symmetric about $X = 0$. The positive and negative linear contributions cancel perfectly, leaving zero covariance despite complete dependence.

---

## Logical Relationships

The following diagram summarizes the implications:

$$
\text{Independent} \implies \text{Uncorrelated (Cov = 0)} \implies E[XY] = E[X]\,E[Y]
$$

None of the reverse arrows hold in general.

!!! tip "Special Case: Joint Normality"
    For **jointly normal** random variables, uncorrelated **does** imply independent. This is one of the remarkable properties of the multivariate normal distribution (Chapter 18). Outside of this special case, zero correlation is strictly weaker than independence.

---

## Another Counterexample

??? example "Dependent but Uncorrelated: Continuous Case"
    Let $X \sim \text{Uniform}(-1, 1)$ and $Y = X^2$. Then $E[X] = 0$, so

    $$
    \text{Cov}(X, Y) = E[XY] - E[X]\,E[Y] = E[X^3] - 0 = \int_{-1}^{1} \frac{x^3}{2}\,dx = 0
    $$

    by the symmetry of $x^3$ on $[-1, 1]$. Yet $Y$ is completely determined by $X$.

---

## Python Verification

```python
import numpy as np

np.random.seed(42)
N = 1_000_000

# Discrete counterexample: X uniform on {-1, 0, 1}, Y = X^2
X = np.random.choice([-1, 0, 1], size=N)
Y = X**2

cov = np.cov(X, Y)[0, 1]
independent = np.allclose(
    np.mean((X == 1) & (Y == 0)),       # P(X=1, Y=0)
    np.mean(X == 1) * np.mean(Y == 0)   # P(X=1)*P(Y=0)
)

print(f"Cov(X, Y) = {cov:.4f}")      # ≈ 0
print(f"Independent? {independent}")   # False
```
