# Merging and Splitting of Poisson Processes

Merging independent Poisson processes yields a Poisson process; splitting one by random classification yields independent Poisson processes.

## Definition

**Merging.** If $\{N_1(t)\}$ and $\{N_2(t)\}$ are independent Poisson processes with rates $\lambda_1$ and $\lambda_2$, then $\{N_1(t) + N_2(t)\}$ is Poisson with rate $\lambda_1 + \lambda_2$.

**Splitting (Thinning).** If $\{N(t)\}$ is Poisson with rate $\lambda$, and each event is independently classified as type A (probability $p$) or type B (probability $1 - p$), then:

- Type A events form a Poisson process with rate $\lambda p$
- Type B events form a Poisson process with rate $\lambda(1-p)$
- The two processes are **independent**

## Explanation

### Why Merging Works

Events from both processes in $(s, s+h]$ form a count $N_1(s,s+h) + N_2(s,s+h) \sim \text{Pois}(\lambda_1 h) + \text{Pois}(\lambda_2 h) = \text{Pois}((\lambda_1+\lambda_2)h)$ by additivity. Independent increments are preserved.

### Why Splitting Works

Conditioning on $N(t) = n$: the number of type A events is $\text{Bin}(n, p)$. Since $N(t) \sim \text{Pois}(\lambda t)$, the type A count is $\text{Pois}(\lambda p t)$ (compound Poisson argument). Independence of the two subprocesses follows from the "chicken-egg" relationship with Poisson and binomial.

### Generalization

Splitting into $k$ types with probabilities $p_1, \ldots, p_k$ ($\sum p_i = 1$) produces $k$ independent Poisson processes with rates $\lambda p_1, \ldots, \lambda p_k$.

## Examples

**Example.** Customers arrive at rate 20/hour. 30% buy product A, 70% buy product B.

```python
import numpy as np

np.random.seed(42)
lam = 20
p = 0.3
n_sim = 100_000

# Splitting
N_total = np.random.poisson(lam, n_sim)
N_A = np.random.binomial(N_total, p)
N_B = N_total - N_A

print(f"Total: mean={N_total.mean():.2f}  (theory: {lam})")
print(f"Type A: mean={N_A.mean():.2f}  (theory: {lam*p})")
print(f"Type B: mean={N_B.mean():.2f}  (theory: {lam*(1-p)})")
print(f"Corr(A,B) = {np.corrcoef(N_A, N_B)[0,1]:.4f}  (theory: 0)")
```
