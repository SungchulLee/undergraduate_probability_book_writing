# 포함배제 원리

## 개요

**포함배제 원리**는 덧셈 법칙을 **겹치는**(서로소가 아닌) 집합까지 다룰 수 있도록 일반화한 것이다. 부류들이 서로 겹치면 크기를 그냥 더하는 것만으로는 여러 부류에 동시에 속하는 원소를 거듭 세게 된다. 포함배제 원리는 이렇게 더 센 몫을 체계적으로 바로잡아 준다.

## 왜 필요한가 — 지뢰찾기

PDF에서는 **지뢰찾기** 게임을 통해 포함배제를 소개한다. 지뢰의 위치를 알아내려면 서로 겹치는 영역을 따져야 하기 때문이다. A, B, C로 표시된 칸들이 이웃한 지뢰 구역을 공유할 때, 그 합집합에 들어 있는 지뢰의 총 개수를 구하려면 겹치는 부분을 조심스럽게 빼 주어야 한다. 이것이 바로 포함배제 원리가 쓰이는 자연스러운 자리이다.

## 두 집합

두 집합 $A$ 와 $B$ 에 대하여 다음이 성립한다.

**상계(거듭 세기):**

$$|A \cup B| \leq |A| + |B|$$

**정확한 공식:**

$$|A \cup B| = |A| + |B| - |A \cap B|$$

$|A \cap B|$ 항은 두 번 세어진 원소($|A|$ 에서 한 번, $|B|$ 에서 한 번)를 바로잡아 준다.

## 세 집합

세 집합 $A$, $B$, $C$ 에 대하여 다음이 성립한다.

**첫 번째 근사(거듭 세기):**

$$|A \cup B \cup C| \leq |A| + |B| + |C|$$

**두 번째 근사(덜 세기):**

$$|A \cup B \cup C| \leq |A| + |B| + |C| - |AB| - |BC| - |CA|$$

**정확한 공식:**

$$|A \cup B \cup C| = |A| + |B| + |C| - |AB| - |BC| - |CA| + |ABC|$$

여기서 $AB$ 는 $A \cap B$ 를 뜻하며, 나머지도 마찬가지이다.

## 일반 공식 — 여러 집합

$n$ 개의 집합 $A_1, A_2, \ldots, A_n$ 에 대하여 다음이 성립한다.

$$\left|\bigcup_{i=1}^{n} A_i\right| = \sum_{i=1}^{n} |A_i| - \sum_{1 \leq i < j \leq n} |A_i A_j| + \sum_{1 \leq i < j < k \leq n} |A_i A_j A_k| - \cdots + (-1)^{n+1} |A_1 A_2 \cdots A_n|$$

더하기와 빼기가 번갈아 나타난다. 낱개 집합은 더하고, 두 집합의 교집합은 빼고, 세 집합의 교집합은 다시 더하는 식이다.

## 본페로니 부등식

포함배제 공식을 도중에 끊어 얻은 부분합은 상계와 하계를 번갈아 준다.

$$\left|\bigcup_{i=1}^{n} A_i\right| \leq \sum_{i=1}^{n} |A_i|$$

$$\left|\bigcup_{i=1}^{n} A_i\right| \geq \sum_{i=1}^{n} |A_i| - \sum_{1 \leq i < j \leq n} |A_i A_j|$$

$$\left|\bigcup_{i=1}^{n} A_i\right| \leq \sum_{i=1}^{n} |A_i| - \sum_{1 \leq i < j \leq n} |A_i A_j| + \sum_{1 \leq i < j < k \leq n} |A_i A_j A_k|$$

이를 **본페로니 부등식**이라 하며, 포함배제 공식을 끝까지 계산하기 어려울 때 쓸모가 있다.

## 여집합과 함께 쓰기

포함배제 원리는 여집합 세기와 자연스럽게 맞물린다. $B = \Omega \setminus \bigcup_{i=1}^{n} A_i$ 라 하면 다음이 성립한다.

$$|B| = |\Omega| - \left|\bigcup_{i=1}^{n} A_i\right|$$

뒤의 절에서 다룰 짝맞추기 문제(완전순열)에서 쓰는 방법이 바로 이것이다.

## 파이썬 구현

```python
from itertools import combinations
from math import comb

def inclusion_exclusion(sets):
    """
    포함배제 원리로 |A1 ∪ A2 ∪ ... ∪ An| 을 계산한다.
    
    매개변수
    ----------
    sets : list of set
        집합 A1, A2, ..., An.
    
    반환값
    -------
    int
        합집합의 크기.
    """
    n = len(sets)
    total = 0
    for k in range(1, n + 1):
        sign = (-1) ** (k + 1)
        for combo in combinations(range(n), k):
            intersection = sets[combo[0]]
            for idx in combo[1:]:
                intersection = intersection & sets[idx]
            total += sign * len(intersection)
    return total

# 예: 두 집합
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
print(f"|A ∪ B| = {inclusion_exclusion([A, B])}")
print(f"Verification: {len(A | B)}")
# Output: |A ∪ B| = 7, Verification: 7

# 예: 세 집합
C = {5, 6, 7, 8}
print(f"|A ∪ B ∪ C| = {inclusion_exclusion([A, B, C])}")
print(f"Verification: {len(A | B | C)}")
# Output: |A ∪ B ∪ C| = 8, Verification: 8

# 세 집합의 경우를 단계별로 확인하기
print(f"\n|A| + |B| + |C| = {len(A) + len(B) + len(C)}")
print(f"|AB| + |BC| + |CA| = {len(A&B) + len(B&C) + len(C&A)}")
print(f"|ABC| = {len(A & B & C)}")
print(f"By IE: {len(A)+len(B)+len(C) - len(A&B)-len(B&C)-len(C&A) + len(A&B&C)}")
```

## 핵심 정리

포함배제 원리는 겹치는 집합들의 합집합 크기를 세는 대표적인 도구이다. 교집합 항을 번갈아 빼고 더하면서 거듭 센 몫을 체계적으로 바로잡는다. 여집합 세기와 함께 쓰면 직접 세기 어려운 문제도 풀리는데, 그 대표가 짝맞추기 문제(완전순열)이다.

## 연습문제

**연습문제 1.** 100명의 학생 가운데 60명이 수학을, 45명이 물리를, 30명이 화학을 공부한다. 수학과 물리를 함께 공부하는 학생이 20명, 수학과 화학을 함께 공부하는 학생이 15명, 물리와 화학을 함께 공부하는 학생이 10명이며, 세 과목을 모두 공부하는 학생이 5명이다.

**(a)** 세 과목 가운데 적어도 하나를 공부하는 학생은 몇 명인가?

**(b)** 세 과목 가운데 어느 것도 공부하지 않는 학생은 몇 명인가?

??? success "연습문제 1 풀이"
    **(a)** 포함배제에 따라 다음을 얻는다.

    $$
    |M \cup P \cup C| = 60 + 45 + 30 - 20 - 15 - 10 + 5 = 95
    $$

    **(b)** $100 - 95 = 5$ 명이 어느 과목도 공부하지 않는다.
