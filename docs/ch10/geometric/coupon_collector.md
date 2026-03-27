# Coupon Collector Problem

## The Problem

A cereal company places one of $n$ different coupons in each box, uniformly at random and independently. You want to collect all $n$ distinct coupons. How many boxes must you buy?

This classic problem appears in many guises: collecting all Monopoly game pieces at a fast food restaurant, seeing every face of a die, or covering all states in a random survey. The solution is a beautiful application of the Geometric distribution.

## Setup and Decomposition

Let $T$ be the total number of boxes needed. We decompose the collection process into **phases**.

- **Phase 1**: You have 0 distinct coupons. Each box gives a new coupon with probability $n/n = 1$. So $T_1 = 1$ (deterministic).
- **Phase 2**: You have 1 distinct coupon. Each box gives a new coupon with probability $(n-1)/n$. So $T_2 \sim \text{Geo}\!\left(\frac{n-1}{n}\right)$.
- **Phase $i$**: You have $i - 1$ distinct coupons. Each box gives a new coupon with probability $\frac{n - (i-1)}{n}$. So $T_i \sim \text{Geo}\!\left(\frac{n-i+1}{n}\right)$.

The total number of boxes is

$$
T = T_1 + T_2 + \cdots + T_n
$$

where the $T_i$ are **independent** Geometric random variables.

---

## Expected Value

By linearity of expectation:

$$
E[T] = \sum_{i=1}^{n} E[T_i] = \sum_{i=1}^{n} \frac{n}{n - i + 1} = n \sum_{j=1}^{n} \frac{1}{j} = n H_n
$$

where $H_n = 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}$ is the **$n$-th harmonic number**.

!!! info "Coupon Collector Expected Time"
    The expected number of boxes to collect all $n$ coupons is

    $$E[T] = n H_n = n\ln n + \gamma n + O(1)$$

    where $\gamma \approx 0.5772$ is the Euler--Mascheroni constant and $H_n \approx \ln n + \gamma$ for large $n$.

---

## Variance

Since the phases are independent:

$$
\text{Var}(T) = \sum_{i=1}^{n} \text{Var}(T_i) = \sum_{i=1}^{n} \frac{1 - \frac{n-i+1}{n}}{\left(\frac{n-i+1}{n}\right)^2} = n^2 \sum_{j=1}^{n} \frac{1}{j^2} - n \sum_{j=1}^{n} \frac{1}{j}
$$

Using $\sum_{j=1}^{\infty} \frac{1}{j^2} = \frac{\pi^2}{6}$, for large $n$:

$$
\text{Var}(T) \approx \frac{\pi^2}{6} n^2
$$

The standard deviation grows as $\Theta(n)$, which is smaller order than the mean $\Theta(n \ln n)$, so the relative variability decreases as $n$ grows.

---

## Example: Dice Faces

Collect all 6 faces of a fair die by rolling repeatedly. With $n = 6$:

$$
E[T] = 6 \left(1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6}\right) = 6 \cdot \frac{49}{20} = 14.7
$$

On average, you need about 14.7 rolls to see all six faces.

The breakdown by phase:

| Phase $i$ | Coupons held | $P(\text{new})$ | $E[T_i]$ |
|:---------:|:------------:|:----------------:|:---------:|
| 1 | 0 | $6/6$ | 1.00 |
| 2 | 1 | $5/6$ | 1.20 |
| 3 | 2 | $4/6$ | 1.50 |
| 4 | 3 | $3/6$ | 2.00 |
| 5 | 4 | $2/6$ | 3.00 |
| 6 | 5 | $1/6$ | 6.00 |

The last phase -- waiting for the final coupon -- dominates and alone contributes $n/1 = n$ to the expected total.

---

## Asymptotic Behavior

For large $n$, the coupon collector time concentrates around its mean. One can show that

$$
P\!\left(T > n \ln n + cn\right) \to 1 - e^{-e^{-c}} \quad \text{as } n \to \infty
$$

for any constant $c$. This is a **Gumbel distribution** limit, indicating that the fluctuations around $n \ln n$ are of order $n$.
