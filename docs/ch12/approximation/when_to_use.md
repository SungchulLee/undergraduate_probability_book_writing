# When to Use the Poisson Approximation

The Poisson approximation replaces the binomial when $n$ is large and $p$ is small — simpler formulas, no large factorials, and it works even when $n$ is unknown.

## Definition

Use $\text{Bin}(n, p) \approx \text{Pois}(\lambda)$ with $\lambda = np$ when:

| Condition | Guideline |
|:----------|:----------|
| $n$ large | $n \ge 20$ (conservative: $n \ge 100$) |
| $p$ small | $p \le 0.05$ |
| $\lambda$ moderate | $np \le 10$ (conservative) |

The error is bounded by $p\lambda = np^2$.

## Explanation

### Why Not Just Use the Binomial?

1. **Computational:** $e^{-\lambda}\lambda^k/k!$ avoids $\binom{n}{k}$ with large factorials
2. **Unknown $n$:** For rare events in continuous time/space, $n$ is ill-defined; $\lambda$ is the natural parameter
3. **Heterogeneous trials:** When $p_i$ vary, the sum is not binomial but is still well-approximated by $\text{Pois}(\sum p_i)$
4. **Nicer properties:** Poisson has additivity and connects to Poisson processes

### When the Approximation Fails

- $p$ is not small (e.g., $p = 0.3$): binomial skewness differs from Poisson
- $n$ is small: insufficient for the limit to apply
- $\lambda$ is very large: both are well-approximated by the normal; Poisson adds nothing

### Typical Applications

Insurance claims, manufacturing defects, network failures, disease counts, particle emissions, typos per page — any count of independently occurring rare events.

## Examples

**Example.** A chip has 1000 components, each failing with probability 0.002.

```python
from scipy.stats import binom, poisson

n, p = 1000, 0.002
la = n * p

print(f"lambda = {la}")
print(f"Le Cam bound = {n*p**2:.6f}")
print(f"\n{'Quantity':>15} {'Binomial':>12} {'Poisson':>12} {'Diff':>12}")
for label, bf, pf in [
    ("P(X=0)", binom.pmf(0,n,p), poisson.pmf(0,la)),
    ("P(X<=3)", binom.cdf(3,n,p), poisson.cdf(3,la)),
    ("P(X>5)", 1-binom.cdf(5,n,p), 1-poisson.cdf(5,la)),
]:
    print(f"{label:>15} {bf:>12.6f} {pf:>12.6f} {abs(bf-pf):>12.2e}")
```
