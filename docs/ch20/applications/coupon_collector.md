# Coupon Collector Problem


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Problem Setup

Suppose there are $n$ different types of coupons (e.g., toys in happy meals). Each time you buy a happy meal, you receive one coupon uniformly at random. Let $T_n$ be the total number of purchases needed to collect **all** $n$ types.

**Claim**: As $n \to \infty$,

$$
\frac{T_n}{n \log n} \xrightarrow{p} 1
$$

## Decomposition

Let $\tau_i$ be the number of additional purchases needed to get the $i$-th **new** coupon after collecting $i-1$ distinct coupons. Then:

**1. Decomposition:**

$$
T_n = \sum_{i=1}^n \tau_i
$$

**2. Distribution:** When you have $i-1$ distinct coupons, the probability of getting a new one is $\frac{n-(i-1)}{n}$. So:

$$
\tau_i \sim \text{Geo}\left(\frac{n-(i-1)}{n}\right)
$$

**3. Independence:** The $\tau_i$ are independent (each phase starts fresh once a new coupon is found).

## Step 1: Compute the Mean

$$
\mathbb{E}T_n = \sum_{i=1}^n \mathbb{E}\tau_i = \sum_{i=1}^n \frac{n}{n-(i-1)} = n\left(1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}\right) = nH_n
$$

where $H_n = \sum_{k=1}^n \frac{1}{k}$ is the $n$-th harmonic number. Since $H_n \sim \log n$:

$$
\mathbb{E}T_n \sim n \log n
$$

## Step 2: Compute the Variance

$$
Var(T_n) = \sum_{i=1}^n Var(\tau_i) = \sum_{i=1}^n \frac{1 - p_i}{p_i^2} \leq \sum_{i=1}^n \frac{n^2}{(n-i+1)^2} = n^2 \sum_{k=1}^n \frac{1}{k^2} \leq Cn^2
$$

since $\sum_{k=1}^{\infty} 1/k^2 = \pi^2/6 < \infty$.

## Step 3: Apply Chebyshev's Inequality

Choose $a_n = n\log n$. Then for any $\varepsilon > 0$:

$$
P\left(\left|\frac{T_n - \mathbb{E}T_n}{a_n}\right| > \varepsilon\right) \leq \frac{Var(T_n)}{\varepsilon^2 a_n^2} \leq \frac{Cn^2}{\varepsilon^2 (n\log n)^2} = \frac{C}{\varepsilon^2 (\log n)^2} \to 0
$$

We also need $\mathbb{E}T_n / a_n \to 1$:

$$
\frac{\mathbb{E}T_n}{n\log n} = \frac{nH_n}{n\log n} = \frac{H_n}{\log n} \to 1
$$

Combining these two facts:

$$
\frac{T_n}{n\log n} = \frac{T_n - \mathbb{E}T_n}{n\log n} + \frac{\mathbb{E}T_n}{n\log n} \xrightarrow{p} 0 + 1 = 1
$$

## Interpretation

To collect all $n$ coupons, you need approximately $n\ln n$ purchases. For example, with $n = 100$ coupon types, you'd expect to need about $100 \times \ln(100) \approx 461$ purchases to collect them all.
