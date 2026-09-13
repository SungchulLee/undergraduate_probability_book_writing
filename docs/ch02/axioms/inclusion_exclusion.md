# 확률의 포함배제 공식

## 두 사건

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

!!! note "왜 빼는가"
    $P(A) + P(B)$ 로 더하면 $A \cap B$ 에 속한 결과가 두 번 세어진다. $P(A \cap B)$ 를 빼서 이 겹세기를 바로잡는 것이다.

**상계 (불의 부등식):**

$$
P(A \cup B) \leq P(A) + P(B)
$$

## 세 사건

**정확한 공식:**

$$
P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(AB) - P(BC) - P(CA) + P(ABC)
$$

여기서 $P(AB) = P(A \cap B)$ 처럼 줄여 쓴 기호를 썼다.

**세 사건에 대한 본페로니 부등식:**

$$
P(A \cup B \cup C) \leq P(A) + P(B) + P(C)
$$

$$
P(A \cup B \cup C) \geq P(A) + P(B) + P(C) - P(AB) - P(BC) - P(CA)
$$

## 일반적인 경우: n개의 사건

### 포함배제 원리

$$
P\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i=1}^{n} P(A_i) - \sum_{1 \leq i < j \leq n} P(A_i A_j) + \sum_{1 \leq i < j < k \leq n} P(A_i A_j A_k) - \cdots + (-1)^{n+1} P(A_1 A_2 \cdots A_n)
$$

간단히 쓰면 다음과 같다.

$$
P\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{k=1}^{n} (-1)^{k+1} \sum_{1 \leq i_1 < \cdots < i_k \leq n} P(A_{i_1} \cap \cdots \cap A_{i_k})
$$

### 본페로니 부등식

포함배제 공식의 부분합은 상계와 하계를 번갈아 가며 준다.

$$
P\left(\bigcup_{i=1}^{n} A_i\right) \leq \sum_{i=1}^{n} P(A_i)
$$

$$
P\left(\bigcup_{i=1}^{n} A_i\right) \geq \sum_{i=1}^{n} P(A_i) - \sum_{1 \leq i < j \leq n} P(A_i A_j)
$$

$$
P\left(\bigcup_{i=1}^{n} A_i\right) \leq \sum_{i=1}^{n} P(A_i) - \sum_{1 \leq i < j \leq n} P(A_i A_j) + \sum_{1 \leq i < j < k \leq n} P(A_i A_j A_k)
$$

이 규칙은 계속 이어진다. **홀수** 개의 항에서 끊으면 **상계**가 되고, **짝수** 개의 항에서 끊으면 **하계**가 된다.

### 이름 붙이기

| 이름 | 공식 |
|------|---------|
| **불의 부등식** | 첫 번째 상계: $P(\cup A_i) \leq \sum P(A_i)$ |
| **본페로니 부등식** | 번갈아 나오는 모든 경계 |
| **포함배제 원리** | 정확한 등식(맨 마지막 줄) |

## 예제: 카드

!!! example "5장의 패에 에이스가 적어도 한 장"
    $i = 1, 2, 3, 4$ 에 대해 $A_i$ 를 $i$ 번째 에이스가 패에 들어 있는 사건이라 하자.

    포함배제에 따라 다음을 얻는다.

    $$
    P(A_1 \cup A_2 \cup A_3 \cup A_4) = \binom{4}{1}\frac{\binom{51}{4}}{\binom{52}{5}} - \binom{4}{2}\frac{\binom{50}{3}}{\binom{52}{5}} + \binom{4}{3}\frac{\binom{49}{2}}{\binom{52}{5}} - \binom{4}{4}\frac{\binom{48}{1}}{\binom{52}{5}}
    $$

    또는 여사건을 쓰면 훨씬 간단하다.

    $$
    P(\text{에이스가 적어도 한 장}) = 1 - P(\text{에이스가 한 장도 없음}) = 1 - \frac{\binom{48}{5}}{\binom{52}{5}}
    $$

## 파이썬 예제

