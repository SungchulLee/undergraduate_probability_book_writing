# Expectation of Products (Independent Case)
<<<<<<< Updated upstream

## Motivation

Linearity tells us $E[X + Y] = E[X] + E[Y]$ always. What about $E[XY]$? In general, $E[XY] \neq E[X]\,E[Y]$. However, when $X$ and $Y$ are independent, expectations **do** factor over products.

---

## Theorem

!!! info "Expectation of a Product of Independent Random Variables"
    If $X$ and $Y$ are independent, then

    $$
    E[XY] = E[X]\,E[Y]
    $$

    provided both expectations exist.

**Proof (discrete case).** By independence, $p(x, y) = p_X(x)\,p_Y(y)$:

$$
E[XY] = \sum_x \sum_y xy\,p(x,y) = \sum_x \sum_y xy\,p_X(x)\,p_Y(y)
$$

$$
= \left(\sum_x x\,p_X(x)\right)\!\left(\sum_y y\,p_Y(y)\right) = E[X]\,E[Y]
$$

$\blacksquare$

**Proof (continuous case).** By independence, $f(x,y) = f_X(x)\,f_Y(y)$:

$$
E[XY] = \int_{-\infty}^{\infty}\!\int_{-\infty}^{\infty} xy\,f_X(x)\,f_Y(y)\,dx\,dy = \left(\int x\,f_X(x)\,dx\right)\!\left(\int y\,f_Y(y)\,dy\right)
$$

$\blacksquare$

---

## Extension to Multiple Variables

!!! info "Product of n Independent Random Variables"
    If $X_1, X_2, \ldots, X_n$ are mutually independent, then

    $$
    E\!\left[\prod_{i=1}^n X_i\right] = \prod_{i=1}^n E[X_i]
    $$

This follows by induction on $n$.

---

## More General Functions

Independence gives a stronger result: for **any** functions $g$ and $h$,

$$
E[g(X)\,h(Y)] = E[g(X)]\,E[h(Y)]
$$

provided the expectations exist. This is because $g(X)$ and $h(Y)$ are also independent when $X$ and $Y$ are independent.

---

## Failure for Dependent Variables

!!! warning "Independence Is Essential"
    When $X$ and $Y$ are dependent, $E[XY]$ can differ from $E[X]\,E[Y]$ by the covariance:

    $$
    E[XY] = E[X]\,E[Y] + \text{Cov}(X, Y)
    $$

??? example "Dependent Case: E[XY] vs E[X]E[Y]"
    Let $X \sim \text{Bernoulli}(1/2)$ and $Y = X$ (perfectly dependent). Then:

    $$
    E[XY] = E[X^2] = E[X] = \frac{1}{2}
    $$

    $$
    E[X]\,E[Y] = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}
    $$

    The difference is $\text{Cov}(X,Y) = \text{Var}(X) = 1/4$.

---

## Application: Variance of a Product

For independent $X$ and $Y$:

$$
\text{Var}(XY) = E[X^2 Y^2] - (E[XY])^2 = E[X^2]\,E[Y^2] - (E[X])^2(E[Y])^2
$$

This can be rewritten as:

$$
\text{Var}(XY) = \text{Var}(X)\,\text{Var}(Y) + \text{Var}(X)(E[Y])^2 + (E[X])^2\,\text{Var}(Y)
$$

---

## Python Verification

```python
import numpy as np

np.random.seed(42)
N = 1_000_000

# Independent case
X = np.random.exponential(2, N)  # E[X] = 2
Y = np.random.poisson(3, N)     # E[Y] = 3

print("--- Independent X, Y ---")
print(f"E[XY] = {np.mean(X * Y):.4f}")
print(f"E[X]*E[Y] = {np.mean(X) * np.mean(Y):.4f}")  # ≈ 6

# Dependent case: Y = X
Y_dep = X
print("\n--- Dependent: Y = X ---")
print(f"E[XY] = E[X^2] = {np.mean(X * Y_dep):.4f}")
print(f"E[X]*E[Y] = {np.mean(X) * np.mean(Y_dep):.4f}")
print(f"Cov(X,Y) = {np.cov(X, Y_dep)[0,1]:.4f}")
```
=======
>>>>>>> Stashed changes
