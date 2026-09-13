# 푸아송 극한정리

## 정리의 서술

!!! info "푸아송 극한정리"
    고정된 $\lambda > 0$ 에 대해 $p_n = \lambda/n$ 이고 $X_n \sim B(n, p_n)$ 이라 하자. 그러면 음이 아닌 모든 정수 $k$ 에 대하여 다음이 성립한다.

    $$
    \lim_{n \to \infty} P(X_n = k) = \frac{e^{-\lambda} \lambda^k}{k!}
    $$

    곧 $n \to \infty$ 일 때 $B(n, \lambda/n) \to \text{Po}(\lambda)$ 로 분포수렴한다.

---

## 증명

$p = \lambda/n$ 인 이항분포의 확률질량함수에서 출발하자.

$$
P(X_n = k) = \binom{n}{k} p^k (1-p)^{n-k}
$$

$p = \lambda/n$ 을 대입하면 다음과 같다.

$$
P(X_n = k) = \frac{n(n-1)(n-2)\cdots(n-k+1)}{k!} \left(\frac{\lambda}{n}\right)^k \left(1 - \frac{\lambda}{n}\right)^{n-k}
$$

이를 다시 정리하면 다음과 같다.

$$
P(X_n = k) = \frac{1}{k!} \cdot \underbrace{\frac{n(n-1)(n-2)\cdots(n-k+1)}{n^k}}_{\to 1} \cdot \lambda^k \cdot \underbrace{\left(1 - \frac{\lambda}{n}\right)^n}_{\to e^{-\lambda}} \cdot \underbrace{\left(1 - \frac{\lambda}{n}\right)^{-k}}_{\to 1}
$$

$k$ 를 고정하고 $n \to \infty$ 로 극한을 취하면 다음을 얻는다.

$$
P(X_n = k) \to \frac{1}{k!} \cdot 1 \cdot \lambda^k \cdot e^{-\lambda} \cdot 1 = \frac{e^{-\lambda} \lambda^k}{k!}
$$

**각 인수에 대한 자세한 설명:**

1. $k$ 가 고정되어 있으므로 $\frac{n(n-1)\cdots(n-k+1)}{n^k} = 1 \cdot \left(1 - \frac{1}{n}\right) \cdot \left(1 - \frac{2}{n}\right) \cdots \left(1 - \frac{k-1}{n}\right) \to 1$ 이다.

2. $e$ 의 고전적인 극한 정의에 따라 $\left(1 - \frac{\lambda}{n}\right)^n \to e^{-\lambda}$ 이다.

3. $k$ 가 고정되어 있고 $\lambda/n \to 0$ 이므로 $\left(1 - \frac{\lambda}{n}\right)^{-k} \to 1$ 이다.

---

## 적률의 수렴

적률도 올바르게 수렴한다.

| | $p = \lambda/n$ 인 $B(n, p)$ | $\text{Po}(\lambda)$ |
|:---|:---:|:---:|
| 평균 | $np = \lambda$ | $\lambda$ |
| 분산 | $npq = \lambda(1 - \lambda/n) \to \lambda$ | $\lambda$ |

평균은 모든 $n$ 에서 정확히 일치한다. 분산은 $n \to \infty$ 일 때 $\text{Var}(X_n) = \lambda(1 - \lambda/n) \to \lambda$ 로 수렴한다.

---

## 일반화: pᵢ가 서로 다른 독립인 베르누이확률변수의 합

푸아송 극한정리는 모든 베르누이 시행의 확률이 같은 경우를 넘어서까지 넓혀진다. $A_1, A_2, \ldots, A_n$ 을 독립인 사건이라 하고 $p_i = P(A_i)$ 라 한 뒤 다음과 같이 두자.

$$
X = \sum_{i=1}^{n} \mathbf{1}_{A_i}
$$

$p_i$ 가 서로 다를 수 있으므로 $X$ 는 일반적으로 $B(n, p)$ 가 **아니다**. 그럼에도 $\lambda = \sum_{i=1}^{n} p_i$ 인 $Y \sim \text{Po}(\lambda)$ 에 대하여 임의의 집합 $A$ 에서 다음이 성립한다.

$$
\left| P(X \in A) - P(Y \in A) \right| \leq \sum_{i=1}^{n} p_i^2 \leq \left(\max_{1 \leq i \leq n} p_i\right) \cdot \sum_{i=1}^{n} p_i = \left(\max_{1 \leq i \leq n} p_i\right) \cdot \lambda
$$

!!! note "르캉 부등식"
    **르캉 부등식**이라 부르는 이 결과는 푸아송 근사의 오차에 대한 뚜렷한 경계를 준다. $\max_i p_i$ 가 작을 때, 곧 낱낱의 사건이 저마다 드물 때 이 경계는 작아진다.

---

## 수치로 보기

