# 예, 확장, 성립하지 않는 경우

## 서술 복습

!!! info "큰수의 약법칙(WLLN)"
    $X_1, X_2, \ldots$ 가 $E[X_i] = \mu$, $\text{Var}(X_i) = \sigma^2 < \infty$ 인 i.i.d. 확률변수라고 하자. 그러면 모든 $\varepsilon > 0$ 에 대하여 다음이 성립한다.

    $$P\!\left(\left|\bar{X}_n - \mu\right| \geq \varepsilon\right) \to 0 \quad n \to \infty \text{ 일 때}$$

    같은 말로 $\bar{X}_n \xrightarrow{p} \mu$ 이다.

표준적인 증명은 체비쇼프 부등식을 쓴다(20.3절 서술과 증명을 보아라).

## 다른 증명: 잘라내기(분산이 유한하지 않아도 된다)

큰수의 약법칙은 **분산이 유한하다는 가정 없이도** 성립한다. $E[|X|] < \infty$ 만 있으면 된다.

!!! info "큰수의 약법칙(평균만 유한한 경우)"
    $X_1, X_2, \ldots$ 가 $E[X_i] = \mu$ 인 i.i.d. 확률변수이면(분산에 대한 가정은 없다) $\bar{X}_n \xrightarrow{p} \mu$ 이다.

**증명의 얼개(잘라내기 방법).** $Y_i = X_i \cdot \mathbf{1}(|X_i| \leq n)$ 으로 잘라낸 확률변수를 정의한다. 그러면 다음이 성립한다.

1. $n \to \infty$ 일 때 $E[Y_i] \to \mu$ 이다(지배수렴정리).
2. $|Y_i| \leq n$ 이므로 $\text{Var}(Y_i) \leq E[Y_i^2] \leq n \cdot E[|X|]$ 이다.
3. $\bar{Y}_n$ 에 체비쇼프 부등식을 적용하면 $P(|\bar{Y}_n - E[Y_1]| > \varepsilon/2) \leq \frac{n E[|X|]}{n^2 (\varepsilon/2)^2} \to 0$ 이다.
4. $P(\bar{X}_n \neq \bar{Y}_n) \leq \sum P(|X_i| > n) = n P(|X_1| > n) \to 0$ 이다.

3단계와 4단계를 합치면 $P(|\bar{X}_n - \mu| > \varepsilon) \to 0$ 을 얻는다. $\square$

## 예: 지수분포의 표본평균

$X_i \sim \text{Exp}(\lambda)$ 이고 $\mu = 1/\lambda$ 라고 하자. 큰수의 약법칙은 $\bar{X}_n$ 이 $1/\lambda$ 로 확률수렴한다고 말한다.

수렴이 얼마나 빠른지는 체비쇼프 부등식으로 셈할 수 있다.

$$P\!\left(\left|\bar{X}_n - \frac{1}{\lambda}\right| \geq \varepsilon\right) \leq \frac{\text{Var}(\bar{X}_n)}{\varepsilon^2} = \frac{1}{n\lambda^2\varepsilon^2}$$

이를테면 $\lambda = 1$, $\varepsilon = 0.1$ 이면 경계가 $\frac{100}{n}$ 이므로 $n \geq 10000$ 이면 이 확률이 1% 이하임이 보장된다.

## 예: 원주율 어림하기

$\pi$ 의 **몬테카를로 어림**을 생각해 보자. $(U_i, V_i) \sim \text{Uniform}([0,1]^2)$ 을 i.i.d. 로 만들고 $X_i = \mathbf{1}(U_i^2 + V_i^2 \leq 1)$ 로 두자. 그러면 $\mu = E[X_i] = \pi/4$ 이고 다음이 성립한다.

$$\hat{\pi}_n = 4\bar{X}_n \xrightarrow{p} \pi$$

## 수렴 속도: 체비쇼프와 중심극한정리

체비쇼프 부등식은 **다항식** 꼴의 경계를 준다. 곧 $P(|\bar{X}_n - \mu| \geq \varepsilon) \leq \frac{\sigma^2}{n\varepsilon^2}$ 이다.

중심극한정리는 **더 날카로운 점근적** 표현을 준다.

$$P\!\left(\left|\bar{X}_n - \mu\right| \geq \varepsilon\right) \approx 2\left(1 - \mathcal{N}\!\left(\frac{\varepsilon\sqrt{n}}{\sigma}\right)\right)$$

이 값은 $n$ 에 대하여 **지수적으로** 줄어들어 체비쇼프의 다항식 경계보다 훨씬 빠르다.

## 큰수의 약법칙이 성립하지 않는 경우

!!! warning "평균이 유한하지 않으면 약법칙도 없다"
    $E[|X|] = \infty$ 이면 큰수의 약법칙은 성립하지 않을 수 있다. 대표적인 예가 **코시분포**이다.

