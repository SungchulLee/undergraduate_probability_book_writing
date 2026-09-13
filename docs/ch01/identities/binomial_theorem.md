# 이항정리

## 개요

**이항정리**는 $(x + y)^n$ 을 이항계수가 들어간 항들의 합으로 전개해 준다. 이는 대수와 조합론을 이어 준다. 전개식의 각 계수가 항을 고르는 방법의 수를 세기 때문이다.

## 정리의 서술

$$\boxed{(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k}}$$

여기서 **이항계수**는 다음과 같다.

$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$

## 조합적 뜻풀이

$(x + y)^n = (x + y)(x + y) \cdots (x + y)$ 를 전개할 때, 전개식의 각 항은 $n$ 개의 인수마다 $x$ 또는 $y$ 를 하나씩 골라 만들어진다.

$x^k y^{n-k}$ 항은 $n$ 개의 인수 가운데 정확히 $k$ 개에서 $x$ 를 고르고(나머지 $n - k$ 개에서는 $y$ 를 고를 때) 나온다. 이렇게 고르는 방법의 수가 $\binom{n}{k}$ 이다.

## 특별한 경우

**$x = y = 1$ 로 두면:**

$$2^n = \sum_{k=0}^{n} \binom{n}{k}$$

이는 원소가 $n$ 개인 집합의 부분집합이 모두 $2^n$ 개임을 말한다.

**$x = 1, y = -1$ 로 두면:**

$$0 = \sum_{k=0}^{n} (-1)^k \binom{n}{k}$$

이는 크기가 짝수인 부분집합의 개수와 홀수인 부분집합의 개수가 같음을 말한다.

## 다항으로의 일반화

**다항 전개**는 이항정리를 $m$ 개의 항으로 넓힌 것이다.

$$(x_1 + x_2 + \cdots + x_m)^n = \sum_{k_1 + k_2 + \cdots + k_m = n} \binom{n}{k_1 \; k_2 \; \cdots \; k_m} x_1^{k_1} x_2^{k_2} \cdots x_m^{k_m}$$

여기서 **다항계수**는 다음과 같다.

$$\binom{n}{k_1 \; k_2 \; \cdots \; k_m} = \frac{n!}{k_1! \, k_2! \cdots k_m!}$$

## 파이썬 구현

```python
from math import comb, factorial

def binomial_expansion(n):
    """
    (x + y)^n 전개식의 계수들을 돌려준다.
    
    매개변수
    ----------
    n : int
        지수.
    
    반환값
    -------
    list of int
        이항계수 [C(n,0), C(n,1), ..., C(n,n)].
    """
    return [comb(n, k) for k in range(n + 1)]

# 예: (x + y)^5
n = 5
coeffs = binomial_expansion(n)
print(f"(x + y)^{n} coefficients: {coeffs}")
# Output: [1, 5, 10, 10, 5, 1]

# 확인: 계수의 합 = 2^n
print(f"Sum of coefficients: {sum(coeffs)}")
print(f"2^{n} = {2**n}")

# 확인: 부호를 번갈아 가며 더하면 0
alt_sum = sum((-1)**k * c for k, c in enumerate(coeffs))
print(f"Alternating sum: {alt_sum}")

# 다항 전개: (x + y + z)^3
n = 3
print(f"\n(x + y + z)^{n} expansion:")
for k1 in range(n + 1):
    for k2 in range(n - k1 + 1):
        k3 = n - k1 - k2
        coeff = factorial(n) // (factorial(k1) * factorial(k2) * factorial(k3))
        terms = []
        if k1 > 0:
            terms.append(f"x^{k1}" if k1 > 1 else "x")
        if k2 > 0:
            terms.append(f"y^{k2}" if k2 > 1 else "y")
        if k3 > 0:
            terms.append(f"z^{k3}" if k3 > 1 else "z")
        term_str = " * ".join(terms) if terms else "1"
        print(f"  {coeff} * {term_str}")
```

## 핵심 정리

이항정리는 대수와 조합론을 잇는 다리이다. $(x+y)^n$ 전개식의 계수 $\binom{n}{k}$ 는 $x$ 를 내놓을 인수 $k$ 개(그리고 $y$ 를 내놓을 인수 $n-k$ 개)를 고르는 방법의 수를 센다. 다항 전개는 이를 항이 몇 개이든 쓸 수 있도록 넓힌 것이며, 그 계수가 다항계수이다.

## 연습문제

**연습문제 1.** 이항정리를 이용하여 $\sum_{k=0}^{n} k \binom{n}{k}$ 를 계산하여라.

??? success "연습문제 1 풀이"
    $(1+x)^n = \sum_{k=0}^n \binom{n}{k} x^k$ 의 양변을 $x$ 에 대하여 미분한다.

    $$
    n(1+x)^{n-1} = \sum_{k=1}^{n} k\binom{n}{k} x^{k-1}
    $$

    여기에 $x = 1$ 을 넣는다.

    $$
    \sum_{k=0}^{n} k\binom{n}{k} = n \cdot 2^{n-1}
    $$

---

**연습문제 2.** $\sum_{k=0}^{n} (-1)^k \binom{n}{k} 3^{n-k} = 2^n$ 임을 증명하여라.

??? success "연습문제 2 풀이"
    이항정리에서 $x = -1$, $y = 3$ 으로 두면 다음을 얻는다.

    $$
    (-1 + 3)^n = \sum_{k=0}^n \binom{n}{k}(-1)^k \cdot 3^{n-k} = 2^n
    $$

    $\square$

---

**연습문제 3.** $(2x - 3)^7$ 에서 $x^4$ 의 계수를 구하여라.

??? success "연습문제 3 풀이"
    이항정리에서 $a = 2x$, $b = -3$ 으로 두면 다음을 얻는다.

    $$
    (2x - 3)^7 = \sum_{k=0}^{7} \binom{7}{k}(2x)^k(-3)^{7-k}
    $$

    $x^4$ 항은 $k = 4$ 일 때 나온다.

    $$
    \binom{7}{4}(2)^4(-3)^3 = 35 \cdot 16 \cdot (-27) = -15120
    $$

---

**연습문제 4.** 이항정리를 이용하여 항등식 $\sum_{k=0}^{n} \binom{n}{k}^2 = \binom{2n}{n}$ 을 증명하여라.

??? success "연습문제 4 풀이"
    $(1+x)^n (1+x)^n = (1+x)^{2n}$ 을 생각하자. 오른쪽 변에서 $x^n$ 의 계수는 $\binom{2n}{n}$ 이다.

    왼쪽 변에서는 두 전개식의 계수를 합성곱으로 엮어 $x^n$ 의 계수를 얻는다.

    $$
    \sum_{k=0}^{n} \binom{n}{k}\binom{n}{n-k} = \sum_{k=0}^{n} \binom{n}{k}^2
    $$

    $\binom{n}{n-k} = \binom{n}{k}$ 이기 때문이다. 양변을 견주면 $\sum_{k=0}^{n} \binom{n}{k}^2 = \binom{2n}{n}$ 을 얻는다. $\square$

---

**연습문제 5.** 다항 전개를 이용하여 $(x + y + z)^{10}$ 의 전개식에 나오는 항의 개수를 구하여라.

??? success "연습문제 5 풀이"
    각 항은 $k_1 + k_2 + k_3 = 10$ 의 음이 아닌 정수해 하나에 대응된다. 막대와 별에 따라 그런 해의 개수는 다음과 같다.

    $$
    \binom{10 + 3 - 1}{3 - 1} = \binom{12}{2} = 66
    $$
