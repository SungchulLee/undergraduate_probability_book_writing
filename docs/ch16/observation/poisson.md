# 푸아송확률변수의 합

이 쪽에서는 독립이고 같은 분포를 따르는 푸아송확률변수의 합이 더하는 개수가 늘어남에 따라 정규분포로 수렴함을 모의실험으로 보인다. 독립인 푸아송확률변수의 합이 다시 푸아송분포를 따르므로, 이는 모수가 클 때 푸아송분포를 정규분포로 근사한다는 잘 알려진 사실을 보여 주기도 한다.

## 배경

**푸아송**확률변수 $X \sim \text{Po}(\lambda)$ 의 확률질량함수는 다음과 같고

$$
P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \qquad k = 0, 1, 2, \ldots
$$

평균과 분산이 모두 $\lambda$ 이다.

$$
E[X] = \lambda, \qquad \text{Var}(X) = \lambda.
$$

독립인 $\text{Po}(\lambda)$ 확률변수 $n$ 개의 합은 다시 푸아송분포를 따른다.

$$
S_n = X_1 + X_2 + \cdots + X_n \sim \text{Po}(n\lambda).
$$

$\lambda = 1$ 이면 $E[S_n] = n$ 이고 $\text{Var}(S_n) = n$ 이다. $\text{Po}(n)$ 의 왜도는 $1/\sqrt{n}$ 이라서 $0$ 으로 가고, 표준화한 분포는 중심극한정리에 따라 $N(0,1)$ 로 수렴한다. 푸아송분포의 정규근사는 $\lambda$ (또는 $n\lambda$)가 클 때 널리 쓰인다.

## 코드

