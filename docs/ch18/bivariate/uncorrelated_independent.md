# 무상관이면 독립이다(정규분포의 경우)

## 개요

일반적으로 상관계수가 $0$ 이라고 해서 독립인 것은 **아니다**. 그러나 이변량정규분포에서는 상관계수가 $0$ 이면 **정말로** 독립이다. 이는 특별하고도 중요한 성질이다. 이 함의가 언제 성립하고 언제 무너지는지를 아는 것은 통계를 쓰는 데 꼭 필요하다.

---

## 전체 그림

$$
\text{독립} \implies \text{Cov}(X, Y) = 0 \qquad \text{(언제나 참)}
$$

$$
\text{Cov}(X, Y) = 0 \;\not\!\!\!\implies \text{독립} \qquad \text{(일반적으로)}
$$

$$
(X, Y)^T \text{ 가 이변량정규분포},\; \text{Cov}(X, Y) = 0 \implies \text{독립} \qquad \text{(특별한 경우!)}
$$

---

## 이변량정규분포에서는 왜 성립하는가

$\rho = 0$ 이면 이변량정규분포의 밀도함수가 다음과 같이 인수분해된다.

$$
f(x, y) = \frac{1}{2\pi\sigma_X\sigma_Y} \exp\left(-\frac{\tilde{x}^2 + \tilde{y}^2}{2}\right) = f_X(x) \cdot f_Y(y)
$$

결합밀도함수가 주변밀도함수의 곱으로 쪼개지는 것이 바로 독립의 **정의**이다. 핵심은 $\rho = 0$ 일 때 지수부에 교차항 $\tilde{x}\tilde{y}$ 가 없다는 데 있다.

---

## 흔한 오해

다음은 **틀린** 서술이다.

> "$X$ 와 $Y$ 가 정규분포를 따르고 $\text{Cov}(X, Y) = 0$ 이므로 $X$ 와 $Y$ 는 독립이다."

$X$ 와 $Y$ 가 각각 정규분포를 따른다는 것이 $(X, Y)^T$ 가 이변량정규분포라는 뜻은 아니기에 이 말은 옳지 않다. 올바른 서술이 되려면 $X$ 와 $Y$ 가 **함께** 이변량정규분포를 따라야 한다.

---

## 반례: 주변분포는 정규분포이지만 결합분포는 아닌 경우

다음은 주변분포가 정규분포이고 무상관인 두 확률변수가 그럼에도 종속일 수 있음을 보여 주는 고전적인 반례이다.

**만드는 법.** $X \sim N(0, 1)$ 이라고 하자. $X$ 와 상관없이 공정한 동전을 던져 앞면이면 $S = +1$, 뒷면이면 $S = -1$ 이라고 하자. 그리고 다음과 같이 정의한다.

$$
Y = S \cdot X
$$

**주장 1: $Y$ 는 표준정규분포를 따른다.**

$$
P(Y \leq y) = P(S = 1)P(X \leq y) + P(S = -1)P(X \geq -y)
$$

$$
= \frac{1}{2}\int_{-\infty}^y \frac{1}{\sqrt{2\pi}} e^{-s^2/2}\,ds + \frac{1}{2}\int_{-y}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-s^2/2}\,ds
$$

표준정규분포의 대칭성에 따라 $P(X \geq -y) = P(X \leq y)$ 이므로 다음을 얻는다.

$$
P(Y \leq y) = P(X \leq y)
$$

따라서 $Y \sim N(0, 1)$ 이다.

**주장 2: $\text{Cov}(X, Y) = 0$ 이다.**

$$
E[XY] = P(S = 1) \cdot E[XY \mid S = 1] + P(S = -1) \cdot E[XY \mid S = -1]
$$

$$
= \frac{1}{2}E[X^2] + \frac{1}{2}E[-X^2] = \frac{1}{2}(1) - \frac{1}{2}(1) = 0
$$

$E[X] = E[Y] = 0$ 이므로

$$
\text{Cov}(X, Y) = E[XY] - E[X]E[Y] = 0 - 0 = 0
$$

이다.

**주장 3: $X$ 와 $Y$ 는 독립이 아니다.**

만드는 방식에서 알 수 있듯이 $X = 2$ 이면 $Y$ 는 $2$ 이거나 $-2$ 이다. 특히 다음이 성립한다.

$$
P(|Y| = |X|) = 1
$$

$X$ 와 $Y$ 가 독립이라면 둘 다 연속확률변수이므로 $P(|Y| = |X|) = 0$ 이어야 한다. 따라서 $X$ 와 $Y$ 는 종속이다.

**이것이 정리와 어긋나지 않는 까닭.** $X$ 와 $Y$ 는 각각 $N(0, 1)$ 을 따르지만 벡터 $(X, Y)^T$ 는 이변량정규분포가 **아니다**. 결합분포는 두 직선 $y = x$ 와 $y = -x$ 위에 확률을 모두(각각 $1/2$ 씩) 얹어 놓은 것이며, 이는 이변량정규분포가 아니다.

