# 이산확률변수의 함수

## 왜 필요한가

분포를 알고 있는 확률변수 $X$ 가 있을 때, 어떤 함수 $g$ 에 대해 $Y = g(X)$ 의 분포가 필요해지는 일이 잦다. 이를테면 다음과 같다.

- $Y = X^2$ (편차의 제곱)
- $Y = |X|$ (절댓값)
- $Y = \mathbf{1}(X > 0)$ (지시함수)
- $Y = \max(X, 0)$ (콜옵션의 보수)

## 이산인 경우

$X$ 가 이산일 때 $Y = g(X)$ 의 분포를 구하는 일은 간단하다. $Y$ 의 같은 값으로 옮겨 가는 $X$ 의 값들을 한데 묶으면 된다.

!!! info "g(X)의 확률질량함수 — 이산인 경우"
    $X$ 가 확률질량함수 $p_X(x)$ 를 갖는 이산확률변수이고 $Y = g(X)$ 이면, $Y$ 도 이산확률변수이고 그 확률질량함수는 다음과 같다.

    $$p_Y(y) = P(Y = y) = \sum_{x:\, g(x) = y} p_X(x)$$

    곧 $y$ 로 옮겨 가는 모든 $x$ 값의 확률을 더한다.

## 예: 대칭인 분포를 제곱하기

$X$ 가 $-2, -1, 0, 1, 2$ 를 각각 확률 $\frac{1}{5}$ 로 갖는다고 하자. $Y = X^2$ 이라 둔다.

| $x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $g(x) = x^2$ | $4$ | $1$ | $0$ | $1$ | $4$ |
| $p_X(x)$ | $1/5$ | $1/5$ | $1/5$ | $1/5$ | $1/5$ |

$y$ 의 값끼리 묶으면 다음과 같다.

| $y$ | $0$ | $1$ | $4$ |
|:---:|:---:|:---:|:---:|
| $p_Y(y)$ | $1/5$ | $2/5$ | $2/5$ |

$X$ 는 다섯 값을 갖는데 $Y$ 는 세 값만 갖는다는 데 유의하자. 함수 $g(x) = x^2$ 이 **일대일이 아니어서** 여러 $x$ 값이 같은 $y$ 로 합쳐지기 때문이다.

## 예: 지시함수

$X \sim \text{Binomial}(10, 0.3)$ 이고 $Y = \mathbf{1}(X \geq 5)$ 라 하자. 그러면 $Y$ 는 베르누이확률변수이다.

$$p_Y(1) = P(X \geq 5), \qquad p_Y(0) = P(X < 5)$$

함수를 씌우면 분포가 크게 단순해질 수 있음을 보여 준다.

## 예: 0과의 최댓값

$X \sim \text{Uniform}\{-3, -2, -1, 0, 1, 2, 3\}$ 이고 $Y = \max(X, 0)$ 이라 하자. 그러면 다음이 성립한다.

$$p_Y(0) = P(X \leq 0) = \frac{4}{7}, \quad p_Y(1) = p_Y(2) = p_Y(3) = \frac{1}{7}$$

이것은 **섞인** 경우이다. $X$ 는 $0$ 에 특별히 몰려 있지 않은데도 $Y$ 는 $0$ 에 점질량을 갖는다.

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))

# --- 예 1: X^2 ---
x_vals = np.array([-2, -1, 0, 1, 2])
px = np.ones(5) / 5
y_vals = x_vals**2

axes[0].bar(x_vals - 0.15, px, width=0.3, color='steelblue', alpha=0.7, label='X')
# Y의 확률질량함수를 계산한다
unique_y = np.unique(y_vals)
py = np.array([px[y_vals == y].sum() for y in unique_y])
axes[0].bar(unique_y + 0.15, py, width=0.3, color='coral', alpha=0.7, label='Y = X²')
axes[0].set_title('Y = X² (many-to-one)')
axes[0].set_xlabel('Value')
axes[0].set_ylabel('Probability')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# --- 예 2: 지시함수 ---
from scipy.stats import binom
n, p = 10, 0.3
x_binom = np.arange(0, 11)
px_binom = binom.pmf(x_binom, n, p)

