# When to Use the Poisson Approximation

## The Three Conditions

The Poisson approximation to the Binomial is appropriate when:

| Condition | Meaning |
|:---|:---|
| $n$ is **large** | Many trials (typically $n \geq 20$) |
| $p$ is **small** | Each trial has a low probability of success (typically $p \leq 0.05$) |
| $\lambda = np$ is **moderate** | The expected count is neither too small nor too large |

In summary: **many trials, each with a small probability of success, producing a moderate expected number of successes**.

---

## Rule of Thumb

A widely used guideline:

!!! tip "Rule of Thumb"
    Use the Poisson approximation $B(n, p) \approx \text{Po}(\lambda)$ when:

    - $n \geq 20$ and $p \leq 0.05$, or more conservatively
    - $n \geq 100$ and $np \leq 10$

    The approximation improves as $n$ increases and $p$ decreases, with $\lambda = np$ held fixed.

---

## Error Bound

For the general case where $A_1, A_2, \ldots, A_n$ are independent events with possibly different probabilities $p_i = P(A_i)$, and $X = \sum_{i=1}^{n} \mathbf{1}_{A_i}$, the **Le Cam bound** gives:

$$

\left| P(X \in A) - P(Y \in A) \right| \leq \sum_{i=1}^{n} p_i^2 \leq \left(\max_{1 \leq i \leq n} p_i\right) \cdot \lambda

$$

where $Y \sim \text{Po}(\lambda)$ and $\lambda = \sum_{i=1}^{n} p_i$.

When all $p_i = p$, this simplifies to:

$$

\text{Error} \leq np^2 = p\lambda

$$

So the error is controlled by $p \cdot \lambda$ — small $p$ and moderate $\lambda$ guarantee a good approximation.

---

## Why Not Just Use the Binomial?

For moderate $n$, computing Binomial probabilities directly is feasible. However, the Poisson approximation is useful in several situations:

1. **Computational simplicity**: $\frac{e^{-\lambda}\lambda^k}{k!}$ avoids computing $\binom{n}{k}$ which involves large factorials when $n$ is large.

2. **Unknown $n$**: In many applications (e.g., modeling rare events in a time period), $n$ is not well-defined. The Poisson model with rate $\lambda$ is the natural starting point.

3. **Heterogeneous probabilities**: When $p_i$ differ across trials, the sum is not exactly Binomial but is still well-approximated by Poisson.

4. **Theoretical elegance**: The Poisson has nicer mathematical properties (e.g., additivity of independent Poissons, connection to Poisson process).

---

## Typical Applications

The Poisson distribution is a natural model whenever we count the number of "rare events" in some fixed domain:

- **Insurance**: Number of claims filed per month
- **Finance**: Number of defaults in a loan portfolio
- **Telecommunications**: Number of calls arriving at a call center per minute
- **Biology**: Number of mutations in a DNA strand
- **Manufacturing**: Number of defects per unit of product
- **Traffic**: Number of accidents at an intersection per year
- **Epidemiology**: Number of disease cases in a region

---

## Diagnostic: When Is the Approximation Poor?

The approximation breaks down when:

- $p$ is not small (e.g., $p = 0.3$): The Binomial is noticeably skewed differently from Poisson
- $n$ is small: Not enough trials for the limit to kick in
- $\lambda = np$ is very large: Both Binomial and Poisson are well-approximated by the Normal (by CLT), so the Poisson adds little value

```python
import numpy as np
from scipy.stats import binom, poisson

def approximation_quality(n, p):
    """Assess the quality of Poisson approximation to B(n,p)."""
    la = n * p
    k_max = min(n, int(la + 5 * np.sqrt(la)) + 1)
    k = np.arange(0, k_max + 1)

    binom_pmf = binom.pmf(k, n, p)
    poisson_pmf = poisson.pmf(k, la)

    max_diff = np.max(np.abs(binom_pmf - poisson_pmf))
    total_variation = 0.5 * np.sum(np.abs(binom_pmf - poisson_pmf))

    print(f"B({n}, {p}) vs Po({la})")
    print(f"  Max PMF difference:   {max_diff:.6e}")
    print(f"  Total variation dist: {total_variation:.6e}")
    print(f"  Le Cam bound (p·λ):   {p * la:.6e}")
    print()

# Good approximation
approximation_quality(1000, 0.01)   # n large, p small
approximation_quality(2000, 0.005)  # n very large, p very small

# Moderate approximation
approximation_quality(100, 0.05)    # n moderate, p moderate
approximation_quality(50, 0.1)      # n moderate, p not so small

# Poor approximation
approximation_quality(20, 0.3)      # p too large
approximation_quality(10, 0.5)      # p way too large
```
