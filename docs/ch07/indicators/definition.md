# Indicator Random Variables

An indicator random variable converts an event into a number — 1 if the event occurs, 0 otherwise. The fundamental bridge $E[\mathbf{1}_A] = P(A)$ connects expectation to probability.

## Definition

For an event $A$, the **indicator random variable** is

$$
\mathbf{1}_A = \begin{cases} 1 & \text{if } A \text{ occurs} \\ 0 & \text{otherwise} \end{cases}
$$

This is $\text{Bern}(P(A))$, so $E[\mathbf{1}_A] = P(A)$ and $\text{Var}(\mathbf{1}_A) = P(A)(1-P(A))$.

## Explanation

### Fundamental Bridge

$$
E[\mathbf{1}_A] = P(A)
$$

This identity is the basis for computing expectations via indicator decomposition.

### Algebraic Properties

| Set Operation | Indicator |
|:--------------|:----------|
| $A^c$ | $1 - \mathbf{1}_A$ |
| $A \cap B$ | $\mathbf{1}_A \cdot \mathbf{1}_B$ |
| $A \cup B$ | $\mathbf{1}_A + \mathbf{1}_B - \mathbf{1}_A\mathbf{1}_B$ |
| $A \subseteq B$ | $\mathbf{1}_A \le \mathbf{1}_B$ |

### Higher Powers

Since $\mathbf{1}_A \in \{0,1\}$: $(\mathbf{1}_A)^k = \mathbf{1}_A$ for all $k \ge 1$.

### Covariance

$$
\text{Cov}(\mathbf{1}_A, \mathbf{1}_B) = P(A \cap B) - P(A)P(B)
$$

This is zero iff $A$ and $B$ are independent.

## Examples

**Example.** Roll a fair die. Let $A$ = {roll $\ge$ 5}, $B$ = {roll is even}.

$P(A) = 2/6$, $P(B) = 3/6$, $P(A \cap B) = P(\{6\}) = 1/6$.

$\text{Cov}(\mathbf{1}_A, \mathbf{1}_B) = 1/6 - (2/6)(3/6) = 1/6 - 1/6 = 0$. Independent!

```python
import numpy as np

np.random.seed(42)
rolls = np.random.randint(1, 7, 1_000_000)
A = (rolls >= 5).astype(int)
B = (rolls % 2 == 0).astype(int)

print(f"E[1_A] = {A.mean():.4f} (theory: {2/6:.4f})")
print(f"E[1_B] = {B.mean():.4f} (theory: {3/6:.4f})")
print(f"E[1_A * 1_B] = {(A*B).mean():.4f} (theory: {1/6:.4f})")
print(f"Cov = {np.cov(A, B)[0,1]:.6f} (theory: 0)")
```
