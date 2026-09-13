# 연속확률변수의 합성곱

## 정의

!!! info "합성곱 (연속)"
    $X$ 와 $Y$ 가 **독립**인 연속확률변수이면, 두 확률밀도함수의 **합성곱**이 $X + Y$ 의 확률밀도함수를 준다.

    $$(f_X * f_Y)(a) = f_{X+Y}(a) = \int_{-\infty}^{\infty} f_X(b) \cdot f_Y(a - b) \, db$$

    적분은 $f_X(b) > 0$ 이면서 동시에 $f_Y(a - b) > 0$ 인 모든 $b$ 에 대하여 취한다.

### 누적분포함수 형태

$$(F_X * F_Y)(a) = F_{X+Y}(a) = \int_{-\infty}^{\infty} F_Y(a - b) \, dF_X(b)$$

여기에서 $dF_X(b) = f_X(b) \, db$ 는 "$X$ 가 $[b, b+db]$ 안에 들어갈 확률"을 뜻한다.

### 유도

$X = b$ 로 조건을 걸면 다음을 얻는다.

$$f_{X+Y}(a) = \int_{-\infty}^{\infty} f_{Y}(a - b) \cdot \underbrace{f_X(b) \, db}_{P(b \leq X \leq b + db)}$$

이것은 $X$ 가 가질 수 있는 모든 값에 대하여 더하면서 각 값마다 $Y = a - X$ 의 밀도를 계산하는 일을 연속인 경우로 옮겨 놓은 것이다.

## 실제 계산

합성곱을 계산할 때 가장 까다로운 대목은 **적분 구간**을 정하는 일이다. 피적분함수가 $0$ 이 아니려면 다음 두 조건이 동시에 성립해야 한다.

- $f_X(b) > 0$: $b$ 가 $X$ 의 받침(support)에 들어 있다
- $f_Y(a - b) > 0$: $a - b$ 가 $Y$ 의 받침에 들어 있다

이 두 제약이 함께 실제 적분 구간을 정한다.

### 요령

1. 받침을 적어 둔다: $b \in [x_{\min}, x_{\max}]$ 이고 $a - b \in [y_{\min}, y_{\max}]$
2. $b$ 에 대하여 푼다: $x_{\min} \leq b \leq x_{\max}$ 와 $a - y_{\max} \leq b \leq a - y_{\min}$ 을 합친다
3. 두 구간의 교집합을 잡으면 그것이 적분 구간이다

## 성질

1. **교환법칙:** $f_X * f_Y = f_Y * f_X$
2. **결합법칙:** $(f_X * f_Y) * f_Z = f_X * (f_Y * f_Z)$
3. **기댓값의 선형성:** $E[X + Y] = E[X] + E[Y]$ (독립이 아니어도 언제나 성립한다)
4. **분산의 덧셈:** $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$ (독립이어야 한다)
5. **적률생성함수의 곱셈:** $M_{X+Y}(t) = M_X(t) \cdot M_Y(t)$ (독립이어야 한다)

## 적률생성함수와의 관계

"밀도의 세계"에서의 합성곱은 "적률생성함수의 세계"에서의 **곱셈**에 해당한다.

$$f_{X+Y} = f_X * f_Y \quad \longleftrightarrow \quad M_{X+Y}(t) = M_X(t) \cdot M_Y(t)$$

이는 신호처리의 합성곱 정리와 같은 모습이다. 거기에서도 시간 영역의 합성곱이 주파수 영역의 곱셈이 된다. 적률생성함수를 쓸 수 있는 상황이라면 합성곱 적분을 계산하기보다 적률생성함수를 곱하는 쪽이 대체로 훨씬 쉽다.

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.signal import fftconvolve

np.random.seed(42)
n_sim = 100000

# 모의실험과 수치계산으로 보는 연속 합성곱
# 예: 독립인 Exp(1) 두 개의 합
lam = 1.0
X = np.random.exponential(1/lam, n_sim)
Y = np.random.exponential(1/lam, n_sim)
S = X + Y

fig, ax = plt.subplots(1, 1, figsize=(8, 5))

# 모의실험 히스토그램
ax.hist(S, bins=80, density=True, alpha=0.5, color='steelblue',
        label='Simulation of X+Y')

# 이론값: Exp(1) * Exp(1) = Gamma(2,1)
a_vals = np.linspace(0, 10, 200)
pdf_gamma = stats.gamma.pdf(a_vals, a=2, scale=1/lam)
ax.plot(a_vals, pdf_gamma, 'r-', lw=2, label='Γ(2,1) PDF (theory)')

# 수치 합성곱
dx = 0.01
x_grid = np.arange(0, 10, dx)
f_exp = lam * np.exp(-lam * x_grid)
f_conv = np.convolve(f_exp, f_exp) * dx
a_conv = np.arange(0, len(f_conv)) * dx
ax.plot(a_conv[:len(a_vals)], f_conv[:len(a_vals)], 'g--', lw=2,
        label='Numerical convolution')

ax.set_title('Convolution: Exp(1) * Exp(1) = Γ(2,1)')
ax.set_xlabel('a')
ax.set_ylabel('f_{X+Y}(a)')
ax.set_xlim(0, 10)
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('continuous_convolution.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 연습문제

**연습문제 1.**
$X$ 와 $Y$ 가 종속일 때에는 합성곱이 $X + Y$ 의 분포를 제대로 주지 **않음**을 보여 주는 예를 들어라. 구체적으로 $X \sim U(0, 1)$ 이고 $Y = X$ 라고 하자. $X + Y$ 의 분포를 구하고, 그것이 $U(0,1)$ 을 자기 자신과 합성곱하여 얻는 삼각분포와 다름을 보여라.
