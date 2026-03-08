# Sum of Independent Binomials

## Statement

If $X \sim \text{B}(n, p)$ and $Y \sim \text{B}(m, p)$ are **independent**, then:

$$X + Y \sim \text{B}(n + m, p)$$

!!! warning "Independence Required"
    Without independence, the result does **not** hold in general. $X \sim \text{B}(n, p)$ and $Y \sim \text{B}(m, p)$ does **not** imply $X + Y \sim \text{B}(n+m, p)$ unless $X$ and $Y$ are independent.

## Proof by Story

Flip a $p$-coin $n$ times and count the number $X$ of heads. Then flip the same coin $m$ additional times and count the number $Y$ of heads in these additional flips. Since the two sets of flips are independent, $X$ and $Y$ are independent. The total $X + Y$ is simply the number of heads in $n + m$ flips, so $X + Y \sim \text{B}(n + m, p)$.

## Proof by Divide and Conquer

**Divide:** Using the law of total probability:

$$P(X + Y = k) = \sum_{\substack{0 \le l \le n \\ 0 \le k-l \le m}} P(X = l, Y = k - l)$$

**Conquer:** By independence:

$$P(X = l, Y = k - l) = P(X = l) \cdot P(Y = k - l) = \binom{n}{l} p^l q^{n-l} \cdot \binom{m}{k-l} p^{k-l} q^{m-(k-l)}$$

Summing and applying **Vandermonde's identity**:

$$P(X + Y = k) = \left[\sum_l \binom{n}{l} \binom{m}{k-l}\right] p^k q^{n+m-k} = \binom{n+m}{k} p^k q^{n+m-k}$$

This confirms $X + Y \sim \text{B}(n+m, p)$.

## Example: Number of Couples with Same Birthday

There are $n$ people in a class. Each chooses a birthday independently and uniformly over 365 days. For each pair $(i, j)$, let $A_{ij}$ be the event that $i$ and $j$ share a birthday, and let $\mathbf{1}_{A_{ij}}$ be its indicator. The number of common-birthday pairs is:

$$X = \sum_{1 \le i < j \le n} \mathbf{1}_{A_{ij}}$$

Each indicator $\mathbf{1}_{A_{ij}} \sim \text{Bern}(1/365)$, but **$X$ is not binomial** because the indicators are **not independent**. For example:

$$P(A_{23} \mid A_{12}, A_{13}) = 1 \ne \frac{1}{365} = P(A_{23})$$

If persons 1 and 2 share a birthday, and persons 1 and 3 share a birthday, then persons 2 and 3 must share a birthday. This dependence invalidates the binomial model.
