# Identifying Distributions via MGFs
<<<<<<< Updated upstream

## The Strategy

The MGF identification method has three steps:

1. **Compute** the MGF of the random variable of interest (often a sum).
2. **Recognize** the result as the MGF of a known distribution.
3. **Conclude** by the uniqueness theorem that the two distributions are identical.

This avoids working directly with convolutions or CDFs, which can be much harder.

## MGF Reference Table

| Distribution | MGF $M_X(t)$ | Domain |
|:---|:---:|:---:|
| $\text{Bernoulli}(p)$ | $1 + p(e^t - 1)$ | all $t$ |
| $B(n, p)$ | $[1 + p(e^t - 1)]^n$ | all $t$ |
| $\text{Po}(\lambda)$ | $e^{\lambda(e^t - 1)}$ | all $t$ |
| $\text{Geo}(p)$ | $\frac{pe^t}{1 - (1-p)e^t}$ | $t < -\ln(1-p)$ |
| $\text{NB}(r, p)$ | $\left[\frac{pe^t}{1-(1-p)e^t}\right]^r$ | $t < -\ln(1-p)$ |
| $\text{Exp}(\lambda)$ | $\frac{\lambda}{\lambda - t}$ | $t < \lambda$ |
| $\text{Gamma}(\alpha, \lambda)$ | $\left(\frac{\lambda}{\lambda - t}\right)^\alpha$ | $t < \lambda$ |
| $N(\mu, \sigma^2)$ | $e^{\mu t + \frac{1}{2}\sigma^2 t^2}$ | all $t$ |

## Example: Sum of Independent Poissons

Let $X \sim \text{Po}(\lambda)$ and $Y \sim \text{Po}(\mu)$ be independent.

**Step 1.** Compute:

$$M_{X+Y}(t) = e^{\lambda(e^t - 1)} \cdot e^{\mu(e^t - 1)} = e^{(\lambda + \mu)(e^t - 1)}$$

**Step 2.** Recognize: this is the MGF of $\text{Po}(\lambda + \mu)$.

**Step 3.** Conclude: $X + Y \sim \text{Po}(\lambda + \mu)$.

## Example: Sum of Independent Normals

Let $X \sim N(\mu_1, \sigma_1^2)$ and $Y \sim N(\mu_2, \sigma_2^2)$ be independent.

**Step 1.** Compute:

$$M_{X+Y}(t) = e^{\mu_1 t + \frac{1}{2}\sigma_1^2 t^2} \cdot e^{\mu_2 t + \frac{1}{2}\sigma_2^2 t^2} = e^{(\mu_1+\mu_2)t + \frac{1}{2}(\sigma_1^2 + \sigma_2^2)t^2}$$

**Step 2.** Recognize: this is the MGF of $N(\mu_1 + \mu_2, \, \sigma_1^2 + \sigma_2^2)$.

**Step 3.** Conclude: $X + Y \sim N(\mu_1 + \mu_2, \, \sigma_1^2 + \sigma_2^2)$.

## Example: Sum of Independent Gammas (Same Rate)

Let $X \sim \text{Gamma}(\alpha_1, \lambda)$ and $Y \sim \text{Gamma}(\alpha_2, \lambda)$ be independent.

**Step 1.** Compute:

$$M_{X+Y}(t) = \left(\frac{\lambda}{\lambda - t}\right)^{\alpha_1} \cdot \left(\frac{\lambda}{\lambda - t}\right)^{\alpha_2} = \left(\frac{\lambda}{\lambda - t}\right)^{\alpha_1 + \alpha_2}$$

**Step 2.** Recognize: this is the MGF of $\text{Gamma}(\alpha_1 + \alpha_2, \lambda)$.

**Step 3.** Conclude: $X + Y \sim \text{Gamma}(\alpha_1 + \alpha_2, \lambda)$.

!!! warning "Same Rate Parameter Required"
    The gamma additivity result requires the same rate $\lambda$. If $X \sim \text{Gamma}(\alpha_1, \lambda_1)$ and $Y \sim \text{Gamma}(\alpha_2, \lambda_2)$ with $\lambda_1 \neq \lambda_2$, the sum is **not** gamma-distributed.

## Example: Sum of Independent Binomials (Same $p$)

Let $X \sim B(n_1, p)$ and $Y \sim B(n_2, p)$ be independent.

$$M_{X+Y}(t) = [1 + p(e^t - 1)]^{n_1} \cdot [1 + p(e^t - 1)]^{n_2} = [1 + p(e^t - 1)]^{n_1 + n_2}$$

This is the MGF of $B(n_1 + n_2, p)$, so $X + Y \sim B(n_1 + n_2, p)$.

## Summary of Closure Properties

| Family | Condition | Result |
|:---|:---|:---|
| Poisson | independent | $\text{Po}(\lambda) + \text{Po}(\mu) = \text{Po}(\lambda + \mu)$ |
| Normal | independent | $N(\mu_1, \sigma_1^2) + N(\mu_2, \sigma_2^2) = N(\mu_1+\mu_2, \sigma_1^2+\sigma_2^2)$ |
| Gamma | independent, same $\lambda$ | $\text{Gamma}(\alpha_1, \lambda) + \text{Gamma}(\alpha_2, \lambda) = \text{Gamma}(\alpha_1+\alpha_2, \lambda)$ |
| Binomial | independent, same $p$ | $B(n_1, p) + B(n_2, p) = B(n_1+n_2, p)$ |
| NB | independent, same $p$ | $\text{NB}(r_1, p) + \text{NB}(r_2, p) = \text{NB}(r_1+r_2, p)$ |
=======
>>>>>>> Stashed changes