p_y1 = px_binom[5:].sum()
p_y0 = px_binom[:5].sum()

axes[1].bar(x_binom, px_binom, color='steelblue', alpha=0.5, label='X ~ Bin(10, 0.3)')
axes[1].bar([0, 1], [p_y0, p_y1], color='coral', alpha=0.7, width=0.4,
            label=f'Y = 1(X≥5): P(0)={p_y0:.3f}, P(1)={p_y1:.3f}')
axes[1].set_title('Indicator: Y = 1(X ≥ 5)')
axes[1].set_xlabel('Value')
axes[1].legend(fontsize=8)
axes[1].grid(True, alpha=0.3)

# --- 예 3: max(X, 0) ---
x_unif = np.arange(-3, 4)
px_unif = np.ones(7) / 7
y_max = np.maximum(x_unif, 0)

unique_ym = np.unique(y_max)
py_max = np.array([px_unif[y_max == y].sum() for y in unique_ym])

axes[2].bar(unique_ym, py_max, color='coral', alpha=0.7)
axes[2].set_title('Y = max(X, 0) — point mass at 0')
axes[2].set_xlabel('y')
axes[2].set_ylabel('P(Y = y)')
for y, p in zip(unique_ym, py_max):
    axes[2].text(y, p + 0.02, f'{p:.2f}', ha='center', fontsize=9)
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('functions_discrete.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 연습문제

**연습문제 1.** $X \sim \text{Bernoulli}(0.3)$ 일 때 $Y = 5X + 2$ 의 확률질량함수를 구하여라.

??? success "연습문제 1 풀이"
    $X$ 는 $\{0, 1\}$ 의 값을 가지므로 $Y$ 는 $\{2, 7\}$ 의 값을 갖는다.

    - $Y = 2 \iff X = 0$ 이고 그 확률은 $0.7$ 이다.
    - $Y = 7 \iff X = 1$ 이고 그 확률은 $0.3$ 이다.

    따라서 $Y$ 의 확률질량함수는 $P(Y = 2) = 0.7$, $P(Y = 7) = 0.3$ 이다.

---

**연습문제 2.** 확률변수 $X$ 가 $\{-2, -1, 0, 1, 2\}$ 의 값을 각각 확률 $1/5$ 로 갖는다고 하자. $Y = X^2$ 의 확률질량함수를 구하여라.

??? success "연습문제 2 풀이"
    $Y = X^2$ 은 $\{0, 1, 4\}$ 의 값을 갖는다.

    - $Y = 0 \iff X = 0$: $P(Y = 0) = 1/5$.
    - $Y = 1 \iff X \in \{-1, 1\}$: $P(Y = 1) = 2/5$.
    - $Y = 4 \iff X \in \{-2, 2\}$: $P(Y = 4) = 2/5$.

    여럿이 하나로 가는 대응이므로 $\pm 1$ 과 $\pm 2$ 가 각각 한 값으로 합쳐진다.

---

**연습문제 3.** 이산확률변수 $X$ 의 확률질량함수가 $k = -1, 0, 1, 2$ 에 대해 $P(X = k) = 1/4$ 이라 하자. $Y = |X|$ 의 확률질량함수와 $Z = \max(X, 0)$ 의 확률질량함수를 구하여라.

??? success "연습문제 3 풀이"
    **$Y = |X|$ 의 확률질량함수.** 값: $\{0, 1, 2\}$.

    - $Y = 0 \iff X = 0$: $P = 1/4$.
    - $Y = 1 \iff X \in \{-1, 1\}$: $P = 2/4 = 1/2$.
    - $Y = 2 \iff X = 2$: $P = 1/4$.

    **$Z = \max(X, 0)$ 의 확률질량함수.** 값: $\{0, 1, 2\}$.

    - $Z = 0 \iff X \in \{-1, 0\}$: $P = 2/4 = 1/2$.
    - $Z = 1 \iff X = 1$: $P = 1/4$.
    - $Z = 2 \iff X = 2$: $P = 1/4$.
