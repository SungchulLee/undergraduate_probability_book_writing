# 나란히 놓고 보기: 모든 분포

이 쪽에서는 서로 다른 여섯 개의 분포족에서 뽑은 i.i.d. 확률변수 두 개의 합을 한 화면에 나란히 보여 주는 종합판을 만든다. 모든 분포를 한 그림에 놓고 견주어 보면, 종 모양으로 다가가는 성향이 **보편적**임을 알 수 있다. 그것은 더해지는 항이 어떤 분포를 따르는지와 무관하다. 그리고 $n$ 을 $2$ 보다 크게 하면 어느 분포족에서나 수렴이 빨라진다.

## 배경

**중심극한정리**는 $X_1, X_2, \ldots, X_n$ 이 i.i.d. 이고 평균 $\mu$ 와 분산 $\sigma^2$ 이 유한하면, 표준화한 합

$$
Z_n = \frac{S_n - n\mu}{\sigma\sqrt{n}}, \qquad S_n = X_1 + X_2 + \cdots + X_n,
$$

이 $n \to \infty$ 일 때 $N(0, 1)$ 로 분포수렴한다고 말한다. 이 종합판은 서로 다른 여섯 분포에 대하여 $n = 2$ 에서 이미 시작된 수렴의 첫머리를 보여 준다.

| 분포 | 대칭인가? | 받침 | 왜도 |
|---|---|---|---|
| $\text{Bernoulli}(0.7)$ | 아니다 | $\{0, 1\}$ | $-0.87$ |
| $\text{Exp}(1)$ | 아니다 | $[0, \infty)$ | $2$ |
| $\text{Po}(1)$ | 아니다 | $\{0, 1, 2, \ldots\}$ | $1$ |
| $N(0, 1)$ | 그렇다 | $(-\infty, \infty)$ | $0$ |
| $\text{Beta}(1, 5)$ | 아니다 | $[0, 1]$ | $1.18$ |
| $F(20, 10)$ | 아니다 | $[0, \infty)$ | $1.60$ |

$n = 2$ 밖에 되지 않는데도 어느 경우에나 합은 이미 원래 분포보다 "더 종 모양"이다. 정규분포는 대조군으로 넣었다. 정규분포는 합성곱에 대하여 닫혀 있으므로 정규확률변수 두 개의 합은 정확히 정규분포를 따르기 때문이다.

## 코드

```python
"""
나란히 놓고 보기: 합은 왜 늘 정규분포를 닮는가?

이 스크립트는 여러 분포에서 뽑은 i.i.d. 확률변수 두 개의 합을 그려,
n=2 만으로도 합이 이미 원래 분포보다 "종 모양"에 가까워짐을 보인다.

n 을 키우면(n=2 를 5, 10, 30 으로 바꾸어 보아라) 중심극한정리에 따라
분포가 정규분포로 수렴한다.

출처: Distributions related to the Poisson point process, Figure 2.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

n = 2           # 더할 확률변수의 개수 (S_n = X_1 + ... + X_n)
n_sim = 10000   # 모의실험 횟수
n_bins = 100    # 히스토그램 구간의 개수

distributions = {
    'Bernoulli(0.7)': lambda size: np.random.binomial(1, 0.7, size),
    'Exp(1)':         lambda size: np.random.exponential(1.0, size),
    'Po(1)':          lambda size: np.random.poisson(1.0, size),
    'N(0,1)':         lambda size: np.random.normal(0, 1, size),
    'Beta(1,5)':      lambda size: np.random.beta(1, 5, size),
    'F(20,10)':       lambda size: np.random.f(20, 10, size),
}

fig, axes = plt.subplots(3, 2, figsize=(12, 12))
axes = axes.flatten()

for idx, (name, sampler) in enumerate(distributions.items()):
    # S_n = X_1 + ... + X_n 을 n_sim 개 만든다
    samples = np.array([sampler(n_sim) for _ in range(n)])
    sums = samples.sum(axis=0)

    ax = axes[idx]
    ax.hist(sums, bins=n_bins, density=True, alpha=0.7,
            color='steelblue', edgecolor='none')
    ax.set_title(f'S_{n} where X_i ~ {name}', fontsize=11)
    ax.set_ylabel('Density')
    ax.grid(True, alpha=0.3)

    # 견주어 볼 정규분포 곡선을 겹쳐 그린다
    mu = np.mean(sums)
    sigma = np.std(sums)
    if sigma > 0:
        x_norm = np.linspace(mu - 4*sigma, mu + 4*sigma, 200)
        ax.plot(x_norm, stats.norm.pdf(x_norm, mu, sigma),
                'r-', lw=1.5, alpha=0.7, label='Normal fit')
        ax.legend(fontsize=9)

plt.suptitle(f'Empirical Distribution of S_{n} = X_1 + X_2 + ... + X_{n}\n'
             f'(n = {n}, {n_sim:,} simulations)',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('clt_dashboard.png', dpi=150, bbox_inches='tight')
plt.show()

# 요약 통계량을 출력한다
print(f"\n{'Distribution':<18} {'Mean':>8} {'Std Dev':>10} {'Skewness':>10} {'Kurtosis':>10}")
print("-" * 60)
for name, sampler in distributions.items():
    samples = np.array([sampler(n_sim) for _ in range(n)])
    sums = samples.sum(axis=0)
    print(f"{name:<18} {np.mean(sums):8.4f} {np.std(sums):10.4f} "
          f"{stats.skew(sums):10.4f} {stats.kurtosis(sums):10.4f}")
```

