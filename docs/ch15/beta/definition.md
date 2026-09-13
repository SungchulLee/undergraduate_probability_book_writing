# 베타분포의 정의

## 베타함수

!!! info "베타함수"
    $\alpha > 0$ 과 $\beta > 0$ 에 대하여 **베타함수**는 다음과 같다.

    $$B(\alpha, \beta) = \int_0^1 x^{\alpha - 1}(1 - x)^{\beta - 1} \, dx$$

    감마함수와는 다음 관계로 이어져 있다.

    $$B(\alpha, \beta) = \frac{\Gamma(\alpha)\,\Gamma(\beta)}{\Gamma(\alpha + \beta)}$$

## 정의

!!! info "베타분포"
    연속확률변수 $X$ 의 확률밀도함수가 다음과 같으면, $X$ 는 모수가 $\alpha > 0$ 과 $\beta > 0$ 인 **베타분포**를 따른다고 하고 $X \sim \text{Beta}(\alpha, \beta)$ 로 적는다.

    $$f(x) = \frac{x^{\alpha - 1}(1 - x)^{\beta - 1}}{B(\alpha, \beta)}, \quad 0 < x < 1$$

    확률밀도함수가 $x^{\alpha-1}(1-x)^{\beta-1}$ 에 비례하므로 같은 말로 다음과 같이 적을 수 있다.

    $$f(x) \propto x^{\alpha - 1}(1 - x)^{\beta - 1}$$

    여기서 베타함수 $B(\alpha, \beta)$ 는 확률밀도함수의 적분이 1이 되도록 해 주는 정규화 상수이다.

## 평균과 분산

!!! info "Beta(α, β) 의 적률"

    $$E[X] = \frac{\alpha}{\alpha + \beta}, \qquad \text{Var}(X) = \frac{\alpha\beta}{(\alpha + \beta)^2(\alpha + \beta + 1)}$$

평균 $\frac{\alpha}{\alpha + \beta}$ 는 전체 $\alpha + \beta$ 에 대한 $\alpha$ 의 비이며, "몫"이나 "비율"로 자연스럽게 읽을 수 있다.

## 직관: 대기시간 가운데 차지하는 몫

베타분포는 감마분포에서 자연스럽게 나온다. $X \sim \Gamma(\alpha, \lambda)$ 와 $Y \sim \Gamma(\beta, \lambda)$ 가 **독립**이면 다음이 성립한다.

1. 전체 $T = X + Y \sim \Gamma(\alpha + \beta, \lambda)$ 이다
2. 몫 $F = \dfrac{X}{X + Y} \sim \text{Beta}(\alpha, \beta)$ 이다
3. $T$ 와 $F$ 는 **독립**이다
4. 베타함수의 항등식 $B(\alpha, \beta) = \dfrac{\Gamma(\alpha)\,\Gamma(\beta)}{\Gamma(\alpha + \beta)}$ 가 덤으로 따라 나온다

### 야코비 방법을 이용한 증명

$X \sim \Gamma(\alpha, \lambda)$ 와 $Y \sim \Gamma(\beta, \lambda)$ 가 독립이라 하자. 다음과 같이 놓는다.

$$t = x + y, \qquad f = \frac{x}{x + y}$$

그러면 $x = tf$ 이고 $y = t(1-f)$ 이다.

**야코비안 계산:**

$$\frac{\partial(t, f)}{\partial(x, y)} = \det \begin{pmatrix} 1 & 1 \\ \frac{t - x}{t^2} & -\frac{x}{t^2} \end{pmatrix} = -\frac{1}{t}$$

따라서 $\left|\frac{\partial(x, y)}{\partial(t, f)}\right| = t$ 이다.

**결합밀도의 변환:**

$$f_{T,F}(t, f) = f_{X,Y}(x, y) \left|\frac{\partial(x, y)}{\partial(t, f)}\right|$$

$$= \frac{\lambda(\lambda x)^{\alpha-1} e^{-\lambda x}}{\Gamma(\alpha)} \cdot \frac{\lambda(\lambda y)^{\beta-1} e^{-\lambda y}}{\Gamma(\beta)} \cdot t$$

$x = tf$, $y = t(1-f)$ 를 대입하고 간단히 하면 다음을 얻는다.

$$f_{T,F}(t, f) = \underbrace{\frac{f^{\alpha-1}(1-f)^{\beta-1}}{\Gamma(\alpha)\Gamma(\beta)/\Gamma(\alpha+\beta)}}_{f \text{ 만의 함수}} \cdot \underbrace{\frac{\lambda(\lambda t)^{(\alpha+\beta)-1} e^{-\lambda t}}{\Gamma(\alpha + \beta)}}_{t \text{ 만의 함수}}$$

