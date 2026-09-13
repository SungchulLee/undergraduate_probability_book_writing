# 베이즈 통계에서의 응용

## 확률 위의 분포로서의 베타분포

베타분포는 $(0, 1)$ 위에서 정의되므로 **확률**, **비율**, **발생률**을 나타내는 모형으로 딱 알맞다. 베이즈 추론에서는 알려지지 않은 확률 $p$ 를 확률변수로 보고 여기에 베타분포를 사전분포로 준다.

## 예: 품질 관리

어떤 공장이 만드는 제품은 불량이거나 불량이 아니다. 참 불량률 $p$ 는 알려져 있지 않다.

**문제 설정:**

- **사전믿음:** 자료를 보기 전에 $p$ 가 5% 언저리라고 믿지만 그리 확신하지는 못한다. 그래서 $p \sim \text{Beta}(2, 38)$ 을 고르는데, 이 분포의 평균은 $\frac{2}{40} = 0.05$ 이고 어느 정도 모여 있다.
- **자료:** 제품 $n = 100$ 개를 검사하여 불량품 $k = 8$ 개를 찾았다.
- **사후분포:** $p \mid X = 8 \sim \text{Beta}(2 + 8, 38 + 92) = \text{Beta}(10, 130)$

사후평균은 $\frac{10}{140} \approx 0.071$ 이며, 사전평균(0.05)과 최대가능도추정값($\frac{8}{100} = 0.08$) 사이에 놓인다.

## 예: A/B 검정

어떤 온라인 서비스가 웹페이지 두 판을 견주어 본다. A판에 대해서는 다음과 같다.

- **사전분포:** $p_A \sim \text{Beta}(1, 1) = \text{Uniform}(0, 1)$ (정보를 담지 않은 사전분포)
- **자료:** 방문자 200명 가운데 50명이 전환했다
- **사후분포:** $p_A \mid \text{자료} \sim \text{Beta}(51, 151)$

B판에 대해서는 다음과 같다.

- **사전분포:** $p_B \sim \text{Beta}(1, 1)$
- **자료:** 방문자 200명 가운데 65명이 전환했다
- **사후분포:** $p_B \mid \text{자료} \sim \text{Beta}(66, 136)$

B가 A보다 나을 확률은 모의실험으로 어림할 수 있다.

$$P(p_B > p_A \mid \text{자료}) \approx \frac{1}{N}\sum_{i=1}^{N} \mathbf{1}(p_B^{(i)} > p_A^{(i)})$$

여기서 $p_A^{(i)}$ 와 $p_B^{(i)}$ 는 각각의 사후분포에서 독립적으로 뽑은 값이다.

## 신용구간

**신용구간**은 신뢰구간에 대응하는 베이즈판이다. **최고사후밀도(HPD)** 구간은 주어진 확률을 담는 가장 짧은 구간이다.

베타분포에 대하여 수준 $1 - \alpha$ 의 **양쪽 꼬리가 같은 신용구간**은 다음과 같다.

$$\left[F^{-1}\!\left(\frac{\alpha}{2}\right),\; F^{-1}\!\left(1 - \frac{\alpha}{2}\right)\right]$$

여기서 $F^{-1}$ 은 베타분포의 분위수함수이다.

## 차례대로 갱신하기

베타-이항 켤레 모형의 큰 장점은 자료를 **차례대로** 받아들일 수 있다는 것이다. 관측값을 하나씩 처리하든 묶음으로 처리하든 같은 사후분포가 나온다.

!!! info "차례대로 갱신하기"
    $\text{Beta}(\alpha_0, \beta_0)$ 에서 시작하면 다음과 같다.

    - 성공을 하나 관찰한 뒤: $\text{Beta}(\alpha_0 + 1, \beta_0)$
    - 실패를 하나 관찰한 뒤: $\text{Beta}(\alpha_0, \beta_0 + 1)$

    성공 $k$ 번과 실패 $n - k$ 번을 (어떤 순서로든) 관찰한 뒤에는 다음과 같다.

    $$\text{Beta}(\alpha_0 + k,\; \beta_0 + n - k)$$

