# 왜도와 첨도

## 왜도 — 대칭성을 재는 값

### 정의

평균이 $\mu$ 이고 표준편차가 $\sigma$ 인 확률변수 $X$ 의 **왜도**는 다음과 같다.

$$\text{왜도}(X) = E\left[\left(\frac{X - \mu}{\sigma}\right)^3\right]$$

이산인 경우와 연속인 경우로 나누어 쓰면 다음과 같다.

$$\text{왜도}(X) = \begin{cases} \displaystyle\sum_x \left(\frac{x - \mu}{\sigma}\right)^3 p(x) & X \text{ 가 이산일 때} \\[10pt] \displaystyle\int_{-\infty}^{\infty} \left(\frac{x - \mu}{\sigma}\right)^3 f(x)\,dx & X \text{ 가 연속일 때} \end{cases}$$

### 뜻풀이

| 왜도 | 모양 | 설명 |
|----------|-------|-------------|
| 음수 | 왼쪽으로 치우침 | 꼬리가 왼쪽으로 뻗는다; 평균 < 중앙값 < 최빈값 |
| 0 | 대칭 | 평균을 중심으로 균형을 이룬다 (예: 정규분포) |
| 양수 | 오른쪽으로 치우침 | 꼬리가 오른쪽으로 뻗는다; 최빈값 < 중앙값 < 평균 |

### 주요 성질

- **대칭인** 분포(정규분포, 균등분포, $t$분포)는 모두 왜도가 $0$ 이다.
- **지수분포**의 왜도는 $2$ 이다(언제나 오른쪽으로 치우친다).
- 왜도는 무차원량이다($\sigma$ 로 표준화하면서 단위가 사라진다).

---

## 첨도 — 꼬리의 두께를 재는 값

### 정의

$X$ 의 **첨도**는 다음과 같다.

$$\text{첨도}(X) = E\left[\left(\frac{X - \mu}{\sigma}\right)^4\right]$$

$$= \begin{cases} \displaystyle\sum_x \left(\frac{x - \mu}{\sigma}\right)^4 p(x) & X \text{ 가 이산일 때} \\[10pt] \displaystyle\int_{-\infty}^{\infty} \left(\frac{x - \mu}{\sigma}\right)^4 f(x)\,dx & X \text{ 가 연속일 때} \end{cases}$$

**초과첨도**는 다음과 같이 정의한다.

$$\text{초과첨도}(X) = \text{첨도}(X) - 3$$

$3$ 을 빼는 까닭은 정규분포의 첨도가 정확히 $3$ 이기 때문이다.

### 뜻풀이

| 첨도 | 초과첨도 | 꼬리의 모습 | 이름 |
|----------|----------------|---------------|------|
| $> 3$ | $> 0$ | 두꺼운 꼬리 (정규분포보다 무겁다) | 급첨 |
| $= 3$ | $= 0$ | 정규분포와 같다 | 중첨 |
| $< 3$ | $< 0$ | 얇은 꼬리 (정규분포보다 가볍다) | 평첨 |

### 주요 성질

- 첨도는 언제나 $\geq 1$ 이다(표준화한 변수를 4제곱한 음이 아닌 양의 기댓값이기 때문이다).
- **정규분포**의 첨도는 $3$ (초과첨도 $= 0$)이며 기준이 된다.
- $\nu > 4$ 인 **$t$분포**의 초과첨도는 $6/(\nu - 4)$ 로 언제나 양수이다(두꺼운 꼬리).
- **균등분포**의 첨도는 $9/5 = 1.8$ 이다(얇은 꼬리, 평첨).

## 파이썬 구현

```python
import numpy as np
from scipy import stats

# 자주 쓰는 분포들의 왜도와 첨도 비교
distributions = {
    'Normal(0,1)':    stats.norm(0, 1),
    'Exp(1)':         stats.expon(scale=1),
    'Uniform(0,1)':   stats.uniform(0, 1),
    'Beta(2,5)':      stats.beta(2, 5),
    't(5)':           stats.t(5),
    'Chi-sq(3)':      stats.chi2(3),
}

print(f"{'Distribution':<16} {'Skewness':>10} {'Kurtosis':>10} {'Excess Kurt':>12}")
print("-" * 52)
for name, dist in distributions.items():
    skew = dist.stats(moments='s')
    kurt = dist.stats(moments='k')  # scipy 는 초과첨도를 돌려준다
    print(f"{name:<16} {float(skew):>10.4f} {float(kurt)+3:>10.4f} {float(kurt):>12.4f}")
```

