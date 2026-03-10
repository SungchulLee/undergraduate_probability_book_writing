# Permutations of Distinct Objects

A permutation is an ordered arrangement. Counting permutations of distinct objects is a direct application of the multiplication rule and the starting point for all of combinatorics.

## Definition

The number of ways to arrange $k$ objects chosen from $n$ distinct objects, where order matters, is

$$
P(n, k) = n(n-1)(n-2)\cdots(n-k+1) = \frac{n!}{(n-k)!}
$$

When $k = n$ (all objects arranged): $P(n,n) = n!$

## Explanation

### Derivation via Sequential Choice

Fill $k$ ordered positions one at a time:

- Position 1: $n$ choices
- Position 2: $n-1$ choices (one object already used)
- Position $k$: $n-k+1$ choices

By the multiplication rule: $P(n,k) = n(n-1)\cdots(n-k+1)$.

### From Permutations to Combinations

Every unordered set of $k$ objects appears as $k!$ different ordered arrangements (one for each internal permutation). This is a $k!$-to-1 mapping from permutations to combinations:

$$
\binom{n}{k} = \frac{P(n,k)}{k!} = \frac{n!}{k!\,(n-k)!}
$$

## Examples

**Example 1 (Officers).** Choose a president, VP, and secretary from 10 people: $P(10,3) = 10 \times 9 \times 8 = 720$.

---

**Example 2 (Bookshelf).** Arrange 5 distinct books on a shelf: $5! = 120$.

---

**Example 3 (Seating).** Seat 8 people in a row of 8 chairs: $8! = 40{,}320$. In a row of 5 chairs: $P(8,5) = 8 \times 7 \times 6 \times 5 \times 4 = 6{,}720$.

```python
from math import perm, factorial
from itertools import permutations

# Example 1
print(f"P(10, 3) = {perm(10, 3)}")
# Output: P(10, 3) = 720

# Example 2: verify by enumeration
books = list("ABCDE")
assert len(list(permutations(books))) == factorial(5) == 120
print(f"5! = {factorial(5)}")

# Example 3
print(f"P(8, 5) = {perm(8, 5)}")
# Output: P(8, 5) = 6720
```
