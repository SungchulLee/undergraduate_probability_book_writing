# Probability Integral Transform

## The Probability Integral Transform

!!! info "Probability Integral Transform"
    If $X$ is a continuous random variable with CDF $F$, then:

    $$F(X) \sim U(0, 1)$$

    That is, applying the CDF of a random variable to itself always produces a standard Uniform.

### Proof

Let $U = F(X)$. Since $F$ is continuous and non-decreasing:

$$P(U \leq u) = P(F(X) \leq u) = P(X \leq F^{-1}(u)) = F(F^{-1}(u)) = u$$

for $0 < u < 1$. This is the CDF of $U(0,1)$.

## The Inverse Transform Method

The converse is equally important and provides a universal simulation technique.

!!! info "Inverse Transform Method (Simulation)"
    To simulate a random variable $X$ with CDF $F$ using a uniform random number:

    **Step 1.** Generate $U \sim U(0, 1)$.

    **Step 2.** Set $X = F^{-1}(U)$.

    If $F$ is not bijective (e.g., for discrete distributions), use the **generalized inverse**:

    $$X = \sup\{x \in \mathbb{R} : F(x) < U\}$$

### Proof

$$P(X \leq x) = P(F^{-1}(U) \leq x) = P(U \leq F(x)) = F(x)$$

So $X$ has the desired CDF $F$.

### Geometric Interpretation

The method works by:

1. Drawing a horizontal line at height $U$ (a random value between 0 and 1)
2. Finding where it intersects the CDF curve $F$
3. Reading off the corresponding $x$-value

Regions where the CDF is steep (high density) correspond to many $U$-values mapping to a narrow range of $x$-values, naturally producing more samples there.

## Worked Example: Simulating Exp(0.5)

??? example "Example: Generating Exponential from Uniform"
    Suppose you have $U \sim U(0, 1)$. Generate $X \sim \text{Exp}(0.5)$.

    **Step 1:** Find the CDF and its inverse.

    $$\bar{F}(x) = e^{-0.5x} \implies F(x) = 1 - e^{-0.5x}, \quad x \geq 0$$

    Setting $u = 1 - e^{-0.5x}$ and solving for $x$:

    $$X = F^{-1}(U) = -2\log(1 - U) \sim \text{Exp}(0.5)$$

    **Step 2:** Simplify using symmetry.

    Since $U \sim U(0,1)$ implies $1 - U \sim U(0,1)$:

    $$X = -2\log(U) \sim \text{Exp}(0.5)$$

## General Exponential Simulation

For any $X \sim \text{Exp}(\lambda)$:

$$X = -\frac{1}{\lambda}\log(U) \sim \text{Exp}(\lambda)$$

This is one of the most commonly used simulation formulas.

## When the Inverse CDF Has No Closed Form

For distributions where $F^{-1}$ cannot be written in closed form (e.g., Normal, Gamma with non-integer shape), alternative methods are used:

- **Numerical inversion:** Use root-finding to solve $F(x) = u$
- **Accept-reject method:** Generate candidates and filter
- **Box-Muller transform:** Specialized for Normal distribution
- **Composition methods:** Decompose into simpler distributions

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 10000

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Demonstrate the inverse transform method for Exp(0.5)
lam = 0.5
U = np.random.uniform(0, 1, n_sim)
X_sim = -np.log(U) / lam  # Inverse CDF method

x_vals = np.linspace(0, 10, 200)
pdf_theory = lam * np.exp(-lam * x_vals)

axes[0].hist(X_sim, bins=60, density=True, alpha=0.5, color='steelblue',
             label='Simulated via F⁻¹(U)')
axes[0].plot(x_vals, pdf_theory, 'r-', lw=2, label='Exp(0.5) PDF')
axes[0].set_title('Inverse Transform: Exp(0.5)')
axes[0].set_xlabel('x')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Visualize the geometric interpretation
cdf_vals = 1 - np.exp(-lam * x_vals)
axes[1].plot(x_vals, cdf_vals, 'b-', lw=2, label='CDF F(x)')

# Show a few sample mappings
for u_val in [0.1, 0.3, 0.5, 0.7, 0.9]:
    x_val = -np.log(1 - u_val) / lam
    axes[1].plot([0, x_val], [u_val, u_val], 'r--', alpha=0.5)
    axes[1].plot([x_val, x_val], [0, u_val], 'r--', alpha=0.5)
    axes[1].plot(x_val, u_val, 'ro', markersize=5)

axes[1].set_title('Geometric Interpretation')
axes[1].set_xlabel('x')
axes[1].set_ylabel('F(x) / U')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# Probability integral transform: F(X) ~ U(0,1)
X_exp = np.random.exponential(1/lam, n_sim)
U_transform = 1 - np.exp(-lam * X_exp)  # F(X)

axes[2].hist(U_transform, bins=50, density=True, alpha=0.7,
             color='orange', label='F(X)')
axes[2].axhline(1.0, color='black', lw=2, linestyle='--',
                label='U(0,1) PDF')
axes[2].set_title('F(X) ~ U(0,1)')
axes[2].set_xlabel('u')
axes[2].set_ylabel('Density')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('probability_integral_transform.png', dpi=150, bbox_inches='tight')
plt.show()

# Verify: compare inverse CDF simulation with scipy
X_scipy = np.random.exponential(1/lam, n_sim)
print(f"Inverse CDF method: mean={np.mean(X_sim):.4f}, var={np.var(X_sim):.4f}")
print(f"Direct sampling:    mean={np.mean(X_scipy):.4f}, var={np.var(X_scipy):.4f}")
print(f"Theory:             mean={1/lam:.4f}, var={1/lam**2:.4f}")
```