$X_1, X_2, \ldots$ 가 i.i.d. $\text{Cauchy}(0, 1)$ 이면 모든 $n$ 에 대하여 $\bar{X}_n$ 도 **똑같은** Cauchy(0,1) 분포를 따른다. 표본평균은 어떤 값으로도 수렴하지 않는다.

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(16, 5))
np.random.seed(42)

# --- 그림 1: 여러 분포에 대한 큰수의 약법칙 수렴 ---
n_max = 5000
ns = np.arange(1, n_max + 1)

# 지수분포
exp_samples = np.random.exponential(1, n_max)
exp_means = np.cumsum(exp_samples) / ns

# 베르누이분포
bern_samples = np.random.binomial(1, 0.3, n_max)
bern_means = np.cumsum(bern_samples) / ns

# 균등분포
unif_samples = np.random.uniform(0, 1, n_max)
unif_means = np.cumsum(unif_samples) / ns

axes[0].plot(ns, exp_means, alpha=0.7, lw=0.8, label='Exp(1), μ=1')
axes[0].plot(ns, bern_means, alpha=0.7, lw=0.8, label='Bern(0.3), μ=0.3')
axes[0].plot(ns, unif_means, alpha=0.7, lw=0.8, label='U(0,1), μ=0.5')
axes[0].axhline(1, color='blue', ls='--', alpha=0.3)
axes[0].axhline(0.3, color='orange', ls='--', alpha=0.3)
axes[0].axhline(0.5, color='green', ls='--', alpha=0.3)
axes[0].set_title('WLLN: Sample Mean Convergence')
axes[0].set_xlabel('n')
axes[0].set_ylabel('$\\bar{X}_n$')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# --- 그림 2: 체비쇼프 경계와 실제 확률 ---
sigma = 1.0  # Exp(1)
mu = 1.0
eps_values = [0.1, 0.2, 0.5]
n_range = np.arange(10, 2001, 10)
n_sim = 10000

for eps in eps_values:
    chebyshev_bound = sigma**2 / (n_range * eps**2)
    chebyshev_bound = np.minimum(chebyshev_bound, 1)

    actual_probs = []
    for n in n_range:
        samples = np.random.exponential(1, (n_sim, n))
        means = samples.mean(axis=1)
        actual_probs.append(np.mean(np.abs(means - mu) >= eps))

    axes[1].plot(n_range, chebyshev_bound, '--', lw=2,
                 label=f'Chebyshev ε={eps}')
    axes[1].plot(n_range, actual_probs, '-', lw=1, alpha=0.7,
                 label=f'Actual ε={eps}')

axes[1].set_title('Chebyshev Bound vs Actual P(|X̄-μ|≥ε)')
axes[1].set_xlabel('n')
axes[1].set_ylabel('Probability')
axes[1].set_yscale('log')
axes[1].legend(fontsize=7, ncol=2)
axes[1].grid(True, alpha=0.3)

# --- 그림 3: 코시분포 — 약법칙이 성립하지 않는다 ---
cauchy_samples = np.random.standard_cauchy(n_max)
cauchy_means = np.cumsum(cauchy_samples) / ns

normal_samples = np.random.normal(0, 1, n_max)
normal_means = np.cumsum(normal_samples) / ns

axes[2].plot(ns, cauchy_means, alpha=0.7, lw=0.8, color='red',
             label='Cauchy (no convergence)')
axes[2].plot(ns, normal_means, alpha=0.7, lw=0.8, color='blue',
             label='N(0,1) → 0')
