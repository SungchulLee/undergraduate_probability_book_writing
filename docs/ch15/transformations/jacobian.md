# 결합변환의 야코비 방법

## 야코비 변환 공식

연속확률변수의 짝 $(X, Y)$ 를 일대일 대응으로 새로운 짝 $(U, V)$ 로 옮길 때, 결합 확률밀도함수는 **야코비 공식**에 따라 변한다.

!!! info "야코비 방법(두 변수)"
    $(U, V) = g(X, Y)$ 가 일대일 대응인 변환이고 그 역이 $x = x(u, v)$, $y = y(u, v)$ 이면 다음이 성립한다.

    $$f_{U,V}(u, v) = f_{X,Y}(x, y) \left|\frac{\partial(x, y)}{\partial(u, v)}\right|$$

    여기서 **야코비 행렬식**은 다음과 같다.

    $$\left|\frac{\partial(x, y)}{\partial(u, v)}\right| = \left|\det \begin{pmatrix} \dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v} \\[8pt] \dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v} \end{pmatrix}\right|$$

## 기하학적 직관

야코비안은 변환이 넓이를 얼마나 일그러뜨리는지를 셈해 준다.

- $(u, v)$ 공간의 작은 직사각형 $du \times dv$ 가 $(x, y)$ 공간의 평행사변형으로 옮겨 간다
- 그 평행사변형의 넓이는 $\left|\frac{\partial(x,y)}{\partial(u,v)}\right| du \, dv$ 이다
- 확률 = 밀도 × 넓이 이므로 밀도는 다음을 만족해야 한다

$$f_{U,V}(u, v) \, du \, dv = f_{X,Y}(x, y) \left|\frac{\partial(x, y)}{\partial(u, v)}\right| du \, dv$$

따라서 $f_{U,V}(u, v) = f_{X,Y}(x, y) \left|\frac{\partial(x, y)}{\partial(u, v)}\right|$ 이다.

## 역야코비안 성질

야코비안은 어느 방향으로든 계산할 수 있다.

$$\left|\frac{\partial(x, y)}{\partial(u, v)}\right| = \frac{1}{\left|\dfrac{\partial(u, v)}{\partial(x, y)}\right|}$$

"앞 방향" 야코비안 $\frac{\partial(u,v)}{\partial(x,y)}$ 를 구한 뒤 역수를 취하는 편이 쉬울 때가 많다.

## 일반적인 n차원의 경우

!!! info "야코비 방법(n차원)"
    일대일 대응인 변환 $(Y_1, \ldots, Y_n) = g(X_1, \ldots, X_n)$ 에 대하여 다음이 성립한다.

    $$f_{Y_1,\ldots,Y_n}(y_1, \ldots, y_n) = f_{X_1,\ldots,X_n}(x_1, \ldots, x_n) \left|\frac{\partial(x_1, \ldots, x_n)}{\partial(y_1, \ldots, y_n)}\right|$$

    여기서

    $$\left|\frac{\partial(x_1, \ldots, x_n)}{\partial(y_1, \ldots, y_n)}\right| = \left|\det \begin{pmatrix} \dfrac{\partial x_1}{\partial y_1} & \cdots & \dfrac{\partial x_1}{\partial y_n} \\ \vdots & \ddots & \vdots \\ \dfrac{\partial x_n}{\partial y_1} & \cdots & \dfrac{\partial x_n}{\partial y_n} \end{pmatrix}\right|$$

    이다.

## 중요한 응용: 감마분포에서 베타분포 유도하기

이 장에서 가장 중요한 응용은 독립인 두 감마확률변수에서 베타분포를 이끌어 내는 것이다(자세한 유도는 베타분포 절을 보라).

$X \sim \Gamma(\alpha, \lambda)$ 와 $Y \sim \Gamma(\beta, \lambda)$ 가 독립일 때 $T = X + Y$, $F = X/(X+Y)$ 로 놓자. 변환은 $x = tf$, $y = t(1-f)$ 이고 다음이 성립한다.

$$\frac{\partial(t, f)}{\partial(x, y)} = \det \begin{pmatrix} 1 & 1 \\ \frac{t - x}{t^2} & -\frac{x}{t^2} \end{pmatrix} = -\frac{1}{t}$$

