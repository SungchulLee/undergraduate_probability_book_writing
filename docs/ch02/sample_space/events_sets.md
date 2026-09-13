# 사건과 집합 연산

## 사건

**사건**은 표본공간 $\Omega$ 의 부분집합 $A$ 를 말한다. 사건은 우리가 관심을 두는 표본(결과)들을 한데 모아 놓은 것이다.

$$
A \subseteq \Omega
$$

!!! example "주사위 굴리기에서의 사건"
    $\Omega = \{1, 2, 3, 4, 5, 6\}$ 일 때,

    - "짝수가 나온다": $A = \{2, 4, 6\}$
    - "3 이하가 나온다": $B = \{1, 2, 3\}$
    - "5가 나온다": $C = \{5\}$ (**단순사건** 또는 **근원사건**)

## 특별한 사건

| 사건 | 기호 | 설명 |
|-------|----------|-------------|
| **전사건** | $\Omega$ | 언제나 일어나는 사건 |
| **공사건** | $\emptyset$ | 결코 일어나지 않는 사건 |
| **근원사건** | $\{\omega\}$ | 결과 하나만을 담은 사건 |

## 사건에 대한 집합 연산

사건은 집합이므로 흔히 쓰는 집합 연산으로 서로 엮을 수 있다. 집합 연산마다 확률에서의 자연스러운 뜻이 따라붙는다.

### 합집합 (또는)

"$A$ 또는 $B$ 가(둘 다여도 좋다) 일어난다"는 사건이다.

$$
A \cup B = \{\omega \in \Omega : \omega \in A \text{ 또는 } \omega \in B\}
$$

### 교집합 (그리고)

"$A$ 와 $B$ 가 모두 일어난다"는 사건이다.

$$
A \cap B = \{\omega \in \Omega : \omega \in A \text{ 그리고 } \omega \in B\}
$$

간단히 쓰려고 $A \cap B$ 를 $AB$ 로 적는 일이 많다.

### 여집합 (아니다)

"$A$ 가 일어나지 않는다"는 사건이다.

$$
A^c = \{\omega \in \Omega : \omega \notin A\}
$$

### 차집합

"$A$ 는 일어나지만 $B$ 는 일어나지 않는다"는 사건이다.

$$
A \setminus B = A \cap B^c = \{\omega \in \Omega : \omega \in A \text{ 그리고 } \omega \notin B\}
$$

## 서로소(배반)인 사건

두 사건 $A$ 와 $B$ 가 동시에 일어날 수 없으면 **서로소**(또는 배반)라고 한다.

$$
A \cap B = \emptyset
$$

더 일반적으로, 모든 $i \neq j$ 에 대해 $A_i \cap A_j = \emptyset$ 이면 사건 $A_1, A_2, \ldots$ 가 **쌍마다 서로소**라고 한다.

## 표본공간의 분할

사건 $A_1, A_2, \ldots, A_n$ 이 다음 두 조건을 만족하면 $\Omega$ 의 **분할**을 이룬다고 한다.

1. 쌍마다 서로소이다: 모든 $i \neq j$ 에 대해 $A_i \cap A_j = \emptyset$
2. 표본공간 전체를 덮는다: $A_1 \cup A_2 \cup \cdots \cup A_n = \Omega$

!!! note "주요 성질"
    임의의 사건 $A$ 에 대해 쌍 $\{A, A^c\}$ 는 언제나 $\Omega$ 의 분할을 이룬다.

## 주요 집합 항등식

다음 항등식들은 사건에 대해서도 성립하며 확률에서 자주 쓰인다.

**교환법칙:**

$$
A \cup B = B \cup A, \qquad A \cap B = B \cap A
$$

**결합법칙:**

$$
(A \cup B) \cup C = A \cup (B \cup C), \qquad (A \cap B) \cap C = A \cap (B \cap C)
$$

**분배법칙:**

$$
A \cap (B \cup C) = (A \cap B) \cup (A \cap C)
$$

$$
A \cup (B \cap C) = (A \cup B) \cap (A \cup C)
$$

## 파이썬 예제

```python
# 주사위 굴리기의 표본공간과 사건을 정의한다
omega = {1, 2, 3, 4, 5, 6}
A = {2, 4, 6}        # 짝수
B = {1, 2, 3}        # 3 이하
C = {4, 5, 6}        # 4 이상

print(f"Ω = {omega}")
print(f"A (even) = {A}")
print(f"B (≤ 3) = {B}")
print(f"C (≥ 4) = {C}")

# 집합 연산
print(f"\nA ∪ B = {A | B}")
print(f"A ∩ B = {A & B}")
print(f"A^c = {omega - A}")
print(f"A \\ B = {A - B}")

# 서로소인지 확인하기
print(f"\nB ∩ C = {B & C}  → Disjoint: {len(B & C) == 0}")
print(f"A ∩ B = {A & B}  → Disjoint: {len(A & B) == 0}")

# 분할인지 확인하기
print(f"\nB ∪ C = {B | C}  → Partition of Ω: {B | C == omega and len(B & C) == 0}")
```

**실행 결과:**
```
Ω = {1, 2, 3, 4, 5, 6}
A (even) = {2, 4, 6}
B (≤ 3) = {1, 2, 3}
C (≥ 4) = {4, 5, 6}

A ∪ B = {1, 2, 3, 4, 6}
A ∩ B = {2}
A^c = {1, 3, 5}
A \ B = {4, 6}

B ∩ C = set()  → Disjoint: True
A ∩ B = {2}  → Disjoint: False

B ∪ C = {1, 2, 3, 4, 5, 6}  → Partition of Ω: True
```

