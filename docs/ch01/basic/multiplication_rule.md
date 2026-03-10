# Multiplication Rule


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Overview

The **multiplication rule** (also called the **counting principle** or **rule of product**) is the most fundamental tool in combinatorics. It states that if a procedure can be broken into sequential stages, and the number of choices at each stage is independent of the choices made at previous stages, then the total number of outcomes is the product of the choices at each stage.

## Statement

If an experiment consists of two sequential stages where:

- Stage 1 has $m$ possible outcomes
- Stage 2 has $n$ possible outcomes (regardless of Stage 1's outcome)

then the total number of outcomes for the combined experiment is:

$$m \times n$$

More generally, if an experiment consists of $k$ sequential stages with $n_1, n_2, \ldots, n_k$ possible outcomes respectively, the total number of outcomes is:

$$n_1 \times n_2 \times \cdots \times n_k$$

## Tree Diagram Interpretation

The multiplication rule is most naturally understood through **tree diagrams**. Each stage of the experiment corresponds to a level of branching in the tree. The total number of paths from the root to the leaves gives the total count.

### Example — Number of Paths from A to C

Consider counting the number of paths from $A$ to $C$, where travel passes through an intermediate point $B$.

$$A \longrightarrow B \longrightarrow C$$

**Branching of paths from $A$ to $B$:** Suppose there are 2 paths, labeled $1$ and $2$.

**Branching of paths from $B$ to $C$:** Suppose there are 3 paths, labeled $a$, $b$, and $c$.

Using a tree diagram, we enumerate all paths from $A$ to $C$:

| Path from $A$ to $B$ | Path from $B$ to $C$ | Combined path $A$ to $C$ |
|:---:|:---:|:---:|
| 1 | $a$ | $1a$ |
| 1 | $b$ | $1b$ |
| 1 | $c$ | $1c$ |
| 2 | $a$ | $2a$ |
| 2 | $b$ | $2b$ |
| 2 | $c$ | $2c$ |

By the multiplication rule:

$$\text{Number of paths from } A \text{ to } C = 2 \times 3 = 6$$

## Choosing Officers — A Classic Application

Suppose there are $n$ people and we wish to choose a **president**, **vice-president**, and **secretary** (all distinct).

- **Choose president:** $n$ choices (number of branching $= n$)
- **Choose vice-president:** $n - 1$ choices (number of branching $= n - 1$)
- **Choose secretary:** $n - 2$ choices (number of branching $= n - 2$)

By the multiplication rule (via tree diagram):

$$\text{Number of ways to choose president, vice-president, secretary} = n \times (n-1) \times (n-2)$$

This is a **permutation** — an ordered selection — and it forms the basis for the general permutation formula discussed in later sections.

## Python Implementation

```python
import itertools
from math import prod

def count_by_multiplication_rule(stage_counts):
    """
    Apply the multiplication rule.
    
    Parameters
    ----------
    stage_counts : list of int
        Number of choices at each stage.
    
    Returns
    -------
    int
        Total number of outcomes.
    """
    return prod(stage_counts)

# Example: Paths from A to C
paths_A_to_B = 2
paths_B_to_C = 3
total = count_by_multiplication_rule([paths_A_to_B, paths_B_to_C])
print(f"Number of paths from A to C: {total}")
# Output: Number of paths from A to C: 6

# Example: Choosing president, VP, secretary from 10 people
n = 10
officers = count_by_multiplication_rule([n, n-1, n-2])
print(f"Number of ways to choose 3 officers from {n} people: {officers}")
# Output: Number of ways to choose 3 officers from 10 people: 720

# Verification via enumeration
people = list(range(1, n+1))
ordered_triples = list(itertools.permutations(people, 3))
print(f"Verification by enumeration: {len(ordered_triples)}")
# Output: Verification by enumeration: 720
```

## Key Takeaway

The multiplication rule transforms a complex counting problem into a sequence of simpler counting problems. The tree diagram provides both a visual proof and a systematic enumeration method: the number of leaves equals the product of the branching factors at each level.
