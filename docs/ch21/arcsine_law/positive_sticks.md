# Arcsine Law — Number of Positive Sticks

## Statement

Starting from the origin, run a simple random walk $S_0 = 0, S_1, S_2, \ldots, S_{2n}$ up to time $2n$ on $\mathbb{Z}$. A **stick** is a segment $(k-1, S_{k-1}) \to (k, S_k)$. A stick is **positive** if its center lies above the $x$-axis, i.e., if

$$
\frac{S_{k-1} + S_k}{2} > 0
$$

Let $N_{2n}$ be the number of positive sticks. Then, for $0 \leq a < b \leq 1$,

$$
P\!\left(a \leq \frac{N_{2n}}{2n} \leq b\right) \to \int_a^b \frac{1}{\pi} \cdot \frac{1}{\sqrt{x(1-x)}} \, dx = \frac{2}{\pi}\left[\arcsin(\sqrt{b}) - \arcsin(\sqrt{a})\right]
$$

## Interpretation

The fraction of time the random walk spends on the positive side follows the same arcsine distribution as the last visit time. This means:

- The walk does **not** spend roughly half its time above and half below zero.
- Instead, it is most likely to spend nearly all its time on one side or the other.
- Spending exactly 50% of the time positive is actually the *least likely* outcome.

## Simulation

**MATLAB:**

```matlab
%% Number of positive sticks
clear all; close all; clc; rng('default')

% Parameters
p = 0.5; n = 10000;       % We flip a fair coin n times
NumSimu = 1000;            % We do this experiment NumSimu times
x = random('Binomial', 1*ones(NumSimu, n), p*ones(NumSimu, n));
x = 2*x - 1;

Number_of_Positive_Sticks = zeros(NumSimu, 1);
for NumS = 1:NumSimu
    Sn = cumsum(x(NumS, :));
    Random_Walk = [0 Sn];
    Center_of_Stick = (Random_Walk(1:end-1) + Random_Walk(2:end)) / 2;
    Positive_Side_Sticks = find(Center_of_Stick > 0);
    Number_of_Positive_Sticks(NumS, 1) = length(Positive_Side_Sticks);
end

hist(Number_of_Positive_Sticks)
```

**Python:**

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

p = 0.5
n = 10000
num_simu = 1000

x = 2 * np.random.binomial(1, p, size=(num_simu, n)) - 1

num_positive_sticks = np.zeros(num_simu)
for s in range(num_simu):
    walk = np.concatenate([[0], np.cumsum(x[s, :])])
    centers = (walk[:-1] + walk[1:]) / 2
    num_positive_sticks[s] = np.sum(centers > 0)

plt.figure()
plt.hist(num_positive_sticks, bins=20, edgecolor='black')
plt.xlabel('Number of Positive Sticks')
plt.ylabel('Frequency')
plt.title(f'Arcsine Law: Positive sticks ({num_simu} simulations of {n} steps)')
plt.show()
```

## Observations

The histogram again shows the characteristic $U$-shaped arcsine distribution. The walk tends to spend most of its time either predominantly positive or predominantly negative, rather than splitting evenly.

## The Three Arcsine Laws

The classical arcsine laws for the symmetric random walk state that all three quantities share the same arcsine distribution:

1. **Last visit time** $L_{2n}/(2n)$ — the last time the walk returns to zero
2. **Fraction of time positive** $N_{2n}/(2n)$ — the proportion of sticks above zero
3. **Time of the maximum** — the time at which the walk achieves its maximum value

These results, due to Paul Lévy, are among the most beautiful and surprising in probability theory.