$$= \underbrace{\frac{f^{\alpha-1}(1-f)^{\beta-1}}{B(\alpha, \beta)}}_{\text{Beta}(\alpha, \beta) \text{ 의 확률밀도함수}} \cdot \underbrace{\frac{\lambda(\lambda t)^{(\alpha+\beta)-1} e^{-\lambda t}}{\Gamma(\alpha + \beta)}}_{\Gamma(\alpha+\beta, \lambda) \text{ 의 확률밀도함수}}$$

결합 확률밀도함수가 $f$ 만의 함수와 $t$ 만의 함수의 곱으로 갈라지므로 $T$ 와 $F$ 는 **독립**이고, 다음이 성립한다.

- $F \sim \text{Beta}(\alpha, \beta)$
- $T \sim \Gamma(\alpha + \beta, \lambda)$

덤으로 정규화 상수를 견주면 $B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha + \beta)}$ 를 얻는다.

## 특별한 경우

| 모수 | 분포 | 모양 |
|:---:|:---:|:---|
| $\text{Beta}(1, 1)$ | $U(0, 1)$ | 평평하다(균등) |
| $\text{Beta}(\alpha, \alpha)$ | 대칭 | $1/2$ 에 대하여 대칭 |
| $\text{Beta}(1, \beta)$ | — | 감소하며 $0$ 근처에 모인다 |
| $\text{Beta}(\alpha, 1)$ | — | 증가하며 $1$ 근처에 모인다 |
| $\alpha, \beta > 1$ | — | 봉우리가 하나인 종 모양 |
| $\alpha, \beta < 1$ | — | U자 모양으로 양 끝에 모인다 |

## 풀이 예제: 은행에서 보낸 대기시간의 몫

??? example "예: 은행과 우체국"
    어떤 은행에 들어갔더니 앞에 한 사람이 줄을 서 있고 창구는 5개이며, 각 창구의 처리 시간은 i.i.d. $\text{Exp}(\lambda_B)$ 로 $\lambda_B^{-1} = 10$ 분이다. 은행을 나온 뒤에는 우체국에 들르는데, 그곳에는 앞에 두 사람이 줄을 서 있고 창구는 2개이며 처리 시간은 i.i.d. $\text{Exp}(\lambda_P)$ 로 $\lambda_P^{-1} = 4$ 분이다.

    전체 대기시간 가운데 은행에서 보낸 시간의 비율을 $F$ 라 하자. $E[F]$ 와 $\text{Var}(F)$ 를 구하여라.

    **은행에서의 대기시간:** 창구가 5개이므로 실질적인 비율은 분당 $5\lambda_B = 0.5$ 이다. 손님 두 명을 처리해야 하므로 다음과 같다.

    $$T_B = X_1 + X_2, \quad X_i \stackrel{\text{iid}}{\sim} \text{Exp}(0.5) \implies T_B \sim \Gamma(2, 0.5)$$

    **우체국에서의 대기시간:** 창구가 2개이므로 실질적인 비율은 분당 $2\lambda_P = 0.5$ 이다. 손님 세 명을 처리해야 하므로 다음과 같다.

    $$T_P = Y_1 + Y_2 + Y_3, \quad Y_j \stackrel{\text{iid}}{\sim} \text{Exp}(0.5) \implies T_P \sim \Gamma(3, 0.5)$$

    $T_B$ 와 $T_P$ 가 독립이고 **비율이 같으므로**($\lambda = 0.5$) 다음이 성립한다.

    $$F = \frac{T_B}{T_B + T_P} \sim \text{Beta}(2, 3)$$

    $\alpha = 2$, $\beta = 3$ 이므로 다음을 얻는다.

    $$E[F] = \frac{2}{2 + 3} = \frac{2}{5} = 0.4$$

    $$\text{Var}(F) = \frac{2 \cdot 3}{5^2 \cdot 6} = \frac{6}{150} = \frac{1}{25} = 0.04$$

## 풀이 예제: 주변분포가 베타분포인 결합 확률밀도함수

