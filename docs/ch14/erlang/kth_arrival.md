# Waiting Time for the k-th Arrival

The time of the $k$-th arrival in a Poisson process follows the Erlang (equivalently, Gamma) distribution, establishing a deep duality between Poisson counts and Gamma waiting times.

## Definition

In a Poisson process with rate $\lambda$, let $S_k$ denote the time of the $k$-th arrival. Since the interarrival times $T_1, T_2, \ldots, T_k$ are iid $\text{Exp}(\lambda)$:

$$
S_k = T_1 + T_2 + \cdots + T_k \sim \Gamma(k, \lambda) = \text{Erlang}(k, \lambda)
$$

**Moments:**

$$
E[S_k] = \frac{k}{\lambda}, \qquad \text{Var}(S_k) = \frac{k}{\lambda^2}
$$

**Poisson-Gamma duality:**

$$
P(S_k \leq t) = P(N(t) \geq k) = 1 - \sum_{j=0}^{k-1} \frac{(\lambda t)^j}{j!} e^{-\lambda t}
$$

where $N(t) \sim \text{Po}(\lambda t)$ is the Poisson count in $[0, t]$.

## Explanation

### The Poisson-Gamma Duality

The event "the $k$-th arrival occurs by time $t$" is logically equivalent to "at least $k$ events occur in $[0, t]$":

$$
\{S_k \leq t\} = \{N(t) \geq k\}
$$

This means the Erlang CDF can be expressed in terms of the Poisson PMF. The duality converts between a continuous waiting-time question and a discrete counting question, and whichever form is more convenient can be used.

### Intuition for the Mean

The expected time to the $k$-th arrival is $E[S_k] = k/\lambda$, which is simply $k$ times the expected interarrival time $1/\lambda$. This is intuitive: on average, each event adds $1/\lambda$ to the total waiting time.

### The Inspection Paradox

Consider a Poisson process with rate $\lambda$ that has been running indefinitely. Pick any **fixed** time point and let $\tau$ be the length of the interarrival interval containing that point.

**Surprising result:** Each individual interarrival time $T_i \sim \text{Exp}(\lambda)$ has mean $1/\lambda$, but the interval you land in satisfies $\tau \sim \Gamma(2, \lambda)$ with mean $2/\lambda$. The selected interval is, on average, **twice** as long as a typical interarrival time.

**Why this happens.** The fixed point splits $\tau$ into two parts:

- **Backward recurrence time** $B$: time since the last arrival before the fixed point
- **Forward recurrence time** $F$: time from the fixed point to the next arrival

By the memoryless property and time-reversibility of the Poisson process, $B \sim \text{Exp}(\lambda)$ and $F \sim \text{Exp}(\lambda)$ independently. Therefore

$$
\tau = B + F \sim \Gamma(2, \lambda)
$$

$$
E[\tau] = \frac{2}{\lambda}
$$

This is an instance of **length-biased sampling**: you are more likely to land in a longer interval than a shorter one, because longer intervals occupy more of the time axis. The probability of landing in a particular interval is proportional to its length, which biases the observed interval upward.

### Everyday Examples of the Inspection Paradox

- **Bus waiting.** If buses arrive as a Poisson process with rate $\lambda$, your expected wait is $1/\lambda$ (the full mean interarrival time), not $1/(2\lambda)$
- **Class sizes.** If you randomly pick a student and ask their class size, the average answer exceeds the overall average class size, because larger classes contain more students to sample
- **Family sizes.** Randomly picking a child and asking about their number of siblings gives a biased-upward answer

## Examples

**Example 1.** Calls arrive at a call center at rate $\lambda = 10$ per hour. Find the probability that the 5th call arrives within the first 30 minutes.

$S_5 \sim \Gamma(5, 10)$. We need $P(S_5 \leq 0.5)$. Using the Poisson-Gamma duality with $\lambda t = 10 \times 0.5 = 5$:

$$
P(S_5 \leq 0.5) = P(N(0.5) \geq 5) = 1 - \sum_{j=0}^{4} \frac{5^j}{j!} e^{-5}
$$

**Example 2.** Simulate the inspection paradox and verify the $k$-th arrival distribution.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
lam = 10.0
n_sim = 200_000

# --- k-th arrival time ---
# P(S_5 <= 0.5) from Example 1
k, t = 5, 0.5
lam_t = lam * t  # = 5.0

# Method 1: Poisson tail
poisson_prob = 1 - sum(
    lam_t**j / np.math.factorial(j) * np.exp(-lam_t)
    for j in range(k)
)

# Method 2: Gamma CDF via scipy
gamma_prob = stats.gamma.cdf(t, a=k, scale=1/lam)

# Method 3: Simulation
arrivals = np.random.exponential(1/lam, size=(n_sim, k)).sum(axis=1)
sim_prob = np.mean(arrivals <= t)

print("=== k-th Arrival: P(S_5 <= 0.5) ===")
print(f"  Poisson formula: {poisson_prob:.6f}")
print(f"  Gamma CDF:       {gamma_prob:.6f}")
print(f"  Simulation:      {sim_prob:.6f}")

# --- Inspection paradox ---
lam_insp = 2.0

# Simulate a Poisson process and find interval containing fixed point
fixed_point = 50.0
tau_samples = []
for _ in range(n_sim):
    interarrivals = np.random.exponential(1/lam_insp, 200)
    arrival_times = np.cumsum(interarrivals)
    idx = np.searchsorted(arrival_times, fixed_point)
    if idx > 0 and idx < len(arrival_times):
        tau_samples.append(interarrivals[idx])

tau_samples = np.array(tau_samples)
regular = np.random.exponential(1/lam_insp, n_sim)

print(f"\n=== Inspection Paradox (lam={lam_insp}) ===")
print(f"  Regular E[T_i]: {np.mean(regular):.4f}  (theory {1/lam_insp:.4f})")
print(f"  Containing E[tau]: {np.mean(tau_samples):.4f}  "
      f"(theory {2/lam_insp:.4f})")
print(f"  Ratio E[tau]/E[T]: {np.mean(tau_samples)/np.mean(regular):.4f}  "
      f"(theory 2.0)")
```
