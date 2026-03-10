# Monte Carlo Simulation


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## The Idea

Monte Carlo methods use **random sampling** to estimate quantities that may be difficult to compute analytically. The Law of Large Numbers provides the theoretical justification: sample averages converge to expected values.

If we want to compute $\theta = \mathbb{E}[g(X)]$ for some random variable $X$ with known distribution, we can:

1. Draw $n$ iid samples $X_1, \ldots, X_n$ from the distribution of $X$.
2. Compute the sample average $\hat{\theta}_n = \frac{1}{n}\sum_{i=1}^n g(X_i)$.
3. By the LLN, $\hat{\theta}_n \to \theta$ as $n \to \infty$.

## Monte Carlo Estimation of pi

### Setup

Draw $n$ random points $X_i$ uniformly from the square $[-1, 1]^2$. Define:

$$
R_i = \begin{cases} 1 & \text{if } X_i \text{ is inside the unit circle} \\ 0 & \text{otherwise} \end{cases}
$$

Then $R_i \overset{iid}{\sim} \text{Bernoulli}(p)$ where:

$$
p = \frac{\text{Area of unit circle}}{\text{Area of square}} = \frac{\pi}{4}
$$

### Estimation

By the Law of Large Numbers:

$$
\frac{1}{n}\sum_{i=1}^n R_i \xrightarrow{a.s.} \frac{\pi}{4}
$$

Therefore:

$$
\pi \approx \frac{4}{n}\sum_{i=1}^n R_i = 4 \times \frac{\text{number of points inside circle}}{n}
$$

### Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n = 5000

# Generate random points in [-1, 1]^2
x = 2 * np.random.rand(2, n) - 1

# Check if inside unit circle
r2 = x[0]**2 + x[1]**2
inside = r2 <= 1

# Estimate pi
estimated_pi = 4 * np.sum(inside) / n
print(f"Estimated pi: {estimated_pi:.4f}")

# Plot
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Scatter plot
axes[0].scatter(x[0, inside], x[1, inside], c='red', s=1, label='Inside')
axes[0].scatter(x[0, ~inside], x[1, ~inside], c='blue', s=1, label='Outside')
axes[0].set_aspect('equal')
axes[0].set_title(f'{n} Random Darts')
axes[0].legend()

# Running estimate
running_pi = 4 * np.cumsum(inside) / np.arange(1, n + 1)
axes[1].plot(range(1, n + 1), running_pi, 'r-', alpha=0.7)
axes[1].axhline(y=np.pi, color='k', linestyle='-', label='True π')
axes[1].set_xlabel('Number of darts')
axes[1].set_ylabel('Estimate of π')
axes[1].set_title('Running Estimate (Strong Law)')
axes[1].legend()

# Histogram of repeated experiments
m = 1000  # number of experiments
n_each = 100  # darts per experiment
estimates = np.array([
    4 * np.sum(np.sum((2*np.random.rand(2, n_each)-1)**2, axis=0) <= 1) / n_each
    for _ in range(m)
])
axes[2].hist(estimates, bins=30, edgecolor='black')
axes[2].axvline(x=np.pi, color='r', linestyle='--', label='True π')
axes[2].set_xlabel('Estimate of π')
axes[2].set_ylabel('Frequency')
axes[2].set_title(f'Histogram ({m} experiments, {n_each} darts each)')
axes[2].legend()

plt.tight_layout()
plt.savefig('monte_carlo_pi.png', dpi=150, bbox_inches='tight')
plt.show()
```

### Observations

- The **left panel** (running estimate of a single trajectory) illustrates the **Strong Law**: one sample path converges to $\pi$.
- The **right panel** (histogram of many estimates) illustrates the **Weak Law**: the distribution of sample means concentrates around $\pi$.
- More darts $\Rightarrow$ better estimate. The standard error is $\sigma/\sqrt{n}$, which decreases at rate $1/\sqrt{n}$.
