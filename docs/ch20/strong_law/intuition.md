# 직관, 보렐–칸텔리, 반복로그 법칙

## 강법칙과 약법칙

!!! info "큰수의 강법칙"
    $X_1, X_2, \ldots$ 가 $E[X_i] = \mu$ 인 i.i.d. 확률변수라고 하자. 그러면 다음이 성립한다.

    $$P\!\left(\lim_{n \to \infty} \bar{X}_n = \mu\right) = 1$$

    곧 $\bar{X}_n \xrightarrow{\text{a.s.}} \mu$ 이다.

약법칙과 갈리는 지점은 다음과 같다.

| | 약법칙 | 강법칙 |
|:---|:---:|:---:|
| **수렴의 뜻** | 확률수렴 | 거의 확실한 수렴 |
| **의미** | 각 $\varepsilon$ 에 대하여 $P(\|\bar{X}_n - \mu\| > \varepsilon) \to 0$ | $P(\bar{X}_n \to \mu) = 1$ |
| **필요한 가정** | 평균이 유한(간단한 증명에는 분산이 유한) | 평균이 유한 |
| **허용하는 것** | 이따금 크게 벗어나는 일 | 크게 벗어나는 일이 유한 번만 |

## 직관으로 보는 차이

약법칙은 이렇게 말한다. "허용오차 $\varepsilon$ 을 어떻게 고정하든, $\bar{X}_n$ 이 $\mu$ 에서 $\varepsilon$ 보다 더 벗어날 확률은 0으로 간다."

강법칙은 이렇게 말한다. "확률 1로 $\bar{X}_n$ 은 **결국** $\mu$ 의 $\varepsilon$ 안에 머물고 (유한 번을 빼면) **다시는 벗어나지 않는다**."

**비유.** 다트를 던지는 사람을 생각해 보자.

- 약법칙: "과녁 한가운데를 둘러싼 어떤 고리를 잡아도 그 밖에 꽂히는 다트의 비율은 0으로 간다." 다만 이따금 엉뚱한 곳으로 날아가는 던지기가 있을 수 있다.
- 강법칙: "어느 $N$ 번째 다트 이후로는 **뒤따르는 모든 다트**가 한가운데에서 $\varepsilon$ 안에 꽂힌다"(확률 1로).

## 보렐–칸텔리를 쓰는 증명 전략

큰수의 강법칙의 증명은 **보렐–칸텔리 보조정리**에 크게 기댄다.

!!! info "제1 보렐–칸텔리 보조정리"
    $\sum_{n=1}^{\infty} P(A_n) < \infty$ 이면 $P(A_n \text{ 이 무한히 자주 일어남}) = 0$ 이다.

    곧 확률 1로 사건 $A_n$ 가운데 **유한 개**만 일어난다.

**큰수의 강법칙에 적용하기.** $A_n = \{|\bar{X}_n - \mu| > \varepsilon\}$ 이라고 하자. $\sum_n P(A_n) < \infty$ 임을 보일 수 있다면, 보렐–칸텔리에 따라 $\bar{X}_n$ 이 $\mu$ 에서 $\varepsilon$ 보다 더 벗어나는 일은 유한 번만 일어나며, 곧 $\bar{X}_n \to \mu$ 가 거의 확실하게 성립한다.

**체비쇼프를 그대로 쓰면 왜 안 되는가?** 체비쇼프는 $P(A_n) \leq \frac{\sigma^2}{n\varepsilon^2}$ 을 주는데 $\sum \frac{1}{n} = \infty$ 이다. 그러니 이 경계는 더할 수 있는 꼴이 아니다.

**요령: 부분수열을 쓴다.** $n_k = k^2$ 을 따라가면 다음이 성립한다.

$$P(|\bar{X}_{k^2} - \mu| > \varepsilon) \leq \frac{\sigma^2}{k^2\varepsilon^2}$$

