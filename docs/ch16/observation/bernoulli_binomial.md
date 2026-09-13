# 베르누이확률변수와 이항확률변수의 합

이 쪽에서는 독립이고 같은 분포를 따르는 베르누이확률변수의 합 — 그것 자체가 이항확률변수이다 — 이 더하는 개수 $n$ 이 커질수록 정규분포 모양으로 분포수렴함을 모의실험으로 보인다. $n$ 을 키워 가며 그린 히스토그램 위에 이론적인 정규분포 밀도함수를 겹쳐 놓아, 중심극한정리를 미리 엿보게 한다.

## 배경

모수가 $p$ 인 **베르누이**확률변수 $X$ 는 확률 $p$ 로 값 $1$ 을, 확률 $1-p$ 로 값 $0$ 을 가진다. 그 평균과 분산은 다음과 같다.

$$
E[X] = p, \qquad \text{Var}(X) = p(1-p).
$$

독립인 $\text{Bernoulli}(p)$ 확률변수 $n$ 개의 합은 $\text{Binomial}(n, p)$ 확률변수이다.

$$
S_n = X_1 + X_2 + \cdots + X_n \sim \text{Bin}(n, p).
$$

$S_n$ 의 평균과 분산은 다음과 같다.

$$
E[S_n] = np, \qquad \text{Var}(S_n) = np(1-p).
$$

$n$ 이 커지면 중심극한정리에 따라 표준화한 합 $(S_n - np)/\sqrt{np(1-p)}$ 이 $N(0,1)$ 로 분포수렴한다. 이항분포는 이 수렴을 눈으로 바로 볼 수 있는 고전적인 무대이다. 더해지는 항 하나하나는 값을 두 개밖에 갖지 못하는데도, 그 합은 금세 종 모양을 띤다.

## 코드

