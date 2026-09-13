# 조합과 이항계수

## 개요

**조합**은 순서를 따지지 않고 대상을 고르는 것이다. 서로 다른 $n$ 개의 대상에서 $k$ 개를 고르는(순서는 따지지 않는) 방법의 수가 바로 **이항계수**이다.

## 정의

이항계수 "$n$ 에서 $k$ 고르기"는 다음과 같이 정의된다.

$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$

## 여럿 대 하나 원리를 이용한 유도

유도는 순열과 조합을 이어 주는 두 단계로 이루어진다.

**1단계: 순서를 따진 뽑기(순열)를 센다.**

$n$ 명 가운데 $k$ 명을 골라 서로 구별되는 $k$ 개의 자리를 채운다. 곱셈 법칙에 따라 다음을 얻는다.

$$P(n,k) = n \times (n-1) \times (n-2) \times \cdots \times (n-k+1)$$

**2단계: 순서를 지운다(여럿 대 하나).**

$k$ 명으로 이루어진 위원회 하나는 $k!$ 가지 서로 다른 순서로 늘어놓을 수 있다. 즉 순서를 따진 뽑기에서 순서를 따지지 않는 뽑기로 가는 $k!$ 대 $1$ 대응이 있다.

$$\binom{n}{k} = \frac{P(n,k)}{k!} = \frac{n \times (n-1) \times \cdots \times (n-k+1)}{k!} = \frac{n!}{k!(n-k)!}$$

## 같은 것을 두 가지로 세기

PDF에서는 같은 양을 서로 다른 두 방법으로 세어 얻는 멋진 항등식 몇 가지를 소개한다.

### 대칭 항등식

**방법 1:** 위원회를 이룰 $k$ 명을 고른다: $\binom{n}{k}$

**방법 2:** 빼놓을 $n - k$ 명을 고른다(나머지가 위원회가 된다): $\binom{n}{n-k}$

둘 다 같은 것을 세므로 다음이 성립한다.

$$\binom{n}{k} = \binom{n}{n-k}$$

### 위원장을 뽑는 위원회

**방법 1:** 위원 $k$ 명을 고른 뒤 그 가운데 1명을 위원장으로 뽑는다: $k \binom{n}{k}$

**방법 2:** $n$ 명 가운데 위원장 1명을 먼저 뽑고, 남은 $k-1$ 명의 위원을 고른다: $n \binom{n-1}{k-1}$

$$k\binom{n}{k} = n\binom{n-1}{k-1}$$

이 항등식을 **흡수 항등식**이라 부르기도 한다.

## 파이썬 구현

```python
from math import comb, factorial

def binomial_coefficient(n, k):
    """
    C(n, k) = n! / (k! * (n-k)!) 를 계산한다.
    
    매개변수
    ----------
    n : int
        전체 대상의 개수.
    k : int
        고를 대상의 개수.
    
    반환값
    -------
    int
        조합의 개수.
    """
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

# 예: 10명 가운데 위원 3명 고르기
n, k = 10, 3
print(f"C({n}, {k}) = {binomial_coefficient(n, k)}")
print(f"Verification (math.comb): {comb(n, k)}")
# Output: C(10, 3) = 120

# 대칭 항등식 확인하기
print(f"\nSymmetry: C({n}, {k}) = {comb(n, k)}, C({n}, {n-k}) = {comb(n, n-k)}")

# 흡수 항등식 확인하기: k * C(n,k) = n * C(n-1, k-1)
lhs = k * comb(n, k)
rhs = n * comb(n - 1, k - 1)
print(f"Absorption: {k}*C({n},{k}) = {lhs}, {n}*C({n-1},{k-1}) = {rhs}")

# 모두 늘어놓아 확인하기
from itertools import combinations
people = list(range(1, n + 1))
committees = list(combinations(people, k))
print(f"\nVerification by enumeration: {len(committees)}")
```

## 핵심 정리

이항계수 $\binom{n}{k}$ 는 순서를 따지지 않는 뽑기의 개수를 센다. 여럿 대 하나 원리에 따라 순열의 개수를 $k!$ 로 나누면 자연스럽게 얻어진다. 같은 양을 서로 다르게 쪼개어 두 가지 방법으로 세는 기법은 강력한 조합 항등식들을 낳는다.

## 연습문제

**연습문제 1.** 표준 카드 한 벌은 52장이다(끗수 13가지, 무늬 4가지). 포커 패는 카드 5장으로 이루어진다.

**(a)** 가능한 포커 패는 몇 가지인가?

**(b)** 원페어(같은 끗수 카드 2장과, 서로 다른 세 끗수의 카드 3장)인 패는 몇 가지인가?

**(c)** 풀하우스(한 끗수 3장과 다른 끗수 2장)인 패는 몇 가지인가?

??? success "연습문제 1 풀이"
    **(a)** $\binom{52}{5} = 2{,}598{,}960$

    **(b)** 페어가 될 끗수를 고른다: $\binom{13}{1}$. 그 페어의 무늬 2가지를 고른다: $\binom{4}{2}$. 나머지 세 끗수를 고른다: $\binom{12}{3}$. 각각의 무늬를 하나씩 고른다: $4^3$.
    전체: $13 \times 6 \times 220 \times 64 = 1{,}098{,}240$

    **(c)** 3장이 될 끗수를 고른다: $13$. 무늬 3가지를 고른다: $\binom{4}{3} = 4$. 페어가 될 끗수를 고른다: $12$. 무늬 2가지를 고른다: $\binom{4}{2} = 6$.
    전체: $13 \times 4 \times 12 \times 6 = 3{,}744$
