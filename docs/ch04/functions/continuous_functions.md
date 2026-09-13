# 연속확률변수의 함수

## 누적분포함수 방법 (일반)

임의의 함수 $g$ 와 연속확률변수 $X$ 에 대해 누적분포함수 방법은 언제나 통한다.

!!! info "누적분포함수 방법"
    $Y = g(X)$ 의 분포를 구하려면 다음과 같이 한다.

    1. $F_Y(y) = P(Y \leq y) = P(g(X) \leq y)$ 를 계산한다
    2. 이를 $X$ 만으로 나타낸 확률로 바꾼다
    3. 미분한다: $f_Y(y) = F_Y'(y)$

**예: $X \sim N(0,1)$ 일 때 $Y = X^2$.**

$y > 0$ 일 때 다음이 성립한다.

$$F_Y(y) = P(X^2 \leq y) = P(-\sqrt{y} \leq X \leq \sqrt{y}) = \mathcal{N}(\sqrt{y}) - \mathcal{N}(-\sqrt{y}) = 2\mathcal{N}(\sqrt{y}) - 1$$

미분하면 다음을 얻는다.

$$f_Y(y) = 2\phi(\sqrt{y}) \cdot \frac{1}{2\sqrt{y}} = \frac{1}{\sqrt{y}} \cdot \frac{1}{\sqrt{2\pi}} e^{-y/2} = \frac{y^{1/2 - 1} e^{-y/2}}{2^{1/2}\,\Gamma(1/2)}$$

이것이 $\chi^2(1)$ 분포, 곧 $\text{Gamma}(1/2, 1/2)$ 이다.

## 변수변환 공식 (단조인 경우)

$g$ 가 **순단조**(순증가이거나 순감소)이고 미분가능하면 지름길이 있다.

!!! info "변수변환 공식"
    $Y = g(X)$ 이고 $g$ 가 순단조이며 미분가능하고 역함수가 $X = g^{-1}(Y)$ 이면 다음이 성립한다.

    $$f_Y(y) = f_X\!\left(g^{-1}(y)\right) \cdot \left|\frac{d}{dy}\,g^{-1}(y)\right|$$

    절댓값을 씌운 덕분에 $g$ 가 증가하든 감소하든 $f_Y(y) \geq 0$ 이 보장된다.

**유도 (증가하는 경우).** $g$ 가 순증가이면 다음이 성립한다.

$$F_Y(y) = P(g(X) \leq y) = P(X \leq g^{-1}(y)) = F_X(g^{-1}(y))$$

연쇄법칙으로 미분하면 다음을 얻는다.

$$f_Y(y) = f_X(g^{-1}(y)) \cdot \frac{d}{dy}g^{-1}(y)$$

감소하는 경우에는 $P(g(X) \leq y) = P(X \geq g^{-1}(y))$ 가 되어 음의 부호가 나오는데, 이것을 절댓값이 흡수한다.

## 예: 일차변환

$X$ 가 확률밀도함수 $f_X$ 를 갖는 연속확률변수이고 $a \neq 0$ 에 대해 $Y = aX + b$ 라 하자.

- 역함수: $X = \frac{Y - b}{a}$
- 도함수: $\frac{dX}{dY} = \frac{1}{a}$

$$f_Y(y) = f_X\!\left(\frac{y - b}{a}\right) \cdot \frac{1}{|a|}$$

**특별한 경우:** $X \sim N(\mu, \sigma^2)$ 이고 $Y = aX + b$ 이면 $Y \sim N(a\mu + b,\; a^2\sigma^2)$ 이다.

## 예: 지수변환

$X \sim \text{Uniform}(0, 1)$ 이고 $Y = -\ln X$ 라 하자. $g(x) = -\ln x$ 는 $(0,1)$ 에서 **순감소**이므로 다음과 같다.

- 역함수: $X = e^{-Y}$
- 도함수: $\frac{dX}{dY} = -e^{-Y}$ 이므로 $\left|\frac{dX}{dY}\right| = e^{-Y}$

$$f_Y(y) = f_X(e^{-y}) \cdot e^{-y} = 1 \cdot e^{-y} = e^{-y}, \quad y > 0$$

이것이 $\text{Exponential}(1)$ 이다. 이 결과가 모의실험에서 쓰는 **역변환 방법**의 바탕이 된다.

## 단조가 아닌 함수: 쪼개어 다루기

$g$ 가 단조가 아니면 $X$ 의 정의역을 $g$ 가 단조인 구간들로 쪼갠 다음, 각 조각에 공식을 적용하고 그 결과를 더한다.

!!! info "단조가 아닌 경우의 변수변환"
    $g$ 가 단조는 아니지만 정의역을 영역 $A_1, A_2, \ldots, A_k$ 로 쪼개어 각 영역에서 $g$ 가 순단조이고 국소역함수가 $h_i = g^{-1}\big|_{A_i}$ 라면 다음이 성립한다.

    $$f_Y(y) = \sum_{i=1}^{k} f_X(h_i(y)) \cdot |h_i'(y)|$$

**예: $X$ 가 $(-\infty, \infty)$ 위에서 확률밀도함수 $f_X$ 를 가질 때 $Y = X^2$.**

