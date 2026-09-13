# 성질과 이산균등분포의 합

## 평균과 분산

!!! info "이산균등분포의 적률"
    $X \sim \text{DiscreteUniform}(a, a+1, \ldots, b)$ 이면(같은 정도로 일어나는 값 $n = b - a + 1$ 개를 갖는다) 다음이 성립한다.

    $$E[X] = \frac{a + b}{2}, \qquad \text{Var}(X) = \frac{n^2 - 1}{12}$$

    여기서 $n = b - a + 1$ 은 값의 개수이다.

**평균의 유도.** 확률질량함수가 $(a+b)/2$ 를 축으로 대칭이라는 점에서 알 수 있고, 직접 구해도 된다.

$$E[X] = \frac{1}{n}\sum_{k=a}^{b} k = \frac{1}{n} \cdot \frac{n(a+b)}{2} = \frac{a+b}{2}$$

**분산의 유도.** $X \sim \text{DiscreteUniform}(1, 2, \ldots, n)$ 에 대하여 다음과 같다.

$$E[X^2] = \frac{1}{n}\sum_{k=1}^{n} k^2 = \frac{(n+1)(2n+1)}{6}$$

$$\text{Var}(X) = \frac{(n+1)(2n+1)}{6} - \left(\frac{n+1}{2}\right)^2 = \frac{n^2 - 1}{12}$$

일반적인 경우 $X \sim \text{DiscreteUniform}(a, \ldots, b)$ 에서는 $Y \sim \text{DiscreteUniform}(1, \ldots, n)$ 에 대하여 $X = a - 1 + Y$ 임에 유의하자. 그러면 $\text{Var}(X) = \text{Var}(Y) = \frac{n^2-1}{12}$ 이다.

## 특별한 경우

**공정한 주사위:** $X \sim \text{DiscreteUniform}(1, 2, 3, 4, 5, 6)$

$$E[X] = 3.5, \qquad \text{Var}(X) = \frac{35}{12} \approx 2.917$$

**공정한 동전(0/1):** $X \sim \text{DiscreteUniform}(0, 1) = \text{Bernoulli}(1/2)$

$$E[X] = 0.5, \qquad \text{Var}(X) = \frac{3}{12} = 0.25$$

## 고전적 확률과의 관계

이산균등분포는 **같은 정도로 일어나는 결과**를 수학적으로 다듬은 것이다. 표본공간에 결과가 $n$ 개 있고 모두 같은 정도로 일어난다면, 결과에 대한 어떤 수치 함수든 이산균등분포를 따르거나 그것의 함수가 된다.

## 누적분포함수

$X \sim \text{DiscreteUniform}(1, \ldots, n)$ 의 누적분포함수는 **계단함수**이다.

$$F(x) = \frac{\lfloor x \rfloor}{n}, \quad 1 \leq x \leq n$$

## 적률생성함수

적률생성함수는 다음과 같다.

$$M_X(t) = \frac{1}{n}\sum_{k=1}^{n} e^{tk} = \frac{e^t(1 - e^{nt})}{n(1 - e^t)}, \quad t \neq 0$$

이는 공비가 $e^t$ 인 등비급수이다.

## 서로 독립인 이산균등분포의 합

$X_1, X_2$ 가 서로 독립인 $\text{DiscreteUniform}(1, \ldots, n)$ 이면 $S = X_1 + X_2$ 의 확률질량함수는 $\{2, 3, \ldots, 2n\}$ 위에서 **삼각형** 모양이 된다.

$$P(S = s) = \frac{n - |s - (n+1)|}{n^2}$$

가장 익숙한 경우는 주사위 두 개를 굴리는 것이다. 이때 $P(S = 7)$ 이 가장 크다.

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# --- 첫째 칸: n 을 바꾸어 가며 본 확률질량함수와 누적분포함수 ---
for n, color in zip([4, 6, 10], ['blue', 'red', 'green']):
    vals = np.arange(1, n + 1)
    pmf = np.ones(n) / n
    axes[0].bar(vals + (n - 6) * 0.15, pmf, width=0.3, alpha=0.6,
                color=color, label=f'n={n}, E={n/2+.5:.1f}')

axes[0].set_title('Discrete Uniform PMF')
axes[0].set_xlabel('x')
axes[0].set_ylabel('P(X=x)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# --- 둘째 칸: 주사위 두 개의 눈의 합 ---
n_die = 6
sums = np.arange(2, 2 * n_die + 1)
pmf_sum = np.array([min(s - 1, 2 * n_die + 1 - s)
                     for s in sums]) / n_die**2

axes[1].bar(sums, pmf_sum, color='steelblue', alpha=0.7)
axes[1].set_title('Sum of Two Fair Dice')
axes[1].set_xlabel('Sum')
axes[1].set_ylabel('Probability')
for s, p in zip(sums, pmf_sum):
    axes[1].text(s, p + 0.005, f'{p:.3f}', ha='center', fontsize=7, rotation=45)
axes[1].grid(True, alpha=0.3)

# --- 셋째 칸: 이산균등분포의 합에 대한 중심극한정리 ---
np.random.seed(42)
n_sim = 100000
ns_sum = [1, 2, 5, 12]
n_die = 6

for n, color in zip(ns_sum, ['red', 'orange', 'green', 'blue']):
    s = np.sum(np.random.randint(1, n_die + 1, (n_sim, n)), axis=1)
    axes[2].hist(s, bins=range(n, n * n_die + 2), density=True,
                 alpha=0.3, color=color, label=f'n={n}')

    # 정규근사
    mu = n * 3.5
    sigma = np.sqrt(n * 35 / 12)
    x = np.linspace(n, n * n_die, 200)
    axes[2].plot(x, stats.norm.pdf(x, mu, sigma), color=color, lw=1.5)

axes[2].set_title('Sum of n Dice → Normal (CLT)')
axes[2].set_xlabel('Sum')
axes[2].legend(fontsize=9)
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('discrete_uniform_properties.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 연습문제

**연습문제 1.** 공정한 주사위 두 개를 서로 독립으로 굴린다. $S$ 를 눈의 합이라 하자. $P(S = 7)$ 을 구하고 7이 가장 잘 나오는 합인 까닭을 설명하여라.
