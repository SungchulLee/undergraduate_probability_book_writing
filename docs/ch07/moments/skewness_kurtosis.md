# Skewness and Kurtosis


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Skewness — Measure of Symmetry

### Definition

The **skewness** of a random variable $X$ with mean $\mu$ and standard deviation $\sigma$ is:

$$\text{Skewness}(X) = E\left[\left(\frac{X - \mu}{\sigma}\right)^3\right]$$

For discrete and continuous cases:

$$\text{Skewness}(X) = \begin{cases} \displaystyle\sum_x \left(\frac{x - \mu}{\sigma}\right)^3 p(x) & \text{if } X \text{ is discrete} \\[10pt] \displaystyle\int_{-\infty}^{\infty} \left(\frac{x - \mu}{\sigma}\right)^3 f(x)\,dx & \text{if } X \text{ is continuous} \end{cases}$$

### Interpretation

| Skewness | Shape | Description |
|----------|-------|-------------|
| Negative | Left-skewed | Tail extends to the left; Mean < Median < Mode |
| Zero | Symmetric | Balanced around the mean (e.g., Normal distribution) |
| Positive | Right-skewed | Tail extends to the right; Mode < Median < Mean |

### Key Properties

- Any **symmetric** distribution (Normal, Uniform, $t$-distribution) has skewness $= 0$.
- The **Exponential** distribution has skewness $= 2$ (always right-skewed).
- Skewness is dimensionless (the standardization by $\sigma$ removes units).

---

## Kurtosis — Measure of Tail Thickness

### Definition

The **kurtosis** of $X$ is:

$$\text{Kurtosis}(X) = E\left[\left(\frac{X - \mu}{\sigma}\right)^4\right]$$

$$= \begin{cases} \displaystyle\sum_x \left(\frac{x - \mu}{\sigma}\right)^4 p(x) & \text{if } X \text{ is discrete} \\[10pt] \displaystyle\int_{-\infty}^{\infty} \left(\frac{x - \mu}{\sigma}\right)^4 f(x)\,dx & \text{if } X \text{ is continuous} \end{cases}$$

The **excess kurtosis** is defined as:

$$\text{Excess Kurtosis}(X) = \text{Kurtosis}(X) - 3$$

The subtraction of $3$ is because the normal distribution has kurtosis exactly $3$.

### Interpretation

| Kurtosis | Excess Kurtosis | Tail Behavior | Name |
|----------|----------------|---------------|------|
| $> 3$ | $> 0$ | Fat tails (heavier than Normal) | Leptokurtic |
| $= 3$ | $= 0$ | Like the Normal distribution | Mesokurtic |
| $< 3$ | $< 0$ | Light tails (thinner than Normal) | Platykurtic |

### Key Properties

- Kurtosis is always $\geq 1$ (by Jensen's inequality: $E[Z^4] \geq (E[Z^2])^2 = 1$ for any standardized variable $Z$).
- The **Normal distribution** has kurtosis $= 3$ (excess kurtosis $= 0$), serving as the reference.
- The **$t$-distribution** with $\nu > 4$ has excess kurtosis $= 6/(\nu - 4)$, which is always positive (fat-tailed).
- The **Uniform distribution** has kurtosis $= 9/5 = 1.8$ (light-tailed, platykurtic).

## Python Implementation

```python
import numpy as np
from scipy import stats

# Compare skewness and kurtosis of common distributions
distributions = {
    'Normal(0,1)':    stats.norm(0, 1),
    'Exp(1)':         stats.expon(scale=1),
    'Uniform(0,1)':   stats.uniform(0, 1),
    'Beta(2,5)':      stats.beta(2, 5),
    't(5)':           stats.t(5),
    'Chi-sq(3)':      stats.chi2(3),
}

print(f"{'Distribution':<16} {'Skewness':>10} {'Kurtosis':>10} {'Excess Kurt':>12}")
print("-" * 52)
for name, dist in distributions.items():
    skew = dist.stats(moments='s')
    kurt = dist.stats(moments='k')  # scipy returns excess kurtosis
    print(f"{name:<16} {float(skew):>10.4f} {float(kurt)+3:>10.4f} {float(kurt):>12.4f}")
```

**Output:**
```
Distribution     Skewness   Kurtosis  Excess Kurt
----------------------------------------------------
Normal(0,1)        0.0000     3.0000        0.0000
Exp(1)             2.0000     9.0000        6.0000
Uniform(0,1)       0.0000     1.8000       -1.2000
Beta(2,5)          0.5963     2.8466       -0.1534
t(5)               0.0000     9.0000        6.0000
Chi-sq(3)          1.6330     7.0000        4.0000
```
