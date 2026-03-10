# Longest Run


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Problem Statement

If one flips a fair coin $n$ times, what is the probability distribution of the **longest run** — the length of the longest sequence of consecutive heads (or tails)?

This is a classic problem in probability that is difficult to solve analytically but easy to explore via simulation.

## Theoretical Background

For a fair coin flipped $n$ times, the expected length of the longest run is approximately

$$
E[\text{Longest Run}] \approx \log_2 n
$$

More precisely, the longest run $R_n$ satisfies

$$
\frac{R_n}{\log_2 n} \to 1 \quad \text{in probability as } n \to \infty
$$

For $n = 10{,}000$, we expect $\log_2(10{,}000) \approx 13.3$, consistent with the simulation histogram centered around 13–15.

## Simulation

We flip a fair coin $n = 10{,}000$ times and record the longest run. We repeat this experiment 1000 times to build a histogram.

**MATLAB:**

```matlab
clear all; close all; clc; rng('default')

p = 0.5; n = 10000;       % We flip a fair coin n times
NumSimu = 1000;            % We do this experiment NumSimu times
x = random('Binomial', 1*ones(NumSimu, n), p*ones(NumSimu, n));

Run = zeros(NumSimu, 1);
for NumS = 1:NumSimu
    Current_Run = 1;
    Overall_Run = 1;
    for i = 2:n
        if x(NumS, i) == x(NumS, i-1)
            Current_Run = Current_Run + 1;
            Overall_Run = max(Current_Run, Overall_Run);
        else
            Current_Run = 1;
        end
    end
    Run(NumS, 1) = Overall_Run;
end

hist(Run)
```

**Python:**

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

p = 0.5
n = 10000
num_simu = 1000

x = np.random.binomial(1, p, size=(num_simu, n))

runs = np.zeros(num_simu)
for s in range(num_simu):
    current_run = 1
    overall_run = 1
    for i in range(1, n):
        if x[s, i] == x[s, i-1]:
            current_run += 1
            overall_run = max(current_run, overall_run)
        else:
            current_run = 1
    runs[s] = overall_run

plt.figure()
plt.hist(runs, bins=range(int(runs.min()), int(runs.max()) + 2),
         edgecolor='black', align='left')
plt.xlabel('Longest Run Length')
plt.ylabel('Frequency')
plt.title(f'Histogram of longest run in {n} coin flips ({num_simu} simulations)')
plt.show()

print(f"Mean longest run: {runs.mean():.2f}")
print(f"Theoretical approximation (log2 n): {np.log2(n):.2f}")
```

## Observations

The histogram of 1000 simulations shows that the longest run in 10,000 fair coin flips typically falls between 10 and 22, with the distribution concentrated around 13–16. This is remarkably consistent with the $\log_2 n$ approximation.

This result has practical implications: people tend to underestimate how long runs can naturally occur in random sequences, which is why truly random sequences often "look" less random than people expect.
