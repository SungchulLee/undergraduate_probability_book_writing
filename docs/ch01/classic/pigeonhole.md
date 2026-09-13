# 비둘기집 원리

## 정리의 서술

!!! info "비둘기집 원리"
    물건 $n$ 개를 상자 $k$ 개에 나누어 넣고 $n > k$ 이면, **적어도 한 상자**에는 물건이 두 개 이상 들어간다.

**엄밀하게 말하면:** 함수 $f: A \to B$ 에서 $|A| > |B|$ 이면 $f$ 는 단사가 아니다. 즉 $A$ 안에 $f(a_1) = f(a_2)$ 를 만족하는 서로 다른 $a_1, a_2$ 가 존재한다.

## 일반화된 비둘기집 원리

!!! info "일반화된 꼴"
    물건 $n$ 개를 상자 $k$ 개에 나누어 넣으면, 적어도 한 상자에는 물건이 $\lceil n/k \rceil$ 개 이상 들어간다.

**증명.** 모든 상자에 물건이 많아야 $\lceil n/k \rceil - 1$ 개씩 들어 있다면 전체는 많아야 $k(\lceil n/k \rceil - 1) < k \cdot n/k = n$ 이 되어 모순이다. $\square$

## 고전적인 응용

### 악수 보조정리

**주장:** $n \geq 2$ 명이 모인 어떤 자리에서든 악수한 횟수가 같은 사람이 적어도 두 명 있다.

**증명.** 각 사람이 악수할 수 있는 횟수는 0부터 $n - 1$ 까지이므로 가능한 값이 $n$ 가지이다. 그런데 0과 $n - 1$ 이 동시에 나타날 수는 없다(누군가 모든 사람과 악수했다면 악수를 한 번도 하지 않은 사람은 없다). 그러므로 $n$ 명에 대하여 가능한 값은 많아야 $n - 1$ 가지이다. 비둘기집 원리에 따라 적어도 두 사람은 같은 횟수를 가진다. $\square$

### 부분집합의 합

**주장:** $\{1, 2, \ldots, 2n\}$ 에서 정수를 $n + 1$ 개 고르면, 그 가운데 연속한 두 수가 반드시 있다.

**증명.** $\{1, \ldots, 2n\}$ 을 $\{1,2\}, \{3,4\}, \ldots, \{2n-1, 2n\}$ 처럼 $n$ 개의 쌍으로 나눈다. 비둘기집 원리에 따라 고른 $n+1$ 개의 정수 가운데 둘은 같은 쌍에 들어간다. $\square$

### 나누어떨어짐

**주장:** 어떤 정수 $n+1$ 개를 고르더라도, 그 가운데 차가 $n$ 으로 나누어떨어지는 두 수가 있다.

**증명.** $n$ 으로 나눈 나머지는 $0, 1, \ldots, n-1$ 의 $n$ 가지뿐이다. 정수는 $n+1$ 개이고 상자(나머지 부류)는 $n$ 개이므로 두 수는 같은 나머지를 가져야 한다. 그 두 수의 차는 $n$ 으로 나누어떨어진다. $\square$

### 단조 부분수열 (에르되시–세케레시)

**주장:** 서로 다른 실수 $n^2 + 1$ 개로 이루어진 어떤 수열에도 길이가 $n + 1$ 인 단조 부분수열이 들어 있다.

**증명의 얼개.** 각 원소 $a_i$ 에 쌍 $(d_i, e_i)$ 를 붙이자. 여기서 $d_i$ 는 $a_i$ 에서 끝나는 가장 긴 증가 부분수열의 길이이고 $e_i$ 는 가장 긴 감소 부분수열의 길이이다. 모든 $d_i \leq n$ 이고 모든 $e_i \leq n$ 이라면 서로 다른 쌍은 많아야 $n^2$ 개인데 원소는 $n^2 + 1$ 개이므로 비둘기집 원리에 어긋난다. $\square$

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# --- 1번 칸: 생일 문제 꼴의 비둘기집 ---
np.random.seed(42)
n_people_range = range(2, 50)
n_trials = 10000

prob_shared = []
for n in n_people_range:
    count = 0
    for _ in range(n_trials):
        # n명을 태어난 달 12개에 배정한다 (k=12인 비둘기집)
        months = np.random.randint(0, 12, n)
        if len(np.unique(months)) < n:
            count += 1
    prob_shared.append(count / n_trials)

axes[0].plot(list(n_people_range), prob_shared, 'bo-', markersize=3)
axes[0].axhline(1.0, color='red', ls='--', alpha=0.5,
                label='Guaranteed at n=13')
axes[0].axvline(13, color='red', ls='--', alpha=0.5)
axes[0].set_title('P(shared birth month) vs n people (12 months)')
axes[0].set_xlabel('Number of people')
axes[0].set_ylabel('Probability')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# --- 2번 칸: 한 통에 들어가는 물건의 최대 개수 ---
n_items_list = [10, 20, 50, 100]
k_bins = 10
n_trials = 5000

for n_items in n_items_list:
    max_counts = []
    for _ in range(n_trials):
        bins = np.random.randint(0, k_bins, n_items)
        _, counts = np.unique(bins, return_counts=True)
        max_counts.append(counts.max())
    lower_bound = int(np.ceil(n_items / k_bins))
    axes[1].hist(max_counts, bins=range(0, max(max_counts)+2),
                 density=True, alpha=0.4,
                 label=f'n={n_items}, ⌈n/k⌉={lower_bound}')

