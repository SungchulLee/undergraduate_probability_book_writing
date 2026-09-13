# 지시확률변수로 기댓값 구하기

## 지시확률변수 방법

많은 확률변수를 지시확률변수의 합으로 나타낼 수 있다.

$$
X = \sum_{i} \mathbf{1}_{A_i}
$$

기댓값의 선형성에 따라 다음을 얻는다.

$$
E[X] = \sum_{i} E[\mathbf{1}_{A_i}] = \sum_{i} P(A_i)
$$

이 방법은 **지시확률변수들이 독립인지 아닌지와 상관없이** 통하므로 확률론에서 가장 쓰임새 넓은 도구 가운데 하나이다.

---

## 지시확률변수로 분산 구하기

$X = \sum_{i=1}^m \mathbf{1}_{A_i}$ 일 때 분산은 좀 더 조심해야 한다.

$$
\text{Var}(X) = \sum_{i=1}^m \text{Var}(\mathbf{1}_{A_i}) + 2\sum_{1 \leq i < j \leq m} \text{Cov}(\mathbf{1}_{A_i}, \mathbf{1}_{A_j})
$$

여기서 각 항은 다음과 같다.

$$
\text{Var}(\mathbf{1}_{A_i}) = P(A_i)(1 - P(A_i))
$$

$$
\text{Cov}(\mathbf{1}_{A_i}, \mathbf{1}_{A_j}) = P(A_i \cap A_j) - P(A_i)P(A_j)
$$

**지시확률변수들이 독립이면** 공분산 항이 모두 사라지고 $\text{Var}(X) = \sum_i \text{Var}(\mathbf{1}_{A_i})$ 가 된다.

---

## 언제 그 합이 이항분포가 되는가

지시확률변수의 합 $X = \sum_{i=1}^m \mathbf{1}_{A_i}$ 가 $\text{Binomial}(m, p)$ 가 되려면 다음 두 조건이 **모두** 필요하다.

1. 각 $\mathbf{1}_{A_i} \sim \text{Bernoulli}(p)$ 이다(같은 $p$).
2. 지시확률변수들이 **상호독립**이다.

둘 중 하나라도 어긋나면 $X$ 는 이항분포가 **아니다**. 그래도 지시확률변수 방법으로 $E[X]$ 와 $\text{Var}(X)$ 는 여전히 구할 수 있다.

---

## 예: 지시확률변수로 보는 이항분포

앞면이 나올 확률이 $p$ 인 동전을 서로 독립으로 $n$ 번 던진다. $S$ 를 앞면의 수라 하자.

$$
S = \sum_{i=1}^n \mathbf{1}_{A_i}, \quad \mathbf{1}_{A_i} \stackrel{iid}{\sim} \text{Bernoulli}(p)
$$

지시확률변수들이 i.i.d. 이므로 다음을 얻는다.

$$
E[S] = np, \quad \text{Var}(S) = npq
$$

---

## 예: 이항분포가 아닌 경우 — 생일이 같은 짝

$n$ 명이 있고 각자의 생일은 365일 가운데 균등하게 고른 것이다. $S_n$ 을 생일이 같은 짝의 개수라 하자.

$$
S_n = \sum_{1 \leq i < j \leq n} \mathbf{1}_{A_{ij}}
$$

여기서 $A_{ij}$ 는 $i$ 번 사람과 $j$ 번 사람의 생일이 같은 사건이다.

**왜 이항분포가 아닌가**: 지시확률변수가 $m = \binom{n}{2}$ 개이고 각각 $p = 1/365$ 이지만, 이들은 **독립이 아니다**. ($A_{12}$ 와 $A_{13}$ 이 모두 일어나면 2번과 3번이 모두 1번과 생일이 같으므로 $A_{23}$ 이 일어나기 쉬워진다.)

그러나 이 지시확률변수들은 **쌍별로 독립**이므로 공분산 항이 사라진다.

$$
E[S_n] = \binom{n}{2} \cdot \frac{1}{365}
$$

$$
\text{Var}(S_n) = \binom{n}{2} \cdot \frac{1}{365} \cdot \frac{364}{365}
$$

---

## 예: 이항분포가 아닌 경우 — 빈 상자

