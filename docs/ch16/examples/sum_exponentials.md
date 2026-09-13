# 독립인 지수확률변수의 합

## 결과

!!! info "지수분포의 합성곱"
    $X_1, X_2, \ldots, X_n$ 이 i.i.d. $\text{Exp}(\lambda)$ 이면 다음이 성립한다.

    $$X_1 + X_2 + \cdots + X_n \sim \Gamma(n, \lambda)$$

    합성곱 기호로 적으면 다음과 같다.

    $$\underbrace{\text{Exp}(\lambda) * \text{Exp}(\lambda) * \cdots * \text{Exp}(\lambda)}_{n \text{ 번}} \stackrel{d}{=} \Gamma(n, \lambda)$$

## 증명: 지수확률변수 두 개

독립인 $X \sim \text{Exp}(\lambda)$ 와 $Y \sim \text{Exp}(\lambda)$ 에 대하여 $a \geq 0$ 일 때 다음이 성립한다.

$$f_{X+Y}(a) = \int_0^a \lambda e^{-\lambda b} \cdot \lambda e^{-\lambda(a-b)} \, db = \lambda^2 e^{-\lambda a} \int_0^a db = \lambda^2 a \, e^{-\lambda a}$$

이것은 $\Gamma(2, \lambda)$ 의 확률밀도함수이다.

$$\frac{\lambda(\lambda a)^{2-1} e^{-\lambda a}}{\Gamma(2)} = \lambda^2 a \, e^{-\lambda a} \quad \checkmark$$

## 증명: 일반적인 n, 귀납법으로

$S_{n-1} = X_1 + \cdots + X_{n-1} \sim \Gamma(n-1, \lambda)$ 와 $X_n \sim \text{Exp}(\lambda)$ 가 독립이면 **감마분포의 덧셈 성질**에 따라 다음이 성립한다.

$$S_n = S_{n-1} + X_n \sim \Gamma(n-1, \lambda) * \Gamma(1, \lambda) = \Gamma(n, \lambda)$$

감마분포의 덧셈 성질(14장에서 합성곱으로 증명하였다)이 귀납법의 한 걸음을 맡아 준다.

## 비율이 서로 다른 경우

지수확률변수들의 비율이 **서로 다르면** 그 합은 더 이상 감마분포를 따르지 않는다. $\lambda_1 \neq \lambda_2$ 인 $X \sim \text{Exp}(\lambda_1)$ 과 $Y \sim \text{Exp}(\lambda_2)$ 에 대하여 다음이 성립한다.

$$f_{X+Y}(a) = \frac{\lambda_1 \lambda_2}{\lambda_1 - \lambda_2}\left(e^{-\lambda_2 a} - e^{-\lambda_1 a}\right), \quad a \geq 0$$

이것은 지수 항들이 섞여 있는 **하이포지수분포**이다.

## 푸아송 과정과의 관계

합 $S_n = X_1 + \cdots + X_n$ 은 비율이 $\lambda$ 인 푸아송 과정에서 **$n$ 번째 도착시각**이다. $S_n \sim \Gamma(n, \lambda)$ 라는 사실이 다음 둘을 이어 준다.

- **세기**(푸아송분포): $N(t) \sim \text{Po}(\lambda t)$
- **기다리기**(감마분포): $S_n \sim \Gamma(n, \lambda)$

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 100000
lam = 2.0

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 여러 n 에 대한 i.i.d. Exp(lambda) n 개의 합
x = np.linspace(0, 10, 300)
for n in [1, 2, 3, 5, 10]:
    # 모의실험
    samples = np.random.exponential(1/lam, (n_sim, n))
    sums = samples.sum(axis=1)

    # 모의실험 결과와 이론값을 그린다
    axes[0].hist(sums, bins=60, density=True, alpha=0.2)
    pdf = stats.gamma.pdf(x, a=n, scale=1/lam)
    axes[0].plot(x, pdf, lw=2, label=f'n={n}: Γ({n},{lam})')

