# 콜모고로프 공리

## 정의

**확률측도** $P$ 는 사건 $A$ 위에 정의된 실수값 함수이다.

$$
A \xrightarrow{P} P(A)
$$

더 정확히 말하면, $P$ 는 사건들의 모임에서 실수로 가는 함수로서 다음 세 가지 공리를 만족한다.

## 세 가지 공리

### 공리 1: 정규화

$$
P(\Omega) = 1, \qquad P(\emptyset) = 0
$$

전사건의 확률은 1이고, 공사건의 확률은 0이다.

### 공리 2: 음이 아님

$$
0 \leq P(A) \leq 1 \quad \text{모든 사건 } A \text{ 에 대해}
$$

모든 사건의 확률은 0과 1 사이의 값이다.

### 공리 3: 가산가법성 (σ-가법성)

**쌍마다 서로소**인 사건열 $A_1, A_2, \ldots$ 에 대해 다음이 성립한다.

$$
P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)
$$

사건들이 동시에 일어날 수 없다면, 그 합집합의 확률은 각 사건의 확률을 모두 더한 값과 같다.

!!! note "역사 한 토막"
    이 공리들은 안드레이 콜모고로프가 1933년에 펴낸 논저 *Grundbegriffe der Wahrscheinlichkeitsrechnung*(확률론의 기초)에서 체계를 갖추었다. 이 공리적 틀은 확률론을 측도론 위에 세움으로써 엄밀한 수학의 자리에 올려놓았다.

## 확률 삼중쌍 (Ω, F, P)

형식을 갖추어 말하면 확률 모형은 세 가지로 이루어진다.

1. **표본공간** $\Omega$: 일어날 수 있는 모든 결과의 집합
2. **$\sigma$-대수** $\mathcal{F}$: 여집합과 가산합집합에 대해 닫혀 있는 $\Omega$ 의 부분집합들의 모임("사건"들)
3. **확률측도** $P$: 세 공리를 만족하는 함수 $P: \mathcal{F} \to [0,1]$

표본공간이 유한하거나 가산일 때는 보통 $\mathcal{F} = 2^\Omega$(모든 부분집합)로 잡는다. $\sigma$-대수는 $\mathbb{R}$ 처럼 비가산인 공간에서 비로소 중요해진다.

## 왜 이런 공리인가

이 공리들은 확률이라는 개념이 앞뒤가 맞으려면 최소한 갖추어야 할 조건을 담고 있다.

- **공리 1**은 눈금을 정한다. 확실한 것은 1, 불가능한 것은 0이다.
- **공리 2**는 확률이 "일어날 법한 정도의 비율"로서 뜻을 갖도록 해 준다.
- **공리 3**은 가장 강력한 공리이다. 복잡한 사건을 겹치지 않는 더 단순한 조각으로 쪼개어 확률을 계산할 수 있게 해 준다.

!!! tip "따라 나오는 유한가법성"
    공리 3에서 곧바로 **유한가법성**이 따라 나온다. 쌍마다 서로소인 사건 $A_1, \ldots, A_n$ 에 대해 다음이 성립한다.

    $$
    P\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i=1}^{n} P(A_i)
    $$

    공리 3에서 $A_{n+1} = A_{n+2} = \cdots = \emptyset$ 로 두기만 하면 된다.

## 확률측도 만들기

유한한 표본공간 $\Omega = \{\omega_1, \omega_2, \ldots, \omega_n\}$ 에서 다음 두 조건을 만족하도록 무게 $p_1, p_2, \ldots, p_n$ 을 매기면,

1. 모든 $i$ 에 대해 $p_i \geq 0$
2. $\sum_{i=1}^{n} p_i = 1$

$P(\{\omega_i\}) = p_i$ 로 정의된 것이 곧 올바른 확률측도가 된다.

## 파이썬 예제

```python
import numpy as np

# Ω = {1, 2, 3, 4, 5, 6} 위에 확률측도를 정의한다
# 예: P(6) = 1/2 이고 나머지는 같은 정도로 일어나는 치우친 주사위
omega = [1, 2, 3, 4, 5, 6]
weights = [1/10, 1/10, 1/10, 1/10, 1/10, 1/2]

# 공리 1 확인: P(Ω) = 1
print(f"Axiom 1: P(Ω) = {sum(weights):.4f}")

# 공리 2 확인: 0 ≤ P(ω) ≤ 1
print(f"Axiom 2: All probabilities in [0,1]: {all(0 <= w <= 1 for w in weights)}")

# 공리 3 확인(유한인 경우): 서로소인 사건
# A = {1, 2}, B = {3, 4}  → 서로소
P_A = weights[0] + weights[1]
P_B = weights[2] + weights[3]
P_AuB = sum(weights[i] for i in [0, 1, 2, 3])
print(f"\nAxiom 3 check:")
print(f"P(A) = {P_A:.4f}, P(B) = {P_B:.4f}")
print(f"P(A) + P(B) = {P_A + P_B:.4f}")
print(f"P(A ∪ B) = {P_AuB:.4f}")
print(f"P(A ∪ B) = P(A) + P(B): {np.isclose(P_AuB, P_A + P_B)}")

# 모의실험으로 확인하기
np.random.seed(42)
n_sim = 100_000
samples = np.random.choice(omega, size=n_sim, p=weights)
print(f"\nSimulated frequencies:")
for val in omega:
    freq = np.mean(samples == val)
    print(f"  P({val}) = {weights[val-1]:.2f}, simulated = {freq:.4f}")
```

