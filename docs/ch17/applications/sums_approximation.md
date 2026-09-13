# 확률변수 합의 근사

## 일반적인 절차

평균이 $\mu$ 이고 분산이 $\sigma^2$ 인 i.i.d. $X_1, \ldots, X_n$ 이 주어지면 중심극한정리에 따라 다음이 성립한다.

$$S_n = \sum_{k=1}^n X_k \approx N(n\mu, \, n\sigma^2)$$

$P(S_n \leq a)$ 를 구하려면 다음과 같이 한다.

**1단계.** 표준화한다.

$$P(S_n \leq a) = P\left(\frac{S_n - n\mu}{\sigma\sqrt{n}} \leq \frac{a - n\mu}{\sigma\sqrt{n}}\right)$$

**2단계.** 중심극한정리를 적용한다.

$$\approx \mathcal{N}\left(\frac{a - n\mu}{\sigma\sqrt{n}}\right)$$

## 예: 시험 채점 시간

어떤 교수가 시험지 $50$ 장을 차례로 채점해야 한다. 시험지 한 장을 채점하는 데 걸리는 시간은 i.i.d. 이고 평균이 $20$ 분, 표준편차가 $4$ 분이다. $450$ 분 안에 적어도 $25$ 장을 채점할 확률은 얼마인가?

$X_k$ 를 $k$ 번째 시험지를 채점하는 데 걸리는 시간이라 하면 $\mu = 20$, $\sigma = 4$ 이다.

$$S_{25} = \sum_{k=1}^{25} X_k$$

$P(S_{25} \leq 450)$ 을 구하면 된다.

$$P(S_{25} \leq 450) = P\left(\frac{S_{25} - 25 \cdot 20}{4\sqrt{25}} \leq \frac{450 - 25 \cdot 20}{4\sqrt{25}}\right)$$

$$\approx \mathcal{N}\left(\frac{450 - 500}{20}\right) = \mathcal{N}(-2.5) = 0.0062$$

$450$ 분 안에 $25$ 장을 다 채점할 확률은 약 $0.62\%$ 밖에 되지 않는다.

## 예: 공정한 동전 던지기

$X_i$ 를 공정한 동전의 $i$ 번째 던지기 결과라 하고 앞면은 $H = 1$, 뒷면은 $T = 0$ 으로 적는다고 하자. $Y_i = 2X_i - 1$ 로 두면 앞면과 뒷면이 각각 $+1$ 과 $-1$ 로 적힌다.

그러면 $E[Y_i] = 0$, $E[Y_i^2] = 1$, $\text{Var}(Y_i) = 1$ 이다.

| 확률변수 | 평균 | 분산 | 근사적인 분포 |
|----------------|------|----------|-------------------------|
| $Y_i$ | $0$ | $1$ | — |
| $\sum_{i=1}^n Y_i$ | $0$ | $n$ | $N(0, n)$ |
| $\frac{1}{\sqrt{n}}\sum_{i=1}^n Y_i$ | $0$ | $1$ | $N(0, 1)$ |
| $\frac{1}{\sqrt{n}}\sum_{i=1}^{nt} Y_i$ | $0$ | $t$ | $N(0, t)$ |
| $\frac{1}{\sqrt{n}}\sum_{i=ns+1}^{nt} Y_i$ | $0$ | $t - s$ | $N(0, t-s)$ |

!!! note "브라운 운동과의 관계"
    마지막 두 줄은 **브라운 운동** $B(t)$ 를 만드는 방법을 넌지시 일러 준다. 브라운 운동은 크기를 조절한 확률보행의 연속시간 극한이다. $B(t) \sim N(0, t)$ 이고 증분 $B(t) - B(s) \sim N(0, t-s)$ 가 독립인데, 이는 위의 중심극한정리 근사와 정확히 들어맞는다.

## 파이썬 구현

```python
import numpy as np
from scipy import stats

# 시험 채점 예제
n = 25
mu, sigma = 20, 4
threshold = 450

z = (threshold - n * mu) / (sigma * np.sqrt(n))
prob = stats.norm.cdf(z)
print(f"P(S_25 <= 450) ≈ {prob:.4f}")

# 모의실험으로 확인한다
np.random.seed(42)
N_sim = 100000
sums = np.sum(np.random.normal(mu, sigma, (N_sim, n)), axis=1)
sim_prob = np.mean(sums <= threshold)
print(f"Simulated:        {sim_prob:.4f}")
```

**실행 결과:**
```
P(S_25 <= 450) ≈ 0.0062
Simulated:        0.0063
```

## 연습문제

**연습문제 1.**
$X_1, \ldots, X_{100}$ 이 i.i.d. 이고 $E[X_i] = 5$, $\text{Var}(X_i) = 9$ 라고 하자. 중심극한정리를 써서 다음을 어림하여라.

(a) $P(S_{100} \leq 520)$

(b) $P(480 \leq S_{100} \leq 520)$

(c) $P(S_{100} \geq 530)$

---

**연습문제 2.**
공정한 주사위를 $360$ 번 던진다. $S$ 를 나온 눈의 총합이라 하자. 중심극한정리를 써서 다음을 어림하여라.

(a) $P(S \geq 1300)$

(b) $P(1200 \leq S \leq 1300)$

*힌트: 주사위를 한 번 던지면 $\mu = 3.5$ 이고 $\sigma^2 = 35/12$ 이다.*
