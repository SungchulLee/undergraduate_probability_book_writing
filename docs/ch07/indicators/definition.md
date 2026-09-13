# 정의와 성질

## 정의

사건 $A$ 에 대하여 **지시확률변수** $\mathbf{1}_A$ ($I_A$ 로도 쓴다)는 다음과 같이 정의한다.

$$
\mathbf{1}_A = \begin{cases} 1 & \text{if } A \text{ occurs} \\ 0 & \text{if } A \text{ does not occur} \end{cases}
$$

지시확률변수는 $p = P(A)$ 인 $\text{Bernoulli}(p)$ 확률변수이다.

---

## 기본 성질

### 기댓값

$$
E[\mathbf{1}_A] = 1 \cdot P(A) + 0 \cdot P(A^c) = P(A)
$$

!!! note "근본이 되는 다리"
    $E[\mathbf{1}_A] = P(A)$. 이 등식은 확률과 기댓값을 이어 주며, 지시확률변수로 평균을 구하는 모든 계산의 출발점이다.

### 분산

$$
\text{Var}(\mathbf{1}_A) = P(A)(1 - P(A)) = pq
$$

여기서 $q = 1 - p$ 이다.

### 고차적률

$\mathbf{1}_A$ 는 0 아니면 1의 값만 가지므로 다음이 성립한다.

$$
(\mathbf{1}_A)^k = \mathbf{1}_A \quad \text{for all } k \geq 1
$$

따라서 모든 $k \geq 1$ 에 대하여 $E[(\mathbf{1}_A)^k] = P(A)$ 이다.

---

## 대수적 성질

지시확률변수는 사건의 집합 연산을 그대로 물려받는다.

| 집합 연산 | 지시확률변수 표현 |
|:---:|:---:|
| $A^c$ (여집합) | $1 - \mathbf{1}_A$ |
| $A \cap B$ (교집합) | $\mathbf{1}_A \cdot \mathbf{1}_B$ |
| $A \cup B$ (합집합) | $\mathbf{1}_A + \mathbf{1}_B - \mathbf{1}_A \cdot \mathbf{1}_B$ |
| $A \subseteq B$ | $\mathbf{1}_A \leq \mathbf{1}_B$ |
| $A$ 와 $B$ 가 서로소 | $\mathbf{1}_{A \cup B} = \mathbf{1}_A + \mathbf{1}_B$ |

### 독립

$A$ 와 $B$ 가 독립일 필요충분조건은 $\mathbf{1}_A$ 와 $\mathbf{1}_B$ 가 독립인 것이며, 이는 다음을 뜻한다.

$$
E[\mathbf{1}_A \cdot \mathbf{1}_B] = E[\mathbf{1}_A] \cdot E[\mathbf{1}_B]
$$

이는 $P(A \cap B) = P(A) P(B)$ 와 같은 말이다.

---

## 지시확률변수의 공분산

임의의 두 사건 $A$ 와 $B$ 에 대하여 다음이 성립한다.

$$
\text{Cov}(\mathbf{1}_A, \mathbf{1}_B) = P(A \cap B) - P(A)P(B)
$$

$A$ 와 $B$ 가 독립이면 $\text{Cov}(\mathbf{1}_A, \mathbf{1}_B) = 0$ 이다.

---

## 파이썬 구현

```python
import numpy as np

np.random.seed(42)
N = 1_000_000

# 사건 "주사위 눈 >= 5" 의 지시확률변수
rolls = np.random.randint(1, 7, N)
indicator = (rolls >= 5).astype(int)

p = 2/6  # P(roll >= 5)
print(f"Theoretical E[1_A] = {p:.4f}")
print(f"Simulated E[1_A] = {np.mean(indicator):.4f}")
print(f"Theoretical Var(1_A) = {p*(1-p):.4f}")
print(f"Simulated Var(1_A) = {np.var(indicator):.4f}")

# 대수적 성질
A = (rolls >= 4).astype(int)  # P(A) = 3/6
B = (rolls % 2 == 0).astype(int)  # P(B) = 3/6 (짝수: 2,4,6)

# 교집합: A ∩ B = {4, 6}
AB_product = A * B
AB_indicator = ((rolls >= 4) & (rolls % 2 == 0)).astype(int)
print(f"\nIntersection via product: {np.mean(AB_product):.4f}")
print(f"Intersection via indicator: {np.mean(AB_indicator):.4f}")
print(f"Theoretical P(A∩B) = {2/6:.4f}")

# 합집합: A ∪ B = {2, 4, 5, 6}
AB_union = A + B - A * B
print(f"Union via formula: {np.mean(AB_union):.4f}")
print(f"Theoretical P(A∪B) = {4/6:.4f}")
```

## 연습문제

**연습문제 1.** $P(A) = 0.4$, $P(B) = 0.5$, $P(A \cap B) = 0.2$ 인 사건 $A$ 와 $B$ 에 대하여 $E[\mathbf{1}_A + \mathbf{1}_B]$ 와 $\text{Var}(\mathbf{1}_A + \mathbf{1}_B)$ 를 구하여라.

