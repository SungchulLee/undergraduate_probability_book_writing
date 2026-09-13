# 감마분포의 특별한 경우로서의 얼랑분포

## 정의

!!! info "얼랑분포"
    모양모수가 $k$ (양의 정수)이고 비율이 $\lambda > 0$ 인 **얼랑분포**는 모양모수를 정수로 제한한 감마분포이다.

    $$\text{Erlang}(k, \lambda) = \Gamma(k, \lambda)$$

    그 확률밀도함수는 다음과 같다.

    $$f(x) = \frac{\lambda(\lambda x)^{k-1} e^{-\lambda x}}{(k-1)!}, \quad x > 0$$

    여기서는 양의 정수 $k$ 에 대하여 $\Gamma(k) = (k-1)!$ 임을 썼다.

## 왜 따로 이름을 붙였는가

얼랑분포는 20세기 초에 전화 통화의 대기시간을 나타내는 모형으로 이 분포를 들여온 A.K. 얼랑의 이름을 딴 것이다. 수학적으로는 감마분포의 특별한 경우일 뿐이지만, 다음과 같은 까닭으로 제 이름을 갖고 있다.

- 응용에서는 일반적인 감마분포보다 먼저 쓰였다
- 모양모수가 정수여서 **i.i.d. 지수확률변수의 합**이라는 구체적인 뜻을 갖는다
- 일반적인 감마분포와 달리 누적분포함수가 유한합으로 된 닫힌 꼴을 갖는다

## 특별한 경우

| 분포 | 모수 | 설명 |
|:---:|:---:|:---|
| $\text{Exp}(\lambda)$ | $\text{Erlang}(1, \lambda)$ | 도착간격 하나 |
| $\text{Erlang}(2, \lambda)$ | $\Gamma(2, \lambda)$ | i.i.d. $\text{Exp}(\lambda)$ 두 개의 합 |
| $\text{Erlang}(k, \lambda)$ | $\Gamma(k, \lambda)$ | i.i.d. $\text{Exp}(\lambda)$ $k$ 개의 합 |

## 누적분포함수(닫힌 꼴)

정수 $k$ 에 대하여 $\text{Erlang}(k, \lambda)$ 의 누적분포함수는 닫힌 꼴을 갖는다.

$$F(x) = 1 - \sum_{j=0}^{k-1} \frac{(\lambda x)^j}{j!} e^{-\lambda x}, \quad x \geq 0$$

이것은 푸아송분포와의 연결에서 유도할 수 있다. $N(t) \sim \text{Po}(\lambda t)$ 일 때 $P(S_k \leq t) = P(N(t) \geq k)$ 이기 때문이다.

## 적률

감마분포에서 다음을 얻는다.

$$E[X] = \frac{k}{\lambda}, \qquad \text{Var}(X) = \frac{k}{\lambda^2}$$

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

lam = 2.0
x = np.linspace(0, 8, 300)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 여러 k 에 대한 얼랑분포 확률밀도함수
for k in [1, 2, 3, 5, 10]:
    pdf = stats.gamma.pdf(x, a=k, scale=1/lam)
    axes[0].plot(x, pdf, lw=2, label=f'Erlang({k}, {lam})')

axes[0].set_title(f'Erlang(k, λ={lam}) PDFs')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# 확인: i.i.d. Exp(λ) k 개의 합 = Erlang(k, λ)
np.random.seed(42)
n_sim = 50000
k = 5

# 방법 1: 지수확률변수의 합
exp_samples = np.random.exponential(1/lam, size=(n_sim, k))
sums = exp_samples.sum(axis=1)

# 방법 2: 감마분포에서 바로 표집
gamma_samples = np.random.gamma(shape=k, scale=1/lam, size=n_sim)

axes[1].hist(sums, bins=60, density=True, alpha=0.4,
             label=f'Sum of {k} Exp({lam})', color='blue')
axes[1].hist(gamma_samples, bins=60, density=True, alpha=0.4,
             label=f'Γ({k}, {lam})', color='red')
pdf_theory = stats.gamma.pdf(x, a=k, scale=1/lam)
axes[1].plot(x, pdf_theory, 'k-', lw=2, label='Theory')
axes[1].set_title(f'Sum of {k} iid Exp({lam}) = Erlang({k}, {lam})')
axes[1].set_xlabel('x')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('erlang_distribution.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 연습문제

**연습문제 1.**
어떤 은행에 들어갔더니 앞에 한 사람이 줄을 서 있고 창구는 5개이며, 각 창구의 처리 시간은 i.i.d. $\text{Exp}(\lambda_B)$ 로 $\lambda_B^{-1} = 10$ 분이다. 은행을 나온 뒤에는 우체국에 들르는데, 그곳에는 앞에 두 사람이 줄을 서 있고 창구는 2개이며 처리 시간은 i.i.d. $\text{Exp}(\lambda_P)$ 로 $\lambda_P^{-1} = 4$ 분이다.

전체 대기시간 가운데 은행에서 보낸 시간의 비율을 $F$ 라 하자. $E[F]$ 와 $\text{Var}(F)$ 를 구하여라.

??? success "연습문제 1 풀이"
    **은행:** 창구가 5개이고 사람이 2명(나 + 앞의 1명)이므로 실질적인 처리 비율은 분당 $5\lambda_B = 0.5$ 이다. 처리를 두 번 기다리므로 $X_i \sim \text{Exp}(0.5)$ 에 대하여 $T_B = X_1 + X_2$ 이고, 따라서 $T_B \sim \Gamma(2, 0.5)$ 이다.

    **우체국:** 창구가 2개이고 사람이 3명(나 + 앞의 2명)이므로 실질적인 처리 비율은 분당 $2\lambda_P = 0.5$ 이다. 처리를 세 번 기다리므로 $Y_j \sim \text{Exp}(0.5)$ 에 대하여 $T_P = Y_1 + Y_2 + Y_3$ 이고, 따라서 $T_P \sim \Gamma(3, 0.5)$ 이다.

    $T_B \sim \Gamma(2, 0.5)$ 와 $T_P \sim \Gamma(3, 0.5)$ 가 독립이고 비율이 같으므로 다음이 성립한다.

    $$F = \frac{T_B}{T_B + T_P} \sim \text{Beta}(2, 3)$$

    $$E[F] = \frac{\alpha}{\alpha + \beta} = \frac{2}{5} = 0.4$$

    $$\text{Var}(F) = \frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)} = \frac{6}{25 \cdot 6} = \frac{1}{25} = 0.04$$
