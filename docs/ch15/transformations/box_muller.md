# Box-Muller Transform


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The **Box-Muller transform** generates standard normal random samples from uniform random samples. This is a fundamental technique in simulation and Monte Carlo methods.

## Method 1: Basic Box-Muller

**Step 1.** Generate two iid $U_1, U_2 \sim U(0, 1)$.

**Step 2.** Set:

$$\Theta = 2\pi U_1, \qquad R^2 = -2\log U_2$$

**Step 3.** Set:

$$Z_1 = R\cos\Theta, \qquad Z_2 = R\sin\Theta$$

Then $Z_1$ and $Z_2$ are **iid** $N(0, 1)$.

### Why It Works

The derivation relies on two background facts.

**Fact 1:** If $U \sim U(0, 1)$, then $V = -2\log U \sim \text{Exp}(1/2)$.

*Proof:*

$$P(V \leq v) = P(-2\log U \leq v) = P\left(\log U \geq -\frac{v}{2}\right) = P\left(U \geq e^{-v/2}\right) = 1 - e^{-v/2}$$

so $f_V(v) = \frac{1}{2}e^{-v/2}$, which is the PDF of $\text{Exp}(1/2)$.

**Fact 2:** If $X, Y \sim N(0,1)$ are iid, let $S = X^2 + Y^2$ and $\Theta = \tan^{-1}(Y/X)$. Then:

- $\Theta \sim U(0, 2\pi)$
- $S \sim \text{Exp}(1/2)$
- $S$ and $\Theta$ are independent

*Proof:* Transform $(X, Y)$ to polar coordinates $(S, \Theta)$ where $X = \sqrt{S}\cos\Theta$, $Y = \sqrt{S}\sin\Theta$, and $S = R^2$. The Jacobian is:

$$\left|\frac{\partial(x,y)}{\partial(s,\theta)}\right| = \begin{vmatrix} \frac{1}{2\sqrt{s}}\cos\theta & -\sqrt{s}\sin\theta \\ \frac{1}{2\sqrt{s}}\sin\theta & \sqrt{s}\cos\theta \end{vmatrix} = \frac{1}{2}$$

The joint density transforms as:

$$f_{S,\Theta}(s, \theta) = f_X(x)f_Y(y) \cdot \left|\frac{\partial(x,y)}{\partial(s,\theta)}\right|$$

$$= \frac{1}{\sqrt{2\pi}}e^{-x^2/2} \cdot \frac{1}{\sqrt{2\pi}}e^{-y^2/2} \cdot \frac{1}{2} = \frac{1}{4\pi}e^{-(x^2+y^2)/2} = \underbrace{\frac{1}{2\pi}}_{\Theta \sim U(0,2\pi)} \cdot \underbrace{\frac{1}{2}e^{-s/2}}_{S \sim \text{Exp}(1/2)}$$

The joint density factors, confirming independence and the marginal distributions.

**The Box-Muller transform reverses this relationship:** since $R^2 = -2\log U_2 \sim \text{Exp}(1/2)$ and $\Theta = 2\pi U_1 \sim U(0, 2\pi)$ are independent, the Cartesian coordinates $Z_1 = R\cos\Theta$ and $Z_2 = R\sin\Theta$ must be iid $N(0,1)$.

## Method 2: Marsaglia Polar Method

**Step 1.** Generate two iid $U_1, U_2 \sim U(0, 1)$.

**Step 2.** Set $V_i = 2U_i - 1$ (so $V_i \sim U(-1, 1)$).

**Step 3.** Compute $r^2 = V_1^2 + V_2^2$. **Reject** and repeat if $r^2 > 1$ (i.e., $(V_1, V_2)$ is outside the unit circle).

**Step 4.** Set:

$$Z_i = V_i \sqrt{\frac{-2\log r^2}{r^2}}$$

Then $Z_1, Z_2$ are iid $N(0, 1)$.

The Marsaglia method avoids computing trigonometric functions (sin, cos), trading them for a rejection step. The acceptance probability is $\pi/4 \approx 78.5\%$.

## Python Implementation

```python
import numpy as np

def box_muller(n):
    """Generate n standard normal samples using Box-Muller."""
    U1 = np.random.uniform(0, 1, (n + 1) // 2)
    U2 = np.random.uniform(0, 1, (n + 1) // 2)
    
    R = np.sqrt(-2 * np.log(U2))
    Theta = 2 * np.pi * U1
    
    Z1 = R * np.cos(Theta)
    Z2 = R * np.sin(Theta)
    
    samples = np.concatenate([Z1, Z2])
    return samples[:n]

# Generate and verify
np.random.seed(42)
Z = box_muller(100000)
print(f"Box-Muller samples (n=100000):")
print(f"  Mean: {Z.mean():.4f}  (expected: 0)")
print(f"  Var:  {Z.var():.4f}  (expected: 1)")
print(f"  Skew: {float(np.mean(((Z - Z.mean())/Z.std())**3)):.4f}  (expected: 0)")
```

**Output:**
```
Box-Muller samples (n=100000):
  Mean: -0.0014  (expected: 0)
  Var:  1.0012  (expected: 1)
  Skew: -0.0068  (expected: 0)
```
