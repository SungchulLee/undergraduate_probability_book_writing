# Waiting Time for the k-th Arrival

## The k-th Arrival Time

In a Poisson process with rate $\lambda$, let $S_k$ denote the time of the $k$-th arrival. Since interarrival times $T_1, T_2, \ldots, T_k$ are iid $\text{Exp}(\lambda)$:

$$S_k = T_1 + T_2 + \cdots + T_k \sim \Gamma(k, \lambda) = \text{Erlang}(k, \lambda)$$

### Mean and Variance of S_k

$$E[S_k] = \frac{k}{\lambda}, \qquad \text{Var}(S_k) = \frac{k}{\lambda^2}$$

The expected time to the $k$-th arrival is simply $k$ times the expected interarrival time, which is intuitive.

## Connection to the Poisson Distribution

The event $\{S_k \leq t\}$ (the $k$-th arrival occurs by time $t$) is equivalent to $\{N(t) \geq k\}$ (at least $k$ arrivals by time $t$), where $N(t) \sim \text{Po}(\lambda t)$. Therefore:

$$P(S_k \leq t) = P(N(t) \geq k) = 1 - \sum_{j=0}^{k-1} \frac{(\lambda t)^j}{j!} e^{-\lambda t}$$

This provides a closed-form CDF for the Erlang distribution and establishes a deep duality: the **Gamma/Erlang CDF** equals the **Poisson tail probability**.

## The Inspection Paradox

!!! warning "Paradox of Interarrival Times"
    Consider a Poisson process with rate $\lambda$ running from $t = -\infty$ to $t = \infty$. Pick a **fixed time point** (say, today's date). Let $\tau$ be the length of the interarrival interval **containing** that fixed point.

    **Surprising result:**

    - Each individual interarrival time $T_i$ is $\text{Exp}(\lambda)$ with mean $1/\lambda$
    - But $\tau \sim \Gamma(2, \lambda)$ with mean $2/\lambda$

    The interval you land in is, on average, **twice as long** as a typical interarrival time!

### Why Does This Happen?

This is an instance of the **inspection paradox** (also called **length-biased sampling** or the **bus waiting paradox**). When you arrive at a random time:

- You are more likely to land in a **longer** interarrival interval than a shorter one
- The probability of landing in an interval is proportional to its length
- This biases the observed interval length upward

### Formal Explanation

The fixed time point splits $\tau$ into two parts:

- The **backward recurrence time** $B$: time from the last arrival before the fixed point
- The **forward recurrence time** $F$: time from the fixed point to the next arrival

By the memoryless property of the Poisson process:

- $F \sim \text{Exp}(\lambda)$ (memoryless: time to next event is always $\text{Exp}(\lambda)$)
- $B \sim \text{Exp}(\lambda)$ (by time-reversibility of the Poisson process)
- $B$ and $F$ are independent

Therefore:

$$\tau = B + F \sim \text{Exp}(\lambda) * \text{Exp}(\lambda) = \Gamma(2, \lambda)$$

$$E[\tau] = \frac{2}{\lambda}, \qquad \text{Var}(\tau) = \frac{2}{\lambda^2}$$

### Everyday Examples of the Inspection Paradox

- **Bus waiting**: If buses arrive as a Poisson process, and you arrive at a random time, your expected wait is $1/\lambda$ — the full mean interarrival time, not half of it
- **Class size**: If you randomly pick a student and ask their class size, the average answer is larger than the overall average class size (larger classes contain more students)
- **Family size**: If you randomly pick a child and ask their family size, the answer is biased upward

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
lam = 1.0
n_sim = 100000

# Simulate Poisson process and find interval containing a fixed point
def simulate_inspection_paradox(lam, fixed_point, n_arrivals=1000):
    """Simulate the interarrival interval containing a fixed point."""
    # Generate many interarrival times
    interarrivals = np.random.exponential(1/lam, n_arrivals)
    arrival_times = np.cumsum(interarrivals)

    # Find the interval containing the fixed point
    idx = np.searchsorted(arrival_times, fixed_point)
    if idx == 0:
        return interarrivals[0]  # fixed point is before first arrival
    return interarrivals[idx]  # length of interval containing fixed point

# Run simulation
fixed_point = 50.0  # arbitrary fixed time
tau_samples = np.array([
    simulate_inspection_paradox(lam, fixed_point, 200)
    for _ in range(n_sim)
])

# Regular interarrival times
regular_interarrivals = np.random.exponential(1/lam, n_sim)

# Plot comparison
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

x = np.linspace(0, 8, 200)

# Histograms
axes[0].hist(regular_interarrivals, bins=80, density=True, alpha=0.5,
             range=(0, 8), label=f'Regular T_i ~ Exp({lam})', color='blue')
axes[0].hist(tau_samples, bins=80, density=True, alpha=0.5,
             range=(0, 8), label=f'τ (containing fixed point)', color='red')
axes[0].plot(x, stats.expon.pdf(x, scale=1/lam), 'b-', lw=2,
             label='Exp(1) PDF')
axes[0].plot(x, stats.gamma.pdf(x, a=2, scale=1/lam), 'r-', lw=2,
             label='Γ(2,1) PDF')
axes[0].set_title('Inspection Paradox')
axes[0].set_xlabel('Interarrival time')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Visualize a Poisson process with the inspection paradox
np.random.seed(7)
interarrivals = np.random.exponential(1/lam, 20)
arrivals = np.cumsum(interarrivals)
arrivals = arrivals[arrivals < 8]

fixed_t = 5.0
axes[1].plot(arrivals, np.zeros(len(arrivals)), 'or', markersize=8)
axes[1].axvline(fixed_t, color='black', lw=2, label=f'Fixed point t={fixed_t}')

# Find containing interval
idx = np.searchsorted(arrivals, fixed_t)
if idx > 0 and idx < len(arrivals):
    left = arrivals[idx-1]
    right = arrivals[idx]
    axes[1].axvline(left, color='red', lw=2, alpha=0.7)
    axes[1].axvline(right, color='red', lw=2, alpha=0.7)
    axes[1].annotate('', xy=(right, -0.3), xytext=(left, -0.3),
                     arrowprops=dict(arrowstyle='<->', color='red', lw=2))
    axes[1].text((left+right)/2, -0.4, f'τ = {right-left:.2f}',
                 ha='center', color='red', fontsize=12)

for a in arrivals:
    axes[1].plot([a, a], [-0.1, 0.1], 'r-', lw=1)

axes[1].set_xlim(0, 8)
axes[1].set_ylim(-0.6, 0.6)
axes[1].set_title('Interarrival Interval Containing Fixed Point')
axes[1].set_xlabel('Time')
axes[1].legend(loc='upper right')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('kth_arrival_paradox.png', dpi=150, bbox_inches='tight')
plt.show()

# Print statistics
print("=== Inspection Paradox Statistics ===")
print(f"Regular interarrival: E[T] = {np.mean(regular_interarrivals):.4f} "
      f"(theory {1/lam:.4f})")
print(f"Containing interval:  E[τ] = {np.mean(tau_samples):.4f} "
      f"(theory {2/lam:.4f})")
print(f"Ratio E[τ]/E[T] = {np.mean(tau_samples)/np.mean(regular_interarrivals):.4f} "
      f"(theory 2.0)")
```
