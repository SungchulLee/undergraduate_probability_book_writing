# Partition Problems

Many counting problems reduce to distributing $n$ objects into $k$ boxes. The answer depends on whether objects and boxes are distinguishable or indistinguishable, making this a unifying framework for combinatorics.

## Definition

A **distribution problem** assigns $n$ objects to $k$ boxes. The four fundamental cases are:

| Objects | Boxes | Constraint | Formula |
|:---:|:---:|:---:|:---:|
| Distinguishable | Distinguishable | None | $k^n$ |
| Distinguishable | Distinguishable | At most 1 per box ($n \le k$) | $k!/(k-n)!$ |
| Indistinguishable | Distinguishable | None | $\binom{n+k-1}{k-1}$ |
| Indistinguishable | Distinguishable | At least 1 per box | $\binom{n-1}{k-1}$ |
| Distinguishable | Indistinguishable | Exactly $k$ non-empty groups | $S(n,k)$ |
| Indistinguishable | Indistinguishable | At most $k$ parts | $p_k(n)$ |

Here $S(n,k)$ is the **Stirling number of the second kind** and $p_k(n)$ is the number of **integer partitions** of $n$ into at most $k$ parts. This classification is part of the **twelvefold way**.

## Explanation

### Case 1: Distinguishable Objects, Distinguishable Boxes

Each of $n$ objects independently goes into one of $k$ boxes. By the multiplication rule: $k^n$.

### Case 2: Indistinguishable Objects, Distinguishable Boxes (Stars and Bars)

Since objects are identical, only the count per box matters. This is the **stars and bars** problem (see Section 1.3):

$$
\binom{n + k - 1}{k - 1}
$$

With the constraint that each box gets at least 1: first give 1 to each box, then distribute the remaining $n - k$ freely:

$$
\binom{n - 1}{k - 1}
$$

### Case 3: Distinguishable Objects, Indistinguishable Boxes (Stirling Numbers)

The number of ways to partition $n$ distinct objects into exactly $k$ non-empty groups is

$$
S(n, k) = \frac{1}{k!}\sum_{j=0}^{k}(-1)^{k-j}\binom{k}{j}j^n
$$

with recurrence $S(n,k) = k \cdot S(n-1,k) + S(n-1,k-1)$ and boundary conditions $S(n,1) = S(n,n) = 1$.

The **Bell number** $B_n = \sum_{k=0}^{n} S(n,k)$ counts all partitions of an $n$-element set (any number of groups). The first values: $B_0 = 1,\; B_1 = 1,\; B_2 = 2,\; B_3 = 5,\; B_4 = 15,\; B_5 = 52$.

### Case 4: Indistinguishable Objects, Indistinguishable Boxes (Integer Partitions)

The number of ways to write $n$ as a sum of at most $k$ positive integers (order irrelevant) is $p_k(n)$. No simple closed form exists; the standard approach uses a recurrence:

$$
p_k(n) = p_k(n - k) + p_{k-1}(n)
$$

with $p_0(0) = 1$ and $p_k(n) = 0$ for $n < 0$ or $k = 0, n > 0$.

## Examples

**Example 1 (Dist-Dist).** Assign 3 students to 4 study groups: $4^3 = 64$ ways.

**Example 2 (Stars and Bars).** Distribute 10 identical cookies to 4 children: $\binom{13}{3} = 286$. With at least 1 each: give 1 to each child first, then distribute the remaining 6: $\binom{9}{3} = 84$.

**Example 3 (Stirling).** Partition $\{a, b, c\}$ into exactly 2 non-empty groups:

$$
\{a\}\{b,c\},\quad \{b\}\{a,c\},\quad \{c\}\{a,b\} \implies S(3,2) = 3
$$

**Example 4 (Integer Partitions).** Partitions of 5 into at most 3 parts:

$$
5,\quad 4+1,\quad 3+2,\quad 3+1+1,\quad 2+2+1 \implies p_3(5) = 5
$$

```python
import numpy as np
import matplotlib.pyplot as plt
from math import comb
from functools import lru_cache

@lru_cache(maxsize=None)
def stirling2(n, k):
    if k == 0:
        return 1 if n == 0 else 0
    if k == 1 or k == n:
        return 1
    if k > n:
        return 0
    return k * stirling2(n - 1, k) + stirling2(n - 1, k - 1)

def bell(n):
    return sum(stirling2(n, k) for k in range(n + 1))

@lru_cache(maxsize=None)
def partitions(n, max_part=None):
    if max_part is None:
        max_part = n
    if n == 0:
        return 1
    if n < 0 or max_part == 0:
        return 0
    return partitions(n - max_part, max_part) + partitions(n, max_part - 1)

# Verify examples
assert 4**3 == 64
assert comb(13, 3) == 286
assert comb(9, 3) == 84
assert stirling2(3, 2) == 3
assert partitions(5, 3) == 5
print("All examples verified.")

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Panel 1: Stirling triangle
N = 8
triangle = np.zeros((N + 1, N + 1))
for n in range(N + 1):
    for k in range(N + 1):
        triangle[n, k] = stirling2(n, k)

im = axes[0].imshow(triangle[1:, 1:], cmap='YlOrRd', aspect='auto')
for i in range(N):
    for j in range(N):
        val = int(triangle[i + 1, j + 1])
        if val > 0:
            axes[0].text(j, i, str(val), ha='center', va='center', fontsize=7)
axes[0].set_title('Stirling Numbers S(n,k)')
axes[0].set_xlabel('k')
axes[0].set_ylabel('n')
axes[0].set_xticks(range(N))
axes[0].set_xticklabels(range(1, N + 1))
axes[0].set_yticks(range(N))
axes[0].set_yticklabels(range(1, N + 1))

# Panel 2: Bell numbers
ns = range(0, 13)
bells = [bell(n) for n in ns]
axes[1].bar(list(ns), bells, color='steelblue', alpha=0.7)
axes[1].set_title('Bell Numbers $B_n$')
axes[1].set_xlabel('n')
axes[1].set_ylabel('$B_n$')
axes[1].set_yscale('log')
axes[1].grid(True, alpha=0.3)

# Panel 3: Comparison of distribution formulas
n_objects = 6
ks = range(1, 7)
dist_dist = [k**n_objects for k in ks]
stars_bars = [comb(n_objects + k - 1, k - 1) for k in ks]
stirling_vals = [sum(stirling2(n_objects, j) for j in range(1, k + 1)) for k in ks]
part_vals = [partitions(n_objects, k) for k in ks]

axes[2].plot(list(ks), dist_dist, 'ro-', label='Dist-Dist: $k^n$', lw=2)
axes[2].plot(list(ks), stars_bars, 'bs-', label='Indist-Dist: Stars&Bars', lw=2)
axes[2].plot(list(ks), stirling_vals, 'g^-', label='Dist-Indist: Stirling', lw=2)
axes[2].plot(list(ks), part_vals, 'mD-', label='Indist-Indist: Partitions', lw=2)
axes[2].set_title(f'Distribution Problems (n={n_objects} objects)')
axes[2].set_xlabel('k (number of boxes)')
axes[2].set_ylabel('Count')
axes[2].set_yscale('log')
axes[2].legend(fontsize=8)
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('partitions.png', dpi=150, bbox_inches='tight')
plt.show()
```
