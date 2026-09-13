# 수치 비교(이항분포와 푸아송분포)

## 확률질량함수를 나란히 놓고 견주기

푸아송 근사의 조건이 갖추어지면($n$ 이 크고 $p$ 가 작으며 $\lambda = np$ 가 알맞은 크기), $B(n, p)$ 와 $\text{Po}(\lambda)$ 의 확률질량함수는 거의 구별되지 않는다.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson

n = 2000
p = 0.005
la = n * p  # λ = 10

k_max = int(la + 6 * np.sqrt(la))
k = np.arange(0, k_max + 1)

binom_pmf = binom.pmf(k, n, p)
poisson_pmf = poisson.pmf(k, la)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].bar(k, binom_pmf, color='steelblue', alpha=0.7, edgecolor='black')
axes[0].set_title(f'PMF of B({n}, {p})')
axes[0].set_xlabel('k')
axes[0].set_ylabel('P(X = k)')
axes[0].set_xlim(-0.5, k_max + 0.5)
axes[0].set_ylim(0, 0.13)
axes[0].grid(True, alpha=0.3)

axes[1].bar(k, poisson_pmf, color='coral', alpha=0.7, edgecolor='black')
axes[1].set_title(f'PMF of Po({int(la)})')
axes[1].set_xlabel('k')
axes[1].set_ylabel('P(X = k)')
axes[1].set_xlim(-0.5, k_max + 0.5)
axes[1].set_ylim(0, 0.13)
axes[1].grid(True, alpha=0.3)

