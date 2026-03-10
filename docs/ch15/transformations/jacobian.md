# Jacobian Method for Joint Transformations


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## The Jacobian Transformation Formula

When transforming a pair of continuous random variables $(X, Y)$ to a new pair $(U, V)$ through a bijective mapping, the joint PDF transforms according to the **Jacobian formula**.

!!! info "Jacobian Method (Bivariate)"
    If $(U, V) = g(X, Y)$ is a bijective transformation with inverse $x = x(u, v)$, $y = y(u, v)$, then:

    $$f_{U,V}(u, v) = f_{X,Y}(x, y) \left|\frac{\partial(x, y)}{\partial(u, v)}\right|$$

    where the **Jacobian determinant** is:

    $$\left|\frac{\partial(x, y)}{\partial(u, v)}\right| = \left|\det \begin{pmatrix} \dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v} \\[8pt] \dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v} \end{pmatrix}\right|$$

## Geometric Intuition

The Jacobian accounts for how the transformation distorts areas:

- A small rectangle $du \times dv$ in $(u, v)$-space maps to a parallelogram in $(x, y)$-space
- The area of that parallelogram is $\left|\frac{\partial(x,y)}{\partial(u,v)}\right| du \, dv$
- Since probability = density × area, the densities must satisfy:

$$f_{U,V}(u, v) \, du \, dv = f_{X,Y}(x, y) \left|\frac{\partial(x, y)}{\partial(u, v)}\right| du \, dv$$

Therefore $f_{U,V}(u, v) = f_{X,Y}(x, y) \left|\frac{\partial(x, y)}{\partial(u, v)}\right|$.

## Inverse Jacobian Property

The Jacobian can be computed in either direction:

$$\left|\frac{\partial(x, y)}{\partial(u, v)}\right| = \frac{1}{\left|\dfrac{\partial(u, v)}{\partial(x, y)}\right|}$$

It is often easier to compute $\frac{\partial(u,v)}{\partial(x,y)}$ (the "forward" Jacobian) and take the reciprocal.

## General n-Dimensional Case

!!! info "Jacobian Method (n-Dimensional)"
    For a bijective transformation $(Y_1, \ldots, Y_n) = g(X_1, \ldots, X_n)$:

    $$f_{Y_1,\ldots,Y_n}(y_1, \ldots, y_n) = f_{X_1,\ldots,X_n}(x_1, \ldots, x_n) \left|\frac{\partial(x_1, \ldots, x_n)}{\partial(y_1, \ldots, y_n)}\right|$$

    where

    $$\left|\frac{\partial(x_1, \ldots, x_n)}{\partial(y_1, \ldots, y_n)}\right| = \left|\det \begin{pmatrix} \dfrac{\partial x_1}{\partial y_1} & \cdots & \dfrac{\partial x_1}{\partial y_n} \\ \vdots & \ddots & \vdots \\ \dfrac{\partial x_n}{\partial y_1} & \cdots & \dfrac{\partial x_n}{\partial y_n} \end{pmatrix}\right|$$

## Key Application: Gamma-to-Beta Derivation

The most important application in this chapter is deriving the Beta distribution from two independent Gamma random variables (see the Beta distribution section for the full derivation).

Given $X \sim \Gamma(\alpha, \lambda)$ and $Y \sim \Gamma(\beta, \lambda)$ independent, let $T = X + Y$ and $F = X/(X+Y)$. The transformation is $x = tf$, $y = t(1-f)$, and:

$$\frac{\partial(t, f)}{\partial(x, y)} = \det \begin{pmatrix} 1 & 1 \\ \frac{t - x}{t^2} & -\frac{x}{t^2} \end{pmatrix} = -\frac{1}{t}$$

So $\left|\frac{\partial(x,y)}{\partial(t,f)}\right| = t$, leading to the factored joint density that proves $F \sim \text{Beta}(\alpha, \beta)$ and the independence of $T$ and $F$.

## Summary: CDF vs Jacobian

| Method | When to Use | Advantages |
|:---|:---|:---|
| **CDF method** | Always works | Handles non-monotone transformations |
| **Jacobian (1D)** | $Y = g(X)$, $g$ monotone | Direct formula, no integration |
| **Jacobian (2D+)** | Bijective joint transformation | Systematic for joint densities |

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 100000

# Demonstrate Jacobian transformation: (X,Y) -> (T,F)
# X ~ Gamma(2, 1), Y ~ Gamma(3, 1) independent
alpha, beta_param = 2, 3
lam = 1.0

X = np.random.gamma(alpha, 1/lam, n_sim)
Y = np.random.gamma(beta_param, 1/lam, n_sim)

T = X + Y        # Should be Gamma(alpha+beta, lambda)
F = X / (X + Y)  # Should be Beta(alpha, beta)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Joint scatter: (X, Y)
axes[0, 0].scatter(X[:2000], Y[:2000], s=1, alpha=0.3)
axes[0, 0].set_title('Original: (X, Y)')
axes[0, 0].set_xlabel('X ~ Γ(2,1)')
axes[0, 0].set_ylabel('Y ~ Γ(3,1)')
axes[0, 0].grid(True, alpha=0.3)

# Joint scatter: (T, F)
axes[0, 1].scatter(T[:2000], F[:2000], s=1, alpha=0.3, color='red')
axes[0, 1].set_title('Transformed: (T, F)')
axes[0, 1].set_xlabel('T = X+Y ~ Γ(5,1)')
axes[0, 1].set_ylabel('F = X/(X+Y) ~ Beta(2,3)')
axes[0, 1].grid(True, alpha=0.3)

# Marginal of T
t_vals = np.linspace(0, 15, 200)
axes[1, 0].hist(T, bins=60, density=True, alpha=0.5, color='steelblue')
axes[1, 0].plot(t_vals, stats.gamma.pdf(t_vals, a=alpha+beta_param, scale=1/lam),
                'r-', lw=2, label=f'Γ({alpha+beta_param},{lam}) PDF')
axes[1, 0].set_title(f'T = X+Y ~ Γ({alpha+beta_param},{lam})')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# Marginal of F
f_vals = np.linspace(0.01, 0.99, 200)
axes[1, 1].hist(F, bins=60, density=True, alpha=0.5, color='orange')
axes[1, 1].plot(f_vals, stats.beta.pdf(f_vals, alpha, beta_param),
                'r-', lw=2, label=f'Beta({alpha},{beta_param}) PDF')
axes[1, 1].set_title(f'F = X/(X+Y) ~ Beta({alpha},{beta_param})')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('jacobian_method.png', dpi=150, bbox_inches='tight')
plt.show()

# Verify independence of T and F
print(f"Corr(T, F) = {np.corrcoef(T, F)[0,1]:.6f} (should be ≈ 0)")
```
