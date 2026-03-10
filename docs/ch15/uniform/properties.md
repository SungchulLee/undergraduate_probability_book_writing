# Properties and Applications of the Uniform Distribution


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Symmetry

If $X \sim U(a, b)$, then $X$ is symmetric about its mean $(a+b)/2$:

$$a + b - X \sim U(a, b)$$

This means $X$ and $a + b - X$ have the same distribution. In particular, if $U \sim U(0,1)$, then $1 - U \sim U(0,1)$.

## Linear Transformation

If $X \sim U(a, b)$ and $Y = cX + d$ with $c > 0$, then:

$$Y \sim U(ca + d, \; cb + d)$$

Any Uniform can be obtained from the standard Uniform: if $U \sim U(0,1)$, then $X = a + (b-a)U \sim U(a,b)$.

## Decomposition Technique

A powerful technique for Uniform problems is to **decompose** the random variable into a known constant plus a simpler Uniform component.

??? example "Example: Breaking the Stick"
    We break a stick of length $L$ into two pieces by choosing the break point uniformly over $[0, L]$. Let $X$ be the length of the **longer** piece. Find its mean and variance.

    **Key insight:** The longer piece always has length at least $L/2$. Decompose $X$ as:

    $$X = \underbrace{\frac{L}{2}}_{\text{half of the stick}} + \underbrace{Y}_{\text{the excess}}$$

    where $Y$ is the distance from the midpoint to the break point, reflected to always be positive. Since the break point is uniform on $[0, L]$, the excess $Y$ is $U(0, L/2)$.

    **Mean:**

    $$E[X] = \frac{L}{2} + E[Y] = \frac{L}{2} + \frac{L}{4} = \frac{3L}{4}$$

    **Variance:** Since shifting by a constant doesn't change variance:

    $$\text{Var}(X) = \text{Var}(Y) = \frac{1}{12}\left(\frac{L}{2}\right)^2 = \frac{L^2}{48}$$

## Universality of the Uniform

The $U(0,1)$ distribution is universal in two senses:

1. **Any CDF applied to its own random variable gives $U(0,1)$:** If $X$ has continuous CDF $F$, then $F(X) \sim U(0,1)$ (the Probability Integral Transform).

2. **Any distribution can be generated from $U(0,1)$:** If $U \sim U(0,1)$, then $F^{-1}(U)$ has CDF $F$ (the Inverse Transform Method, see the Transformations section).

## Sum of Uniforms

The sum of independent Uniforms produces a distribution that is **not** Uniform (unless the individual Uniforms are degenerate). The sum of two iid $U(0,1)$ has a triangular distribution on $(0, 2)$. As more Uniforms are summed, the distribution approaches Normal by the Central Limit Theorem (see Chapter 16 for convolution details).

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n_sim = 100000

# Break the stick example
L = 10.0
break_points = np.random.uniform(0, L, n_sim)
longer_piece = np.maximum(break_points, L - break_points)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Distribution of longer piece
axes[0].hist(longer_piece, bins=60, density=True, alpha=0.7,
             color='steelblue', label='Simulated')
axes[0].axvline(np.mean(longer_piece), color='red', lw=2, linestyle='--',
                label=f'Mean = {np.mean(longer_piece):.3f}')
axes[0].axvline(3*L/4, color='black', lw=2, linestyle=':',
                label=f'Theory = {3*L/4:.3f}')
axes[0].set_title(f'Length of Longer Piece (L={L})')
axes[0].set_xlabel('Length')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

print(f"Break the stick (L={L}):")
print(f"  E[X] = {np.mean(longer_piece):.4f} (theory {3*L/4:.4f})")
print(f"  Var(X) = {np.var(longer_piece):.4f} (theory {L**2/48:.4f})")

# Universality: F(X) ~ U(0,1)
from scipy import stats
X_exp = np.random.exponential(2.0, n_sim)  # Exp(0.5)
U_transform = stats.expon.cdf(X_exp, scale=2.0)  # F(X)

axes[1].hist(U_transform, bins=50, density=True, alpha=0.7,
             color='orange', label='F(X) where X ~ Exp(0.5)')
axes[1].axhline(1.0, color='black', lw=2, linestyle='--',
                label='U(0,1) PDF')
axes[1].set_title('Probability Integral Transform: F(X) ~ U(0,1)')
axes[1].set_xlabel('u')
axes[1].set_ylabel('Density')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('uniform_properties.png', dpi=150, bbox_inches='tight')
plt.show()
```
