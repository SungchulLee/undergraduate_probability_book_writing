# 카이제곱확률변수의 합

이 쪽에서는 독립이고 같은 분포를 따르는 카이제곱확률변수의 합이 더하는 개수가 늘어남에 따라 정규분포로 수렴함을 모의실험으로 보인다. $\chi^2(1)$ 확률변수는 표준정규확률변수의 제곱이므로, 이 모의실험은 정규분포에서 만들어 낸 분포에 다시 중심극한정리를 적용하는 모습을 보여 주기도 한다.

## 배경

자유도가 $k$ 인 **카이제곱**확률변수 $X \sim \chi^2(k)$ 는 독립인 표준정규확률변수의 제곱 $k$ 개의 합으로 정의한다. 가장 간단한 경우는 $Z \sim N(0,1)$ 에 대하여 $X = Z^2$ 인 $X \sim \chi^2(1)$ 이다. 그 밀도함수는 다음과 같고

$$
f(x) = \frac{1}{\sqrt{2\pi x}} \, e^{-x/2}, \qquad x > 0,
$$

평균과 분산은 다음과 같다.

$$
E[X] = 1, \qquad \text{Var}(X) = 2.
$$

카이제곱분포는 감마분포의 특별한 경우이다. 곧 $\chi^2(k) = \text{Gamma}(k/2, 2)$ 이다. 독립인 $\chi^2(1)$ 복사본 $n$ 개를 더하면 다음을 얻고

$$
S_n = X_1 + X_2 + \cdots + X_n \sim \chi^2(n),
$$

그 평균과 분산은 다음과 같다.

$$
E[S_n] = n, \qquad \text{Var}(S_n) = 2n.
$$

$\chi^2(1)$ 분포는 오른쪽으로 크게 치우쳐 있으므로(왜도 $= 2\sqrt{2} \approx 2.83$) 대칭인 분포보다 정규분포로의 수렴이 느리다. 그렇더라도 $n = 30$ 쯤 되면 정규근사가 꽤 좋다.

## 코드