```python
"""i.i.d. Po(1) 확률변수의 합이 정규분포로 다가가는 모습."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 10000

fig, axes = plt.subplots(2, 3, figsize=(14, 8))
for idx, n in enumerate([2, 3, 5, 10, 30, 100]):
    ax = axes.flatten()[idx]
    S = np.sum(np.random.poisson(1.0, (n, n_sim)), axis=0)
    ax.hist(S, bins=range(int(S.min()), int(S.max())+2), density=True,
            alpha=0.7, color='steelblue', edgecolor='black', align='left')
    mu, sigma = n, np.sqrt(n)
    x = np.linspace(max(0, mu - 4*sigma), mu + 4*sigma, 200)
    ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', lw=2)
    ax.set_title(f'n = {n}')
    ax.grid(True, alpha=0.3)

plt.suptitle('Sum of Po(1) → Normal', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('poisson_clt.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 실행 결과

이 스크립트는 $n = 2, 3, 5, 10, 30, 100$ 에 대한 히스토그램을 $2 \times 3$ 격자로 그린다. 각 히스토그램은 10,000번의 모의실험에서 얻은 $S_n \sim \text{Po}(n)$ 의 경험적 확률질량함수를 정수 구간의 막대그래프로 보여 주고, 그 위에 정규분포 밀도함수 $N(n, n)$ 을 빨간 곡선으로 겹쳐 놓는다.

- $n = 2$ 에서는 히스토그램이 이산적이고 오른쪽으로 치우친 것이 눈에 띈다.
- $n = 5$ 쯤 되면 이산적이면서도 종 모양을 닮기 시작한다.
- $n = 10$ 에서는 정규근사가 잘 들어맞는다.
- $n = 30$ 과 $n = 100$ 에서는 히스토그램과 정규분포 곡선을 거의 구별할 수 없고, 가질 수 있는 값이 많아진 탓에 푸아송분포의 이산성도 거의 보이지 않는다.

## 뜻풀이

푸아송분포는 이산분포에 대한 중심극한정리를 깔끔하게 보여 준다.

1. **합성곱에 대하여 닫혀 있다.** 대부분의 분포와 달리 푸아송족은 덧셈에 대하여 닫혀 있다. 곧 $\text{Po}(\lambda_1) + \text{Po}(\lambda_2) = \text{Po}(\lambda_1 + \lambda_2)$ 이다. 따라서 $\text{Po}(1)$ 을 $n$ 개 더하는 일은 $\text{Po}(n)$ 하나를 관찰하는 일과 같고, 우리가 실제로 보고 있는 것은 $\mu \to \infty$ 일 때 $\text{Po}(\mu)$ 에 무슨 일이 일어나는가이다.
2. **왜도가 $1/\sqrt{\mu}$ 이다.** 푸아송분포의 왜도는 $1/\sqrt{\mu}$ 이므로 $\mu$ 가 커지면 줄어든다. $\mu = 100$ 이면 왜도가 $0.1$ 밖에 되지 않으니 정규분포가 훌륭하게 들어맞는 까닭을 알 수 있다.
3. **실용적인 어림 규칙.** $\text{Po}(\mu)$ 의 정규근사는 흔히 $\mu \geq 20$ 이면 충분하다고 본다. 연속성 보정을 곁들이면 $\mu \geq 10$ 정도에서도 잘 맞는다.

## 연습문제

**연습문제 1.**
정규근사를 써서 $S_{30} \sim \text{Po}(30)$ 일 때 $P(S_{30} \geq 35)$ 를 어림하여라. `scipy.stats.poisson.sf(34, 30)` 으로 얻은 정확한 값과 견주어라.

??? success "연습문제 1 풀이"
    $\mu = 30$ 이고 $\sigma = \sqrt{30} \approx 5.477$ 이므로 다음을 얻는다.

    $$
    P(S_{30} \geq 35) \approx P\!\left(Z \geq \frac{34.5 - 30}{\sqrt{30}}\right) = P\!\left(Z \geq \frac{4.5}{5.477}\right) = P(Z \geq 0.821) \approx 0.206.
    $$

    (이산확률변수에 대하여 $P(S \geq 35)$ 를 구하는 것이므로 연속성 보정으로 $34.5$ 를 썼다.) 정확한 값은 `scipy.stats.poisson.sf(34, 30)` $\approx 0.2048$ 이다. 근사가 가깝다.

---

**연습문제 2.**
$\text{Po}(\lambda)$ 의 적률생성함수가 $M_X(t) = e^{\lambda(e^t - 1)}$ 임을 보이고, 이를 써서 독립인 푸아송확률변수의 합이 푸아송분포를 따름을 증명하여라.

??? success "연습문제 2 풀이"
    적률생성함수는 다음과 같다.

    $$
    M_X(t) = E[e^{tX}] = \sum_{k=0}^{\infty} e^{tk} \frac{\lambda^k e^{-\lambda}}{k!} = e^{-\lambda} \sum_{k=0}^{\infty} \frac{(\lambda e^t)^k}{k!} = e^{-\lambda} \cdot e^{\lambda e^t} = e^{\lambda(e^t - 1)}.
    $$

    독립인 $X_i \sim \text{Po}(\lambda_i)$ 에 대하여 다음이 성립한다.

    $$
    M_{S_n}(t) = \prod_{i=1}^n e^{\lambda_i(e^t - 1)} = e^{(\lambda_1 + \cdots + \lambda_n)(e^t - 1)},
    $$

    이것은 $\text{Po}(\lambda_1 + \cdots + \lambda_n)$ 의 적률생성함수이다. 적률생성함수의 유일성에 따라 $S_n \sim \text{Po}(\lambda_1 + \cdots + \lambda_n)$ 이다. $\square$

---

**연습문제 3.**
$\text{Po}(\mu)$ 의 왜도와 초과첨도를 구하고, $\mu \to \infty$ 일 때 둘 다 $0$ 으로 감을 확인하여라.

??? success "연습문제 3 풀이"
    $\text{Po}(\mu)$ 의 누적률은 모두 $\mu$ 와 같다. 곧 $\kappa_1 = \kappa_2 = \kappa_3 = \kappa_4 = \mu$ 이다. 왜도와 초과첨도는 다음과 같다.

    $$
    \gamma_1 = \frac{\kappa_3}{\kappa_2^{3/2}} = \frac{\mu}{\mu^{3/2}} = \frac{1}{\sqrt{\mu}},
    $$

    $$
    \gamma_2 = \frac{\kappa_4}{\kappa_2^2} = \frac{\mu}{\mu^2} = \frac{1}{\mu}.
    $$

    $\mu \to \infty$ 일 때 $\gamma_1 \to 0$ 이고 $\gamma_2 \to 0$ 이므로, 왜도가 $0$ 이고 초과첨도도 $0$ 인 정규분포로 수렴함을 확인할 수 있다.

---

**연습문제 4.**
푸아송분포는 이항분포의 극한으로 얻을 수 있다. 곧 $\text{Bin}(n, \lambda/n) \to \text{Po}(\lambda)$ 이다. 이것이 베르누이 합에 대한 중심극한정리와 어떤 관계인지 설명하여라.

??? success "연습문제 4 풀이"
    $p = \lambda/n$ 인 $X \sim \text{Bin}(n, p)$ 는 $Y_i \sim \text{Bernoulli}(\lambda/n)$ 에 대하여 $X = \sum_{i=1}^n Y_i$ 로 적을 수 있다. $\lambda$ 를 고정한 채 $n \to \infty$ 로 보내면 다음과 같다.

    - **푸아송 극한정리**는 $X$ 가 $\text{Po}(\lambda)$ 로 분포수렴한다고 말한다. 여기에서는 $n \to \infty$ 일 때 $p \to 0$ 이다.
    - **중심극한정리**는 표준화한 $(X - np)/\sqrt{np(1-p)}$ 가 $N(0,1)$ 로 간다고 말한다. 여기에서는 $p$ 가 고정되어 있다.

    두 가지는 서로 다른 점근적 상황이다. 푸아송 극한에서는 $p$ 가 줄어들어 평균 $np = \lambda$ 가 그대로이므로 합이 "거의 자라지 않는다." 중심극한정리에서는 $p$ 가 고정되어 평균이 $n$ 처럼 자라므로 합이 실제로 쌓여 간다. 둘 다 각자의 상황에서는 타당한 근사이다.

---

**연습문제 5.**
각 $X_i \sim \text{Po}(3)$ 인 $S_n$ 을 모의실험하도록 코드를 고쳐라. $S_n$ 의 분포는 무엇인가? 정규근사 $N(3n, 3n)$ 이 여전히 잘 맞는지 확인하여라.

??? success "연습문제 5 풀이"
    닫힘 성질에 따라 각 $X_i \sim \text{Po}(3)$ 일 때 $S_n \sim \text{Po}(3n)$ 이다. 코드에서는 `np.random.poisson(1.0, ...)` 를 `np.random.poisson(3.0, ...)` 로 바꾸고 `mu, sigma = 3*n, np.sqrt(3*n)` 으로 두면 된다. 정규근사 $N(3n, 3n)$ 이 잘 맞으며, 왜도가 $1/\sqrt{n}$ 이 아니라 $1/\sqrt{3n}$ 이므로 사실 수렴이 더 빠르다. 따라서 같은 $n$ 에서도 $\lambda = 1$ 인 경우보다 근사가 더 좋다.
