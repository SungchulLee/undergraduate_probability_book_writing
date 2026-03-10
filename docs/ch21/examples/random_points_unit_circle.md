# Random Points and the Unit Circle

Uniform random points in the square, classified by whether they fall inside the unit circle, provide a visual introduction to Monte Carlo estimation of $\pi$.

## Definition

Generate $(X_i, Y_i)$ uniformly in $[-1,1]^2$. The point is inside the unit circle iff $X_i^2 + Y_i^2 \le 1$. The fraction inside estimates:

$$
\frac{\text{Area of circle}}{\text{Area of square}} = \frac{\pi}{4}
$$

So $\hat{\pi} = 4 \times \frac{\text{points inside}}{n}$.

## Explanation

### Why It Works

Each $(X_i, Y_i)$ is iid $U([-1,1]^2)$. Letting $R_i = \mathbf{1}(X_i^2 + Y_i^2 \le 1)$, we have $E[R_i] = \pi/4$. By the SLLN, $\bar{R}_n \xrightarrow{a.s.} \pi/4$.

### Convergence Rate

The standard error is $\sqrt{\operatorname{Var}(R_1)/n} = \sqrt{(\pi/4)(1 - \pi/4)/n} \approx 0.42/\sqrt{n}$. With $n = 10{,}000$, the SE is about 0.004, giving roughly one decimal of $\pi$.

## Examples

**Example.** Estimate $\pi$ with 100,000 random points.

```python
import numpy as np

np.random.seed(42)
n = 100_000

X = np.random.uniform(-1, 1, n)
Y = np.random.uniform(-1, 1, n)
inside = (X**2 + Y**2) <= 1

pi_hat = 4 * inside.mean()
print(f"Points inside: {inside.sum()} / {n}")
print(f"π estimate: {pi_hat:.6f} (true: {np.pi:.6f})")
print(f"Error: {abs(pi_hat - np.pi):.6f}")
```
