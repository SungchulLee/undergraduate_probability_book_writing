# Standardization


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Standardization of a Random Variable

If $X$ has mean $\mu$ and standard deviation $\sigma$, then:

$$Z = \frac{X - \mu}{\sigma}$$

has mean $0$ and standard deviation $1$.

If $X$ is normal, then $Z$ is also normal, i.e., $Z \sim N(0,1)$.

## Reverse Standardization

If $Z$ has mean $0$ and standard deviation $1$, then:

$$X = \mu + \sigma Z$$

has mean $\mu$ and standard deviation $\sigma$.

If $Z$ is normal, then $X$ is also normal, i.e., $X \sim N(\mu, \sigma^2)$.

## Standardization in the CLT

The CLT tells us that for iid $X_1, \ldots, X_n$ with mean $\mu$ and variance $\sigma^2$:

$$Z_n = \frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0,1)$$

This means the **standardized sum** converges to the standard normal. Equivalently, by reverse standardization:

$$S_n \approx n\mu + \sigma\sqrt{n} \cdot Z \quad \text{where } Z \sim N(0,1)$$

so $S_n \approx N(n\mu, \, n\sigma^2)$.

## Using Standardization to Compute Probabilities

To approximate $P(a \leq S_n \leq b)$:

**Step 1.** Standardize:

$$P(a \leq S_n \leq b) = P\left(\frac{a - n\mu}{\sigma\sqrt{n}} \leq \frac{S_n - n\mu}{\sigma\sqrt{n}} \leq \frac{b - n\mu}{\sigma\sqrt{n}}\right)$$

**Step 2.** Apply the CLT approximation:

$$\approx \Phi\left(\frac{b - n\mu}{\sigma\sqrt{n}}\right) - \Phi\left(\frac{a - n\mu}{\sigma\sqrt{n}}\right)$$

where $\Phi$ is the CDF of $N(0,1)$.
