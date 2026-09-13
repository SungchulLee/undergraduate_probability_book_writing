# 독립인 균등확률변수의 합

## 균등확률변수 두 개의 합성곱

!!! info "i.i.d. U(-1/2, 1/2) 두 개의 합"
    $X$ 와 $Y$ 가 독립이고 둘 다 $U(-1/2, 1/2)$ 를 따르면, $X + Y$ 는 **삼각분포**를 따른다.

    $$f_{X+Y}(a) = (1 - |a|)^+, \quad -1 \leq a \leq 1$$

    여기에서 $(x)^+ = \max(x, 0)$ 이다.

### 유도 (0 ≤ a ≤ 1 인 경우)

대칭성이 있으므로 $0 \leq a \leq 1$ 인 경우에 대해서만 합성곱을 계산하면 충분하다.

$$f_{X+Y}(a) = \int_{-\infty}^{\infty} f_X(b) \, f_Y(a - b) \, db$$

**적분 구간 정하기:** 두 밀도함수 모두 $(-1/2, 1/2)$ 위에서 $1$ 이고 그 밖에서는 $0$ 이다. 따라서 다음이 성립해야 한다.

$$-\frac{1}{2} \leq b \leq \frac{1}{2} \quad \text{이고} \quad -\frac{1}{2} \leq a - b \leq \frac{1}{2}$$

둘째 조건에서 $a - \frac{1}{2} \leq b \leq a + \frac{1}{2}$ 을 얻는다.

$0 \leq a \leq 1$ 일 때 두 구간의 교집합은 $a - \frac{1}{2} \leq b \leq \frac{1}{2}$ 이다.

$$f_{X+Y}(a) = \int_{a - 1/2}^{1/2} 1 \, db = \frac{1}{2} - \left(a - \frac{1}{2}\right) = 1 - a$$

대칭성에 따라 $-1 \leq a \leq 0$ 일 때에는 $f_{X+Y}(a) = 1 + a$ 이다. 둘을 합치면 $f_{X+Y}(a) = 1 - |a|$ 이다.

## 일반적인 경우: i.i.d. U(0, 1) 두 개의 합

$X, Y$ 가 i.i.d. $U(0, 1)$ 이면 $X + Y$ 는 $(0, 2)$ 위의 **삼각분포**를 따른다.

$$f_{X+Y}(a) = \begin{cases} a & 0 \leq a \leq 1 \\ 2 - a & 1 < a \leq 2 \end{cases}$$

이는 $U(-1/2, 1/2)$ 에서 얻은 결과를 옮겨 놓은 것일 뿐이다. $X' = X - 1/2 \sim U(-1/2, 1/2)$ 로 놓으면 $X + Y = (X' + Y') + 1$ 이기 때문이다.

## 균등확률변수 n 개의 합

$n$ 이 커지면 중심극한정리에 따라 $S_n = X_1 + \cdots + X_n$ 의 분포가 정규분포에 가까워진다. 합성곱 $U * U$ 는 삼각형을 주고, $U * U * U$ 는 구간마다 이차식인 함수를 주며, 이런 식으로 이어진다. 일반적으로 $U(0,1)$ 을 $n$ 번 합성곱한 분포를 **어윈–홀 분포**라 하며, 이는 구간마다 $n-1$ 차 다항식으로 주어진다.

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 100000

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# i.i.d. U(-1/2, 1/2) 두 개의 합
X = np.random.uniform(-0.5, 0.5, n_sim)
Y = np.random.uniform(-0.5, 0.5, n_sim)
S = X + Y

a_vals = np.linspace(-1, 1, 200)
pdf_theory = np.maximum(1 - np.abs(a_vals), 0)

axes[0].hist(S, bins=100, density=True, alpha=0.5, color='steelblue',
             label='Simulated X+Y')
axes[0].plot(a_vals, pdf_theory, 'r-', lw=2, label='(1-|a|)⁺')
axes[0].set_title('X + Y where X, Y iid U(-1/2, 1/2)')
axes[0].set_xlabel('a')
axes[0].set_ylabel('Density')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# n 을 키워 가며 본 i.i.d. U(-1/2, 1/2) n 개의 합
colors = ['blue', 'red', 'green', 'orange', 'purple']
for i, n in enumerate([2, 3, 5, 10, 30]):
    samples = np.random.uniform(-0.5, 0.5, (n_sim, n))
    sums = samples.sum(axis=1)
    axes[1].hist(sums, bins=80, density=True, alpha=0.3,
                 color=colors[i % len(colors)], label=f'n={n}')

# n=30 에 대한 정규분포를 겹쳐 그린다
x_norm = np.linspace(-4, 4, 200)
axes[1].plot(x_norm, stats.norm.pdf(x_norm, loc=0, scale=np.sqrt(30/12)),
             'k-', lw=2, label='Normal approx (n=30)')
axes[1].set_title('Sum of n iid U(-1/2, 1/2) → Normal')
axes[1].set_xlabel('Sum')
axes[1].legend(fontsize=9)
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('sum_uniforms.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 연습문제

**연습문제 1.**
$X \sim U(0, 1)$ 과 $Y \sim U(0, 2)$ 가 독립이라고 하자. 모든 $a \geq 0$ 에 대하여 $f_{X+Y}(a)$ 를 구하여라.

*힌트: 받침 $0 \leq b \leq 1$ 과 $0 \leq a - b \leq 2$ 의 교집합을 잡아 적분 구간을 정한다. $0 \leq a \leq 1$, $1 < a \leq 2$, $2 < a \leq 3$ 의 세 경우로 나누어 생각한다.*
