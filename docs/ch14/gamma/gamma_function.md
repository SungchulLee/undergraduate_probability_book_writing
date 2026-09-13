# 감마함수

## 정의

!!! info "감마함수"
    $\alpha > 0$ 에 대하여 **감마함수**는 다음과 같이 정의된다.

    $$\Gamma(\alpha) = \int_0^\infty x^{\alpha - 1} e^{-x} \, dx$$

감마함수는 계승을 정수가 아닌 값으로 넓힌 것이며, 감마분포의 정규화 상수 구실을 한다.

## 주요 성질

### 성질 1: 점화 관계

$$\Gamma(\alpha + 1) = \alpha \, \Gamma(\alpha)$$

**증명.** $u = x^{\alpha}$, $dv = e^{-x} dx$ 로 놓고 부분적분을 한다.

$$\Gamma(\alpha + 1) = \int_0^\infty x^{(\alpha+1)-1} e^{-x} \, dx = \int_0^\infty -x^{(\alpha+1)-1} \left(e^{-x}\right)' dx$$

$$= \left[-x^{(\alpha+1)-1} e^{-x}\right]_0^\infty - \int_0^\infty \left(-x^{(\alpha+1)-1}\right)' e^{-x} \, dx = \alpha \int_0^\infty x^{\alpha - 1} e^{-x} \, dx = \alpha \, \Gamma(\alpha)$$

### 성질 2: 특별한 값

$$\Gamma(1/2) = \sqrt{\pi}, \qquad \Gamma(1) = 1, \qquad \Gamma(2) = 1$$

**$\Gamma(1/2) = \sqrt{\pi}$ 의 증명.**

$s = \sqrt{x}$ 로 치환하면 $ds = \frac{dx}{2\sqrt{x}}$ 이므로 다음을 얻는다.

$$\Gamma(1/2) = \int_0^\infty x^{-1/2} e^{-x} \, dx = 2 \int_0^\infty e^{-s^2} \, ds = \sqrt{\pi}$$

마지막 단계에는 가우스적분 $\int_0^\infty e^{-s^2} ds = \sqrt{\pi}/2$ 를 썼다. 이 적분은 정규분포를 다룰 때 나온다.

**$\Gamma(1) = 1$ 의 증명.**

$$\Gamma(1) = \int_0^\infty e^{-x} \, dx = 1$$

### 성질 3: 계승과의 연결

$$\Gamma(n + 1) = n! \quad \text{for } n = 0, 1, 2, \ldots$$

**증명.** 점화 성질을 써서 귀납법으로 보인다.

- 시작: $\Gamma(1) = 0! = 1$ ✓
- 귀납 단계: $\Gamma(n + 1) = n \cdot \Gamma(n) = n \cdot (n-1)! = n!$ ✓

### 반정수 값

점화 관계와 $\Gamma(1/2) = \sqrt{\pi}$ 를 합치면 다음을 얻는다.

$$\Gamma(3/2) = \frac{1}{2}\sqrt{\pi}, \qquad \Gamma(5/2) = \frac{3}{4}\sqrt{\pi}, \qquad \Gamma(n + 1/2) = \frac{(2n)!}{4^n \, n!} \sqrt{\pi}$$

## 정규화 상수로서의 구실

감마함수는 감마분포의 확률밀도함수를 적분한 값이 1이 되도록 해 준다. $\Gamma(\alpha, \lambda)$ 분포에 대하여 다음이 성립한다.

$$\int_0^\infty \frac{\lambda(\lambda x)^{\alpha - 1} e^{-\lambda x}}{\Gamma(\alpha)} \, dx = 1$$

$u = \lambda x$ 로 치환하면 이를 확인할 수 있다.

$$\frac{1}{\Gamma(\alpha)} \int_0^\infty u^{\alpha - 1} e^{-u} \, du = \frac{\Gamma(\alpha)}{\Gamma(\alpha)} = 1$$

## 베타함수와의 연결

**베타함수**는 감마함수와 밀접하게 이어져 있다.

$$B(\alpha, \beta) = \int_0^1 x^{\alpha - 1} (1 - x)^{\beta - 1} \, dx = \frac{\Gamma(\alpha) \, \Gamma(\beta)}{\Gamma(\alpha + \beta)}$$

이 항등식은 독립인 감마확률변수를 거치는 감마–베타 연결로 증명된다(15장의 베타분포 절을 보라).

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma, factorial
from scipy.integrate import quad

# 감마함수의 성질 확인
print("=== Gamma Function Properties ===")
print(f"Γ(1) = {gamma(1):.6f} (should be 1)")
print(f"Γ(2) = {gamma(2):.6f} (should be 1)")
print(f"Γ(1/2) = {gamma(0.5):.6f} (should be √π = {np.sqrt(np.pi):.6f})")
print(f"Γ(3/2) = {gamma(1.5):.6f} (should be √π/2 = {np.sqrt(np.pi)/2:.6f})")
print()

# 계승과의 연결 확인
for n in range(1, 8):
    print(f"Γ({n+1}) = {gamma(n+1):.1f}, {n}! = {factorial(n, exact=True)}")

# 감마함수 그리기
x = np.linspace(0.01, 5.5, 500)
y = gamma(x)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 감마함수
axes[0].plot(x, y, 'b-', lw=2)
# 정수 값 표시
for n in range(1, 6):
    axes[0].plot(n, gamma(n), 'ro', markersize=8)
    axes[0].annotate(f'Γ({n})={gamma(n):.0f}',
                     xy=(n, gamma(n)), xytext=(n+0.1, gamma(n)+1),
                     fontsize=9)
axes[0].set_title('Gamma Function Γ(α)')
axes[0].set_xlabel('α')
axes[0].set_ylabel('Γ(α)')
axes[0].set_ylim(0, 30)
axes[0].grid(True, alpha=0.3)

# 점화 관계 확인: Γ(α+1) = α·Γ(α)
alpha_vals = np.linspace(0.1, 5, 100)
lhs = gamma(alpha_vals + 1)
rhs = alpha_vals * gamma(alpha_vals)
axes[1].plot(alpha_vals, lhs, 'b-', lw=2, label='Γ(α+1)')
axes[1].plot(alpha_vals, rhs, 'r--', lw=2, label='α·Γ(α)')
axes[1].set_title('Recursion Property: Γ(α+1) = α·Γ(α)')
axes[1].set_xlabel('α')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('gamma_function.png', dpi=150, bbox_inches='tight')
plt.show()

# 적분으로 정의한 값을 수치적으로 확인
for alpha in [0.5, 1.0, 2.0, 3.0, 4.5]:
    result, _ = quad(lambda x: x**(alpha-1) * np.exp(-x), 0, np.inf)
    print(f"∫x^({alpha}-1)e^(-x)dx = {result:.6f}, Γ({alpha}) = {gamma(alpha):.6f}")
```

## 연습문제

**연습문제 1.**
다음을 계산하여라.

(a) $\Gamma(6)$

(b) $\Gamma(5/2)$

(c) $B(3, 4)$, 여기서 $B$ 는 베타함수이다.

??? success "연습문제 1 풀이"
    (a) $\Gamma(6) = 5! = 120$

    (b) $\Gamma(5/2) = \frac{3}{2} \cdot \Gamma(3/2) = \frac{3}{2} \cdot \frac{1}{2} \cdot \Gamma(1/2) = \frac{3}{4}\sqrt{\pi} \approx 1.329$

    (c) $B(3, 4) = \frac{\Gamma(3)\Gamma(4)}{\Gamma(7)} = \frac{2! \cdot 3!}{6!} = \frac{12}{720} = \frac{1}{60}$
