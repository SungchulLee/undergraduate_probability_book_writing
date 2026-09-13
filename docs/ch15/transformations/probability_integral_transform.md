# 확률적분변환

## 확률적분변환이란

!!! info "확률적분변환"
    $X$ 가 누적분포함수 $F$ 를 갖는 연속확률변수이면 다음이 성립한다.

    $$F(X) \sim U(0, 1)$$

    곧 확률변수에 자기 자신의 누적분포함수를 씌우면 언제나 표준균등분포가 나온다.

### 증명

$U = F(X)$ 라 하자. $F$ 가 연속이고 감소하지 않으므로 $0 < u < 1$ 에 대하여 다음이 성립한다.

$$P(U \leq u) = P(F(X) \leq u) = P(X \leq F^{-1}(u)) = F(F^{-1}(u)) = u$$

이것은 $U(0,1)$ 의 누적분포함수이다.

## 역변환 방법

거꾸로 가는 방향도 그에 못지않게 중요하며, 보편적인 모의실험 기법을 준다.

!!! info "역변환 방법(모의실험)"
    균등난수를 써서 누적분포함수가 $F$ 인 확률변수 $X$ 를 만들려면 다음과 같이 한다.

    **1단계.** $U \sim U(0, 1)$ 을 만든다.

    **2단계.** $X = F^{-1}(U)$ 로 놓는다.

    $F$ 가 일대일 대응이 아니면(예를 들어 이산분포의 경우) **일반화된 역함수**를 쓴다.

    $$X = \sup\{x \in \mathbb{R} : F(x) < U\}$$

### 증명

$$P(X \leq x) = P(F^{-1}(U) \leq x) = P(U \leq F(x)) = F(x)$$

따라서 $X$ 는 바라던 누적분포함수 $F$ 를 갖는다.

### 기하학적 뜻풀이

이 방법이 하는 일은 다음과 같다.

1. 높이 $U$(0과 1 사이의 무작위 값)에 가로선을 긋는다
2. 그 선이 누적분포함수 곡선 $F$ 와 만나는 곳을 찾는다
3. 그에 해당하는 $x$ 값을 읽는다

누적분포함수가 가파른 곳(밀도가 높은 곳)에서는 많은 $U$ 값이 좁은 범위의 $x$ 값으로 옮겨 가므로, 그곳에서 표본이 자연스럽게 더 많이 나온다.

## 풀이 예제: Exp(0.5) 만들기

??? example "예: 균등분포에서 지수분포 만들기"
    $U \sim U(0, 1)$ 이 주어졌다고 하자. $X \sim \text{Exp}(0.5)$ 를 만들어 보자.

    **1단계:** 누적분포함수와 그 역함수를 구한다.

    $$\bar{F}(x) = e^{-0.5x} \implies F(x) = 1 - e^{-0.5x}, \quad x \geq 0$$

    $u = 1 - e^{-0.5x}$ 로 놓고 $x$ 에 대하여 풀면 다음을 얻는다.

    $$X = F^{-1}(U) = -2\log(1 - U) \sim \text{Exp}(0.5)$$

    **2단계:** 대칭성을 써서 간단히 한다.

    $U \sim U(0,1)$ 이면 $1 - U \sim U(0,1)$ 이므로 다음이 성립한다.

    $$X = -2\log(U) \sim \text{Exp}(0.5)$$

## 일반적인 지수분포의 모의실험

어떤 $X \sim \text{Exp}(\lambda)$ 에 대해서도 다음이 성립한다.

$$X = -\frac{1}{\lambda}\log(U) \sim \text{Exp}(\lambda)$$

이것은 가장 널리 쓰이는 모의실험 공식 가운데 하나이다.

## 역누적분포함수가 닫힌 꼴이 아닐 때

$F^{-1}$ 을 닫힌 꼴로 적을 수 없는 분포(예를 들어 정규분포나 모양모수가 정수가 아닌 감마분포)에 대해서는 다른 방법을 쓴다.

- **수치적 역변환:** 근 찾기로 $F(x) = u$ 를 푼다
- **기각 표집:** 후보를 만들어 걸러 낸다
- **박스–뮐러 변환:** 정규분포에 특화된 방법이다
- **합성 방법:** 더 간단한 분포들로 쪼갠다

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 10000

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Exp(0.5) 에 대한 역변환 방법 보이기
lam = 0.5
U = np.random.uniform(0, 1, n_sim)
X_sim = -np.log(U) / lam  # 역누적분포함수 방법

x_vals = np.linspace(0, 10, 200)
pdf_theory = lam * np.exp(-lam * x_vals)

axes[0].hist(X_sim, bins=60, density=True, alpha=0.5, color='steelblue',
             label='Simulated via F⁻¹(U)')
axes[0].plot(x_vals, pdf_theory, 'r-', lw=2, label='Exp(0.5) PDF')
axes[0].set_title('Inverse Transform: Exp(0.5)')
axes[0].set_xlabel('x')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# 기하학적 뜻풀이 그리기
cdf_vals = 1 - np.exp(-lam * x_vals)
axes[1].plot(x_vals, cdf_vals, 'b-', lw=2, label='CDF F(x)')

# 몇 개의 표본이 어떻게 옮겨 가는지 보인다
for u_val in [0.1, 0.3, 0.5, 0.7, 0.9]:
    x_val = -np.log(1 - u_val) / lam
    axes[1].plot([0, x_val], [u_val, u_val], 'r--', alpha=0.5)
    axes[1].plot([x_val, x_val], [0, u_val], 'r--', alpha=0.5)
    axes[1].plot(x_val, u_val, 'ro', markersize=5)

axes[1].set_title('Geometric Interpretation')
axes[1].set_xlabel('x')
axes[1].set_ylabel('F(x) / U')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# 확률적분변환: F(X) ~ U(0,1)
X_exp = np.random.exponential(1/lam, n_sim)
U_transform = 1 - np.exp(-lam * X_exp)  # F(X)

axes[2].hist(U_transform, bins=50, density=True, alpha=0.7,
             color='orange', label='F(X)')
axes[2].axhline(1.0, color='black', lw=2, linestyle='--',
                label='U(0,1) PDF')
axes[2].set_title('F(X) ~ U(0,1)')
axes[2].set_xlabel('u')
axes[2].set_ylabel('Density')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('probability_integral_transform.png', dpi=150, bbox_inches='tight')
plt.show()

# 확인: 역누적분포함수 방법과 scipy 를 견준다
X_scipy = np.random.exponential(1/lam, n_sim)
print(f"Inverse CDF method: mean={np.mean(X_sim):.4f}, var={np.var(X_sim):.4f}")
print(f"Direct sampling:    mean={np.mean(X_scipy):.4f}, var={np.var(X_scipy):.4f}")
print(f"Theory:             mean={1/lam:.4f}, var={1/lam**2:.4f}")
```

## 연습문제

**연습문제 1.**
$X$ 의 누적분포함수가 $x > 0$ 에 대하여 $F(x) = 1 - e^{-x^2}$ 이라 하자. $F(X) \sim U(0, 1)$ 임을 보여라.

??? success "연습문제 1 풀이"
    $0 < u < 1$ 에 대하여 다음이 성립한다.

    $$P(F(X) \leq u) = P(X \leq F^{-1}(u))= F(F^{-1}(u)) = u$$

    이것은 $U(0, 1)$ 의 누적분포함수이다. 이 결과는 연속인 어떤 누적분포함수 $F$ 에 대해서도 성립한다.
