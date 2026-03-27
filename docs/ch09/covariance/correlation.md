# Correlation Coefficient

## Motivation

Covariance tells us the direction of a linear relationship, but its magnitude depends on the units of $X$ and $Y$. Doubling all values of $X$ would double the covariance, even though the relationship has not changed. The **correlation coefficient** solves this by normalizing covariance to a dimensionless quantity between $-1$ and $1$.

---

## Definition

!!! info "Correlation Coefficient"
    For random variables $X$ and $Y$ with positive standard deviations $\sigma_X$ and $\sigma_Y$, the **(Pearson) correlation coefficient** is

    $$
    \rho(X, Y) = \frac{\text{Cov}(X, Y)}{\sigma_X \, \sigma_Y}
    $$

Equivalently, $\rho(X, Y) = \text{Cov}\!\left(\frac{X - \mu_X}{\sigma_X},\; \frac{Y - \mu_Y}{\sigma_Y}\right)$, so correlation is the covariance of the standardized variables.

---

## Range of Correlation

$$
-1 \leq \rho(X, Y) \leq 1
$$

This follows from the **Cauchy--Schwarz inequality** $|\text{Cov}(X,Y)| \leq \sigma_X \sigma_Y$, which is proved in the next section.

---

## Equality Cases

!!! info "Perfect Linear Relationship"
    $\rho(X, Y) = 1$ if and only if $Y = aX + b$ for some constants with $a > 0$.

    $\rho(X, Y) = -1$ if and only if $Y = aX + b$ for some constants with $a < 0$.

**Proof sketch.** If $Y = aX + b$ with $a > 0$, then $\text{Cov}(X, Y) = a\,\text{Var}(X)$, $\sigma_Y = a\sigma_X$, so $\rho = a\,\text{Var}(X)/(a\sigma_X^2) = 1$. The converse follows from the equality condition of Cauchy--Schwarz.

---

## Interpretation

| Range of $\rho$ | Interpretation |
|:---:|:---|
| $\rho = 1$ | Perfect positive linear relationship |
| $0.7 \leq \rho < 1$ | Strong positive linear association |
| $0.3 \leq \rho < 0.7$ | Moderate positive linear association |
| $0 < \rho < 0.3$ | Weak positive linear association |
| $\rho = 0$ | No linear association (uncorrelated) |
| $\rho < 0$ | Negative linear association (same scale) |

!!! warning "Correlation Is Not Causation"
    A high correlation between $X$ and $Y$ does not imply that changes in $X$ cause changes in $Y$. They may both be driven by a third variable, or the relationship may be coincidental.

!!! tip "Correlation Measures Linear Association Only"
    Two variables can have a strong nonlinear relationship yet $\rho = 0$. For instance, if $X \sim \text{Uniform}(-1, 1)$ and $Y = X^2$, then $\rho(X, Y) = 0$ even though $Y$ is completely determined by $X$.

---

## Properties

1. $\rho(X, Y) = \rho(Y, X)$

2. $\rho(aX + b,\; cY + d) = \text{sign}(ac)\,\rho(X, Y)$ for $ac \neq 0$

3. $\rho(X, X) = 1$

4. If $X$ and $Y$ are independent, then $\rho(X, Y) = 0$ (converse is false in general)

---

## Example

??? example "Computing Correlation from a Joint PMF"
    Using the joint PMF from the covariance section:

    |  | $Y = 0$ | $Y = 1$ |
    |:---:|:---:|:---:|
    | $X = 1$ | 0.2 | 0.3 |
    | $X = 2$ | 0.4 | 0.1 |

    We found $\text{Cov}(X, Y) = -0.1$, $E[X] = 1.5$, $E[Y] = 0.4$.

    **Compute variances:**

    $$
    E[X^2] = 1^2(0.5) + 2^2(0.5) = 2.5, \quad \text{Var}(X) = 2.5 - 1.5^2 = 0.25
    $$

    $$
    E[Y^2] = 0^2(0.6) + 1^2(0.4) = 0.4, \quad \text{Var}(Y) = 0.4 - 0.4^2 = 0.24
    $$

    **Correlation:**

    $$
    \rho(X, Y) = \frac{-0.1}{\sqrt{0.25}\sqrt{0.24}} = \frac{-0.1}{0.5 \times 0.4899} \approx -0.408
    $$

    The moderate negative correlation is consistent with the pattern in the PMF table: higher $X$ values are associated with lower $Y$ values.

---

## Visualizing Correlation

The companion script `correlation_simulation.py` generates scatter plots of bivariate normal samples at $\rho = -0.8, 0, 0.5, 0.95$, showing how the shape of the point cloud tightens around a line as $|\rho| \to 1$.

```python
import numpy as np

# Compute sample correlation
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

rho = np.corrcoef(x, y)[0, 1]
print(f"Sample correlation: {rho:.4f}")  # 0.7746
```
