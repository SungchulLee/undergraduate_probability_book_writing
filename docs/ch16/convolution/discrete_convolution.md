# Convolution for Discrete Random Variables


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Definition

!!! info "Convolution (Discrete)"
    If $X$ and $Y$ are **independent** discrete random variables, the **convolution** of their PMFs gives the PMF of $X + Y$:

    $$(p_X * p_Y)(a) = p_{X+Y}(a) = \sum_b p_X(b) \cdot p_Y(a - b)$$

    The sum ranges over all values $b$ where both $p_X(b) > 0$ and $p_Y(a - b) > 0$.

### Notation

| Notation | Meaning |
|:---:|:---|
| $F_X * F_Y$ | CDF of $X + Y$ when $X, Y$ independent |
| $p_X * p_Y$ | PMF of $X + Y$ when $X, Y$ independent |
| $f_X * f_Y$ | PDF of $X + Y$ when $X, Y$ independent |

### Derivation

By the law of total probability, conditioning on $X = b$:

$$P(X + Y = a) = \sum_b P(X + Y = a \mid X = b) \cdot P(X = b)$$

$$= \sum_b P(Y = a - b \mid X = b) \cdot P(X = b) = \sum_b p_Y(a - b) \cdot p_X(b)$$

The last step uses independence: $P(Y = a - b \mid X = b) = P(Y = a - b)$.

## CDF Convolution

The CDF version of convolution is:

$$(F_X * F_Y)(a) = F_{X+Y}(a) = \sum_b F_Y(a - b) \cdot p_X(b)$$

where we sum over all values $b$ in the support of $X$, weighing $F_Y(a - b)$ by $P(X = b)$.

## Properties of Convolution

1. **Commutativity:** $p_X * p_Y = p_Y * p_X$
2. **Associativity:** $(p_X * p_Y) * p_Z = p_X * (p_Y * p_Z)$
3. **Requires independence:** Convolution only gives the distribution of $X + Y$ when $X$ and $Y$ are independent

Associativity means we can compute the distribution of $X_1 + X_2 + \cdots + X_n$ by convolving one distribution at a time.

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt

# Discrete convolution example: sum of two dice
# X, Y ~ DiscreteUniform{1,2,3,4,5,6}

# PMFs (indexed 0-5 for values 1-6)
p = np.ones(6) / 6

# Convolve to get PMF of X + Y (values 2 through 12)
p_sum = np.convolve(p, p)
values = np.arange(2, 13)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# PMF of sum of two dice
axes[0].bar(values, p_sum, color='steelblue', alpha=0.7, edgecolor='black')
axes[0].set_title('PMF of Sum of Two Fair Dice')
axes[0].set_xlabel('Sum')
axes[0].set_ylabel('P(X+Y = k)')
axes[0].set_xticks(values)
axes[0].grid(True, alpha=0.3)

# Verify via simulation
np.random.seed(42)
n_sim = 100000
X = np.random.randint(1, 7, n_sim)
Y = np.random.randint(1, 7, n_sim)
S = X + Y

counts = np.bincount(S, minlength=13)[2:13]
probs_sim = counts / n_sim

axes[1].bar(values - 0.15, p_sum, 0.3, color='steelblue', alpha=0.7,
            label='Convolution', edgecolor='black')
axes[1].bar(values + 0.15, probs_sim, 0.3, color='orange', alpha=0.7,
            label='Simulation', edgecolor='black')
axes[1].set_title('Convolution vs Simulation')
axes[1].set_xlabel('Sum')
axes[1].set_ylabel('Probability')
axes[1].set_xticks(values)
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('discrete_convolution.png', dpi=150, bbox_inches='tight')
plt.show()

print("Sum | Convolution | Simulation")
print("-" * 35)
for v, pc, ps in zip(values, p_sum, probs_sim):
    print(f"  {v:2d} |    {pc:.4f}    |   {ps:.4f}")
```
