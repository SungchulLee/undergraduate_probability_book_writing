# Convergence of t(d) to N(0,1) as d approaches infinity

## Statement

As the degrees of freedom $d \to \infty$:

$$t_d \xrightarrow{d} N(0, 1)$$

The $t$ distribution converges to the standard normal distribution.

## Intuitive Explanation

Recall the definition: $T = Z / \sqrt{V/d}$ where $Z \sim N(0,1)$ and $V \sim \chi^2_d$.

By the Law of Large Numbers, since $V = \sum_{i=1}^d W_i^2$ where $W_i$ iid $N(0,1)$:

$$\frac{V}{d} = \frac{1}{d}\sum_{i=1}^d W_i^2 \xrightarrow{p} E[W_1^2] = 1$$

Therefore $\sqrt{V/d} \xrightarrow{p} 1$, and by Slutsky's theorem:

$$T = \frac{Z}{\sqrt{V/d}} \xrightarrow{d} \frac{Z}{1} = Z \sim N(0,1)$$

## Pointwise PDF Convergence

At each point $t$, the $t_d$ PDF converges to the standard normal PDF:

$$\left(1 + \frac{t^2}{d}\right)^{-(d+1)/2} \to e^{-t^2/2} \quad \text{as } d \to \infty$$

This follows from $\lim_{d\to\infty}\left(1 + \frac{a}{d}\right)^d = e^a$ with $a = -t^2/2$.

## Practical Implications

| $d$ | $\text{Var}(t_d) = d/(d-2)$ | $P(\|T\| > 1.96)$ |
|-----|-----|-----|
| $1$ (Cauchy) | $\infty$ | $0.3183$ |
| $5$ | $1.667$ | $0.1076$ |
| $10$ | $1.250$ | $0.0785$ |
| $30$ | $1.071$ | $0.0593$ |
| $100$ | $1.020$ | $0.0536$ |
| $\infty$ (Normal) | $1.000$ | $0.0500$ |

For $d \geq 30$, the $t$ distribution is very close to the standard normal. In practice, using $z$-critical values instead of $t$-critical values introduces only minor error for large degrees of freedom.

## Python Visualization

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 500)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, stats.norm.pdf(x), 'r-', lw=2.5, label='$N(0,1)$')
for d in range(1, 11):
    alpha = 0.3 + 0.07 * d
    ax.plot(x, stats.t.pdf(x, d), 'b-', alpha=alpha)

ax.set_xlabel('$x$')
ax.set_ylabel('Density')
ax.set_title('$t_d$ converges to $N(0,1)$ as $d \\to \\infty$')
ax.legend()
plt.tight_layout()
plt.show()
```

This reproduces the convergence shown in the lecture figure: the blue $t_d$ curves approach the red $N(0,1)$ curve as $d$ increases, with the fat tails shrinking toward the normal tails.
