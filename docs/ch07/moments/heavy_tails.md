# 두꺼운 꼬리와 적률 문제

## 초과첨도

**초과첨도**는 $\gamma_2 = \kappa_4 - 3$ 으로 정의한다. 여기서 $\kappa_4 = E[(X - \mu)^4] / \sigma^4$ 는 (그냥) 첨도이다. 3을 빼는 것은 $\kappa_4 = 3$ 인 정규분포를 기준으로 삼아 눈금을 맞추기 위해서이다.

!!! info "초과첨도 읽는 법"
    | $\gamma_2$ | 종류 | 꼬리 | 예 |
    |:---:|:---:|:---:|:---:|
    | $\gamma_2 > 0$ | 급첨 | 정규분포보다 무겁다 | $t$분포, 라플라스분포 |
    | $\gamma_2 = 0$ | 중첨 | 정규분포와 비슷하다 | 정규분포 |
    | $\gamma_2 < 0$ | 평첨 | 정규분포보다 가볍다 | 균등분포, 대칭인 베타분포 |

**흔한 오해:** 첨도를 "봉우리가 뾰족한 정도"를 재는 값이라고 설명하는 일이 잦지만, 더 정확히는 **꼬리의 무게**, 곧 중심에서 멀리 떨어진 곳에 확률질량이 얼마나 놓여 있는지를 재는 값이다.

## 자주 쓰는 분포의 초과첨도

| 분포 | 초과첨도 $\gamma_2$ |
|:---|:---:|
| $\text{Uniform}(a, b)$ | $-6/5$ |
| $\text{Normal}$ | $0$ |
| $\text{Exponential}(\lambda)$ | $6$ |
| $\text{Laplace}(0, b)$ | $3$ |
| $t(\nu)$, $\nu > 4$ | $6/(\nu - 4)$ |
| $\text{Beta}(\alpha, \alpha)$ | $-6/(2\alpha + 3)$ |
| $\text{Bernoulli}(p)$ | $(1 - 6p(1-p))/(p(1-p))$ |

## 적률 문제

!!! info "적률 문제"
    **물음:** $k = 1, 2, 3, \ldots$ 에 대한 적률의 수열 $\mu_k = E[X^k]$ 가 $X$ 의 분포를 유일하게 결정하는가?

    **답:** 언제나 그런 것은 아니다. 적률이 분포를 유일하게 가려내면 그 분포를 **적률결정적**이라 하고, 그렇지 않으면 **적률비결정적**이라 한다.

**유일성을 보장하는 충분조건:**

1. **칼레만 조건.** $\sum_{k=1}^{\infty} (E[|X|^{2k}])^{-1/(2k)} = \infty$ 이면 그 분포는 적률로 결정된다.
2. **적률생성함수가 0의 어떤 근방에서 존재한다.** 이 조건이면 칼레만 조건이 따라 나온다.

**로그정규분포라는 반례.** 로그정규분포는 **적률비결정적**인 분포의 고전적인 예이다. 다음 밀도함수의 족을 보자.

$$f_a(x) = f_0(x)\left[1 + a\sin(2\pi\ln x)\right], \quad -1 \leq a \leq 1$$

여기서 $f_0$ 는 표준 로그정규 확률밀도함수이다. 이들은 서로 다른 분포이면서도 **적률이 모두 같다**.

## 표준화적률

$k$ 차 **표준화적률**은 다음과 같다.

$$\tilde{\mu}_k = E\!\left[\left(\frac{X - \mu}{\sigma}\right)^k\right]$$

- $\tilde{\mu}_1 = 0$, $\tilde{\mu}_2 = 1$, $\tilde{\mu}_3 = \gamma_1$ (왜도), $\tilde{\mu}_4 = \kappa_4$ (첨도)

대칭인 분포에서는 홀수 차수의 표준화적률이 모두 0이다.

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

x = np.linspace(-6, 6, 1000)

# --- 패널 1: 첨도 비교 ---
dists = [
    ('Uniform', stats.uniform(-np.sqrt(3), 2*np.sqrt(3)), -1.2),
    ('Normal', stats.norm(), 0),
    ('Laplace', stats.laplace(), 3),
    ('t(5)', stats.t(5), 6),
]
colors = ['green', 'blue', 'orange', 'red']

for (name, dist, kurt), color in zip(dists, colors):
    axes[0].plot(x, dist.pdf(x), color=color, lw=2,
                 label=f'{name} (γ₂={kurt})')

axes[0].set_title('Distributions with Different Kurtosis')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].legend(fontsize=9)
axes[0].grid(True, alpha=0.3)

# --- 패널 2: 4제곱이 꼬리에 주는 가중치 ---
np.random.seed(42)
z = np.sort(np.abs(np.random.normal(0, 1, 10000)))
contrib = z**4
cum_frac = np.cumsum(contrib[::-1]) / contrib.sum()
pct = np.linspace(0, 100, len(z))

axes[1].plot(pct, cum_frac, 'b-', lw=2)
axes[1].axhline(0.5, color='red', ls='--', alpha=0.5)
axes[1].set_title('Cumulative 4th Moment from Largest |z|')
axes[1].set_xlabel('Top percentile of |z| values')
axes[1].set_ylabel('Fraction of total E[Z⁴]')
axes[1].grid(True, alpha=0.3)

# --- 패널 3: 로그정규분포의 적률비결정성 ---
x_ln = np.linspace(0.01, 5, 500)
f0 = stats.lognorm.pdf(x_ln, s=1, scale=1)

