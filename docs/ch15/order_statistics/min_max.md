# Distribution of the Minimum and Maximum

The CDF of the sample minimum and maximum have particularly simple forms because the events "all values exceed $x$" and "all values are at most $x$" factor by independence.

## Definition

Let $X_1, \ldots, X_n$ be iid with CDF $F$ and PDF $f$. Then:

**Maximum:** The CDF of $X_{(n)} = \max(X_1, \ldots, X_n)$ is:

$$
F_{X_{(n)}}(x) = [F(x)]^n
$$

and the PDF is:

$$
f_{X_{(n)}}(x) = n[F(x)]^{n-1} f(x)
$$

**Minimum:** The survival function of $X_{(1)} = \min(X_1, \ldots, X_n)$ is:

$$
P(X_{(1)} > x) = [1 - F(x)]^n
$$

so the CDF and PDF are:

$$
F_{X_{(1)}}(x) = 1 - [1 - F(x)]^n, \qquad f_{X_{(1)}}(x) = n[1 - F(x)]^{n-1} f(x)
$$

## Explanation

### Derivation of the maximum CDF

The event $\{X_{(n)} \leq x\}$ means every observation is at most $x$:

$$
P(X_{(n)} \leq x) = P(X_1 \leq x, X_2 \leq x, \ldots, X_n \leq x)
$$

By independence:

$$
= P(X_1 \leq x) \cdot P(X_2 \leq x) \cdots P(X_n \leq x) = [F(x)]^n
$$

Differentiating: $f_{X_{(n)}}(x) = n[F(x)]^{n-1} f(x)$.

### Derivation of the minimum CDF

The event $\{X_{(1)} > x\}$ means every observation exceeds $x$:

$$
P(X_{(1)} > x) = P(X_1 > x, X_2 > x, \ldots, X_n > x) = [1 - F(x)]^n
$$

Therefore $F_{X_{(1)}}(x) = 1 - [1 - F(x)]^n$, and differentiating gives the PDF.

### The minimum of exponentials

For iid $X_i \sim \text{Exp}(\lambda)$:

$$
P(X_{(1)} > x) = [e^{-\lambda x}]^n = e^{-n\lambda x}
$$

So $X_{(1)} \sim \text{Exp}(n\lambda)$. The minimum of $n$ independent exponentials with rate $\lambda$ is exponential with rate $n\lambda$. This extends to non-identical rates: if $X_i \sim \text{Exp}(\lambda_i)$ independently, then $\min_i X_i \sim \text{Exp}(\sum_i \lambda_i)$.

### Asymptotics as n grows

As $n \to \infty$:

- The maximum $X_{(n)}$ converges to the right endpoint of the support (if finite), or grows without bound.
- The minimum $X_{(1)}$ converges to the left endpoint of the support.
- The rate of convergence and the limiting distribution depend on the tail behavior of $F$ (this is the domain of extreme value theory).

### Mean of the maximum for Uniform(0,1)

For $U_1, \ldots, U_n \sim U(0, 1)$:

$$
E[U_{(n)}] = \int_0^1 n x^n \, dx = \frac{n}{n+1}
$$

$$
E[U_{(1)}] = \int_0^1 n(1-x)^{n-1}\,dx = \frac{1}{n+1}
$$

Note the symmetry: $E[U_{(1)}] + E[U_{(n)}] = 1$.

## Examples

**Example 1: Maximum of uniform random variables.**

Let $U_1, \ldots, U_5 \sim U(0, 1)$ iid. Find $P(U_{(5)} > 0.9)$ and $E[U_{(5)}]$.

$$
P(U_{(5)} > 0.9) = 1 - (0.9)^5 = 1 - 0.59049 = 0.40951
$$

$$
E[U_{(5)}] = \frac{5}{6} \approx 0.8333
$$

```python
import numpy as np

np.random.seed(42)
n, n_sim = 5, 100000

samples = np.random.uniform(0, 1, (n_sim, n))
maxima = samples.max(axis=1)

p_theory = 1 - 0.9**5
e_theory = n / (n + 1)

print(f"Maximum of {n} iid U(0,1):")
print(f"  P(max > 0.9) = {np.mean(maxima > 0.9):.4f}  (theory: {p_theory:.4f})")
print(f"  E[max]       = {maxima.mean():.4f}  (theory: {e_theory:.4f})")
```

**Output:**
```
Maximum of 5 iid U(0,1):
  P(max > 0.9) = 0.4099  (theory: 0.4095)
  E[max]       = 0.8334  (theory: 0.8333)
```

**Example 2: Minimum of exponentials.**

Five light bulbs have iid lifetimes $\sim \text{Exp}(0.001)$ (mean 1000 hours). Find the distribution and expected time until the first bulb burns out.

$$
X_{(1)} \sim \text{Exp}(5 \times 0.001) = \text{Exp}(0.005)
$$

$$
E[X_{(1)}] = \frac{1}{0.005} = 200 \text{ hours}
$$

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n, lam = 5, 0.001
n_sim = 100000

samples = np.random.exponential(1/lam, (n_sim, n))
minima = samples.min(axis=1)

rate_min = n * lam
print(f"Minimum of {n} iid Exp({lam}):")
print(f"  Min ~ Exp({rate_min})")
print(f"  E[min]   = {minima.mean():.1f} hours  (theory: {1/rate_min:.1f})")
print(f"  SD[min]  = {minima.std():.1f} hours  (theory: {1/rate_min:.1f})")

# Verify exponential distribution
ks_stat, p_val = stats.kstest(minima, 'expon', args=(0, 1/rate_min))
print(f"  KS test vs Exp({rate_min}): p-value = {p_val:.4f}")
```

**Output:**
```
Minimum of 5 iid Exp(0.001):
  Min ~ Exp(0.005)
  E[min]   = 200.5 hours  (theory: 200.0)
  SD[min]  = 200.7 hours  (theory: 200.0)
  KS test vs Exp(0.005): p-value = 0.6782
```

**Example 3: Range of a uniform sample.**

For $n = 10$ iid $U(0, 1)$, find the expected range $E[U_{(n)} - U_{(1)}]$.

$$
E[U_{(n)} - U_{(1)}] = E[U_{(n)}] - E[U_{(1)}] = \frac{n}{n+1} - \frac{1}{n+1} = \frac{n-1}{n+1}
$$

```python
import numpy as np

np.random.seed(42)
n, n_sim = 10, 100000

samples = np.sort(np.random.uniform(0, 1, (n_sim, n)), axis=1)
ranges = samples[:, -1] - samples[:, 0]

theory = (n - 1) / (n + 1)
print(f"Range of {n} iid U(0,1):")
print(f"  E[range] = {ranges.mean():.4f}  (theory: {theory:.4f})")
print(f"  E[max]   = {samples[:,-1].mean():.4f}  (theory: {n/(n+1):.4f})")
print(f"  E[min]   = {samples[:,0].mean():.4f}  (theory: {1/(n+1):.4f})")
```

**Output:**
```
Range of 10 iid U(0,1):
  E[range] = 0.8184  (theory: 0.8182)
  E[max]   = 0.9093  (theory: 0.9091)
  E[min]   = 0.0909  (theory: 0.0909)
```
