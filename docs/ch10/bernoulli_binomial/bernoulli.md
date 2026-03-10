# Bernoulli Distribution

The Bernoulli distribution models a single trial with two outcomes — the atom from which many discrete distributions are built.

## Definition

$X \sim \text{Bern}(p)$ if $X$ takes values 0 and 1 with

$$
P(X = 1) = p, \qquad P(X = 0) = 1 - p = q
$$

**Moments:**

$$
E[X] = p, \qquad \text{Var}(X) = p(1-p) = pq
$$

**MGF:**

$$
M_X(t) = q + pe^t
$$

## Explanation

### As an Indicator

A Bernoulli random variable is an indicator: $X = \mathbf{1}_A$ where $A$ is the event of "success." This makes Bernoulli variables the building blocks of counting — any count of successes is a sum of Bernoulli indicators.

### Variance as a Function of $p$

The variance $pq = p(1-p)$ is maximized at $p = 1/2$ (most uncertain) and equals zero at $p = 0$ or $p = 1$ (deterministic). The graph of $pq$ vs $p$ is a downward parabola.

### Key Properties

- $X^2 = X$ (since $0^2 = 0$ and $1^2 = 1$), which gives the shortcut $E[X^2] = E[X] = p$
- $E[X^k] = p$ for all $k \ge 1$ (all moments equal $p$)
- $1 - X \sim \text{Bern}(q)$ (swapping success and failure)

## Examples

**Example.** A fair coin: $X \sim \text{Bern}(1/2)$. Then $E[X] = 0.5$, $\text{Var}(X) = 0.25$.

A biased detector with 90% sensitivity: $X \sim \text{Bern}(0.9)$. Then $\text{Var}(X) = 0.09$.

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

for p in [0.1, 0.3, 0.5, 0.7, 0.9]:
    X = np.random.binomial(1, p, n_sim)
    print(f"p={p}: E[X]={X.mean():.4f} (theory: {p}), "
          f"Var={X.var():.4f} (theory: {p*(1-p):.4f})")
```
