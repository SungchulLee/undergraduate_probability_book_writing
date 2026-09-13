# 확률의 곱셈 법칙

## 연쇄 법칙 (곱의 법칙)

**연쇄 법칙**(**곱셈 법칙**이라고도 한다)을 쓰면 조건을 차례로 걸어 가며 사건들의 교집합의 확률을 구할 수 있다.

### 두 사건

$$
P(AB) = P(A)\,P(B \mid A)
$$

조건부확률의 정의를 옮겨 쓰면 곧바로 나온다.

### 세 사건

$$
P(ABC) = P(A)\,P(B \mid A)\,P(C \mid AB)
$$

### 네 사건

$$
P(ABCD) = P(A)\,P(B \mid A)\,P(C \mid AB)\,P(D \mid ABC)
$$

### 일반적인 꼴

사건 $A_1, A_2, \ldots, A_n$ 에 대해 다음이 성립한다.

$$
P(A_1 A_2 \cdots A_n) = P(A_1)\,P(A_2 \mid A_1)\,P(A_3 \mid A_1 A_2) \cdots P(A_n \mid A_1 A_2 \cdots A_{n-1})
$$

인수마다 그 앞의 모든 사건을 조건으로 건다.

## 예제 — 생일 문제

$p(n)$ 을 $n$ 명 가운데 생일이 적어도 한 쌍 겹칠 확률이라 하자. $p(n) > 0.5$ 가 되는 가장 작은 $n$ 을 구하여라.

### 문제 설정

다음과 같이 정의하자.

$$
B_k = \{\text{앞의 } k \text{ 명의 생일이 모두 다르다}\}
$$

여사건의 확률(겹치지 않을 확률)은 연쇄 법칙으로 구할 수 있다.

$$
1 - p(n) = P(B_1 B_2 B_3 \cdots B_n)
$$

$$
= P(B_1)\,P(B_2 \mid B_1)\,P(B_3 \mid B_1 B_2) \cdots P(B_n \mid B_1 B_2 \cdots B_{n-1})
$$

### 각 인수 구하기

앞의 $k-1$ 명의 생일이 모두 다르다고 할 때, $k$ 번째 사람은 365일 가운데 $k-1$ 일을 피해야 한다.

$$
P(B_k \mid B_1 B_2 \cdots B_{k-1}) = \frac{365 - (k-1)}{365}
$$

그러므로 다음을 얻는다.

$$
1 - p(n) = 1 \cdot \frac{364}{365} \cdot \frac{363}{365} \cdots \frac{365 - (n-1)}{365}
$$

### 근사로 구하기

$x$ 가 작을 때의 근사식 $1 - x \approx e^{-x}$ 를 쓰면 다음과 같다.

$$
1 - p(n) \approx e^{-1/365} \cdot e^{-2/365} \cdots e^{-(n-1)/365} = e^{-n(n-1)/(2 \times 365)}
$$

$e^{-n(n-1)/(2 \times 365)} = 0.5$ 로 두고 풀면 다음을 얻는다.

$$
n(n-1) = 2 \times 365 \times \ln 2 \approx 506 \implies n \approx 23
$$

### 정확히 구하기

| $p(22)$ | $p(23)$ | $p(24)$ |
|---------|---------|---------|
| 0.4757 | 0.5073 | 0.5383 |

생일이 겹칠 확률이 50%를 넘으려면 사람이 적어도 **$n = 23$** 명 있어야 한다.

### 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt

# q(n) = P(n명 가운데 생일이 겹치지 않음)
q = np.ones(365)
for n in range(1, 365):
    q[n] = q[n-1] * (1 - n / 365)

# p(n) = P(n명 가운데 생일이 적어도 한 쌍 겹침)
p = 1 - q

# p(n) >= 0.5 가 되는 가장 작은 n 찾기
min_people = np.argmax(p >= 0.5) + 1  # 1부터 세므로 +1

print(f"Minimum people for >50% match probability: {min_people}")
print(f"p(22) = {p[21]:.4f}, p(23) = {p[22]:.4f}, p(24) = {p[23]:.4f}")

# 그림 그리기
plt.figure(figsize=(8, 5))
plt.plot(range(1, 366), p, 'b-')
plt.axhline(y=0.5, color='b', linestyle='--', alpha=0.5)
plt.axvline(x=min_people, color='r', linestyle='--', alpha=0.5)
plt.xlabel('Number of People')
plt.ylabel('Probability of Match')
plt.title('Birthday Problem')
plt.grid(True, alpha=0.3)
plt.xlim([0, 366])
plt.ylim([-0.1, 1.1])
plt.tight_layout()
plt.savefig('birthday_problem.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 연습문제

**연습문제 1.** 표준 52장 카드 한 벌에서 비복원으로 카드 3장을 차례로 뽑는다. 세 장이 모두 하트일 확률은 얼마인가? 연쇄 법칙을 써라.

??? success "연습문제 1 풀이"
    $H_i$ 를 $i$ 번째 카드가 하트인 사건이라 하자. 연쇄 법칙에 따라 다음을 얻는다.

    $$
    P(H_1 H_2 H_3) = P(H_1) P(H_2 \mid H_1) P(H_3 \mid H_1 H_2) = \frac{13}{52} \cdot \frac{12}{51} \cdot \frac{11}{50} = \frac{1716}{132600} \approx 0.01294
    $$

---

**연습문제 2.** 연쇄 법칙을 써서 다음 항등식을 증명하여라.

$$
P(A_1 A_2 \cdots A_n) = P(A_1)\,P(A_2 \mid A_1)\,P(A_3 \mid A_1 A_2) \cdots P(A_n \mid A_1 A_2 \cdots A_{n-1})
$$

??? success "연습문제 2 풀이"
    **$n$ 에 대한 귀납법으로 증명한다.**

    **첫 단계** ($n = 2$): 조건부확률의 정의에 따라 $P(A_2 \mid A_1) = P(A_1 A_2)/P(A_1)$ 이므로 $P(A_1 A_2) = P(A_1) P(A_2 \mid A_1)$ 이다.

    **귀납 단계.** 항등식이 사건 $n - 1$ 개에 대해 성립한다고 하자. $A_1 A_2 \cdots A_{n-1}$ 과 $A_n$ 의 쌍에 첫 단계를 적용한다.

    $$
    P(A_1 \cdots A_n) = P(A_1 \cdots A_{n-1}) \cdot P(A_n \mid A_1 \cdots A_{n-1})
    $$

    귀납 가정에 따라 다음이 성립한다.

    $$
    P(A_1 \cdots A_{n-1}) = P(A_1) P(A_2 \mid A_1) \cdots P(A_{n-1} \mid A_1 \cdots A_{n-2})
    $$

    이를 대입하면 바라던 항등식을 얻는다. $P(A_1 \cdots A_{n-1}) > 0$ 이기만 하면 모든 조건부확률이 잘 정의된다. $\square$
