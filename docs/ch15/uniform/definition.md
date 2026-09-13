# 연속균등분포

## 정의

!!! info "연속균등분포"
    연속확률변수 $X$ 의 확률밀도함수가 다음과 같으면, $X$ 는 구간 $(a, b)$ 위의 **균등분포**를 따른다고 하고 $X \sim U(a, b)$ 로 적는다.

    $$f(x) = \frac{1}{b - a}, \quad a < x < b$$

    구간 $(a, b)$ 안의 모든 값이 같은 정도로 일어난다. 곧 어떤 부분구간에 떨어질 확률이 그 부분구간의 길이에만 달려 있다는 뜻이다.

### 누적분포함수

$$F(x) = \begin{cases} 0 & x \leq a \\ \dfrac{x - a}{b - a} & a < x < b \\ 1 & x \geq b \end{cases}$$

### 푸아송 과정에서 오는 직관

푸아송 과정 $\text{NPP}(\lambda)$ 에서 구간 $[a, b]$ 안에 도착이 꼭 한 번 있었다면, 그 도착의 위치는 $[a, b]$ 위에서 균등분포를 따른다. 더 일반적으로 $N([a,b]) = n$ 이 주어지면 $n$ 개의 도착 위치는 i.i.d. $U(a, b)$ 확률변수 $n$ 개처럼 분포한다(크기순으로 늘어놓으면 순서통계량이 된다).

## 평균과 분산

!!! info "U(a, b) 의 적률"

    $$E[X] = \frac{a + b}{2}, \qquad \text{Var}(X) = \frac{(b - a)^2}{12}$$

### 평균의 유도

$$E[X] = \int_a^b x f(x) \, dx = \frac{1}{b - a} \int_a^b x \, dx = \frac{1}{b - a} \left[\frac{x^2}{2}\right]_a^b = \frac{b^2 - a^2}{2(b-a)}$$

인수분해 $a^2 - b^2 = (a+b)(a-b)$ 를 쓰면 다음을 얻는다.

$$E[X] = \frac{(b+a)(b-a)}{2(b-a)} = \frac{a + b}{2}$$

### 분산의 유도

먼저 $E[X^2]$ 을 구한다.

$$E[X^2] = \int_a^b x^2 f(x) \, dx = \frac{1}{b - a} \int_a^b x^2 \, dx = \frac{1}{b - a} \left[\frac{x^3}{3}\right]_a^b = \frac{b^3 - a^3}{3(b-a)}$$

인수분해 $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$ 를 쓰면 다음을 얻는다.

$$E[X^2] = \frac{(b - a)(b^2 + ab + a^2)}{3(b - a)} = \frac{a^2 + ab + b^2}{3}$$

따라서 다음이 성립한다.

$$\text{Var}(X) = E[X^2] - (E[X])^2 = \frac{a^2 + ab + b^2}{3} - \frac{(a+b)^2}{4}$$

$$= \frac{4(a^2 + ab + b^2) - 3(a^2 + 2ab + b^2)}{12} = \frac{a^2 - 2ab + b^2}{12} = \frac{(b - a)^2}{12}$$

### 쓸모 있는 대수 항등식

위의 유도에는 자주 나오는 인수분해 항등식 두 가지가 쓰였다.

$$a^2 - b^2 = (a + b)(a - b)$$

$$a^3 - b^3 = (a - b)(a^2 + ab + b^2)$$

$a^3 + b^3 = (a + b)(a^2 - ab + b^2)$ 도 쓸모가 있다.

## 표준균등분포 U(0, 1)

가장 중요한 특별한 경우는 $U(0, 1)$ 이다.

$$f(x) = 1, \quad 0 < x < 1, \qquad F(x) = x, \quad 0 \leq x \leq 1$$

$$E[X] = \frac{1}{2}, \qquad \text{Var}(X) = \frac{1}{12}$$

