# Combinations and Binomial Coefficients


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Overview

A **combination** is an unordered selection of objects. The number of ways to choose $k$ objects from $n$ distinct objects (without regard to order) is given by the **binomial coefficient**.

## Definition

The binomial coefficient "$n$ choose $k$" is:

$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$

## Derivation via Many-to-One

The derivation proceeds in two steps, connecting permutations to combinations:

**Step 1: Count ordered selections (permutations).**

Choose $k$ people from $n$ to fill $k$ distinct positions. By the multiplication rule:

$$P(n,k) = n \times (n-1) \times (n-2) \times \cdots \times (n-k+1)$$

**Step 2: Remove the ordering (many-to-one).**

Each unordered committee of $k$ people can be arranged in $k!$ different orders. This is a $k!$-to-1 mapping from ordered selections to unordered selections.

$$\binom{n}{k} = \frac{P(n,k)}{k!} = \frac{n \times (n-1) \times \cdots \times (n-k+1)}{k!} = \frac{n!}{k!(n-k)!}$$

## Two Different Ways of Counting

Several elegant identities arise from counting the same quantity in two different ways.

### Symmetry Identity

**Method 1:** Choose $k$ people to form a committee: $\binom{n}{k}$

**Method 2:** Choose $n - k$ people to exclude (the rest form the committee): $\binom{n}{n-k}$

Since both count the same thing:

$$\binom{n}{k} = \binom{n}{n-k}$$

### Committee with President

**Method 1:** Choose $k$ members, then elect 1 as president: $k \binom{n}{k}$

**Method 2:** Elect 1 president from $n$ people, then choose remaining $k-1$ members: $n \binom{n-1}{k-1}$

$$k\binom{n}{k} = n\binom{n-1}{k-1}$$

This identity is sometimes called the **absorption identity**.

## Python Implementation

```python
from math import comb, factorial

def binomial_coefficient(n, k):
    """
    Compute C(n, k) = n! / (k! * (n-k)!)
    
    Parameters
    ----------
    n : int
        Total number of objects.
    k : int
        Number of objects to choose.
    
    Returns
    -------
    int
        Number of combinations.
    """
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

# Example: Choose 3 committee members from 10 people
n, k = 10, 3
print(f"C({n}, {k}) = {binomial_coefficient(n, k)}")
print(f"Verification (math.comb): {comb(n, k)}")
# Output: C(10, 3) = 120

# Verify symmetry identity
print(f"\nSymmetry: C({n}, {k}) = {comb(n, k)}, C({n}, {n-k}) = {comb(n, n-k)}")

# Verify absorption identity: k * C(n,k) = n * C(n-1, k-1)
lhs = k * comb(n, k)
rhs = n * comb(n - 1, k - 1)
print(f"Absorption: {k}*C({n},{k}) = {lhs}, {n}*C({n-1},{k-1}) = {rhs}")

# Enumeration verification
from itertools import combinations
people = list(range(1, n + 1))
committees = list(combinations(people, k))
print(f"\nVerification by enumeration: {len(committees)}")
```

## Key Takeaway

The binomial coefficient $\binom{n}{k}$ counts unordered selections. It arises naturally from dividing the permutation count by $k!$ via the many-to-one principle. The "two ways of counting" technique — counting the same quantity via different decompositions — yields powerful combinatorial identities.
