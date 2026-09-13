# 푸아송분포의 정의와 성질

## 정의

확률변수 $X$ 의 확률질량함수가 다음과 같으면, $X$ 는 모수가 $\lambda > 0$ 인 **푸아송분포**를 따른다고 하고 $X \sim \text{Po}(\lambda)$ 로 적는다.

$$
P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}, \quad k = 0, 1, 2, \ldots
$$

모수 $\lambda$ 는 이 분포의 **평균**이자 **분산**이기도 하다.

---

## 확률질량함수의 합이 1임을 확인하기

이것이 올바른 확률분포인지 확인하기 위해 확률질량함수의 합이 1임을 살펴보자.

$$
\sum_{k=0}^{\infty} \frac{e^{-\lambda} \lambda^k}{k!} = e^{-\lambda} \sum_{k=0}^{\infty} \frac{\lambda^k}{k!} = e^{-\lambda} \cdot e^{\lambda} = 1
$$

여기에는 테일러급수 전개 $e^{\lambda} = \sum_{k=0}^{\infty} \frac{\lambda^k}{k!}$ 가 쓰였다.

---

## 직관: 푸아송분포는 어디에서 오는가

푸아송분포는 $n$ 이 크고 $p$ 가 작으며 $\lambda = np$ 가 고정되어 있을 때 이항분포 $B(n, p)$ 의 근사로서 자연스럽게 나타난다.

| 분포 | 확률변수 |
|:---|:---|
| $B(p)$ | $p$-동전을 한 번 던져 앞면이 나왔는지 살핀다 |
| $B(n, p)$ | $p$-동전을 $n$ 번 던져 앞면의 개수를 센다 |
| $\text{Po}(\lambda) \approx B(n, p)$ | $np = \lambda$ 를 고정하고 $n \to \infty$ 로 보내면서 $p$-동전을 $n$ 번 던져 앞면의 개수를 센다 |
| $\text{Geo}(p)$ | 첫 앞면이 나올 때까지 $p$-동전을 던져 던진 횟수를 센다 |
| $\text{NB}(r, p)$ | $r$ 번째 앞면이 나올 때까지 $p$-동전을 던져 던진 횟수를 센다 |

푸아송분포는 정해진 시간 동안이나 정해진 공간 안에서 일어나는 "드문 사건"의 개수를 세는 것으로 생각할 수 있다. 각 사건이 어느 한 순간에 일어날 확률은 매우 작지만, 일어날 기회는 아주 많은 상황이다.

---

## 이산분포의 모수 요약

| 분포 | 기댓값 | 분산 |
|:---|:---:|:---:|
| $B(p)$ | $p$ | $pq$ |
| $B(n, p)$ | $np$ | $npq$ |
| $\text{Po}(\lambda) \approx B(n, p)$ | $\lambda$ | $\lambda$ |
| $\text{Geo}(p)$ | $\frac{1}{p}$ | $\frac{q}{p^2}$ |
| $\text{NB}(r, p)$ | $\frac{r}{p}$ | $\frac{rq}{p^2}$ |

푸아송분포의 두드러진 특징은 평균과 분산이 같다는 것이다($\lambda = \lambda$). 이 성질은 흔히 진단 기준으로 쓰인다. 자료의 평균이 분산과 거의 같다면 푸아송 모형이 알맞을 수 있다.

---

## 확률질량함수와 누적분포함수 그림으로 보기

$\text{Po}(\lambda)$ 의 확률질량함수는 음이 아닌 정수 위에 모여 있는 이산분포이다. $\lambda$ 가 커지면 분포는 오른쪽으로 옮겨 가고 더 넓게 퍼지며, 중심극한정리에 따라 정규분포의 모양에 가까워져 더 대칭이 된다.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

la = 10
m = 30
x = np.arange(0, m + 1)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 확률질량함수
pmf_vals = poisson.pmf(x, la)
axes[0].bar(x, pmf_vals, color='steelblue', alpha=0.7, edgecolor='black')
axes[0].set_title(f'PMF of Po({la})')
axes[0].set_xlabel('k')
axes[0].set_ylabel('P(X = k)')
axes[0].set_xlim(-0.5, m + 0.5)
axes[0].grid(True, alpha=0.3)

