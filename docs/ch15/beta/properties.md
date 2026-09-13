# 성질과 모양 분석

## 특별한 경우

베타분포는 낯익은 여러 분포를 특별한 경우로 품고 있다.

!!! info "Beta(α, β) 의 특별한 경우"
    | 모수 | 분포 | 확률밀도함수 |
    |:---:|:---:|:---:|
    | $\alpha = 1, \beta = 1$ | $\text{Uniform}(0,1)$ | $f(x) = 1$ |
    | $\alpha = n, \beta = 1$ | 거듭제곱분포 | $f(x) = nx^{n-1}$ |
    | $\alpha = 1, \beta = n$ | 뒤집은 거듭제곱분포 | $f(x) = n(1-x)^{n-1}$ |
    | $\alpha = \tfrac{1}{2}, \beta = \tfrac{1}{2}$ | 아크사인분포 | $f(x) = \frac{1}{\pi\sqrt{x(1-x)}}$ |

$\text{Beta}(1,1) = \text{Uniform}(0,1)$ 인 경우는 바로 나온다. $\alpha = \beta = 1$ 이면 확률밀도함수가 $f(x) = \frac{x^0(1-x)^0}{B(1,1)} = \frac{1}{1} = 1$ 이기 때문이다.

## 모양 분석

베타분포 확률밀도함수의 모양은 모수가 1보다 큰지 작은지에 따라 달라진다.

**최빈값.** $\alpha, \beta > 1$ 이면 베타분포는 봉우리가 하나이고 최빈값은 다음과 같다.

$$\text{Mode} = \frac{\alpha - 1}{\alpha + \beta - 2}$$

이것은 $f'(x) = 0$ 으로 놓아 $(\alpha - 1)(1 - x) = (\beta - 1)x$ 를 얻는 데에서 나온다.

**모양의 갈래:**

- $\alpha > 1, \beta > 1$: $(0, 1)$ 위에서 봉우리가 하나인 종 모양
- $\alpha < 1, \beta < 1$: U자 모양(양 끝에 봉우리가 둘)
- $\alpha = \beta$: $x = 1/2$ 에 대하여 대칭
- $\alpha > \beta$: 왼쪽으로 치우쳐 있다(확률이 1쪽에 모인다)
- $\alpha < \beta$: 오른쪽으로 치우쳐 있다(확률이 0쪽에 모인다)

## 고차 적률

!!! info "원점 적률"
    $X \sim \text{Beta}(\alpha, \beta)$ 에 대하여 다음이 성립한다.

    $$E[X^k] = \frac{B(\alpha + k, \beta)}{B(\alpha, \beta)} = \prod_{j=0}^{k-1} \frac{\alpha + j}{\alpha + \beta + j}$$

특히 다음과 같다.

$$E[X] = \frac{\alpha}{\alpha + \beta}, \qquad E[X^2] = \frac{\alpha(\alpha+1)}{(\alpha+\beta)(\alpha+\beta+1)}$$

**왜도:**

$$\gamma_1 = \frac{2(\beta - \alpha)\sqrt{\alpha + \beta + 1}}{(\alpha + \beta + 2)\sqrt{\alpha\beta}}$$

$\alpha = \beta$ 이면 왜도가 0이다(분포가 대칭이다).

**첨도(초과첨도):**

$$\gamma_2 = \frac{6(\alpha^3 - \alpha^2(2\beta - 1) + \beta^2(\beta + 1) - 2\alpha\beta(\beta + 2))}{{\alpha\beta(\alpha + \beta + 2)(\alpha + \beta + 3)}}$$

## 베이즈 켤레성

베타분포는 이항분포 가능도에 대한 **켤레사전분포**이다. 곧 베타분포를 사전분포로 삼고 이항분포 자료를 관찰하면 사후분포도 베타분포가 된다는 뜻이다.

!!! info "베타-이항 켤레성"
    **사전분포:** $p \sim \text{Beta}(\alpha, \beta)$

    **가능도:** $X \mid p \sim \text{Binomial}(n, p)$

    **사후분포:** $p \mid X = k \sim \text{Beta}(\alpha + k, \beta + n - k)$

**유도.** 베이즈 정리에 따라 다음이 성립한다.

