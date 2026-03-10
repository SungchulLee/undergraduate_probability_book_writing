# Buffon's Needle


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Setup

On a sheet of paper, draw parallel horizontal lines **1 unit apart**. Drop a needle of **length 1** onto the paper at random. The needle's position is determined by:

- $Y$: the height of the lower end, uniformly distributed on $[0, 1]$.
- $\Theta$: the angle of the needle relative to horizontal, uniformly distributed on $[0, \pi]$.

The height of the upper end is $Y + \sin\Theta$.

The needle **crosses a line** (at $y = 1$) if and only if $Y + \sin\Theta \geq 1$.

## Crossing Probability

Define the indicator:

$$
R_i = \begin{cases} 1 & \text{if the needle crosses a line on the } i\text{-th drop} \\ 0 & \text{otherwise} \end{cases}
$$

Then $R_i \overset{iid}{\sim} \text{Bernoulli}(p)$ where:

$$
p = P(Y + \sin\Theta \geq 1)
$$

To compute $p$:

$$
p = \int_0^{\pi} \int_0^1 \mathbf{1}(y + \sin\theta \geq 1)\, dy\, \frac{d\theta}{\pi}
$$

For a fixed $\theta$, the integral over $y$ gives $\min(\sin\theta, 1)$. For a unit-length needle on unit-spaced lines, this simplifies to:

$$
p = \frac{1}{\pi}\int_0^{\pi} \sin\theta\, d\theta = \frac{2}{\pi}
$$

## Estimating pi

By the Law of Large Numbers, after $n$ drops:

$$
\frac{1}{n}\sum_{i=1}^n R_i \xrightarrow{a.s.} \frac{2}{\pi}
$$

Therefore:

$$
\pi \approx \frac{2n}{\sum_{i=1}^n R_i} = \frac{2}{\text{proportion of crossings}}
$$

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n = 5000

# Random lower height Y ~ Uniform(0, 1) and angle Theta ~ Uniform(0, pi)
y = np.random.rand(n)           # height of lower end
theta = np.random.rand(n)       # angle / pi (so theta*pi is actual angle)

# Height of upper end
h = y + np.sin(np.pi * theta)

# Does the needle cross the line at y = 1?
crosses = h >= 1

# Estimate pi
estimated_pi = 2 * n / np.sum(crosses)
print(f"Estimated pi: {estimated_pi:.4f}")

# Running estimate
cumulative_crosses = np.cumsum(crosses)
running_pi = 2 * np.arange(1, n + 1) / cumulative_crosses

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Running estimate
axes[0].plot(range(1, n + 1), running_pi, 'r-', alpha=0.7)
axes[0].axhline(y=np.pi, color='k', linestyle='-', label='True π')
axes[0].set_xlabel('Number of drops')
axes[0].set_ylabel('Estimate of π')
axes[0].set_ylim([2, 4])
axes[0].set_title("Buffon's Needle: Running Estimate")
axes[0].legend()
axes[0].grid(True)

# Histogram of repeated experiments
m = 1000
n_each = 100
estimates = []
for _ in range(m):
    y_exp = np.random.rand(n_each)
    theta_exp = np.random.rand(n_each)
    h_exp = y_exp + np.sin(np.pi * theta_exp)
    n_crosses = np.sum(h_exp >= 1)
    if n_crosses > 0:
        estimates.append(2 * n_each / n_crosses)
estimates = np.array(estimates)

axes[1].hist(estimates, bins=30, edgecolor='black')
axes[1].axvline(x=np.pi, color='r', linestyle='--', label='True π')
axes[1].set_xlabel('Estimate of π')
axes[1].set_ylabel('Frequency')
axes[1].set_title(f'Histogram ({m} experiments, {n_each} drops each)')
axes[1].legend()

plt.tight_layout()
plt.savefig('buffon_needle.png', dpi=150, bbox_inches='tight')
plt.show()
```

## Historical Significance

Buffon's needle problem, proposed by Georges-Louis Leclerc, Comte de Buffon in 1777, is one of the earliest problems in geometric probability. It provides a beautiful connection between geometry ($\pi$) and probability, and is a classic example of Monte Carlo estimation long before the term was coined.
