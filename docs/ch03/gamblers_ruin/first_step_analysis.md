# First Step Analysis

First step analysis derives recurrence relations by conditioning on the outcome of the first step. It is the standard technique for solving random walk problems.

## Definition

**First step analysis** decomposes $Q(i) = P(\text{ruin} \mid \text{start at } i)$ by conditioning on the first bet:

$$
Q(i) = p\,Q(i+1) + q\,Q(i-1), \quad 1 \le i \le N-1
$$

with $Q(0) = 1$, $Q(N) = 0$.

## Explanation

### Derivation

By the law of total probability, conditioning on win ($W$) or loss ($W^c$):

$$
Q(i) = P(W)\,P(\text{ruin} \mid W, \text{start at } i) + P(W^c)\,P(\text{ruin} \mid W^c, \text{start at } i)
$$

After a win the gambler has $i+1$; after a loss, $i-1$. By the Markov property (the future depends only on the current state): $P(\text{ruin} \mid W, \text{start at } i) = Q(i+1)$.

### Characteristic Equation

Guess $Q(i) = \lambda^i$. Substituting into the recurrence:

$$
p\lambda^2 - \lambda + q = 0
$$

Roots: $\lambda_1 = 1$ and $\lambda_2 = q/p$.

General solution: $Q(i) = \alpha \cdot 1^i + \beta \cdot (q/p)^i = \alpha + \beta(q/p)^i$ when $p \ne q$. The constants $\alpha, \beta$ are determined by the boundary conditions.

## Examples

**Example (Setting up the system).** For $N = 4$, $p = 0.4$:

$$
Q(1) = 0.4\,Q(2) + 0.6 \cdot 1
$$

$$
Q(2) = 0.4\,Q(3) + 0.6\,Q(1)
$$

$$
Q(3) = 0.4 \cdot 0 + 0.6\,Q(2)
$$

This is a $3 \times 3$ tridiagonal system. Solving: $Q(1) = 0.936$, $Q(2) = 0.839$, $Q(3) = 0.503$.

```python
import numpy as np

# Solve tridiagonal system for N=4, p=0.4
p, q, N = 0.4, 0.6, 4
A = np.zeros((N-1, N-1))
b = np.zeros(N-1)

for i in range(N-1):
    A[i, i] = 1
    if i > 0:
        A[i, i-1] = -q
    if i < N-2:
        A[i, i+1] = -p
b[0] = q  # from Q(0) = 1

Q_int = np.linalg.solve(A, b)
print("Q(i) for i=1,2,3:", [f"{x:.4f}" for x in Q_int])
```