관측의 순서는 상관이 없고 오직 횟수의 합만이 중요하다.

## 예측분포

사전분포가 $\text{Beta}(\alpha, \beta)$ 일 때 $n$ 번의 시행에서 성공 $k$ 번을 관찰했다면, 다음 시행에서 성공할 **사후예측확률**은 다음과 같다.

$$P(X_{n+1} = 1 \mid \text{자료}) = E[p \mid \text{자료}] = \frac{\alpha + k}{\alpha + \beta + n}$$

$\alpha = \beta = 1$ (균등한 사전분포)이면 이것은 **라플라스의 이어짐 규칙**이 된다.

$$P(X_{n+1} = 1 \mid n \text{ 번 가운데 성공 } k \text{ 번}) = \frac{k + 1}{n + 2}$$

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# --- 패널 1: 차례대로 하는 베이즈 갱신 ---
x = np.linspace(0, 1, 500)
alpha0, beta0 = 1, 1
np.random.seed(42)
true_p = 0.35
observations = np.random.binomial(1, true_p, 20)

steps = [0, 1, 3, 5, 10, 20]
colors = plt.cm.viridis(np.linspace(0, 0.9, len(steps)))

for i, n in enumerate(steps):
    k = observations[:n].sum()
    a, b = alpha0 + k, beta0 + n - k
    axes[0].plot(x, stats.beta.pdf(x, a, b), color=colors[i], lw=2,
                 label=f'n={n}, k={k}: Beta({a},{b})')

axes[0].axvline(true_p, color='red', ls='--', lw=1.5, label=f'True p={true_p}')
axes[0].set_title('Sequential Bayesian Updating')
axes[0].set_xlabel('p')
axes[0].set_ylabel('Density')
axes[0].legend(fontsize=8)
axes[0].grid(True, alpha=0.3)

# --- 패널 2: A/B 검정 ---
n_sim = 100000
pA = np.random.beta(51, 151, n_sim)
pB = np.random.beta(66, 136, n_sim)

axes[1].hist(pA, bins=80, density=True, alpha=0.5, color='blue', label='Version A')
axes[1].hist(pB, bins=80, density=True, alpha=0.5, color='red', label='Version B')
prob_b_better = np.mean(pB > pA)
axes[1].set_title(f'A/B Test: P(B > A) = {prob_b_better:.3f}')
axes[1].set_xlabel('Conversion rate p')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# --- 패널 3: 신용구간이 좁아지는 모습 ---
sample_sizes = np.arange(1, 201)
ci_widths = []
alpha_p, beta_p = 1, 1
true_rate = 0.3

for n in sample_sizes:
    k = int(n * true_rate)
    a, b = alpha_p + k, beta_p + n - k
    lo = stats.beta.ppf(0.025, a, b)
    hi = stats.beta.ppf(0.975, a, b)
    ci_widths.append(hi - lo)

axes[2].plot(sample_sizes, ci_widths, 'b-', lw=2)
axes[2].set_title('95% Credible Interval Width vs Sample Size')
axes[2].set_xlabel('Number of observations')
axes[2].set_ylabel('CI Width')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('beta_bayesian_applications.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 연습문제

**연습문제 1.**
어떤 동전의 앞면이 나올 확률 $p$ 가 알려져 있지 않다. 사전분포는 $p \sim \text{Beta}(2, 2)$ 이다. 동전을 10번 던져 앞면을 7번 얻었다. 사후분포와 사후평균을 구하여라.

??? success "연습문제 1 풀이"
    베타-이항 켤레성에 따라 사후분포는 다음과 같다.

    $$p \mid X = 7 \sim \text{Beta}(2 + 7, 2 + 3) = \text{Beta}(9, 5)$$

    사후평균은 $\frac{9}{14} \approx 0.643$ 이다.

    이 값은 사전평균 $\frac{2}{4} = 0.5$ 와 최대가능도추정값 $\frac{7}{10} = 0.7$ 사이에 있으며, $n = 10$ 이 사전의 가상 관측수 $\alpha + \beta = 4$ 보다 크므로 자료 쪽에 더 가깝다.
