# 격자경로와 투표 문제

## 문제 설정

**격자경로**란 정수 격자 $\mathbb{Z}^2$ 위에서 한 걸음마다 **오른쪽(R)** 또는 **위쪽(U)** 으로만 움직이는 경로이다. 여기서는 $(0, 0)$ 에서 $(m, n)$ 까지 가는 그런 경로의 개수를 센다.

## 기본적인 세기

!!! info "격자경로의 개수"
    오른쪽 걸음 $m$ 번과 위쪽 걸음 $n$ 번을 써서 $(0, 0)$ 에서 $(m, n)$ 까지 가는 격자경로의 개수는 다음과 같다.

    $$\binom{m + n}{m} = \binom{m + n}{n}$$

**증명.** 각 경로는 모두 $m + n$ 번의 걸음으로 이루어지며 그 가운데 $m$ 번은 R이고 $n$ 번은 U이어야 한다. $m + n$ 개의 자리 가운데 어느 $m$ 개가 R 걸음인지 고르면 경로가 완전히 정해진다. $\square$

**예.** $(0,0)$ 에서 $(3,2)$ 까지 가는 경로는 걸음 수가 $5$ 이고 그 가운데 오른쪽 걸음 $3$ 개를 고르면 되므로 $\binom{5}{3} = 10$ 개이다.

## 이항계수와의 연결

각 격자경로는 길이가 $m + n$ 이고 1이 정확히 $m$ 개(R 걸음), 0이 $n$ 개(U 걸음)인 이진 문자열에 대응된다. 이로써 다음 셋 사이에 일대일대응이 생긴다.

- $(0,0)$ 에서 $(m,n)$ 까지 가는 격자경로
- 길이가 $m+n$ 이고 1이 $m$ 개인 이진 문자열
- $\{1, 2, \ldots, m+n\}$ 의 원소 $m$ 개짜리 부분집합

## 주어진 점을 지나는 경로

$(0,0)$ 에서 $(m,n)$ 까지 가되 중간 지점 $(a,b)$ 를 지나는 격자경로의 개수는($0 \leq a \leq m$, $0 \leq b \leq n$) 다음과 같다.

$$\binom{a+b}{a} \cdot \binom{(m-a)+(n-b)}{m-a}$$

이는 **곱셈 법칙**에서 나온다. $(0,0)$ 에서 $(a,b)$ 까지 가는 경로와 $(a,b)$ 에서 $(m,n)$ 까지 가는 경로를 따로 세어 곱하면 된다.

## 어떤 영역을 피하는 경로: 반사 원리

!!! info "반사 원리(앙드레)"
    $(0,0)$ 에서 $(m,n)$ 까지 가면서 직선 $y = x + c$ 에 **닿거나 그것을 넘는** 격자경로의 개수는, 출발점을 반사한 $(−c, c)$ 에서 $(m, n)$ 까지 가는 격자경로의 전체 개수와 같고 그 값은 $\binom{m+n}{m+c}$ 이다($n > m + c$ 일 때).

반사 원리는 다음과 같은 곳에서 쓰이는 강력한 기법이다.

- **투표 문제**: 후보 A가 $a$ 표, B가 $b$ 표를 얻었다($a > b$). 개표가 진행되는 내내 A가 **줄곧 앞서** 있을 확률은 $\frac{a - b}{a + b}$ 이다.
- 확률보행의 **최댓값**의 분포를 유도하기
- 확률보행의 **아크사인 법칙**을 증명하기

## 투표 문제

**문제:** 어느 선거에서 후보 A가 $a$ 표, B가 $b$ 표를 얻었고 $a > b$ 이다. 개표 순서가 모두 같은 정도로 일어난다고 할 때, 개표가 진행되는 **내내 A가 B보다 줄곧 앞서** 있을 확률은 얼마인가?

!!! info "투표 문제의 답"

    $$P(\text{개표 내내 A가 줄곧 앞섬}) = \frac{a - b}{a + b}$$

**반사 원리를 이용한 증명.** 개표 순서는 모두 $\binom{a+b}{a}$ 가지이다. A가 내내 줄곧 앞서 있는 순서는 $(0,0)$ 에서 $(a,b)$ 까지 가면서 대각선 $y = x$ 에 **한 번도 닿지 않는** 격자경로에 대응된다. 반사 원리에 따라 대각선에 **닿는** 경로의 개수는 $\binom{a+b}{a-1}$ 이다. 따라서 다음을 얻는다.

