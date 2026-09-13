# 지수분포의 합으로서의 감마분포

## 정의

!!! info "감마분포"
    연속확률변수 $X$ 의 확률밀도함수가 다음과 같으면, $X$ 는 모양모수가 $\alpha > 0$ 이고 비율모수가 $\lambda > 0$ 인 **감마분포**를 따른다고 하고 $X \sim \Gamma(\alpha, \lambda)$ 로 적는다.

    $$f(x) = \frac{\lambda(\lambda x)^{\alpha - 1} e^{-\lambda x}}{\Gamma(\alpha)}, \quad x > 0$$

### 직관: α번째 도착을 기다리기

비율이 $\lambda$ 인 푸아송 과정에서 **$\alpha$ 번째 도착**까지 걸리는 시간은 $\Gamma(\alpha, \lambda)$ 를 따른다. $\alpha$ 가 양의 정수 $n$ 일 때 이 대기시간은 각각 $\text{Exp}(\lambda)$ 인 i.i.d. 도착간격 $n$ 개의 합이다.

## 지수분포의 합으로 만들기

$X_1, X_2, \ldots, X_n$ 이 i.i.d. $\text{Exp}(\lambda)$ 이면 그 합은 감마분포를 따른다.

$$S_n = X_1 + X_2 + \cdots + X_n \sim \Gamma(n, \lambda)$$

이것은 합성곱을 사슬처럼 이어 가며 쌓아 올린 결과이다.

| 합 | 분포 |
|:---:|:---:|
| $X_1$ | $\text{Exp}(\lambda) \stackrel{d}{=} \Gamma(1, \lambda)$ |
| $X_1 + X_2$ | $\text{Exp}(\lambda) * \text{Exp}(\lambda) \stackrel{d}{=} \Gamma(2, \lambda)$ |
| $X_1 + X_2 + X_3$ | $\Gamma(2, \lambda) * \text{Exp}(\lambda) \stackrel{d}{=} \Gamma(3, \lambda)$ |
| $X_1 + \cdots + X_n$ | $\Gamma(n, \lambda)$ |

### 확인: Exp(λ) = Γ(1, λ)

감마분포의 확률밀도함수에 $\alpha = 1$ 을 넣으면 다음을 얻는다.

$$\frac{\lambda(\lambda x)^{1-1} e^{-\lambda x}}{\Gamma(1)} = \lambda e^{-\lambda x}$$

$\Gamma(1) = 1$ 이고 $(\lambda x)^0 = 1$ 이기 때문이다. 이것은 바로 $\text{Exp}(\lambda)$ 의 확률밀도함수이다.

## 덧셈 성질

!!! info "감마분포의 덧셈 성질"
    $X \sim \Gamma(\alpha, \lambda)$ 와 $Y \sim \Gamma(\beta, \lambda)$ 가 **독립**이고 **비율이 같으면**($\lambda$ 가 같으면) 다음이 성립한다.

    $$X + Y \sim \Gamma(\alpha + \beta, \lambda)$$

    합성곱 기호로 쓰면 $\Gamma(\alpha, \lambda) * \Gamma(\beta, \lambda) \stackrel{d}{=} \Gamma(\alpha + \beta, \lambda)$ 이다.

### 합성곱을 이용한 증명

독립인 $X \sim \Gamma(\alpha, \lambda)$ 와 $Y \sim \Gamma(\beta, \lambda)$ 에 대하여 $x \geq 0$ 일 때 다음이 성립한다.

$$f_{X+Y}(x) = \int_0^x f_X(s) \, f_Y(x - s) \, ds$$

$$= \int_0^x \frac{\lambda(\lambda s)^{\alpha - 1} e^{-\lambda s}}{\Gamma(\alpha)} \cdot \frac{\lambda(\lambda(x - s))^{\beta - 1} e^{-\lambda(x-s)}}{\Gamma(\beta)} \, ds$$

$s$ 에 의존하지 않는 항을 밖으로 빼내면 다음과 같다.

$$= \frac{1}{\Gamma(\alpha)\Gamma(\beta)} \left[\int_0^x \lambda(\lambda s)^{\alpha-1} \lambda(\lambda(x-s))^{\beta-1} \, ds \right] e^{-\lambda x}$$

$t = s/x$ 로 치환하면($ds = x \, dt$) 다음을 얻는다.