```python
from math import comb
from itertools import combinations

def inclusion_exclusion(sets, omega_size):
    """
    포함배제를 써서 P(A1 ∪ A2 ∪ ... ∪ An)을 구한다.
    """
    n = len(sets)
    total = 0
    for k in range(1, n + 1):
        sign = (-1)**(k + 1)
        for combo in combinations(range(n), k):
            intersection = sets[combo[0]]
            for idx in combo[1:]:
                intersection = intersection & sets[idx]
            total += sign * len(intersection) / omega_size
    return total

# 예: 공정한 주사위 굴리기
omega = set(range(1, 7))
A = {2, 4, 6}     # 짝수
B = {1, 2, 3}     # 3 이하
C = {3, 4, 5, 6}  # 3 이상

# 두 사건
ie_2 = inclusion_exclusion([A, B], len(omega))
direct_2 = len(A | B) / len(omega)
print(f"Two events: P(A ∪ B)")
print(f"  Inclusion-exclusion: {ie_2:.4f}")
print(f"  Direct: {direct_2:.4f}")

# 세 사건
ie_3 = inclusion_exclusion([A, B, C], len(omega))
direct_3 = len(A | B | C) / len(omega)
print(f"\nThree events: P(A ∪ B ∪ C)")
print(f"  Inclusion-exclusion: {ie_3:.4f}")
print(f"  Direct: {direct_3:.4f}")

# 세 사건에 대한 본페로니 경계
S1 = sum(len(s)/len(omega) for s in [A, B, C])
S2 = sum(len(A_i & A_j)/len(omega)
         for A_i, A_j in combinations([A, B, C], 2))

print(f"\nBonferroni bounds:")
print(f"  Upper (S1):       {S1:.4f}")
print(f"  Lower (S1 - S2):  {S1 - S2:.4f}")
print(f"  Exact:            {ie_3:.4f}")

# 5장의 패에 에이스가 적어도 한 장
print(f"\n--- At Least One Ace in 5-Card Hand ---")
p_no_ace = comb(48, 5) / comb(52, 5)
p_at_least_one = 1 - p_no_ace
print(f"P(at least one ace) = 1 - C(48,5)/C(52,5) = {p_at_least_one:.6f}")
```

**실행 결과:**
```
Two events: P(A ∪ B)
  Inclusion-exclusion: 0.8333
  Direct: 0.8333

Three events: P(A ∪ B ∪ C)
  Inclusion-exclusion: 1.0000
  Direct: 1.0000

Bonferroni bounds:
  Upper (S1):       2.1667
  Lower (S1 - S2):  0.8333
  Exact:            1.0000

--- At Least One Ace in 5-Card Hand ---
P(at least one ace) = 1 - C(48,5)/C(52,5) = 0.341392
```

## 연습문제

**연습문제 1.** 콜모고로프 공리와 $P(A) = P(A \cap B) + P(A \cap B^c)$ 라는 사실만 써서, 임의의 사건 $A$ 와 $B$ 에 대해 다음이 성립함을 증명하여라.

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

??? success "연습문제 1 풀이"
    $A \cup B$ 를 서로소인 조각으로 쪼갠다.

    $$
    A \cup B = (A \cap B^c) \cup (A \cap B) \cup (A^c \cap B)
    $$

    오른쪽의 세 집합은 쌍마다 서로소이다($A$ 와 $B$ 에 속하는지 여부로 $A \cup B$ 를 나눈 것이다). 유한가법성에 따라 다음을 얻는다.

    $$
    P(A \cup B) = P(A \cap B^c) + P(A \cap B) + P(A^c \cap B)
    $$

    $P(A) = P(A \cap B) + P(A \cap B^c)$ 와 마찬가지 꼴인 $P(B) = P(A \cap B) + P(A^c \cap B)$ 를 쓰면 다음과 같다.

    $$
    P(A) + P(B) = P(A \cap B^c) + P(A^c \cap B) + 2 P(A \cap B)
    $$

    여기서 $P(A \cap B)$ 를 한 번 빼면 다음을 얻는다.

    $$
    P(A) + P(B) - P(A \cap B) = P(A \cap B^c) + P(A^c \cap B) + P(A \cap B) = P(A \cup B)
    $$

    $\square$

---

**연습문제 2 (짝맞추기 문제).** $n$ 명이 각자 모자를 한 통에 넣은 뒤 저마다 모자 하나를 무작위로 집어 간다고 하자. 포함배제 원리를 써서 적어도 한 사람이 자기 모자를 되찾을 확률을 구하여라.

*힌트:* $A_i$ 를 $i$ 번째 사람이 자기 모자를 집는 사건이라 하자. $P(A_i)$, $P(A_i \cap A_j)$ 등을 구한 뒤 포함배제를 적용하여라.

??? success "연습문제 2 풀이"
    $A_i$ 를 $i$ 번째 사람이 자기 모자를 집는 사건이라 하자. 구하려는 확률은 $P\left(\bigcup_{i=1}^n A_i\right)$ 이다.

    크기가 $k$ 인 임의의 부분집합 $S \subseteq \{1, \ldots, n\}$ 에 대해 사건 $\bigcap_{i \in S} A_i$ 는 그 $k$ 명의 모자를 고정한다. 나머지 $n - k$ 개의 모자는 자유롭게 뒤섞일 수 있으므로 전체 $n!$ 가지 가운데 $(n-k)!$ 가지가 된다. 따라서 다음을 얻는다.

    $$
    P\left(\bigcap_{i \in S} A_i\right) = \frac{(n-k)!}{n!}
    $$

    포함배제에 따라 다음이 성립한다.

    $$
    P\left(\bigcup_{i=1}^n A_i\right) = \sum_{k=1}^{n} (-1)^{k+1} \binom{n}{k} \frac{(n-k)!}{n!} = \sum_{k=1}^{n} \frac{(-1)^{k+1}}{k!}
    $$

    $n \to \infty$ 일 때 이 값은 $1 - 1/e \approx 0.6321$ 로 수렴한다.
