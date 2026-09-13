# 다항계수

## 개요

**다항계수**는 $n$ 개의 대상을 셋 이상의 묶음으로 나누는 경우까지 이항계수를 넓힌 것이다. 서로 다른 $n$ 개의 대상을 크기가 정해진 여러 묶음으로 가르는 방법의 수를 세며, 같은 뜻으로 같은 종류가 여럿 있는 대상들의 서로 다른 배열의 수를 센다.

## 정의

다항계수는 다음과 같이 정의된다.

$$\binom{n}{k_1 \; k_2 \; \cdots \; k_m} = \frac{n!}{k_1! \, k_2! \cdots k_m!}$$

여기서 $k_1 + k_2 + \cdots + k_m = n$ 이다.

## 중복이 있는 순열과의 연결

중복이 있는 순열 절에서 유도했듯이, $i$ 종류가 $k_i$ 개씩 있는 $n$ 개의 대상을 늘어놓는 서로 다른 배열의 수는 정확히 다항계수이다.

$$\frac{n!}{k_1! \, k_2! \cdots k_m!}$$

예를 들어 BBOOO로 만드는 서로 다른 낱말의 수는 다음과 같다.

$$\binom{5}{2 \; 3} = \frac{5!}{2! \cdot 3!} = 10$$

## 다항 전개

다항계수는 **다항 전개**의 계수로 나타난다.

$$(x_1 + x_2 + \cdots + x_m)^n = \sum_{k_1 + k_2 + \cdots + k_m = n} \binom{n}{k_1 \; k_2 \; \cdots \; k_m} x_1^{k_1} x_2^{k_2} \cdots x_m^{k_m}$$

여기서 합은 $k_1 + k_2 + \cdots + k_m = n$ 을 만족하는 모든 음이 아닌 정수해에 걸쳐 이루어진다.

각 항 $\binom{n}{k_1 \cdots k_m} x_1^{k_1} \cdots x_m^{k_m}$ 은, $(x_1 + \cdots + x_m)$ 이라는 $n$ 개의 인수마다 $x_i$ 가운데 하나를 골라 $x_i$ 를 $k_i$ 번 고르게 하는 방법의 수를 센다.

## 특별한 경우: 이항계수

$m = 2$ 이면 다항계수는 이항계수가 된다.

$$\binom{n}{k_1 \; k_2} = \frac{n!}{k_1! \, k_2!} = \binom{n}{k_1}$$

$k_2 = n - k_1$ 이기 때문이다.

## 파이썬 구현

```python
from math import factorial, comb
from itertools import product

def multinomial(n, groups):
    """
    다항계수 n! / (k1! * k2! * ... * km!) 을 계산한다.
    
    매개변수
    ----------
    n : int
        전체 대상의 개수.
    groups : list of int
        각 묶음의 크기 (합이 n이어야 한다).
    
    반환값
    -------
    int
        다항계수.
    """
    assert sum(groups) == n, "Group sizes must sum to n"
    result = factorial(n)
    for k in groups:
        result //= factorial(k)
    return result

# 예: BBOOO로 만드는 낱말
print(f"Multinomial(5; 2, 3) = {multinomial(5, [2, 3])}")
# Output: 10

# 예: 12명을 4명씩 세 묶음으로 나누기
print(f"Multinomial(12; 4, 4, 4) = {multinomial(12, [4, 4, 4])}")
# Output: 34650

# 다항 전개 확인하기: (x + y + z)^3
# 모든 항과 그 계수
n = 3
m = 3
print(f"\nMultinomial expansion of (x1 + x2 + x3)^{n}:")
for k1 in range(n + 1):
    for k2 in range(n - k1 + 1):
        k3 = n - k1 - k2
        coeff = multinomial(n, [k1, k2, k3])
        if coeff > 0:
            print(f"  ({k1},{k2},{k3}): coefficient = {coeff}")
```

## 핵심 정리

다항계수 $\frac{n!}{k_1! \cdots k_m!}$ 은 두 관점을 하나로 묶는다. 같은 종류가 여럿 있는 대상들의 서로 다른 배열의 수를 세는 동시에, 다항 전개의 계수를 준다. 이항계수는 $m = 2$ 인 특별한 경우이다.

## 연습문제

**연습문제 1.** 단어 MISSISSIPPI의 글자로 만들 수 있는 서로 다른 배열은 몇 가지인가?

??? success "연습문제 1 풀이"
    MISSISSIPPI는 글자가 11개이며 M(1개), I(4개), S(4개), P(2개)로 이루어져 있다. 다항계수는 다음과 같다.

    $$
    \binom{11}{1\;4\;4\;2} = \frac{11!}{1!\,4!\,4!\,2!} = \frac{39916800}{1 \cdot 24 \cdot 24 \cdot 2} = 34650
    $$

---

**연습문제 2.** 12명으로 이루어진 학급을 5명, 4명, 3명의 과제 모둠 세 개로 나눈다. 몇 가지 방법이 있는가?

??? success "연습문제 2 풀이"
    $$
    \binom{12}{5\;4\;3} = \frac{12!}{5!\,4!\,3!} = \frac{479001600}{120 \cdot 24 \cdot 6} = 27720
    $$

---

**연습문제 3.** $(x + y + z)^6$ 의 전개식에서 $x^2 y^3 z$ 의 계수를 구하여라.

??? success "연습문제 3 풀이"
    다항 전개에 따라 계수는 다음과 같다.

    $$
    \binom{6}{2\;3\;1} = \frac{6!}{2!\,3!\,1!} = \frac{720}{2 \cdot 6 \cdot 1} = 60
    $$

---

**연습문제 4.** 합이 음이 아닌 정수해 전체에 걸쳐 이루어질 때 $\sum_{k_1+k_2+\cdots+k_m = n} \binom{n}{k_1\;k_2\;\cdots\;k_m} = m^n$ 임을 증명하여라.

??? success "연습문제 4 풀이"
    다항 전개에서 $x_1 = x_2 = \cdots = x_m = 1$ 로 두면 다음을 얻는다.

    $$
    (1 + 1 + \cdots + 1)^n = m^n = \sum_{k_1+\cdots+k_m=n} \binom{n}{k_1\;\cdots\;k_m} \cdot 1^{k_1} \cdots 1^{k_m}
    $$

    $\square$

---

**연습문제 5.** 어느 피자 가게가 토핑 3종류를 내놓는다. 손님이 토핑을 정확히 8인분 주문한다(중복 허용, 피자 위의 순서는 상관없다). 다항계수의 틀에서 볼 때, 가능한 주문의 수가 $\binom{8}{k_1\;k_2\;k_3}$ 을 합한 것이 아니라 $\binom{10}{2}$ 인 까닭을 설명하여라.

??? success "연습문제 5 풀이"
    같은 종류의 토핑끼리는 구별되지 않고 순서도 상관없다. 이는 막대와 별 문제이다. 똑같은 8인분을 3종류에 나누어 주는 것이므로 답은 다음과 같다.

    $$
    \binom{8 + 3 - 1}{3 - 1} = \binom{10}{2} = 45
    $$

    다항계수 $\binom{8}{k_1\;k_2\;k_3}$ 은 이름표가 붙은 대상들의 *순서를 따진 배열*의 수를 센다. 인분마다 서로 구별되고 늘어놓는 순서가 뜻을 가질 때라면 그 계수가 맞다. 그러나 같은 토핑의 인분끼리는 똑같고 배열 순서도 아무 상관이 없으므로 막대와 별이 올바른 모형이다.
