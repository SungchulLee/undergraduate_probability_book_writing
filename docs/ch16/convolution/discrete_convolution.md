# 이산확률변수의 합성곱

## 정의

!!! info "합성곱 (이산)"
    $X$ 와 $Y$ 가 **독립**인 이산확률변수이면, 두 확률질량함수의 **합성곱**이 $X + Y$ 의 확률질량함수를 준다.

    $$(p_X * p_Y)(a) = p_{X+Y}(a) = \sum_b p_X(b) \cdot p_Y(a - b)$$

    합은 $p_X(b) > 0$ 이면서 동시에 $p_Y(a - b) > 0$ 인 모든 값 $b$ 에 대하여 취한다.

### 기호

| 기호 | 뜻 |
|:---:|:---|
| $F_X * F_Y$ | $X, Y$ 가 독립일 때 $X + Y$ 의 누적분포함수 |
| $p_X * p_Y$ | $X, Y$ 가 독립일 때 $X + Y$ 의 확률질량함수 |
| $f_X * f_Y$ | $X, Y$ 가 독립일 때 $X + Y$ 의 확률밀도함수 |

### 유도

$X = b$ 로 조건을 걸고 전확률 법칙을 쓰면 다음을 얻는다.

$$P(X + Y = a) = \sum_b P(X + Y = a \mid X = b) \cdot P(X = b)$$

$$= \sum_b P(Y = a - b \mid X = b) \cdot P(X = b) = \sum_b p_Y(a - b) \cdot p_X(b)$$

마지막 단계에서 독립성 $P(Y = a - b \mid X = b) = P(Y = a - b)$ 을 썼다.

## 누적분포함수의 합성곱

합성곱의 누적분포함수 형태는 다음과 같다.

$$(F_X * F_Y)(a) = F_{X+Y}(a) = \sum_b F_Y(a - b) \cdot p_X(b)$$

여기에서 합은 $X$ 의 받침(support)에 있는 모든 값 $b$ 에 대하여 취하며, $F_Y(a - b)$ 에 $P(X = b)$ 라는 무게를 준다.

## 합성곱의 성질

1. **교환법칙:** $p_X * p_Y = p_Y * p_X$
2. **결합법칙:** $(p_X * p_Y) * p_Z = p_X * (p_Y * p_Z)$
3. **독립이어야 한다:** 합성곱이 $X + Y$ 의 분포를 주는 것은 $X$ 와 $Y$ 가 독립일 때뿐이다

결합법칙이 성립하므로 $X_1 + X_2 + \cdots + X_n$ 의 분포는 한 번에 하나씩 합성곱을 해 나가며 구할 수 있다.

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve

# 이산 합성곱 예제: 주사위 두 개의 합
# X, Y ~ DiscreteUniform{1,2,3,4,5,6}

# 확률질량함수 (값 1~6 을 첨자 0~5 로 둔다)
p = np.ones(6) / 6

# 합성곱으로 X + Y 의 확률질량함수를 얻는다 (값은 2부터 12까지)
p_sum = np.convolve(p, p)
values = np.arange(2, 13)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 주사위 두 개의 합의 확률질량함수
axes[0].bar(values, p_sum, color='steelblue', alpha=0.7, edgecolor='black')
axes[0].set_title('PMF of Sum of Two Fair Dice')
axes[0].set_xlabel('Sum')
axes[0].set_ylabel('P(X+Y = k)')
axes[0].set_xticks(values)
axes[0].grid(True, alpha=0.3)

# 모의실험으로 확인한다
np.random.seed(42)
n_sim = 100000
X = np.random.randint(1, 7, n_sim)
Y = np.random.randint(1, 7, n_sim)
S = X + Y

counts = np.bincount(S, minlength=13)[2:13]
probs_sim = counts / n_sim

axes[1].bar(values - 0.15, p_sum, 0.3, color='steelblue', alpha=0.7,
            label='Convolution', edgecolor='black')
axes[1].bar(values + 0.15, probs_sim, 0.3, color='orange', alpha=0.7,
            label='Simulation', edgecolor='black')
axes[1].set_title('Convolution vs Simulation')
axes[1].set_xlabel('Sum')
axes[1].set_ylabel('Probability')
axes[1].set_xticks(values)
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('discrete_convolution.png', dpi=150, bbox_inches='tight')
plt.show()

print("Sum | Convolution | Simulation")
print("-" * 35)
for v, pc, ps in zip(values, p_sum, probs_sim):
    print(f"  {v:2d} |    {pc:.4f}    |   {ps:.4f}")
