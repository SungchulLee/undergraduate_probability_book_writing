# Indicator Random Variables: Definition and Properties


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Definition

For an event $A$, the **indicator random variable** $\mathbf{1}_A$ (also written $I_A$) is defined as

$$
\mathbf{1}_A = \begin{cases} 1 & \text{if } A \text{ occurs} \\ 0 & \text{if } A \text{ does not occur} \end{cases}
$$

An indicator random variable is a $\text{Bernoulli}(p)$ random variable where $p = P(A)$.

---

## Basic Properties

### Expectation

$$
E[\mathbf{1}_A] = 1 \cdot P(A) + 0 \cdot P(A^c) = P(A)
$$

!!! note "Fundamental Bridge"
    $E[\mathbf{1}_A] = P(A)$. This connects probability to expectation and is the basis for computing means via indicators.

### Variance

$$
\text{Var}(\mathbf{1}_A) = P(A)(1 - P(A)) = pq
$$

where $q = 1 - p$.

### Higher Moments

Since $\mathbf{1}_A$ takes values 0 and 1 only:

$$
(\mathbf{1}_A)^k = \mathbf{1}_A \quad \text{for all } k \geq 1
$$

Therefore $E[(\mathbf{1}_A)^k] = P(A)$ for all $k \geq 1$.

---

## Algebraic Properties

Indicators inherit set operations from events:

| Set Operation | Indicator Expression |
|:---:|:---:|
| $A^c$ (complement) | $1 - \mathbf{1}_A$ |
| $A \cap B$ (intersection) | $\mathbf{1}_A \cdot \mathbf{1}_B$ |
| $A \cup B$ (union) | $\mathbf{1}_A + \mathbf{1}_B - \mathbf{1}_A \cdot \mathbf{1}_B$ |
| $A \subseteq B$ | $\mathbf{1}_A \leq \mathbf{1}_B$ |
| $A$ and $B$ disjoint | $\mathbf{1}_{A \cup B} = \mathbf{1}_A + \mathbf{1}_B$ |

### Independence

$A$ and $B$ are independent if and only if $\mathbf{1}_A$ and $\mathbf{1}_B$ are independent, which means:

$$
E[\mathbf{1}_A \cdot \mathbf{1}_B] = E[\mathbf{1}_A] \cdot E[\mathbf{1}_B]
$$

equivalently $P(A \cap B) = P(A) P(B)$.

---

## Covariance of Indicators

For any two events $A$ and $B$:

$$
\text{Cov}(\mathbf{1}_A, \mathbf{1}_B) = P(A \cap B) - P(A)P(B)
$$

If $A$ and $B$ are independent, then $\text{Cov}(\mathbf{1}_A, \mathbf{1}_B) = 0$.

---

## Python Implementation

```python
import numpy as np

np.random.seed(42)
N = 1_000_000

# Indicator for event: die roll >= 5
rolls = np.random.randint(1, 7, N)
indicator = (rolls >= 5).astype(int)

p = 2/6  # P(roll >= 5)
print(f"Theoretical E[1_A] = {p:.4f}")
print(f"Simulated E[1_A] = {np.mean(indicator):.4f}")
print(f"Theoretical Var(1_A) = {p*(1-p):.4f}")
print(f"Simulated Var(1_A) = {np.var(indicator):.4f}")

# Algebraic properties
A = (rolls >= 4).astype(int)  # P(A) = 3/6
B = (rolls % 2 == 0).astype(int)  # P(B) = 3/6 (even: 2,4,6)

# Intersection: A ∩ B = {4, 6}
AB_product = A * B
AB_indicator = ((rolls >= 4) & (rolls % 2 == 0)).astype(int)
print(f"\nIntersection via product: {np.mean(AB_product):.4f}")
print(f"Intersection via indicator: {np.mean(AB_indicator):.4f}")
print(f"Theoretical P(A∩B) = {2/6:.4f}")

# Union: A ∪ B = {2, 4, 5, 6}
AB_union = A + B - A * B
print(f"Union via formula: {np.mean(AB_union):.4f}")
print(f"Theoretical P(A∪B) = {4/6:.4f}")
```
