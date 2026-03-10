# Combinations and Binomial Coefficients

A combination is an unordered selection. The binomial coefficient counts how many ways to choose $k$ objects from $n$ distinct objects when order does not matter.

## Definition

The **binomial coefficient** "$n$ choose $k$" is

$$
\binom{n}{k} = \frac{n!}{k!\,(n-k)!}
$$

for integers $0 \le k \le n$, and $\binom{n}{k} = 0$ when $k < 0$ or $k > n$.

## Explanation

### Derivation via the Many-to-One Principle

**Step 1: Count ordered selections.** Choose $k$ people from $n$ for $k$ distinct positions. By the multiplication rule:

$$
P(n,k) = n(n-1)(n-2)\cdots(n-k+1) = \frac{n!}{(n-k)!}
$$

**Step 2: Remove the ordering.** Each unordered set of $k$ people appears as $k!$ different ordered selections. This is a $k!$-to-1 mapping, so

$$
\binom{n}{k} = \frac{P(n,k)}{k!} = \frac{n!}{k!\,(n-k)!}
$$

### Identities via Double Counting

Counting the same quantity two ways yields identities:

**Symmetry.** Choosing $k$ members for a committee is the same as choosing $n-k$ people to exclude:

$$
\binom{n}{k} = \binom{n}{n-k}
$$

**Absorption.** Choose a committee of $k$, then elect 1 president: $k\binom{n}{k}$. Or, elect 1 president from $n$, then choose $k-1$ remaining members: $n\binom{n-1}{k-1}$.

$$
k\binom{n}{k} = n\binom{n-1}{k-1}
$$

## Examples

**Example 1.** Choose a 3-person committee from 10 people: $\binom{10}{3} = \frac{10!}{3!\,7!} = 120$.

---

**Example 2 (Poker hands).** A 5-card hand from a standard 52-card deck: $\binom{52}{5} = 2{,}598{,}960$.

How many hands contain exactly 2 aces? Choose 2 aces from 4: $\binom{4}{2} = 6$. Choose 3 non-aces from 48: $\binom{48}{3} = 17{,}296$. By the multiplication rule: $6 \times 17{,}296 = 103{,}776$.

---

**Example 3 (Verification).** Enumerate all 3-element subsets of $\{1,\ldots,10\}$ and verify.

```python
from math import comb
from itertools import combinations

# Example 1
print(f"C(10, 3) = {comb(10, 3)}")
# Output: C(10, 3) = 120

# Verify by enumeration
committees = list(combinations(range(1, 11), 3))
print(f"Enumeration: {len(committees)}")
# Output: Enumeration: 120

# Example 2: Poker hands with exactly 2 aces
hands_2_aces = comb(4, 2) * comb(48, 3)
print(f"Hands with exactly 2 aces: {hands_2_aces}")
# Output: Hands with exactly 2 aces: 103776

# Verify identities
n, k = 10, 3
assert comb(n, k) == comb(n, n - k), "Symmetry failed"
assert k * comb(n, k) == n * comb(n - 1, k - 1), "Absorption failed"
print("Symmetry and absorption identities verified.")
```
