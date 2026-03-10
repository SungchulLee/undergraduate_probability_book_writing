# Permutations of Distinct Objects


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Overview

A **permutation** is an ordered arrangement of objects. When all objects are distinct, counting permutations reduces to a direct application of the multiplication rule.

## Definition

The number of ways to arrange $k$ objects chosen from $n$ distinct objects, where **order matters**, is denoted $P(n, k)$ or $nPk$:

$$P(n, k) = n \times (n-1) \times (n-2) \times \cdots \times (n - k + 1) = \frac{n!}{(n-k)!}$$

### Special Case: Arranging All n Objects

When $k = n$, we arrange all objects:

$$P(n, n) = n!$$

## Derivation via Tree Diagram

Consider choosing $k$ people from $n$ to fill ordered positions (e.g., president, vice-president, ..., secretary):

- **Position 1 (president):** $n$ choices
- **Position 2 (vice-president):** $n - 1$ choices
- **Position 3:** $n - 2$ choices
- $\vdots$
- **Position $k$ (secretary):** $n - (k-1)$ choices

By the multiplication rule (via tree diagram):

$$P(n, k) = n \times (n-1) \times (n-2) \times \cdots \times (n - k + 1)$$

## From Permutation to Combination

The key insight connecting permutations and combinations is the **many-to-one** principle. When we choose $k$ people for a committee (without distinct roles), every committee of $k$ people corresponds to $k!$ different ordered arrangements (permutations of those same $k$ people).

This is a $k!$-to-1 mapping from ordered selections to unordered selections:

$$\binom{n}{k} = \frac{P(n,k)}{k!} = \frac{n!}{k!(n-k)!}$$

## Python Implementation

```python
from math import factorial, perm

def permutation(n, k):
    """
    Compute P(n, k) = n! / (n-k)!
    
    Parameters
    ----------
    n : int
        Total number of objects.
    k : int
        Number of objects to arrange.
    
    Returns
    -------
    int
        Number of permutations.
    """
    return factorial(n) // factorial(n - k)

# Example: Choose president, VP, secretary from 10 people
n = 10
k = 3
print(f"P({n}, {k}) = {permutation(n, k)}")
print(f"Verification (math.perm): {perm(n, k)}")
# Output: P(10, 3) = 720

# Example: Arrange all 5 distinct books on a shelf
n = 5
print(f"P({n}, {n}) = {n}! = {factorial(n)}")
# Output: P(5, 5) = 5! = 120

# Enumeration verification
import itertools
books = ['A', 'B', 'C', 'D', 'E']
arrangements = list(itertools.permutations(books))
print(f"Verification by enumeration: {len(arrangements)}")
# Output: Verification by enumeration: 120
```

## Key Takeaway

Permutations count ordered selections. The formula $P(n,k) = n!/(n-k)!$ follows directly from the multiplication rule applied to sequential choices. The connection to combinations comes through the many-to-one principle: dividing by $k!$ removes the ordering.