표준균등분포는 난수 생성과 모의실험의 바탕이 된다.

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# 여러 구간에 대한 확률밀도함수와 누적분포함수
intervals = [(0, 1), (-2, 3), (1, 4)]
colors = ['blue', 'red', 'green']

for (a, b), color in zip(intervals, colors):
    x = np.linspace(a - 1, b + 1, 300)
    pdf = stats.uniform.pdf(x, loc=a, scale=b-a)
    cdf = stats.uniform.cdf(x, loc=a, scale=b-a)

    axes[0].plot(x, pdf, color=color, lw=2, label=f'U({a},{b})')
    axes[1].plot(x, cdf, color=color, lw=2, label=f'U({a},{b})')

axes[0].set_title('PDF of Uniform Distribution')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].set_title('CDF of Uniform Distribution')
axes[1].set_xlabel('x')
axes[1].set_ylabel('F(x)')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# 모의실험으로 평균과 분산 확인
np.random.seed(42)
n_sim = 100000
a, b = 2, 8
X = np.random.uniform(a, b, n_sim)

axes[2].hist(X, bins=50, density=True, alpha=0.7, color='steelblue')
axes[2].axvline(np.mean(X), color='red', lw=2, linestyle='--',
                label=f'Sample mean = {np.mean(X):.3f}')
axes[2].axvline((a+b)/2, color='black', lw=2, linestyle=':',
                label=f'Theory mean = {(a+b)/2:.3f}')
axes[2].set_title(f'U({a},{b}) Simulation')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('uniform_definition.png', dpi=150, bbox_inches='tight')
plt.show()