## 연습문제

**연습문제 1.** $\Omega = \{1,2,3,4,5,6,7,8\}$, $A = \{1,2,3,4\}$, $B = \{3,4,5,6\}$, $C = \{5,6,7,8\}$ 이라 하자. $A \cup B$, $A \cap B$, $A^c$, $B \setminus A$, $(A \cup C)^c$ 를 구하여라.

??? success "연습문제 1 풀이"

    - $A \cup B = \{1,2,3,4,5,6\}$
    - $A \cap B = \{3,4\}$
    - $A^c = \{5,6,7,8\}$
    - $B \setminus A = B \cap A^c = \{5,6\}$
    - $A \cup C = \{1,2,3,4,5,6,7,8\} = \Omega$ 이므로 $(A \cup C)^c = \emptyset$

---

**연습문제 2.** 다음 모임이 $\Omega = \{1,2,\ldots,10\}$ 의 분할을 이루는지 판정하여라.

**(a)** $A_1 = \{1,2,3\}$, $A_2 = \{4,5,6\}$, $A_3 = \{7,8,9,10\}$

**(b)** $A_1 = \{1,3,5,7,9\}$, $A_2 = \{2,4,6,8\}$

??? success "연습문제 2 풀이"
    **(a)** 쌍마다 서로소인가: 그렇다. 합집합: $\{1,\ldots,10\} = \Omega$. 따라서 분할이 **맞다**.

    **(b)** 쌍마다 서로소인가: 그렇다. 그러나 $A_1 \cup A_2 = \{1,2,\ldots,9\} \neq \Omega$ 이다(10이 빠져 있다). 따라서 분할이 **아니다**.

---

**연습문제 3.** 원소를 따라가는 방법으로 분배법칙 $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ 를 증명하여라.

??? success "연습문제 3 풀이"
    ($\subseteq$) $\omega \in A \cap (B \cup C)$ 라 하자. 그러면 $\omega \in A$ 이고 $\omega \in B \cup C$ 이다. 따라서 $\omega \in B$ 이거나 $\omega \in C$ 이다. $\omega \in B$ 이면 $\omega \in A \cap B$ 이고, $\omega \in C$ 이면 $\omega \in A \cap C$ 이다. 어느 쪽이든 $\omega \in (A \cap B) \cup (A \cap C)$ 이다.

    ($\supseteq$) $\omega \in (A \cap B) \cup (A \cap C)$ 라 하자. 그러면 $\omega \in A \cap B$ 이거나 $\omega \in A \cap C$ 이다. 어느 경우든 $\omega \in A$ 이다. 또한 $\omega \in B$ 이거나 $\omega \in C$ 이므로 $\omega \in B \cup C$ 이다. 그러므로 $\omega \in A \cap (B \cup C)$ 이다. $\square$

---

**연습문제 4.** 표준 52장 카드 한 벌에서 카드 한 장을 뽑는다. $A$ = "뽑은 카드가 하트이다", $B$ = "뽑은 카드가 그림카드(J, Q, K)이다", $C$ = "뽑은 카드가 빨간색이다"라 하자. 다음 사건을 집합 기호로 나타내고 그 원소의 개수를 구하여라.

**(a)** 뽑은 카드가 빨간색 그림카드이다.

**(b)** 뽑은 카드가 하트이지만 그림카드는 아니다.

**(c)** 뽑은 카드가 빨간색도 아니고 그림카드도 아니다.

??? success "연습문제 4 풀이"
    **(a)** $B \cap C$: 빨간색인 그림카드. 무늬마다 그림카드가 3장이고 빨간 무늬가 2가지이므로 $|B \cap C| = 6$ 이다.

    **(b)** $A \setminus B = A \cap B^c$: 그림카드가 아닌 하트. $|A| = 13$ 이고 $|A \cap B| = 3$ 이므로 $|A \setminus B| = 10$ 이다.

    **(c)** $C^c \cap B^c = (C \cup B)^c$: 빨간색도 그림카드도 아닌 카드. $|C| = 26$, $|B| = 12$, $|B \cap C| = 6$ 이다. 포함배제에 따라 $|C \cup B| = 32$ 이므로 $|(C \cup B)^c| = 52 - 32 = 20$ 이다.

---

**연습문제 5.** 임의의 사건 $A$ 와 $B$ 에 대해 $A = (A \cap B) \cup (A \cap B^c)$ 이고 오른쪽의 두 집합이 서로소임을 증명하여라.

??? success "연습문제 5 풀이"
    $\{B, B^c\}$ 는 $\Omega$ 의 분할이므로 모든 $\omega \in A$ 는 $\omega \in B$ 와 $\omega \in B^c$ 가운데 정확히 하나를 만족한다. 그러므로 $\omega \in A \cap B$ 이거나 $\omega \in A \cap B^c$ 이다(둘 다일 수는 없다). 따라서 다음을 얻는다.

    $$
    A = (A \cap B) \cup (A \cap B^c)
    $$

    서로소임을 보이자. 만약 $\omega \in (A \cap B) \cap (A \cap B^c)$ 라면 $\omega \in B$ 이면서 $\omega \in B^c$ 가 되어 모순이다. 그러므로 $(A \cap B) \cap (A \cap B^c) = \emptyset$ 이다. $\square$
