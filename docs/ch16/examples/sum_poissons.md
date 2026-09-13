# 독립인 푸아송확률변수의 합(합성곱으로)

## 결과

!!! info "푸아송분포의 합성곱"
    $X \sim \text{Po}(\lambda_1)$ 과 $Y \sim \text{Po}(\lambda_2)$ 가 독립이면 다음이 성립한다.

    $$X + Y \sim \text{Po}(\lambda_1 + \lambda_2)$$

    합성곱 기호로 적으면 $\text{Po}(\lambda_1) * \text{Po}(\lambda_2) = \text{Po}(\lambda_1 + \lambda_2)$ 이다.

## 합성곱을 쓴 증명

음이 아닌 정수 $a$ 에 대하여 다음이 성립한다.

$$p_{X+Y}(a) = \sum_b p_X(b) \, p_Y(a - b)$$

합은 $b \geq 0$ 이고 $a - b \geq 0$ 인 범위, 곧 정수 $0 \leq b \leq a$ 에 대하여 취한다.

$$p_{X+Y}(a) = \sum_{b=0}^{a} \frac{\lambda_1^b}{b!} e^{-\lambda_1} \cdot \frac{\lambda_2^{a-b}}{(a-b)!} e^{-\lambda_2}$$

$e^{-(\lambda_1 + \lambda_2)}$ 를 밖으로 빼내면 다음을 얻는다.

$$= e^{-(\lambda_1 + \lambda_2)} \sum_{b=0}^{a} \frac{\lambda_1^b}{b!} \cdot \frac{\lambda_2^{a-b}}{(a-b)!}$$

$a!$ 를 곱하고 나누면 다음과 같다.

$$= \frac{e^{-(\lambda_1 + \lambda_2)}}{a!} \sum_{b=0}^{a} \frac{a!}{b!(a-b)!} \lambda_1^b \lambda_2^{a-b}$$

여기에서 **이항정리** $\sum_{b=0}^{a} \binom{a}{b} \lambda_1^b \lambda_2^{a-b} = (\lambda_1 + \lambda_2)^a$ 을 알아보면 다음을 얻는다.

$$= \frac{(\lambda_1 + \lambda_2)^a}{a!} e^{-(\lambda_1 + \lambda_2)}$$

이것은 $\text{Po}(\lambda_1 + \lambda_2)$ 의 확률질량함수이다. $\square$

## 적률생성함수를 쓴 다른 증명

적률생성함수를 쓰면 더 간결하다.

$$M_{X+Y}(t) = M_X(t) \cdot M_Y(t) = e^{\lambda_1(e^t - 1)} \cdot e^{\lambda_2(e^t - 1)} = e^{(\lambda_1 + \lambda_2)(e^t - 1)}$$

이것은 $\text{Po}(\lambda_1 + \lambda_2)$ 의 적률생성함수이다. 적률생성함수의 유일성에 따라 $X + Y \sim \text{Po}(\lambda_1 + \lambda_2)$ 이다.

## 일반적인 합

수학적 귀납법으로(또는 합성곱의 결합법칙으로) 다음을 얻는다.

$X_1, X_2, \ldots, X_n$ 이 독립이고 $X_i \sim \text{Po}(\lambda_i)$ 이면 다음이 성립한다.

$$X_1 + X_2 + \cdots + X_n \sim \text{Po}(\lambda_1 + \lambda_2 + \cdots + \lambda_n)$$

## 푸아송 과정과의 관계

이 결과는 푸아송 과정의 **합침 성질**에서 자연스럽게 따라 나온다. 비율이 $\lambda_1$ 과 $\lambda_2$ 인 두 독립인 푸아송 과정을 포개면, 합쳐진 과정은 비율이 $\lambda_1 + \lambda_2$ 인 푸아송 과정이 된다.

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 100000

lambda1, lambda2 = 3.0, 5.0

# 모의실험
X = np.random.poisson(lambda1, n_sim)
Y = np.random.poisson(lambda2, n_sim)
S = X + Y

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 모의실험 결과와 이론값을 견준다
k_vals = np.arange(0, 25)
pmf_theory = stats.poisson.pmf(k_vals, lambda1 + lambda2)

counts = np.bincount(S, minlength=25)[:25]
pmf_sim = counts / n_sim

axes[0].bar(k_vals - 0.15, pmf_sim, 0.3, color='steelblue', alpha=0.7,
            label='Simulation', edgecolor='black')
axes[0].bar(k_vals + 0.15, pmf_theory, 0.3, color='orange', alpha=0.7,
            label=f'Po({lambda1+lambda2})', edgecolor='black')