$$= \frac{1}{\Gamma(\alpha)\Gamma(\beta)} \left[\int_0^1 t^{\alpha-1}(1-t)^{\beta-1} \, dt \right] \lambda(\lambda x)^{\alpha + \beta - 1} e^{-\lambda x}$$

여기서 적분은 **베타함수** $B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha + \beta)}$ 이므로 다음과 같이 된다.

$$f_{X+Y}(x) = \frac{\lambda(\lambda x)^{(\alpha + \beta) - 1} e^{-\lambda x}}{\Gamma(\alpha + \beta)}$$

이것은 $\Gamma(\alpha + \beta, \lambda)$ 의 확률밀도함수이다.

## 관련된 분포들

| 분포 | 감마분포꼴 | 설명 |
|:---:|:---:|:---|
| $\text{Exp}(\lambda)$ | $\Gamma(1, \lambda)$ | 첫 도착까지의 시간 |
| 얼랑$(2, \lambda)$ | $\Gamma(2, \lambda)$ | 두 번째 도착까지의 시간 |
| 얼랑$(k, \lambda)$ | $\Gamma(k, \lambda)$ | $k$ 번째 도착까지의 시간(정수 $k$) |
| $\chi^2_1$ | $\Gamma(1/2, 1/2)$ | 표준정규확률변수의 제곱 |
| $\chi^2_d$ | $\Gamma(d/2, 1/2)$ | 표준정규확률변수 $d$ 개의 제곱의 합 |

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# lambda 를 고정하고 여러 alpha 값에 대한 감마분포 확률밀도함수를 그린다
lam = 2.0
x = np.linspace(0, 10, 500)
alphas = [1, 2, 3, 4, 5]
colors = ['blue', 'red', 'magenta', 'black', 'cyan']

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 확률밀도함수 그림
for alpha, color in zip(alphas, colors):
    # scipy 는 shape=alpha, scale=1/lambda 를 쓴다
    pdf = stats.gamma.pdf(x, a=alpha, scale=1/lam)
    axes[0].plot(x, pdf, color=color, lw=2, label=f'α={alpha}')

axes[0].set_title(f'PDF of Gamma Distribution (λ = {lam})')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].set_ylim(0, 2)
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# 덧셈 성질 보이기: Γ(2,λ) + Γ(3,λ) = Γ(5,λ)
np.random.seed(42)
n_sim = 50000

X = np.random.gamma(shape=2, scale=1/lam, size=n_sim)  # Γ(2, λ)
Y = np.random.gamma(shape=3, scale=1/lam, size=n_sim)  # Γ(3, λ)
Z = X + Y  # Γ(5, λ) 가 되어야 한다

axes[1].hist(Z, bins=80, density=True, alpha=0.5, color='blue',
             label='X + Y (simulated)')
x_theory = np.linspace(0, 8, 200)
pdf_theory = stats.gamma.pdf(x_theory, a=5, scale=1/lam)
axes[1].plot(x_theory, pdf_theory, 'r-', lw=2,
             label='Γ(5, 2) PDF')
axes[1].set_title('Additivity: Γ(2,2) + Γ(3,2) = Γ(5,2)')
axes[1].set_xlabel('x')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('gamma_definition.png', dpi=150, bbox_inches='tight')
plt.show()

# 지수분포의 합으로 확인하기
print("=== Γ(n, λ) as Sum of n iid Exp(λ) ===")
for n in [2, 3, 5, 10]:
    exp_samples = np.random.exponential(1/lam, size=(n_sim, n))
    sums = exp_samples.sum(axis=1)
    gamma_samples = np.random.gamma(shape=n, scale=1/lam, size=n_sim)
    print(f"n={n}: Sum of Exp mean={np.mean(sums):.4f}, "
          f"Gamma mean={np.mean(gamma_samples):.4f}, "
          f"theory={n/lam:.4f}")
```

## 연습문제

**연습문제 1.**
$X \sim \Gamma(2, 5)$ 와 $Y \sim \Gamma(3, 5)$ 가 독립일 때 $X + Y$ 의 분포와 평균, 분산을 구하여라.

??? success "연습문제 1 풀이"
    $X + Y \sim \Gamma(2 + 3, 5) = \Gamma(5, 5)$ 이다.

    $E[X + Y] = 5/5 = 1$

    $\text{Var}(X + Y) = 5/25 = 0.2$
