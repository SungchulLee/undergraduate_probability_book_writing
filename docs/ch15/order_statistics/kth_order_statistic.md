# PDF of the k-th Order Statistic
<<<<<<< Updated upstream

## Main Result

!!! info "Density of the k-th Order Statistic"
    Let $X_1, \ldots, X_n$ be iid with CDF $F$ and PDF $f$. The PDF of $X_{(k)}$ is:

    $$f_{X_{(k)}}(x) = \frac{n!}{(k-1)!\,(n-k)!} \, [F(x)]^{k-1} \, [1 - F(x)]^{n-k} \, f(x)$$

## Derivation via Multinomial Argument

To have $X_{(k)}$ in a small interval $(x, x + dx)$, the $n$ observations must split into three groups:

1. **$k - 1$ observations** fall below $x$, each with probability $F(x)$
2. **1 observation** falls in $(x, x + dx)$, with probability $f(x)\,dx$
3. **$n - k$ observations** fall above $x + dx$, each with probability $1 - F(x)$

The number of ways to assign the $n$ observations to these three groups is the multinomial coefficient $\frac{n!}{(k-1)!\cdot 1!\cdot (n-k)!}$. Therefore:

$$P(x < X_{(k)} < x + dx) = \frac{n!}{(k-1)!\cdot 1!\cdot (n-k)!} \, [F(x)]^{k-1} \, f(x)\,dx \, [1 - F(x)]^{n-k}$$

Dividing by $dx$ gives the PDF. $\square$

## Verification of Special Cases

Setting $k = 1$:

$$f_{X_{(1)}}(x) = n[1 - F(x)]^{n-1} f(x)$$

Setting $k = n$:

$$f_{X_{(n)}}(x) = n[F(x)]^{n-1} f(x)$$

Both match the min/max formulas derived in the previous section.

## Worked Example: Median of Five Uniforms

??? example "Example: Median of U(0, 1) Sample"
    Let $n = 5$ and $X_i \overset{\text{iid}}{\sim} U(0, 1)$. The median is $X_{(3)}$.

    With $F(x) = x$ and $f(x) = 1$ on $(0, 1)$:

    $$f_{X_{(3)}}(x) = \frac{5!}{2!\cdot 2!} \, x^2(1-x)^2 = 30\, x^2(1-x)^2, \quad 0 < x < 1$$

    This is a $\text{Beta}(3, 3)$ density, symmetric about $1/2$.

    $$E[X_{(3)}] = \frac{3}{6} = \frac{1}{2}, \qquad \text{Var}(X_{(3)}) = \frac{3 \cdot 3}{36 \cdot 7} = \frac{1}{28}$$

## CDF of the k-th Order Statistic

The CDF can be expressed using the incomplete Beta function. Since $X_{(k)} \leq x$ requires at least $k$ out of $n$ observations to fall below $x$:

$$F_{X_{(k)}}(x) = \sum_{j=k}^{n} \binom{n}{j} [F(x)]^j [1 - F(x)]^{n-j}$$

This is the tail probability of a $\text{Binomial}(n, F(x))$ distribution, which equals the regularized incomplete Beta function $I_{F(x)}(k, n - k + 1)$.

## Python Implementation

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n, k, n_sim = 5, 3, 100000

# Simulate the median of 5 U(0,1) samples
samples = np.sort(np.random.uniform(0, 1, (n_sim, n)), axis=1)
median_samples = samples[:, k - 1]

x = np.linspace(0.01, 0.99, 200)
pdf_theory = stats.beta.pdf(x, k, n - k + 1)

print(f"Median X_(3) of 5 U(0,1) samples:")
print(f"  E[X_(3)] = {median_samples.mean():.4f}  (theory 0.5000)")
print(f"  Var[X_(3)] = {median_samples.var():.4f}  (theory {1/28:.4f})")

# General formula verification for k=2, n=6
n2, k2 = 6, 2
samples2 = np.sort(np.random.uniform(0, 1, (n_sim, n2)), axis=1)
os2 = samples2[:, k2 - 1]
print(f"\nX_(2) of 6 U(0,1) samples:")
print(f"  E[X_(2)] = {os2.mean():.4f}  (theory {k2/(n2+1):.4f})")
```

**Output:**
```
Median X_(3) of 5 U(0,1) samples:
  E[X_(3)] = 0.5006  (theory 0.5000)
  Var[X_(3)] = 0.0355  (theory 0.0357)

X_(2) of 6 U(0,1) samples:
  E[X_(2)] = 0.2856  (theory 0.2857)
```
=======
>>>>>>> Stashed changes