```python
"""i.i.d. Bernoulli(0.7) 확률변수의 합이 정규분포로 다가가는 모습."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 10000
p = 0.7

fig, axes = plt.subplots(2, 3, figsize=(14, 8))
for idx, n in enumerate([2, 5, 10, 20, 50, 100]):
    ax = axes.flatten()[idx]
    S = np.random.binomial(n, p, n_sim)
    ax.hist(S, bins=range(int(S.min()), int(S.max())+2), density=True,
            alpha=0.7, color='steelblue', edgecolor='black', align='left')
    mu, sigma = n*p, np.sqrt(n*p*(1-p))
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 200)
    ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', lw=2)
    ax.set_title(f'Bin({n}, {p})')
    ax.grid(True, alpha=0.3)

plt.suptitle('Sum of Bernoulli(0.7) -> Normal', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('bernoulli_binomial_clt.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 실행 결과

이 스크립트는 $n = 2, 5, 10, 20, 50, 100$ 에 대한 히스토그램을 $2 \times 3$ 격자로 그린다. 각 히스토그램은 10,000번의 모의실험에서 얻은 $S_n \sim \text{Bin}(n, 0.7)$ 의 경험적 분포를 보여 주고, 그 위에 정규분포 밀도함수 $N(np, \, np(1-p))$ 를 빨간 곡선으로 겹쳐 견주게 한다.

- $n$ 이 작을 때(예를 들어 $n = 2$)에는 히스토그램이 눈에 띄게 이산적이고 비대칭이다.
- $n = 10$ 쯤 되면 히스토그램이 종 모양을 닮기 시작한다.
- $n = 50$ 과 $n = 100$ 에서는 히스토그램과 정규분포 곡선을 거의 구별할 수 없다.

## 뜻풀이

이 히스토그램들은 **이항분포의 정규근사**를 보여 준다. $n$ 이 커지면 $\text{Bin}(n, p)$ 는 $N(np, np(1-p))$ 로 잘 근사된다. 눈여겨볼 만한 점이 몇 가지 있다.

1. **비대칭이 사라진다.** $p = 0.7$ 이면 베르누이분포가 한쪽으로 치우쳐 있고, $n$ 이 작을 때에는 그 합도 이 치우침을 물려받는다. $n$ 이 커지면 왜도가 $1/\sqrt{n}$ 의 속도로 줄어든다.
2. **이산성이 씻겨 나간다.** $S_n$ 은 언제나 정수이지만, $n$ 이 커지면 가질 수 있는 값들 사이의 간격이 표준편차에 견주어 작아져 분포가 연속처럼 보인다.
3. **$n$ 이 그리 크지 않아도 정규분포 곡선이 잘 들어맞는다.** 실제로 정규근사를 쓸 수 있는 기준으로 $np \geq 5$ 와 $n(1-p) \geq 5$ 라는 어림 규칙이 흔히 인용되는 까닭이 여기에 있다.

## 연습문제

**연습문제 1.**
$p = 0.5$ (공정한 동전)로 모의실험을 돌려 보아라. $p = 0.7$ 인 경우와 견주어 수렴이 얼마나 빠른가? 그 까닭을 설명하여라.

??? success "연습문제 1 풀이"
    $p = 0.5$ 이면 베르누이 시행 하나하나가 대칭이므로, 모든 $n$ 에 대하여 합 $S_n$ 이 평균 $n/2$ 을 중심으로 대칭이다. 정규분포도 대칭이므로 $n$ 이 작아도 근사가 잘 맞는다. 이에 견주어 $p = 0.7$ 은 크기가 $(1 - 2p)/\sqrt{np(1-p)} = -0.4/\sqrt{n \cdot 0.21}$ 인 왜도를 만들어 내며, 이것이 무시할 만해지려면 $n$ 이 더 커야 한다. 따라서 $p = 0.5$ 일 때 수렴이 더 빠르다.

---

**연습문제 2.**
$S_n \sim \text{Bin}(n, p)$ 에 대하여 왜도 $\gamma_1 = E[(S_n - \mu)^3]/\sigma^3$ 을 구하고, $n \to \infty$ 일 때 이것이 $0$ 으로 감을 보여라.

??? success "연습문제 2 풀이"
    $\text{Bernoulli}(p)$ 확률변수 하나의 3차 중심적률은 $E[(X - p)^3] = p(1-p)(1-2p)$ 이다. 독립성에 따라 $S_n$ 의 3차 중심적률은 $n \cdot p(1-p)(1-2p)$ 이다. 또 $S_n$ 의 표준편차는 $\sigma = \sqrt{np(1-p)}$ 이다. 따라서 다음이 성립한다.

    $$
    \gamma_1 = \frac{n \cdot p(1-p)(1-2p)}{[np(1-p)]^{3/2}} = \frac{1 - 2p}{\sqrt{np(1-p)}}.
    $$

    $n \to \infty$ 일 때 $\gamma_1 \to 0$ 이므로 왜도가 사라지고 분포가 정규분포처럼 대칭이 됨을 알 수 있다.

---

**연습문제 3.**
$S_{100} \sim \text{Bin}(100, 0.7)$ 일 때 연속성 보정을 쓴 정규근사로 $P(S_{100} \leq 65)$ 를 어림하여라. 그리고 정확한 값과 견주어라.

??? success "연습문제 3 풀이"
    $\mu = 100 \cdot 0.7 = 70$ 이고 $\sigma = \sqrt{100 \cdot 0.7 \cdot 0.3} = \sqrt{21} \approx 4.583$ 이다. 연속성 보정을 쓰면 다음을 얻는다.

    $$
    P(S_{100} \leq 65) \approx P\!\left(Z \leq \frac{65.5 - 70}{\sqrt{21}}\right) = P\!\left(Z \leq \frac{-4.5}{4.583}\right) = P(Z \leq -0.982) \approx 0.163.
    $$

    정확한 값(`scipy.stats.binom.cdf(65, 100, 0.7)` 로 계산한다)은 약 $0.1631$ 이다. 근사가 아주 훌륭하다.

---

**연습문제 4.**
$n \to \infty$ 일 때 $\text{Bin}(n, p)$ 의 적률생성함수가 적절한 뜻에서 $N(np, np(1-p))$ 의 적률생성함수로 수렴함을 증명하여라. (힌트: 표준화한 변수를 가지고 다룬다.)

??? success "연습문제 4 풀이"
    $Z_n = (S_n - np)/\sqrt{np(1-p)}$ 으로 놓자. 표준화한 베르누이확률변수 하나의 적률생성함수는 다음과 같다.

    $$
    M_{(X_i - p)/\sqrt{p(1-p)}}(t) = (1-p)e^{-pt/\sqrt{p(1-p)}} + p \, e^{(1-p)t/\sqrt{p(1-p)}}.
    $$

    독립성에 따라 $M_{Z_n}(t) = \left[M_{(X_1 - p)/\sqrt{p(1-p)}}(t/\sqrt{n})\right]^n$ 이다. 작은 $u = t/\sqrt{n}$ 에 대하여 $e^{u}$ 를 테일러 급수로 펼치면 다음을 얻는다.

    $$
    M_{(X_1-p)/\sqrt{p(1-p)}}(t/\sqrt{n}) = 1 + \frac{t^2}{2n} + O(n^{-3/2}).
    $$

    따라서 $n \to \infty$ 일 때 $M_{Z_n}(t) = \left(1 + \frac{t^2}{2n} + O(n^{-3/2})\right)^n \to e^{t^2/2}$ 이고, 이것은 $N(0,1)$ 의 적률생성함수이다. $\square$

---

**연습문제 5.**
$S_n$ 대신 표준화한 합 $(S_n - np)/\sqrt{np(1-p)}$ 을 그리고 그 위에 표준정규분포 $N(0,1)$ 의 밀도함수를 겹치도록 코드를 고쳐라. 여섯 개 패널이 모두 같은 곡선을 겹쳐 쓰게 됨을 확인하여라.

??? success "연습문제 5 풀이"
    반복문 안의 히스토그램과 곡선 부분을 다음으로 바꾼다.

    ```python
    S = np.random.binomial(n, p, n_sim)
    Z = (S - n*p) / np.sqrt(n*p*(1-p))
    ax.hist(Z, bins=30, density=True, alpha=0.7, color='steelblue', edgecolor='black')
    x = np.linspace(-4, 4, 200)
    ax.plot(x, stats.norm.pdf(x, 0, 1), 'r-', lw=2)
    ```

    이제 모든 패널이 같은 빨간 곡선, 곧 표준정규분포 $N(0,1)$ 의 확률밀도함수를 쓰며, $n$ 이 커질수록 히스토그램이 그 곡선으로 다가간다. 이것이 바로 중심극한정리의 핵심이다. 중심을 맞추고 크기를 조절하고 나면 모양이 보편적인 하나로 모인다.
