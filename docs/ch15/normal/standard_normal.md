# Standard Normal and Z-Scores

The standard normal distribution $N(0,1)$ serves as the universal reference for all normal distributions, and the Z-score provides the link between any normal random variable and the standard normal table.

## Definition

Let $Z \sim N(0, 1)$ denote a **standard normal** random variable. Its PDF and CDF are:

$$
\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}, \qquad \Phi(z) = \int_{-\infty}^{z} \phi(s)\,ds
$$

The **Z-score** of a value $x$ from a $N(\mu, \sigma^2)$ distribution is:

$$
z = \frac{x - \mu}{\sigma}
$$

If $X \sim N(\mu, \sigma^2)$, then the random variable $Z = \frac{X - \mu}{\sigma}$ satisfies $Z \sim N(0, 1)$. The Z-score measures how many standard deviations $x$ lies from the mean.

## Explanation

### CDF properties and symmetry

The standard normal CDF $\Phi$ has the following key properties:

| Property | Formula |
|----------|---------|
| Interval probability | $P(a \leq Z \leq b) = \Phi(b) - \Phi(a)$ |
| Left-tail symmetry | $\Phi(-z) = 1 - \Phi(z)$ |
| Right-tail complement | $P(Z \geq z) = 1 - \Phi(z)$ |
| Median | $\Phi(0) = 0.5$ |

The symmetry relation $\Phi(-z) = 1 - \Phi(z)$ follows from the symmetry of the bell curve about zero. This means that a table listing $\Phi(z)$ only for $z \geq 0$ is sufficient: for negative arguments, use the identity.

### Standardization of a general normal

For any $X \sim N(\mu, \sigma^2)$, probabilities can be computed via standardization:

$$
P(X \leq x) = P\!\left(\frac{X - \mu}{\sigma} \leq \frac{x - \mu}{\sigma}\right) = \Phi\!\left(\frac{x - \mu}{\sigma}\right)
$$

This is the fundamental technique for computing normal probabilities: convert to a Z-score, then look up (or compute) the standard normal CDF.

### Interpreting Z-scores

A Z-score tells you the relative position within a normal distribution:

| Z-score | Interpretation |
|---------|---------------|
| $z = 0$ | At the mean |
| $z = 1$ | One standard deviation above the mean |
| $z = -2$ | Two standard deviations below the mean |
| $\lvert z \rvert > 3$ | Unusually extreme (less than 0.3% probability) |

### Quantiles

The $\alpha$-quantile $z_\alpha$ of $N(0,1)$ is defined by $\Phi(z_\alpha) = \alpha$, or equivalently $z_\alpha = \Phi^{-1}(\alpha)$.

For $X \sim N(\mu, \sigma^2)$, the $\alpha$-quantile is:

$$
q_\alpha = \mu + \sigma \cdot z_\alpha
$$

Common quantiles of the standard normal:

| $\alpha$ | $z_\alpha$ |
|----------|-----------|
| $0.025$ | $-1.960$ |
| $0.05$ | $-1.645$ |
| $0.10$ | $-1.282$ |
| $0.50$ | $0$ |
| $0.90$ | $1.282$ |
| $0.95$ | $1.645$ |
| $0.975$ | $1.960$ |

### Reading a Z-table

A standard normal table lists values of $\Phi(z)$ for $z$ from $0.00$ to about $3.49$. To use it:

1. **For positive z:** Read $\Phi(z)$ directly from the table.
2. **For negative z:** Use $\Phi(-z) = 1 - \Phi(z)$.
3. **For tail probabilities:** $P(Z > z) = 1 - \Phi(z)$.
4. **For intervals:** $P(a < Z < b) = \Phi(b) - \Phi(a)$.

In practice, software functions like `scipy.stats.norm.cdf` replace the need for printed tables.

## Examples

**Example 1: Standard normal interval probability.**

Compute $P(-1 \leq Z \leq 2)$.

$$
P(-1 \leq Z \leq 2) = \Phi(2) - \Phi(-1) = \Phi(2) - (1 - \Phi(1)) = 0.9772 - 0.1587 = 0.8186
$$

```python
from scipy import stats

p = stats.norm.cdf(2) - stats.norm.cdf(-1)
print(f"P(-1 <= Z <= 2) = {p:.4f}")
```

**Output:**
```
P(-1 <= Z <= 2) = 0.8186
```

**Example 2: IQ scores.**

IQ scores follow $X \sim N(100, 15^2)$. Find the probability that a randomly selected person has an IQ above 130.

The Z-score is $z = (130 - 100)/15 = 2.00$.

$$
P(X > 130) = P(Z > 2) = 1 - \Phi(2) = 1 - 0.9772 = 0.0228
$$

```python
from scipy import stats

mu, sigma = 100, 15
x = 130
z = (x - mu) / sigma
p = 1 - stats.norm.cdf(z)
print(f"Z-score of {x}: z = ({x} - {mu}) / {sigma} = {z:.2f}")
print(f"P(X > {x}) = P(Z > {z:.2f}) = 1 - Phi({z:.2f}) = {p:.4f}")
print(f"About {100*p:.2f}% of the population has IQ above {x}")
```

**Output:**
```
Z-score of 130: z = (130 - 100) / 15 = 2.00
P(X > 130) = P(Z > 2.00) = 1 - Phi(2.00) = 0.0228
About 2.28% of the population has IQ above 130
```

**Example 3: Quantile of a general normal.**

The weights of packages follow $X \sim N(50, 4^2)$ grams. Find the weight that 95% of packages fall below.

$$
q_{0.95} = \mu + \sigma \cdot z_{0.95} = 50 + 4 \times 1.645 = 56.58
$$

```python
from scipy import stats

mu, sigma = 50, 4
alpha = 0.95
z_alpha = stats.norm.ppf(alpha)
q = mu + sigma * z_alpha
print(f"z_{{0.95}} = {z_alpha:.4f}")
print(f"95th percentile of N({mu}, {sigma}^2) = {mu} + {sigma} * {z_alpha:.4f} = {q:.2f} grams")

# Verify
print(f"P(X <= {q:.2f}) = {stats.norm.cdf(q, loc=mu, scale=sigma):.4f}")
```

**Output:**
```
z_{0.95} = 1.6449
95th percentile of N(50, 4^2) = 50 + 4 * 1.6449 = 56.58 grams
P(X <= 56.58) = 0.9500
```

**Example 4: Comparing scores from different distributions.**

Alice scored 85 on a test with $N(70, 10^2)$ and Bob scored 92 on a test with $N(78, 8^2)$. Who performed better relative to their class?

```python
from scipy import stats

z_alice = (85 - 70) / 10
z_bob = (92 - 78) / 8
print(f"Alice: z = (85 - 70) / 10 = {z_alice:.2f}")
print(f"Bob:   z = (92 - 78) / 8  = {z_bob:.2f}")
print(f"Alice's percentile: {100*stats.norm.cdf(z_alice):.1f}%")
print(f"Bob's percentile:   {100*stats.norm.cdf(z_bob):.1f}%")
print(f"Bob performed better relative to his class (higher Z-score)")
```

**Output:**
```
Alice: z = (85 - 70) / 10 = 1.50
Bob:   z = (92 - 78) / 8  = 1.75
Alice's percentile: 93.3%
Bob's percentile:   96.0%
Bob performed better relative to his class (higher Z-score)
```
