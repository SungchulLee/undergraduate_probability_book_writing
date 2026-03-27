# Independent Increments

## Definition

The **independent increments** property is one of the three defining axioms of the Poisson process. It states that the numbers of events in non-overlapping time intervals are independent random variables.

!!! info "Independent Increments"
    A counting process $\{N(t)\}$ has **independent increments** if, for any choice of times $0 \leq t_1 < t_2 < \cdots < t_n$, the random variables

    $$
    N(t_1),\; N(t_1, t_2),\; N(t_2, t_3),\; \ldots,\; N(t_{n-1}, t_n)
    $$

    are mutually independent.

In particular, for any two non-overlapping intervals $(a, b]$ and $(c, d]$ with $b \leq c$:

$$
P(N(a,b) = j,\; N(c,d) = k) = P(N(a,b) = j) \cdot P(N(c,d) = k)
$$

---

## Intuition: No Memory Between Intervals

Independent increments mean that the process has **no memory across disjoint intervals**. Knowing that 10 calls arrived between 9:00 and 10:00 gives no information about how many will arrive between 10:00 and 11:00.

This reflects a deep property of the underlying random mechanism: events at different times are generated independently. In the subdivision argument, this came from the independence of the Bernoulli trials in different subintervals.

---

## Consequences

**Joint distributions factor.** For a Poisson process with rate $\lambda$ and disjoint intervals $(a_1, b_1], \ldots, (a_m, b_m]$:

$$
P\bigl(N(a_1, b_1) = k_1, \ldots, N(a_m, b_m) = k_m\bigr) = \prod_{i=1}^{m} \frac{e^{-\lambda(b_i - a_i)} [\lambda(b_i - a_i)]^{k_i}}{k_i!}
$$

**Covariance is zero for disjoint intervals.** If $(a, b]$ and $(c, d]$ do not overlap, then

$$
\text{Cov}(N(a,b),\; N(c,d)) = 0
$$

**Covariance for overlapping intervals.** For $s < t$:

$$
\text{Cov}(N(s), N(t)) = \text{Var}(N(s)) = \lambda s
$$

since $N(t) = N(s) + N(s, t)$ and $N(s)$ is independent of $N(s, t)$.

---

## What Independent Increments Excludes

Not all counting processes have independent increments. Consider these contrasting examples:

- **Clustering**: If one earthquake makes aftershocks more likely, the counts in adjacent intervals are positively correlated. This violates independent increments.
- **Inhibition**: If a cell that just fired enters a refractory period (unable to fire again for some time), nearby intervals have negatively correlated counts.
- **Scheduling**: Buses that run on a fixed schedule have highly dependent counts in adjacent intervals.

The Poisson process models **completely random** event occurrences, with no clustering, inhibition, or regularity beyond what chance alone produces.

---

## Independent Increments vs Independence of N(s) and N(t)

!!! warning "A Common Confusion"
    Independent increments does **not** mean that $N(s)$ and $N(t)$ are independent for $s < t$. In fact, they are positively correlated:

    $$
    \text{Cov}(N(s), N(t)) = \lambda \min(s, t) > 0
    $$

    The reason is that $N(t) = N(s) + N(s,t)$, so $N(t)$ includes all events counted by $N(s)$. Independence applies to the **increments** $N(s)$ and $N(s,t)$, not to the cumulative counts $N(s)$ and $N(t)$.

??? example "Example: Morning and Afternoon Calls"
    A call center has Poisson arrivals with rate $\lambda = 4$ per hour. Let $A = N(0, 3)$ be the morning count (9am--noon) and $B = N(3, 6)$ be the afternoon count (noon--3pm).

    By independent increments, $A$ and $B$ are independent with $A \sim \text{Po}(12)$ and $B \sim \text{Po}(12)$.

    The probability of a quiet morning and busy afternoon:

    $$
    P(A \leq 8,\; B \geq 16) = P(A \leq 8) \cdot P(B \geq 16)
    $$

    Each factor can be computed from the Poisson CDF.