따라서 $\left|\frac{\partial(x,y)}{\partial(t,f)}\right| = t$ 이고, 이로부터 곱으로 갈라지는 결합밀도를 얻어 $F \sim \text{Beta}(\alpha, \beta)$ 와 $T$, $F$ 의 독립성이 증명된다.

## 정리하며: 누적분포함수 방법과 야코비 방법

| 방법 | 언제 쓰는가 | 장점 |
|:---|:---|:---|
| **누적분포함수 방법** | 언제나 통한다 | 단조가 아닌 변환도 다룰 수 있다 |
| **야코비안(1차원)** | $Y = g(X)$ 이고 $g$ 가 단조일 때 | 공식이 바로 있고 적분이 필요 없다 |
| **야코비안(2차원 이상)** | 일대일 대응인 결합변환일 때 | 결합밀도를 체계적으로 다룰 수 있다 |

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 100000

# 야코비 변환 보이기: (X,Y) -> (T,F)
# X ~ Gamma(2, 1), Y ~ Gamma(3, 1) 이고 서로 독립
alpha, beta_param = 2, 3
lam = 1.0

X = np.random.gamma(alpha, 1/lam, n_sim)
Y = np.random.gamma(beta_param, 1/lam, n_sim)

T = X + Y        # Gamma(alpha+beta, lambda) 가 되어야 한다
F = X / (X + Y)  # Beta(alpha, beta) 가 되어야 한다

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 결합 산점도: (X, Y)
axes[0, 0].scatter(X[:2000], Y[:2000], s=1, alpha=0.3)
axes[0, 0].set_title('Original: (X, Y)')
axes[0, 0].set_xlabel('X ~ Γ(2,1)')
axes[0, 0].set_ylabel('Y ~ Γ(3,1)')
axes[0, 0].grid(True, alpha=0.3)

# 결합 산점도: (T, F)
axes[0, 1].scatter(T[:2000], F[:2000], s=1, alpha=0.3, color='red')
axes[0, 1].set_title('Transformed: (T, F)')
axes[0, 1].set_xlabel('T = X+Y ~ Γ(5,1)')
axes[0, 1].set_ylabel('F = X/(X+Y) ~ Beta(2,3)')
axes[0, 1].grid(True, alpha=0.3)

# T 의 주변분포
t_vals = np.linspace(0, 15, 200)
axes[1, 0].hist(T, bins=60, density=True, alpha=0.5, color='steelblue')
axes[1, 0].plot(t_vals, stats.gamma.pdf(t_vals, a=alpha+beta_param, scale=1/lam),
                'r-', lw=2, label=f'Γ({alpha+beta_param},{lam}) PDF')
axes[1, 0].set_title(f'T = X+Y ~ Γ({alpha+beta_param},{lam})')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# F 의 주변분포
f_vals = np.linspace(0.01, 0.99, 200)
axes[1, 1].hist(F, bins=60, density=True, alpha=0.5, color='orange')
axes[1, 1].plot(f_vals, stats.beta.pdf(f_vals, alpha, beta_param),
                'r-', lw=2, label=f'Beta({alpha},{beta_param}) PDF')
axes[1, 1].set_title(f'F = X/(X+Y) ~ Beta({alpha},{beta_param})')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('jacobian_method.png', dpi=150, bbox_inches='tight')
plt.show()

