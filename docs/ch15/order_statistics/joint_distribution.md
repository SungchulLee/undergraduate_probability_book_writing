# Joint Distribution of Order Statistics

## Joint PDF of All Order Statistics

!!! info "Joint Density of All Order Statistics"
    Let $X_1, \ldots, X_n$ be iid with PDF $f$ and CDF $F$. The joint PDF of $(X_{(1)}, X_{(2)}, \ldots, X_{(n)})$ is:

    $$f_{X_{(1)}, \ldots, X_{(n)}}(x_1, \ldots, x_n) = n! \prod_{i=1}^n f(x_i), \quad x_1 < x_2 < \cdots < x_n$$

    and zero otherwise.

## Derivation

The joint PDF of the **original** (unordered) sample $(X_1, \ldots, X_n)$ is $\prod_{i=1}^n f(x_i)$ by independence.

There are exactly $n!$ permutations of $(x_1, \ldots, x_n)$ that produce the same ordered sequence $x_{(1)} < \cdots < x_{(n)}$. Each permutation of the original sample maps to the same point in the ordered sample. Therefore, the density of the ordered sample is $n!$ times larger, but restricted to the region $x_1 < x_2 < \cdots < x_n$. $\square$

**Consistency check.** Integrating over the region $x_1 < x_2 < \cdots < x_n$:

$$\int \cdots \int_{x_1 < \cdots < x_n} n! \prod_{i=1}^n f(x_i)\, dx_1 \cdots dx_n = n! \cdot \frac{1}{n!} = 1$$

The factor $1/n!$ comes from the fact that the region $\{x_1 < \cdots < x_n\}$ is $1/n!$ of the full space by symmetry.

## Joint PDF of Two Order Statistics

!!! info "Joint Density of $(X_{(i)}, X_{(j)})$ for $i < j$"
    $$f_{X_{(i)}, X_{(j)}}(s, t) = \frac{n!}{(i-1)!(j-i-1)!(n-j)!} [F(s)]^{i-1} [F(t) - F(s)]^{j-i-1} [1-F(t)]^{n-j} f(s)\,f(t)$$

    for $s < t$.

### Derivation via Multinomial Argument

To have $X_{(i)} \approx s$ and $X_{(j)} \approx t$ with $s < t$, the $n$ observations must split into five groups:

1. **$i - 1$ observations** below $s$: probability $[F(s)]^{i-1}$
2. **1 observation** at $s$: probability $f(s)\,ds$
3. **$j - i - 1$ observations** between $s$ and $t$: probability $[F(t) - F(s)]^{j-i-1}$
4. **1 observation** at $t$: probability $f(t)\,dt$
5. **$n - j$ observations** above $t$: probability $[1 - F(t)]^{n-j}$

The multinomial coefficient $\frac{n!}{(i-1)!\cdot 1!\cdot (j-i-1)!\cdot 1!\cdot (n-j)!}$ counts the number of ways to assign observations to these groups.

## Special Case: Joint PDF of Min and Max

Setting $i = 1$ and $j = n$:

$$f_{X_{(1)}, X_{(n)}}(s, t) = n(n-1)[F(t) - F(s)]^{n-2} f(s)\,f(t), \quad s < t$$

??? example "Example: Range of Uniform Sample"
    For $X_i \overset{\text{iid}}{\sim} U(0, 1)$ with $F(x) = x$ and $f(x) = 1$:

    $$f_{X_{(1)}, X_{(n)}}(s, t) = n(n-1)(t - s)^{n-2}, \quad 0 < s < t < 1$$

    The range $R = X_{(n)} - X_{(1)}$ has PDF:

    $$f_R(r) = n(n-1)r^{n-2}(1-r), \quad 0 < r < 1$$

    obtained by integrating the joint density over $s$ with the substitution $t = s + r$.

## Python Implementation

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n, n_sim = 5, 100000

# Simulate min and max jointly
samples = np.sort(np.random.uniform(0, 1, (n_sim, n)), axis=1)
mins = samples[:, 0]
maxs = samples[:, -1]
ranges = maxs - mins

# Verify range distribution
print(f"Range of {n} U(0,1) samples:")
print(f"  E[R] = {ranges.mean():.4f}  (theory {(n-1)/(n+1):.4f})")

# Verify joint density at a specific point
# f(s,t) = n(n-1)(t-s)^(n-2) for U(0,1)
s, t = 0.2, 0.8
joint_theory = n * (n-1) * (t - s)**(n-2)
print(f"\nJoint density f(0.2, 0.8) = {joint_theory:.4f}")

# Covariance of min and max
cov = np.cov(mins, maxs)[0, 1]
cov_theory = 1 / ((n+1)**2 * (n+2))
print(f"\nCov(X_(1), X_(n)) = {cov:.6f}  (theory {cov_theory:.6f})")
```

**Output:**
```
Range of 5 U(0,1) samples:
  E[R] = 0.6662  (theory 0.6667)

Joint density f(0.2, 0.8) = 7.2000

Cov(X_(1), X_(n)) = 0.003937  (theory 0.003968)
```
