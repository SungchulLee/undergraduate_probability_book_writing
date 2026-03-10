# The Gamma Function

The Gamma function extends the factorial to non-integer (and even complex) arguments and serves as the normalizing constant for the Gamma distribution.

## Definition

For $\alpha > 0$, the **Gamma function** is

$$
\Gamma(\alpha) = \int_0^\infty x^{\alpha - 1} e^{-x} \, dx
$$

**Key values:**

$$
\Gamma(1) = 1, \qquad \Gamma(1/2) = \sqrt{\pi}, \qquad \Gamma(n+1) = n! \text{ for } n = 0, 1, 2, \ldots
$$

**Recursion:**

$$
\Gamma(\alpha + 1) = \alpha \, \Gamma(\alpha)
$$

**Beta function connection:**

$$
B(\alpha, \beta) = \int_0^1 x^{\alpha - 1}(1 - x)^{\beta - 1} \, dx = \frac{\Gamma(\alpha)\,\Gamma(\beta)}{\Gamma(\alpha + \beta)}
$$

## Explanation

### Proof of the Recursion Property

Integration by parts with $u = x^\alpha$ and $dv = e^{-x} \, dx$ gives

$$
\Gamma(\alpha + 1) = \int_0^\infty x^\alpha e^{-x} \, dx = \left[-x^\alpha e^{-x}\right]_0^\infty + \alpha \int_0^\infty x^{\alpha - 1} e^{-x} \, dx
$$

The boundary term vanishes (exponential decay dominates polynomial growth), leaving

$$
\Gamma(\alpha + 1) = \alpha \, \Gamma(\alpha)
$$

### Proof that Gamma(n+1) = n!

By induction using the recursion:

- **Base case:** $\Gamma(1) = \int_0^\infty e^{-x} \, dx = 1 = 0!$
- **Inductive step:** $\Gamma(n+1) = n \cdot \Gamma(n) = n \cdot (n-1)! = n!$

Therefore $\Gamma(n+1) = n!$ for all non-negative integers $n$.

An equivalent and widely used form: $\Gamma(k) = (k-1)!$ for positive integers $k$. This is the convention that appears in the Gamma distribution PDF.

### Proof that Gamma(1/2) = sqrt(pi)

Substitute $x = s^2$ (so $dx = 2s \, ds$):

$$
\Gamma(1/2) = \int_0^\infty x^{-1/2} e^{-x} \, dx = \int_0^\infty \frac{1}{s} e^{-s^2} \cdot 2s \, ds = 2 \int_0^\infty e^{-s^2} \, ds = \sqrt{\pi}
$$

The last step uses the Gaussian integral $\int_0^\infty e^{-s^2} \, ds = \sqrt{\pi}/2$, which is proved by squaring the integral and switching to polar coordinates.

### Half-Integer Values

Combining the recursion with $\Gamma(1/2) = \sqrt{\pi}$:

$$
\Gamma(3/2) = \frac{1}{2}\sqrt{\pi}, \qquad \Gamma(5/2) = \frac{3}{4}\sqrt{\pi}, \qquad \Gamma(7/2) = \frac{15}{8}\sqrt{\pi}
$$

The general formula is

$$
\Gamma\!\left(n + \frac{1}{2}\right) = \frac{(2n)!}{4^n \, n!} \sqrt{\pi}
$$

### Role as Normalizing Constant

The Gamma function ensures that the Gamma distribution PDF integrates to 1. For $X \sim \Gamma(\alpha, \lambda)$:

$$
\int_0^\infty \frac{\lambda(\lambda x)^{\alpha - 1} e^{-\lambda x}}{\Gamma(\alpha)} \, dx = \frac{1}{\Gamma(\alpha)} \int_0^\infty u^{\alpha - 1} e^{-u} \, du = \frac{\Gamma(\alpha)}{\Gamma(\alpha)} = 1
$$

after substituting $u = \lambda x$. Without the $\Gamma(\alpha)$ in the denominator, the PDF would not normalize to 1.

### The Beta Function Connection

The Beta function $B(\alpha, \beta)$ arises naturally when dividing one Gamma random variable by the sum of two independent Gamma random variables. The identity

$$
B(\alpha, \beta) = \frac{\Gamma(\alpha)\,\Gamma(\beta)}{\Gamma(\alpha + \beta)}
$$

is proved using independent Gamma random variables in the Beta distribution chapter (Chapter 15).

## Examples

**Example 1.** Evaluate $\Gamma(6)$, $\Gamma(5/2)$, and $B(3, 4)$.

- $\Gamma(6) = 5! = 120$
- $\Gamma(5/2) = \frac{3}{2} \cdot \Gamma(3/2) = \frac{3}{2} \cdot \frac{1}{2} \cdot \Gamma(1/2) = \frac{3}{4}\sqrt{\pi} \approx 1.3293$
- $B(3, 4) = \frac{\Gamma(3)\Gamma(4)}{\Gamma(7)} = \frac{2! \cdot 3!}{6!} = \frac{12}{720} = \frac{1}{60}$

**Example 2.** Verify the Gamma function properties numerically.

```python
import numpy as np
from scipy.special import gamma
from scipy.integrate import quad

# --- Factorial connection ---
print("=== Gamma(n+1) = n! ===")
for n in range(7):
    print(f"Gamma({n+1}) = {gamma(n+1):.1f},  {n}! = {np.math.factorial(n)}")

# --- Special values ---
print(f"\n=== Special Values ===")
print(f"Gamma(1)   = {gamma(1):.6f}  (should be 1)")
print(f"Gamma(1/2) = {gamma(0.5):.6f}  (should be sqrt(pi) = "
      f"{np.sqrt(np.pi):.6f})")
print(f"Gamma(3/2) = {gamma(1.5):.6f}  (should be sqrt(pi)/2 = "
      f"{np.sqrt(np.pi)/2:.6f})")
print(f"Gamma(5/2) = {gamma(2.5):.6f}  (should be 3*sqrt(pi)/4 = "
      f"{3*np.sqrt(np.pi)/4:.6f})")

# --- Recursion verification ---
print(f"\n=== Recursion: Gamma(a+1) = a * Gamma(a) ===")
for a in [0.5, 1.5, 2.7, 4.0]:
    lhs = gamma(a + 1)
    rhs = a * gamma(a)
    print(f"a={a}: Gamma({a+1}) = {lhs:.6f}, a*Gamma({a}) = {rhs:.6f}")

# --- Numerical integration check ---
print(f"\n=== Integral Definition ===")
for alpha in [0.5, 1.0, 2.0, 3.5]:
    result, _ = quad(lambda x: x**(alpha-1) * np.exp(-x), 0, np.inf)
    print(f"integral for alpha={alpha}: {result:.6f}, "
          f"Gamma({alpha}) = {gamma(alpha):.6f}")

# --- Beta function ---
from scipy.special import beta
B_val = beta(3, 4)
formula = gamma(3) * gamma(4) / gamma(7)
print(f"\n=== Beta Function ===")
print(f"B(3,4) = {B_val:.6f}, Gamma(3)*Gamma(4)/Gamma(7) = {formula:.6f}, "
      f"1/60 = {1/60:.6f}")
```
