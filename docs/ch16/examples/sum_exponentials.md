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

---

**연습문제 2.**
$X_1, \ldots, X_n$ 이 i.i.d. $\text{Exp}(\lambda)$ 라고 하자. $S_n = \sum_{i=1}^n X_i$ 의 적률생성함수를 써서 $S_n \sim \text{Gamma}(n, \lambda)$ 임을 보여라. 또 $E[S_n]$ 과 $\text{Var}(S_n)$ 을 구하여라.
