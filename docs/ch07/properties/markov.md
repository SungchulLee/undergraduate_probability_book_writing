# Markov's Inequality

Markov's inequality bounds the tail probability of a non-negative random variable using only its mean — the simplest concentration inequality.

## Definition

If $X \ge 0$ and $a > 0$, then

$$
P(X \ge a) \le \frac{E[X]}{a}
$$

## Explanation

### Proof

$$
E[X] = \int_0^{\infty} x\,f(x)\,dx \ge \int_a^{\infty} x\,f(x)\,dx \ge a\int_a^{\infty} f(x)\,dx = a\,P(X \ge a)
$$

### Strengths and Weaknesses

The bound requires only the mean — no variance, no distributional shape. But it is often very loose. It becomes the foundation for stronger bounds: Chebyshev's inequality applies Markov to $(X - \mu)^2$, and Chernoff bounds apply it to $e^{tX}$.

## Examples

**Example.** $X \sim \text{Exp}(1)$, so $E[X] = 1$. Markov gives $P(X \ge 3) \le 1/3$. The exact value is $e^{-3} \approx 0.05$.

```python
import numpy as np

np.random.seed(42)
X = np.random.exponential(1, 1_000_000)

for a in [2, 3, 5]:
    bound = 1 / a
    actual = np.mean(X >= a)
    print(f"P(X >= {a}): Markov <= {bound:.4f}, actual = {actual:.4f}")
```
