# 드 모르간 법칙

## 정리의 서술

**드 모르간 법칙**은 합집합, 교집합, 여집합 사이를 잇는 기본 관계를 알려 준다. 확률에서 사건을 다룰 때 없어서는 안 될 도구이다.

### 두 사건일 때

$$
(A \cup B)^c = A^c \cap B^c
$$

$$
(A \cap B)^c = A^c \cup B^c
$$

말로 옮기면 다음과 같다.

- 합집합의 여집합은 여집합들의 교집합이다: "$A$ 도 $B$ 도 아니다"는 "$A$ 가 아니고 **그리고** $B$ 가 아니다"라는 뜻이다.
- 교집합의 여집합은 여집합들의 합집합이다: "$A$ 와 $B$ 가 둘 다이지는 않다"는 "$A$ 가 아니거나 **또는** $B$ 가 아니다"라는 뜻이다.

### 유한개의 사건일 때

$$
\left(\bigcup_{i=1}^{n} A_i\right)^c = \bigcap_{i=1}^{n} A_i^c
$$

$$
\left(\bigcap_{i=1}^{n} A_i\right)^c = \bigcup_{i=1}^{n} A_i^c
$$

### 가산개의 사건일 때

$$
\left(\bigcup_{i=1}^{\infty} A_i\right)^c = \bigcap_{i=1}^{\infty} A_i^c
$$

$$
\left(\bigcap_{i=1}^{\infty} A_i\right)^c = \bigcup_{i=1}^{\infty} A_i^c
$$

## 증명 (두 사건인 경우)

양쪽이 서로의 부분집합임을 보여 $(A \cup B)^c = A^c \cap B^c$ 를 증명한다.

**$(\subseteq)$** $\omega \in (A \cup B)^c$ 라 하자. 그러면 $\omega \notin A \cup B$ 이고, 이는 $\omega \notin A$ 이면서 $\omega \notin B$ 라는 뜻이다. 그러므로 $\omega \in A^c$ 이고 $\omega \in B^c$ 이므로 $\omega \in A^c \cap B^c$ 이다.

**$(\supseteq)$** $\omega \in A^c \cap B^c$ 라 하자. 그러면 $\omega \notin A$ 이고 $\omega \notin B$ 이므로 $\omega \notin A \cup B$ 이다. 그러므로 $\omega \in (A \cup B)^c$ 이다.

$(A \cap B)^c = A^c \cup B^c$ 의 증명도 마찬가지 방식이다.

## 확률에서 드 모르간 법칙이 중요한 까닭

드 모르간 법칙은 "적어도 하나" 꼴의 문제를 "하나도 없다" 꼴의 문제로 바꾸는 데 자주 쓰인다.

$$
P\left(\bigcup_{i=1}^{n} A_i\right) = 1 - P\left(\bigcap_{i=1}^{n} A_i^c\right)
$$

특히 $A_i^c$ 쪽이 다루기 쉬울 때—이를테면 사건들이 독립일 때—큰 힘을 발휘한다.

!!! example "실제 응용"
    **문제:** 독립인 $n$ 개의 사건 가운데 적어도 하나가 일어날 확률은 얼마인가?

    $A_i$ 를 $i$ 번째 사건이라 하고 $P(A_i) = p_i$ 라 하자. 그러면 다음이 성립한다.

    $$
    P\left(\bigcup_{i=1}^{n} A_i\right) = 1 - P\left(\bigcap_{i=1}^{n} A_i^c\right) = 1 - \prod_{i=1}^{n}(1 - p_i)
    $$

    마지막 등식에서 독립성을 썼다.

## 파이썬 예제

```python
# 집합으로 드 모르간 법칙을 확인한다
omega = {1, 2, 3, 4, 5, 6}
A = {1, 2, 3}
B = {2, 3, 4}

# 드 모르간 제1법칙: (A ∪ B)^c = A^c ∩ B^c
lhs_1 = omega - (A | B)
rhs_1 = (omega - A) & (omega - B)
print(f"(A ∪ B)^c = {lhs_1}")
print(f"A^c ∩ B^c = {rhs_1}")
print(f"Equal: {lhs_1 == rhs_1}\n")

# 드 모르간 제2법칙: (A ∩ B)^c = A^c ∪ B^c
lhs_2 = omega - (A & B)
rhs_2 = (omega - A) | (omega - B)
print(f"(A ∩ B)^c = {lhs_2}")
print(f"A^c ∪ B^c = {rhs_2}")
print(f"Equal: {lhs_2 == rhs_2}")
```

**실행 결과:**
```
(A ∪ B)^c = {5, 6}
A^c ∩ B^c = {5, 6}
Equal: True

(A ∩ B)^c = {1, 4, 5, 6}
A^c ∪ B^c = {1, 4, 5, 6}
Equal: True
```

```python
import numpy as np

# 확률에의 응용: 여집합으로 "적어도 하나" 구하기
# 주사위를 4번 굴린다. P(6이 적어도 한 번 나온다)는?
n_rolls = 4
p_six = 1/6

# 곧바로: P(6이 적어도 한 번) = 1 - P(6이 한 번도 안 나옴)
# 드 모르간을 쓰면: P(∪ Ai) = 1 - P(∩ Ai^c) = 1 - (5/6)^4
p_at_least_one = 1 - (1 - p_six)**n_rolls
print(f"P(at least one 6 in {n_rolls} rolls) = 1 - (5/6)^{n_rolls} = {p_at_least_one:.4f}")

# 모의실험으로 확인하기
np.random.seed(42)
n_sim = 100_000
rolls = np.random.randint(1, 7, size=(n_sim, n_rolls))
sim_prob = np.mean(np.any(rolls == 6, axis=1))
print(f"Simulated probability: {sim_prob:.4f}")
```

**실행 결과:**
```
P(at least one 6 in 4 rolls) = 1 - (5/6)^4 = 0.5177
Simulated probability: 0.5169
```

## 연습문제

**연습문제 1.** $\Omega = \{1, 2, 3, 4, 5, 6, 7, 8\}$ 에서 사건 $A = \{1, 2, 3, 4\}$ 와 $B = \{3, 4, 5, 6\}$ 에 대해 드 모르간 법칙이 성립함을 확인하여라.

??? success "연습문제 1 풀이"
    먼저 기본이 되는 집합들을 구한다.

    - $A \cup B = \{1, 2, 3, 4, 5, 6\}$ 이므로 $(A \cup B)^c = \{7, 8\}$ 이다.
    - $A \cap B = \{3, 4\}$ 이므로 $(A \cap B)^c = \{1, 2, 5, 6, 7, 8\}$ 이다.
    - $A^c = \{5, 6, 7, 8\}$ 이고 $B^c = \{1, 2, 7, 8\}$ 이다.

    이제 두 가지 드 모르간 법칙을 확인한다.

    - $A^c \cap B^c = \{5, 6, 7, 8\} \cap \{1, 2, 7, 8\} = \{7, 8\} = (A \cup B)^c$. $\checkmark$
    - $A^c \cup B^c = \{5, 6, 7, 8\} \cup \{1, 2, 7, 8\} = \{1, 2, 5, 6, 7, 8\} = (A \cap B)^c$. $\checkmark$