함수 $g(x) = x^2$ 은 $(-\infty, 0)$ 에서 감소하고 $(0, \infty)$ 에서 증가한다. 두 국소역함수는 $h_1(y) = -\sqrt{y}$ 와 $h_2(y) = \sqrt{y}$ 이고, 각각의 도함수는 $|h_i'(y)| = \frac{1}{2\sqrt{y}}$ 이다.

$$f_Y(y) = \frac{f_X(-\sqrt{y}) + f_X(\sqrt{y})}{2\sqrt{y}}, \quad y > 0$$

$f_X$ 가 0을 중심으로 대칭이면 이는 $f_Y(y) = \frac{f_X(\sqrt{y})}{\sqrt{y}}$ 로 간단해진다.

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

x = np.linspace(-4, 4, 1000)

# --- 1번 그림: X ~ N(0,1)일 때 Y = X^2 ---
fX = stats.norm.pdf(x)
axes[0].plot(x, fX, 'b-', lw=2, label='$f_X$: N(0,1)')

y = np.linspace(0.01, 10, 500)
fY_theory = stats.chi2.pdf(y, df=1)

# 모의실험
np.random.seed(42)
X_sim = np.random.normal(0, 1, 200000)
Y_sim = X_sim**2
axes[0].hist(Y_sim, bins=100, density=True, alpha=0.4, color='coral',
             range=(0, 10), label='Y = X² simulated')
axes[0].plot(y, fY_theory, 'r-', lw=2, label='χ²(1) PDF')
axes[0].set_xlim(-4, 10)
axes[0].set_title('Y = X², X ~ N(0,1) → χ²(1)')
axes[0].legend(fontsize=9)
axes[0].grid(True, alpha=0.3)

# --- 2번 그림: Y = -ln(X), X ~ U(0,1) → Exp(1) ---
X_unif = np.random.uniform(0, 1, 200000)
Y_exp = -np.log(X_unif)

y2 = np.linspace(0.01, 6, 300)
axes[1].hist(Y_exp, bins=80, density=True, alpha=0.5, color='steelblue',
             label='Y = -ln(X) simulated')
axes[1].plot(y2, stats.expon.pdf(y2), 'r-', lw=2, label='Exp(1) PDF')
axes[1].set_title('Y = -ln(X), X ~ U(0,1) → Exp(1)')
axes[1].set_xlabel('y')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# --- 3번 그림: X ~ N(0,1)일 때 Y = |X| → 반정규분포 ---
Y_abs = np.abs(X_sim)
y3 = np.linspace(0, 4, 300)
fY_half = 2 * stats.norm.pdf(y3)  # 반정규분포의 확률밀도함수

axes[2].hist(Y_abs, bins=80, density=True, alpha=0.5, color='steelblue',
             label='|X| simulated')
axes[2].plot(y3, fY_half, 'r-', lw=2, label='Half-Normal PDF')
axes[2].set_title('Y = |X|, X ~ N(0,1) → Half-Normal')
axes[2].set_xlabel('y')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('functions_continuous.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 연습문제

**연습문제 1.** $X \sim \text{Uniform}(0, 1)$ (연속)이라 하자. 누적분포함수 방법으로 $Y = X^2$ 의 확률밀도함수를 구하여라.

??? success "연습문제 1 풀이"
    $y \in (0, 1)$ 에 대해 다음이 성립한다.

    $$
    F_Y(y) = P(X^2 \leq y) = P(X \leq \sqrt{y}) = \sqrt{y}
    $$

    ($[0, 1]$ 위에서 $P(X \leq x) = x$ 임과 $X \geq 0$ 임을 썼다.) 미분하면 다음을 얻는다.

    $$
    f_Y(y) = \frac{d}{dy} \sqrt{y} = \frac{1}{2 \sqrt{y}}, \quad 0 < y < 1
    $$

    $X$ 가 $[0, 1]$ 위의 균등분포를 따를 때 $X^2$ 은 0 가까이에 질량을 몰아 놓으므로, 밀도가 $y = 0$ 근처에서 치솟는다.

---

**연습문제 2.** 어떤 센서가 재는 온도가 (섭씨로) $[20, 30]$ 위의 균등분포를 따른다고 하자. 이 측정값을 $Y = 1.8 X + 32$ 로 화씨로 바꾼다. 변수변환 공식으로 $Y$ 의 확률밀도함수를 구하고 $\int f_Y(y) \, dy = 1$ 임을 확인하여라.

??? success "연습문제 2 풀이"
    $X \sim \text{Uniform}(20, 30)$ 이므로 $[20, 30]$ 에서 $f_X(x) = 1/10$ 이다. 대응 $y = g(x) = 1.8 x + 32$ 는 순증가이고 역함수는 $x = (y - 32)/1.8$, 그리고 $|dx/dy| = 1/1.8$ 이다.

    변수변환 공식에 따라 $y \in [20 \cdot 1.8 + 32, 30 \cdot 1.8 + 32] = [68, 86]$ 에서 다음이 성립한다.

    $$
    f_Y(y) = f_X\!\left(\tfrac{y - 32}{1.8}\right) \cdot \frac{1}{1.8} = \frac{1}{10} \cdot \frac{1}{1.8} = \frac{1}{18}
    $$

    따라서 $Y \sim \text{Uniform}(68, 86)$ 이다. 확인해 보면 다음과 같다.

    $$
    \int_{68}^{86} \frac{1}{18} \, dy = \frac{86 - 68}{18} = 1
    $$

    $\checkmark$
