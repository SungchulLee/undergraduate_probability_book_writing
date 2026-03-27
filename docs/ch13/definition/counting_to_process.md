# From Counting to the Poisson Process

## Counting Rare Events in Continuous Time

In Chapter 12, we saw that the Poisson distribution arises naturally when we count the number of successes in a large number of independent Bernoulli trials, each with a small success probability. The **Poisson process** extends this idea from a fixed number of trials to events occurring continuously in time.

Consider events that happen "randomly" along the time axis — phone calls arriving at a call center, radioactive atoms decaying, or customers entering a store. We want a mathematical model that captures the essential features of such processes.

---

## The Subdivision Argument

Fix a time interval $[0, t]$ and suppose events occur at an average rate of $\lambda$ per unit time. To build a model, we subdivide $[0, t]$ into $n$ tiny subintervals, each of length $\Delta = t/n$.

**Key assumptions for each subinterval:**

1. The probability of exactly one event in a subinterval is approximately $\lambda \Delta = \lambda t / n$
2. The probability of two or more events in a single subinterval is negligible
3. Events in different subintervals occur independently

Under these assumptions, the number of events in $[0, t]$ is approximately

$$
N(t) \approx \sum_{i=1}^{n} X_i
$$

where $X_1, X_2, \ldots, X_n$ are independent Bernoulli random variables with success probability $p = \lambda t / n$. Therefore $N(t) \approx B(n, \lambda t / n)$.

---

## Taking the Limit

As $n \to \infty$, the subintervals become infinitesimally small, and the approximation becomes exact. By the **Poisson limit theorem** (Chapter 12), with $n$ trials each having probability $p_n = \lambda t / n$ and $np_n = \lambda t$ fixed:

$$
P(N(t) = k) = \lim_{n \to \infty} \binom{n}{k} \left(\frac{\lambda t}{n}\right)^k \left(1 - \frac{\lambda t}{n}\right)^{n-k} = \frac{e^{-\lambda t} (\lambda t)^k}{k!}
$$

!!! info "From Binomial to Poisson"
    As the number of subintervals $n \to \infty$:

    $$
    B\!\left(n, \frac{\lambda t}{n}\right) \xrightarrow{d} \text{Po}(\lambda t)
    $$

    The count of events in a time interval of length $t$ follows a Poisson distribution with parameter $\lambda t$.

---

## What Makes This a "Process"

The argument above tells us the distribution of $N(t)$ for a single interval. A **Poisson process** goes further by specifying how counts in *different* intervals relate to each other.

The three properties inherited from the subdivision argument are:

1. **Independent increments** — events in non-overlapping intervals are independent (because the Bernoulli trials in different subintervals were independent)
2. **Stationary increments** — the distribution of the number of events in an interval depends only on the length of the interval, not on where it starts (because we used the same rate $\lambda$ everywhere)
3. **No simultaneous events** — the probability of two or more events in an infinitesimal interval is negligible

These properties, formalized in the next section, define the Poisson process precisely.

---

## A Concrete Example

??? example "Phone Calls at a Help Desk"
    A help desk receives calls at an average rate of $\lambda = 3$ calls per hour. What is the probability of receiving exactly 5 calls in a 2-hour period?

    The number of calls in 2 hours is $N(2) \sim \text{Po}(3 \times 2) = \text{Po}(6)$:

    $$
    P(N(2) = 5) = \frac{e^{-6} \cdot 6^5}{5!} = \frac{e^{-6} \cdot 7776}{120} \approx 0.1606
    $$

---

## Summary

| Discrete Model | Continuous Model |
|:---|:---|
| $n$ independent Bernoulli trials | Events in continuous time $[0, t]$ |
| Success probability $p = \lambda t / n$ | Rate $\lambda$ per unit time |
| Count $\sim B(n, \lambda t/n)$ | Count $\sim \text{Po}(\lambda t)$ as $n \to \infty$ |
| Fixed number of trials | Infinitely many infinitesimal "trials" |

The Poisson process is the natural continuous-time extension of Bernoulli counting. The Poisson limit theorem provides the mathematical bridge between these two frameworks.
