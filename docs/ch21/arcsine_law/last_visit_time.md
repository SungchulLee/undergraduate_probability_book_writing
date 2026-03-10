# Arcsine Law — Last Visit Time


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Statement

Starting from the origin, run a simple random walk $S_0 = 0, S_1, S_2, \ldots, S_{2n}$ up to time $2n$ on $\mathbb{Z}$. Let $L_{2n}$ be the **last visit time to the origin**, i.e., the last time the walk returns to zero.

Then, for $0 \leq a < b \leq 1$,

$$
P\!\left(a \leq \frac{L_{2n}}{2n} \leq b\right) \to \int_a^b \frac{1}{\pi} \cdot \frac{1}{\sqrt{x(1-x)}} \, dx = \frac{2}{\pi}\left[\arcsin(\sqrt{b}) - \arcsin(\sqrt{a})\right]
$$

as $n \to \infty$.

## The Arcsine Distribution

The limiting density

$$
f(x) = \frac{1}{\pi \sqrt{x(1-x)}}, \quad 0 < x < 1
$$

is called the **arcsine distribution**. Its CDF is

$$
F(x) = \frac{2}{\pi} \arcsin(\sqrt{x})
$$

This distribution is $U$-shaped: it assigns the most probability mass near $x = 0$ and $x = 1$. This means the random walk's last visit to zero is most likely to occur either very early or very late — not in the middle.

## Intuition

The arcsine law is counterintuitive. One might expect the walk to visit zero "evenly" throughout its duration, but in fact the opposite is true. The walk tends to stay on one side of zero for long stretches, and the last time it touches zero is typically near the beginning or end of the walk.

## Simulation

**MATLAB:**

```matlab
clear all; close all; clc; rng('default')

% Parameters
p = 0.5; n = 10000;       % We flip a fair coin n times
NumSimu = 1000;            % We do this experiment NumSimu times
x = random('Binomial', 1*ones(NumSimu, n), p*ones(NumSimu, n));
x = 2*x - 1;              % Convert to +1/-1 steps

Last_Visit_Time = zeros(NumSimu, 1);
for NumS = 1:NumSimu
    Sn = cumsum(x(NumS, :));
    Random_Walk = [0 Sn];
    Last_Visit_Time(NumS, 1) = find(Random_Walk == 0, 1, 'last') - 1;
end

hist(Last_Visit_Time)
```

**Python:**

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

p = 0.5
n = 10000
num_simu = 1000

# Generate +1/-1 steps
x = 2 * np.random.binomial(1, p, size=(num_simu, n)) - 1

last_visit_time = np.zeros(num_simu)
for s in range(num_simu):
    walk = np.concatenate([[0], np.cumsum(x[s, :])])
    zeros = np.where(walk == 0)[0]
    last_visit_time[s] = zeros[-1]

plt.figure()
plt.hist(last_visit_time, bins=20, edgecolor='black')
plt.xlabel('Last Visit Time to Origin')
plt.ylabel('Frequency')
plt.title(f'Arcsine Law: Last visit time ({num_simu} simulations of {n} steps)')
plt.show()
```

## Observations

The histogram shows a clear $U$-shaped distribution: the last visit to zero clusters near the endpoints (time 0 and time $n$), with relatively few visits in the middle. This matches the arcsine density perfectly.

This is one of three classical arcsine laws for random walks, alongside the fraction of time spent positive (see next section) and the time of the maximum.
