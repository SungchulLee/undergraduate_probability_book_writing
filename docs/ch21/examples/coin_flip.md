# Coin Flip Using Uniform Samples

## From Uniform to Bernoulli

One of the most fundamental simulation techniques is generating Bernoulli random variables from uniform random variables. Given $U \sim U(0,1)$ and a success probability $p \in [0,1]$, we define

$$
B = \begin{cases} 1 & \text{if } U > 1 - p \\ 0 & \text{if } U \leq 1 - p \end{cases}
$$

Then $B \sim \text{Bernoulli}(p)$, since $P(B = 1) = P(U > 1-p) = p$.

## Example

Generate 5 uniform samples $U_i$ from $[0,1]$ and convert them to Bernoulli samples $B_i$ with success rate $p = 0.499$.

**MATLAB:**

```matlab
clear all; close all; clc; rng('default')

n = 5; p = 0.499;

% n uniform samples
U = rand(1, n)

% n Bernoulli samples B(p)
B = U; B(U <= 1-p) = 0; B(U > 1-p) = 1
```

**Output:**

```
U =
    0.8147    0.9058    0.1270    0.9134    0.6324

B =
    1    1    0    1    1
```

Since $1 - p = 0.501$, only $U_3 = 0.1270$ falls below the threshold, so $B_3 = 0$ while the rest are 1.

**Python:**

```python
import numpy as np

np.random.seed(0)

n = 5
p = 0.499

# n uniform samples
U = np.random.rand(n)
print("U =", U)

# n Bernoulli samples
B = (U > 1 - p).astype(int)
print("B =", B)
```

## Why This Works

This technique is an instance of the **inverse transform method**. The CDF of a Bernoulli($p$) random variable is

$$
F(x) = \begin{cases} 0 & x < 0 \\ 1 - p & 0 \leq x < 1 \\ 1 & x \geq 1 \end{cases}
$$

Setting $B = \mathbf{1}(U > 1 - p)$ is equivalent to applying the generalized inverse of $F$ to $U$. This principle generalizes: any distribution can be sampled from a uniform random variable via its inverse CDF (see the Probability Integral Transform).
