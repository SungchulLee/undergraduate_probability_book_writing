# 변수변환(한 변수)

## 확률밀도함수를 구하는 두 가지 방법

확률밀도함수 $f_X(x)$ 를 아는 확률변수 $X$ 와 변환 $Y = g(X)$ 가 주어졌을 때, $Y$ 의 확률밀도함수를 구하는 체계적인 방법이 두 가지 있다.

## 방법 1: 누적분포함수 방법

!!! info "누적분포함수 방법"

    1. $F_Y(y) = P(Y \leq y) = P(g(X) \leq y)$ 를 구한다
    2. 이를 $P(X \leq \cdot)$ 이나 $P(X \geq \cdot)$ 의 꼴로 나타낸다
    3. 미분한다: $f_Y(y) = F_Y'(y)$

이 방법은 완전히 일반적이어서 단조가 아닌 변환을 포함한 어떤 변환에도 통한다.

## 방법 2: 야코비 방법

!!! info "야코비 방법(한 변수)"
    $Y = g(X)$ 에서 $g$ 가 **단조이고 미분가능한** 함수이며 역함수가 $x = g^{-1}(y)$ 이면 다음이 성립한다.

    $$f_Y(y) = f_X(x) \left|\frac{dx}{dy}\right|$$

    여기서 $x = g^{-1}(y)$ 이다.

절댓값은 $g$ 가 증가하든 감소하든 확률밀도함수가 음이 되지 않도록 해 준다. 인수 $|dx/dy|$ 는 변환이 밀도를 얼마나 늘이거나 누르는지를 셈해 준다.

### 직관적인 근거

$g$ 가 증가함수이면 $P(Y \leq y) = P(X \leq x)$ 이므로 다음이 성립한다.

$$f_Y(y) = f_X(x) \frac{dx}{dy}$$

$g$ 가 감소함수이면 $P(Y \leq y) = P(X \geq x)$ 이므로 음의 부호가 붙는데, 이는 절댓값이 흡수한다.

### 두 방법 사이의 관계

야코비 방법은 누적분포함수 방법에서 나온 지름길이다. 연쇄법칙을 쓰면 다음과 같다.

$$F_Y(y) = P(X \leq g^{-1}(y)) \implies f_Y(y) = f_X(g^{-1}(y)) \cdot \frac{d}{dy}g^{-1}(y) = f_X(x)\left|\frac{dx}{dy}\right|$$

### 역수 성질

야코비안은 어느 쪽으로든 계산할 수 있다.

$$\left|\frac{dx}{dy}\right| = \frac{1}{\left|\dfrac{dy}{dx}\right|}$$

$dx/dy$ 를 바로 구하는 것보다 $dy/dx$ 를 구하는 편이 쉬울 때 흔히 이 꼴을 쓴다.

## 풀이 예제: X ~ U(0, 1) 일 때 Y = X³

??? example "예: 균등확률변수의 세제곱"
    $X \sim U(0,1)$ 이고 $Y = X^3$ 이라 하자. $0 < y < 1$ 에서 $f_Y(y)$ 를 구하여라.

    **방법 1: 누적분포함수**

    $$P(Y \leq y) = P(X^3 \leq y) = P(X \leq y^{1/3}) = y^{1/3}$$

    미분하면 다음을 얻는다.

    $$f_Y(y) = \frac{1}{3} y^{-2/3}, \quad 0 < y < 1$$

    **방법 2: 야코비안**

    $y = x^3$ 이므로 $x = y^{1/3}$ 이다.

    $$\frac{dy}{dx} = 3x^2 = 3(x^3)^{2/3} = 3y^{2/3}$$

    $$\left|\frac{dx}{dy}\right| = \frac{1}{3y^{2/3}} = \frac{1}{3}y^{-2/3}$$

    따라서 다음을 얻는다.

    $$f_Y(y) = f_X(x) \left|\frac{dx}{dy}\right| = 1 \cdot \frac{1}{3}y^{-2/3} = \frac{1}{3}y^{-2/3}, \quad 0 < y < 1$$

    두 방법의 답이 일치한다. 세제곱 함수가 $0$ 근처의 값을 누르고 $1$ 근처의 값을 늘이므로 밀도가 $y = 0$ 근처에 모인다.

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 100000

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# X ~ U(0,1) 일 때 Y = X^3
X = np.random.uniform(0, 1, n_sim)
Y = X ** 3

y_vals = np.linspace(0.01, 0.99, 200)
pdf_theory = (1/3) * y_vals ** (-2/3)

axes[0].hist(Y, bins=80, density=True, alpha=0.5, color='steelblue',
             label='Y = X³ simulated')
axes[0].plot(y_vals, pdf_theory, 'r-', lw=2,
             label=r'$f_Y(y) = \frac{1}{3}y^{-2/3}$')
axes[0].set_title('Y = X³ where X ~ U(0,1)')
axes[0].set_xlabel('y')
axes[0].set_ylabel('Density')
axes[0].set_ylim(0, 5)
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# 누적분포함수 비교
y_grid = np.linspace(0, 1, 200)
cdf_empirical = np.array([np.mean(Y <= y) for y in y_grid])
cdf_theory = y_grid ** (1/3)

axes[1].plot(y_grid, cdf_empirical, 'b-', lw=2, alpha=0.7,
             label='Empirical CDF')
axes[1].plot(y_grid, cdf_theory, 'r--', lw=2,
             label=r'$F_Y(y) = y^{1/3}$')
axes[1].set_title('CDF of Y = X³')
axes[1].set_xlabel('y')
axes[1].set_ylabel('F(y)')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('change_of_variables.png', dpi=150, bbox_inches='tight')
plt.show()
```


## 연습문제

**연습문제 1.**
$X \sim \text{Exp}(1)$ 이고 $Y = \sqrt{X}$ 라 하자. $Y$ 의 확률밀도함수를 구하여라.

??? success "연습문제 1 풀이"
    **누적분포함수 방법:** $y > 0$ 에 대하여 $F_Y(y) = P(\sqrt{X} \leq y) = P(X \leq y^2) = 1 - e^{-y^2}$ 이다.

    따라서 $y > 0$ 에 대하여 $f_Y(y) = 2y\, e^{-y^2}$ 이다.

    이것은 **레일리분포**이다(같은 말로 모양모수가 2인 와이블분포이다).
