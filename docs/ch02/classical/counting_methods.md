# Counting Methods in Probability

Under the equally likely model, $P(A) = |A|/|\Omega|$, so computing probabilities reduces to counting. This page applies counting techniques to two classic problems: Newton's solution to the Pepys problem and the ballot theorem.

## Definition

The general strategy for probability via counting:

1. Define $\Omega$ and compute $|\Omega|$
2. Define event $A$ and count $|A|$ (often via complement: $|A| = |\Omega| - |A^c|$)
3. $P(A) = |A|/|\Omega|$

## Explanation

### Newton-Pepys Problem (1693)

Samuel Pepys asked Isaac Newton: which is most likely?

- **A:** At least one 6 in 6 dice
- **B:** At least two 6's in 12 dice
- **C:** At least three 6's in 18 dice

Each scenario has the same expected number of 6's (1, 2, and 3 respectively), so Pepys guessed C. Newton showed A is most likely.

**Computation via complement counting:**

$$
P(A) = 1 - \left(\frac{5}{6}\right)^6 = 0.6651
$$

$$
P(B) = 1 - \sum_{k=0}^{1}\binom{12}{k}\left(\frac{1}{6}\right)^k\left(\frac{5}{6}\right)^{12-k} = 0.6187
$$

$$
P(C) = 1 - \sum_{k=0}^{2}\binom{18}{k}\left(\frac{1}{6}\right)^k\left(\frac{5}{6}\right)^{18-k} = 0.5973
$$

The key insight: as the number of dice increases, so does the **variance**, making it more likely to fall short of the proportional target.

### Ballot Theorem

Candidate A gets $a$ votes, B gets $b$ votes ($a > b$). If counted in random order, the probability A is strictly ahead throughout is

$$
P(\text{A strictly ahead}) = \frac{a - b}{a + b}
$$

**Proof sketch.** Model the count as a lattice path from $(0,0)$ to $(b,a)$ (right = B vote, up = A vote). A is strictly ahead iff the path stays strictly above the diagonal. Paths starting with B immediately fail: $\binom{a+b-1}{b-1}$ such paths. By the reflection principle, paths starting with A that later touch the diagonal are in bijection with paths starting with B, giving another $\binom{a+b-1}{b-1}$ bad paths.

$$
P = 1 - \frac{2\binom{a+b-1}{b-1}}{\binom{a+b}{b}} = 1 - \frac{2b}{a+b} = \frac{a-b}{a+b}
$$

## Examples

**Example 1 (Newton-Pepys verification).**

| Scenario | Dice | Target | $P$ |
|:---:|:---:|:---:|:---:|
| A | 6 | $\ge 1$ six | 0.6651 |
| B | 12 | $\ge 2$ sixes | 0.6187 |
| C | 18 | $\ge 3$ sixes | 0.5973 |

$P(A) > P(B) > P(C)$. Newton was right.

---

**Example 2 (Ballot).** $a = 10, b = 5$: $P = 5/15 = 1/3$.

```python
from math import comb
from scipy.stats import binom
import numpy as np

# Newton-Pepys
P_A = 1 - (5/6)**6
P_B = 1 - binom.cdf(1, 12, 1/6)
P_C = 1 - binom.cdf(2, 18, 1/6)
print(f"P(A) = {P_A:.4f}, P(B) = {P_B:.4f}, P(C) = {P_C:.4f}")
print(f"P(A) > P(B) > P(C): {P_A > P_B > P_C}")

# Ballot theorem simulation
np.random.seed(42)
for a, b in [(10, 5), (7, 3), (15, 8)]:
    theory = (a - b) / (a + b)
    count = 0
    votes = np.array([1]*a + [-1]*b)
    for _ in range(100_000):
        np.random.shuffle(votes)
        if np.all(np.cumsum(votes) > 0):
            count += 1
    print(f"a={a}, b={b}: theory={(a-b)}/{a+b}={theory:.4f}, sim={count/100_000:.4f}")
```
