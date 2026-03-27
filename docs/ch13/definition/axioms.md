# Definition and Axioms

## The Counting Process

A **counting process** $\{N(t) : t \geq 0\}$ records the total number of events that have occurred by time $t$. It satisfies $N(0) = 0$, takes non-negative integer values, and is non-decreasing: if $s < t$, then $N(s) \leq N(t)$.

We write $N(s, t) = N(t) - N(s)$ for the number of events in the interval $(s, t]$.

---

## Formal Definition

!!! info "Poisson Process"
    A counting process $\{N(t) : t \geq 0\}$ is a **Poisson process with rate** $\lambda > 0$ if:

    1. **Initialization**: $N(0) = 0$
    2. **Independent increments**: For any $0 \leq t_1 < t_2 < \cdots < t_n$, the increments $N(t_1, t_2), N(t_2, t_3), \ldots, N(t_{n-1}, t_n)$ are mutually independent
    3. **Stationary Poisson increments**: For any $s \geq 0$ and $t > 0$, the increment $N(s, s+t)$ follows a Poisson distribution with parameter $\lambda t$:

    $$
    P(N(s, s+t) = k) = \frac{e^{-\lambda t}(\lambda t)^k}{k!}, \quad k = 0, 1, 2, \ldots
    $$

**Axiom 1** says the count starts at zero. **Axiom 2** says that knowing the number of events in one time window tells us nothing about events in a non-overlapping window. **Axiom 3** says that the distribution of the count depends only on the length $t$ of the interval, not on the starting time $s$.

---

## Infinitesimal Characterization

An equivalent way to define the Poisson process uses conditions on tiny time intervals. This formulation is often more intuitive and is the basis for many derivations.

!!! info "Infinitesimal Definition"
    A counting process $\{N(t) : t \geq 0\}$ with $N(0) = 0$ and independent, stationary increments is a Poisson process with rate $\lambda$ if, for an infinitesimal interval of length $h$:

    $$
    P(N(h) = 1) = \lambda h + o(h)
    $$

    $$
    P(N(h) \geq 2) = o(h)
    $$

Here $o(h)$ denotes any function satisfying $o(h)/h \to 0$ as $h \to 0$. In words:

- The probability of exactly one event in a tiny interval is proportional to the interval length
- The probability of two or more events in the same tiny interval is negligible compared to $h$

---

## Equivalence of the Two Definitions

The infinitesimal conditions, combined with independent and stationary increments, imply that $N(s, s+t) \sim \text{Po}(\lambda t)$. To see why, let $P_k(t) = P(N(t) = k)$. The infinitesimal conditions give:

$$
P_0(t + h) = P_0(t)(1 - \lambda h) + o(h)
$$

Rearranging and taking $h \to 0$ yields the differential equation $P_0'(t) = -\lambda P_0(t)$ with $P_0(0) = 1$, so $P_0(t) = e^{-\lambda t}$. Similarly, for $k \geq 1$:

$$
P_k(t + h) = P_k(t)(1 - \lambda h) + P_{k-1}(t) \cdot \lambda h + o(h)
$$

This gives $P_k'(t) = -\lambda P_k(t) + \lambda P_{k-1}(t)$, which can be solved recursively to obtain the Poisson PMF $P_k(t) = e^{-\lambda t}(\lambda t)^k / k!$.

---

## Notation Conventions

Throughout this chapter, we use the following notation:

| Symbol | Meaning |
|:---|:---|
| $N(t)$ | Total number of events in $[0, t]$ |
| $N(s, t)$ | Number of events in $(s, t]$, equal to $N(t) - N(s)$ |
| $\lambda$ | Rate parameter (events per unit time) |
| $S_n$ | Arrival time of the $n$-th event |
| $T_n = S_n - S_{n-1}$ | Interarrival time between events $n-1$ and $n$ |

---

## Connection to the Subdivision Argument

The formal axioms capture precisely the three properties we identified in the subdivision argument from the previous section. Dividing $[0, t]$ into $n$ subintervals with independent Bernoulli trials naturally produces independent increments and stationary increments. The Poisson limit theorem then delivers the Poisson distribution for counts in any interval.

The infinitesimal characterization makes this connection even more transparent: each tiny subinterval of length $h$ is like a single Bernoulli trial with success probability $\lambda h$, and we are performing infinitely many such trials.
