# Sample Mean and Sample Variance

## Setup

Let $X_1, X_2, \ldots, X_n$ be **iid** random variables from $N(\mu, \sigma^2)$. The two fundamental summary statistics are:

**Sample Mean:**

$$\bar{X} = \frac{\sum_{i=1}^n X_i}{n}$$

**Sample Variance:**

$$S^2 = \frac{\sum_{i=1}^n (X_i - \bar{X})^2}{n - 1}$$

## Distributional Properties

### Distribution of the Sample Mean

Since $X_i \sim N(\mu, \sigma^2)$ are independent, the sample mean is a linear combination of normals:

$$\bar{X} \sim N\!\left(\mu, \frac{\sigma^2}{n}\right)$$

Standardizing:

$$\frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0, 1)$$

### Distribution of the Sample Variance

The scaled sample variance follows a chi-squared distribution:

$$\frac{(n-1)S^2}{\sigma^2} = \sum_{i=1}^n \left(\frac{X_i - \bar{X}}{\sigma}\right)^2 \sim \chi^2_{n-1}$$

The proof of this result is the central topic of Section 19.2.

## Independence of $\bar{X}$ and $S^2$

A remarkable and non-obvious fact: **$\bar{X}$ and $S^2$ are independent**. This is specific to normal populations and is crucial for deriving the Student's $t$ distribution.

The proof uses the multivariate normal structure — see Section 19.2 for the full derivation.

## Summary of Key Results

For $X_1, \ldots, X_n$ iid $N(\mu, \sigma^2)$:

| Statistic | Distribution |
|-----------|-------------|
| $\bar{X}$ | $N(\mu, \sigma^2/n)$ |
| $\frac{\bar{X} - \mu}{\sigma/\sqrt{n}}$ | $N(0, 1)$ |
| $\frac{(n-1)S^2}{\sigma^2}$ | $\chi^2_{n-1}$ |
| $\bar{X}$ and $S^2$ | Independent |
| $\frac{\bar{X} - \mu}{S/\sqrt{n}}$ | $t_{n-1}$ |

These four results form the foundation for classical statistical inference about normal populations.
