# Samples from Normal Distributions


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Generating Normal Samples

To generate samples from $N(\mu, \sigma^2)$, we use the standard transformation: if $Z \sim N(0,1)$, then

$$
X = \mu + \sigma Z \sim N(\mu, \sigma^2)
$$

In MATLAB, `randn(1, n)` generates $n$ standard normal samples, so `mu + sigma * randn(1, n)` generates samples from $N(\mu, \sigma^2)$.

## Example: Mixture of Two Normals

Generate 600 samples from $N(1, 1)$ and 400 samples from $N(4, 1)$, then combine them into a single dataset of 1000 samples.

**MATLAB:**

```matlab
clear all; close all; clc; rng('default')

% n1 samples from N(mu1, si1)
n1 = 600;
mu1 = 1; si1 = 1;
x1 = mu1 + si1 * randn(1, n1);
subplot(131)
hist(x1)

% n2 samples from N(mu2, si2)
n2 = 400;
mu2 = 4; si2 = 1;
x2 = mu2 + si1 * randn(1, n2);
subplot(132)
hist(x2)

% Samples from two different normal distributions
x = [x1 x2];
subplot(133)
hist(x)
```

**Python:**

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# 600 samples from N(1, 1)
n1 = 600; mu1 = 1; si1 = 1
x1 = mu1 + si1 * np.random.randn(n1)

# 400 samples from N(4, 1)
n2 = 400; mu2 = 4; si2 = 1
x2 = mu2 + si2 * np.random.randn(n2)

# Combined samples
x = np.concatenate([x1, x2])

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

axes[0].hist(x1, bins=20, edgecolor='black')
axes[0].set_title(f'600 samples from $N({mu1}, {si1}^2)$')

axes[1].hist(x2, bins=20, edgecolor='black')
axes[1].set_title(f'400 samples from $N({mu2}, {si2}^2)$')

axes[2].hist(x, bins=20, edgecolor='black')
axes[2].set_title('Combined 1000 samples')

plt.tight_layout()
plt.show()
```

## Mixture Distributions

The combined histogram is an example of a **mixture distribution**. The density of the mixture is

$$
f(x) = w_1 \, f_1(x) + w_2 \, f_2(x)
$$

where $w_1 = \frac{n_1}{n_1 + n_2} = 0.6$, $w_2 = 0.4$, and $f_i$ is the density of $N(\mu_i, \sigma_i^2)$.

The resulting histogram shows a bimodal shape — a characteristic signature of mixture distributions when the component means are sufficiently separated relative to their standard deviations.
