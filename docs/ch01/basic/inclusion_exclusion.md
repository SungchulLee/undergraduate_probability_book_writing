# Inclusion-Exclusion Principle

The addition rule requires disjoint categories. When categories overlap, the inclusion-exclusion principle provides the correct count by systematically compensating for overcounting.

## Definition

For $n$ finite sets $A_1, A_2, \ldots, A_n$:

$$
\left|\bigcup_{i=1}^{n} A_i\right| = \sum_{k=1}^{n} (-1)^{k+1} \sum_{1 \le i_1 < \cdots < i_k \le n} |A_{i_1} \cap \cdots \cap A_{i_k}|
$$

In words: add single-set sizes, subtract pairwise intersections, add triple intersections, and continue alternating signs through all $n$-fold intersections.

**Special cases.** For two sets:

$$
|A \cup B| = |A| + |B| - |A \cap B|
$$

For three sets:

$$
|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |B \cap C| - |C \cap A| + |A \cap B \cap C|
$$

## Explanation

### Why the Signs Alternate

Consider two overlapping sets $A$ and $B$. Simply adding $|A| + |B|$ counts every element of $A \cap B$ twice. Subtracting $|A \cap B|$ corrects this, giving each element exactly one count.

With three sets the situation is more delicate. After adding single sizes and subtracting pairwise intersections, an element in all three sets has been added three times and subtracted three times — it is missing entirely. The final $+|A \cap B \cap C|$ term restores it.

In general, an element belonging to exactly $m$ of the $n$ sets is counted $\binom{m}{1} - \binom{m}{2} + \cdots + (-1)^{m+1}\binom{m}{m}$ times, which equals exactly 1 by the binomial theorem.

### Bonferroni Inequalities

When computing all $2^n - 1$ intersection terms is impractical, the partial sums of the inclusion-exclusion formula give alternating bounds:

- Truncating after terms of **odd** order (singles, triples, ...) gives an **upper bound**.
- Truncating after terms of **even** order (pairs, quadruples, ...) gives a **lower bound**.

These are the **Bonferroni inequalities**, widely used in probability for bounding $P(A_1 \cup \cdots \cup A_n)$.

### Combining with Complement Counting

To count elements in **none** of $A_1, \ldots, A_n$, combine inclusion-exclusion with the complement:

$$
|\Omega \setminus (A_1 \cup \cdots \cup A_n)| = |\Omega| - \left|\bigcup_{i=1}^{n} A_i\right|
$$

This technique drives the derangement formula (covered later in this chapter).

## Examples

**Example 1 (Divisibility).** How many integers from 1 to 1000 are divisible by 2, 3, or 5?

Let $A_2, A_3, A_5$ be the sets of multiples of 2, 3, 5 respectively in $\{1, \ldots, 1000\}$.

| Term | Value |
|:---|:---|
| $\|A_2\| = \lfloor 1000/2 \rfloor$ | 500 |
| $\|A_3\| = \lfloor 1000/3 \rfloor$ | 333 |
| $\|A_5\| = \lfloor 1000/5 \rfloor$ | 200 |
| $\|A_2 \cap A_3\| = \lfloor 1000/6 \rfloor$ | 166 |
| $\|A_2 \cap A_5\| = \lfloor 1000/10 \rfloor$ | 100 |
| $\|A_3 \cap A_5\| = \lfloor 1000/15 \rfloor$ | 66 |
| $\|A_2 \cap A_3 \cap A_5\| = \lfloor 1000/30 \rfloor$ | 33 |

$$
|A_2 \cup A_3 \cup A_5| = (500 + 333 + 200) - (166 + 100 + 66) + 33 = 734
$$

---

**Example 2 (Euler's totient).** Count the integers from 1 to 30 that are coprime to 30.

Since $30 = 2 \cdot 3 \cdot 5$, an integer is *not* coprime to 30 if and only if it is divisible by 2, 3, or 5. By Example 1's method (with $\Omega = \{1, \ldots, 30\}$):

$$
|A_2 \cup A_3 \cup A_5| = (15 + 10 + 6) - (5 + 3 + 2) + 1 = 22
$$

So $\varphi(30) = 30 - 22 = 8$. The eight coprime values are $\{1, 7, 11, 13, 17, 19, 23, 29\}$.

```python
from itertools import combinations
from math import gcd

def inclusion_exclusion(sets):
    """Compute |A1 ∪ ... ∪ An| via inclusion-exclusion."""
    n = len(sets)
    total = 0
    for k in range(1, n + 1):
        sign = (-1) ** (k + 1)
        for combo in combinations(range(n), k):
            intersection = sets[combo[0]]
            for idx in combo[1:]:
                intersection = intersection & sets[idx]
            total += sign * len(intersection)
    return total

# Verify Example 1
omega = set(range(1, 1001))
A2 = {x for x in omega if x % 2 == 0}
A3 = {x for x in omega if x % 3 == 0}
A5 = {x for x in omega if x % 5 == 0}
print(f"|A2 ∪ A3 ∪ A5| = {inclusion_exclusion([A2, A3, A5])}")
# Output: |A2 ∪ A3 ∪ A5| = 734

# Verify Example 2
coprime_30 = [x for x in range(1, 31) if gcd(x, 30) == 1]
print(f"φ(30) = {len(coprime_30)}, values: {coprime_30}")
# Output: φ(30) = 8, values: [1, 7, 11, 13, 17, 19, 23, 29]
```