**실행 결과:**
```
Axiom 1: P(Ω) = 1.0000
Axiom 2: All probabilities in [0,1]: True

Axiom 3 check:
P(A) = 0.2000, P(B) = 0.2000
P(A) + P(B) = 0.4000
P(A ∪ B) = 0.4000
P(A ∪ B) = P(A) + P(B): True

Simulated frequencies:
  P(1) = 0.10, simulated = 0.1003
  P(2) = 0.10, simulated = 0.0988
  P(3) = 0.10, simulated = 0.1001
  P(4) = 0.10, simulated = 0.1007
  P(5) = 0.10, simulated = 0.1002
  P(6) = 0.50, simulated = 0.4999
```

## 연습문제

**연습문제 1.** $\Omega = \{a, b, c, d\}$ 라 하자. 다음 가운데 올바른 확률측도를 정의하는 것은 어느 것인지 판정하고, 아니라면 어떤 공리를 어겼는지 밝혀라.

**(a)** $P(\{a\}) = 0.3,\; P(\{b\}) = 0.3,\; P(\{c\}) = 0.3,\; P(\{d\}) = 0.3$

**(b)** $P(\{a\}) = 0.5,\; P(\{b\}) = 0.3,\; P(\{c\}) = 0.1,\; P(\{d\}) = 0.1$

**(c)** $P(\{a\}) = 0.6,\; P(\{b\}) = 0.5,\; P(\{c\}) = -0.2,\; P(\{d\}) = 0.1$

??? success "연습문제 1 풀이"
    **(a)** 올바르지 않다. $\sum p_i = 1.2 \neq 1$ 이다. 공리 1($P(\Omega) = 1$)을 어긴다.

    **(b)** 올바르다. 모든 $p_i \in [0,1]$ 이고 $\sum p_i = 1$ 이다.

    **(c)** 올바르지 않다. $P(\{c\}) = -0.2 < 0$ 이다. 공리 2(음이 아님)를 어긴다.

---

**연습문제 2.** 사건 $A$ 와 $B$ 에 대해 $P(A) = 0.6$, $P(B) = 0.7$ 이라 하자. $P(A \cap B) \geq 0.3$ 임을 증명하여라.

??? success "연습문제 2 풀이"
    포함배제 공식에 따라 다음이 성립한다.

    $$
    P(A \cup B) = P(A) + P(B) - P(A \cap B)
    $$

    공리 2에 따라 $P(A \cup B) \leq 1$ 이므로 다음을 얻는다.

    $$
    1 \geq 0.6 + 0.7 - P(A \cap B) \implies P(A \cap B) \geq 0.3
    $$

    $\square$

---

**연습문제 3.** 임의의 사건 $A$ 에 대해 $P(A^c) = 1 - P(A)$ 임을 공리에서 출발해 증명하여라.

??? success "연습문제 3 풀이"
    $A$ 와 $A^c$ 는 서로소이고 $A \cup A^c = \Omega$ 이므로 공리 3(유한가법성)에 따라 다음을 얻는다.

    $$
    P(\Omega) = P(A) + P(A^c)
    $$

    공리 1에 따라 $P(\Omega) = 1$ 이므로 $P(A^c) = 1 - P(A)$ 이다. $\square$

---

**연습문제 4.** 사건 $A_1, A_2, \ldots$ 가 쌍마다 서로소이고 $n = 1, 2, 3, \ldots$ 에 대해 $P(A_n) = \frac{1}{2^n}$ 이라 하자. $P\!\left(\bigcup_{n=1}^{\infty} A_n\right) = 1$ 인가?

??? success "연습문제 4 풀이"
    가산가법성(공리 3)에 따라 다음을 얻는다.

    $$
    P\!\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} P(A_n) = \sum_{n=1}^{\infty} \frac{1}{2^n} = 1
    $$

    그렇다. 이 확률은 1이다.

---

**연습문제 5.** 가산가법성 없이 유한가법성만으로는 엄밀한 확률론을 세울 수 없는 까닭을 설명하여라. 그 차이가 실제로 문제가 되는 구체적인 예를 들어라.

??? success "연습문제 5 풀이"
    균등분포를 얹은 $\Omega = (0, 1]$ 을 생각하자. $n = 1, 2, 3, \ldots$ 에 대해 $A_n = (1/(n+1), 1/n]$ 이라 두자. 이들은 쌍마다 서로소이고 $\bigcup_{n=1}^{\infty} A_n = (0, 1] = \Omega$ 이므로 $P(\Omega) = \sum_{n=1}^{\infty} P(A_n) = 1$ 이어야 한다.

    그런데 유한가법성만 가지고서는 $P\!\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} P(A_n)$ 를 이끌어 낼 수 없다. 유한합집합만 다룰 수 있기 때문이다. 그러면 $P(\Omega) = 1$ 이면서도 가산분할의 확률의 합이 $P(\Omega)$ 가 되지 않는 괴상한 "확률측도"를 만들어 낼 수 있게 된다. 가산가법성은 이런 이상한 일을 막아 주고, 사건의 극한이 앞뒤 맞게 움직이도록(확률의 연속성) 보장해 준다.