## 실행 결과

이 스크립트는 여섯 분포마다 하나씩 히스토그램을 그려 $3 \times 2$ 격자로 보여 준다. 각 패널은 10,000번의 모의실험에서 얻은 $S_2 = X_1 + X_2$ 의 경험적 분포를 보여 주고, 그 위에 (표본평균과 표본표준편차로 맞춘) 빨간 정규분포 밀도함수 곡선을 겹쳐 견주게 한다.

또 이 스크립트는 분포마다 요약 통계량 표를 찍는다.

- **평균**: 각 분포족에서 $2 E[X_i]$ 에 가까워야 한다.
- **표준편차**: $\sqrt{2} \cdot \text{SD}(X_i)$ 에 가까워야 한다.
- **왜도**: 비대칭의 정도를 잰다. $0$ 에 가까울수록 종 모양에 가깝다.
- **초과첨도**: 꼬리의 무게를 잰다. $0$ 에 가까울수록 정규분포에 가깝다.

눈으로 볼 때 두드러지는 점은 다음과 같다.

- $N(0,1)$ 패널은 완벽하게 정규분포로 보인다(정규확률변수의 합은 정규분포이므로 당연하다).
- $\text{Bernoulli}(0.7)$ 패널은 막대가 (0, 1, 2 자리에) 셋뿐이어서 이산적임이 뚜렷하다.
- $\text{Exp}(1)$ 과 $F(20, 10)$ 패널은 오른쪽으로 치우쳐 있지만 원래 분포보다는 이미 매끄럽다.
- $\text{Po}(1)$ 패널은 이산적이면서 오른쪽으로 조금 치우쳐 있다.
- $\text{Beta}(1, 5)$ 패널은 $[0, 2]$ 위에서 치우쳐 있지만 연속인 모양을 보인다.

## 뜻풀이

이 종합판이 전하려는 메시지는 하나다. **중심극한정리는 보편적이다.** 원래 분포의 모양이나 받침, 대칭 여부가 어떠하든 그 합은 정규분포 모양으로 다가간다. 나란히 놓고 견주어 보면 다음을 알 수 있다.

1. **$n = 2$ 에서 이미 매끄러워지기 시작한다.** 합성곱은 언제나 더 매끄러운 분포를 만든다. 이산분포는 가질 수 있는 값이 늘어나고, 연속분포는 뾰족한 특징이 깎여 나간다.
2. **대칭인 분포가 더 빨리 수렴한다.** $N(0,1)$ 패널은 이미 정확하다. 왜도가 $0$ 인 분포는(여기에 고른 여섯에는 들어 있지 않지만 다른 쪽에서 다루었다) 중심극한정리 전개에서 가장 앞선 보정 항이 사라지므로 더 빨리 수렴한다.
3. **가장 큰 걸림돌은 왜도이다.** $\text{Exp}(1)$ 과 $F(20, 10)$ 패널이 정규분포에서 가장 눈에 띄게 벗어나 있는데, 이 둘의 왜도가 여섯 가운데 가장 크다. 베리–에센 정리가 이를 수치로 말해 준다. 수렴 속도가 $C \cdot E[|X|^3] / (\sigma^3 \sqrt{n})$ 으로 눌린다는 것이다.
4. **$n$ 을 바꾸어 보면 배울 것이 많다.** 코드는 `n = 2` 를 `n = 5`, `10`, `30` 으로 바꾸어 다시 돌려 보며 수렴이 빨라지는 모습을 볼 수 있게 짜 놓았다. 이렇게 직접 만져 보는 것이 중심극한정리에 대한 직관을 기르는 가장 좋은 방법 가운데 하나이다.

