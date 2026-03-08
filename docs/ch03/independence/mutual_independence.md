# Mutual Independence

## Definition

Events $A_1, A_2, \ldots, A_n$ are **(mutually) independent** if for **every** subcollection $A_{i_1}, A_{i_2}, \ldots, A_{i_m}$ (with $2 \le m \le n$):

$$
P(A_{i_1} A_{i_2} \cdots A_{i_m}) = P(A_{i_1})\,P(A_{i_2}) \cdots P(A_{i_m})
$$

This requires the product rule to hold for **all** subsets of size 2, 3, ..., up to $n$. For $n$ events, there are $\binom{n}{2} + \binom{n}{3} + \cdots + \binom{n}{n} = 2^n - n - 1$ conditions to verify.

## Pairwise Independence

Events $A_1, A_2, \ldots, A_n$ are **pairwise independent** if for **every pair** $A_i, A_j$ (with $i \ne j$):

$$
P(A_i A_j) = P(A_i)\,P(A_j)
$$

This only requires $\binom{n}{2}$ conditions — the product rule for every pair.

## Mutual Independence Implies Pairwise Independence

Mutual independence implies pairwise independence (take $m = 2$ in the definition). However, the converse is **false**: pairwise independence does **not** imply mutual independence.

## Example — Pairwise Independent but Not Independent

Consider $n$ people in a class, each choosing a birthday independently and uniformly over 365 days. For each pair $i$ and $j$, let $A_{ij}$ be the event that persons $i$ and $j$ share the same birthday.

### A_ij Are Not Independent

Consider persons 1, 2, and 3. If we know $A_{12}$ (persons 1 and 2 share a birthday) and $A_{13}$ (persons 1 and 3 share a birthday), then persons 2 and 3 must also share that same birthday:

$$
P(A_{23} \mid A_{12}, A_{13}) = 1 \ne P(A_{23}) = \frac{1}{365}
$$

Knowing $A_{12}$ and $A_{13}$ gives complete information about $A_{23}$, so these events are not mutually independent.

### A_ij Are Pairwise Independent

For any two events $A_{12}$ and $A_{13}$:

$$
P(A_{13} \mid A_{12}) = \frac{P(A_{12} \cap A_{13})}{P(A_{12})}
$$

The event $A_{12} \cap A_{13}$ means all three of persons 1, 2, 3 share the same birthday. Person 1 picks any day (\$365/365$), person 2 matches (\$1/365$), person 3 matches (\$1/365$):

$$
P(A_{12} \cap A_{13}) = \frac{1}{365^2}
$$

Therefore:

$$
P(A_{13} \mid A_{12}) = \frac{1/365^2}{1/365} = \frac{1}{365} = P(A_{13})
$$

So $A_{12}$ and $A_{13}$ are independent. The same argument applies to any pair $A_{ij}$ and $A_{kl}$ that share exactly one index, and to pairs that share no index at all. Hence the events are pairwise independent.

!!! note "Why the Distinction Matters"
    The gap between pairwise and mutual independence has important consequences. For example, the variance of a sum $\text{Var}(X_1 + \cdots + X_n)$ equals $\sum \text{Var}(X_i)$ under pairwise independence (pairwise uncorrelatedness suffices), but the MGF of a sum factors only under mutual independence. Many probabilistic arguments require the stronger condition.
