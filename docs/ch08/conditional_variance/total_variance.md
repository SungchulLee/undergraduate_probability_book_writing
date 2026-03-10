# Law of Total Variance (Eve's Law)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Statement

For any random variables $X$ and $Y$:

$$
\text{Var}(X) = E\bigl[\text{Var}(X \mid Y)\bigr] + \text{Var}\bigl(E(X \mid Y)\bigr)
$$

This is known as **Eve's law** (a mnemonic: **E**xpected **V**ariance + **V**ariance of **E**xpectation, or EVVE).

## Interpretation

The total variance of $X$ decomposes into two components:

**$E\bigl[\text{Var}(X \mid Y)\bigr]$** — the **average within-group variance** (also called *unexplained variance*). This is the average residual uncertainty that remains after conditioning on $Y$. It measures the spread within each group defined by $Y$, averaged across groups.

**$\text{Var}\bigl(E(X \mid Y)\bigr)$** — the **between-group variance** (also called *explained variance*). This measures how much the group means vary from group to group. It captures the variation in $X$ that is "explained" by knowing $Y$.

## Consequence

Since both components are non-negative (variance is always $\geq 0$ and expectation of a non-negative quantity is $\geq 0$):

$$
\text{Var}(X) \geq E\bigl[\text{Var}(X \mid Y)\bigr] \qquad \text{and} \qquad \text{Var}(X) \geq \text{Var}\bigl(E(X \mid Y)\bigr)
$$

In other words, **conditioning can only reduce average variance**: the average conditional variance is at most the unconditional variance.

## Proof

Starting from $\text{Var}(X) = E(X^2) - (EX)^2$ and applying the tower property to both terms:

$$
E(X^2) = E\bigl[E(X^2 \mid Y)\bigr]
$$

Write $E(X^2 \mid Y) = \text{Var}(X \mid Y) + \bigl(E(X \mid Y)\bigr)^2$ (conditional shortcut formula), so:

$$
E(X^2) = E\bigl[\text{Var}(X \mid Y)\bigr] + E\bigl[(E(X \mid Y))^2\bigr]
$$

Also, $(EX)^2 = \bigl(E[E(X \mid Y)]\bigr)^2$ by the tower property. Therefore:

$$
\begin{aligned}
\text{Var}(X) &= E\bigl[\text{Var}(X \mid Y)\bigr] + E\bigl[(E(X \mid Y))^2\bigr] - \bigl(E[E(X \mid Y)]\bigr)^2 \\
&= E\bigl[\text{Var}(X \mid Y)\bigr] + \text{Var}\bigl(E(X \mid Y)\bigr)
\end{aligned}
$$

## Worked Examples

### Department Store

With $T = \sum_{i=1}^{N} X_i$, $E(T \mid N) = 8N$, and $\text{Var}(T \mid N) = 16N$:

| Component | Computation | Value |
|:----------|:-----------|------:|
| $\text{Var}\bigl(E(T \mid N)\bigr)$ | $\text{Var}(8N) = 64 \cdot 100$ | 6400 |
| $E\bigl[\text{Var}(T \mid N)\bigr]$ | $E(16N) = 16 \cdot 50$ | 800 |
| $\text{Var}(T)$ | $6400 + 800$ | 7200 |

The between-group variance (6400) dominates: most of the variability in daily spending comes from variability in the *number* of customers, not from variability in *individual* spending.

### Trapped Miner

The recursive application of Eve's law:

$$
\text{Var}(T) = 72.67 + \tfrac{2}{3}\,\text{Var}(T) \implies \text{Var}(T) = 218
$$

### Waiting for HH

$$
\text{Var}(W_{HH}) = 9 + 2 + \tfrac{1}{2}\,\text{Var}(W_{HH}) \implies \text{Var}(W_{HH}) = 22
$$

## Python Verification

```python
import numpy as np

np.random.seed(42)
n_sim = 500_000

# Verify Eve's law with Exponential example
# X | Y=y ~ Exp(1/y), Y ~ Exp(1)
Y = np.random.exponential(1, n_sim)
X = np.array([np.random.exponential(y) for y in Y])

# E(X|Y) = Y,  Var(X|Y) = Y^2
E_X_given_Y = Y
Var_X_given_Y = Y**2

# Eve's law components
var_of_expectation = np.var(E_X_given_Y)
expected_variance = np.mean(Var_X_given_Y)
total_var = np.var(X)

print("=== Eve's Law Verification (Exponential Example) ===")
print(f"Var(X)                    = {total_var:.3f}")
print(f"Var(E(X|Y))               = {var_of_expectation:.3f}")
print(f"E(Var(X|Y))               = {expected_variance:.3f}")
print(f"Var(E(X|Y)) + E(Var(X|Y)) = {var_of_expectation + expected_variance:.3f}")
print(f"Match: {np.isclose(total_var, var_of_expectation + expected_variance, atol=0.1)}")
```