```

## 연습문제

**연습문제 1.**
$X$ 와 $Y$ 가 독립이고 각각 $\{0, 1, 2\}$ 위에서 균등하다고 하자. 합성곱 공식을 써서 $X + Y$ 의 확률질량함수를 구하고, 확률의 합이 1임을 확인하여라.

??? success "연습문제 1 풀이"
    **1단계: 합의 범위와 합성곱 식.** $p_X(b) = p_Y(b) = \tfrac{1}{3}$ 이 $b \in \{0,1,2\}$ 에서 성립한다. $X$ 와 $Y$ 가 각각 $0$ 부터 $2$ 까지의 값을 가지므로 $a = X + Y$ 의 받침은 $\{0, 1, 2, 3, 4\}$ 이다. 합성곱 공식을 쓰면 다음과 같다.

    $$
    p_{X+Y}(a) = \sum_{b} p_X(b) \, p_Y(a - b) = \frac{1}{9} \sum_{b} 1
    $$

    합은 $b \in \{0,1,2\}$ 이면서 동시에 $a - b \in \{0,1,2\}$ 인 $b$ 에 대하여 취하므로, 결국 $\max(0, a-2) \leq b \leq \min(2, a)$ 를 만족하는 정수 $b$ 의 개수를 세면 된다.

    $$
    p_{X+Y}(a) = \frac{1}{9}\Big[\min(2, a) - \max(0, a-2) + 1\Big]
    $$

    **2단계: 값을 하나씩 세기.** 각 $a$ 마다 $(b, a-b)$ 꼴의 순서쌍을 직접 나열하면 알아보기 쉽다.

    | $a$ | 가능한 $(b,\, a-b)$ | 항의 개수 | $p_{X+Y}(a)$ |
    |:---:|:---|:---:|:---:|
    | $0$ | $(0,0)$ | $1$ | $1/9$ |
    | $1$ | $(0,1), (1,0)$ | $2$ | $2/9$ |
    | $2$ | $(0,2), (1,1), (2,0)$ | $3$ | $3/9 = 1/3$ |
    | $3$ | $(1,2), (2,1)$ | $2$ | $2/9$ |
    | $4$ | $(2,2)$ | $1$ | $1/9$ |

    **3단계: 합이 1인지 확인.**

    $$
    \sum_{a=0}^{4} p_{X+Y}(a) = \frac{1}{9} + \frac{2}{9} + \frac{3}{9} + \frac{2}{9} + \frac{1}{9} = \frac{9}{9} = 1
    $$

    분자 $1, 2, 3, 2, 1$ 은 $9$ 개의 같은 정도로 일어나는 순서쌍 $(X, Y)$ 를 합에 따라 나눈 개수이다. 이 삼각형 모양은 주사위 두 개의 합에서 $1, 2, \ldots, 6, \ldots, 2, 1$ 이 나오는 것과 똑같은 까닭에서 생긴다. 균등한 확률질량함수를 자기 자신과 합성곱하면 삼각형이 된다. $\square$

---

**연습문제 2.**
$X \sim \text{Bin}(3, 1/2)$ 와 $Y \sim \text{Bin}(2, 1/2)$ 가 독립이라고 하자. 합성곱 공식을 써서 $P(X + Y = 3)$ 을 구하여라.

*힌트: $X$ 가 가질 수 있는 모든 값에 대하여 더한다.*

??? success "연습문제 2 풀이"
    **1단계: 더할 항을 고르기.** 합성곱 공식은 다음과 같다.

    $$
    P(X + Y = 3) = \sum_{b} P(X = b) \, P(Y = 3 - b)
    $$

    $X$ 의 받침은 $\{0,1,2,3\}$ 이고 $Y$ 의 받침은 $\{0,1,2\}$ 이다. $3 - b \in \{0,1,2\}$ 이려면 $b \geq 1$ 이어야 하므로 살아남는 항은 $b = 1, 2, 3$ 뿐이다. $b = 0$ 은 $P(Y = 3) = 0$ 이라 사라진다.

    **2단계: 각 항 계산.** $p = 1/2$ 이므로 $P(X = b) = \binom{3}{b}\tfrac{1}{8}$ 이고 $P(Y = c) = \binom{2}{c}\tfrac{1}{4}$ 이다.

    | $b$ | $P(X = b)$ | $P(Y = 3-b)$ | 곱 |
    |:---:|:---:|:---:|:---:|
    | $1$ | $\binom{3}{1}/8 = 3/8$ | $\binom{2}{2}/4 = 1/4$ | $3/32$ |
    | $2$ | $\binom{3}{2}/8 = 3/8$ | $\binom{2}{1}/4 = 1/2$ | $3/16 = 6/32$ |
    | $3$ | $\binom{3}{3}/8 = 1/8$ | $\binom{2}{0}/4 = 1/4$ | $1/32$ |

    **3단계: 더하기.**

    $$
    P(X + Y = 3) = \frac{3}{32} + \frac{6}{32} + \frac{1}{32} = \frac{10}{32} = \frac{5}{16} = 0.3125
    $$

    **확인.** 성공확률이 $p = 1/2$ 로 같으므로 이항분포의 덧셈성에 따라 $X + Y \sim \text{Bin}(5, 1/2)$ 이다. 곧바로 계산하면 다음과 같다.

    $$
    P(X + Y = 3) = \binom{5}{3}\left(\frac{1}{2}\right)^{5} = \frac{10}{32} = \frac{5}{16}
    $$

    두 값이 일치한다. 위의 합성곱 합 $\binom{3}{1}\binom{2}{2} + \binom{3}{2}\binom{2}{1} + \binom{3}{3}\binom{2}{0} = 3 + 6 + 1 = 10 = \binom{5}{3}$ 은 바로 반데르몽드 항등식이며, 성공확률이 같을 때 이항분포가 합성곱에 대하여 닫혀 있는 까닭이 여기에 있다. $\square$
