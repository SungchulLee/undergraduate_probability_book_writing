# Law of Total Probability

The law of total probability computes $P(A)$ by dividing the problem into simpler conditional pieces over a partition of the sample space. It is the probabilistic version of "divide and conquer."

## Definition

If $B_1, B_2, \ldots, B_n$ partition $\Omega$ (pairwise disjoint, union = $\Omega$), then for any event $A$:

$$
P(A) = \sum_{k=1}^{n} P(B_k)\,P(A \mid B_k)
$$

Combined with Bayes' theorem:

$$
P(B_j \mid A) = \frac{P(B_j)\,P(A \mid B_j)}{\sum_{k=1}^{n} P(B_k)\,P(A \mid B_k)}
$$

## Explanation

The law decomposes $A = \bigcup_k (A \cap B_k)$ into disjoint pieces, then applies the chain rule to each piece: $P(A \cap B_k) = P(B_k)\,P(A \mid B_k)$. Summing over $k$ gives $P(A)$.

The key is choosing the right partition. A good partition makes the conditional probabilities $P(A \mid B_k)$ easy to compute.

## Examples

**Example (Monty Hall).** Three doors: one car, two goats. You pick door 1, the host opens door 3 (a goat). Should you switch?

Let $C$ = "initially chose car", $G$ = "initially chose goat", $W$ = "win under switch strategy."

$$
P(W) = P(C)\,P(W \mid C) + P(G)\,P(W \mid G) = \frac{1}{3} \cdot 0 + \frac{2}{3} \cdot 1 = \frac{2}{3}
$$

Switching wins with probability $2/3$, staying wins with probability $1/3$.

```python
import numpy as np

# Monty Hall simulation
np.random.seed(42)
n_sim = 100_000
wins_switch = 0
wins_stay = 0

for _ in range(n_sim):
    car = np.random.randint(3)
    choice = np.random.randint(3)
    if choice == car:
        wins_stay += 1
    else:
        wins_switch += 1

print(f"P(win | stay)   = {wins_stay/n_sim:.4f}")
print(f"P(win | switch) = {wins_switch/n_sim:.4f}")
```