그리고 $\sum \frac{1}{k^2} < \infty$ 이다. 따라서 $\bar{X}_{k^2} \to \mu$ 가 거의 확실하게 성립한다. 그다음 이웃한 제곱수 $k^2$ 과 $(k+1)^2$ 사이의 $\bar{X}_n$ 이 $\bar{X}_{k^2}$ 에서 크게 벗어날 수 없음을 보이면 증명이 끝난다.

## 약법칙이 강법칙을 함의하는가

**아니다.** 확률수렴하지만 거의 확실하게 수렴하지는 않는 수열이 있다.

**반례(타자기 수열).** 르베그 측도를 준 $\Omega = [0, 1]$ 에서 다음과 같이 정의하자.

$$X_n = \mathbf{1}\!\left[\frac{n - 2^k}{2^k}, \frac{n - 2^k + 1}{2^k}\right) \quad \text{단, } 2^k \leq n < 2^{k+1}$$

이 구간들은 폭을 줄여 가며 $[0, 1]$ 을 돌아다닌다. 그러면 구간의 길이가 $\to 0$ 이므로 $X_n \xrightarrow{p} 0$ 이지만, **모든** $\omega \in [0,1]$ 에 대하여 $X_n(\omega) = 1$ 이 무한히 자주 일어난다. 따라서 $X_n$ 은 0으로 거의 확실하게 수렴하지 **않는다**.

## 특정 분포에 대한 큰수의 강법칙

### 베르누이분포의 강법칙(보렐의 정리)

$X_i \sim \text{Bernoulli}(p)$ 가 i.i.d. 이면 다음이 성립한다.

$$\frac{X_1 + \cdots + X_n}{n} \xrightarrow{\text{a.s.}} p$$

이는 역사적으로 큰수의 강법칙의 첫 번째 형태였다(보렐, 1909). 이 정리는 빈도주의적 해석을 엄밀하게 다듬는다. 곧 성공의 긴 눈으로 본 상대도수가 확률 1로 $p$ 에 수렴한다는 것이다.

### 정규분포의 강법칙

$X_i \sim N(\mu, \sigma^2)$ 가 i.i.d. 이면 $\bar{X}_n \xrightarrow{\text{a.s.}} \mu$ 이다. 더 나아가 그 속도는 **반복로그 법칙**으로 잴 수 있다.

$$\limsup_{n \to \infty} \frac{\bar{X}_n - \mu}{\sigma\sqrt{2\ln\ln n / n}} = 1 \quad \text{a.s.}$$

이는 $\bar{X}_n$ 이 $\mu$ 주위에서 흔들리는 **정확한 테두리**를 알려 준다.

## 반복로그 법칙

!!! info "반복로그 법칙(LIL)"
    $X_i$ 가 $E[X_i] = 0$, $\text{Var}(X_i) = \sigma^2$ 인 i.i.d. 확률변수이면 다음이 성립한다.

    $$\limsup_{n \to \infty} \frac{S_n}{\sigma\sqrt{2n\ln\ln n}} = 1 \quad \text{a.s.}$$

    $$\liminf_{n \to \infty} \frac{S_n}{\sigma\sqrt{2n\ln\ln n}} = -1 \quad \text{a.s.}$$

반복로그 법칙은 중심극한정리($S_n / \sqrt{n}$ 이 대략 표준정규분포를 따른다고 말한다)와 큰수의 강법칙($S_n / n \to 0$ 이라고 말한다) 사이에 자리한다. 이 법칙은 확률보행 $S_n$ 의 **정확한 테두리**를 알려 준다. 곧 $S_n$ 은 $\pm\sqrt{2n\ln\ln n}$ 만큼 무한히 자주 자라지만 그보다 더 빠르게 자라지는 않는다.

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(16, 5))
np.random.seed(42)

# --- 그림 1: 강법칙과 약법칙을 눈으로 보기 ---
n_max = 10000
ns = np.arange(1, n_max + 1)
eps = 0.05

# 여러 줄기
n_paths = 20
for i in range(n_paths):
    samples = np.random.exponential(1, n_max)
    means = np.cumsum(samples) / ns
    axes[0].plot(ns, means, alpha=0.3, lw=0.5, color='steelblue')