??? example "예: 주변분포가 베타분포인 종속 확률변수"
    $X$ 와 $Y$ 의 결합 확률밀도함수가 다음과 같다고 하자.

    $$f(x, y) = cxy, \quad 0 \leq x \leq 1, \; 0 \leq y \leq 1, \; 0 \leq x + y \leq 1$$

    **(a) $c$ 를 구하여라.**

    $$\int_0^1 \int_0^{1-y} cxy \, dx \, dy = \frac{c}{2} \int_0^1 y(1-y)^2 \, dy = \frac{c}{2} B(2, 3)$$

    베타적분을 알아보면 $\int_0^1 y^{2-1}(1-y)^{3-1} dy = B(2,3) = \frac{\Gamma(2)\Gamma(3)}{\Gamma(5)} = \frac{1! \cdot 2!}{4!} = \frac{1}{12}$ 이다.

    따라서 $\frac{c}{2} \cdot \frac{1}{12} = 1 \implies c = 24$ 이다.

    **(b) 주변 확률밀도함수를 구하여라.**

    $0 \leq x \leq 1$ 에 대하여 다음이 성립한다.

    $$f_X(x) = \int_0^{1-x} 24xy \, dy = 12x(1-x)^2 = \frac{x^{2-1}(1-x)^{3-1}}{B(2,3)}$$

    따라서 $X \sim \text{Beta}(2, 3)$ 이고, 대칭성에 따라 $Y \sim \text{Beta}(2, 3)$ 이다.

    **(c) $X$ 와 $Y$ 는 독립인가?**

    아니다. 제약 $x + y \leq 1$ 때문에 곱으로 갈라지지 않는다.

    $$f(x,y) = 24xy \cdot \mathbf{1}(0 \leq x \leq 1) \cdot \mathbf{1}(0 \leq y \leq 1) \cdot \underbrace{\mathbf{1}(x + y \leq 1)}_{\text{쪼갤 수 없음}}$$

    만약 독립이라면 $X + Y$ 가 2까지 커질 수 있어야 하지만, 이 결합 확률밀도함수는 $x + y > 1$ 에 아무런 확률도 주지 않는다.

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 베타분포의 확률밀도함수 그리기
x = np.linspace(0.001, 0.999, 300)
params = [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]
colors = ['blue', 'red', 'magenta', 'black', 'cyan']

for (a, b), color in zip(params, colors):
    pdf = stats.beta.pdf(x, a, b)
    axes[0].plot(x, pdf, color=color, lw=2,
                 label=f'α={a}, β={b}')

axes[0].set_title('PDF of Beta Distribution')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].set_ylim(0, 6)
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# 감마-베타 연결 확인
np.random.seed(42)
n_sim = 100000
alpha, beta_param = 2, 3
lam = 0.5

X_gamma = np.random.gamma(shape=alpha, scale=1/lam, size=n_sim)
Y_gamma = np.random.gamma(shape=beta_param, scale=1/lam, size=n_sim)
F = X_gamma / (X_gamma + Y_gamma)

axes[1].hist(F, bins=60, density=True, alpha=0.5, color='steelblue',
             label='X/(X+Y) simulated')
x_theory = np.linspace(0.001, 0.999, 200)
pdf_theory = stats.beta.pdf(x_theory, alpha, beta_param)
axes[1].plot(x_theory, pdf_theory, 'r-', lw=2,
             label=f'Beta({alpha},{beta_param}) PDF')
axes[1].set_title(f'Γ({alpha},λ) / [Γ({alpha},λ)+Γ({beta_param},λ)] ~ Beta({alpha},{beta_param})')
axes[1].set_xlabel('f')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('beta_definition.png', dpi=150, bbox_inches='tight')
plt.show()

# T 와 F 의 독립성 확인
T = X_gamma + Y_gamma
corr = np.corrcoef(T, F)[0, 1]
print(f"Correlation between T and F: {corr:.6f} (should be ≈ 0)")
print(f"E[F] = {np.mean(F):.4f} (theory {alpha/(alpha+beta_param):.4f})")
var_theory = alpha * beta_param / ((alpha+beta_param)**2 * (alpha+beta_param+1))
print(f"Var(F) = {np.var(F):.4f} (theory {var_theory:.4f})")
```

## 연습문제

**연습문제 1.**
$X \sim \text{Beta}(3, 5)$ 라 하자.

(a) $E[X]$ 와 $\text{Var}(X)$ 를 구하여라.

(b) $E[X^2]$ 을 구하여라.

(c) $1 - X$ 의 분포를 구하여라.

??? success "연습문제 1 풀이"
    (a) $E[X] = \frac{3}{8} = 0.375$, $\text{Var}(X) = \frac{15}{64 \cdot 9} = \frac{15}{576} \approx 0.0260$

    (b) $E[X^2] = \text{Var}(X) + (E[X])^2 = \frac{15}{576} + \frac{9}{64} = \frac{15 + 81}{576} = \frac{96}{576} = \frac{1}{6}$

    (c) 반사 성질에 따라 $1 - X \sim \text{Beta}(5, 3)$ 이다.