```python
import numpy as np
from scipy.stats import binom, poisson
from math import comb, factorial

def poisson_limit_demo(n_values, la=10):
    """정해진 k 값들에서 B(n, λ/n)이 Po(λ)로 수렴함을 보인다."""
    k_values = [0, 5, 10, 15, 20]
    poisson_probs = {k: poisson.pmf(k, la) for k in k_values}

    print(f"Convergence of B(n, {la}/n) to Po({la})")
    print(f"{'n':>10}", end="")
    for k in k_values:
        print(f"{'k='+str(k):>12}", end="")
    print()
    print("-" * (10 + 12 * len(k_values)))

    for n in n_values:
        p = la / n
        print(f"{n:>10}", end="")
        for k in k_values:
            binom_prob = binom.pmf(k, n, p)
            print(f"{binom_prob:>12.6f}", end="")
        print()

    print(f"{'Po(' + str(la) + ')':>10}", end="")
    for k in k_values:
        print(f"{poisson_probs[k]:>12.6f}", end="")
    print()

poisson_limit_demo([20, 50, 100, 500, 1000, 10000])
```

예상되는 실행 결과는 다음과 같다.

```
Convergence of B(n, 10/n) to Po(10)
         n         k=0         k=5        k=10        k=15        k=20
------------------------------------------------------------------------
        20    0.003520    0.014786    0.176197    0.014786    0.000000
        50    0.000132    0.018133    0.131839    0.034469    0.000014
       100    0.000027    0.033139    0.131966    0.034955    0.000188
       500    0.000046    0.036249    0.126259    0.034643    0.000864
      1000    0.000046    0.036459    0.125937    0.034660    0.000876
     10000    0.000045    0.036558    0.125838    0.034665    0.000881
    Po(10)    0.000045    0.036561    0.125110    0.034718    0.000866
```

---

## 그림으로 보기

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson

la = 10
n_values = [20, 50, 200, 2000]
k_max = 25
k = np.arange(0, k_max + 1)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.ravel()

poisson_pmf = poisson.pmf(k, la)

for idx, n in enumerate(n_values):
    p = la / n
    binom_pmf = binom.pmf(k, n, p)

    axes[idx].bar(k - 0.2, binom_pmf, width=0.4, alpha=0.7,
                  label=f'B({n}, {la/n:.4f})', color='steelblue')
    axes[idx].bar(k + 0.2, poisson_pmf, width=0.4, alpha=0.7,
                  label=f'Po({la})', color='coral')
    axes[idx].set_title(f'n = {n}, p = {la/n:.4f}')
    axes[idx].set_xlabel('k')
    axes[idx].set_ylabel('P(X = k)')
    axes[idx].legend()
    axes[idx].grid(True, alpha=0.3)

    max_diff = np.max(np.abs(binom_pmf - poisson_pmf))
    axes[idx].text(0.95, 0.95, f'Max |diff| = {max_diff:.2e}',
                   transform=axes[idx].transAxes, ha='right', va='top',
                   fontsize=9, bbox=dict(boxstyle='round', facecolor='wheat'))

plt.suptitle(f'Poisson Limit Theorem: B(n, λ/n) → Po(λ), λ = {la}',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('poisson_limit_theorem.png', dpi=150, bbox_inches='tight')
plt.show()
```


## 연습문제

**연습문제 1.**
어떤 제조 공정에서 마이크로칩 한 개가 불량일 확률이 $p = 0.002$ 이다. 한 묶음에는 $n = 1000$ 개의 칩이 들어 있다.

**(a)** $X$ 를 불량 칩의 개수라 하자. $X$ 의 정확한 분포는 무엇인가? 푸아송 근사는 무엇인가?

**(b)** 정확한 이항분포와 푸아송 근사를 모두 써서 $P(X = 0)$, $P(X \leq 3)$, $P(X > 5)$ 를 계산하고 견주어 보아라.

**(c)** 이 근사에 대한 르캉 오차 경계를 계산하여라.

??? success "연습문제 1 풀이"

    **(a)** 정확하게는 $X \sim B(1000, 0.002)$ 이다. 푸아송 근사는 $\lambda = np = 2$ 인 $X \approx \text{Po}(\lambda)$ 이다.

    **(b)**

    ```python
    from scipy.stats import binom, poisson

    n, p = 1000, 0.002
    la = n * p

    print(f"{'':>20} {'Binomial':>12} {'Poisson':>12} {'Diff':>12}")
    print("-" * 58)

    b0, p0 = binom.pmf(0, n, p), poisson.pmf(0, la)
    print(f"{'P(X=0)':>20} {b0:>12.6f} {p0:>12.6f} {abs(b0-p0):>12.2e}")

    b3, p3 = binom.cdf(3, n, p), poisson.cdf(3, la)
    print(f"{'P(X≤3)':>20} {b3:>12.6f} {p3:>12.6f} {abs(b3-p3):>12.2e}")

    b5, p5 = 1 - binom.cdf(5, n, p), 1 - poisson.cdf(5, la)
    print(f"{'P(X>5)':>20} {b5:>12.6f} {p5:>12.6f} {abs(b5-p5):>12.2e}")
    ```

    **(c)** 르캉 경계는 $np^2 = 1000 \cdot (0.002)^2 = 0.004$ 이다.
