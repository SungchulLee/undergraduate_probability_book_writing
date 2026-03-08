# 2D Simple Random Walk

## Definition

A **2D simple random walk** starts at the origin $(0, 0)$ and at each step moves to one of the four neighboring lattice points — right, left, up, or down — each with probability $\frac{1}{4}$.

At step $k$, the increment $(X_k, Y_k)$ is chosen uniformly from $\{(1,0), (-1,0), (0,1), (0,-1)\}$, and the position after $m$ steps is

$$
(S_m^x, S_m^y) = \sum_{k=1}^{m} (X_k, Y_k)
$$

## Simulation

The idea is to use a single uniform random variable to determine the direction at each step. We partition $[0,1)$ into four equal subintervals:

- $[0, 0.25)$: move right $(+1, 0)$
- $[0.25, 0.5)$: move left $(-1, 0)$
- $[0.5, 0.75)$: move up $(0, +1)$
- $[0.75, 1)$: move down $(0, -1)$

**MATLAB:**

```matlab
clear all; close all; clc; rng('default')

m = 100;
coin = rand(m, 1);

increment = zeros(m, 2);
increment(coin < 0.25, 1) = 1;   increment(coin < 0.25, 2) = 0;
increment(0.25 <= coin & coin < 0.5, 1) = -1;  increment(0.25 <= coin & coin < 0.5, 2) = 0;
increment(0.5 <= coin & coin < 0.75, 1) = 0;   increment(0.5 <= coin & coin < 0.75, 2) = 1;
increment(0.75 < coin, 1) = 0;   increment(0.75 < coin, 2) = -1;

walk = cumsum(increment);
walk = [0 0; walk];
r = max(max(abs(walk))) + 1;

plot(0, 0, 'or'); grid on; hold on;
axis([-r r -r r])
for k = 1:m
    plot([walk(k,1) walk(k+1,1)], [walk(k,2) walk(k+1,2)], '-r')
    pause(0.1)
end
```

**Python:**

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

m = 100
directions = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
choices = np.random.randint(0, 4, size=m)
increments = directions[choices]

walk = np.vstack([[0, 0], np.cumsum(increments, axis=0)])

plt.figure(figsize=(6, 6))
plt.plot(walk[:, 0], walk[:, 1], '-r', linewidth=0.8)
plt.plot(0, 0, 'or', markersize=8)
plt.grid(True)
plt.axis('equal')
plt.title('2D Simple Random Walk (100 steps)')
plt.show()
```

## Properties

The 2D simple random walk is **recurrent**: it returns to the origin with probability 1 (Pólya's theorem, 1921). However, the expected number of steps to return is infinite.

This is in contrast to the 3D simple random walk, which is **transient** — the probability of ever returning to the origin is approximately 0.3405.