공 $n$ 개와 상자 $M = 365$ 개가 있다. 각 공은 서로 독립으로 상자를 하나 균등하게 무작위로 고른다. $S_n$ 을 빈 상자의 개수라 하자.

$$
S_n = \sum_{i=1}^{365} \mathbf{1}_{A_i}
$$

여기서 $A_i$ 는 $i$ 번 상자가 비어 있는 사건이다. 각 $\mathbf{1}_{A_i} \sim \text{Bernoulli}(p)$ 이고 $p = \left(\frac{364}{365}\right)^n$ 이지만, 지시확률변수들은 **독립이 아니다**(어떤 상자가 비어 있으면 나머지 상자에 공이 들어 있을 가능성이 조금 커진다).

$$
E[S_n] = 365 \cdot p
$$

$$
\text{Var}(S_n) = 365 \cdot pq + 2\binom{365}{2} \left[\left(\frac{363}{365}\right)^n - p^2\right]
$$

---

## 파이썬 구현

```python
import numpy as np
from math import comb

# 생일이 같은 짝: 평균과 분산
def birthday_pairs_stats(n_people):
    m = comb(n_people, 2)
    p = 1 / 365
    mean = m * p
    var = m * p * (1 - p)  # 쌍별로 독립
    return mean, var

n = 30
mu, v = birthday_pairs_stats(n)
print(f"Birthday pairs (n={n}): E = {mu:.4f}, SD = {np.sqrt(v):.4f}")

# 빈 상자: 평균과 분산
def empty_bins_stats(n_balls, M=365):
    p = ((M - 1) / M) ** n_balls
    p2 = ((M - 2) / M) ** n_balls
    mean = M * p
    var = M * p * (1 - p) + 2 * comb(M, 2) * (p2 - p**2)
    return mean, var

n_balls = 100
mu, v = empty_bins_stats(n_balls)
print(f"Empty bins (n={n_balls}): E = {mu:.4f}, SD = {np.sqrt(v):.4f}")

# 몬테카를로로 확인: 생일이 같은 짝
np.random.seed(42)
N_sim = 100_000
n_people = 30
pair_counts = []
for _ in range(N_sim):
    bdays = np.random.randint(0, 365, n_people)
    count = 0
    for i in range(n_people):
        for j in range(i+1, n_people):
            if bdays[i] == bdays[j]:
                count += 1
    pair_counts.append(count)

pair_counts = np.array(pair_counts)
mu_exact = comb(n_people, 2) / 365
print(f"\nBirthday pairs MC: E = {np.mean(pair_counts):.4f}, exact = {mu_exact:.4f}")
```

## 연습문제

**연습문제 1.** 부부 10쌍이 20개의 자리가 있는 원탁에 무작위로 앉는다. 지시확률변수를 써서 서로 이웃해 앉는 부부 쌍 수의 기댓값을 구하여라.

??? success "연습문제 1 풀이"
    $\mathbf{1}_{A_i}$ 를 $i$ 번 부부가 이웃해 앉음을 나타내는 지시확률변수라 하자. 20명이 둘러앉은 원형 배열에서 각 사람은 이웃이 2명이다. 한쪽 배우자를 고정하면 남은 19자리 가운데 이웃한 2자리에 다른 배우자가 앉을 확률은 $2/19$ 이다.

    $$
    E\!\left[\sum_{i=1}^{10} \mathbf{1}_{A_i}\right] = 10 \cdot \frac{2}{19} = \frac{20}{19} \approx 1.053
    $$

---

**연습문제 2.** 52장짜리 카드 한 벌을 섞는다. $X$ 를 처음의 정렬된 순서와 자리가 같은 카드의 수(고정점의 수)라 하자. $E[X]$ 와 $\text{Var}(X)$ 를 구하여라.