axes[0].set_title(f'Sum of n iid Exp({lam})')
axes[0].set_xlabel('Sum')
axes[0].set_ylabel('Density')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# 비율이 서로 다른 경우: Exp(1) + Exp(3)
l1, l2 = 1.0, 3.0
X1 = np.random.exponential(1/l1, n_sim)
X2 = np.random.exponential(1/l2, n_sim)
S = X1 + X2

a_vals = np.linspace(0, 6, 200)
pdf_hypo = l1 * l2 / (l1 - l2) * (np.exp(-l2 * a_vals) - np.exp(-l1 * a_vals))

axes[1].hist(S, bins=60, density=True, alpha=0.5, color='steelblue',
             label='Simulated')
axes[1].plot(a_vals, pdf_hypo, 'r-', lw=2, label='Hypoexponential PDF')
axes[1].set_title(f'Exp({l1}) + Exp({l2}) (different rates)')
axes[1].set_xlabel('Sum')
axes[1].set_ylabel('Density')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('sum_exponentials.png', dpi=150, bbox_inches='tight')
plt.show()

# 적률을 확인한다
for n in [2, 5, 10]:
    samples = np.random.exponential(1/lam, (n_sim, n))
    sums = samples.sum(axis=1)
    print(f"Sum of {n} Exp({lam}): mean={np.mean(sums):.4f} "
          f"(theory {n/lam:.4f}), var={np.var(sums):.4f} "
          f"(theory {n/lam**2:.4f})")
