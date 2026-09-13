# 푸아송분포의 평균과 분산

## Po(λ)의 평균

### 직접 계산하기

$X \sim \text{Po}(\lambda)$ 에 대하여 다음과 같다.

$$
E[X] = \sum_{k=0}^{\infty} k \cdot \frac{e^{-\lambda} \lambda^k}{k!} = \sum_{k=1}^{\infty} k \cdot \frac{e^{-\lambda} \lambda^k}{k!}
$$

$k/k! = 1/(k-1)!$ 이므로 $j = k - 1$ 로 바꾸면 다음을 얻는다.

$$
E[X] = e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^k}{(k-1)!} = e^{-\lambda} \lambda \sum_{j=0}^{\infty} \frac{\lambda^j}{j!} = e^{-\lambda} \lambda \cdot e^{\lambda} = \lambda
$$

### 지시확률변수로 쪼개어 보기

이항분포 근사를 쓰는 깔끔한 다른 방법도 있다. $\lambda = np$ 이고 $X \sim B(n, p) \approx \text{Po}(\lambda)$ 이면 $X = \sum_{i=1}^{n} \mathbf{1}_{A_i}$ 로 적을 수 있다. 여기서 $\mathbf{1}_{A_i} \sim B(p)$ 는 독립인 지시확률변수이다. 기댓값의 선형성에 따라 다음을 얻는다.

$$
E[X] = \sum_{i=1}^{n} E[\mathbf{1}_{A_i}] = np = \lambda
$$

---

## 2차 적률과 분산

### E[X²] 계산하기

항등식 $E[X^2] = E[X(X-1)] + E[X]$ 를 쓴다.

$$
E[X(X-1)] = \sum_{k=0}^{\infty} k(k-1) \cdot \frac{e^{-\lambda} \lambda^k}{k!} = \sum_{k=2}^{\infty} \frac{e^{-\lambda} \lambda^k}{(k-2)!}
$$

$j = k - 2$ 로 바꾸면 다음과 같다.

$$
E[X(X-1)] = e^{-\lambda} \lambda^2 \sum_{j=0}^{\infty} \frac{\lambda^j}{j!} = e^{-\lambda} \lambda^2 e^{\lambda} = \lambda^2
$$

그러므로 다음을 얻는다.

$$
E[X^2] = E[X(X-1)] + E[X] = \lambda^2 + \lambda
$$

### 분산

$$
\text{Var}(X) = E[X^2] - (E[X])^2 = (\lambda^2 + \lambda) - \lambda^2 = \lambda
$$

!!! note "평균과 분산이 같다"
    푸아송분포에서는 $E[X] = \text{Var}(X) = \lambda$ 이다. 이것은 푸아송분포를 다른 이산분포와 구별해 주는 표지가 되는 성질이다. 표준편차는 $\sigma = \sqrt{\lambda}$ 이다.

---

## 이항분포 근사로 보기

$\lambda = np$ 를 고정하고 $n \to \infty$ 로 보내면 $\text{Po}(\lambda) \approx B(n, p)$ 이므로 다음과 같다.

| | $B(n, p)$ | $\text{Po}(\lambda) \approx B(n, p)$ |
|:---|:---:|:---:|
| 기댓값 | $np$ | $\lambda$ |
| 분산 | $npq$ | $\lambda$ |

분산이 맞아떨어지는 것은 근사적인 뜻에서이다. $p = \lambda/n \to 0$ 이므로 $n \to \infty$ 일 때 $npq = np(1-p) = \lambda(1 - \lambda/n) \to \lambda$ 이다.

---

## 수치로 확인하기

```python
import numpy as np
from scipy.stats import poisson

lambdas = [1, 5, 10, 20, 50]

print(f"{'λ':>5} {'E[X]':>10} {'Var(X)':>10} {'SD(X)':>10}")
print("-" * 40)
for la in lambdas:
    mean = poisson.mean(la)
    var = poisson.var(la)
    std = poisson.std(la)
    print(f"{la:>5} {mean:>10.4f} {var:>10.4f} {std:>10.4f}")
```

예상되는 실행 결과는 다음과 같다.

```
    λ       E[X]     Var(X)      SD(X)
----------------------------------------
    1     1.0000     1.0000     1.0000
    5     5.0000     5.0000     2.2361
   10    10.0000    10.0000     3.1623
   20    20.0000    20.0000     4.4721
   50    50.0000    50.0000     7.0711
```

---

## 모의실험으로 확인하기

```python
import numpy as np

np.random.seed(42)
la = 10
n_samples = 100_000

samples = np.random.poisson(la, n_samples)

print(f"Theoretical mean: {la}")
print(f"Sample mean:      {samples.mean():.4f}")
print(f"Theoretical var:  {la}")
print(f"Sample variance:  {samples.var(ddof=1):.4f}")
```

---

## 분산지수

**분산지수**(흩어짐의 지수)는 다음과 같이 정의된다.

$$
D = \frac{\text{Var}(X)}{E[X]}
$$

푸아송분포에서는 $D = 1$ 이다(등분산). 여기에서 간단한 진단 기준이 나온다.

- $D \approx 1$: 푸아송 모형이 알맞을 수 있다
- $D > 1$: **과대분산** — 음이항분포를 생각해 보라
- $D < 1$: **과소분산** — $p$ 가 작은 이항분포를 생각해 보라

```python
import numpy as np

np.random.seed(42)

# 푸아송 자료
poisson_data = np.random.poisson(10, 1000)
D_poisson = poisson_data.var(ddof=1) / poisson_data.mean()
print(f"Poisson D = {D_poisson:.4f}")  # 1에 가까워야 한다

# 과대분산 자료(음이항분포)
from scipy.stats import nbinom
nb_data = nbinom.rvs(n=5, p=0.3, size=1000)
D_nb = nb_data.var(ddof=1) / nb_data.mean()
print(f"Neg Binomial D = {D_nb:.4f}")  # 1보다 커야 한다
```


## 연습문제

**연습문제 1.**
30일 동안 하루에 들어온 고객 불만 건수를 다음과 같이 관찰하였다.

```
3, 1, 4, 2, 7, 0, 3, 5, 1, 2, 8, 3, 2, 1, 4,
6, 0, 3, 2, 5, 1, 4, 3, 2, 1, 9, 3, 2, 4, 1
```

**(a)** 표본평균과 표본분산을 계산하여라.

**(b)** 분산지수 $D = s^2/\bar{x}$ 를 계산하여라.

**(c)** 이 자료에 푸아송 모형이 알맞아 보이는가? 그 까닭은 무엇인가?

??? success "연습문제 1 풀이"

    ```python
    import numpy as np

    data = np.array([3,1,4,2,7,0,3,5,1,2,8,3,2,1,4,
                     6,0,3,2,5,1,4,3,2,1,9,3,2,4,1])

    mean = data.mean()
    var = data.var(ddof=1)
    D = var / mean

    print(f"Sample mean: {mean:.4f}")
    print(f"Sample var:  {var:.4f}")
    print(f"Dispersion index D = {D:.4f}")

    if abs(D - 1) < 0.5:
        print("D ≈ 1: Poisson model is plausible")
    elif D > 1.5:
        print("D >> 1: Overdispersed — consider Negative Binomial")
    else:
        print("D < 1: Underdispersed — Poisson may not fit well")
    ```

    표본평균은 대략 3.0이고 표본분산은 대략 4.3이므로 $D \approx 1.44$ 이다. 이는 가벼운 과대분산을 뜻한다. 푸아송 모형도 첫 근사로는 무리가 없지만 음이항분포가 더 잘 맞을 수 있다.
