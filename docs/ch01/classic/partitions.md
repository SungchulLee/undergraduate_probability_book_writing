# 분할 문제와 열두 가지 길

## 물건을 상자에 나누어 넣기

많은 세기 문제는 물건 $n$ 개를 여러 조건 아래 상자 $k$ 개에 나누어 넣는 문제로 환원된다. 답은 물건과 상자가 **서로 구별되는지** 아니면 **구별되지 않는지**에 따라 달라진다.

## 경우별 요약

!!! info "나누어 넣기의 경우의 수"
    | 물건 | 상자 | 조건 | 공식 |
    |:---:|:---:|:---:|:---:|
    | 구별됨 | 구별됨 | 없음 | $k^n$ |
    | 구별됨 | 구별됨 | 상자마다 많아야 1개 ($n \leq k$) | $k!/(k-n)!$ |
    | 구별됨 | 구별됨 | 상자마다 꼭 1개 ($n = k$) | $k!$ |
    | 구별 안 됨 | 구별됨 | 없음 | $\binom{n+k-1}{k-1}$ |
    | 구별 안 됨 | 구별됨 | 상자마다 적어도 1개 | $\binom{n-1}{k-1}$ |
    | 구별됨 | 구별 안 됨 | 없음 | $\sum_{j=1}^{k} S(n,j)$ |
    | 구별 안 됨 | 구별 안 됨 | 없음 | $p_k(n)$ |

여기서 $S(n, k)$ 는 **제2종 스털링 수**를, $p_k(n)$ 은 **$n$ 을 많아야 $k$ 개의 조각으로 나누는 분할의 개수**를 뜻한다.

## 경우 1: 구별되는 물건, 구별되는 상자 (조건 없음)

$n$ 개의 물건이 저마다 따로 $k$ 개의 상자 가운데 하나로 들어간다. 곱셈 법칙에 따라 $k^n$ 이다.

**예.** 학생 3명을 모둠 4개에 배정하는 방법은 $4^3 = 64$ 가지이다.

## 경우 2: 구별되지 않는 물건, 구별되는 상자 — 막대와 별

이것이 바로 고전적인 **막대와 별** 문제이다(1.3절에서 다루었다).

!!! info "막대와 별"
    똑같은 물건 $n$ 개를 서로 다른 상자 $k$ 개에 나누어 넣는 방법의 수는 다음과 같다.

    $$\binom{n + k - 1}{k - 1}$$

    "상자마다 적어도 1개"라는 조건이 붙으면 다음과 같다.

    $$\binom{n - 1}{k - 1}$$

**예.** 똑같은 과자 10개를 네 아이에게 나누어 주는 방법은 $\binom{13}{3} = 286$ 가지이다.

**모두 적어도 1개씩 받는 경우:** 먼저 아이마다 1개씩 주고(4개를 쓴다), 남은 6개를 자유롭게 나누면 $\binom{9}{3} = 84$ 가지이다.

## 경우 3: 구별되는 물건, 구별되지 않는 상자 — 스털링 수

상자가 서로 구별되지 않을 때, 서로 다른 $n$ 개의 물건을 공집합이 아닌 정확히 $k$ 개의 묶음으로 나누는 방법의 수가 **제2종 스털링 수** $S(n, k)$ 이다.

!!! info "제2종 스털링 수"
    $S(n, k)$ 는 원소가 $n$ 개인 집합을 공집합이 아닌 정확히 $k$ 개의 부분집합으로 나누는 방법의 수를 센다.

    $$S(n, k) = \frac{1}{k!} \sum_{j=0}^{k} (-1)^{k-j} \binom{k}{j} j^n$$

    **점화식:** $S(n, k) = k \cdot S(n-1, k) + S(n-1, k-1)$

    **경계 조건:** $S(n, 1) = S(n, n) = 1$ 이고, $n \geq 1$ 일 때 $S(n, 0) = 0$ 이다.

**예.** $\{a, b, c\}$ 를 공집합이 아닌 두 묶음으로 나누면 다음과 같다.

$\{a\}\{b,c\}$, $\{b\}\{a,c\}$, $\{c\}\{a,b\}$ — 따라서 $S(3, 2) = 3$ 이다.