axes[0].axhline(1, color='red', ls='-', lw=2, label='μ = 1')
axes[0].axhline(1 + eps, color='red', ls='--', alpha=0.5)
axes[0].axhline(1 - eps, color='red', ls='--', alpha=0.5)
axes[0].set_title('SLLN: All paths converge to μ')
axes[0].set_xlabel('n')
axes[0].set_ylabel('$\\bar{X}_n$')
axes[0].set_ylim(0.8, 1.2)
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# --- 그림 2: 반복로그 법칙 ---
n_lil = 100000
samples = np.random.normal(0, 1, n_lil)
S_n = np.cumsum(samples)
ns_lil = np.arange(1, n_lil + 1)

# 반복로그 법칙의 테두리
with np.errstate(divide='ignore', invalid='ignore'):
    envelope = np.sqrt(2 * ns_lil * np.log(np.log(ns_lil)))
    envelope[:3] = np.nan  # log(log(1)) 문제를 피한다

axes[1].plot(ns_lil, S_n, alpha=0.5, lw=0.3, color='steelblue',
             label='$S_n$')
axes[1].plot(ns_lil, envelope, 'r-', lw=1.5, alpha=0.7,
             label='$\\sqrt{2n\\ln\\ln n}$')
axes[1].plot(ns_lil, -envelope, 'r-', lw=1.5, alpha=0.7)
axes[1].fill_between(ns_lil, -envelope, envelope, alpha=0.1, color='red')
axes[1].set_title('Law of the Iterated Logarithm')
axes[1].set_xlabel('n')
axes[1].set_ylabel('$S_n$')
axes[1].legend(fontsize=9)
axes[1].grid(True, alpha=0.3)

# --- 그림 3: 보렐–칸텔리 보여 주기 ---
# ε 를 키워 가며 |X̄_n - μ| > ε 가 몇 번 일어나는지 센다
n_bc = 5000
samples = np.random.normal(0, 1, n_bc)
means = np.cumsum(samples) / np.arange(1, n_bc + 1)

epsilons = [0.5, 0.2, 0.1, 0.05]
for eps in epsilons:
    violations = np.abs(means) > eps
    cum_violations = np.cumsum(violations)
    axes[2].plot(np.arange(1, n_bc + 1), cum_violations, lw=1.5,
                 label=f'ε={eps}: {int(cum_violations[-1])} violations')