## 연습문제

**연습문제 1.**
$n = 2$ 대신 $n = 30$ 을 쓰도록 코드를 고쳐라. 이제 어느 분포가 정규분포와 구별되지 않는가? 어느 분포가 아직 벗어남을 드러내는가?

??? success "연습문제 1 풀이"
    `n = 2` 를 `n = 30` 으로 바꾸어 다시 돌린다. $n = 30$ 에서는 다음과 같다.

    - $N(0,1)$: 언제나처럼 정확히 정규분포이다.
    - $\text{Bernoulli}(0.7)$, $\text{Po}(1)$, $\text{Beta}(1,5)$: 모두 정규분포에 아주 가깝게 보인다. $n = 30$ 에서 왜도가 각각 약 $-0.87/\sqrt{30} \approx -0.16$, $1/\sqrt{30} \approx 0.18$, $1.18/\sqrt{30} \approx 0.22$ 로 작다.
    - $\text{Exp}(1)$: 왜도가 $2/\sqrt{30} \approx 0.37$ 이다. 정규분포에 가깝지만 오른쪽으로 살짝 치우친 것이 보일 수 있다.
    - $F(20, 10)$: 왜도가 $1.60/\sqrt{30} \approx 0.29$ 이다. $\text{Exp}(1)$ 과 비슷하게 거의 정규분포이다.

    $n = 30$ 에서는 여섯 가지 모두 대체로 종 모양으로 보인다.

---

**연습문제 2.**
여섯 분포 각각에 대하여 $E[X_i]$ 와 $\text{Var}(X_i)$ 를 이론적으로 구하여라. 모의실험으로 얻은 평균과 표준편차가 (알맞은 인수를 곱하면) 이와 맞아떨어짐을 확인하여라.

??? success "연습문제 2 풀이"
    | 분포 | $E[X_i]$ | $\text{Var}(X_i)$ | $E[S_2]$ | $\text{SD}(S_2)$ |
    |---|---|---|---|---|
    | $\text{Bernoulli}(0.7)$ | $0.7$ | $0.21$ | $1.4$ | $\sqrt{0.42} \approx 0.648$ |
    | $\text{Exp}(1)$ | $1$ | $1$ | $2$ | $\sqrt{2} \approx 1.414$ |
    | $\text{Po}(1)$ | $1$ | $1$ | $2$ | $\sqrt{2} \approx 1.414$ |
    | $N(0,1)$ | $0$ | $1$ | $0$ | $\sqrt{2} \approx 1.414$ |
    | $\text{Beta}(1,5)$ | $1/6$ | $5/252$ | $1/3$ | $\sqrt{10/252} \approx 0.199$ |
    | $F(20,10)$ | $10/8 = 1.25$ | $\frac{2 \cdot 10^2 \cdot 28}{20 \cdot 8^2 \cdot 6} = \frac{35}{48} \approx 0.729$ | $2.5$ | $\sqrt{2 \cdot 0.729} \approx 1.208$ |

    요약 표에 찍힌 모의실험 값들이 이 이론값에 가까워야 한다.

---

**연습문제 3.**
종합판에 $N(0,1)$ 분포를 넣은 까닭은 무엇인가? 어떤 구실을 하는가?

??? success "연습문제 3 풀이"
    $N(0,1)$ 분포는 **대조군**, 곧 기준선 구실을 한다. 정규분포족은 합성곱에 대하여 닫혀 있으므로($N(\mu_1, \sigma_1^2) + N(\mu_2, \sigma_2^2) = N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$) i.i.d. $N(0,1)$ 확률변수 $n$ 개의 합 $S_n$ 은 모든 $n$ 에 대하여 정확히 $N(0, n)$ 이다. 따라서 겹쳐 놓은 정규분포 곡선과 히스토그램이 완벽하게 맞아떨어지며, 이는 "정규분포로의 수렴"이 이미 끝났을 때의 모습을 눈으로 보여 주는 기준이 된다. 다른 패널에서 이 완벽한 일치로부터 벗어나는 정도는 모두 원래 분포가 정규분포가 아니라는 데에서 온다.

---

