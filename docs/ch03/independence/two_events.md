# Independence of Two Events


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Definition

Events $A$ and $B$ are **independent** if

$$
P(AB) = P(A)\,P(B)
$$

Equivalently (when $P(A) > 0$ and $P(B) > 0$):

$$
P(B \mid A) = P(B) \quad \text{and} \quad P(A \mid B) = P(A)
$$

Independence means that knowing $A$ occurred gives no information about whether $B$ occurs, and vice versa.

## Key Properties

**Complements:** If $A$ and $B$ are independent, then so are:

- $A$ and $B^c$
- $A^c$ and $B$
- $A^c$ and $B^c$

**Proof for $A$ and $B^c$:**

$$
P(AB^c) = P(A) - P(AB) = P(A) - P(A)\,P(B) = P(A)\,(1 - P(B)) = P(A)\,P(B^c)
$$

## Independence vs. Disjointness

Independence and disjointness are very different concepts:

- **Disjoint events** ($A \cap B = \emptyset$) **cannot** be independent (unless one has probability 0), because $P(AB) = 0 \ne P(A)\,P(B)$ when both have positive probability.
- **Independent events** with positive probabilities must have nonempty intersection.

Intuitively: if $A$ and $B$ are disjoint, then knowing $A$ occurred tells you $B$ did **not** occur — they are maximally dependent (negatively).

## Computing Intersection and Union Probabilities

### Intersection: P(A1 ∩ A2 ∩ ... ∩ An)

**Independent events:**

$$
P(A_1 A_2 \cdots A_n) = P(A_1)\,P(A_2) \cdots P(A_n)
$$

**Dependent events (chain rule):**

$$
P(A_1 A_2 \cdots A_n) = P(A_1)\,P(A_2 \mid A_1)\,P(A_3 \mid A_1 A_2) \cdots P(A_n \mid A_1 \cdots A_{n-1})
$$

### Union: P(A1 ∪ A2 ∪ ... ∪ An)

**Disjoint events:**

$$
P\!\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i=1}^{n} P(A_i)
$$

**Non-disjoint events (inclusion–exclusion):**

$$
P\!\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i=1}^{n} P(A_i) - \sum_{1 \le i < j \le n} P(A_i A_j) + \cdots + (-1)^{n+1} P(A_1 A_2 \cdots A_n)
$$

**Complement method:**

$$
P\!\left(\bigcup_{i=1}^{n} A_i\right) = 1 - P\!\left(\bigcap_{i=1}^{n} A_i^c\right)
$$

This is often the most efficient approach when the $A_i$ are independent, since then $P\!\left(\bigcap_{i=1}^{n} A_i^c\right) = \prod_{i=1}^{n} P(A_i^c)$.
