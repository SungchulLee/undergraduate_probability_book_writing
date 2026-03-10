# Coupon Collector Problem

The coupon collector problem asks how many random draws are needed to see every type at least once — a natural application of geometric decomposition.

## Definition

There are $n$ types of coupons, each equally likely to appear. Let $T$ be the number of draws until all $n$ types have been collected. Then:

$$
E[T] = n\,H_n = n\sum_{k=1}^n \frac{1}{k}
$$

$$
\text{Var}(T) = n^2 \sum_{k=1}^n \frac{1}{k^2} - n\,H_n
$$

where $H_n = 1 + 1/2 + \cdots + 1/n$ is the $n$-th harmonic number.

## Explanation

### Decomposition into Phases

Divide the collection process into $n$ phases. Phase $i$ starts when you have $i - 1$ distinct types and ends when you get the $i$-th new type. In phase $i$, each draw yields a new type with probability $(n - i + 1)/n$.

$$
T = \tau_1 + \tau_2 + \cdots + \tau_n, \qquad \tau_i \sim \text{Geo}\!\left(\frac{n - i + 1}{n}\right)
$$

The phases are independent (memoryless property of geometric). Therefore:

$$
E[T] = \sum_{i=1}^n \frac{n}{n-i+1} = n\sum_{k=1}^n \frac{1}{k}
$$

### Asymptotic Behavior

$H_n \approx \ln n + \gamma$ where $\gamma \approx 0.577$ is the Euler-Mascheroni constant, so:

$$
E[T] \approx n\ln n + \gamma n
$$

For $n = 100$: $E[T] \approx 100 \cdot 5.187 \approx 519$.

### Birthday Problem Connection

The coupon collector is the "complement" of the birthday problem: the birthday problem asks when a collision (duplicate) first occurs; the coupon collector asks when coverage (all types seen) is complete.

## Examples

**Example.** $n = 50$ collectible cards.

$$
E[T] = 50\,H_{50} \approx 50 \times 4.499 \approx 225
$$

```python
import numpy as np

np.random.seed(42)
n = 50
H_n = sum(1/k for k in range(1, n + 1))
E_T = n * H_n
Var_T = n**2 * sum(1/k**2 for k in range(1, n + 1)) - n * H_n

print(f"Theory: E[T] = {E_T:.1f}, SD(T) = {np.sqrt(Var_T):.1f}")

# Simulate
n_sim = 100_000
results = []
for _ in range(n_sim):
    collected = set()
    t = 0
    while len(collected) < n:
        collected.add(np.random.randint(n))
        t += 1
    results.append(t)

results = np.array(results)
print(f"Simulated: E[T] = {results.mean():.1f}, SD(T) = {results.std():.1f}")
```