axes[2].axhline(0, color='black', ls='--', alpha=0.3)
axes[2].set_title('WLLN Fails for Cauchy')
axes[2].set_xlabel('n')
axes[2].set_ylabel('$\\bar{X}_n$')
axes[2].set_ylim(-5, 5)
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('wlln_examples.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 연습문제

**연습문제 1.**
$X_1, X_2, \ldots$ 가 i.i.d. $\text{Uniform}(0, 1)$ 이라고 하자. $\frac{1}{n}\sum_{i=1}^n X_i^2 \xrightarrow{p} 1/3$ 임을 보여라.

*힌트: $g(X_i) = X_i^2$ 에 큰수의 약법칙을 적용하여라.*

??? success "연습문제 1 풀이"
    요령은 $X_i$ 가 아니라 **새 확률변수** $Y_i = X_i^2$ 을 놓고 거기에 약법칙을 쓰는 것이다.

    **1단계: 새 수열이 가정을 만족하는지 확인한다.** $Y_i = X_i^2$ 으로 두자. $X_1, X_2, \ldots$ 가 i.i.d. 이면 그 각각에 같은 함수 $g(x) = x^2$ 을 씌운 $Y_1, Y_2, \ldots$ 도 i.i.d. 이다. $Y_i$ 는 $X_i$ 하나에만 기대므로 독립성이 그대로 이어지고, $X_i$ 들이 같은 분포를 따르므로 $Y_i$ 들도 같은 분포를 따른다.

    **2단계: $Y_i$ 의 평균을 구한다.** $X \sim \text{Uniform}(0,1)$ 의 확률밀도함수는 $[0,1]$ 위에서 $f(x) = 1$ 이므로, 무의식적 통계학자의 법칙(LOTUS)을 쓰면 다음과 같다.

    $$
    \mathbb{E}[Y_i] = \mathbb{E}[X_i^2] = \int_0^1 x^2 \cdot 1\, dx = \left[\frac{x^3}{3}\right]_0^1 = \frac{1}{3}
    $$

    이것이 목표로 하는 극한값이다.

    **3단계: $Y_i$ 의 분산이 유한함을 확인한다.** 4차 적률을 셈한다.

    $$
    \mathbb{E}[Y_i^2] = \mathbb{E}[X_i^4] = \int_0^1 x^4\, dx = \frac{1}{5}
    $$

    그러므로 분산은 다음과 같다.

    $$
    \text{Var}(Y_i) = \mathbb{E}[X_i^4] - \left(\mathbb{E}[X_i^2]\right)^2 = \frac{1}{5} - \frac{1}{9} = \frac{9 - 5}{45} = \frac{4}{45} < \infty
    $$

    유한하므로 체비쇼프 판 약법칙을 쓸 수 있다. (사실 $0 \leq X_i \leq 1$ 이므로 $0 \leq Y_i \leq 1$ 이고, 유계인 확률변수는 모든 적률이 유한하다.)

    **4단계: 약법칙을 적용한다.** $\bar{Y}_n = \frac{1}{n}\sum_{i=1}^n X_i^2$ 으로 두면 $\mathbb{E}\bar{Y}_n = 1/3$ 이고 $\text{Var}(\bar{Y}_n) = \frac{4}{45n}$ 이다. 체비쇼프 부등식에서 임의의 $\varepsilon > 0$ 에 대하여 다음을 얻는다.

    $$
    P\left(\left|\frac{1}{n}\sum_{i=1}^n X_i^2 - \frac{1}{3}\right| \geq \varepsilon\right) \leq \frac{\text{Var}(\bar{Y}_n)}{\varepsilon^2} = \frac{4}{45 n \varepsilon^2} \longrightarrow 0
    $$

    따라서 다음이 성립한다.

    $$
    \frac{1}{n}\sum_{i=1}^n X_i^2 \xrightarrow{p} \frac{1}{3}
    $$

    **덧붙임: 왜 이 요령이 늘 통하는가.** 이 페이지 첫머리의 일반형 약법칙이 말하듯, $\mathbb{E}|g(X_i)| < \infty$ 이기만 하면 어떤 함수 $g$ 에 대해서도 다음이 성립한다.

    $$
    \frac{1}{n}\sum_{i=1}^n g(X_i) \xrightarrow{p} \mathbb{E}[g(X_1)]
    $$

    $g$ 를 씌워도 i.i.d. 성질이 보존되기 때문이다. 이 사실이 몬테카를로 방법 전체를 떠받친다. 적분 $\int_0^1 g(x)\,dx$ 를 알고 싶으면 $U(0,1)$ 에서 표본을 뽑아 $g$ 값의 평균을 내면 된다.

    표본분산이 참분산으로 수렴한다는 것도 같은 요령의 결과이다. $g(x) = x^2$ 과 $g(x) = x$ 에 각각 약법칙을 쓰면 다음을 얻는다.

    $$
    \frac{1}{n}\sum_{i=1}^n X_i^2 - \left(\frac{1}{n}\sum_{i=1}^n X_i\right)^2 \xrightarrow{p} \frac{1}{3} - \left(\frac{1}{2}\right)^2 = \frac{1}{12} = \text{Var}(X_1)
    $$

    이는 $U(0,1)$ 의 분산 $1/12$ 과 정확히 맞아떨어진다. $\square$

---

**연습문제 2.**
$X_1, X_2, \ldots$ 가 독립이지만 같은 분포를 따르지는 않고, 모든 $i$ 에 대하여 $E[X_i] = \mu$ 이며 어떤 상수 $C$ 에 대하여 $\text{Var}(X_i) \leq C$ 라고 하자. 이때에도 큰수의 약법칙 $\bar{X}_n \xrightarrow{p} \mu$ 가 성립함을 증명하여라.

??? success "연습문제 2 풀이"
    체비쇼프를 쓰는 증명을 다시 들여다보면, 같은 분포를 따른다는 가정이 실제로 쓰인 곳이 한 군데도 없음을 알 수 있다. 필요한 것은 **평균이 모두 같다**는 것과 **분산이 고르게 눌려 있다**는 것뿐이다.

    **1단계: 표본평균의 평균을 구한다.** 기댓값의 선형성은 독립성조차 요구하지 않는다. 모든 $i$ 에 대하여 $\mathbb{E}[X_i] = \mu$ 이므로 다음과 같다.

    $$
    \mathbb{E}[\bar{X}_n] = \frac{1}{n}\sum_{i=1}^n \mathbb{E}[X_i] = \frac{1}{n} \cdot n\mu = \mu
    $$

    평균이 모두 **같은 값** $\mu$ 라는 점이 여기에서 결정적이다. 만약 $\mathbb{E}[X_i] = \mu_i$ 로 저마다 달랐다면 표본평균의 평균은 $\bar{\mu}_n = \frac{1}{n}\sum_i \mu_i$ 가 되고, 결론도 그 값으로 바뀐다.

    **2단계: 표본평균의 분산을 누른다.** $X_1, \ldots, X_n$ 이 **독립**이므로 공분산 항이 모두 사라지고 분산이 그대로 더해진다.

    $$
    \text{Var}(\bar{X}_n) = \text{Var}\left(\frac{1}{n}\sum_{i=1}^n X_i\right) = \frac{1}{n^2}\sum_{i=1}^n \text{Var}(X_i)
    $$

    이제 가정 $\text{Var}(X_i) \leq C$ 를 항마다 쓴다.

    $$
    \text{Var}(\bar{X}_n) \leq \frac{1}{n^2}\sum_{i=1}^n C = \frac{nC}{n^2} = \frac{C}{n}
    $$

    **3단계: 체비쇼프 부등식을 적용한다.** $\varepsilon > 0$ 을 아무렇게나 고정한다. 1단계에서 $\bar{X}_n$ 의 평균이 $\mu$ 이므로 다음이 성립한다.

    $$
    P\left(\left|\bar{X}_n - \mu\right| \geq \varepsilon\right) \leq \frac{\text{Var}(\bar{X}_n)}{\varepsilon^2} \leq \frac{C}{n\varepsilon^2} \longrightarrow 0 \qquad (n \to \infty)
    $$

    $C$ 와 $\varepsilon$ 은 $n$ 에 기대지 않는 고정된 값이므로 오른쪽은 $0$ 으로 간다. 따라서 $\bar{X}_n \xrightarrow{p} \mu$ 이다. $\square$

    **가정을 하나씩 따져 보기.** 무엇이 없어도 되고 무엇이 꼭 필요한지 정리해 두자.

    | 가정 | 꼭 필요한가 | 어디에 쓰였나 |
    |---|---|---|
    | 같은 분포 | **필요 없다** | 아무 데도 쓰이지 않았다 |
    | 평균이 모두 $\mu$ | 필요하다 | 1단계 |
    | 독립 | 약하게 필요하다 | 2단계(무상관이면 충분하다) |
    | 분산이 $C$ 로 눌림 | 필요하다 | 2단계 |

    - **독립은 무상관으로 약화할 수 있다.** 2단계에서 실제로 쓴 것은 $i \neq j$ 일 때 $\text{Cov}(X_i, X_j) = 0$ 이라는 사실뿐이다. 독립은 무상관을 함의하지만 그 역은 아니므로, 이 정리는 무상관인 수열로 그대로 확장된다.
    - **고른 상계 $C$ 가 없으면 무너질 수 있다.** 이를테면 $\text{Var}(X_i) = i^2$ 이라면 다음과 같이 되어 $0$ 으로 가지 않는다.

    $$
    \text{Var}(\bar{X}_n) = \frac{1}{n^2}\sum_{i=1}^n i^2 = \frac{(n+1)(2n+1)}{6n} \longrightarrow \infty
    $$

    - 사실 필요한 것은 상계 $C$ 보다 더 약한 조건이다. $\frac{1}{n^2}\sum_{i=1}^n \text{Var}(X_i) \to 0$ 이기만 하면 같은 증명이 그대로 통한다. 분산이 $\text{Var}(X_i) = i$ 처럼 자라더라도 $\frac{1}{n^2}\cdot\frac{n(n+1)}{2} \to \infty$ 는 아니고 $\frac{n+1}{2n} \to \frac{1}{2}$ 로 머무니 이 조건이 깨지지만, $\text{Var}(X_i) = \sqrt{i}$ 처럼 더 느리게 자라면 $\frac{1}{n^2}\sum \sqrt{i} \approx \frac{2}{3\sqrt{n}} \to 0$ 이므로 약법칙이 성립한다.
