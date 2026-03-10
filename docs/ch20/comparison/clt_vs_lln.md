# CLT vs LLN

The LLN tells us **where** the sample mean goes; the CLT tells us **how it fluctuates** around that limit — complementary perspectives on the same convergence.

## Definition

| | LLN | CLT |
|:---|:---|:---|
| Statement | $\bar{X}_n \to \mu$ | $\sqrt{n}(\bar{X}_n - \mu)/\sigma \xrightarrow{d} N(0,1)$ |
| Question | Where is the limit? | What is the fluctuation shape? |
| Scale | $\bar{X}_n - \mu \to 0$ | $\bar{X}_n - \mu \approx \sigma/\sqrt{n} \cdot Z$ |

## Explanation

### How They Connect

The CLT says $\bar{X}_n \approx \mu + \frac{\sigma}{\sqrt{n}} Z$ where $Z \sim N(0,1)$. The LLN says $\sigma/\sqrt{n} \to 0$, so $\bar{X}_n \to \mu$. The CLT refines the LLN by characterizing the rate and distributional shape of convergence.

### Known vs Unknown Variance

**Known $\sigma$**: $\frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \approx N(0,1)$ by the CLT.

**Unknown $\sigma$**: Replace with sample SD $S$. The LLN justifies this: $S^2 \xrightarrow{a.s.} \sigma^2$. For normal populations, the exact distribution is $t_{n-1}$; for large $n$, the CLT gives $N(0,1)$.

### Together in Statistics

The LLN + CLT together underpin confidence intervals, hypothesis testing, and the bootstrap. The LLN ensures consistency; the CLT provides distributional approximations.

## Examples

**Example.** Compare LLN convergence and CLT distributional shape.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n_sim = 100_000

for n in [10, 100, 1000]:
    means = np.random.exponential(1.0, (n_sim, n)).mean(axis=1)
    Z = (means - 1.0) / (1.0 / np.sqrt(n))
    ks_stat, p = stats.kstest(Z, 'norm')
    print(f"n={n:5d}: |X̄-μ|_max={np.max(np.abs(means-1)):.4f}, "
          f"CLT KS={ks_stat:.4f}")
```