axes[2].set_title('Cumulative Violations |X̄ₙ - μ| > ε')
axes[2].set_xlabel('n')
axes[2].set_ylabel('Count of violations so far')
axes[2].legend(fontsize=8)
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('slln_intuition.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 연습문제

**연습문제 1.**
동전 던지기로 약법칙과 강법칙을 견주어 보이는 그림에서, 한 줄기가 수렴하는 그림과 여러 실험의 히스토그램이 몰리는 그림 가운데 어느 것이 어느 법칙에 해당하는지, 그 까닭과 함께 설명하여라.

??? success "연습문제 1 풀이"
    **답:** 한 줄기가 수렴하는 그림은 **강법칙**을, 여러 실험의 히스토그램이 몰리는 그림은 **약법칙**을 나타낸다.

    **1단계: 두 정의가 무엇을 재는지 본다.** 공정한 동전을 던져 앞면이면 $1$, 뒷면이면 $0$ 인 $X_i \sim \text{Bernoulli}(0.5)$ 를 만들고 $\bar{X}_n$ 을 $n$ 번째까지의 앞면 비율이라고 하자.

    $$
    \text{강법칙:}\quad P\!\left(\lim_{n \to \infty} \bar{X}_n = 0.5\right) = 1
    $$

    $$
    \text{약법칙:}\quad \text{각 } \varepsilon > 0 \text{ 에 대하여} \quad P\!\left(\left|\bar{X}_n - 0.5\right| > \varepsilon\right) \to 0
    $$

    강법칙 쪽 식의 확률 안에는 **$n$ 이 없다**. 확률변수 하나에 대한 서술이 아니라 **수열 전체**, 곧 표본경로 $\big(\bar{X}_1(\omega), \bar{X}_2(\omega), \ldots\big)$ 하나에 대한 서술이다. 반면 약법칙 쪽 식은 각 $n$ 마다 따로 잰 확률들의 수열이 $0$ 으로 간다는 서술이다.

    **2단계: 한 줄기 그림 = 강법칙.** 왼쪽 그림은 동전을 계속 던지면서 그때까지의 비율을 $n$ 에 대하여 이어 그린 것이다. 이것은 **$\omega$ 를 하나 뽑아 그 경로 전체를 따라간 그림**이다. 이 곡선이 $0.5$ 로 가라앉는 모습은 곧 $\bar{X}_n(\omega) \to 0.5$ 를 눈으로 본 것이며, 강법칙은 이런 일이 확률 $1$ 로, 곧 **거의 모든 경로에서** 일어난다고 말한다. 여러 줄기를 겹쳐 그려 모두가 $0.5$ 로 모이는 모습을 보이면 "확률 1"이라는 대목까지 드러난다.

    **3단계: 히스토그램 그림 = 약법칙.** 오른쪽 그림은 성격이 전혀 다르다. $n$ 을 **고정해** 두고 "동전을 $n$ 번 던져 비율을 적는" 실험을 수천 번 되풀이한 뒤, 얻은 값들의 히스토그램을 그린 것이다. 이 히스토그램은 확률변수 $\bar{X}_n$ **하나의 분포**를 그린 것이다. $n$ 을 키울수록 히스토그램이 $0.5$ 둘레로 좁아지는 모습은 곧 다음을 눈으로 본 것이다.

    $$
    P\!\left(\left|\bar{X}_n - 0.5\right| > \varepsilon\right) = (\text{히스토그램에서 } 0.5 \pm \varepsilon \text{ 밖에 놓인 비율}) \to 0
    $$

    이것이 바로 확률수렴, 곧 약법칙이다.

    **4단계: 왜 히스토그램으로는 강법칙을 볼 수 없는가.** 이 대목이 문제의 핵심이다. 히스토그램은 각 $n$ 에서 분포의 **옆모습**만 보여 줄 뿐, 서로 다른 $n$ 의 값들이 **같은 경로에서 나온 것인지**를 알려 주지 못한다. 그런데 강법칙은 정확히 그 정보를 요구한다. "이 경로가 어느 시점 이후로 $0.5$ 가까이에 눌러앉는가"를 물으려면 $\bar{X}_1, \bar{X}_2, \ldots$ 를 한 줄로 이어 보아야 한다.

    실제로 이 페이지에 나온 **타자기 수열**이 그 차이를 똑똑히 보여 준다. 그 수열은 각 $n$ 의 히스토그램만 보면 $0$ 에 완벽하게 몰려 가지만(확률수렴), 경로를 하나 붙잡고 따라가면 값 $1$ 이 무한히 자주 튀어나와 끝내 수렴하지 않는다. 히스토그램만으로는 이 두 상황을 구별할 수 없다.

    **5단계: 정리.**

    | 그림 | 무엇을 고정하고 무엇을 움직이나 | 무엇을 그리나 | 어느 법칙 |
    |---|---|---|---|
    | 한 줄기(또는 여러 줄기) | 경로 $\omega$ 를 고정, $n$ 을 키움 | 표본경로 $n \mapsto \bar{X}_n(\omega)$ | 강법칙(거의 확실한 수렴) |
    | 히스토그램 | $n$ 을 고정, 실험을 되풀이 | 확률변수 $\bar{X}_n$ 의 분포 | 약법칙(확률수렴) |

    한마디로, **세로로 보면 약법칙이고 가로로 보면 강법칙이다**. 히스토그램은 시간을 한 순간에 세워 놓고 여러 세계를 견주고, 한 줄기 그림은 한 세계 안에서 시간을 따라 걷는다. $\square$