plt.suptitle(f'Poisson Approximation: B({n}, {p}) ≈ Po({int(la)})',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('binomial_vs_poisson.png', dpi=150, bbox_inches='tight')
plt.show()

max_diff = np.max(np.abs(binom_pmf - poisson_pmf))
print(f"Maximum difference between PMFs: {max_diff:.4e}")
```

$n = 2000$, $p = 0.005$, $\lambda = 10$ 일 때 두 확률질량함수의 최대 차이는 대략 $3.14 \times 10^{-4}$ 이다.

---

## 점마다 견주어 본 표

```python
import numpy as np
from scipy.stats import binom, poisson

n = 2000
p = 0.005
la = n * p

print(f"{'k':>4} {'B(2000,0.005)':>15} {'Po(10)':>15} {'Difference':>15}")
print("-" * 52)
for k in range(21):
    b = binom.pmf(k, n, p)
    po = poisson.pmf(k, la)
    print(f"{k:>4} {b:>15.8f} {po:>15.8f} {b - po:>15.2e}")
```

---

## 예: 생일이 같은 부부의 쌍의 수

어느 해에 뉴욕에서 약 80,000쌍이 결혼하였다. 생일이 같은(두 사람이 한 해의 같은 날에 태어난) 부부가 250쌍보다 많을 확률을 어림해 보자.

**문제 설정**: $n = 80{,}000$ 을 부부의 쌍의 수라 하자. 각 부부 $i$ 에 대해 $A_i$ 를 "부부 $i$ 의 생일이 같다"는 사건이라 하자. 생일이 365일에 고르게 퍼져 있다고 보면 다음과 같다.

$$
p = P(A_i) = \frac{1}{365}
$$

$S_n = \sum_{i=1}^{n} \mathbf{1}_{A_i}$ 을 생일이 같은 부부의 쌍의 수라 하면 다음이 성립한다.

$$
S_n \sim B(n, p) \approx \text{Po}(\lambda), \quad \lambda = np = \frac{80{,}000}{365} \approx 219.18
$$

**구하려는 것**: $P(S_n > 250)$ 이다.

```python
import numpy as np
from scipy.stats import binom, poisson
import time

n = 80_000
p = 1 / 365
la = n * p
m = 250

# --- 정확한 이항분포 ---
t0 = time.time()
# 넘침을 피하기 위해 로그 공간에서 계산한다
binom_prob = 1 - binom.cdf(m, n, p)
binom_time = time.time() - t0

# --- 푸아송 근사 ---
t0 = time.time()
poisson_prob = 1 - poisson.cdf(m, la)
poisson_time = time.time() - t0

print(f"λ = np = {la:.4f}")
print()
print(f"Exact (Binomial):       P(S_n > 250) = {binom_prob:.6f}")
print(f"Approximate (Poisson):  P(X  > 250) = {poisson_prob:.6f}")
print()
print(f"Absolute difference: {abs(binom_prob - poisson_prob):.6e}")
print(f"Binomial time:  {binom_time:.6f} s")
print(f"Poisson time:   {poisson_time:.6f} s")
```

**결과**:

| 방법 | $P(\cdot > 250)$ |
|:---|:---:|
| 정확한 값: $S_n \sim B(80000, 1/365)$ | 0.0187 |
| 근삿값: $X \sim \text{Po}(219.18)$ | 0.0188 |

푸아송 근사는 소수점 넷째 자리까지 정확하다.

---

## 되풀이 계산(큰 계승을 피하기)

$n$ 이 아주 클 때 $\binom{n}{k}$ 를 직접 계산하면 넘침이 일어날 수 있다. 이항분포와 푸아송분포의 확률질량함수는 모두 점화식을 써서 되풀이하여 계산할 수 있다.

**이항분포의 점화식**: $P(X = 0) = q^n$ 에서 출발한다.

$$
P(X = k) = P(X = k-1) \cdot \frac{n - k + 1}{k} \cdot \frac{p}{q}
$$

**푸아송분포의 점화식**: $P(X = 0) = e^{-\lambda}$ 에서 출발한다.

$$
P(X = k) = P(X = k-1) \cdot \frac{\lambda}{k}
$$

```python
import numpy as np
import time

n = 80_000
p = 1 / 365
q = 1 - p
la = n * p
m = 250

# --- 되풀이 계산한 이항분포 ---
t0 = time.time()
prob = q ** n
cum_prob = prob
for i in range(1, m + 1):
    prob = prob * (n - i + 1) / i * p / q
    cum_prob += prob
binom_exact = 1 - cum_prob
binom_time = time.time() - t0

# --- 되풀이 계산한 푸아송분포 ---
t0 = time.time()
prob = np.exp(-la)
cum_prob = prob
for i in range(1, m + 1):
    prob = prob * la / i
    cum_prob += prob
poisson_approx = 1 - cum_prob
poisson_time = time.time() - t0

print(f"Binomial (iterative):  P(S > {m}) = {binom_exact:.6f}  ({binom_time:.6f} s)")
print(f"Poisson (iterative):   P(X > {m}) = {poisson_approx:.6f}  ({poisson_time:.6f} s)")
```

---

## n이 커질 때의 수렴

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson

la = 10
n_values = [20, 50, 100, 200, 500, 1000, 5000, 10000]
k_max = 25
k = np.arange(0, k_max + 1)

poisson_pmf = poisson.pmf(k, la)

max_diffs = []
for n in n_values:
    p = la / n
    binom_pmf = binom.pmf(k, n, p)
    max_diffs.append(np.max(np.abs(binom_pmf - poisson_pmf)))

plt.figure(figsize=(8, 5))
plt.loglog(n_values, max_diffs, 'o-', color='steelblue', linewidth=2, markersize=8)
plt.xlabel('n', fontsize=12)
plt.ylabel('Max |PMF difference|', fontsize=12)
plt.title(f'Convergence Rate: B(n, {la}/n) → Po({la})', fontsize=14)
plt.grid(True, alpha=0.3, which='both')

# O(1/n) 기준선을 덧그린다
n_arr = np.array(n_values, dtype=float)
plt.loglog(n_arr, max_diffs[0] * n_values[0] / n_arr, '--', color='gray',
           alpha=0.5, label='O(1/n) reference')
plt.legend()
plt.tight_layout()
plt.savefig('poisson_convergence_rate.png', dpi=150, bbox_inches='tight')
plt.show()
```

확률질량함수의 최대 차이는 $O(1/n)$ 으로 줄어들며, 이는 르캉 경계 $p \cdot \lambda = \lambda^2/n$ 과 들어맞는다.


## 연습문제

**연습문제 1.**
**(a)** $\lambda = 5$ 에 대하여, $X_n \sim B(n, 5/n)$ 이고 $Y \sim \text{Po}(5)$ 일 때 $n = 10, 20, 50, 100, 500, 1000$ 각각에 대해 확률질량함수의 최대 차이 $\max_k |P(X_n = k) - P(Y = k)|$ 를 계산하여라.

**(b)** 최대 차이를 $n$ 의 함수로 로그-로그 눈금에 그려라. 관찰되는 수렴 속도는 어떠한가?

**(c)** 각 $n$ 에 대해 관찰된 최대 차이를 르캉 경계 $\lambda^2/n$ 과 견주어 보아라.

??? success "연습문제 1 풀이"

    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import binom, poisson

    la = 5
    n_values = [10, 20, 50, 100, 500, 1000]

    print(f"{'n':>6} {'Max |diff|':>12} {'Le Cam (λ²/n)':>14} {'Ratio':>8}")
    print("-" * 44)

    max_diffs = []
    for n in n_values:
        p = la / n
        k = np.arange(0, max(30, int(la + 6*np.sqrt(la))))
        b_pmf = binom.pmf(k, n, p)
        p_pmf = poisson.pmf(k, la)
        md = np.max(np.abs(b_pmf - p_pmf))
        max_diffs.append(md)
        lecam = la**2 / n
        print(f"{n:>6} {md:>12.6e} {lecam:>14.6e} {md/lecam:>8.4f}")

    plt.figure(figsize=(8, 5))
    plt.loglog(n_values, max_diffs, 'o-', label='Max |PMF diff|')
    plt.loglog(n_values, [la**2/n for n in n_values], 's--', label='λ²/n bound')
    plt.xlabel('n')
    plt.ylabel('Error')
    plt.title('Convergence Rate of Poisson Approximation')
    plt.legend()
    plt.grid(True, alpha=0.3, which='both')
    plt.tight_layout()
    plt.show()
    ```

    수렴 속도는 $O(1/n)$ 이며, 이는 르캉 경계와 들어맞는다.
