# Computing P(A1 ∪ A2 ∪ ... ∪ An)

## Disjoint Events

When $A_1, A_2, \ldots$ are **mutually disjoint** ($A_i \cap A_j = \emptyset$ for $i \ne j$), the union probability is simply the sum:

$$
P\!\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i) \quad \text{(countable additivity)}
$$

$$
P\!\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i=1}^{n} P(A_i) \quad \text{(finite additivity)}
$$

## Non-Disjoint Events — Inclusion-Exclusion Principle

When the events are **not** disjoint, we must account for overlaps using the **inclusion-exclusion principle**.

### Bonferroni Inequalities (Truncated Forms)

The inclusion-exclusion alternating sum can be truncated at any level to obtain bounds:

**First-order bound (union bound):**

$$
P\!\left(\bigcup_{i=1}^{n} A_i\right) \le \sum_{i=1}^{n} P(A_i)
$$

**Second-order bound:**

$$
P\!\left(\bigcup_{i=1}^{n} A_i\right) \ge \sum_{i=1}^{n} P(A_i) - \sum_{1 \le i < j \le n} P(A_i A_j)
$$

**Third-order bound:**

$$
P\!\left(\bigcup_{i=1}^{n} A_i\right) \le \sum_{i=1}^{n} P(A_i) - \sum_{1 \le i < j \le n} P(A_i A_j) + \sum_{1 \le i < j < k \le n} P(A_i A_j A_k)
$$

The pattern alternates: truncating after an odd number of terms gives an **upper bound**, and truncating after an even number gives a **lower bound**.

### Exact Formula

$$
P\!\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i=1}^{n} P(A_i) - \sum_{1 \le i < j \le n} P(A_i A_j) + \sum_{1 \le i < j < k \le n} P(A_i A_j A_k) - \cdots + (-1)^{n+1} P(A_1 A_2 \cdots A_n)
$$

## Complement Method

An alternative approach uses De Morgan's law:

$$
P\!\left(\bigcup_{i=1}^{n} A_i\right) = 1 - P\!\left(\bigcap_{i=1}^{n} A_i^c\right)
$$

This is particularly useful when the complements $A_i^c$ are **independent**, because then:

$$
P\!\left(\bigcap_{i=1}^{n} A_i^c\right) = \prod_{i=1}^{n} P(A_i^c) = \prod_{i=1}^{n} \bigl(1 - P(A_i)\bigr)
$$

So:

$$
P\!\left(\bigcup_{i=1}^{n} A_i\right) = 1 - \prod_{i=1}^{n} \bigl(1 - P(A_i)\bigr)
$$

## Summary — Which Method to Use

| Scenario | Best Method |
|----------|-------------|
| Disjoint events | Direct sum: $\sum P(A_i)$ |
| Independent events | Complement: $1 - \prod(1 - P(A_i))$ |
| Few events, overlaps known | Inclusion-exclusion |
| Many events, need a bound | Union bound or Bonferroni |
| General dependent events | Inclusion-exclusion (exact) or complement + chain rule |
