# Circular Permutations

## Overview

A **circular permutation** arranges objects around a circle, where rotations of the same arrangement are considered identical. This is another application of the many-to-one principle.

## Derivation

To arrange $n$ distinct objects in a circle:

**Step 1:** Arrange all $n$ objects in a line. There are $n!$ such arrangements.

**Step 2:** Recognize that for each circular arrangement, there are exactly $n$ linear arrangements that correspond to it (obtained by rotating the circle — choosing which element appears "first" in the line).

**Step 3:** This is an $n$-to-1 mapping. By the many-to-one principle:

$$\text{Number of circular permutations} = \frac{n!}{n} = (n-1)!$$

## Formula

The number of ways to arrange $n$ distinct objects in a circle is:

$$(n-1)!$$

## Intuitive Explanation

In a circular arrangement, there is no distinguished "first position." We can fix one object's position (breaking the rotational symmetry) and arrange the remaining $n-1$ objects in $(n-1)!$ ways.

## Python Implementation

```python
from math import factorial

def circular_permutations(n):
    """
    Number of ways to arrange n distinct objects in a circle.
    
    Parameters
    ----------
    n : int
        Number of distinct objects.
    
    Returns
    -------
    int
        Number of circular permutations.
    """
    return factorial(n - 1)

# Example: Seat 5 people around a circular table
n = 5
print(f"Circular permutations of {n} people: {circular_permutations(n)}")
# Output: Circular permutations of 5 people: 24

# Compare with linear permutations
print(f"Linear permutations: {factorial(n)}")
print(f"Ratio (should be {n}): {factorial(n) // circular_permutations(n)}")
```

## Key Takeaway

Circular permutations illustrate the many-to-one principle: each circular arrangement corresponds to $n$ linear arrangements (one for each rotation), so we divide $n!$ by $n$ to get $(n-1)!$.