## 경우 4: 구별되지 않는 물건, 구별되지 않는 상자 — 정수의 분할

$n$ 을 많아야 $k$ 개의 양의 정수의 합으로 쓰는(순서는 따지지 않는) 방법의 수가 **분할함수** $p_k(n)$ 이다.

**예.** 5를 많아야 3개의 조각으로 나누는 분할은 $5 = 5 = 4+1 = 3+2 = 3+1+1 = 2+2+1$ 이므로 $p_3(5) = 5$ 이다.

## 벨 수

**벨 수** $B_n$ 은 원소가 $n$ 개인 집합을 공집합이 아닌 부분집합들로 나누는 모든 분할의 개수를 센다(묶음의 개수는 몇이든 상관없다).

$$B_n = \sum_{k=0}^{n} S(n, k)$$

처음 몇 개는 $B_0 = 1, B_1 = 1, B_2 = 2, B_3 = 5, B_4 = 15, B_5 = 52$ 이다.

## 열두 가지 길

위의 표는 조합론자들이 **열두 가지 길**이라 부르는 것의 일부이다. 물건과 상자가 구별되는지, 그리고 상자에 몇 개든 담을 수 있는지 많아야 하나인지 적어도 하나인지에 따라 나누어 넣기 문제를 체계적으로 분류한 것이다.

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from math import comb, factorial
from functools import lru_cache

# 스털링 수
@lru_cache(maxsize=None)
def stirling2(n, k):
    if k == 0:
        return 1 if n == 0 else 0
    if k == 1 or k == n:
        return 1
    if k > n:
        return 0
    return k * stirling2(n - 1, k) + stirling2(n - 1, k - 1)

# 벨 수
def bell(n):
    return sum(stirling2(n, k) for k in range(n + 1))

# 정수의 분할
@lru_cache(maxsize=None)
def partitions(n, max_part=None):
    if max_part is None:
        max_part = n
    if n == 0:
        return 1
    if n < 0 or max_part == 0:
        return 0
    return partitions(n - max_part, max_part) + partitions(n, max_part - 1)

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# --- 1번 칸: 스털링 삼각형 ---
N = 8
triangle = np.zeros((N + 1, N + 1))
for n in range(N + 1):
    for k in range(N + 1):
        triangle[n, k] = stirling2(n, k)

im = axes[0].imshow(triangle[1:, 1:], cmap='YlOrRd', aspect='auto')
for i in range(N):
    for j in range(N):
        val = int(triangle[i + 1, j + 1])
        if val > 0:
            axes[0].text(j, i, str(val), ha='center', va='center', fontsize=7)
axes[0].set_title('Stirling Numbers S(n,k)')
axes[0].set_xlabel('k')
axes[0].set_ylabel('n')
axes[0].set_xticks(range(N))
axes[0].set_xticklabels(range(1, N + 1))
axes[0].set_yticks(range(N))
axes[0].set_yticklabels(range(1, N + 1))

# --- 2번 칸: 벨 수 ---
ns = range(0, 13)
bells = [bell(n) for n in ns]
axes[1].bar(list(ns), bells, color='steelblue', alpha=0.7)
axes[1].set_title('Bell Numbers $B_n$')
axes[1].set_xlabel('n')
axes[1].set_ylabel('$B_n$')
axes[1].set_yscale('log')
axes[1].grid(True, alpha=0.3)

# --- 3번 칸: 나누어 넣기 공식들 견주어 보기 ---
n_objects = 6
ks = range(1, 7)

dist_dist = [k**n_objects for k in ks]           # 구별되는 물건, 구별되는 상자
stars_bars = [comb(n_objects + k - 1, k - 1) for k in ks]  # 구별 안 되는 물건, 구별되는 상자
stirling_vals = [sum(stirling2(n_objects, j) for j in range(1, k+1)) for k in ks]
part_vals = [partitions(n_objects, k) for k in ks]