$$P = \frac{\binom{a+b}{a} - \binom{a+b}{a-1}}{\binom{a+b}{a}} = 1 - \frac{a}{a+b-a+1} \cdot \frac{(a+b-a)!}{a!} \cdots = \frac{a-b}{a+b}$$

## 카탈란 수

$(0,0)$ 에서 $(n,n)$ 까지 가면서 대각선 $y = x$ 위로 **결코 올라가지 않는** 격자경로의 개수가 $n$ 번째 **카탈란 수**이다.

!!! info "카탈란 수"

    $$C_n = \frac{1}{n+1}\binom{2n}{n}$$

처음 몇 개의 값은 $C_0 = 1, C_1 = 1, C_2 = 2, C_3 = 5, C_4 = 14, C_5 = 42$ 이다.

**유도.** $(0,0)$ 에서 $(n,n)$ 까지 가는 경로는 모두 $\binom{2n}{n}$ 개이다. 대각선을 넘는 나쁜 경로들은 $y = x + 1$ 에 대한 반사를 통해 $(−1, 1)$ 에서 $(n, n)$ 까지 가는 경로들과 일대일로 대응되며, 그 개수는 $\binom{2n}{n+1}$ 이다. 따라서 다음을 얻는다.

$$C_n = \binom{2n}{n} - \binom{2n}{n+1} = \frac{1}{n+1}\binom{2n}{n}$$

카탈란 수는 여러 조합적 대상의 개수를 센다. 올바른 괄호 짜임새, 마디가 $n$ 개인 이진나무, 다각형의 삼각분할, 교차하지 않는 분할 등이 그 예이다.

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from math import comb, factorial

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# --- 1번 칸: (0,0)에서 (3,2)까지 가는 모든 격자경로 ---
from itertools import combinations

m, n = 3, 2
total_steps = m + n
paths = list(combinations(range(total_steps), m))  # R 걸음의 자리

for path_r in paths:
    x, y = [0], [0]
    for step in range(total_steps):
        if step in path_r:
            x.append(x[-1] + 1)
            y.append(y[-1])
        else:
            x.append(x[-1])
            y.append(y[-1] + 1)
    axes[0].plot(x, y, alpha=0.5, lw=1.5)

axes[0].set_title(f'All {comb(total_steps, m)} lattice paths (0,0)→({m},{n})')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[0].set_xticks(range(m + 1))
axes[0].set_yticks(range(n + 1))
axes[0].grid(True, alpha=0.3)
axes[0].set_aspect('equal')

# --- 2번 칸: 투표 문제 모의실험 ---
np.random.seed(42)
a_votes, b_votes = 7, 3
n_sim = 100000
ahead_count = 0

for _ in range(n_sim):
    ballot = np.random.permutation([1]*a_votes + [-1]*b_votes)
    cumsum = np.cumsum(ballot)
    if np.all(cumsum > 0):
        ahead_count += 1

p_sim = ahead_count / n_sim
p_theory = (a_votes - b_votes) / (a_votes + b_votes)

axes[1].bar(['Simulated', 'Theory'], [p_sim, p_theory],
            color=['steelblue', 'coral'], alpha=0.7)
axes[1].set_title(f'Ballot Problem: a={a_votes}, b={b_votes}')
axes[1].set_ylabel('P(A strictly ahead)')
for i, v in enumerate([p_sim, p_theory]):
    axes[1].text(i, v + 0.01, f'{v:.4f}', ha='center', fontsize=11)
axes[1].grid(True, alpha=0.3)

