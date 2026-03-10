# Computing P(A1 ∩ A2 ∩ ... ∩ An)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Independent Events

When $A_1, A_2, \ldots, A_n$ are independent, the intersection probability factors into a product:

$$
P(A_1 A_2 \cdots A_n) = P(A_1)\,P(A_2)\,P(A_3) \cdots P(A_n)
$$

Written out for small cases:

$$
P(AB) = P(A)\,P(B)
$$

$$
P(ABC) = P(A)\,P(B)\,P(C)
$$

$$
P(ABCD) = P(A)\,P(B)\,P(C)\,P(D)
$$

## Dependent Events — Chain Rule

When the events are **not** independent, we use the **chain rule** (multiplication rule):

$$
P(AB) = P(A)\,P(B \mid A)
$$

$$
P(ABC) = P(A)\,P(B \mid A)\,P(C \mid AB)
$$

$$
P(ABCD) = P(A)\,P(B \mid A)\,P(C \mid AB)\,P(D \mid ABC)
$$

In general:

$$
P(A_1 A_2 \cdots A_n) = P(A_1)\,P(A_2 \mid A_1)\,P(A_3 \mid A_1 A_2) \cdots P(A_n \mid A_1 A_2 \cdots A_{n-1})
$$

Each factor conditions on **all** preceding events.

## When to Use Which

| Scenario | Method | Formula |
|----------|--------|---------|
| Events are independent | Product rule | $\prod_{i=1}^{n} P(A_i)$ |
| Events are dependent | Chain rule | $P(A_1) \prod_{k=2}^{n} P(A_k \mid A_1 \cdots A_{k-1})$ |
| Joint probability table available | Direct lookup | Read $P(A_i \cap B_j)$ from table |

!!! note "Connection"
    The chain rule is always valid (for both dependent and independent events). For independent events, $P(A_k \mid A_1 \cdots A_{k-1}) = P(A_k)$, so the chain rule simplifies to the product rule.