axes[2].plot(list(ks), dist_dist, 'ro-', label='Dist-Dist: $k^n$', lw=2)
axes[2].plot(list(ks), stars_bars, 'bs-', label='Indist-Dist: Stars&Bars', lw=2)
axes[2].plot(list(ks), stirling_vals, 'g^-', label='Dist-Indist: Stirling', lw=2)
axes[2].plot(list(ks), part_vals, 'mD-', label='Indist-Indist: Partitions', lw=2)
axes[2].set_title(f'Distribution Problems (n={n_objects} objects)')
axes[2].set_xlabel('k (number of boxes)')
axes[2].set_ylabel('Count')
axes[2].set_yscale('log')
axes[2].legend(fontsize=8)
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('partitions.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 연습문제

**연습문제 1.** 똑같은 과자 8개를 서로 다른 세 아이에게 나누어 주되 아이마다 적어도 2개씩 받도록 한다. 몇 가지 방법이 있는가?

??? success "연습문제 1 풀이"
    먼저 아이마다 2개씩 준다($6$ 개를 쓴다). 그러고 나서 남은 $8 - 6 = 2$ 개를 세 아이에게 자유롭게 나눈다. 막대와 별에 따라 다음을 얻는다.

    $$
    \binom{2 + 3 - 1}{3 - 1} = \binom{4}{2} = 6
    $$

---

**연습문제 2.** 점화식을 이용하여 스털링 수 $S(4, 2)$ 를 구하여라. 그리고 $\{1, 2, 3, 4\}$ 를 공집합이 아닌 정확히 두 부분집합으로 나누는 분할을 모두 적어라.

??? success "연습문제 2 풀이"
    $S(n, k) = k \cdot S(n-1, k) + S(n-1, k-1)$ 을 쓰면 다음을 얻는다.

    $$
    S(4, 2) = 2 \cdot S(3, 2) + S(3, 1) = 2 \cdot 3 + 1 = 7
    $$

    7개의 분할은 다음과 같다.

    $\{1\}\{2,3,4\}$, $\{2\}\{1,3,4\}$, $\{3\}\{1,2,4\}$, $\{4\}\{1,2,3\}$,
    $\{1,2\}\{3,4\}$, $\{1,3\}\{2,4\}$, $\{1,4\}\{2,3\}$.

---

**연습문제 3.** 7을 정확히 3개의 조각으로 나누는 정수 분할을 모두 구하여라. 몇 개인가?

??? success "연습문제 3 풀이"
    $a \geq b \geq c \geq 1$ 이면서 $a + b + c = 7$ 인 것을 찾으면 된다.

    - $5 + 1 + 1$
    - $4 + 2 + 1$
    - $3 + 3 + 1$
    - $3 + 2 + 2$

    그런 분할은 **4개**이다.

---

**연습문제 4.** $B_n$ 이 $n$ 번째 벨 수일 때 $B_{n+1} = \sum_{k=0}^{n} \binom{n}{k} B_k$ 임을 증명하여라.

??? success "연습문제 4 풀이"
    원소가 $n+1$ 개인 집합 $\{1, 2, \ldots, n+1\}$ 을 생각하자. 이 집합을 나눌 때, 먼저 $\{1, \ldots, n\}$ 의 원소 가운데 어느 것이 원소 $n+1$ 과 같은 묶음에 들어가는지 정한다. $n+1$ 을 품은 묶음에 $\{1, \ldots, n\}$ 에서 고른 원소가 $n - k$ 개 더 들어 있다고 하면, 그것을 고르는 방법은 $\binom{n}{n-k} = \binom{n}{k}$ 가지이다. 남은 $k$ 개의 원소는 아무렇게나 나눌 수 있으므로 $B_k$ 가지 분할이 생긴다. $k$ 에 대하여 모두 더하면 다음을 얻는다.

    $$
    B_{n+1} = \sum_{k=0}^{n} \binom{n}{k} B_k
    $$

    $\square$

---

**연습문제 5.** 어느 교수가 서로 다른 과제 5개를 서로 구별되지 않는 연구 모둠 3개에 배정한다(모둠마다 적어도 하나는 맡아야 한다). 몇 가지 방법이 있는가?

??? success "연습문제 5 풀이"
    모둠이 서로 구별되지 않고 어느 모둠도 비어서는 안 되므로 $S(5, 3)$ 을 구하면 된다.

    점화식을 쓰면 $S(5, 3) = 3 \cdot S(4, 3) + S(4, 2) = 3 \cdot 6 + 7 = 25$ 이다.

    따라서 **25**가지이다.
