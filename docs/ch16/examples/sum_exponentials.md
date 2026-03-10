# Sum of Exponentials

The sum of $n$ independent $\operatorname{Exp}(\lambda)$ random variables has the $\operatorname{Gamma}(n, \lambda)$ distribution — the waiting time for $n$ events in a Poisson process.

## Definition

If $X_1, X_2, \ldots, X_n$ are iid $\operatorname{Exp}(\lambda)$, then:

$$
S_n = X_1 + X_2 + \cdots + X_n \sim \operatorname{Gamma}(n, \lambda)
$$

When the rates differ ($X_i \sim \operatorname{Exp}(\lambda_i)$ with distinct $\lambda_i$), the sum has a **hypoexponential** distribution, which is not Gamma.

## Explanation

### Proof for Two Exponentials

For independent $X, Y \sim \operatorname{Exp}(\lambda)$ and $a \ge 0$:

$$
f_{X+Y}(a) = \int_0^a \lambda e^{-\lambda b} \cdot \lambda e^{-\lambda(a-b)} \, db = \lambda^2 e^{-\lambda a} \int_0^a db = \lambda^2 a \, e^{-\lambda a}
$$

This is the $\operatorname{Gamma}(2, \lambda)$ PDF: $\frac{\lambda(\lambda a)^{1} e^{-\lambda a}}{1!}$.

### Induction to General n

If $S_{n-1} \sim \operatorname{Gamma}(n-1, \lambda)$ and $X_n \sim \operatorname{Exp}(\lambda)$ are independent, then by Gamma additivity:

$$
S_n = S_{n-1} + X_n \sim \operatorname{Gamma}(n-1, \lambda) * \operatorname{Gamma}(1, \lambda) = \operatorname{Gamma}(n, \lambda)
$$

### Different Rates

For $X \sim \operatorname{Exp}(\lambda_1)$, $Y \sim \operatorname{Exp}(\lambda_2)$ with $\lambda_1 \ne \lambda_2$:

$$
f_{X+Y}(a) = \frac{\lambda_1 \lambda_2}{\lambda_1 - \lambda_2}\left(e^{-\lambda_2 a} - e^{-\lambda_1 a}\right), \quad a \ge 0
$$

### Poisson Process Connection

$S_n$ is the $n$-th arrival time in a Poisson process with rate $\lambda$:

- **Counting**: $N(t) \sim \operatorname{Pois}(\lambda t)$
- **Waiting**: $S_n \sim \operatorname{Gamma}(n, \lambda)$
- **Duality**: $P(N(t) \ge n) = P(S_n \le t)$

## Examples

**Example.** Service times are iid $\operatorname{Exp}(2)$. Find $P(S_5 > 4)$, the probability that serving 5 customers takes more than 4 minutes.

Since $S_5 \sim \operatorname{Gamma}(5, 2)$, we compute the survival function.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
lam = 2.0
n_sim = 100_000

# P(S_5 > 4) where S_5 ~ Gamma(5, 2)
p_theory = 1 - stats.gamma.cdf(4, a=5, scale=1/lam)

# Simulation
samples = np.random.exponential(1/lam, (n_sim, 5))
sums = samples.sum(axis=1)
p_sim = np.mean(sums > 4)

print(f"P(S_5 > 4): simulation={p_sim:.4f}, theory={p_theory:.4f}")

# Verify moments for various n
for n in [2, 5, 10]:
    S = np.random.exponential(1/lam, (n_sim, n)).sum(axis=1)
    print(f"Sum of {n} Exp({lam}): mean={S.mean():.3f} (theory {n/lam:.3f}), "
          f"var={S.var():.3f} (theory {n/lam**2:.3f})")
```
