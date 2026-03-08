# Addition Rule

## Overview

The **addition rule** (also called the **rule of sum** or **divide and conquer**) states that if we can partition the outcomes of an experiment into disjoint (mutually exclusive) categories, then the total count is the sum of the counts in each category.

## Statement

If the sample space $\Omega$ can be divided into disjoint categories $A_1, A_2, \ldots, A_m$ such that:

$$\Omega = A_1 \cup A_2 \cup \cdots \cup A_m, \qquad A_i \cap A_j = \emptyset \text{ for } i \neq j$$

then:

$$|\Omega| = \sum_{i=1}^{m} |A_i|$$

## The Divide and Conquer Strategy

The addition rule naturally leads to a systematic counting strategy:

**[Step 1]** Divide all the cases into several disjoint categories $A_i$.

**[Step 2]** Count all the cases in each category $A_i$.

**[Step 3]** $|\Omega| = \sum_i |A_i|$.

This "divide and conquer" approach is one of the most powerful techniques in combinatorics. When a problem seems intractable as a whole, partitioning it into manageable pieces often reveals the answer.

## Counting by Complement

A special case of the addition rule uses the partition $\{A, A^c\}$:

$$|\Omega| = |A| + |A^c|$$

Rearranging:

$$|A| = |\Omega| - |A^c|$$

This is the **complement counting** technique. It is especially useful when counting elements **not** in a set is easier than counting elements in the set directly.

## Enumeration

The most basic counting method is **enumeration**: list all the cases in $\Omega$ and count them. While simple in principle, enumeration is often impractical for large sets. The addition rule, multiplication rule, and other techniques provide more efficient alternatives.

## Summary of Counting Methods

The following hierarchy of counting methods will be developed throughout this chapter:

| Method | Description |
|:---|:---|
| **Enumeration** | List all cases in $\Omega$ and count them |
| **Divide and conquer** | Partition into disjoint categories, count each, sum |
| **Tree diagram** | Use tree structure to partition and apply multiplication rule |
| **Many-to-one** | Establish a $k$-to-1 mapping to simplify counting |
| **Inclusion-exclusion** | Handle overlapping (non-disjoint) categories |
| **Complement** | Count $|A| = |\Omega| - |A^c|$ |

## Python Implementation

```python
def count_by_addition_rule(category_counts):
    """
    Apply the addition rule (sum of disjoint categories).
    
    Parameters
    ----------
    category_counts : list of int
        Count of elements in each disjoint category.
    
    Returns
    -------
    int
        Total count.
    """
    return sum(category_counts)

def count_by_complement(total, complement_count):
    """
    Count by complement: |A| = |Omega| - |A^c|.
    
    Parameters
    ----------
    total : int
        Size of the universal set |Omega|.
    complement_count : int
        Size of the complement |A^c|.
    
    Returns
    -------
    int
        Size of set A.
    """
    return total - complement_count

# Example: Count integers from 1 to 100 divisible by 2 or 3
# Category A: divisible by 2 but not 3 → 50 - 16 = 34
# Category B: divisible by 3 but not 2 → 33 - 16 = 17
# Category C: divisible by both 2 and 3 (i.e., by 6) → 16
total_div_2_or_3 = count_by_addition_rule([34, 17, 16])
print(f"Integers from 1 to 100 divisible by 2 or 3: {total_div_2_or_3}")
# Output: Integers from 1 to 100 divisible by 2 or 3: 67

# Example: Count integers from 1 to 100 NOT divisible by 5
not_div_5 = count_by_complement(100, 20)  # 20 multiples of 5
print(f"Integers from 1 to 100 not divisible by 5: {not_div_5}")
# Output: Integers from 1 to 100 not divisible by 5: 80
```

## Key Takeaway

The addition rule is the complement to the multiplication rule. Where the multiplication rule handles sequential stages, the addition rule handles disjoint alternatives. Together, they form the foundation of all counting arguments.
