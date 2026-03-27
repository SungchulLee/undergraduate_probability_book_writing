# Cauchy--Schwarz Inequality

## Statement

!!! info "Cauchy--Schwarz Inequality for Random Variables"
    For any random variables $X$ and $Y$ with finite second moments:

    $$
    \bigl|E[XY]\bigr|^2 \leq E[X^2]\,E[Y^2]
    $$

    Equivalently, in terms of covariance:

    $$
    \bigl|\text{Cov}(X, Y)\bigr| \leq \sigma_X \, \sigma_Y
    $$

    Equality holds if and only if $Y = aX + b$ for some constants $a, b$ (i.e., $X$ and $Y$ are linearly related with probability 1).

---

## Proof

The proof uses a simple but powerful idea: the variance of any random variable is non-negative.

Let $U = X - \mu_X$ and $V = Y - \mu_Y$ be the centered versions. For any real number $t$, consider the random variable $U + tV$. Since variance is non-negative:

$$
0 \leq \text{Var}(U + tV) = E[(U + tV)^2]
$$

Expanding:

$$
0 \leq E[U^2] + 2t\,E[UV] + t^2\,E[V^2]
$$

This is a quadratic in $t$: $f(t) = E[V^2]\,t^2 + 2\,E[UV]\,t + E[U^2]$. Since $f(t) \geq 0$ for all $t$, the discriminant must be non-positive:

$$
\Delta = 4\bigl(E[UV]\bigr)^2 - 4\,E[U^2]\,E[V^2] \leq 0
$$

Therefore:

$$
\bigl(E[UV]\bigr)^2 \leq E[U^2]\,E[V^2]
$$

Since $E[UV] = \text{Cov}(X, Y)$, $E[U^2] = \text{Var}(X) = \sigma_X^2$, and $E[V^2] = \text{Var}(Y) = \sigma_Y^2$:

$$
\bigl|\text{Cov}(X, Y)\bigr| \leq \sigma_X\,\sigma_Y
$$

$\blacksquare$

---

## Equality Condition

Equality holds ($\Delta = 0$) if and only if $f(t^*) = 0$ for some $t^* \in \mathbb{R}$, which means $U + t^* V = 0$ with probability 1, i.e., $X - \mu_X = -t^*(Y - \mu_Y)$ almost surely.

This is equivalent to $Y = aX + b$ for constants $a = -1/t^*$ and $b = \mu_Y - a\mu_X$.

---

## Corollary: Correlation Is Bounded

Dividing both sides of $|\text{Cov}(X,Y)| \leq \sigma_X \sigma_Y$ by $\sigma_X \sigma_Y > 0$:

$$
|\rho(X, Y)| \leq 1 \qquad\text{i.e.,}\qquad -1 \leq \rho(X, Y) \leq 1
$$

This is the rigorous justification for the range of the correlation coefficient stated in the previous section.

---

## The E[XY] Form

Applying the inequality to non-centered variables $X$ and $Y$ directly:

$$
\bigl(E[XY]\bigr)^2 \leq E[X^2]\,E[Y^2]
$$

This is sometimes called the **Schwarz inequality for expectations** and is useful for bounding mixed moments.

---

## Example

??? example "Bounding an Unknown Expectation"
    Suppose $E[X^2] = 4$ and $E[Y^2] = 9$. Without knowing the joint distribution, we can bound:

    $$
    |E[XY]| \leq \sqrt{E[X^2]\,E[Y^2]} = \sqrt{4 \cdot 9} = 6
    $$

    So $-6 \leq E[XY] \leq 6$.

??? example "Application to Correlation"
    Suppose $\text{Var}(X) = 16$, $\text{Var}(Y) = 25$, and $\text{Cov}(X,Y) = -15$. Then:

    $$
    |\text{Cov}(X,Y)| = 15 \leq \sqrt{16 \cdot 25} = 20 \quad\checkmark
    $$

    $$
    \rho(X,Y) = \frac{-15}{\sqrt{16}\sqrt{25}} = \frac{-15}{20} = -0.75
    $$

    which satisfies $|\rho| \leq 1$.

---

## Python Verification

```python
import numpy as np

np.random.seed(42)
N = 1_000_000

# Generate correlated random variables
X = np.random.normal(0, 2, N)  # sigma_X = 2
Y = 0.6 * X + np.random.normal(0, 1, N)

cov_XY = np.cov(X, Y)[0, 1]
sigma_X = np.std(X, ddof=0)
sigma_Y = np.std(Y, ddof=0)

print(f"|Cov(X,Y)| = {abs(cov_XY):.4f}")
print(f"sigma_X * sigma_Y = {sigma_X * sigma_Y:.4f}")
print(f"Cauchy-Schwarz satisfied: {abs(cov_XY) <= sigma_X * sigma_Y}")
```