```python
"""i.i.d. Chi-squared(1) 확률변수의 합이 정규분포로 다가가는 모습."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 10000

fig, axes = plt.subplots(2, 3, figsize=(14, 8))
for idx, n in enumerate([2, 3, 5, 10, 30, 100]):
    ax = axes.flatten()[idx]
    S = np.sum(np.random.chisquare(1, (n, n_sim)), axis=0)
    ax.hist(S, bins=100, density=True, alpha=0.7, color='steelblue')
    mu, sigma = n, np.sqrt(2*n)
    x = np.linspace(max(0, mu - 4*sigma), mu + 4*sigma, 200)
    ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', lw=2)
    ax.set_title(f'n = {n}')
    ax.grid(True, alpha=0.3)

plt.suptitle('Sum of χ²(1) → Normal', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('chi_squared_clt.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 실행 결과

이 스크립트는 $n = 2, 3, 5, 10, 30, 100$ 에 대한 히스토그램을 $2 \times 3$ 격자로 그린다. 각 히스토그램은 10,000번의 모의실험에서 얻은 $S_n \sim \chi^2(n)$ 의 경험적 분포를 보여 주고, 그 위에 정규분포 밀도함수 $N(n, 2n)$ 을 빨간 곡선으로 겹쳐 놓는다.

- $n = 2$ 에서는 $\chi^2(2) = \text{Exp}(1/2)$ 이므로 히스토그램이 $\text{Exp}(1/2)$ 의 밀도함수를 보여 주며, 오른쪽으로 크게 치우쳐 있다.
- $n = 3$ 과 $n = 5$ 에서는 치우침이 여전히 뚜렷하지만 줄어들고 있다.
- $n = 10$ 쯤 되면 분포가 종 모양으로 보이기 시작한다.
- $n = 30$ 과 $n = 100$ 에서는 히스토그램과 정규분포 곡선이 바싹 들어맞는다.

## 뜻풀이

카이제곱분포는 통계학(가설검정, 신뢰구간)에서 바탕이 되는 분포이므로, 언제 정규근사를 쓸 수 있는지 아는 것이 실제로 중요하다.

1. **처음의 왜도가 크다.** $\chi^2(1)$ 분포의 왜도는 $2\sqrt{2} \approx 2.83$ 으로, 이 장에서 다루는 분포 가운데 가장 큰 축에 든다. $\chi^2(n)$ 의 왜도는 $2\sqrt{2/n}$ 이므로 왜도를 $0.2$ 아래로 내리려면 $n$ 이 약 $200$ 은 되어야 한다.
2. **특별한 경우 $n = 2$.** $\chi^2(2)$ 분포는 정확히 $\text{Exp}(1/2)$ 이며, 이것이 카이제곱족과 지수족을 이어 준다.
3. **표본분산과의 관계.** 통계학에서 $X_1, \ldots, X_m \sim N(\mu, \sigma^2)$ 이면 표본분산 $S^2$ 에 대하여 $(m-1)S^2/\sigma^2 \sim \chi^2(m-1)$ 이다. 표본이 클 때 $\sigma^2$ 에 대한 신뢰구간을 만들 때 카이제곱분포의 정규근사를 쓴다.

## 연습문제

**연습문제 1.**
두 밀도함수를 견주어 $\chi^2(2) = \text{Exp}(1/2)$ 임을 확인하여라.

??? success "연습문제 1 풀이"
    $\chi^2(k)$ 의 밀도함수는 $f(x) = \frac{x^{k/2-1} e^{-x/2}}{2^{k/2} \Gamma(k/2)}$ 이다. $k = 2$ 이면 다음과 같다.

    $$
    f(x) = \frac{x^0 e^{-x/2}}{2^1 \Gamma(1)} = \frac{e^{-x/2}}{2}, \qquad x > 0.
    $$

    비율이 $\lambda = 1/2$ 인 $\text{Exp}(\lambda)$ 의 밀도함수는 $x > 0$ 에서 $f(x) = \frac{1}{2} e^{-x/2}$ 이다. 둘이 같다. $\square$

---

**연습문제 2.**
$t < 1/2$ 에서 $\chi^2(k)$ 의 적률생성함수가 $M(t) = (1 - 2t)^{-k/2}$ 임을 보이고, 이를 써서 독립인 카이제곱확률변수의 합이 다시 카이제곱분포를 따름을 증명하여라.

??? success "연습문제 2 풀이"
    $\chi^2(k) = \text{Gamma}(k/2, 2)$ 이므로 그 적률생성함수는 다음과 같다.

    $$
    M(t) = (1 - 2t)^{-k/2}, \qquad t < \frac{1}{2}.
    $$

    $X_i \sim \chi^2(k_i)$ 가 독립이면 다음이 성립한다.

    $$
    M_{S}(t) = \prod_{i=1}^n (1 - 2t)^{-k_i/2} = (1-2t)^{-(k_1 + \cdots + k_n)/2},
    $$

    이것은 $\chi^2(k_1 + \cdots + k_n)$ 의 적률생성함수이다. 적률생성함수의 유일성에 따라 $S \sim \chi^2(k_1 + \cdots + k_n)$ 이다. $\square$

---

**연습문제 3.**
$\chi^2(n)$ 의 왜도를 구하고, 왜도가 $0.5$ 아래로 내려가려면 $n$ 이 얼마나 커야 하는지 구하여라.

??? success "연습문제 3 풀이"
    $\chi^2(n)$ 의 왜도는 다음과 같다.

    $$
    \gamma_1 = \sqrt{\frac{8}{n}} = \frac{2\sqrt{2}}{\sqrt{n}}.
    $$

    $\gamma_1 < 0.5$ 로 놓으면 다음을 얻는다.

    $$
    \frac{2\sqrt{2}}{\sqrt{n}} < 0.5 \implies \sqrt{n} > 4\sqrt{2} \implies n > 32.
    $$

    곧 왜도가 $0.5$ 아래로 내려가려면 $n \geq 33$ 이어야 한다.

---

**연습문제 4.**
$n$ 이 클 때 $\sqrt{2\chi^2(n)} - \sqrt{2n - 1} \approx N(0, 1)$ 이라는 잘 알려진 근사가 있다(피셔 근사). 델타 방법을 써서 $\sqrt{2\chi^2(n)}$ 의 평균과 분산을 어림잡아 유도하여라.

??? success "연습문제 4 풀이"
    $E[Y] = n$ 이고 $\text{Var}(Y) = 2n$ 인 $Y = \chi^2(n)$ 으로 놓자. 델타 방법은 매끄러운 함수 $g$ 에 대하여 $\sigma^2/\mu^2$ 이 작을 때 $g(Y) \approx N(g(\mu), [g'(\mu)]^2 \sigma^2)$ 임을 말해 준다. $g(y) = \sqrt{2y}$ 로 두면 다음과 같다.

    $$
    g'(y) = \frac{1}{\sqrt{2y}}, \qquad g(\mu) = \sqrt{2n}, \qquad [g'(\mu)]^2 \sigma^2 = \frac{1}{2n} \cdot 2n = 1.
    $$

    따라서 $\sqrt{2Y} \approx N(\sqrt{2n}, 1)$ 이다. 피셔는 근사를 더 좋게 하려고 $\sqrt{2n}$ 을 $\sqrt{2n-1}$ 로 바꾸었고, 그 결과가 $\sqrt{2\chi^2(n)} - \sqrt{2n-1} \approx N(0,1)$ 이다.

---

**연습문제 5.**
독립인 $Z_i \sim N(0,1)$ 에 대하여 $S_n = Z_1^2 + Z_2^2 + \cdots + Z_n^2$ 이 $\chi^2(n)$ 과 같은 분포를 따르는 까닭을 설명하고, 이 표현을 써서 $E[S_n] = n$ 과 $\text{Var}(S_n) = 2n$ 을 다른 방법으로 증명하여라.

??? success "연습문제 5 풀이"
    정의에 따라 $\chi^2(n)$ 은 독립인 표준정규확률변수의 제곱 $n$ 개의 합이므로 $S_n \sim \chi^2(n)$ 이다.

    적률을 보자. $\text{Var}(Z_i) = E[Z_i^2] - (E[Z_i])^2 = 1$ 이므로 $E[Z_i^2] = 1$ 이다. 선형성에 따라 $E[S_n] = n \cdot 1 = n$ 이다.

    분산을 보자. $\text{Var}(Z_i^2) = E[Z_i^4] - (E[Z_i^2])^2$ 이다. $Z_i \sim N(0,1)$ 이므로 $E[Z_i^4] = 3$ 이다(표준정규분포의 4차 적률이다). 따라서 $\text{Var}(Z_i^2) = 3 - 1 = 2$ 이고, 독립성에 따라 다음을 얻는다.

    $$
    \text{Var}(S_n) = n \cdot 2 = 2n.
    $$
