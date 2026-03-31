# Uniform Distribution of Arrivals (Given N(t) = n)
<<<<<<< Updated upstream

## The Main Result

One of the most remarkable properties of the Poisson process is that, given the total count in an interval, the arrival times are uniformly distributed.

!!! info "Conditional Uniformity"
    Let $\{N(t)\}$ be a Poisson process with rate $\lambda$. Given that $N(t) = n$, the $n$ arrival times $S_1, S_2, \ldots, S_n$ have the same joint distribution as the **order statistics** of $n$ independent $\text{Uniform}(0, t)$ random variables.

In other words, if we know that exactly $n$ events occurred in $[0, t]$, then those events are scattered uniformly and independently across the interval (up to ordering).

---

## Proof via Subdivision

Divide $[0, t]$ into $m$ equal subintervals, each of length $t/m$. Given $N(t) = n$, what is the probability that specific subintervals $i_1, i_2, \ldots, i_n$ each contain exactly one event?

By independent increments, the count in each subinterval is $\text{Po}(\lambda t/m)$, independently. The conditional probability that the $n$ events fall in $n$ specified subintervals (one each) is:

$$
P\bigl(\text{one event in each of subintervals } i_1, \ldots, i_n \mid N(t) = n\bigr)
$$

Using the multinomial structure of independent Poisson counts conditional on their sum (which gives a multinomial distribution with equal probabilities):

$$
= \frac{n!}{m^n} \cdot \frac{1}{n!} = \frac{1}{m^n}
$$

This is exactly the probability that $n$ independent uniform draws on $\{1, 2, \ldots, m\}$ land in those $n$ subintervals. As $m \to \infty$, this converges to the statement that the arrival times are iid $\text{Uniform}(0, t)$, up to ordering.

---

## Conditional Joint Density

The conditional joint density of the ordered arrival times $S_1 < S_2 < \cdots < S_n$, given $N(t) = n$, is:

$$
f_{S_1, \ldots, S_n \mid N(t) = n}(s_1, \ldots, s_n) = \frac{n!}{t^n}, \quad 0 < s_1 < s_2 < \cdots < s_n < t
$$

This is the joint density of the order statistics of $n$ iid $\text{Uniform}(0, t)$ random variables. Each unordered arrival time has marginal density $1/t$ on $[0, t]$, and the factor $n!$ accounts for the ordering.

---

## Conditional Distribution of a Single Arrival

Given $N(t) = 1$, the single arrival time $S_1$ is uniformly distributed:

$$
S_1 \mid N(t) = 1 \sim \text{Uniform}(0, t)
$$

More generally, given $N(t) = n$, each individual arrival time $S_k$ has a marginal distribution that is the $k$-th order statistic of $n$ iid $\text{Uniform}(0, t)$ random variables (see Chapter 15 on order statistics):

$$
E[S_k \mid N(t) = n] = \frac{k \cdot t}{n+1}
$$

---

## Why This Matters

The conditional uniformity property has both conceptual and practical significance:

- **Conceptual**: It captures the idea of "complete randomness." Given the count, there is no preferred time for events to cluster — they are as random as possible.
- **Simulation**: To simulate a Poisson process on $[0, t]$, one can first draw $n \sim \text{Po}(\lambda t)$ and then generate $n$ iid $\text{Uniform}(0, t)$ values and sort them. This is often more efficient than generating exponential interarrival times sequentially.
- **Inference**: In statistical applications, the uniformity property simplifies likelihood calculations for Poisson process models.

---

## Example

??? example "Bus Arrivals in One Hour"
    Buses arrive at a stop as a Poisson process with rate $\lambda = 6$ per hour. Given that exactly 4 buses arrived between 8:00 and 9:00, what is the expected time of the second bus?

    Given $N(1) = 4$, the four arrival times behave as order statistics of 4 iid $\text{Uniform}(0, 1)$ random variables (measuring time in hours from 8:00).

    The expected value of the $k$-th order statistic out of $n$ is $k/(n+1)$:

    $$
    E[S_2 \mid N(1) = 4] = \frac{2}{5} = 0.4 \text{ hours} = 24 \text{ minutes}
    $$

    So the expected time of the second bus is 8:24.

??? example "Conditional Probability of Early Arrival"
    With $\lambda = 6$ per hour, given $N(1) = 1$ (exactly one bus in the hour), what is the probability it arrived in the first 10 minutes?

    Given $N(1) = 1$, the arrival time is $\text{Uniform}(0, 1)$ (in hours). The probability of arriving in the first 10 minutes ($= 1/6$ hour) is:

    $$
    P\!\left(S_1 < \frac{1}{6} \;\middle|\; N(1) = 1\right) = \frac{1/6}{1} = \frac{1}{6}
    $$

---

## Connection to Splitting

The conditional uniformity theorem is closely related to the splitting property. Asking "given $N(t) = n$, did the $k$-th event fall in a subinterval $A$?" is equivalent to thinning each event with probability $|A|/t$ (the fraction of the interval occupied by $A$). This perspective unifies the conditional and splitting results.
=======
>>>>>>> Stashed changes
