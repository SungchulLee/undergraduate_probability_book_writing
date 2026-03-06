# Exercises: Distributions Related to the Normal

## Exercise 1: Basic Chi-Squared Calculation

Let $Z_1, Z_2, Z_3$ be iid $N(0,1)$. Find $E[Z_1^2 + Z_2^2 + Z_3^2]$ and $\text{Var}(Z_1^2 + Z_2^2 + Z_3^2)$.

### Solution

$Z_1^2 + Z_2^2 + Z_3^2 \sim \chi^2_3$, so $E = 3$ and $\text{Var} = 2(3) = 6$.

---

## Exercise 2: PDF of a Squared Normal via CDF Method

Let $X \sim N(0, \sigma^2)$. Derive the PDF of $Y = X^2$ using the CDF method.

### Solution

For $y > 0$:

$$P(Y \leq y) = P(X^2 \leq y) = P(-\sqrt{y} \leq X \leq \sqrt{y}) = \Phi\!\left(\frac{\sqrt{y}}{\sigma}\right) - \Phi\!\left(\frac{-\sqrt{y}}{\sigma}\right)$$

Differentiating:

$$f_Y(y) = \frac{1}{\sigma\sqrt{2\pi}} e^{-y/(2\sigma^2)} \cdot \frac{1}{2\sqrt{y}} + \frac{1}{\sigma\sqrt{2\pi}} e^{-y/(2\sigma^2)} \cdot \frac{1}{2\sqrt{y}} = \frac{1}{\sigma\sqrt{2\pi y}} e^{-y/(2\sigma^2)}$$

When $\sigma = 1$, this gives $f_Y(y) = \frac{1}{\sqrt{2\pi y}} e^{-y/2}$, which is the $\chi^2_1 = \Gamma(1/2, 1/2)$ PDF.

---

## Exercise 3: Additivity of Chi-Squared

If $V_1 \sim \chi^2_3$ and $V_2 \sim \chi^2_7$ are independent, what is the distribution of $V_1 + V_2$?

### Solution

$V_1 + V_2 \sim \chi^2_{3+7} = \chi^2_{10}$.

---

## Exercise 4: Chi-Squared MGF Identification

A random variable $W$ has MGF $\varphi_W(t) = (1 - 2t)^{-5}$. Identify the distribution.

### Solution

$(1 - 2t)^{-5} = (1 - 2t)^{-d/2}$ with $d = 10$. So $W \sim \chi^2_{10}$.

---

## Exercise 5: Sample Variance Distribution

A sample of $n = 16$ is drawn from $N(\mu, 25)$. Find the distribution of $(n-1)S^2/\sigma^2$.

### Solution

$$\frac{(n-1)S^2}{\sigma^2} = \frac{15 S^2}{25} \sim \chi^2_{15}$$

$E = 15$, $\text{Var} = 30$.

---

## Exercise 6: Independence of X-bar and S^2

Let $X_1, \ldots, X_n$ be iid $N(\mu, \sigma^2)$. Show that $\text{Cov}(\bar{X}, X_i - \bar{X}) = 0$ for all $i$.

### Solution

$$\text{Cov}(\bar{X}, X_i - \bar{X}) = \text{Cov}(\bar{X}, X_i) - \text{Var}(\bar{X})$$

$$= \text{Cov}\!\left(\frac{1}{n}\sum_j X_j, X_i\right) - \frac{\sigma^2}{n} = \frac{\sigma^2}{n} - \frac{\sigma^2}{n} = 0$$

---

## Exercise 7: Student's t from Definition

Let $Z \sim N(0,1)$ and $V \sim \chi^2_4$ be independent. Find the mean and variance of $T = Z/\sqrt{V/4}$.

### Solution

$T \sim t_4$. Mean $= 0$ (since $d = 4 > 1$). Variance $= 4/(4-2) = 2$.

---

## Exercise 8: Studentized Mean

A sample of $n = 9$ from $N(50, \sigma^2)$ yields $\bar{x} = 53$ and $s = 6$. Find $P(\bar{X} \geq 53)$ under $\mu = 50$.

### Solution

$$T = \frac{53 - 50}{6/\sqrt{9}} = \frac{3}{2} = 1.5$$

$P(\bar{X} \geq 53) = P(t_8 \geq 1.5)$.

```python
from scipy import stats
print(f"{stats.t(8).sf(1.5):.4f}")  # 0.0856
```

---

## Exercise 9: Cauchy Has No Mean

Show that $E[T]$ does not exist when $T \sim t_1$ (Cauchy distribution).

### Solution

The PDF is $f(t) = \frac{1}{\pi(1 + t^2)}$. We need:

$$E[|T|] = \frac{2}{\pi} \int_0^{\infty} \frac{t}{1+t^2}\,dt = \frac{2}{\pi} \left[\frac{1}{2}\ln(1+t^2)\right]_0^{\infty} = \infty$$

Since $E[|T|] = \infty$, the mean does not exist.

---

## Exercise 10: F Distribution from t^2

If $T \sim t_{15}$, find $P(T^2 > 4.54)$.

### Solution

$T^2 \sim F_{1, 15}$.

```python
from scipy import stats
print(f"{stats.f(1, 15).sf(4.54):.4f}")  # 0.0500
```

This equals $P(|T| > \sqrt{4.54}) = P(|T| > 2.131) \approx 0.05$, the two-sided $t$-test critical value.

---

## Exercise 11: F Distribution Properties

If $F \sim F_{5, 10}$, find $E[F]$ and verify the reciprocal property via simulation.

### Solution

$E[F] = \frac{d_2}{d_2 - 2} = \frac{10}{8} = 1.25$.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
f_samples = np.random.f(5, 10, 100_000)
print(f"Simulated mean of F(5,10): {f_samples.mean():.4f}  (theory: 1.25)")

# Reciprocal property
recip = 1.0 / f_samples
ks_stat, pval = stats.kstest(recip, 'f', args=(10, 5))
print(f"KS test 1/F(5,10) ~ F(10,5): p = {pval:.4f}")
```

---

## Exercise 12: Decomposition Identity

Verify the identity $\sum(X_i - \mu)^2 = \sum(X_i - \bar{X})^2 + n(\bar{X} - \mu)^2$ by simulation.

### Solution

```python
import numpy as np

np.random.seed(42)
mu, sigma, n = 5, 3, 20
x = np.random.normal(mu, sigma, n)
x_bar = x.mean()

lhs = np.sum((x - mu)**2)
rhs = np.sum((x - x_bar)**2) + n * (x_bar - mu)**2
print(f"LHS: {lhs:.6f}")
print(f"RHS: {rhs:.6f}")
print(f"Difference: {abs(lhs - rhs):.2e}")
```

**Output:**
```
LHS: 164.823456
RHS: 164.823456
Difference: 2.84e-14
```

---

## Exercise 13: Probability with Sample Variance

A sample of $n = 10$ from $N(\mu, 25)$. Find $P(S^2 > 30)$.

### Solution

$$\frac{(n-1)S^2}{\sigma^2} = \frac{9 \times 30}{25} = 10.8$$

$$P(S^2 > 30) = P(\chi^2_9 > 10.8)$$

```python
from scipy import stats
print(f"{stats.chi2(9).sf(10.8):.4f}")  # 0.2897
```
