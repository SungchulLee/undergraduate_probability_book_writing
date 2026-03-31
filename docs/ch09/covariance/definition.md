# Covariance Definition and Properties
<<<<<<< Updated upstream

## Motivation

Variance measures how a single random variable deviates from its mean. But when we have two random variables, we often want to know whether they tend to deviate **together**. Covariance captures exactly this: it quantifies the degree to which $X$ and $Y$ move in the same direction.

---

## Definition

!!! info "Covariance"
    For random variables $X$ and $Y$ with finite second moments, the **covariance** of $X$ and $Y$ is

    $$
    \text{Cov}(X, Y) = E\bigl[(X - \mu_X)(Y - \mu_Y)\bigr]
    $$

    where $\mu_X = E[X]$ and $\mu_Y = E[Y]$.

**Interpretation.** When $X$ is above its mean and $Y$ is above its mean simultaneously, the product $(X - \mu_X)(Y - \mu_Y)$ is positive. When they deviate in opposite directions, the product is negative. The covariance averages these products:

- $\text{Cov}(X, Y) > 0$: $X$ and $Y$ tend to increase together
- $\text{Cov}(X, Y) < 0$: when one increases, the other tends to decrease
- $\text{Cov}(X, Y) = 0$: no linear association (the variables are **uncorrelated**)

---

## Computational Shortcut

Expanding the definition gives a formula that is usually easier to compute.

$$
\text{Cov}(X, Y) = E[XY] - E[X]\,E[Y]
$$

**Derivation.**

$$
\text{Cov}(X, Y) = E\bigl[(X - \mu_X)(Y - \mu_Y)\bigr] = E[XY - \mu_Y X - \mu_X Y + \mu_X \mu_Y]
$$

By linearity of expectation:

$$
= E[XY] - \mu_Y E[X] - \mu_X E[Y] + \mu_X \mu_Y = E[XY] - \mu_X \mu_Y
$$

!!! tip "Analogy with Variance"
    Setting $Y = X$ in the shortcut gives $\text{Cov}(X, X) = E[X^2] - (E[X])^2 = \text{Var}(X)$, which is the familiar shortcut formula for variance.

---

## Properties

1. **Symmetry**: $\text{Cov}(X, Y) = \text{Cov}(Y, X)$

2. **Covariance with itself**: $\text{Cov}(X, X) = \text{Var}(X)$

3. **Covariance with a constant**: $\text{Cov}(X, c) = 0$ for any constant $c$

4. **Scaling and shifting**: $\text{Cov}(aX + b,\; cY + d) = ac \cdot \text{Cov}(X, Y)$

5. **Bilinearity**: For constants $a_1, a_2, b_1, b_2$:

$$
\text{Cov}(a_1 X_1 + a_2 X_2,\; Y) = a_1 \text{Cov}(X_1, Y) + a_2 \text{Cov}(X_2, Y)
$$

More generally:

$$
\text{Cov}\!\left(\sum_{i=1}^m a_i X_i,\; \sum_{j=1}^n b_j Y_j\right) = \sum_{i=1}^m \sum_{j=1}^n a_i b_j \,\text{Cov}(X_i, Y_j)
$$

**Proof of Property 4.** Using the shortcut:

$$
\text{Cov}(aX+b,\; cY+d) = E[(aX+b)(cY+d)] - E[aX+b]\,E[cY+d]
$$

$$
= ac\,E[XY] + ad\,E[X] + bc\,E[Y] + bd - (a\,E[X]+b)(c\,E[Y]+d)
$$

$$
= ac\,E[XY] - ac\,E[X]\,E[Y] = ac\,\text{Cov}(X,Y)
$$

---

## Example: Joint PMF Table

??? example "Worked Example"
    Let $(X, Y)$ have the joint PMF:

    |  | $Y = 0$ | $Y = 1$ |
    |:---:|:---:|:---:|
    | $X = 1$ | 0.2 | 0.3 |
    | $X = 2$ | 0.4 | 0.1 |

    **Step 1.** Compute marginal means.

    $$
    E[X] = 1(0.5) + 2(0.5) = 1.5, \qquad E[Y] = 0(0.6) + 1(0.4) = 0.4
    $$

    **Step 2.** Compute $E[XY]$.

    $$
    E[XY] = (1)(0)(0.2) + (1)(1)(0.3) + (2)(0)(0.4) + (2)(1)(0.1) = 0.5
    $$

    **Step 3.** Apply the shortcut.

    $$
    \text{Cov}(X, Y) = E[XY] - E[X]\,E[Y] = 0.5 - (1.5)(0.4) = -0.1
    $$

    The negative covariance indicates that larger values of $X$ tend to occur with smaller values of $Y$ in this distribution.

---

## Python Verification

```python
import numpy as np

# Joint PMF from the example
x_vals = np.array([1, 1, 2, 2])
y_vals = np.array([0, 1, 0, 1])
probs  = np.array([0.2, 0.3, 0.4, 0.1])

E_X  = np.sum(x_vals * probs)        # 1.5
E_Y  = np.sum(y_vals * probs)        # 0.4
E_XY = np.sum(x_vals * y_vals * probs)  # 0.5

cov_XY = E_XY - E_X * E_Y
print(f"E[X]  = {E_X}")
print(f"E[Y]  = {E_Y}")
print(f"E[XY] = {E_XY}")
print(f"Cov(X,Y) = {cov_XY}")  # -0.1
```
=======
>>>>>>> Stashed changes
