# Chapter 12 Exercises: Poisson Approximation


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

---

## Exercise 1: Poisson PMF Basics

Let $X \sim \text{Po}(6)$.

**(a)** Compute $P(X = 0)$, $P(X = 3)$, $P(X = 6)$, and $P(X = 10)$.

**(b)** Compute $P(X \leq 4)$ and $P(X > 8)$.

**(c)** Find the mode of $X$.

**(d)** Verify numerically that $E[X] = \text{Var}(X) = 6$.

??? solution "Solution"

    **(a)**

    $$
    P(X = k) = \frac{e^{-6} \cdot 6^k}{k!}
    $$

    ```python
    from scipy.stats import poisson

    la = 6
    for k in [0, 3, 6, 10]:
        print(f"P(X = {k}) = {poisson.pmf(k, la):.6f}")
    ```

    - $P(X = 0) = e^{-6} \approx 0.002479$
    - $P(X = 3) = \frac{e^{-6} \cdot 216}{6} \approx 0.089235$
    - $P(X = 6) \approx 0.160623$
    - $P(X = 10) \approx 0.041303$

    **(b)**

    ```python
    print(f"P(X ≤ 4) = {poisson.cdf(4, la):.6f}")
    print(f"P(X > 8) = {1 - poisson.cdf(8, la):.6f}")
    ```

    $P(X \leq 4) \approx 0.2851$, $P(X > 8) \approx 0.1528$.

    **(c)** Since $\lambda = 6$ is an integer, the mode is at both $k = 5$ and $k = 6$.

    **(d)**

    ```python
    import numpy as np
    np.random.seed(42)
    samples = np.random.poisson(6, 100_000)
    print(f"Sample mean: {samples.mean():.4f}")
    print(f"Sample var:  {samples.var(ddof=1):.4f}")
    ```

---

## Exercise 2: Poisson Approximation to the Binomial

A manufacturing process produces microchips with a defect probability of $p = 0.002$ per chip. A batch contains $n = 1000$ chips.

**(a)** Let $X$ be the number of defective chips. What is the exact distribution of $X$? What is the Poisson approximation?

**(b)** Compute $P(X = 0)$, $P(X \leq 3)$, and $P(X > 5)$ using both the exact Binomial and the Poisson approximation. Compare.

**(c)** Compute the Le Cam error bound for this approximation.

??? solution "Solution"

    **(a)** $X \sim B(1000, 0.002)$ exactly. Poisson approximation: $X \approx \text{Po}(\lambda)$ with $\lambda = np = 2$.

    **(b)**

    ```python
    from scipy.stats import binom, poisson

    n, p = 1000, 0.002
    la = n * p

    print(f"{'':>20} {'Binomial':>12} {'Poisson':>12} {'Diff':>12}")
    print("-" * 58)

    b0, p0 = binom.pmf(0, n, p), poisson.pmf(0, la)
    print(f"{'P(X=0)':>20} {b0:>12.6f} {p0:>12.6f} {abs(b0-p0):>12.2e}")

    b3, p3 = binom.cdf(3, n, p), poisson.cdf(3, la)
    print(f"{'P(X≤3)':>20} {b3:>12.6f} {p3:>12.6f} {abs(b3-p3):>12.2e}")

    b5, p5 = 1 - binom.cdf(5, n, p), 1 - poisson.cdf(5, la)
    print(f"{'P(X>5)':>20} {b5:>12.6f} {p5:>12.6f} {abs(b5-p5):>12.2e}")
    ```

    **(c)** Le Cam bound: $np^2 = 1000 \cdot (0.002)^2 = 0.004$.

---

## Exercise 3: Couples with the Same Birthday

Approximately 80,000 marriages took place in New York last year.

**(a)** Estimate the probability that more than 250 couples share a birthday, using the Poisson approximation.

**(b)** Compute the exact probability using the Binomial distribution and compare.

**(c)** What is $\lambda$ in this problem? Compute $E[S_n]$ and $\text{SD}(S_n)$ where $S_n$ is the number of couples with the same birthday.

??? solution "Solution"

    **(a)** With $n = 80{,}000$, $p = 1/365$, $\lambda = np = 80000/365 \approx 219.18$:

    ```python
    from scipy.stats import poisson, binom

    n = 80_000
    p = 1 / 365
    la = n * p

    poisson_prob = 1 - poisson.cdf(250, la)
    print(f"P(X > 250) ≈ {poisson_prob:.4f}  (Poisson)")
    ```

    $P(X > 250) \approx 0.0188$.

    **(b)**

    ```python
    binom_prob = 1 - binom.cdf(250, n, p)
    print(f"P(S > 250) = {binom_prob:.4f}  (Binomial exact)")
    ```

    $P(S_n > 250) = 0.0187$. The Poisson approximation is excellent.

    **(c)** $\lambda = 80000/365 \approx 219.18$. $E[S_n] = \lambda \approx 219.18$. $\text{SD}(S_n) \approx \sqrt{219.18} \approx 14.81$.

---

## Exercise 4: Sum of Independent Poissons

Customers arrive at a store from three independent sources:

- Walk-ins: $X_1 \sim \text{Po}(8)$ per hour
- Online orders for pickup: $X_2 \sim \text{Po}(5)$ per hour
- Phone orders: $X_3 \sim \text{Po}(2)$ per hour

**(a)** What is the distribution of the total number of customers per hour?

**(b)** Compute $P(\text{total} > 20)$ and $P(\text{total} = 15)$.

