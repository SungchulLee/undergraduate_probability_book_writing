# $E(X \mid Y)$ as a Random Variable

## The Local Average Interpretation

$E(X \mid Y)$ can be understood as a **local average** of $X$. For each value $y$ that $Y$ takes, $E(X \mid Y = y)$ averages $X$ over only those outcomes where $Y = y$. As $Y$ varies across its range, these local averages trace out a random variable.

## Coin Flip Example

Consider three fair coin flips. Let $X$ be the total number of heads and $Y$ be the indicator of getting a head on the first flip ($Y = 1$ if the first flip is H, $Y = 0$ otherwise).

The sample space is $\{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}$, each with probability $1/8$.

**Values of $X$** (number of heads) for each outcome:

| Outcome | HHH | HHT | HTH | HTT | THH | THT | TTH | TTT |
|:--------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $X$     |  3  |  2  |  2  |  1  |  2  |  1  |  1  |  0  |

**Computing $E(X \mid Y)$:**

When $Y = 1$ (first flip is H): the outcomes are $\{HHH, HHT, HTH, HTT\}$, so $E(X \mid Y = 1) = \frac{3 + 2 + 2 + 1}{4} = 2$.

When $Y = 0$ (first flip is T): the outcomes are $\{THH, THT, TTH, TTT\}$, so $E(X \mid Y = 0) = \frac{2 + 1 + 1 + 0}{4} = 1$.

Therefore:

$$
E(X \mid Y) = \begin{cases} 2 & \text{with probability } 1/2 \\ 1 & \text{with probability } 1/2 \end{cases}
$$

The red bars in the figure show $E(X \mid Y)$ for each outcome — outcomes with the same $Y$ value get the same conditional expectation. This is the "local average" at work: $E(X \mid Y)$ smooths out $X$ within each group defined by $Y$.

## Properties as a Random Variable

Since $E(X \mid Y)$ is a random variable, it has its own expectation and variance:

$$
E\bigl[E(X \mid Y)\bigr] = E(X) \qquad \text{(Law of Total Expectation)}
$$

$$
\text{Var}\bigl(E(X \mid Y)\bigr) \leq \text{Var}(X) \qquad \text{(Conditioning reduces variance)}
$$

These are explored in detail in the next sections.

## Python Simulation

```python
import numpy as np

np.random.seed(42)
n_sim = 100_000

# Three fair coin flips
flips = np.random.randint(0, 2, size=(n_sim, 3))
X = flips.sum(axis=1)          # total heads
Y = flips[:, 0]                # first flip indicator

# Conditional expectations
E_X_given_Y1 = X[Y == 1].mean()
E_X_given_Y0 = X[Y == 0].mean()

print(f"E(X | Y=1) = {E_X_given_Y1:.4f}  (theory: 2.0)")
print(f"E(X | Y=0) = {E_X_given_Y0:.4f}  (theory: 1.0)")

# Verify law of total expectation
E_X = X.mean()
E_EXY = 0.5 * E_X_given_Y1 + 0.5 * E_X_given_Y0
print(f"\nE(X) = {E_X:.4f}")
print(f"E[E(X|Y)] = {E_EXY:.4f}  (should match E(X))")
```
