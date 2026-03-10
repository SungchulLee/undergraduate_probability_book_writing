# Addition Rule

The addition rule is the first principle for counting outcomes that fall into distinct, non-overlapping categories. It is the natural counterpart of the multiplication rule: where multiplication handles sequential stages, addition handles disjoint alternatives.

## Definition

If a finite set $\Omega$ can be partitioned into pairwise disjoint subsets $A_1, A_2, \ldots, A_m$,

$$
\Omega = A_1 \cup A_2 \cup \cdots \cup A_m, \qquad A_i \cap A_j = \emptyset \text{ for } i \neq j
$$

then the total count is

$$
|\Omega| = \sum_{i=1}^{m} |A_i|
$$

The condition $A_i \cap A_j = \emptyset$ (disjointness) is essential. If categories overlap, elements are double-counted and the formula fails — that situation requires inclusion–exclusion instead.

## Explanation

### The Divide-and-Conquer Strategy

The addition rule yields a systematic three-step approach to counting:

1. **Partition** all outcomes into disjoint categories $A_1, \ldots, A_m$.
2. **Count** each category $|A_i|$ separately.
3. **Sum** to obtain $|\Omega| = \sum_i |A_i|$.

The power of this strategy is that each category can be simpler than the whole. When a problem resists direct enumeration, a well-chosen partition often decomposes it into tractable pieces.

### Counting by Complement

A particularly useful special case partitions $\Omega$ into a set and its complement, $\{A, A^c\}$:

$$
|A| = |\Omega| - |A^c|
$$

Complement counting is the right tool whenever the "bad" outcomes are easier to enumerate than the "good" ones. Many combinatorial problems become one-liners once you switch to counting the complement.

## Examples

**Example 1 (Integers divisible by 2 or 3).** Count the integers from 1 to 100 that are divisible by 2 or 3.

Partition the target set into three disjoint categories:

| Category | Description | Count |
|:---|:---|:---|
| $A_1$ | Divisible by 2 but not 3 | $50 - 16 = 34$ |
| $A_2$ | Divisible by 3 but not 2 | $33 - 16 = 17$ |
| $A_3$ | Divisible by both (i.e., by 6) | $\lfloor 100/6 \rfloor = 16$ |

By the addition rule: $|A_1| + |A_2| + |A_3| = 34 + 17 + 16 = 67$.

(Equivalently, by inclusion–exclusion: $50 + 33 - 16 = 67$.)

---

**Example 2 (Complement counting).** Count the integers from 1 to 100 that are **not** divisible by 5.

There are $\lfloor 100/5 \rfloor = 20$ multiples of 5, so the complement count gives $100 - 20 = 80$.

---

**Example 3 (Three-digit even numbers).** How many three-digit even numbers have no repeated digits?

Partition by the last digit $d \in \{0, 2, 4, 6, 8\}$:

- **Case $d = 0$:** The first digit has 9 choices ($1$–$9$), the second has 8 remaining. Count: $9 \times 8 = 72$.
- **Case $d \neq 0$:** The first digit has 8 choices ($1$–$9$ excluding $d$), the second has 8 remaining (0–9 excluding the first and last). Count: $4 \times 8 \times 8 = 256$.

Total: $72 + 256 = 328$.

```python
from itertools import permutations

# Verify Example 3 by brute force
count = sum(
    1
    for p in permutations(range(10), 3)
    if p[0] != 0 and p[2] % 2 == 0
)
print(f"Three-digit even numbers with no repeated digits: {count}")
# Output: Three-digit even numbers with no repeated digits: 328
```
