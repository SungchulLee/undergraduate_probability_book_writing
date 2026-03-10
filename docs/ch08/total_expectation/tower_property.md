# Law of Iterated Expectations (Tower Property)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Statement

For any random variables $X$ and $Y$:

$$
E(X) = E\bigl[E(X \mid Y)\bigr]
$$

This is also called the **tower property** or the **law of total expectation**. The outer expectation is taken over the randomness in $Y$.

## Properties of Conditional Expectation

The following properties hold and are essential tools for computing conditional expectations:

**(1) Linearity:** $E(X + Y \mid Z) = E(X \mid Z) + E(Y \mid Z)$

**(2) Scaling:** $E(aX \mid Y) = a \, E(X \mid Y)$

**(3) Known values pull out:** $E(g(Y) \mid Y) = g(Y)$

**(4) Factoring out known:** $E(g(Y) \cdot X \mid Y) = g(Y) \cdot E(X \mid Y)$

**(5) Independence:** $E(X \mid Y) = E(X)$ if $X$ and $Y$ are independent

**(6) Tower property:** $E(X) = E\bigl[E(X \mid Y)\bigr]$

Properties (3) and (4) capture the idea that when conditioning on $Y$, any function of $Y$ behaves like a constant and can be pulled out of the expectation.

## Proof of the Tower Property (Discrete Case)

$$
\begin{aligned}
E\bigl[E(X \mid Y)\bigr] &= \sum_{y_j} E(X \mid Y = y_j) \, P(Y = y_j) \\[6pt]
&= \sum_{y_j} \left( \sum_{x_i} x_i \, P(X = x_i \mid Y = y_j) \right) P(Y = y_j) \\[6pt]
&= \sum_{x_i} x_i \left( \sum_{y_j} P(X = x_i \mid Y = y_j) \, P(Y = y_j) \right) \\[6pt]
&= \sum_{x_i} x_i \, P(X = x_i) \\[6pt]
&= E(X)
\end{aligned}
$$

The key step uses the law of total probability: $\sum_{y_j} P(X = x_i \mid Y = y_j) \, P(Y = y_j) = P(X = x_i)$.

## Intuition

The tower property says: to compute the overall average of $X$, you can first compute the average of $X$ within each group defined by $Y$, and then take a weighted average of these group averages (weighted by the probability of each group). This is the same idea behind stratified sampling or group-by-then-aggregate operations.

## Example: Symmetry Argument

Let $X$ and $Y$ be iid $\text{Binomial}(n, p)$. Compute $E(X \mid X + Y = m)$.

**Known information:** Since $X + Y = m$ is given, $E(X + Y \mid X + Y = m) = m$.

**By linearity:** $E(X + Y \mid X + Y = m) = E(X \mid X + Y = m) + E(Y \mid X + Y = m)$.

**By symmetry:** Since $X$ and $Y$ are iid, they play identical roles in determining $X + Y$. Therefore $E(X \mid X + Y = m) = E(Y \mid X + Y = m)$.

**Combining:** $2 \, E(X \mid X + Y = m) = m$, so:

$$
E(X \mid X + Y = m) = \frac{m}{2}
$$

## Python Simulation

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000
n, p = 10, 0.3

X = np.random.binomial(n, p, n_sim)
Y = np.random.binomial(n, p, n_sim)
S = X + Y

# Verify E(X | X+Y = m) = m/2
for m in [3, 5, 8, 10]:
    mask = (S == m)
    if mask.sum() > 0:
        cond_mean = X[mask].mean()
        print(f"E(X | X+Y={m}) = {cond_mean:.3f}  (theory: {m/2:.1f})")

# Verify tower property: E[E(X|Y)] = E(X)
print(f"\nE(X) = {X.mean():.4f}  (theory: {n*p})")
```
