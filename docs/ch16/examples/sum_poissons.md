# Sum of Independent Poissons (via Convolution)

## Result

!!! info "Convolution of Poisson Distributions"
    If $X \sim \text{Po}(\lambda_1)$ and $Y \sim \text{Po}(\lambda_2)$ are independent, then:

    $$X + Y \sim \text{Po}(\lambda_1 + \lambda_2)$$

    In convolution notation: $\text{Po}(\lambda_1) * \text{Po}(\lambda_2) = \text{Po}(\lambda_1 + \lambda_2)$

## Proof via Convolution

For a non-negative integer $a$:

$$p_{X+Y}(a) = \sum_b p_X(b) \, p_Y(a - b)$$

The sum runs over $b \geq 0$ and $a - b \geq 0$, i.e., $0 \leq b \leq a$ (integers):

$$p_{X+Y}(a) = \sum_{b=0}^{a} \frac{\lambda_1^b}{b!} e^{-\lambda_1} \cdot \frac{\lambda_2^{a-b}}{(a-b)!} e^{-\lambda_2}$$

Factor out $e^{-(\lambda_1 + \lambda_2)}$:

$$= e^{-(\lambda_1 + \lambda_2)} \sum_{b=0}^{a} \frac{\lambda_1^b}{b!} \cdot \frac{\lambda_2^{a-b}}{(a-b)!}$$

Multiply and divide by $a!$:

$$= \frac{e^{-(\lambda_1 + \lambda_2)}}{a!} \sum_{b=0}^{a} \frac{a!}{b!(a-b)!} \lambda_1^b \lambda_2^{a-b}$$

Recognize the **Binomial Theorem**: $\sum_{b=0}^{a} \binom{a}{b} \lambda_1^b \lambda_2^{a-b} = (\lambda_1 + \lambda_2)^a$:

$$= \frac{(\lambda_1 + \lambda_2)^a}{a!} e^{-(\lambda_1 + \lambda_2)}$$

This is the PMF of $\text{Po}(\lambda_1 + \lambda_2)$. $\square$

## Alternative Proof via MGFs

The MGF approach is more concise:

$$M_{X+Y}(t) = M_X(t) \cdot M_Y(t) = e^{\lambda_1(e^t - 1)} \cdot e^{\lambda_2(e^t - 1)} = e^{(\lambda_1 + \lambda_2)(e^t - 1)}$$

which is the MGF of $\text{Po}(\lambda_1 + \lambda_2)$. By uniqueness of MGFs, $X + Y \sim \text{Po}(\lambda_1 + \lambda_2)$.

## General Sum

By induction (or associativity of convolution):

If $X_1, X_2, \ldots, X_n$ are independent with $X_i \sim \text{Po}(\lambda_i)$, then:

$$X_1 + X_2 + \cdots + X_n \sim \text{Po}(\lambda_1 + \lambda_2 + \cdots + \lambda_n)$$

## Connection to the Poisson Process

This result follows naturally from the **merging property** of Poisson processes: if two independent Poisson processes with rates $\lambda_1$ and $\lambda_2$ are superimposed, the merged process is Poisson with rate $\lambda_1 + \lambda_2$.

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 100000

lambda1, lambda2 = 3.0, 5.0

# Simulate
X = np.random.poisson(lambda1, n_sim)
Y = np.random.poisson(lambda2, n_sim)
S = X + Y

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Compare simulation with theory
k_vals = np.arange(0, 25)
pmf_theory = stats.poisson.pmf(k_vals, lambda1 + lambda2)

counts = np.bincount(S, minlength=25)[:25]
pmf_sim = counts / n_sim

axes[0].bar(k_vals - 0.15, pmf_sim, 0.3, color='steelblue', alpha=0.7,
            label='Simulation', edgecolor='black')
axes[0].bar(k_vals + 0.15, pmf_theory, 0.3, color='orange', alpha=0.7,
            label=f'Po({lambda1+lambda2})', edgecolor='black')
axes[0].set_title(f'Po({lambda1}) + Po({lambda2}) = Po({lambda1+lambda2})')
axes[0].set_xlabel('k')
axes[0].set_ylabel('P(X+Y = k)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Verify the convolution computation step by step
pmf_x = stats.poisson.pmf(k_vals, lambda1)
pmf_y = stats.poisson.pmf(k_vals, lambda2)
pmf_conv = np.convolve(pmf_x, pmf_y)[:25]

axes[1].bar(k_vals - 0.15, pmf_conv, 0.3, color='green', alpha=0.7,
            label='Numerical convolution', edgecolor='black')
axes[1].bar(k_vals + 0.15, pmf_theory, 0.3, color='orange', alpha=0.7,
            label=f'Po({lambda1+lambda2}) PMF', edgecolor='black')
axes[1].set_title('Numerical Convolution vs Theory')
axes[1].set_xlabel('k')
axes[1].set_ylabel('P(X+Y = k)')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('sum_poissons.png', dpi=150, bbox_inches='tight')
plt.show()

print(f"Simulation: mean={np.mean(S):.4f} (theory {lambda1+lambda2:.4f})")
print(f"Simulation: var={np.var(S):.4f} (theory {lambda1+lambda2:.4f})")
```
