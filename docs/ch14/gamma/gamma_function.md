# The Gamma Function


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Definition

!!! info "Gamma Function"
    For $\alpha > 0$, the **Gamma function** is defined as:

    $$\Gamma(\alpha) = \int_0^\infty x^{\alpha - 1} e^{-x} \, dx$$

The Gamma function extends the factorial to non-integer values and serves as the normalizing constant for the Gamma distribution.

## Key Properties

### Property 1: Recursion

$$\Gamma(\alpha + 1) = \alpha \, \Gamma(\alpha)$$

**Proof.** Integration by parts with $u = x^{\alpha}$, $dv = e^{-x} dx$:

$$\Gamma(\alpha + 1) = \int_0^\infty x^{(\alpha+1)-1} e^{-x} \, dx = \int_0^\infty -x^{(\alpha+1)-1} \left(e^{-x}\right)' dx$$

$$= \left[-x^{(\alpha+1)-1} e^{-x}\right]_0^\infty - \int_0^\infty \left(-x^{(\alpha+1)-1}\right)' e^{-x} \, dx = \alpha \int_0^\infty x^{\alpha - 1} e^{-x} \, dx = \alpha \, \Gamma(\alpha)$$

### Property 2: Special Values

$$\Gamma(1/2) = \sqrt{\pi}, \qquad \Gamma(1) = 1, \qquad \Gamma(2) = 1$$

**Proof of $\Gamma(1/2) = \sqrt{\pi}$.**

With the substitution $s = \sqrt{x}$, so $ds = \frac{dx}{2\sqrt{x}}$:

$$\Gamma(1/2) = \int_0^\infty x^{-1/2} e^{-x} \, dx = 2 \int_0^\infty e^{-s^2} \, ds = \sqrt{\pi}$$

The last step uses the Gaussian integral $\int_0^\infty e^{-s^2} ds = \sqrt{\pi}/2$, which arises in the study of the Normal distribution.

**Proof of $\Gamma(1) = 1$.**

$$\Gamma(1) = \int_0^\infty e^{-x} \, dx = 1$$

### Property 3: Factorial Connection

$$\Gamma(n + 1) = n! \quad \text{for } n = 0, 1, 2, \ldots$$

**Proof.** By induction using the recursion property:

- Base case: $\Gamma(1) = 0! = 1$ ✓
- Inductive step: $\Gamma(n + 1) = n \cdot \Gamma(n) = n \cdot (n-1)! = n!$ ✓

### Half-Integer Values

Combining the recursion with $\Gamma(1/2) = \sqrt{\pi}$:

$$\Gamma(3/2) = \frac{1}{2}\sqrt{\pi}, \qquad \Gamma(5/2) = \frac{3}{4}\sqrt{\pi}, \qquad \Gamma(n + 1/2) = \frac{(2n)!}{4^n \, n!} \sqrt{\pi}$$

## Role as Normalizing Constant

The Gamma function ensures that the Gamma distribution PDF integrates to 1. For the $\Gamma(\alpha, \lambda)$ distribution:

$$\int_0^\infty \frac{\lambda(\lambda x)^{\alpha - 1} e^{-\lambda x}}{\Gamma(\alpha)} \, dx = 1$$

This can be verified by substituting $u = \lambda x$:

$$\frac{1}{\Gamma(\alpha)} \int_0^\infty u^{\alpha - 1} e^{-u} \, du = \frac{\Gamma(\alpha)}{\Gamma(\alpha)} = 1$$

## The Beta Function Connection

The **Beta function** is closely related to the Gamma function:

$$B(\alpha, \beta) = \int_0^1 x^{\alpha - 1} (1 - x)^{\beta - 1} \, dx = \frac{\Gamma(\alpha) \, \Gamma(\beta)}{\Gamma(\alpha + \beta)}$$

This identity is proved via the Gamma-Beta connection through independent Gamma random variables (see the Beta distribution section in Chapter 15).

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma, factorial
from scipy.integrate import quad

# Verify Gamma function properties
print("=== Gamma Function Properties ===")
print(f"Γ(1) = {gamma(1):.6f} (should be 1)")
print(f"Γ(2) = {gamma(2):.6f} (should be 1)")
print(f"Γ(1/2) = {gamma(0.5):.6f} (should be √π = {np.sqrt(np.pi):.6f})")
print(f"Γ(3/2) = {gamma(1.5):.6f} (should be √π/2 = {np.sqrt(np.pi)/2:.6f})")
print()

# Verify factorial connection
for n in range(1, 8):
    print(f"Γ({n+1}) = {gamma(n+1):.1f}, {n}! = {factorial(n, exact=True)}")

# Plot the Gamma function
x = np.linspace(0.01, 5.5, 500)
y = gamma(x)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Gamma function
axes[0].plot(x, y, 'b-', lw=2)
# Mark integer values
for n in range(1, 6):
    axes[0].plot(n, gamma(n), 'ro', markersize=8)
    axes[0].annotate(f'Γ({n})={gamma(n):.0f}',
                     xy=(n, gamma(n)), xytext=(n+0.1, gamma(n)+1),
                     fontsize=9)
axes[0].set_title('Gamma Function Γ(α)')
axes[0].set_xlabel('α')
axes[0].set_ylabel('Γ(α)')
axes[0].set_ylim(0, 30)
axes[0].grid(True, alpha=0.3)

# Verify recursion: Γ(α+1) = α·Γ(α)
alpha_vals = np.linspace(0.1, 5, 100)
lhs = gamma(alpha_vals + 1)
rhs = alpha_vals * gamma(alpha_vals)
axes[1].plot(alpha_vals, lhs, 'b-', lw=2, label='Γ(α+1)')
axes[1].plot(alpha_vals, rhs, 'r--', lw=2, label='α·Γ(α)')
axes[1].set_title('Recursion Property: Γ(α+1) = α·Γ(α)')
axes[1].set_xlabel('α')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('gamma_function.png', dpi=150, bbox_inches='tight')
plt.show()

# Numerical verification of the integral definition
for alpha in [0.5, 1.0, 2.0, 3.0, 4.5]:
    result, _ = quad(lambda x: x**(alpha-1) * np.exp(-x), 0, np.inf)
    print(f"∫x^({alpha}-1)e^(-x)dx = {result:.6f}, Γ({alpha}) = {gamma(alpha):.6f}")
```
