# Distribution of the Minimum and Maximum
<<<<<<< Updated upstream

## CDF of the Maximum

Let $X_1, \ldots, X_n$ be iid with CDF $F$ and PDF $f$. The maximum $X_{(n)}$ satisfies:

$$F_{X_{(n)}}(x) = P(X_{(n)} \leq x) = P(X_1 \leq x, \ldots, X_n \leq x) = [F(x)]^n$$

The key step uses independence: the maximum is at most $x$ if and only if **every** observation is at most $x$.

!!! info "Distribution of the Maximum"
    $$F_{X_{(n)}}(x) = [F(x)]^n, \qquad f_{X_{(n)}}(x) = n[F(x)]^{n-1} f(x)$$

The PDF follows by differentiating the CDF using the chain rule.

## CDF of the Minimum

For the minimum $X_{(1)}$, the **survival function** is easier to work with:

$$P(X_{(1)} > x) = P(X_1 > x, \ldots, X_n > x) = [1 - F(x)]^n$$

The minimum exceeds $x$ if and only if **every** observation exceeds $x$.

!!! info "Distribution of the Minimum"
    $$F_{X_{(1)}}(x) = 1 - [1 - F(x)]^n, \qquad f_{X_{(1)}}(x) = n[1 - F(x)]^{n-1} f(x)$$

## Example: Uniform(0, 1)

??? example "Min and Max of Uniform Sample"
    Let $X_1, \ldots, X_n \overset{\text{iid}}{\sim} U(0, 1)$, so $F(x) = x$ and $f(x) = 1$ for $0 < x < 1$.

    **Maximum:**

    $$f_{X_{(n)}}(x) = nx^{n-1}, \quad 0 < x < 1$$

    This is a $\text{Beta}(n, 1)$ distribution.

    $$E[X_{(n)}] = \frac{n}{n+1}, \qquad \text{Var}(X_{(n)}) = \frac{n}{(n+1)^2(n+2)}$$

    **Minimum:**

    $$f_{X_{(1)}}(x) = n(1-x)^{n-1}, \quad 0 < x < 1$$

    This is a $\text{Beta}(1, n)$ distribution.

    $$E[X_{(1)}] = \frac{1}{n+1}, \qquad \text{Var}(X_{(1)}) = \frac{n}{(n+1)^2(n+2)}$$

    Note the symmetry: $E[X_{(1)}] + E[X_{(n)}] = 1$.

## Example: Exponential

??? example "Minimum of Exponential Sample"
    Let $X_1, \ldots, X_n \overset{\text{iid}}{\sim} \text{Exp}(\lambda)$, so $F(x) = 1 - e^{-\lambda x}$.

    $$P(X_{(1)} > x) = [e^{-\lambda x}]^n = e^{-n\lambda x}$$

    Therefore $X_{(1)} \sim \text{Exp}(n\lambda)$.

    The minimum of $n$ iid exponentials with rate $\lambda$ is exponential with rate $n\lambda$. The expected minimum is $1/(n\lambda)$, which is $1/n$ of the individual mean.

## Distribution of the Range

The **range** $R = X_{(n)} - X_{(1)}$ measures the spread of the sample.

For $U(0,1)$ samples, the range has PDF:

$$f_R(r) = n(n-1)r^{n-2}(1-r), \quad 0 < r < 1$$

with $E[R] = \frac{n-1}{n+1}$.

## Python Implementation

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n, n_sim = 10, 100000

# Simulate min and max of U(0,1) samples
samples = np.random.uniform(0, 1, (n_sim, n))
mins = samples.min(axis=1)
maxs = samples.max(axis=1)

x = np.linspace(0.001, 0.999, 200)

print(f"Max of {n} U(0,1):")
print(f"  E[X_(n)] = {maxs.mean():.4f}  (theory {n/(n+1):.4f})")
print(f"Min of {n} U(0,1):")
print(f"  E[X_(1)] = {mins.mean():.4f}  (theory {1/(n+1):.4f})")
print(f"Range:")
print(f"  E[R] = {(maxs - mins).mean():.4f}  (theory {(n-1)/(n+1):.4f})")

# Exponential minimum
lam = 2
exp_samples = np.random.exponential(1/lam, (n_sim, n))
exp_mins = exp_samples.min(axis=1)
print(f"\nMin of {n} Exp({lam}):")
print(f"  E[X_(1)] = {exp_mins.mean():.4f}  (theory {1/(n*lam):.4f})")
```

**Output:**
```
Max of 10 U(0,1):
  E[X_(n)] = 0.9090  (theory 0.9091)
Min of 10 U(0,1):
  E[X_(1)] = 0.0909  (theory 0.0909)
Range:
  E[R] = 0.8181  (theory 0.8182)

Min of 10 Exp(2):
  E[X_(1)] = 0.0501  (theory 0.0500)
```
=======
>>>>>>> Stashed changes