```

## 연습문제

**연습문제 1.**
$X$ 와 $Y$ 가 독립인 $\text{Exp}(1)$ 확률변수라고 하자. 합성곱 적분으로 $X + Y$ 의 확률밀도함수를 구하고, 그 결과가 $\text{Gamma}(2, 1)$ 과 일치함을 확인하여라.

??? success "연습문제 1 풀이"
    **1단계: 적분 구간 정하기.** $\lambda = 1$ 이므로 $f_X(b) = e^{-b}$ 가 $b \geq 0$ 에서, $f_Y(c) = e^{-c}$ 가 $c \geq 0$ 에서 성립한다. 피적분함수가 $0$ 이 아니려면 다음 두 조건이 동시에 필요하다.

    $$
    b \geq 0 \quad \text{이고} \quad a - b \geq 0
    $$

    둘을 합치면 $0 \leq b \leq a$ 이다. 특히 $a < 0$ 이면 그런 $b$ 가 없으므로 $f_{X+Y}(a) = 0$ 이다.

    **2단계: 합성곱 적분 계산.** $a \geq 0$ 에 대하여 다음과 같다.

    $$
    f_{X+Y}(a) = \int_0^a e^{-b} \, e^{-(a-b)} \, db
    $$

    지수를 합치면 $-b - (a - b) = -a$ 가 되어 $b$ 가 사라진다. 이것이 계산이 쉬워지는 까닭이다.

    $$
    f_{X+Y}(a) = \int_0^a e^{-a} \, db = e^{-a} \int_0^a db = a\, e^{-a}
    $$

    **3단계: 감마분포와 맞추어 보기.** $\Gamma(\alpha, \lambda)$ 의 확률밀도함수는 다음과 같다.

    $$
    f(a) = \frac{\lambda^{\alpha}}{\Gamma(\alpha)} a^{\alpha - 1} e^{-\lambda a}, \qquad a > 0
    $$

    여기에 $\alpha = 2$, $\lambda = 1$ 을 넣고 $\Gamma(2) = 1! = 1$ 을 쓰면 다음을 얻는다.

    $$
    f(a) = \frac{1^2}{1} \cdot a^{2-1} e^{-a} = a\,e^{-a}
    $$

    2단계의 결과와 똑같으므로 $X + Y \sim \Gamma(2, 1)$ 이다.

    **확인.** 밀도가 맞는지 적분으로 점검한다. 부분적분을 쓰면 다음과 같다.

    $$
    \int_0^{\infty} a\, e^{-a}\, da = \Big[-a e^{-a}\Big]_0^{\infty} + \int_0^{\infty} e^{-a}\, da = 0 + 1 = 1
    $$

    또 $E[X + Y] = 1 + 1 = 2$ 와 $\text{Var}(X+Y) = 1 + 1 = 2$ 인데, 이는 $\Gamma(2,1)$ 의 평균 $\alpha/\lambda = 2$ 및 분산 $\alpha/\lambda^2 = 2$ 와 맞아떨어진다. 지수분포의 밀도는 $a = 0$ 에서 가장 크지만, 두 개를 더한 $a e^{-a}$ 는 $a = 0$ 에서 $0$ 이 되고 $a = 1$ 에서 꼭대기를 이룬다. 둘 다 거의 $0$ 이어야 합이 $0$ 근처가 되기 때문이다. $\square$

---

**연습문제 2.**
$X_1, \ldots, X_n$ 이 i.i.d. $\text{Exp}(\lambda)$ 라고 하자. $S_n = \sum_{i=1}^n X_i$ 의 적률생성함수를 써서 $S_n \sim \text{Gamma}(n, \lambda)$ 임을 보여라. 또 $E[S_n]$ 과 $\text{Var}(S_n)$ 을 구하여라.

??? success "연습문제 2 풀이"
    **1단계: $\text{Exp}(\lambda)$ 의 적률생성함수.** 정의대로 계산한다.

    $$
    M_X(t) = E\!\left[e^{tX}\right] = \int_0^{\infty} e^{tx} \lambda e^{-\lambda x} \, dx = \lambda \int_0^{\infty} e^{-(\lambda - t)x} \, dx
    $$

    이 적분이 수렴하려면 $\lambda - t > 0$, 곧 $t < \lambda$ 이어야 한다. 그때 값은 다음과 같다.

    $$
    M_X(t) = \lambda \cdot \frac{1}{\lambda - t} = \frac{\lambda}{\lambda - t} = \left(1 - \frac{t}{\lambda}\right)^{-1}, \qquad t < \lambda
    $$

    **2단계: 합의 적률생성함수.** $X_1, \ldots, X_n$ 이 독립이므로 적률생성함수는 곱해진다. 같은 분포를 따르므로 같은 인수가 $n$ 번 나온다.

    $$
    M_{S_n}(t) = \prod_{i=1}^{n} M_{X_i}(t) = \left(\frac{\lambda}{\lambda - t}\right)^{n}, \qquad t < \lambda
    $$

    **3단계: 알아보기.** $\Gamma(\alpha, \lambda)$ 의 적률생성함수는 $t < \lambda$ 에서 $\left(\dfrac{\lambda}{\lambda - t}\right)^{\alpha}$ 이다. 위 식은 $\alpha = n$ 인 경우와 정확히 같다. 적률생성함수의 유일성에 따라 다음을 얻는다.

    $$
    S_n \sim \Gamma(n, \lambda)
    $$

    **4단계: 평균과 분산.** 두 가지 길이 있다. 지수분포 하나의 평균이 $1/\lambda$, 분산이 $1/\lambda^2$ 이므로 기댓값의 선형성과 독립성을 쓰면 곧바로 나온다.

    $$
    E[S_n] = \sum_{i=1}^{n} E[X_i] = \frac{n}{\lambda}
    $$

    $$
    \text{Var}(S_n) = \sum_{i=1}^{n} \text{Var}(X_i) = \frac{n}{\lambda^2}
    $$

    감마분포의 공식 $E = \alpha/\lambda$, $\text{Var} = \alpha/\lambda^2$ 에 $\alpha = n$ 을 넣어도 같은 값이다.

    $n$ 이 커질수록 변동계수가 $\dfrac{\sqrt{n}/\lambda}{n/\lambda} = \dfrac{1}{\sqrt{n}}$ 으로 줄어든다. 곧 도착을 여러 번 기다릴수록 전체 대기시간의 상대적인 흔들림이 작아지며, 이것이 $\Gamma(n, \lambda)$ 의 모양이 $n$ 과 함께 정규분포에 가까워지는 까닭이다. $\square$
