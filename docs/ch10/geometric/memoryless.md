# Memoryless Property

## Intuition

Imagine you have been rolling a die for 20 rolls without seeing a six. Does the fact that you have already waited 20 rolls make a six more likely on the next roll? With independent trials the answer is no -- the die has no memory. The probability of needing $t$ more rolls is exactly the same as if you were starting fresh. This "fresh start" property is called **memorylessness**, and among discrete distributions it characterizes the Geometric.

## Statement

!!! info "Memoryless Property"
    A random variable $X \sim \text{Geo}(p)$ satisfies: for all $s, t \ge 1$,

    $$P(X > s + t \mid X > s) = P(X > t)$$

    Equivalently, given that the first $s$ trials were all failures, the **remaining** waiting time has the same Geometric distribution as the original.

---

## Proof

Using the tail probability $P(X > k) = q^k$ from the Geometric distribution:

$$
P(X > s + t \mid X > s) = \frac{P(X > s + t)}{P(X > s)} = \frac{q^{s+t}}{q^s} = q^t = P(X > t)
$$

The key step is that the exponential form $q^k$ factorizes: $q^{s+t} = q^s \cdot q^t$. This factorization is what makes the property work.

---

## Uniqueness: Only Discrete Memoryless Distribution

The Geometric distribution is the **only** discrete distribution on $\{1, 2, 3, \ldots\}$ that is memoryless.

??? note "Proof Sketch"
    Suppose $X$ is a positive-integer-valued random variable with $P(X > s + t \mid X > s) = P(X > t)$ for all $s, t \ge 1$. Let $g(k) = P(X > k)$. Then the memoryless property gives

    $$g(s + t) = g(s) \cdot g(t)$$

    for all positive integers $s, t$. The only solution with $g(0) = 1$ and $0 < g(1) < 1$ is $g(k) = q^k$ for some $q \in (0, 1)$. Setting $p = 1 - q$, we recover $P(X > k) = (1-p)^k$, which is the Geometric tail probability.

---

## Conditional Distribution Interpretation

Another way to state the memoryless property: given that we have waited $s$ trials without success, the number of **additional** trials needed is again $\text{Geo}(p)$. Formally, if $X \sim \text{Geo}(p)$, then

$$
(X - s \mid X > s) \sim \text{Geo}(p)
$$

The conditional distribution is identical to the original distribution. The process "restarts" after every failure.

---

## Continuous Counterpart

The Exponential distribution is the continuous analog of the Geometric and is the **only** continuous memoryless distribution. If $T \sim \text{Exp}(\lambda)$, then

$$
P(T > s + t \mid T > s) = P(T > t)
$$

This parallel is not a coincidence: as $n \to \infty$ with $p = \lambda / n$, the rescaled Geometric converges to the Exponential.

---

## Examples

**Coin flips.** You have flipped a fair coin 100 times without seeing heads. The probability of needing at least 5 more flips is $P(X > 5) = (1/2)^5 = 1/32$, the same as at the start.

**Equipment failure.** A machine component fails on each day independently with probability 0.01. Given that it has survived 200 days, the probability it lasts at least 30 more days is $(0.99)^{30} \approx 0.740$, regardless of how long it has already been running.

!!! warning "Gambler's Fallacy"
    The memoryless property is the mathematical reason behind the **Gambler's Fallacy**: past failures do not make future success "due." If each trial is independent with the same probability, the system truly has no memory.