for a in [-0.8, 0, 0.8]:
    f_a = f0 * (1 + a * np.sin(2 * np.pi * np.log(x_ln)))
    label = f'a={a}' if a != 0 else 'LogNormal (a=0)'
    axes[2].plot(x_ln, f_a, lw=2, label=label)

axes[2].set_title('Same Moments, Different Distributions')
axes[2].set_xlabel('x')
axes[2].set_ylabel('f(x)')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('heavy_tails_moment_problem.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 연습문제

**연습문제 1.** $\text{Exponential}(\lambda)$ 분포의 초과첨도를 정의에서 곧바로 구하여라.

??? success "연습문제 1 풀이"
    $X \sim \text{Exp}(\lambda)$ 에 대하여 $\mu = 1/\lambda$, $\sigma^2 = 1/\lambda^2$ 이다. 4차 중심적률은 다음과 같다.

    $$
    E[(X - \mu)^4] = E[X^4] - 4\mu E[X^3] + 6\mu^2 E[X^2] - 3\mu^4
    $$

    $E[X^k] = k!/\lambda^k$ 를 쓰면 $E[X^2] = 2/\lambda^2$, $E[X^3] = 6/\lambda^3$, $E[X^4] = 24/\lambda^4$ 이다.

    $$
    E[(X-\mu)^4] = \frac{24}{\lambda^4} - \frac{4}{\lambda}\cdot\frac{6}{\lambda^3} + \frac{6}{\lambda^2}\cdot\frac{2}{\lambda^2} - \frac{3}{\lambda^4} = \frac{24 - 24 + 12 - 3}{\lambda^4} = \frac{9}{\lambda^4}
    $$

    첨도 $= 9/\lambda^4 \div (1/\lambda^4) = 9$ 이다. 초과첨도 $= 9 - 3 = 6$ 이다.

---

**연습문제 2.** $\text{Uniform}(a,b)$ 분포의 초과첨도를 구하여 이 분포가 평첨임을 보여라.

??? success "연습문제 2 풀이"
    일반성을 잃지 않고 $a = 0$, $b = 1$ 이라 하자. 그러면 $\mu = 1/2$, $\sigma^2 = 1/12$ 이다.

    $$
    E[(X - 1/2)^4] = \int_0^1 (x - 1/2)^4\,dx = \frac{1}{80}
    $$

    첨도 $= \frac{1/80}{(1/12)^2} = \frac{1/80}{1/144} = \frac{144}{80} = \frac{9}{5} = 1.8$ 이다.

    초과첨도 $= 1.8 - 3 = -1.2 < 0$ 이다. 따라서 균등분포가 평첨임이 확인된다.

---

**연습문제 3.** 자유도가 $\nu$ 인 $t$분포의 초과첨도는 $\nu > 4$ 일 때 $6/(\nu - 4)$ 이다. $\nu \to \infty$ 이면 어떻게 되는가? 이것은 $t$분포와 정규분포의 관계에 대하여 무엇을 말해 주는가?

??? success "연습문제 3 풀이"
    $\nu \to \infty$ 이면 $6/(\nu - 4) \to 0$ 이므로 초과첨도가 0에 가까워진다(중첨). 이는 $\nu \to \infty$ 일 때 $t_\nu \to N(0,1)$ 이라는 사실과 들어맞는다. $\nu$ 가 작을 때 $t$분포는 정규분포보다 꼬리가 두껍고, $\nu$ 가 커질수록 꼬리가 정규분포를 닮아 간다.

---

**연습문제 4.** 평균, 분산, 왜도는 같지만 첨도가 다른 두 분포의 예를 들어라.

??? success "연습문제 4 풀이"
    $X \sim N(0, 1)$ (왜도 0, 초과첨도 0)과 분산이 1이 되도록 눈금을 맞춘 $Y \sim \text{Logistic}(0, \sqrt{3}/\pi)$ 를 생각하자. 로지스틱분포는 대칭이므로(왜도 0) 초과첨도가 $6/5 = 1.2$ 이다. 둘 다 평균 0, 분산 1, 왜도 0 이지만 첨도가 다르다. 또는 분산이 1이 되도록 눈금을 맞춘 임의의 대칭인 $t_\nu$ 분포($\nu > 4$)도 왜도가 0 이면서 초과첨도가 $6/(\nu - 4) > 0$ 이다.

---

**연습문제 5.** 로그정규분포는 왜 칼레만 조건을 어기는가? 또 임의의 $t > 0$ 에 대하여 그 적률생성함수가 존재하지 않음을 확인하여라.

??? success "연습문제 5 풀이"
    $X \sim \text{LogNormal}(0, 1)$ 에 대하여 $E[X^k] = e^{k^2/2}$ 이다. 칼레만 조건은 $\sum (E[X^{2k}])^{-1/(2k)} = \sum e^{-k} < \infty$ 가 발산할 것을 요구하는데 이 급수는 수렴한다. 합이 무한이 아니라 유한하므로 칼레만 조건이 **깨지고**, 따라서 적률이 분포를 유일하게 결정하지 못한다.

    적률생성함수를 보자. $Z \sim N(0,1)$ 일 때 $E[e^{tX}] = E[e^{t e^Z}]$ 이다. $t > 0$ 이면 다음과 같다.

    $$
    E[e^{tX}] = \int_{-\infty}^{\infty} e^{te^z} \frac{e^{-z^2/2}}{\sqrt{2\pi}}\,dz = \infty
    $$

    $z \to \infty$ 일 때 $te^z$ 가 $z^2/2$ 보다 빠르게 커지기 때문이다. 그러므로 임의의 $t > 0$ 에 대하여 적률생성함수는 존재하지 않는다.