**연습문제 4.**
$F(20, 10)$ 분포는 왜도가 적당히 큰 분포의 예로 넣었다. 일반적인 $X \sim F(d_1, d_2)$ 에 대하여 $E[X]$ 와 $\text{Var}(X)$ 를 구하여라(분산이 존재하도록 $d_2 > 4$ 라고 가정한다).

??? success "연습문제 4 풀이"
    $d_2 > 2$ 인 $X \sim F(d_1, d_2)$ 에 대하여 다음이 성립한다.

    $$
    E[X] = \frac{d_2}{d_2 - 2}.
    $$

    $d_2 > 4$ 이면 다음이 성립한다.

    $$
    \text{Var}(X) = \frac{2 d_2^2 (d_1 + d_2 - 2)}{d_1 (d_2 - 2)^2 (d_2 - 4)}.
    $$

    $d_1 = 20$ 이고 $d_2 = 10$ 이면 $E[X] = 10/8 = 1.25$ 이고 다음을 얻는다.

    $$
    \text{Var}(X) = \frac{2 \cdot 100 \cdot 28}{20 \cdot 64 \cdot 6} = \frac{5600}{7680} = \frac{35}{48} \approx 0.729.
    $$

---

**연습문제 5.**
종합판에 일곱 번째 분포로 $\text{Cauchy}(0, 1)$ 분포를 더해 보아라. 무슨 일이 일어나는가? 중심극한정리가 적용되는가? 그 까닭은 무엇인가?

??? success "연습문제 5 풀이"
    `distributions` 사전에 다음을 더한다.

    ```python
    'Cauchy(0,1)': lambda size: np.random.standard_cauchy(size),
    ```

    그리고 부분 그림 격자를 `plt.subplots(4, 2, ...)` 로 바꾼다. 이렇게 얻은 코시 합의 히스토그램은 정규분포처럼 보이지 **않는다**. 여전히 코시분포처럼 꼬리가 두껍고 봉우리가 뾰족하다. 코시분포는 평균도 분산도 유한하지 않기 때문이다($E[|X|] = \infty$). 따라서 중심극한정리가 적용되지 않는다. 사실 i.i.d. $\text{Cauchy}(0, 1)$ 확률변수 $n$ 개의 합을 ($\sqrt{n}$ 이 아니라) $n$ 으로 나누면 다시 $\text{Cauchy}(0, 1)$ 이 된다. 코시분포는 정규분포로 수렴하지 않는 안정분포이다.

---

**연습문제 6.**
베리–에센 정리는 중심극한정리의 수렴 속도에 대한 수치적인 경계를 준다. 이 정리를 적고, 이를 써서 여섯 분포를 수렴이 빠르리라 예상되는 순서로 늘어놓아라.

??? success "연습문제 6 풀이"
    **베리–에센 정리**는 다음을 말한다. $X_1, \ldots, X_n$ 이 i.i.d. 이고 $E[X_i] = 0$, $E[X_i^2] = \sigma^2 > 0$, $E[|X_i|^3] = \rho < \infty$ 이면 다음이 성립한다.

    $$
    \sup_x \left| P\!\left(\frac{S_n}{\sigma\sqrt{n}} \leq x\right) - \mathcal{N}(x) \right| \leq \frac{C \rho}{\sigma^3 \sqrt{n}},
    $$

    여기에서 $C \leq 0.4748$ 이다(지금까지 알려진 가장 좋은 상수이다). 핵심이 되는 양은 $\rho/\sigma^3 = E[|X|^3]/(\text{Var}(X))^{3/2}$ 이다.

    $\rho/\sigma^3$ 이 작을수록 수렴이 빠르므로 그 순서로 늘어놓으면 다음과 같다.

    1. $N(0,1)$: 모든 $n$ 에 대하여 정확하다(오차가 $0$ 이다).
    2. $\text{Bernoulli}(0.7)$: 받침이 유계이고 $\rho/\sigma^3$ 이 작다.
    3. $\text{Beta}(1,5)$: 받침이 $[0,1]$ 로 유계이고 비율이 중간쯤이다.
    4. $\text{Po}(1)$: 꼬리가 가볍고 왜도가 중간쯤이다.
    5. $\text{Exp}(1)$: $\rho/\sigma^3 = E[|X-1|^3] / 1 = 2 + 2e^{-1} \approx 2.74$ 이다.
    6. $F(20,10)$: 지수분포보다 꼬리가 두껍고 여섯 가운데 $\rho/\sigma^3$ 이 가장 크다.