axes[0].set_title(f'Po({lambda1}) + Po({lambda2}) = Po({lambda1+lambda2})')
axes[0].set_xlabel('k')
axes[0].set_ylabel('P(X+Y = k)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# 합성곱 계산을 한 단계씩 확인한다
pmf_x = stats.poisson.pmf(k_vals, lambda1)
pmf_y = stats.poisson.pmf(k_vals, lambda2)
pmf_conv = np.convolve(pmf_x, pmf_y)[:25]

axes[1].bar(k_vals - 0.15, pmf_conv, 0.3, color='green', alpha=0.7,
            label='Numerical convolution', edgecolor='black')
axes[1].bar(k_vals + 0.15, pmf_theory, 0.3, color='orange', alpha=0.7,
            label=f'Po({lambda1+lambda2}) PMF', edgecolor='black')
axes[1].set_title('Numerical Convolution vs Theory')
axes[1].set_xlabel('k')
axes[1].set_ylabel('P(X+Y = k)')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('sum_poissons.png', dpi=150, bbox_inches='tight')
plt.show()

print(f"Simulation: mean={np.mean(S):.4f} (theory {lambda1+lambda2:.4f})")
print(f"Simulation: var={np.var(S):.4f} (theory {lambda1+lambda2:.4f})")
```

## 연습문제

**연습문제 1.**
$X \sim \text{Po}(2)$ 와 $Y \sim \text{Po}(3)$ 이 독립일 때 $P(X + Y = 4)$ 를 다음 두 가지 방법으로 구하여라. (a) 푸아송 확률질량함수를 직접 합성곱한다. (b) $X + Y \sim \text{Po}(5)$ 임을 알아본다.

??? success "연습문제 1 풀이"
    **(a) 직접 합성곱하기.** 합은 $0 \leq b \leq 4$ 인 정수에 대하여 취한다.

    $$
    P(X + Y = 4) = \sum_{b=0}^{4} \frac{2^b}{b!} e^{-2} \cdot \frac{3^{4-b}}{(4-b)!} e^{-3}
    $$

    공통인수 $e^{-5}$ 를 밖으로 빼내고 다섯 항을 하나씩 계산한다.

    | $b$ | $P(X = b)$ | $P(Y = 4-b)$ | 곱 |
    |:---:|:---:|:---:|:---:|
    | $0$ | $e^{-2}$ | $\frac{27}{8}e^{-3}$ | $\frac{27}{8}e^{-5} \approx 0.0227$ |
    | $1$ | $2e^{-2}$ | $\frac{9}{2}e^{-3}$ | $9\,e^{-5} \approx 0.0606$ |
    | $2$ | $2e^{-2}$ | $\frac{9}{2}e^{-3}$ | $9\,e^{-5} \approx 0.0606$ |
    | $3$ | $\frac{4}{3}e^{-2}$ | $3e^{-3}$ | $4\,e^{-5} \approx 0.0270$ |
    | $4$ | $\frac{2}{3}e^{-2}$ | $e^{-3}$ | $\frac{2}{3}e^{-5} \approx 0.0045$ |

    다섯 항의 계수를 더하면 다음과 같다.

    $$
    \frac{27}{8} + 9 + 9 + 4 + \frac{2}{3} = \frac{81 + 216 + 216 + 96 + 16}{24} = \frac{625}{24}
    $$

    그러므로 다음을 얻는다.

    $$
    P(X + Y = 4) = \frac{625}{24}\, e^{-5} \approx 0.1755
    $$

    **(b) 덧셈 성질 쓰기.** 푸아송분포는 합성곱에 대하여 닫혀 있으므로 $X + Y \sim \text{Po}(2 + 3) = \text{Po}(5)$ 이다. 확률질량함수에 $a = 4$ 를 바로 넣는다.

    $$
    P(X + Y = 4) = \frac{5^4}{4!}e^{-5} = \frac{625}{24}e^{-5} \approx 0.1755
    $$

    **두 방법 견주기.** 두 답이 정확히 같은 수 $\frac{625}{24}e^{-5} \approx 0.1755$ 이다. (a)에서 (b)로 넘어가는 대수 계산의 핵심은 이 절에서 본 이항정리이다. 계수의 합 $\frac{625}{24}$ 는 $\frac{1}{4!}\sum_{b=0}^{4}\binom{4}{b}2^b 3^{4-b} = \frac{(2+3)^4}{4!} = \frac{625}{24}$ 로 다시 적을 수 있다. 다섯 항을 일일이 더하는 대신 비율을 더해서 $\text{Po}(5)$ 를 쓰는 쪽이 언제나 훨씬 빠르다. $\square$