# 누적분포함수
cdf_vals = poisson.cdf(x, la)
axes[1].step(x, cdf_vals, where='mid', color='steelblue', linewidth=2)
axes[1].set_title(f'CDF of Po({la})')
axes[1].set_xlabel('k')
axes[1].set_ylabel('P(X ≤ k)')
axes[1].set_xlim(-0.5, m + 0.5)
axes[1].set_ylim(0, 1.05)
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('poisson_pmf_cdf.png', dpi=150, bbox_inches='tight')
plt.show()
```

---

## 주요 성질

1. **받침(support)**: $X$ 는 $\{0, 1, 2, \ldots\}$ 의 값(음이 아닌 정수)을 갖는다.

2. **최빈값**: $\text{Po}(\lambda)$ 의 최빈값은 $\lambda$ 가 정수가 아닐 때는 $\lfloor \lambda \rfloor$ 이고, $\lambda$ 가 양의 정수일 때는 $\lambda - 1$ 과 $\lambda$ 둘 다이다.

3. **이웃한 확률의 비**: $k \geq 1$ 에 대하여

   $$
   \frac{P(X = k)}{P(X = k-1)} = \frac{\lambda}{k}
   $$

   이다. 곧 $k < \lambda$ 일 때는 확률이 늘어나고 $k > \lambda$ 일 때는 줄어든다.

4. **꼬리의 모습**: $k!$ 이 어떤 지수함수보다도 빠르게 커지므로, 푸아송분포의 확률질량함수는 큰 $k$ 에서 지수보다도 빠르게(어떤 기하분포보다도 빠르게) 줄어든다.

5. **평균과 분산이 같다**: $E[X] = \text{Var}(X) = \lambda$ 이다. 이것은 흔히 쓰는 분포들 가운데 푸아송분포만이 갖는 지문과 같다.

---

## 파이썬으로 푸아송확률 계산하기

```python
from scipy.stats import poisson

la = 10

# 낱낱의 확률
print(f"P(X = 5) = {poisson.pmf(5, la):.6f}")
print(f"P(X = 10) = {poisson.pmf(10, la):.6f}")

# 누적확률
print(f"P(X <= 8) = {poisson.cdf(8, la):.6f}")
print(f"P(X > 12) = {1 - poisson.cdf(12, la):.6f}")

# 분위수
print(f"Median = {poisson.median(la)}")
print(f"95th percentile = {poisson.ppf(0.95, la)}")

# 평균과 분산
print(f"Mean = {poisson.mean(la)}, Variance = {poisson.var(la)}")
```

## 연습문제

**연습문제 1.**
$X \sim \text{Po}(6)$ 이라 하자.

**(a)** $P(X = 0)$, $P(X = 3)$, $P(X = 6)$, $P(X = 10)$ 을 계산하여라.

**(b)** $P(X \leq 4)$ 와 $P(X > 8)$ 을 계산하여라.

**(c)** $X$ 의 최빈값을 구하여라.

**(d)** $E[X] = \text{Var}(X) = 6$ 임을 수치적으로 확인하여라.

??? success "연습문제 1 풀이"

    **(a)**

    $$
    P(X = k) = \frac{e^{-6} \cdot 6^k}{k!}
    $$

    ```python
    from scipy.stats import poisson

    la = 6
    for k in [0, 3, 6, 10]:
        print(f"P(X = {k}) = {poisson.pmf(k, la):.6f}")
    ```

    - $P(X = 0) = e^{-6} \approx 0.002479$
    - $P(X = 3) = \frac{e^{-6} \cdot 216}{6} \approx 0.089235$
    - $P(X = 6) \approx 0.160623$
    - $P(X = 10) \approx 0.041303$

    **(b)**

    ```python
    print(f"P(X ≤ 4) = {poisson.cdf(4, la):.6f}")
    print(f"P(X > 8) = {1 - poisson.cdf(8, la):.6f}")
    ```

    $P(X \leq 4) \approx 0.2851$ 이고 $P(X > 8) \approx 0.1528$ 이다.

    **(c)** $\lambda = 6$ 이 정수이므로 최빈값은 $k = 5$ 와 $k = 6$ 둘 다이다.

    **(d)**

    ```python
    import numpy as np
    np.random.seed(42)
    samples = np.random.poisson(6, 100_000)
    print(f"Sample mean: {samples.mean():.4f}")
    print(f"Sample var:  {samples.var(ddof=1):.4f}")
    ```