**실행 결과:**
```
Distribution     Skewness   Kurtosis  Excess Kurt
----------------------------------------------------
Normal(0,1)        0.0000     3.0000        0.0000
Exp(1)             2.0000     9.0000        6.0000
Uniform(0,1)       0.0000     1.8000       -1.2000
Beta(2,5)          0.5963     2.8466       -0.1534
t(5)               0.0000     9.0000        6.0000
Chi-sq(3)          1.6330     7.0000        4.0000
```

## 연습문제

**연습문제 1.** $\text{Bernoulli}(p)$ 분포의 왜도를 구하여라. $p$ 가 어떤 값일 때 왜도가 0이 되는가?

??? success "연습문제 1 풀이"
    $X \sim \text{Bernoulli}(p)$ 라 하자. 그러면 $\mu = p$, $\sigma = \sqrt{pq}$ 이다.

    $$
    E[(X - p)^3] = (1-p)^3 \cdot p + (-p)^3 \cdot q = p(1-p)[(1-p)^2 - p^2] = pq(1 - 2p)
    $$

    $$
    \text{왜도} = \frac{pq(1-2p)}{(pq)^{3/2}} = \frac{1 - 2p}{\sqrt{pq}}
    $$

    이 값은 $p = 1/2$ 일 때(대칭인 동전) 0이고, $p < 1/2$ 이면 양수, $p > 1/2$ 이면 음수이다.

---

**연습문제 2.** $X$ 가 평균을 중심으로 대칭이면(곧 $X - \mu$ 와 $\mu - X$ 의 분포가 같으면) $\text{왜도}(X) = 0$ 임을 보여라.

??? success "연습문제 2 풀이"
    $Y = X - \mu$ 라 하자. 대칭이라는 것은 $Y \stackrel{d}{=} -Y$ 라는 뜻이다. 그러므로 $E[Y^3] = E[(-Y)^3] = -E[Y^3]$ 이고, 따라서 $2E[Y^3] = 0$ 이므로 $E[Y^3] = 0$ 이다. 왜도 $= E[Y^3]/\sigma^3 = 0$ 이다. $\square$

---

**연습문제 3.** $\text{Gamma}(\alpha, \lambda)$ 분포의 왜도는 $2/\sqrt{\alpha}$ 이다. 왜도가 1이 되는 $\alpha$ 의 값을 구하여라.

??? success "연습문제 3 풀이"
    $2/\sqrt{\alpha} = 1$ 로 놓으면 $\sqrt{\alpha} = 2$ 이므로 $\alpha = 4$ 이다.

    곧 $\text{Gamma}(4, \lambda)$ 분포의 왜도가 정확히 1이다.

---

**연습문제 4.** 어떤 분포의 평균이 5, 분산이 4, 첨도가 6이다. 초과첨도는 얼마인가? 이 분포는 급첨, 중첨, 평첨 가운데 어느 것인가?

??? success "연습문제 4 풀이"
    초과첨도 $= 6 - 3 = 3 > 0$ 이다.

    초과첨도가 양수이므로 이 분포는 **급첨**이다(정규분포보다 꼬리가 두껍다).

---

**연습문제 5.** 4차 적률이 유한한 임의의 확률변수 $X$ 에 대하여 $\text{첨도}(X) \geq 1$ 임을 증명하고, 등호가 $X$ 가 정확히 두 값만 가질 때 성립함을 보여라.

??? success "연습문제 5 풀이"
    $Z = (X - \mu)/\sigma$ 라 하자. 그러면 $E[Z^2] = 1$ 이고 $\kappa_4 = E[Z^4]$ 이다.

    볼록함수 $t \mapsto t^2$ 에 옌센 부등식을 적용하면 다음을 얻는다.

    $$
    E[Z^4] = E[(Z^2)^2] \geq (E[Z^2])^2 = 1
    $$

    옌센 부등식에서 등호는 $Z^2$ 이 거의 확실하게 상수일 때 성립하며, 이는 거의 확실하게 $|Z| = c$ 라는 뜻이다. $E[Z^2] = 1$ 이므로 $c = 1$ 이어야 하고 따라서 거의 확실하게 $Z = \pm 1$ 이다. 곧 $X$ 는 $\mu \pm \sigma$ 라는 두 값만 갖는다. $\square$
