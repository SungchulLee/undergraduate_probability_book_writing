# 로그정규확률변수의 합

이 쪽에서는 독립이고 같은 분포를 따르는 로그정규확률변수의 합이 더하는 개수가 늘어남에 따라 정규분포로 수렴함을 모의실험으로 보인다. 로그정규분포는 오른쪽 꼬리가 두꺼워서 이 장의 예 가운데 수렴이 가장 느린 축에 들지만, 그래도 중심극한정리는 끝내 이긴다.

## 배경

**로그정규**확률변수 $X \sim \text{LogNormal}(\mu, \sigma^2)$ 는 $Z \sim N(\mu, \sigma^2)$ 에 대하여 $X = e^Z$ 로 정의한다. 그 밀도함수는 다음과 같다.

$$
f(x) = \frac{1}{x \sigma \sqrt{2\pi}} \exp\!\left(-\frac{(\ln x - \mu)^2}{2\sigma^2}\right), \qquad x > 0.
$$

표준적인 경우인 $\mu = 0$, $\sigma = 1$ 에서는 다음과 같다.

$$
E[X] = e^{1/2}, \qquad \text{Var}(X) = (e - 1)e.
$$

독립인 $\text{LogNormal}(0, 1)$ 확률변수 $n$ 개의 합

$$
S_n = X_1 + X_2 + \cdots + X_n
$$

에 대하여 다음이 성립한다.

$$
E[S_n] = n e^{1/2}, \qquad \text{Var}(S_n) = n(e - 1)e.
$$

흔히 보는 여러 분포족과 달리 로그정규확률변수의 합은 로그정규분포가 **아니다**. $S_n$ 의 분포를 닫힌 꼴로 적을 수 없다. $\text{LogNormal}(0, 1)$ 분포는 오른쪽 꼬리가 두껍고 왜도가 크다는 점(약 $6.18$)이 두드러지며, 그래서 꼬리가 가벼운 분포보다 정규분포로의 수렴이 느리다.

## 코드

