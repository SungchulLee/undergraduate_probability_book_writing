# Approximating Sums of Random Variables

## General Procedure

Given iid $X_1, \ldots, X_n$ with mean $\mu$ and variance $\sigma^2$, the CLT gives:

$$S_n = \sum_{k=1}^n X_k \approx N(n\mu, \, n\sigma^2)$$

To compute $P(S_n \leq a)$:

**Step 1.** Standardize:

$$P(S_n \leq a) = P\left(\frac{S_n - n\mu}{\sigma\sqrt{n}} \leq \frac{a - n\mu}{\sigma\sqrt{n}}\right)$$

**Step 2.** Apply the CLT:

$$\approx \Phi\left(\frac{a - n\mu}{\sigma\sqrt{n}}\right)$$

## Example: Exam Grading Time

An instructor has $50$ exams to grade sequentially. The time to grade each exam is iid with mean $20$ minutes and standard deviation $4$ minutes. What is the probability of grading at least $25$ exams in $450$ minutes?

Let $X_k$ = time to grade the $k$-th exam, with $\mu = 20$, $\sigma = 4$.

$$S_{25} = \sum_{k=1}^{25} X_k$$

We need $P(S_{25} \leq 450)$:

$$P(S_{25} \leq 450) = P\left(\frac{S_{25} - 25 \cdot 20}{4\sqrt{25}} \leq \frac{450 - 25 \cdot 20}{4\sqrt{25}}\right)$$

$$\approx \Phi\left(\frac{450 - 500}{20}\right) = \Phi(-2.5) = 0.0062$$

There is only about a $0.62\%$ chance of finishing at least $25$ exams in $450$ minutes.

## Example: Fair Coin Flips

Let $X_i$ be the $i$-th flip of a fair coin, recording $H = 1$ and $T = 0$. Define $Y_i = 2X_i - 1$, so $H$ and $T$ are recorded as $+1$ and $-1$.

Then $E[Y_i] = 0$, $E[Y_i^2] = 1$, $\text{Var}(Y_i) = 1$.

| Random Variable | Mean | Variance | Approximate Distribution |
|----------------|------|----------|-------------------------|
| $Y_i$ | $0$ | $1$ | — |
| $\sum_{i=1}^n Y_i$ | $0$ | $n$ | $N(0, n)$ |
| $\frac{1}{\sqrt{n}}\sum_{i=1}^n Y_i$ | $0$ | $1$ | $N(0, 1)$ |
| $\frac{1}{\sqrt{n}}\sum_{i=1}^{nt} Y_i$ | $0$ | $t$ | $N(0, t)$ |
| $\frac{1}{\sqrt{n}}\sum_{i=ns+1}^{nt} Y_i$ | $0$ | $t - s$ | $N(0, t-s)$ |

!!! note "Connection to Brownian Motion"
    The last two rows hint at the construction of **Brownian motion** $B(t)$, which is the continuous-time limit of the scaled random walk. $B(t) \sim N(0, t)$ and increments $B(t) - B(s) \sim N(0, t-s)$ are independent — exactly matching the CLT approximations above.

## Python Implementation

```python
import numpy as np
from scipy import stats

# Exam grading example
n = 25
mu, sigma = 20, 4
threshold = 450

z = (threshold - n * mu) / (sigma * np.sqrt(n))
prob = stats.norm.cdf(z)
print(f"P(S_25 <= 450) ≈ {prob:.4f}")

# Simulation verification
np.random.seed(42)
N_sim = 100000
sums = np.sum(np.random.normal(mu, sigma, (N_sim, n)), axis=1)
sim_prob = np.mean(sums <= threshold)
print(f"Simulated:        {sim_prob:.4f}")
```

**Output:**
```
P(S_25 <= 450) ≈ 0.0062
Simulated:        0.0063
```