# --- 3번 칸: 카탈란 수 ---
ns = np.arange(0, 15)
catalans = [comb(2*nn, nn) // (nn + 1) for nn in ns]

axes[2].bar(ns, catalans, color='steelblue', alpha=0.7)
axes[2].set_title('Catalan Numbers $C_n$')
axes[2].set_xlabel('n')
axes[2].set_ylabel('$C_n$')
axes[2].set_yscale('log')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('lattice_paths.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 연습문제

**연습문제 1.** $(0,0)$ 에서 $(5,3)$ 까지 가는 격자경로는 몇 개인가? 그 가운데 점 $(2,1)$ 을 지나는 것은 몇 개인가?

??? success "연습문제 1 풀이"
    전체 경로: $\binom{8}{5} = 56$.

    $(2,1)$ 을 지나는 경로는 $(0,0)$ 에서 $(2,1)$ 까지 가는 경로의 수와 $(2,1)$ 에서 $(5,3)$ 까지 가는 경로의 수를 곱한 것이다.

    $$
    \binom{3}{2} \cdot \binom{5}{3} = 3 \times 10 = 30
    $$

---

**연습문제 2.** 투표 문제에서 후보 A가 10표, 후보 B가 4표를 얻었다. 개표가 진행되는 내내 A가 B보다 줄곧 앞서 있을 확률은 얼마인가?

??? success "연습문제 2 풀이"
    투표 문제의 공식에 따라 다음을 얻는다.

    $$
    P(\text{개표 내내 A가 줄곧 앞섬}) = \frac{a - b}{a + b} = \frac{10 - 4}{10 + 4} = \frac{6}{14} = \frac{3}{7} \approx 0.4286
    $$

---

**연습문제 3.** 여섯 번째 카탈란 수 $C_6$ 을 구하고, 공식 $C_n = \frac{1}{n+1}\binom{2n}{n}$ 으로 확인하여라.

??? success "연습문제 3 풀이"
    $$
    C_6 = \frac{1}{7}\binom{12}{6} = \frac{924}{7} = 132
    $$

    점화식 $C_n = \sum_{i=0}^{n-1} C_i C_{n-1-i}$ 로도 확인할 수 있다.

    $C_6 = C_0 C_5 + C_1 C_4 + C_2 C_3 + C_3 C_2 + C_4 C_1 + C_5 C_0 = 42 + 14 + 10 + 10 + 14 + 42 = 132$. $\checkmark$

---

**연습문제 4.** $(0,0)$ 에서 $(n,n)$ 까지 가면서 대각선 $y = x$ 에 닿기는 하되 결코 넘지 않는 격자경로의 개수가 $\binom{2n}{n} - 2\binom{2n}{n+1}/(n+1) \cdot (n+1)$ 임을 증명하여라. 그리고 이를 간단히 하여 $C_n$ 과 같음을 보여라.

??? success "연습문제 4 풀이"
    $(0,0)$ 에서 $(n,n)$ 까지 가는 경로는 모두 $\binom{2n}{n}$ 개이다.

    대각선을 넘는(어느 순간 $y = x$ 위로 올라가는) 경로는 반사 원리로 셀 수 있다. 처음 넘는 지점 뒤쪽 부분을 $y = x + 1$ 에 대하여 반사하면 $(-1, 1)$ 에서 $(n, n)$ 까지 가는 경로, 즉 오른쪽 걸음 $n+1$ 번과 위쪽 걸음 $n-1$ 번으로 이루어진 경로와 일대일로 대응된다.

    $$
    \text{나쁜 경로의 수} = \binom{2n}{n+1}
    $$

    따라서 좋은 경로(결코 넘지 않는 경로)의 개수는 다음과 같다.

    $$
    \binom{2n}{n} - \binom{2n}{n+1} = \frac{(2n)!}{n!\,n!} - \frac{(2n)!}{(n+1)!\,(n-1)!} = \frac{(2n)!}{n!\,n!}\left(1 - \frac{n}{n+1}\right) = \frac{1}{n+1}\binom{2n}{n} = C_n
    $$

    $\square$

---

**연습문제 5.** 어느 도시의 길이 동서로 4블록, 남북으로 3블록인 격자를 이룬다. 한 사람이 남서쪽 모퉁이에서 출발하여 북쪽 또는 동쪽으로만 걸어 북동쪽 모퉁이에 닿으려 한다. 어느 한 교차로(동쪽으로 2블록, 북쪽으로 1블록 지점)가 막혀 있다면 갈 수 있는 경로는 몇 개인가?

??? success "연습문제 5 풀이"
    제한이 없을 때의 전체 경로: $\binom{7}{4} = 35$.

    막힌 점 $(2,1)$ 을 지나는 경로는 $(0,0)$ 에서 $(2,1)$ 까지 가는 경로의 수와 $(2,1)$ 에서 $(4,3)$ 까지 가는 경로의 수를 곱한 것이다.

    $$
    \binom{3}{2} \cdot \binom{4}{2} = 3 \times 6 = 18
    $$

    따라서 갈 수 있는 경로는 $35 - 18 = 17$ 개이다.