```python
"""i.i.d. LogNormal(0,1) 확률변수의 합이 정규분포로 다가가는 모습."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 10000

fig, axes = plt.subplots(2, 3, figsize=(14, 8))
for idx, n in enumerate([2, 3, 5, 10, 30, 100]):
    ax = axes.flatten()[idx]
    S = np.sum(np.random.lognormal(0, 1, (n, n_sim)), axis=0)
    ax.hist(S, bins=100, density=True, alpha=0.7, color='steelblue')
    mu_ln, var_ln = np.exp(0.5), (np.exp(1)-1)*np.exp(1)
    mu, sigma = n * mu_ln, np.sqrt(n * var_ln)
    x = np.linspace(max(0, mu - 4*sigma), mu + 4*sigma, 200)
    ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', lw=2)
    ax.set_title(f'n = {n}')
    ax.grid(True, alpha=0.3)

plt.suptitle('Sum of LogNormal(0,1) → Normal', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('lognormal_clt.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 실행 결과

이 스크립트는 $n = 2, 3, 5, 10, 30, 100$ 에 대한 히스토그램을 $2 \times 3$ 격자로 그린다. 각 히스토그램은 10,000번의 모의실험에서 얻은 $S_n$ 의 경험적 분포를 보여 주고, 그 위에 정규분포 밀도함수 $N(n e^{1/2}, \, n(e-1)e)$ 를 빨간 곡선으로 겹쳐 놓는다.

- $n = 2$ 와 $n = 3$ 에서는 히스토그램이 오른쪽으로 크게 치우쳐 긴 꼬리를 드리운다.
- $n = 5$ 쯤 되어도 모양이 눈에 띄게 비대칭이다.
- $n = 10$ 에서는 겹쳐 놓은 정규분포 곡선이 가운데 부분은 잡아내지만 오른쪽 꼬리는 놓친다.
- $n = 30$ 에서는 들어맞는 정도가 크게 나아지고, $n = 100$ 에서는 히스토그램이 정규분포 곡선에 가까워진다.

## 뜻풀이

로그정규분포는 중심극한정리를 혹독하게 시험한다. 모든 적률이 유한하므로 중심극한정리가 적용되기는 하지만 수렴이 느리다.

1. **왜도가 극단적으로 크다.** $\text{LogNormal}(0, 1)$ 의 왜도는 $(e + 2)\sqrt{e - 1} \approx 6.18$ 이다. 복사본 $n$ 개를 더한 합의 왜도는 $6.18/\sqrt{n}$ 이며, $n = 100$ 에서도 여전히 약 $0.62$ 이다. 지수분포(왜도 $2/\sqrt{n}$)나 균등분포(왜도 $0$)와 견주어 보아라.
2. **꼬리가 두껍지만 유한하다.** 로그정규분포의 꼬리는 어떤 거듭제곱 법칙보다도 빨리 줄어들지만 지수 꼬리보다는 느리게 줄어든다. 모든 적률이 존재하므로 중심극한정리가 적용되지만, 꼬리가 천천히 줄어드는 탓에 수렴이 느리다.
3. **실제로 자주 만난다.** 로그정규확률변수의 합은 금융(포트폴리오 수익률), 신뢰성 공학(시스템 수명), 무선통신(신호 세기)에서 나타난다. 정규분포로의 수렴이 느리다는 것은, 이런 응용에서는 $n$ 이 아주 크지 않은 한 정규근사를 조심해서 써야 한다는 뜻이다.

## 연습문제

**연습문제 1.**
바탕이 되는 정규확률변수의 적률생성함수를 써서 $X \sim \text{LogNormal}(\mu, \sigma^2)$ 의 $E[X]$ 와 $\text{Var}(X)$ 를 유도하여라.

??? success "연습문제 1 풀이"
    $Z \sim N(\mu, \sigma^2)$ 에 대하여 $X = e^Z$ 이므로 다음이 성립한다.

    $$
    E[X] = E[e^Z] = M_Z(1) = e^{\mu + \sigma^2/2}.
    $$

    $$
    E[X^2] = E[e^{2Z}] = M_Z(2) = e^{2\mu + 2\sigma^2}.
    $$

    $$
    \text{Var}(X) = E[X^2] - (E[X])^2 = e^{2\mu + 2\sigma^2} - e^{2\mu + \sigma^2} = e^{2\mu + \sigma^2}(e^{\sigma^2} - 1).
    $$

    $\mu = 0$, $\sigma = 1$ 이면 $E[X] = e^{1/2}$ 이고 $\text{Var}(X) = e^1(e^1 - 1) = (e-1)e$ 이다.

---

**연습문제 2.**
독립인 로그정규확률변수의 곱은 로그정규분포이지만 그 합은 그렇지 않음을 보이고, 무엇이 그 차이를 만드는지 설명하여라.

??? success "연습문제 2 풀이"
    독립인 $Z_i \sim N(\mu_i, \sigma_i^2)$ 에 대하여 $X_i = e^{Z_i}$ 이면 다음이 성립한다.

    $$
    \prod_{i=1}^n X_i = e^{Z_1 + Z_2 + \cdots + Z_n}.
    $$

    $Z_1 + \cdots + Z_n \sim N(\sum \mu_i, \sum \sigma_i^2)$ 이므로 그 곱은 로그정규분포이다.

    한편 합 $X_1 + X_2 + \cdots + X_n = e^{Z_1} + e^{Z_2} + \cdots + e^{Z_n}$ 은 어떤 정규확률변수 $W$ 에 대해서도 $e^W$ 꼴로 적을 수 없으므로 로그정규분포가 아니다. 핵심은 로그 변환이 곱을 합으로 바꾸어 주고(합은 정규성을 보존한다) 지수함수들의 합에 대해서는 그런 변환이 없다는 데 있다.

---

**연습문제 3.**
$\text{LogNormal}(0, \sigma^2)$ 의 왜도를 $\sigma$ 의 함수로 구하고 $\sigma \in [0.1, 2]$ 에서 그려라. 왜도가 (지수분포와 같은) $2$ 가 되는 $\sigma$ 의 값은 얼마인가?

??? success "연습문제 3 풀이"
    $\text{LogNormal}(\mu, \sigma^2)$ 의 왜도는 다음과 같다.

    $$
    \gamma_1 = (e^{\sigma^2} + 2)\sqrt{e^{\sigma^2} - 1}.
    $$

    이 값은 $\mu$ 와 무관하고 $\sigma$ 에만 좌우된다. $\gamma_1 = 2$ 로 놓으면 다음과 같다.

    $$
    (e^{\sigma^2} + 2)\sqrt{e^{\sigma^2} - 1} = 2.
    $$

    $u = e^{\sigma^2}$ 로 놓으면 $(u + 2)\sqrt{u - 1} = 2$ 이다. 양변을 제곱하면 $(u+2)^2(u-1) = 4$ 이다. $u \approx 1.22$ (곧 $\sigma^2 \approx 0.20$, $\sigma \approx 0.45$)를 넣어 보면 $(3.22)^2(0.22) \approx 2.28$ 로 너무 크다. 수치적으로 풀면 $\sigma \approx 0.37$ 을 얻는다. 곧 $\text{LogNormal}(0, 0.14)$ 분포가 $\text{Exp}(1)$ 과 같은 왜도를 가진다.

---

**연습문제 4.**
꼬리가 두꺼운데도 로그정규확률변수의 합에 중심극한정리가 적용되는 까닭은 무엇인가? 성립해야 하는 조건을 정확히 적어라.

??? success "연습문제 4 풀이"
    중심극한정리는 더해지는 항들이 i.i.d. 이고 **평균과 분산이 유한할** 것을 요구한다. $X \sim \text{LogNormal}(\mu, \sigma^2)$ 에 대하여 다음이 성립한다.

    $$
    E[X] = e^{\mu + \sigma^2/2} < \infty, \qquad \text{Var}(X) = e^{2\mu + \sigma^2}(e^{\sigma^2} - 1) < \infty.
    $$

    유한한 $\mu$ 와 $\sigma^2$ 에 대하여 둘 다 유한하므로 중심극한정리가 적용된다. 사실 로그정규분포의 모든 적률이 유한하다. 곧 $E[X^k] = e^{k\mu + k^2\sigma^2/2} < \infty$ 이다. 로그정규분포의 "두꺼운 꼬리"는 분산이 무한한 거듭제곱 법칙 분포($\alpha \leq 2$ 인 파레토분포 같은 것)보다는 가벼우며, 그런 분포에서는 중심극한정리가 성립하지 않는다.

---

**연습문제 5.**
$\text{LogNormal}(0, 0.25)$ (곧 $\sigma = 0.5$)를 쓰도록 코드를 고쳐라. $\sigma = 1$ 인 경우와 수렴 속도를 견주면 어떠한가?

??? success "연습문제 5 풀이"
    `np.random.lognormal(0, 1, ...)` 를 `np.random.lognormal(0, 0.5, ...)` 로 바꾸고 적률 계산도 다음과 같이 고친다.

    ```python
    mu_ln = np.exp(0.5 * 0.25)       # = exp(0.125)
    var_ln = (np.exp(0.25) - 1) * np.exp(0.25)
    ```

    $\text{LogNormal}(0, 0.25)$ 의 왜도는 $(e^{0.25} + 2)\sqrt{e^{0.25} - 1} \approx (1.284 + 2)\sqrt{0.284} \approx 1.75$ 로, $\sigma = 1$ 일 때의 $6.18$ 보다 훨씬 작다. 정규분포로의 수렴이 눈에 띄게 빨라져서, $n \geq 30$ 까지 갈 것 없이 $n = 10$ 쯤이면 히스토그램이 종 모양으로 보인다.
