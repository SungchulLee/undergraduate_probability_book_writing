# Number of Events in an Interval

## The Fundamental Property

The defining property of a Poisson process with rate $\lambda$ is that the number of events in any interval of length $t$ follows a Poisson distribution.

!!! info "Events in an Interval"
    If $\{N(t)\}$ is a Poisson process with rate $\lambda$, then for any $s \geq 0$ and $t > 0$:

    $$
    N(s, s+t) \sim \text{Po}(\lambda t)
    $$

    with PMF

    $$
    P(N(s, s+t) = k) = \frac{e^{-\lambda t}(\lambda t)^k}{k!}, \quad k = 0, 1, 2, \ldots
    $$

Note that the distribution depends only on the **length** $t$ of the interval, not on the starting time $s$. This is the stationarity property at work.

---

## Derivation from the Infinitesimal Conditions

Starting from the infinitesimal characterization, let $P_k(t) = P(N(t) = k)$. Consider what happens in the interval $(t, t+h]$:

**Case $k = 0$:** No events in $[0, t+h]$ requires no events in $[0, t]$ and none in $(t, t+h]$:

$$
P_0(t+h) = P_0(t)\bigl[1 - \lambda h + o(h)\bigr]
$$

Rearranging: $\frac{P_0(t+h) - P_0(t)}{h} = -\lambda P_0(t) + o(1)$. Taking $h \to 0$:

$$
P_0'(t) = -\lambda P_0(t), \quad P_0(0) = 1
$$

The solution is $P_0(t) = e^{-\lambda t}$.

**Case $k \geq 1$:** Exactly $k$ events in $[0, t+h]$ can happen as $k$ events in $[0, t]$ and none in $(t, t+h]$, or $k-1$ events in $[0, t]$ and one in $(t, t+h]$:

$$
P_k(t+h) = P_k(t)(1 - \lambda h) + P_{k-1}(t) \cdot \lambda h + o(h)
$$

Taking $h \to 0$:

$$
P_k'(t) = -\lambda P_k(t) + \lambda P_{k-1}(t), \quad P_k(0) = 0
$$

Solving recursively (e.g., using the integrating factor $e^{\lambda t}$) yields:

$$
P_k(t) = \frac{e^{-\lambda t}(\lambda t)^k}{k!}
$$

This confirms $N(t) \sim \text{Po}(\lambda t)$.

---

## Mean and Variance

Since $N(s, s+t) \sim \text{Po}(\lambda t)$:

$$
E[N(s, s+t)] = \lambda t, \qquad \text{Var}(N(s, s+t)) = \lambda t
$$

The expected count is proportional to the interval length, and the variance equals the mean — the hallmark of the Poisson distribution.

---

## Worked Examples

??? example "Phone Calls in One Hour"
    A switchboard receives calls at a rate of $\lambda = 5$ calls per hour.

    **How many calls are expected in 1 hour?**

    $E[N(1)] = 5 \times 1 = 5$ calls.

    **What is the probability of receiving exactly 3 calls?**

    $$
    P(N(1) = 3) = \frac{e^{-5} \cdot 5^3}{3!} = \frac{e^{-5} \cdot 125}{6} \approx 0.1404
    $$

    **What is the probability of receiving 8 or more calls?**

    $$
    P(N(1) \geq 8) = 1 - \sum_{k=0}^{7} \frac{e^{-5} \cdot 5^k}{k!} \approx 1 - 0.8666 = 0.1334
    $$

??? example "Events in a 30-Minute Window"
    With the same rate $\lambda = 5$ calls per hour, the number of calls in a 30-minute window is $N(0.5) \sim \text{Po}(5 \times 0.5) = \text{Po}(2.5)$.

    The probability of no calls in 30 minutes is:

    $$
    P(N(0.5) = 0) = e^{-2.5} \approx 0.0821
    $$

---

## Counts in Multiple Disjoint Intervals

By independent increments, the counts in non-overlapping intervals are independent Poisson random variables. For disjoint intervals $(a_1, b_1], (a_2, b_2], \ldots, (a_m, b_m]$:

$$
N(a_i, b_i) \sim \text{Po}(\lambda(b_i - a_i)) \quad \text{independently for } i = 1, 2, \ldots, m
$$

This makes it straightforward to compute joint probabilities by multiplying the individual Poisson PMFs.

??? example "Two Disjoint Intervals"
    With $\lambda = 5$ per hour, find $P(N(0,1) = 3 \text{ and } N(2,4) = 7)$.

    By independence: $N(0,1) \sim \text{Po}(5)$ and $N(2,4) \sim \text{Po}(10)$ are independent, so

    $$
    P(N(0,1) = 3,\; N(2,4) = 7) = \frac{e^{-5} \cdot 5^3}{3!} \cdot \frac{e^{-10} \cdot 10^7}{7!} \approx 0.1404 \times 0.0901 \approx 0.0126
    $$
