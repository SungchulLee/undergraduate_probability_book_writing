# Combinations with Repetition (Stars and Bars)

## Overview

**Combinations with repetition** count the number of ways to choose $k$ items from $n$ types when repetition is allowed and order does not matter. The classic technique for solving these problems is the **stars and bars** method.

## Problem Statement

How many ways can we choose $k$ items from $n$ types, where each type can be chosen multiple times?

Equivalently: how many non-negative integer solutions are there to:

$$x_1 + x_2 + \cdots + x_n = k, \qquad x_i \geq 0$$

## Stars and Bars Formula

Represent the $k$ items as $k$ stars ($\star$) and separate the $n$ types using $n - 1$ bars ($|$). Any arrangement of $k$ stars and $n - 1$ bars gives a valid selection.

The total number of symbols is $k + n - 1$, and we choose positions for the $n - 1$ bars (or equivalently, for the $k$ stars):

$$\binom{k + n - 1}{n - 1} = \binom{k + n - 1}{k}$$

## Example

Choose 3 items from 4 types ($n = 4$, $k = 3$):

$$\binom{3 + 4 - 1}{4 - 1} = \binom{6}{3} = 20$$

One arrangement: $\star \star \, | \, \star \, | \, | \,$ means 2 of type 1, 1 of type 2, 0 of type 3, 0 of type 4.

## Python Implementation

```python
from math import comb

def combinations_with_repetition(n, k):
    """
    Number of ways to choose k items from n types with repetition.
    
    Parameters
    ----------
    n : int
        Number of types.
    k : int
        Number of items to choose.
    
    Returns
    -------
    int
        Number of multisets of size k from n types.
    """
    return comb(k + n - 1, n - 1)

# Example: Choose 3 items from 4 types
n, k = 4, 3
print(f"Combinations with repetition: C({k+n-1}, {n-1}) = {combinations_with_repetition(n, k)}")
# Output: 20

# Verification by enumeration
count = 0
solutions = []
for x1 in range(k + 1):
    for x2 in range(k - x1 + 1):
        for x3 in range(k - x1 - x2 + 1):
            x4 = k - x1 - x2 - x3
            solutions.append((x1, x2, x3, x4))
            count += 1
print(f"Verification by enumeration: {count}")
```

## Key Takeaway

The stars and bars technique transforms a selection-with-repetition problem into a problem of placing dividers among identical objects, reducing it to a standard combination $\binom{k+n-1}{n-1}$.
