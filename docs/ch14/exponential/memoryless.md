# Memoryless Property

The Exponential distribution is the unique continuous distribution with the memoryless property: given that you have already waited for time $s$, the remaining wait has the same distribution as if you had just started.

## Definition

If $X \sim \text{Exp}(\lambda)$, then for all $s, t \geq 0$:

$$
P(X > s + t \mid X > s) = P(X > t)
$$

Equivalently, if no event has occurred by time $s$, the remaining time until the first event has the same $\text{Exp}(\lambda)$ distribution -- the process "restarts" from scratch.

**Uniqueness.** The Exponential distribution is the **only** continuous distribution with this property. Similarly, the Geometric distribution is the only discrete distribution with the memoryless property.

## Explanation

### Proof of the Memoryless Property

The proof is a direct computation using the survival function $\bar{F}(t) = e^{-\lambda t}$:

$$
P(X > s + t \mid X > s) = \frac{P(X > s + t)}{P(X > s)} = \frac{e^{-\lambda(s+t)}}{e^{-\lambda s}} = e^{-\lambda t} = P(X > t)
$$

The key is the multiplicative property of the exponential function: $e^{-\lambda(s+t)} = e^{-\lambda s} \cdot e^{-\lambda t}$.

### Proof of Uniqueness

Suppose $X$ is a continuous, positive random variable satisfying $P(X > s + t \mid X > s) = P(X > t)$ for all $s, t \geq 0$. Writing $\bar{F}(t) = P(X > t)$, the memoryless property implies the **functional equation**

$$
\bar{F}(s + t) = \bar{F}(s) \cdot \bar{F}(t)
$$

for all $s, t \geq 0$. The only continuous solutions with $\bar{F}(0) = 1$ and $\bar{F}(t) \to 0$ as $t \to \infty$ are $\bar{F}(t) = e^{-\lambda t}$ for some $\lambda > 0$. This is Cauchy's exponential equation. Therefore $X \sim \text{Exp}(\lambda)$.

### Constant Hazard Rate

The **hazard rate** (or failure rate) of a continuous distribution is

$$
h(t) = \frac{f(t)}{\bar{F}(t)}
$$

For the Exponential distribution:

$$
h(t) = \frac{\lambda e^{-\lambda t}}{e^{-\lambda t}} = \lambda
$$

The hazard rate is **constant** -- the probability of failure in the next instant is always $\lambda \, dt$, regardless of how long the system has been running. A constant hazard rate is equivalent to the memoryless property.

Distributions with *increasing* hazard rates model wear-out (e.g., Weibull with shape $> 1$), while *decreasing* hazard rates model infant mortality.

### Fresh Start Property in Poisson Processes

At any point in time during a Poisson process, the time until the next event has distribution $\text{Exp}(\lambda)$, regardless of when the last event occurred. This is why Poisson processes are sometimes called processes "without aftereffects."

### Minimum of Independent Exponentials

If $X_1 \sim \text{Exp}(\lambda_1)$ and $X_2 \sim \text{Exp}(\lambda_2)$ are independent, then

$$
\min(X_1, X_2) \sim \text{Exp}(\lambda_1 + \lambda_2)
$$

**Proof.** By independence:

$$
P(\min(X_1, X_2) > t) = P(X_1 > t) P(X_2 > t) = e^{-\lambda_1 t} e^{-\lambda_2 t} = e^{-(\lambda_1 + \lambda_2)t}
$$

which is the survival function of $\text{Exp}(\lambda_1 + \lambda_2)$.

This generalizes: the minimum of $n$ independent exponentials with rates $\lambda_1, \ldots, \lambda_n$ is $\text{Exp}(\lambda_1 + \cdots + \lambda_n)$. The rates add because competing Poisson processes merge into a single process with the combined rate.

## Examples

**Example 1.** A light bulb has lifetime $X \sim \text{Exp}(1/1000)$ (mean 1000 hours). Given that it has already lasted 800 hours, find the expected remaining lifetime.

By the memoryless property, the remaining lifetime is still $\text{Exp}(1/1000)$ with mean 1000 hours. The 800 hours already elapsed provide no information about the future.

**Example 2.** Machines A and B have independent lifetimes $T_A \sim \text{Exp}(0.1)$ and $T_B \sim \text{Exp}(0.2)$ (rates in failures per year). Find the expected time until the first failure.

$\min(T_A, T_B) \sim \text{Exp}(0.1 + 0.2) = \text{Exp}(0.3)$, so $E[\min(T_A, T_B)] = 1/0.3 \approx 3.33$ years.

**Example 3.** Demonstrate the memoryless property and the minimum-of-exponentials result by simulation.

```python
import numpy as np

np.random.seed(42)
n_sim = 500_000
lam = 1.0

# --- Memoryless property ---
X = np.random.exponential(1/lam, n_sim)
s = 2.0

# Remaining time given X > s
X_remaining = X[X > s] - s

print("=== Memoryless Property ===")
print(f"Unconditional mean:  {np.mean(X):.4f}  (theory {1/lam:.4f})")
print(f"Remaining | X > {s}:  {np.mean(X_remaining):.4f}  (theory {1/lam:.4f})")
print(f"Unconditional var:   {np.var(X):.4f}  (theory {1/lam**2:.4f})")
print(f"Remaining var:       {np.var(X_remaining):.4f}  (theory {1/lam**2:.4f})")

# --- Minimum of exponentials ---
lam1, lam2 = 0.1, 0.2
T_A = np.random.exponential(1/lam1, n_sim)
T_B = np.random.exponential(1/lam2, n_sim)
T_min = np.minimum(T_A, T_B)

print("\n=== Minimum of Exponentials ===")
print(f"E[min(T_A, T_B)]: sim={np.mean(T_min):.4f}, "
      f"theory={1/(lam1+lam2):.4f}")
print(f"Var[min(T_A,T_B)]: sim={np.var(T_min):.4f}, "
      f"theory={1/(lam1+lam2)**2:.4f}")

# Verify the distribution is Exp(0.3) by checking survival function
t_test = 5.0
surv_sim = np.mean(T_min > t_test)
surv_theory = np.exp(-(lam1 + lam2) * t_test)
print(f"P(min > {t_test}): sim={surv_sim:.4f}, theory={surv_theory:.4f}")
```
