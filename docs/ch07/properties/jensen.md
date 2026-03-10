# Jensen's Inequality

Jensen's inequality relates the expectation of a function to the function of the expectation — the direction depends on convexity.

## Definition

If $g$ is **convex** and $E[X]$, $E[g(X)]$ are finite:

$$
E[g(X)] \ge g(E[X])
$$

If $g$ is **concave**, the inequality reverses: $E[g(X)] \le g(E[X])$.

## Explanation

### Intuition

A convex function curves upward, so the average of function values exceeds the function value at the average. The chord connecting two points on a convex curve lies above the curve.

### Common Applications

| $g(x)$ | Convexity | Jensen |
|:--------|:----------|:-------|
| $x^2$ | Convex | $E[X^2] \ge (E[X])^2$ |
| $e^x$ | Convex | $E[e^X] \ge e^{E[X]}$ |
| $\|x\|$ | Convex | $E[\|X\|] \ge \|E[X]\|$ |
| $\ln x$ | Concave | $E[\ln X] \le \ln E[X]$ |

The first row implies $\text{Var}(X) \ge 0$. The last row gives: geometric mean $\le$ arithmetic mean.

## Examples

**Example.** $X \sim \text{Exp}(1)$. Jensen with $g(x) = x^2$ (convex):

$E[X^2] = 2 \ge 1 = (E[X])^2$.

Jensen with $g(x) = \ln x$ (concave):

$E[\ln X] = -\gamma \approx -0.577 \le 0 = \ln E[X]$ (where $\gamma$ is the Euler-Mascheroni constant).

```python
import numpy as np

np.random.seed(42)
X = np.random.exponential(1, 1_000_000)

print(f"E[X^2] = {np.mean(X**2):.4f} >= (E[X])^2 = {np.mean(X)**2:.4f}")
print(f"E[ln X] = {np.mean(np.log(X)):.4f} <= ln(E[X]) = {np.log(np.mean(X)):.4f}")
```
