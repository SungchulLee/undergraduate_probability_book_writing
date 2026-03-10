# Why Chi-Squared, t, and F Arise Naturally

When sampling from a normal population, replacing the unknown $\sigma$ with the sample standard deviation $S$ changes the sampling distribution from normal to something heavier-tailed. The chi-squared, Student's $t$, and $F$ distributions are the three distributions that emerge from this substitution.

## Definition

The three distributions derived from normal samples are built in sequence:

$$
\chi^2_d = \sum_{i=1}^d Z_i^2, \qquad t_d = \frac{Z}{\sqrt{\chi^2_d / d}}, \qquad F_{d_1,d_2} = \frac{\chi^2_{d_1}/d_1}{\chi^2_{d_2}/d_2}
$$

where all component random variables are independent and $Z, Z_i \sim N(0,1)$.

## Explanation

### Known versus unknown variance

For $X_1, \ldots, X_n$ iid from $N(\mu, \sigma^2)$, when $\sigma$ is known the standardized mean is standard normal:

$$
\frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0, 1)
$$

When $\sigma$ is unknown, replacing it with $S$ gives a ratio whose distribution depends on the random denominator:

$$
\frac{\bar{X} - \mu}{S / \sqrt{n}} \sim t_{n-1}
$$

### The logical chain

Each distribution builds on the previous one:

- **Chi-squared** captures the distribution of sums of squared standard normals, governing $S^2$.
- **Student's $t$** arises as the ratio of a standard normal to $\sqrt{\chi^2/d}$, governing the studentized mean.
- **$F$** arises as the ratio of two independent chi-squared variables (each divided by their degrees of freedom), governing comparisons of variances.

### Techniques for deriving PDFs

The derivations in this chapter rely on two transformation methods. The **CDF method** computes $P(Y \le y)$ and differentiates. The **Jacobian method** uses the change-of-variables formula for densities:

$$
f_Y(y) = f_X\!\bigl(g^{-1}(y)\bigr) \left|\frac{dx}{dy}\right|
$$

## Examples

**Example 1.** Verify the CDF and Jacobian methods agree for $Y = X^3$ where $X \sim U(0,1)$.

```python
import numpy as np

np.random.seed(42)
x = np.random.uniform(0, 1, 500_000)
y = x**3

# Theoretical PDF: f_Y(y) = (1/3) y^{-2/3} for 0 < y < 1
# Check P(Y <= 0.5) = 0.5^{1/3}
empirical = np.mean(y <= 0.5)
theory = 0.5 ** (1/3)
print(f"P(Y <= 0.5): simulated={empirical:.4f}, theory={theory:.4f}")
```
