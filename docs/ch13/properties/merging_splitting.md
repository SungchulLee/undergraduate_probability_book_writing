# Merging and Splitting of Poisson Processes

## Merging (Superposition)

When two independent Poisson processes are combined, the result is again a Poisson process.

!!! info "Merging Theorem"
    Let $\{N_1(t)\}$ and $\{N_2(t)\}$ be independent Poisson processes with rates $\lambda_1$ and $\lambda_2$. Then the **merged process** $\{N(t)\} = \{N_1(t) + N_2(t)\}$ is a Poisson process with rate $\lambda_1 + \lambda_2$.

**Proof.** We verify the three axioms for $N(t) = N_1(t) + N_2(t)$:

1. $N(0) = N_1(0) + N_2(0) = 0$

2. **Independent increments**: For disjoint intervals, $N_1$ and $N_2$ each have independent increments, and the two processes are independent of each other. Therefore the increments of the sum are also independent.

3. **Poisson distribution**: For any interval of length $t$, the increment $N(s, s+t) = N_1(s, s+t) + N_2(s, s+t)$ is the sum of independent Poisson random variables:

$$
N_1(s, s+t) \sim \text{Po}(\lambda_1 t), \quad N_2(s, s+t) \sim \text{Po}(\lambda_2 t)
$$

By the additivity of independent Poisson random variables (Chapter 12):

$$
N(s, s+t) \sim \text{Po}(\lambda_1 t + \lambda_2 t) = \text{Po}((\lambda_1 + \lambda_2) t) \qquad \blacksquare
$$

**Generalization.** If $N_1, N_2, \ldots, N_m$ are independent Poisson processes with rates $\lambda_1, \ldots, \lambda_m$, then their superposition is a Poisson process with rate $\lambda_1 + \cdots + \lambda_m$.

---

## Splitting (Thinning)

The reverse operation is **splitting** (also called **thinning**): each event in a Poisson process is independently classified into one of several types.

!!! info "Splitting Theorem"
    Let $\{N(t)\}$ be a Poisson process with rate $\lambda$. Suppose each event is independently classified as Type 1 with probability $p$ and Type 2 with probability $q = 1 - p$. Let $N_1(t)$ and $N_2(t)$ count the Type 1 and Type 2 events respectively. Then:

    1. $\{N_1(t)\}$ is a Poisson process with rate $p\lambda$
    2. $\{N_2(t)\}$ is a Poisson process with rate $q\lambda$
    3. $\{N_1(t)\}$ and $\{N_2(t)\}$ are **independent**

**Proof sketch.** Consider any interval of length $t$. Conditional on $N(t) = n$, each of the $n$ events is independently Type 1 with probability $p$, so $N_1(t) \mid N(t) = n \sim B(n, p)$. Then:

$$
P(N_1(t) = k) = \sum_{n=k}^{\infty} \binom{n}{k} p^k q^{n-k} \cdot \frac{e^{-\lambda t}(\lambda t)^n}{n!}
$$

$$
= \frac{e^{-\lambda t}(p\lambda t)^k}{k!} \sum_{n=k}^{\infty} \frac{(q\lambda t)^{n-k}}{(n-k)!}
= \frac{e^{-\lambda t}(p\lambda t)^k}{k!} \cdot e^{q\lambda t}
= \frac{e^{-p\lambda t}(p\lambda t)^k}{k!}
$$

So $N_1(t) \sim \text{Po}(p\lambda t)$. Similarly, $N_2(t) \sim \text{Po}(q\lambda t)$. Independence of $N_1$ and $N_2$ follows from a similar joint calculation. $\blacksquare$

---

## Generalization: Multi-Way Splitting

Each event can be classified into $m$ types with probabilities $p_1, p_2, \ldots, p_m$ (where $\sum p_i = 1$). The resulting processes $N_1, N_2, \ldots, N_m$ are:

- Independent Poisson processes
- With rates $p_1 \lambda, p_2 \lambda, \ldots, p_m \lambda$

This follows by applying the two-way splitting theorem repeatedly, or by a direct multinomial argument.

---

## Examples

??? example "Hospital Emergency Room"
    Patients arrive at an ER as a Poisson process with rate $\lambda = 10$ per hour. Each patient is independently classified as:

    - Critical (probability 0.1): rate $= 0.1 \times 10 = 1$ per hour
    - Urgent (probability 0.3): rate $= 0.3 \times 10 = 3$ per hour
    - Non-urgent (probability 0.6): rate $= 0.6 \times 10 = 6$ per hour

    The three streams are independent Poisson processes. The probability of no critical patients in a 2-hour shift is:

    $$
    P(N_{\text{crit}}(2) = 0) = e^{-1 \times 2} = e^{-2} \approx 0.1353
    $$

??? example "Network Traffic"
    Two independent servers generate requests at rates $\lambda_1 = 20$ and $\lambda_2 = 30$ per second. By merging, the total traffic to a load balancer is a Poisson process with rate $50$ per second.

    The probability of more than 60 requests in 1 second is $P(N(1) > 60)$ where $N(1) \sim \text{Po}(50)$.

---

## Summary

| Operation | Input | Output |
|:---|:---|:---|
| Merging | Independent $\text{PP}(\lambda_1)$ and $\text{PP}(\lambda_2)$ | $\text{PP}(\lambda_1 + \lambda_2)$ |
| Splitting (prob $p$) | $\text{PP}(\lambda)$ | Independent $\text{PP}(p\lambda)$ and $\text{PP}((1-p)\lambda)$ |

Merging and splitting are inverses of each other, and both preserve the Poisson process structure. These operations make the Poisson process a natural building block for modeling complex systems composed of multiple independent streams.
