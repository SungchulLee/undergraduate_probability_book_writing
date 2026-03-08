# Mean and Variance of the Poisson Distribution

## Mean of Po(lambda)

### Direct Computation

For $X \sim \text{Po}(\lambda)$:

$$
E[X] = \sum_{k=0}^{\infty} k \cdot \frac{e^{-\lambda} \lambda^k}{k!} = \sum_{k=1}^{\infty} k \cdot \frac{e^{-\lambda} \lambda^k}{k!}
$$

Since $k/k! = 1/(k-1)!$, substituting $j = k - 1$:

$$
E[X] = e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^k}{(k-1)!} = e^{-\lambda} \lambda \sum_{j=0}^{\infty} \frac{\lambda^j}{j!} = e^{-\lambda} \lambda \cdot e^{\lambda} = \lambda
$$

### Via Indicator Decomposition

An elegant alternative uses the Binomial approximation. If $X \sim B(n, p) \approx \text{Po}(\lambda)$ with $\lambda = np$, then $X = \sum_{i=1}^{n} \mathbf{1}_{A_i}$ where $\mathbf{1}_{A_i} \sim B(p)$ are independent indicators. By linearity of expectation:

$$
E[X] = \sum_{i=1}^{n} E[\mathbf{1}_{A_i}] = np = \lambda
$$

---

## Second Moment and Variance

### Computing E[X^2]

We use the identity $E[X^2] = E[X(X-1)] + E[X]$:

$$
E[X(X-1)] = \sum_{k=0}^{\infty} k(k-1) \cdot \frac{e^{-\lambda} \lambda^k}{k!} = \sum_{k=2}^{\infty} \frac{e^{-\lambda} \lambda^k}{(k-2)!}
$$

Substituting $j = k - 2$:

$$
E[X(X-1)] = e^{-\lambda} \lambda^2 \sum_{j=0}^{\infty} \frac{\lambda^j}{j!} = e^{-\lambda} \lambda^2 e^{\lambda} = \lambda^2
$$

Therefore:

$$
E[X^2] = E[X(X-1)] + E[X] = \lambda^2 + \lambda
$$

### Variance

$$
\text{Var}(X) = E[X^2] - (E[X])^2 = (\lambda^2 + \lambda) - \lambda^2 = \lambda
$$

!!! note "Mean Equals Variance"
    For the Poisson distribution, $E[X] = \text{Var}(X) = \lambda$. This is a hallmark property that distinguishes the Poisson from other discrete distributions. The standard deviation is $\sigma = \sqrt{\lambda}$.

---

## Via Binomial Approximation

Since $\text{Po}(\lambda) \approx B(n, p)$ with $\lambda = np$ fixed and $n \to \infty$:

| | $B(n, p)$ | $\text{Po}(\lambda) \approx B(n, p)$ |
|:---|:---:|:---:|
| Expectation | $np$ | $\lambda$ |
| Variance | $npq$ | $\lambda$ |

The variance match is approximate: $npq = np(1-p) = \lambda(1 - \lambda/n) \to \lambda$ as $n \to \infty$ (since $p = \lambda/n \to 0$).

---

## Numerical Verification

```python
import numpy as np
from scipy.stats import poisson

lambdas = [1, 5, 10, 20, 50]

print(f"{'λ':>5} {'E[X]':>10} {'Var(X)':>10} {'SD(X)':>10}")
print("-" * 40)
for la in lambdas:
    mean = poisson.mean(la)
    var = poisson.var(la)
    std = poisson.std(la)
    print(f"{la:>5} {mean:>10.4f} {var:>10.4f} {std:>10.4f}")
```

Expected output:

```
    λ       E[X]     Var(X)      SD(X)
----------------------------------------
    1     1.0000     1.0000     1.0000
    5     5.0000     5.0000     2.2361
   10    10.0000    10.0000     3.1623
   20    20.0000    20.0000     4.4721
   50    50.0000    50.0000     7.0711
```

---

## Simulation Verification

```python
import numpy as np

np.random.seed(42)
la = 10
n_samples = 100_000

samples = np.random.poisson(la, n_samples)

print(f"Theoretical mean: {la}")
print(f"Sample mean:      {samples.mean():.4f}")
print(f"Theoretical var:  {la}")
print(f"Sample variance:  {samples.var(ddof=1):.4f}")
```

---

## Dispersion Index

The **dispersion index** (or index of dispersion) is defined as:

$$
D = \frac{\text{Var}(X)}{E[X]}
$$

For a Poisson distribution, $D = 1$ (equidispersion). This motivates a simple diagnostic:

- $D \approx 1$: Poisson model may be appropriate
- $D > 1$: **Overdispersion** — consider Negative Binomial
- $D < 1$: **Underdispersion** — consider Binomial with small $p$

```python
import numpy as np

np.random.seed(42)

# Poisson data
poisson_data = np.random.poisson(10, 1000)
D_poisson = poisson_data.var(ddof=1) / poisson_data.mean()
print(f"Poisson D = {D_poisson:.4f}")  # Should be ≈ 1

# Overdispersed data (Negative Binomial)
from scipy.stats import nbinom
nb_data = nbinom.rvs(n=5, p=0.3, size=1000)
D_nb = nb_data.var(ddof=1) / nb_data.mean()
print(f"Neg Binomial D = {D_nb:.4f}")  # Should be > 1
```