$$f(p \mid X = k) \propto f(k \mid p) \cdot f(p) \propto p^k(1-p)^{n-k} \cdot p^{\alpha - 1}(1-p)^{\beta - 1} = p^{\alpha + k - 1}(1-p)^{\beta + n - k - 1}$$

이것은 $\text{Beta}(\alpha + k, \beta + n - k)$ 밀도함수의 알맹이이다.

**뜻풀이:**

- $\alpha$ 는 "사전의 성공 횟수", $\beta$ 는 "사전의 실패 횟수" 구실을 한다
- $\alpha + \beta$ 는 사전분포가 얼마나 많은 정보를 담고 있는지를 정한다
- 사후평균은 사전평균과 자료의 가중평균이다

$$E[p \mid X = k] = \frac{\alpha + k}{\alpha + \beta + n} = \frac{\alpha + \beta}{\alpha + \beta + n} \cdot \underbrace{\frac{\alpha}{\alpha + \beta}}_{\text{사전평균}} + \frac{n}{\alpha + \beta + n} \cdot \underbrace{\frac{k}{n}}_{\text{MLE}}$$

## 대칭성과 반사

!!! info "반사 성질"
    $X \sim \text{Beta}(\alpha, \beta)$ 이면 $1 - X \sim \text{Beta}(\beta, \alpha)$ 이다.

**증명.** $Y = 1 - X$ 라 하자. $0 < y < 1$ 에 대하여 다음이 성립한다.

$$P(Y \leq y) = P(X \geq 1 - y) = \int_{1-y}^{1} \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}\,dx$$

$u = 1 - x$ 로 치환하면 다음을 얻는다.

$$= \int_0^{y} \frac{(1-u)^{\alpha-1}u^{\beta-1}}{B(\alpha,\beta)}\,du$$

이것은 $\text{Beta}(\beta, \alpha)$ 의 누적분포함수이다. $\square$

## 순서통계량과의 연결

베타분포는 균등분포에서 나온 순서통계량의 분포로 자연스럽게 나타난다.

!!! info "순서통계량과의 연결"
    $U_1, U_2, \ldots, U_n \overset{\text{iid}}{\sim} \text{Uniform}(0,1)$ 이고 $U_{(k)}$ 가 $k$ 번째로 작은 값이면 다음이 성립한다.

    $$U_{(k)} \sim \text{Beta}(k, n - k + 1)$$

이는 15.5절(순서통계량)에서 자세히 증명한다.

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# --- 패널 1: 모양의 갈래 ---
x = np.linspace(0.001, 0.999, 500)
cases = [
    ((0.5, 0.5), 'U-shaped', 'red'),
    ((1, 1), 'Uniform', 'black'),
    ((2, 5), 'Right-skewed', 'blue'),
    ((5, 2), 'Left-skewed', 'green'),
    ((5, 5), 'Symmetric bell', 'purple'),
    ((10, 10), 'Concentrated', 'orange'),
]
for (a, b), label, color in cases:
    pdf = stats.beta.pdf(x, a, b)
    pdf = np.clip(pdf, 0, 8)
    axes[0].plot(x, pdf, color=color, lw=2, label=f'({a},{b}) {label}')
axes[0].set_title('Beta PDF Shape Regimes')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].set_ylim(0, 5)
axes[0].legend(fontsize=8)
axes[0].grid(True, alpha=0.3)

# --- 패널 2: 베이즈 갱신 ---
alpha_prior, beta_prior = 2, 2
n_obs, k_obs = 10, 7

alpha_post = alpha_prior + k_obs
beta_post = beta_prior + n_obs - k_obs

axes[1].plot(x, stats.beta.pdf(x, alpha_prior, beta_prior),
             'b-', lw=2, label=f'Prior: Beta({alpha_prior},{beta_prior})')
axes[1].plot(x, stats.beta.pdf(x, alpha_post, beta_post),
             'r-', lw=2, label=f'Posterior: Beta({alpha_post},{beta_post})')
axes[1].axvline(k_obs / n_obs, color='green', ls='--', lw=1.5,
                label=f'MLE = {k_obs}/{n_obs}')
axes[1].set_title(f'Bayesian Updating (observed {k_obs}/{n_obs})')
axes[1].set_xlabel('p')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# --- 패널 3: 순서통계량 ---
np.random.seed(42)
n, k = 10, 3
n_sim = 100000
samples = np.sort(np.random.uniform(size=(n_sim, n)), axis=1)
order_stat = samples[:, k - 1]

