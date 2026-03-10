# Mean and Variance of the Exponential Distribution

The mean and variance of $\text{Exp}(\lambda)$ have clean closed forms that mirror the Geometric distribution, with the rate $\lambda$ playing the role of the success probability $p$.

## Definition

If $X \sim \text{Exp}(\lambda)$, then

$$
E[X] = \frac{1}{\lambda}, \qquad \text{Var}(X) = \frac{1}{\lambda^2}, \qquad \text{SD}(X) = \frac{1}{\lambda}
$$

The $n$-th moment is

$$
E[X^n] = \frac{n!}{\lambda^n}
$$

The moment generating function is

$$
M_X(t) = \frac{\lambda}{\lambda - t}, \quad t < \lambda
$$

## Explanation

### Deriving the Mean

Using integration by parts with $u = x$ and $dv = \lambda e^{-\lambda x} \, dx$:

$$
E[X] = \int_0^\infty x \lambda e^{-\lambda x} \, dx = \left[-x e^{-\lambda x}\right]_0^\infty + \int_0^\infty e^{-\lambda x} \, dx = 0 + \frac{1}{\lambda} = \frac{1}{\lambda}
$$

The boundary term vanishes because $x e^{-\lambda x} \to 0$ as $x \to \infty$ (the exponential decay dominates the linear growth).

**Interpretation.** The mean $1/\lambda$ is the average waiting time between events in a Poisson process with rate $\lambda$. If events occur at rate $\lambda = 5$ per hour, the average time between events is $1/5$ hour $= 12$ minutes.

### Deriving the Second Moment

Compute $E[X^2]$ using the substitution $u = \lambda x$:

$$
E[X^2] = \int_0^\infty x^2 \lambda e^{-\lambda x} \, dx = \frac{1}{\lambda^2} \int_0^\infty u^2 e^{-u} \, du = \frac{\Gamma(3)}{\lambda^2} = \frac{2!}{\lambda^2} = \frac{2}{\lambda^2}
$$

### Deriving the Variance

$$
\text{Var}(X) = E[X^2] - (E[X])^2 = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} = \frac{1}{\lambda^2}
$$

### Standard Deviation Equals the Mean

A notable property: for the Exponential distribution, the standard deviation equals the mean:

$$
\text{SD}(X) = \frac{1}{\lambda} = E[X]
$$

This means the **coefficient of variation** $\text{CV} = \text{SD}(X) / E[X]$ is always $1$, regardless of the rate parameter. The Exponential distribution is the boundary case: distributions with $\text{CV} < 1$ are more regular (less variable) than exponential, while those with $\text{CV} > 1$ are more bursty (more variable).

### General Moments via the Gamma Function

The $n$-th moment has a clean factorial form:

$$
E[X^n] = \int_0^\infty x^n \lambda e^{-\lambda x} \, dx = \frac{1}{\lambda^n} \int_0^\infty u^n e^{-u} \, du = \frac{\Gamma(n+1)}{\lambda^n} = \frac{n!}{\lambda^n}
$$

### MGF Derivation and Moment Extraction

$$
M_X(t) = E[e^{tX}] = \int_0^\infty e^{tx} \lambda e^{-\lambda x} \, dx = \lambda \int_0^\infty e^{-(\lambda - t)x} \, dx = \frac{\lambda}{\lambda - t}
$$

The integral converges when $\lambda - t > 0$, i.e., $t < \lambda$. Differentiating:

$$
M_X'(t) = \frac{\lambda}{(\lambda - t)^2} \implies M_X'(0) = \frac{1}{\lambda} = E[X]
$$

$$
M_X''(t) = \frac{2\lambda}{(\lambda - t)^3} \implies M_X''(0) = \frac{2}{\lambda^2} = E[X^2]
$$

### Discrete-Continuous Analogy

| Distribution | Mean | Variance |
|:---:|:---:|:---:|
| $\text{Geo}(p)$ | $\dfrac{1}{p}$ | $\dfrac{q}{p^2}$ |
| $\text{NegBin}(n, p)$ | $\dfrac{n}{p}$ | $\dfrac{nq}{p^2}$ |
| $\text{Exp}(\lambda)$ | $\dfrac{1}{\lambda}$ | $\dfrac{1}{\lambda^2}$ |
| $\Gamma(n, \lambda)$ | $\dfrac{n}{\lambda}$ | $\dfrac{n}{\lambda^2}$ |

The Geometric is to the Negative Binomial as the Exponential is to the Gamma: each row is $n$ times (or $\alpha$ times) the first.

## Examples

**Example 1.** A radioactive source emits particles at rate $\lambda = 3$ per second. Find the mean, variance, and standard deviation of the time between emissions.

The interarrival time is $X \sim \text{Exp}(3)$, so $E[X] = 1/3$ seconds, $\text{Var}(X) = 1/9$ seconds$^2$, and $\text{SD}(X) = 1/3$ seconds.

**Example 2.** Verify the moments and the MGF numerically for several rate parameters.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n_sim = 200_000

print("=== Moment Verification ===")
print(f"{'lam':>5} | {'E[X] thy':>9} {'E[X] sim':>9} | "
      f"{'Var thy':>9} {'Var sim':>9} | {'SD=Mean?':>9}")
print("-" * 68)

for lam in [0.5, 1.0, 2.0, 5.0]:
    X = np.random.exponential(1/lam, n_sim)
    mean_thy = 1 / lam
    var_thy = 1 / lam**2
    print(f"{lam:5.1f} | {mean_thy:9.4f} {np.mean(X):9.4f} | "
          f"{var_thy:9.4f} {np.var(X):9.4f} | "
          f"{np.std(X)/np.mean(X):9.4f}")

# Verify higher moments: E[X^n] = n! / lambda^n
print("\n=== Higher Moments for Exp(2) ===")
lam = 2.0
X = np.random.exponential(1/lam, n_sim)
for n in range(1, 6):
    theory = np.math.factorial(n) / lam**n
    simulated = np.mean(X**n)
    print(f"E[X^{n}]: theory={theory:.4f}, sim={simulated:.4f}")

# Verify MGF: M(t) = lambda/(lambda-t)
print("\n=== MGF Verification for Exp(2) ===")
for t in [0.5, 1.0, 1.5]:
    mgf_theory = lam / (lam - t)
    mgf_sim = np.mean(np.exp(t * X))
    print(f"M({t}): theory={mgf_theory:.4f}, sim={mgf_sim:.4f}")
```