---

## 파이썬: 반례 확인하기

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n = 10_000

# 반례를 만든다
X = np.random.randn(n)
S = np.random.choice([-1, 1], size=n)
Y = S * X

# 성질을 확인한다
print(f"Correlation(X, Y) = {np.corrcoef(X, Y)[0, 1]:.6f}")
print(f"E[X] = {X.mean():.4f}, E[Y] = {Y.mean():.4f}")
print(f"Var(X) = {X.var():.4f}, Var(Y) = {Y.var():.4f}")
print(f"P(|Y| = |X|) = {np.mean(np.abs(Y - np.abs(X)) < 1e-10):.4f}")

# 독립성 검사: P(X > 0, Y > 0) 과 P(X > 0) * P(Y > 0) 견주기
p_joint = np.mean((X > 0) & (Y > 0))
p_x = np.mean(X > 0)
p_y = np.mean(Y > 0)
print(f"\nP(X>0, Y>0) = {p_joint:.4f}")
print(f"P(X>0) * P(Y>0) = {p_x * p_y:.4f}")
print(f"If independent these should be equal — they're not!")

# 그림으로 보기
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# 산점도
axes[0].scatter(X[:2000], Y[:2000], s=2, alpha=0.3)
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')
axes[0].set_title(f'X vs Y (ρ = {np.corrcoef(X, Y)[0, 1]:.3f})')
axes[0].set_aspect('equal')

# X 의 주변분포
axes[1].hist(X, bins=60, density=True, alpha=0.6, label='X')
axes[1].hist(Y, bins=60, density=True, alpha=0.6, label='Y')
x_grid = np.linspace(-4, 4, 200)
axes[1].plot(x_grid, 1/np.sqrt(2*np.pi) * np.exp(-x_grid**2/2),
             'k--', label='N(0,1)')
axes[1].set_title('Marginals: Both N(0,1)')
axes[1].legend()

# 종속임을 보여 주는 증거: |Y| 와 |X|
axes[2].scatter(np.abs(X[:2000]), np.abs(Y[:2000]), s=2, alpha=0.3)
axes[2].plot([0, 4], [0, 4], 'r--', linewidth=2, label='|Y| = |X|')
axes[2].set_xlabel('|X|')
axes[2].set_ylabel('|Y|')
axes[2].set_title('Dependence: |Y| = |X| always')
axes[2].legend()

plt.tight_layout()
plt.show()
```

---

## 요약 표

| 조건 | 독립인가? |
|:---|:---:|
| $X \perp Y$ | 언제나 $\implies \text{Cov}(X, Y) = 0$ |
| $\text{Cov}(X, Y) = 0$ | 일반적으로는 충분하지 않음 |
| $X, Y$ 가 각각 정규분포, $\text{Cov}(X, Y) = 0$ | **충분하지 않음** |
| $(X, Y)^T$ 가 이변량정규분포, $\text{Cov}(X, Y) = 0$ | **충분함** ✓ |

---

## 핵심 정리

- 이변량정규분포에서는 무상관과 독립이 $\iff$ 관계이다. 이는 대부분의 분포에서는 성립하지 않는 특별한 성질이다.
- 결정적인 조건은 $X$ 와 $Y$ 가 각각 정규분포를 따르는 것이 아니라 $(X, Y)^T$ 가 **함께** 이변량정규분포를 따르는 것이다.
- 고전적인 반례($S$ 가 무작위 부호일 때 $Y = SX$)는 두 표준정규확률변수가 무상관이면서도 완전히 종속일 수 있음을 보여 준다.
- 실제로는 상관계수가 $0$ 이므로 독립이라고 결론짓기 전에 결합정규성을 반드시 확인해야 한다.

## 연습문제

**연습문제 1.**
$X \sim N(0, 1)$ 이고 $Y = X^2$ 이라고 하자.

**(a)** $\text{Cov}(X, Y) = 0$ 임을 보여라.

**(b)** $X$ 와 $Y$ 가 독립이 아님을 보여라.

**(c)** $(X, Y)^T$ 는 이변량정규분포를 따르는가? 그 까닭을 말하여라.

??? success "연습문제 1 풀이"
    **(a)** 표준정규분포의 대칭성에 따라 $E[XY] = E[X^3] = 0$ 이다. $E[X] = 0$ 이므로 $\text{Cov}(X, Y) = E[XY] - E[X]E[Y] = 0$ 이다.

    **(b)** $P(Y \leq 0.01 \mid X = 5) = 0$ 이지만 $P(Y \leq 0.01) > 0$ 이므로 $X$ 와 $Y$ 는 종속이다.

    **(c)** 아니다. 이변량정규분포에서는 모든 조건부분포가 정규분포이어야 하지만, $Y \mid X = x$ 는 $x^2$ 에 몰린 퇴화분포이며 정규분포가 아니다.