axes[2].hist(order_stat, bins=60, density=True, alpha=0.5,
             color='steelblue', label=f'$U_{{({k})}}$ simulated')
theory = stats.beta.pdf(x, k, n - k + 1)
axes[2].plot(x, theory, 'r-', lw=2,
             label=f'Beta({k},{n-k+1}) PDF')
axes[2].set_title(f'Order Statistic $U_{{({k})}}$ from Uniform(0,1), n={n}')
axes[2].set_xlabel('x')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('beta_properties.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 연습문제

**연습문제 1.** $X \sim \text{Beta}(3, 2)$ 라 하자. $E[X]$, $\text{Var}(X)$, 그리고 최빈값을 구하여라.

??? success "연습문제 1 풀이"
    $E[X] = \frac{3}{3+2} = 0.6$ 이다. $\text{Var}(X) = \frac{3 \cdot 2}{(5)^2 \cdot 6} = \frac{6}{150} = 0.04$ 이다.

    최빈값 $= \frac{3-1}{3+2-2} = \frac{2}{3} \approx 0.667$ 이다.

---

**연습문제 2.** $X \sim \text{Beta}(1, 1)$ 일 때 확률밀도함수를 계산하여 $X \sim \text{Uniform}(0, 1)$ 임을 확인하여라.

??? success "연습문제 2 풀이"
    $f(x) = \frac{x^{1-1}(1-x)^{1-1}}{B(1,1)} = \frac{1}{B(1,1)}$ 이다. $B(1,1) = \frac{\Gamma(1)\Gamma(1)}{\Gamma(2)} = \frac{1 \cdot 1}{1} = 1$ 이므로 $0 < x < 1$ 에 대하여 $f(x) = 1$ 이다. 이것이 $\text{Uniform}(0,1)$ 의 확률밀도함수이다. $\square$

---

**연습문제 3.** 베타-이항 켤레성을 써라. 앞면이 나올 확률 $p$ 에 대한 사전분포가 $\text{Beta}(2, 2)$ 라 하자. 동전을 10번 던져 앞면을 7번 얻었다. 사후분포와 사후평균을 구하여라.

??? success "연습문제 3 풀이"
    사후분포: $\text{Beta}(2 + 7, 2 + 3) = \text{Beta}(9, 5)$ 이다.

    사후평균: $\frac{9}{9 + 5} = \frac{9}{14} \approx 0.643$ 이다.

    이 값이 사전평균($0.5$)과 최대가능도추정값($0.7$) 사이에 있음에 눈길을 주자. 예상한 대로이다.

---

**연습문제 4.** 반사 성질을 증명하여라. 곧 $X \sim \text{Beta}(\alpha, \beta)$ 이면 $1 - X \sim \text{Beta}(\beta, \alpha)$ 임을 보여라.

??? success "연습문제 4 풀이"
    $Y = 1 - X$ 라 하자. $Y$ 의 누적분포함수는 다음과 같다.

    $$
    F_Y(y) = P(1 - X \leq y) = P(X \geq 1 - y) = 1 - F_X(1 - y)
    $$

    미분하면 $f_Y(y) = f_X(1-y) = \frac{(1-y)^{\alpha-1}y^{\beta-1}}{B(\alpha,\beta)} = \frac{y^{\beta-1}(1-y)^{\alpha-1}}{B(\beta,\alpha)}$ 이다.

    $B(\alpha, \beta) = B(\beta, \alpha)$ 이기 때문이다. 이것이 $\text{Beta}(\beta, \alpha)$ 의 확률밀도함수이다. $\square$

---

**연습문제 5.** 원점 적률 공식 $E[X^k] = \prod_{j=0}^{k-1}\frac{\alpha+j}{\alpha+\beta+j}$ 를 써서 $X \sim \text{Beta}(2, 3)$ 의 $E[X^2]$ 을 구하여라.

??? success "연습문제 5 풀이"
    $$
    E[X^2] = \frac{\alpha}{\alpha+\beta} \cdot \frac{\alpha+1}{\alpha+\beta+1} = \frac{2}{5} \cdot \frac{3}{6} = \frac{6}{30} = \frac{1}{5} = 0.2
    $$