axes[1].set_title(f'Max items in any bin (k={k_bins} bins)')
axes[1].set_xlabel('Max count')
axes[1].set_ylabel('Frequency')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('pigeonhole.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 연습문제

**연습문제 1.** 어떤 6명을 모아 놓더라도 서로 아는 3명이 있거나 서로 모르는 3명이 있음을 보여라. (이것이 램지 수 $R(3,3) = 6$ 이다.)

??? success "연습문제 1 풀이"
    한 사람 $P$ 를 고정하자. 나머지 5명은 저마다 $P$ 를 알거나 모른다. 비둘기집 원리에 따라 적어도 $\lceil 5/2 \rceil = 3$ 명은 같은 쪽에 속한다.

    **경우 1:** 적어도 3명이 $P$ 를 안다. 이들을 $A, B, C$ 라 하자. $A, B, C$ 가운데 서로 아는 쌍이 있다면 그 쌍과 $P$ 가 서로 아는 3명을 이룬다. $A, B, C$ 가운데 서로 아는 쌍이 하나도 없다면 $A, B, C$ 가 서로 모르는 3명이다.

    **경우 2:** 적어도 3명이 $P$ 를 모른다. 논증은 대칭이다. 그 셋 가운데 서로 모르는 쌍이 있으면 그 쌍과 $P$ 가 서로 모르는 3명을 이루고, 그렇지 않으면 셋이 모두 서로 안다. $\square$

---

**연습문제 2.** $n$ 명으로 이루어진 어떤 무리에서도 그 무리 안의 친구 수가 같은 사람이 적어도 두 명 있음을 증명하여라("친구 관계"는 대칭이라고 하자).

??? success "연습문제 2 풀이"
    각 사람의 친구 수는 0부터 $n-1$ 까지이므로 가능한 값이 $n$ 가지이다. 그런데 0과 $n-1$ 이 동시에 나타날 수는 없다. 누군가 모든 사람과 친구라면 친구가 0명인 사람은 없기 때문이다. 그러므로 실제로 나올 수 있는 친구 수는 많아야 $n-1$ 가지이다. 사람은 $n$ 명이고 가능한 값은 많아야 $n-1$ 가지이므로, 비둘기집 원리에 따라 적어도 두 사람의 친구 수가 같다. $\square$

---

**연습문제 3.** 어떤 정수 52개를 고르더라도 그 가운데 차가 51로 나누어떨어지는 두 수가 있음을 증명하여라.

??? success "연습문제 3 풀이"
    51로 나눈 나머지는 $\{0, 1, 2, \ldots, 50\}$ 의 51가지뿐이다. 정수는 52개이고 나머지 부류는 51개이므로, 비둘기집 원리에 따라 적어도 두 정수는 51로 나눈 나머지가 같다. 그 두 수의 차는 51로 나누어떨어진다. $\square$

---

**연습문제 4.** 양말 서랍에 빨간 양말 10짝, 파란 양말 8짝, 초록 양말 6짝이 뒤섞여 있다. 보지 않고 양말을 꺼낼 때 다음을 확실히 보장하려면 최소 몇 짝을 꺼내야 하는가?

**(a)** 같은 색 한 켤레

**(b)** 빨간 양말 두 짝 이상

??? success "연습문제 4 풀이"
    **(a)** 색은 3가지이다. 비둘기집 원리에 따라 $3 + 1 = 4$ 짝을 꺼내면 같은 색이 두 짝 이상 나오는 것이 보장된다.

    **(b)** 가장 나쁜 경우에는 빨간 양말이 나오기 전에 파란 양말 8짝과 초록 양말 6짝을 모두 꺼낼 수도 있다. 따라서 빨간 양말 2짝을 보장하려면 $8 + 6 + 2 = 16$ 짝을 꺼내야 한다.

---

**연습문제 5.** $a_1, a_2, \ldots, a_{10}$ 을 $\{1, 2, \ldots, 50\}$ 에서 고른 서로 다른 정수라 하자. $\{a_1, \ldots, a_{10}\}$ 의 서로소인 공집합이 아닌 부분집합 $A$ 와 $B$ 가운데 $\sum_{a \in A} a = \sum_{b \in B} b$ 를 만족하는 것이 존재함을 증명하여라.

??? success "연습문제 5 풀이"
    $\{a_1, \ldots, a_{10}\}$ 의 공집합이 아닌 부분집합은 $2^{10} - 1 = 1023$ 개이다. 각 부분집합의 원소의 합은 1 이상 $41 + 42 + \cdots + 50 = 455$ 이하이다($\{1, \ldots, 50\}$ 에서 서로 다른 10개를 골랐을 때의 최댓값이다). $1023 > 455$ 이므로 비둘기집 원리에 따라 원소의 합이 같은 서로 다른 공집합 아닌 부분집합 $S_1$ 과 $S_2$ 가 존재한다. $A = S_1 \setminus S_2$, $B = S_2 \setminus S_1$ 이라 두자. 그러면 $A$ 와 $B$ 는 서로소이고 공집합이 아니며($S_1 \neq S_2$ 이므로), 다음이 성립한다.

    $$
    \sum_{a \in A} a = \sum_{b \in B} b
    $$

    $\square$