??? success "연습문제 2 풀이"
    $A_i$ 를 "$i$ 번 카드가 $i$ 번 자리에 있다"라 하고 $X = \sum_{i=1}^{52} \mathbf{1}_{A_i}$ 라 하자. 각 $P(A_i) = 1/52$ 이므로 $E[X] = 52 \cdot (1/52) = 1$ 이다.

    분산을 구하자. $i \neq j$ 에 대하여 $P(A_i \cap A_j) = 1/(52 \cdot 51)$ 이다.

    $$
    \text{Cov}(\mathbf{1}_{A_i}, \mathbf{1}_{A_j}) = \frac{1}{52 \cdot 51} - \frac{1}{52^2} = \frac{1}{52}\!\left(\frac{1}{51} - \frac{1}{52}\right) = \frac{1}{52 \cdot 51 \cdot 52}
    $$

    $$
    \text{Var}(X) = 52 \cdot \frac{1}{52} \cdot \frac{51}{52} + 2\binom{52}{2}\cdot \frac{1}{52 \cdot 51 \cdot 52} = \frac{51}{52} + \frac{1}{52} = 1
    $$

---

**연습문제 3.** $\{1, 2, \ldots, n\}$ 의 무작위 순열에서 원소 $i$ 가 $i$ 번 자리에 있는 첨자 $i$ 의 개수(고정점의 수)를 $X$ 라 하자. 모든 $n \geq 2$ 에 대하여 $E[X] = 1$ 이고 $\text{Var}(X) = 1$ 임을 증명하여라.

??? success "연습문제 3 풀이"
    **평균:** $E[X] = \sum_{i=1}^n P(A_i) = n \cdot (1/n) = 1$ 이다.

    **분산:** $\text{Var}(\mathbf{1}_{A_i}) = (1/n)(1 - 1/n)$ 이고 $\text{Cov}(\mathbf{1}_{A_i}, \mathbf{1}_{A_j}) = \frac{1}{n(n-1)} - \frac{1}{n^2} = \frac{1}{n^2(n-1)}$ 이다.

    $$
    \text{Var}(X) = n \cdot \frac{n-1}{n^2} + 2\binom{n}{2} \cdot \frac{1}{n^2(n-1)} = \frac{n-1}{n} + \frac{n(n-1)}{2} \cdot \frac{2}{n^2(n-1) \cdot 1}
    $$

    둘째 항을 정리하면 $\frac{1}{n}$ 이다. 그러므로 $\text{Var}(X) = \frac{n-1}{n} + \frac{1}{n} = 1$ 이다. $\square$

---

**연습문제 4.** 공 $n$ 개를 서로 독립으로 균등하게 $M$ 개의 상자에 던져 넣을 때, 지시확률변수를 써서 **비어 있지 않은** 상자 수의 기댓값을 구하여라.

??? success "연습문제 4 풀이"
    $\mathbf{1}_{B_j}$ 를 $j$ 번 상자가 비어 있지 않음을 나타내는 지시확률변수라 하자. 그러면 $P(B_j) = 1 - (1 - 1/M)^n$ 이고 다음을 얻는다.

    $$
    E[\text{비어 있지 않은 상자의 수}] = M\!\left[1 - \left(1 - \frac{1}{M}\right)^n\right]
    $$

---

**연습문제 5.** 생일 짝의 지시확률변수 $\mathbf{1}_{A_{ij}}$ 가 쌍별로는 독립이지만 상호독립은 아닌 까닭을 설명하여라.

??? success "연습문제 5 풀이"
    **쌍별 독립:** $\{i,j\} \cap \{k,l\} = \emptyset$ 인 서로 다른 두 짝 $(i,j)$ 와 $(k,l)$ 에 대하여 사건 $A_{ij}$ 와 $A_{kl}$ 은 서로 겹치지 않는 생일들에만 달려 있으므로 독립이다. 사람 한 명을 공유하는 두 짝, 이를테면 $(1,2)$ 와 $(1,3)$ 의 경우에는 1번의 생일이 2번과도 3번과도 같아야 하는데 이 둘은 서로 독립인 선택이므로 $P(A_{12} \cap A_{13}) = 1/365^2 = P(A_{12})P(A_{13})$ 이다.

    **상호독립은 아님:** $A_{12}$, $A_{13}$, $A_{23}$ 을 생각하자. $P(A_{12} \cap A_{13} \cap A_{23}) = P(\text{세 사람의 생일이 모두 같다}) = 1/365^2$ 이다. 그런데 $P(A_{12})P(A_{13})P(A_{23}) = 1/365^3 \neq 1/365^2$ 이다. $A_{12} \cap A_{13}$ 이 일어나면 $A_{23}$ 이 저절로 따라오므로 세 사건의 교집합의 확률이 더 크다.