??? success "연습문제 1 풀이"
    $E[\mathbf{1}_A + \mathbf{1}_B] = P(A) + P(B) = 0.9$ 이다.

    $\text{Var}(\mathbf{1}_A + \mathbf{1}_B) = \text{Var}(\mathbf{1}_A) + \text{Var}(\mathbf{1}_B) + 2\text{Cov}(\mathbf{1}_A, \mathbf{1}_B)$ 이다.

    $\text{Var}(\mathbf{1}_A) = 0.4 \times 0.6 = 0.24$, $\text{Var}(\mathbf{1}_B) = 0.5 \times 0.5 = 0.25$ 이다.

    $\text{Cov}(\mathbf{1}_A, \mathbf{1}_B) = P(A \cap B) - P(A)P(B) = 0.2 - 0.2 = 0$ 이다.

    $$
    \text{Var}(\mathbf{1}_A + \mathbf{1}_B) = 0.24 + 0.25 + 0 = 0.49
    $$

---

**연습문제 2.** $\mathbf{1}_{A \cup B \cup C}$ 를 $\mathbf{1}_A$, $\mathbf{1}_B$, $\mathbf{1}_C$ 로 나타내어라. 그런 다음 기댓값을 취하여 세 사건에 대한 포함배제 공식을 이끌어내어라.

??? success "연습문제 2 풀이"
    $$
    \mathbf{1}_{A \cup B \cup C} = 1 - (1 - \mathbf{1}_A)(1 - \mathbf{1}_B)(1 - \mathbf{1}_C)
    $$

    전개하면 다음과 같다.

    $$
    = \mathbf{1}_A + \mathbf{1}_B + \mathbf{1}_C - \mathbf{1}_A\mathbf{1}_B - \mathbf{1}_A\mathbf{1}_C - \mathbf{1}_B\mathbf{1}_C + \mathbf{1}_A\mathbf{1}_B\mathbf{1}_C
    $$

    양변에 기댓값을 취하고 $E[\mathbf{1}_A\mathbf{1}_B] = P(A \cap B)$ 를 쓰면 다음을 얻는다.

    $$
    P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(AB) - P(AC) - P(BC) + P(ABC)
    $$

    $\square$

---

**연습문제 3.** $(\mathbf{1}_A)^2 = \mathbf{1}_A$ 임을 증명하고, 이를 써서 $\text{Var}(\mathbf{1}_A) = P(A)(1 - P(A))$ 를 이끌어내어라.

??? success "연습문제 3 풀이"
    $\mathbf{1}_A \in \{0, 1\}$ 이고 $0^2 = 0$, $1^2 = 1$ 이므로 $(\mathbf{1}_A)^2 = \mathbf{1}_A$ 이다.

    따라서 $E[(\mathbf{1}_A)^2] = E[\mathbf{1}_A] = P(A)$ 이고 다음을 얻는다.

    $$
    \text{Var}(\mathbf{1}_A) = E[(\mathbf{1}_A)^2] - (E[\mathbf{1}_A])^2 = P(A) - P(A)^2 = P(A)(1 - P(A))
    $$

    $\square$

---

**연습문제 4.** 공정한 주사위를 한 번 던진다. $A$ 를 "눈이 짝수이다", $B$ 를 "눈이 $\geq 4$ 이다"라 하자. 여섯 가지 결과를 모두 따져 $\mathbf{1}_{A \cap B} = \mathbf{1}_A \cdot \mathbf{1}_B$ 임을 보여라.

??? success "연습문제 4 풀이"
    | 결과 | $\mathbf{1}_A$ | $\mathbf{1}_B$ | $\mathbf{1}_A \cdot \mathbf{1}_B$ | $\mathbf{1}_{A \cap B}$ |
    |:---:|:---:|:---:|:---:|:---:|
    | 1 | 0 | 0 | 0 | 0 |
    | 2 | 1 | 0 | 0 | 0 |
    | 3 | 0 | 0 | 0 | 0 |
    | 4 | 1 | 1 | 1 | 1 |
    | 5 | 0 | 1 | 0 | 0 |
    | 6 | 1 | 1 | 1 | 1 |

    모든 칸이 일치하므로 $\mathbf{1}_{A \cap B} = \mathbf{1}_A \cdot \mathbf{1}_B$ 임이 확인된다. $\checkmark$

---

**연습문제 5.** $X_1, \ldots, X_n$ 을 $P(X_i > 0) = p$ 인 i.i.d. 확률변수라 하고 $Y = \sum_{i=1}^n \mathbf{1}_{\{X_i > 0\}}$ 이라 하자. $Y$ 의 분포는 무엇이며 그 까닭은 무엇인가?

??? success "연습문제 5 풀이"
    각 $\mathbf{1}_{\{X_i > 0\}}$ 는 Bernoulli($p$) 확률변수이다. $X_1, \ldots, X_n$ 이 서로 독립이므로 지시확률변수들도 서로 독립이다. 서로 독립인 $n$ 개의 Bernoulli($p$) 확률변수의 합이므로 다음과 같다.

    $$
    Y \sim \text{Binomial}(n, p)
    $$