print(f"U({a},{b}): E[X] = {np.mean(X):.4f} (theory {(a+b)/2:.4f})")
print(f"U({a},{b}): Var(X) = {np.var(X):.4f} (theory {(b-a)**2/12:.4f})")
```

## 연습문제

**연습문제 1.**
$X \sim U(2, 8)$ 이라 하자.

(a) $P(3 < X < 6)$ 을 구하여라.

(b) $E[X^2]$ 을 구하여라.

(c) $X$ 의 중앙값을 구하여라.

??? success "연습문제 1 풀이"
    (a) $P(3 < X < 6) = \frac{6 - 3}{8 - 2} = \frac{1}{2}$

    (b) $E[X^2] = \frac{a^2 + ab + b^2}{3} = \frac{4 + 16 + 64}{3} = 28$

    (c) 중앙값은 $\frac{a + b}{2} = 5$ 이고, 대칭성에 따라 평균과 같다.

---

**연습문제 2.** $U \sim U(0, 1)$ 이라 하자.

(a) 일반적인 $U(a, b)$ 공식을 끌어다 쓰지 말고 적분으로 $E[U]$ 와 $\text{Var}(U)$ 를 직접 구하여라.

(b) $P(U \leq 0.3 \text{ 또는 } U \geq 0.7)$ 을 구하여라.

(c) $P(|U - 1/2| \leq c) = 0.6$ 이 되는 상수 $c$ 를 구하여라.

??? success "연습문제 2 풀이"
    (a) $(0, 1)$ 위에서 $f(u) = 1$ 이므로 다음을 얻는다.

    $$
    E[U] = \int_0^1 u\,du = \tfrac{1}{2}, \qquad E[U^2] = \int_0^1 u^2\,du = \tfrac{1}{3}
    $$

    $$
    \text{Var}(U) = \tfrac{1}{3} - \tfrac{1}{4} = \tfrac{1}{12}
    $$

    (b) 여사건을 쓰면 $P(U \leq 0.3 \text{ 또는 } U \geq 0.7) = 1 - P(0.3 < U < 0.7) = 1 - 0.4 = 0.6$ 이다.

    (c) 사건 $|U - 1/2| \leq c$ 는 구간 $[1/2 - c,\, 1/2 + c]$ 이고, 그 길이는 $2c$ 이며 $c \leq 1/2$ 인 한 $(0, 1)$ 안에 들어 있다. 따라서 $P(|U - 1/2| \leq c) = 2c$ 이므로 $c = 0.3$ 이다.

---

**연습문제 3.** $U \sim U(0, 1)$ 이고 $Y = U^2$ 이라 하자. $Y$ 의 누적분포함수와 확률밀도함수를 구하고, $E[Y] = 1/3$ 임을 두 가지 방법으로 확인하여라. 곧 $f_Y$ 에서 직접 구하는 방법과 LOTUS 공식 $E[U^2] = \int_0^1 u^2\,du$ 를 쓰는 방법이다.

??? success "연습문제 3 풀이"
    $y \in (0, 1)$ 에 대하여 다음이 성립한다.

    $$
    F_Y(y) = P(U^2 \leq y) = P(U \leq \sqrt{y}) = \sqrt{y}
    $$

    미분하면 다음을 얻는다.

    $$
    f_Y(y) = \frac{1}{2\sqrt{y}}, \quad 0 < y < 1
    $$

    이 확률밀도함수는 $y = 0$ 에서 발산하지만 여전히 적분할 수 있다.

    **$f_Y$ 에서 구하기:**

    $$
    E[Y] = \int_0^1 y \cdot \frac{1}{2\sqrt{y}}\,dy = \frac{1}{2}\int_0^1 y^{1/2}\,dy = \frac{1}{2} \cdot \frac{2}{3} = \frac{1}{3}
    $$

    **LOTUS로 구하기:** $E[U^2] = \int_0^1 u^2\,du = 1/3$ 이다. 두 답이 일치하며, 이것이 바로 LOTUS가 보장하는 바이다. $\square$

---

**연습문제 4.** *버스 기다리기.* 나는 매시 정각으로부터 $[0, 30]$ 분 사이에 균등분포를 따르는 시각에 버스 정류장에 도착한다. 버스도 나와 독립적으로 매시 정각으로부터 $[0, 30]$ 분 사이에 균등분포를 따르는 시각에 도착한다. 버스가 내가 도착한 시각 이후에 와야만 나는 버스를 탈 수 있다.

(a) 내가 버스를 무사히 탈 확률을 구하여라.

(b) 버스를 탔다는 조건 아래에서 기다린 시간의 기댓값을 구하여라.

??? success "연습문제 4 풀이"
    내가 도착한 시각을 $A$, 버스가 도착한 시각을 $B$ 라 하면 둘 다 $U(0, 30)$ 이고 서로 독립이다. 버스를 타는 것은 $B \geq A$ 일 때 그리고 오직 그때만이다.

    (a) 대칭성에 따라 $P(B \geq A) = P(A \geq B) = 1/2$ 이다($A = B$ 일 확률은 0이다). 따라서 버스를 탈 확률은 $1/2$ 이다.

    (b) $B \geq A$ 라는 조건 아래에서, 삼각형 $\{0 \leq a \leq b \leq 30\}$ 위로 제한한 $(A, B)$ 의 결합밀도는 다음과 같다.

    $$
    f_{A, B \mid B \geq A}(a, b) = \frac{1/900}{1/2} = \frac{2}{900} = \frac{1}{450}
    $$

    기다린 시간은 $W = B - A$ 이다. $E[W \mid B \geq A]$ 를 구하려면 다음과 같이 적분한다.

    $$
    E[W \mid B \geq A] = \int_0^{30}\int_0^b (b - a) \cdot \frac{1}{450}\,da\,db = \frac{1}{450}\int_0^{30}\frac{b^2}{2}\,db = \frac{1}{450}\cdot\frac{30^3}{6} = 10 \text{ 분}
    $$

    따라서 버스를 탔다는 조건 아래에서 평균 $10$ 분을 기다린다. (검산: 이는 $30$ 분 창의 3분의 1이며, "균등하게 뽑은 두 값 사이의 평균 간격"에서 기대할 수 있는 값과 같다.) $\square$
