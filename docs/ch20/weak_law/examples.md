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

---

**연습문제 2.**
$X_1, X_2, \ldots$ 가 독립이지만 같은 분포를 따르지는 않고, 모든 $i$ 에 대하여 $E[X_i] = \mu$ 이며 어떤 상수 $C$ 에 대하여 $\text{Var}(X_i) \leq C$ 라고 하자. 이때에도 큰수의 약법칙 $\bar{X}_n \xrightarrow{p} \mu$ 가 성립함을 증명하여라.