**(c)** Simulate 10,000 hours and verify the theoretical distribution.

??? solution "Solution"

    **(a)** By the additivity property, $X_1 + X_2 + X_3 \sim \text{Po}(8 + 5 + 2) = \text{Po}(15)$.

    **(b)**

    ```python
    from scipy.stats import poisson

    la = 15
    print(f"P(total > 20) = {1 - poisson.cdf(20, la):.6f}")
    print(f"P(total = 15) = {poisson.pmf(15, la):.6f}")
    ```

    **(c)**

    ```python
    import numpy as np

    np.random.seed(42)
    n_sim = 10_000

    X1 = np.random.poisson(8, n_sim)
    X2 = np.random.poisson(5, n_sim)
    X3 = np.random.poisson(2, n_sim)
    total = X1 + X2 + X3

    print(f"Sample mean: {total.mean():.3f} (theoretical: 15)")
    print(f"Sample var:  {total.var(ddof=1):.3f} (theoretical: 15)")
    ```

---

## Exercise 5: Quality Control

A car manufacturer inspects vehicles before shipment. Each vehicle is checked for $n = 500$ potential defects, each occurring independently with probability $p = 0.001$.

**(a)** What is the expected number of defects per vehicle?

**(b)** What is the probability of a vehicle having zero defects?

**(c)** What is the probability of finding more than 3 defects on a vehicle?

**(d)** The factory ships 200 vehicles per day. Using the additivity property, what is the expected total number of defects found per day, and what is its distribution?

??? solution "Solution"

    **(a)** $\lambda = np = 500 \times 0.001 = 0.5$.

    **(b)** $P(X = 0) = e^{-0.5} \approx 0.6065$.

    **(c)**

    ```python
    from scipy.stats import poisson
    la = 0.5
    print(f"P(X > 3) = {1 - poisson.cdf(3, la):.6f}")
    ```

    $P(X > 3) \approx 0.0018$.

    **(d)** Each vehicle has defects $\sim \text{Po}(0.5)$. For 200 independent vehicles, total defects $\sim \text{Po}(200 \times 0.5) = \text{Po}(100)$. Expected total: 100 defects per day.

---

## Exercise 6: Convergence Rate

**(a)** For $\lambda = 5$, compute the maximum PMF difference $\max_k |P(X_n = k) - P(Y = k)|$ where $X_n \sim B(n, 5/n)$ and $Y \sim \text{Po}(5)$, for $n = 10, 20, 50, 100, 500, 1000$.

**(b)** Plot the maximum difference as a function of $n$ on a log-log scale. What is the observed convergence rate?

**(c)** Compare the observed maximum difference with the Le Cam bound $\lambda^2/n$ for each $n$.

??? solution "Solution"

    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import binom, poisson

    la = 5
    n_values = [10, 20, 50, 100, 500, 1000]

    print(f"{'n':>6} {'Max |diff|':>12} {'Le Cam (λ²/n)':>14} {'Ratio':>8}")
    print("-" * 44)

    max_diffs = []
    for n in n_values:
        p = la / n
        k = np.arange(0, max(30, int(la + 6*np.sqrt(la))))
        b_pmf = binom.pmf(k, n, p)
        p_pmf = poisson.pmf(k, la)
        md = np.max(np.abs(b_pmf - p_pmf))
        max_diffs.append(md)
        lecam = la**2 / n
        print(f"{n:>6} {md:>12.6e} {lecam:>14.6e} {md/lecam:>8.4f}")

    plt.figure(figsize=(8, 5))
    plt.loglog(n_values, max_diffs, 'o-', label='Max |PMF diff|')
    plt.loglog(n_values, [la**2/n for n in n_values], 's--', label='λ²/n bound')
    plt.xlabel('n')
    plt.ylabel('Error')
    plt.title('Convergence Rate of Poisson Approximation')
    plt.legend()
    plt.grid(True, alpha=0.3, which='both')
    plt.tight_layout()
    plt.show()
    ```

    The convergence rate is $O(1/n)$, consistent with the Le Cam bound.

---

## Exercise 7: Overdispersion Test

You observe the following daily counts of customer complaints over 30 days:

```
3, 1, 4, 2, 7, 0, 3, 5, 1, 2, 8, 3, 2, 1, 4,
6, 0, 3, 2, 5, 1, 4, 3, 2, 1, 9, 3, 2, 4, 1
```

**(a)** Compute the sample mean and sample variance.

**(b)** Compute the dispersion index $D = s^2/\bar{x}$.

**(c)** Does a Poisson model seem appropriate for this data? Why or why not?

??? solution "Solution"

    ```python
    import numpy as np

    data = np.array([3,1,4,2,7,0,3,5,1,2,8,3,2,1,4,
                     6,0,3,2,5,1,4,3,2,1,9,3,2,4,1])

    mean = data.mean()
    var = data.var(ddof=1)
    D = var / mean

    print(f"Sample mean: {mean:.4f}")
    print(f"Sample var:  {var:.4f}")
    print(f"Dispersion index D = {D:.4f}")

    if abs(D - 1) < 0.5:
        print("D ≈ 1: Poisson model is plausible")
    elif D > 1.5:
        print("D >> 1: Overdispersed — consider Negative Binomial")
    else:
        print("D < 1: Underdispersed — Poisson may not fit well")
    ```

    The sample mean is approximately 3.0 and sample variance is approximately 4.3, giving $D \approx 1.44$. This suggests mild overdispersion — a Poisson model is a reasonable first approximation but a Negative Binomial might fit better.