# T 와 F 의 독립성 확인
print(f"Corr(T, F) = {np.corrcoef(T, F)[0,1]:.6f} (should be ≈ 0)")
```

## 연습문제

**연습문제 1.** $(X, Y)$ 가 i.i.d. $\text{Exp}(1)$ 이라 하자. 야코비 방법으로 $U = X + Y$ 와 $V = X/(X+Y)$ 의 결합 확률밀도함수를 구하여라.

??? success "연습문제 1 풀이"
    역변환: $X = UV$, $Y = U(1-V)$ 이다. 야코비안은 다음과 같다.

    $$
    J = \det\begin{pmatrix} V & U \\ 1-V & -U \end{pmatrix} = -UV - U(1-V) = -U
    $$

    따라서 $|J| = U$ 이다. 결합 확률밀도함수는 $u > 0$, $0 < v < 1$ 에 대하여 $f_{U,V}(u,v) = e^{-uv} \cdot e^{-u(1-v)} \cdot u = ue^{-u}$ 이다.

    이것이 $f_U(u) \cdot f_V(v) = ue^{-u} \cdot 1$ 로 갈라지므로 $U \sim \text{Gamma}(2,1)$ 과 $V \sim \text{Uniform}(0,1)$ 이 독립임을 알 수 있다.

---

**연습문제 2.** $X \sim N(0,1)$ 과 $Y \sim N(0,1)$ 이 독립이라 하자. 극좌표 $R = \sqrt{X^2 + Y^2}$ 와 $\Theta = \arctan(Y/X)$ 로 변환할 때 야코비안 $|\partial(x,y)/\partial(r,\theta)|$ 를 구하여라.

??? success "연습문제 2 풀이"
    $x = r\cos\theta$, $y = r\sin\theta$ 이다.

    $$
    J = \det\begin{pmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{pmatrix} = r\cos^2\theta + r\sin^2\theta = r
    $$

    따라서 $|J| = r$ 이다.

---

**연습문제 3.** $(X, Y)$ 의 결합 확률밀도함수가 단위 정사각형 $[0,1]^2$ 위에서 $f(x,y) = 1$ 이라 하자. 누적분포함수 방법이나 야코비 방법으로 $U = X + Y$ 의 확률밀도함수를 구하여라.

??? success "연습문제 3 풀이"
    $U = X + Y$, $V = X$ 로 놓자. 역변환은 $X = V$, $Y = U - V$ 이고 야코비안 $= 1$ 이다. $(U,V)$ 의 결합 확률밀도함수는 $0 < v < 1$, $0 < u - v < 1$, 곧 $\max(0, u-1) < v < \min(1, u)$ 에 대하여 $f_{U,V}(u,v) = 1$ 이다.

    $U$ 의 주변분포: $f_U(u) = \int_{\max(0,u-1)}^{\min(1,u)} 1\,dv$ 이다.

    $0 < u \leq 1$ 이면 $f_U(u) = u$ 이고, $1 < u < 2$ 이면 $f_U(u) = 2 - u$ 이다. 이것은 $(0, 2)$ 위의 삼각분포이다.

---

**연습문제 4.** $(X, Y)$ 가 i.i.d. $\text{Uniform}(0,1)$ 이라 하자. $U = XY$, $V = X$ 로 치환하여 $W = XY$ 의 확률밀도함수를 구하여라.

??? success "연습문제 4 풀이"
    역변환: $X = V$, $Y = U/V$ 이다. 야코비안은 $|J| = 1/V$ 이다. 영역은 $0 < V < 1$, $0 < U/V < 1$ 이므로 $U < V < 1$ 이다.

    $u < v < 1$ 에 대하여 $f_{U,V}(u,v) = 1 \cdot (1/v)$ 이다.

    $$
    f_W(w) = \int_w^1 \frac{1}{v}\,dv = -\ln w, \quad 0 < w < 1
    $$

---

**연습문제 5.** 변환 방법이 통하려면 받침(support) 전체에서 야코비안이 0이 아니어야 하는 까닭을 설명하여라. 야코비안이 사라지면 기하학적으로 어떤 일이 일어나는가?

??? success "연습문제 5 풀이"
    야코비안 $|J|$ 는 변환이 국소적으로 부피를 얼마나 늘이거나 줄이는지를 나타내는 인수이다. $|J| = 0$ 인 곳에서는 변환이 $(u,v)$ 공간에서 넓이가 양수인 영역을 $(x,y)$ 공간의 더 낮은 차원의 집합(예를 들어 곡선이나 점)으로 뭉갠다. 그곳에서는 역변환이 제대로 정의되지 않으므로 일대일이라는 요건이 깨진다. 기하학적으로는 한없이 작은 직사각형이 넓이 0으로 "짓눌리므로" 밀도 공식 $f_{U,V} = f_{X,Y} |J|$ 가 $0/0$(부정형)이 되거나 무한대가 된다. 표준적인 야코비 방법은 일대일 대응을 요구하므로, 변환이 전체에서 일대일이 아니라면 받침을 일대일이 되는 영역들로 쪼개어 다루어야 한다.
