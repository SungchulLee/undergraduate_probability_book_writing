# Conditional Expectation Given a Random Variable

Letting $y$ vary over all values of $Y$ turns the number $E[X \mid Y = y]$ into a random variable $E[X \mid Y]$ — a function of $Y$.

## Definition

Define $g(y) = E[X \mid Y = y]$. The **conditional expectation of $X$ given $Y$** is the random variable

$$
E[X \mid Y] = g(Y)
$$

Formally, $E[X \mid Y](\omega) = E[X \mid Y = Y(\omega)]$.

When $Y$ is discrete with values $y_1, y_2, \ldots$:

$$
E[X \mid Y] = \begin{cases}
E[X \mid Y = y_1] & \text{if } Y = y_1 \\
E[X \mid Y = y_2] & \text{if } Y = y_2 \\
\vdots
\end{cases}
$$

## Explanation

### From Number to Random Variable

The chain $\omega \to Y(\omega) = y \to E[X \mid Y = y]$ shows how the randomness of $E[X \mid Y]$ is inherited entirely from $Y$. Once $Y$ is observed, $E[X \mid Y]$ becomes a known number.

### Key Properties

All the following hold as identities between random variables:

1. **Linearity:** $E[aX + bZ \mid Y] = a\,E[X \mid Y] + b\,E[Z \mid Y]$
2. **Known values pull out:** $E[h(Y) \mid Y] = h(Y)$
3. **Factoring out known:** $E[h(Y) \cdot X \mid Y] = h(Y) \cdot E[X \mid Y]$
4. **Independence:** If $X \perp Y$, then $E[X \mid Y] = E[X]$ (a constant)

Properties (2) and (3) express the idea that conditioning on $Y$ makes any function of $Y$ behave like a constant.

### Variance Version

Similarly, $\text{Var}(X \mid Y)$ is the random variable obtained by evaluating $\text{Var}(X \mid Y = y)$ at $Y$:

$$
\text{Var}(X \mid Y) = E[X^2 \mid Y] - (E[X \mid Y])^2
$$

## Examples

**Example.** Three fair coin flips. $X$ = total heads, $Y$ = indicator of head on first flip.

- $E[X \mid Y = 1] = (3 + 2 + 2 + 1)/4 = 2$
- $E[X \mid Y = 0] = (2 + 1 + 1 + 0)/4 = 1$

So $E[X \mid Y] = Y + 1$, taking value 2 or 1 each with probability $1/2$.

```python
import numpy as np

np.random.seed(42)
n_sim = 100_000

flips = np.random.randint(0, 2, size=(n_sim, 3))
X = flips.sum(axis=1)
Y = flips[:, 0]

E_X_given_Y1 = X[Y == 1].mean()
E_X_given_Y0 = X[Y == 0].mean()

print(f"E[X | Y=1] = {E_X_given_Y1:.4f}  (theory: 2.0)")
print(f"E[X | Y=0] = {E_X_given_Y0:.4f}  (theory: 1.0)")

# Verify E[E[X|Y]] = E[X]
E_X = X.mean()
E_EXY = 0.5 * E_X_given_Y1 + 0.5 * E_X_given_Y0
print(f"\nE[X] = {E_X:.4f}")
print(f"E[E[X|Y]] = {E_EXY:.4f}  (should match)")
```
