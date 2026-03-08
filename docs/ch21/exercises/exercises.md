# Exercises: Simulation

## Exercise 1: Estimating e via Simulation

Let $U_1, U_2, \ldots$ be iid $\text{Uniform}(0, 1)$. Define $N = \min\{n : U_1 + U_2 + \cdots + U_n > 1\}$. It is known that $E[N] = e$.

**(a)** Write a simulation to estimate $E[N]$ using $10{,}000$ trials.

**(b)** Report your estimate and its standard error. Compare with $e \approx 2.71828$.

**(c)** Plot the running estimate $\hat{e}_k = \frac{1}{k}\sum_{i=1}^{k} N_i$ as a function of $k$.

## Exercise 2: Rejection Sampling

The **rejection method** generates samples from a target density $f(x)$ using a proposal density $g(x)$ and constant $M$ such that $f(x) \leq Mg(x)$ for all $x$.

**(a)** Implement rejection sampling to generate samples from $f(x) = \frac{3}{2}(1 - x^2)$ on $[-1, 1]$ using $g(x) = \frac{1}{2}$ (uniform on $[-1,1]$). What is the optimal $M$?

**(b)** Generate $10{,}000$ samples and plot a histogram against the true density.

**(c)** What fraction of proposals are accepted? Compare with $1/M$.

## Exercise 3: Birthday Problem Simulation

**(a)** Write a simulation to estimate $P(\text{at least two people share a birthday})$ for group sizes $n = 2, 3, \ldots, 60$. Use $10{,}000$ trials per group size. (Assume 365 equally likely birthdays.)

**(b)** Plot simulated probabilities against the exact formula. At what $n$ does the probability first exceed 0.5?

**(c)** Modify the simulation for the "triple birthday problem": $P(\text{at least three share a birthday})$. Plot for $n = 2, \ldots, 100$.

## Exercise 4: Gambler's Ruin Duration

In the Gambler's Ruin with initial fortune $i$, target $N$, and $P(\text{win}) = p$:

**(a)** For $p = 0.5$, $i = 5$, $N = 10$: simulate $10{,}000$ games and estimate the expected duration $E[D]$. Compare with the theoretical value $E[D] = i(N - i) = 25$.

**(b)** For $p = 0.4$, estimate $E[D]$ by simulation. Plot the histogram of game durations.

**(c)** How does $E[D]$ depend on $N$ (fixing $i = N/2$, $p = 0.5$)? Plot $E[D]$ vs $N$ for $N = 4, 6, \ldots, 50$.

## Exercise 5: Buffon's Needle (Extended)

**(a)** Simulate Buffon's needle experiment: a needle of length $\ell$ is dropped on parallel lines with spacing $d \geq \ell$. The probability of crossing a line is $\frac{2\ell}{\pi d}$. Use this to estimate $\pi$ from $100{,}000$ drops with $\ell = d = 1$.

**(b)** Plot the running estimate of $\pi$ as a function of the number of drops.

**(c)** Compare the convergence rate (standard error vs $n$) with the circle-area method from Section 21.2.

## Exercise 6: Random Walk Properties

**(a)** Simulate a 1D simple random walk $S_n = \sum_{i=1}^n X_i$ where $P(X_i = 1) = P(X_i = -1) = 1/2$, for $n = 10{,}000$ steps. Plot 5 sample paths.

**(b)** For each path, compute the fraction of time $S_n > 0$. Repeat for $1{,}000$ paths and plot a histogram. What is the distribution? (This is related to the arcsine law.)

**(c)** Estimate $P(S_n = 0 \text{ for some } n > 100 \mid S_{100} = 0)$. (Hint: condition on $S_{100} = 0$ and continue the walk.)

## Exercise 7: Inverse CDF Method

**(a)** Use the inverse CDF method to generate samples from the distribution with CDF $F(x) = 1 - e^{-x^2}$ for $x \geq 0$.

**(b)** Generate $10{,}000$ samples and verify the mean and variance via simulation. Find $E[X]$ and $\text{Var}(X)$ numerically.

**(c)** Plot the histogram against the true PDF $f(x) = 2xe^{-x^2}$.

## Exercise 8: Markov Chain Monte Carlo (Preview)

The **Metropolis algorithm** generates samples from a distribution by proposing random moves and accepting/rejecting them.

**(a)** Implement the Metropolis algorithm to sample from $f(x) \propto e^{-|x|^3}$ on $\mathbb{R}$, using $N(x_{\text{current}}, \sigma^2)$ proposals.

**(b)** Generate a chain of length $50{,}000$. Plot the trace plot and histogram.

**(c)** Experiment with $\sigma = 0.1, 1, 5$. How does the proposal scale affect mixing?

## Solutions

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

# ===== Exercise 1 =====
def estimate_e(n_trials=10000):
    Ns = []
    for _ in range(n_trials):
        total, n = 0, 0
        while total <= 1:
            total += np.random.uniform()
            n += 1
        Ns.append(n)
    return np.array(Ns)

Ns = estimate_e()
print(f"Ex1: E[N] ≈ {np.mean(Ns):.5f} (true e = {np.e:.5f})")
print(f"     SE = {np.std(Ns)/np.sqrt(len(Ns)):.5f}")

# ===== Exercise 2 =====
def rejection_sampling(n_samples=10000):
    M = 3  # max of f(x)/g(x): max of (3/2)(1-x^2)/(1/2) = 3 at x=0
    samples = []
    n_proposed = 0
    while len(samples) < n_samples:
        x = np.random.uniform(-1, 1)
        u = np.random.uniform()
        fx = 1.5 * (1 - x**2)
        gx = 0.5
        if u <= fx / (M * gx):
            samples.append(x)
        n_proposed += 1
    acceptance_rate = n_samples / n_proposed
    return np.array(samples), acceptance_rate

samples_rej, acc_rate = rejection_sampling()
print(f"\nEx2: Acceptance rate = {acc_rate:.4f} (theory 1/M = {1/3:.4f})")

# ===== Exercise 4 =====
def gamblers_ruin_duration(i, N, p, n_trials=10000):
    durations = []
    for _ in range(n_trials):
        fortune = i
        steps = 0
        while 0 < fortune < N:
            fortune += 1 if np.random.random() < p else -1
            steps += 1
        durations.append(steps)
    return np.array(durations)

durations = gamblers_ruin_duration(5, 10, 0.5)
print(f"\nEx4: E[D] ≈ {np.mean(durations):.1f} (theory = 25)")

# ===== Exercise 5 =====
def buffon_needle(n_drops=100000, ell=1, d=1):
    theta = np.random.uniform(0, np.pi, n_drops)
    x = np.random.uniform(0, d / 2, n_drops)
    crosses = x <= (ell / 2) * np.sin(theta)
    p_cross = np.cumsum(crosses) / np.arange(1, n_drops + 1)
    pi_est = (2 * ell) / (d * p_cross)
    return pi_est

pi_estimates = buffon_needle()
print(f"\nEx5: π estimate = {pi_estimates[-1]:.5f}")
```
