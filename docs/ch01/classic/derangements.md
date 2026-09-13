# 짝맞추기 문제와 완전순열

## 개요

**짝맞추기 문제**(**모자 찾기 문제** 또는 **problème des rencontres**라고도 한다)는 다음을 묻는다. $\{1, 2, \ldots, n\}$ 위의 일대일대응 가운데 **고정점이 하나도 없는** 것은 몇 개인가? 이런 순열을 **완전순열**이라 한다.

## 문제 설정

$f$ 를 $\{1, 2, \ldots, n\}$ 위의 일대일대응(순열)이라 하자.

$f(x) = x$ 를 만족하는 점 $x$ 를 $f$ 의 **고정점**이라 한다.

**목표:** 고정점이 **하나도 없는** 순열(완전순열)의 개수를 센다.

### 집합 정하기

- $\Omega$ — $\{1, 2, \ldots, n\}$ 위의 모든 일대일대응 $f$ 의 집합. 따라서 $|\Omega| = n!$
- $A_i$ — $i$ 를 고정하는(즉 $f(i) = i$ 인) 일대일대응 $f$ 의 집합
- $\bigcup_{i=1}^{n} A_i$ — **어떤** $i$ 를 고정하는 일대일대응의 집합
- $B = \Omega \setminus \bigcup_{i=1}^{n} A_i$ — 고정점이 **하나도 없는** 일대일대응(완전순열)의 집합

## 포함배제 적용하기

$|B| = |\Omega| - |\bigcup_{i=1}^{n} A_i|$ 가 필요하므로 먼저 $|\bigcup_{i=1}^{n} A_i|$ 를 계산한다.

### 교집합의 크기 구하기

**낱개 집합:** $|A_i|$ 는 $i$ 를 고정하는 순열의 개수이다. 남은 $n - 1$ 개의 원소는 자유롭게 늘어놓을 수 있다.

$$|A_i| = (n-1)!$$

이런 집합이 $\binom{n}{1}$ 개 있으므로 $\sum |A_i| = \binom{n}{1}(n-1)!$ 이다.

**두 집합의 교집합:** $|A_i \cap A_j|$ 는 $i$ 와 $j$ 를 모두 고정하는 순열의 개수이다.

$$|A_i \cap A_j| = (n-2)!$$

이런 쌍이 $\binom{n}{2}$ 개 있으므로 $\sum |A_i \cap A_j| = \binom{n}{2}(n-2)!$ 이다.

**일반적인 꼴:** $|A_{i_1} \cap A_{i_2} \cap \cdots \cap A_{i_k}|$ 는 정해진 $k$ 개의 점을 고정하는 순열의 개수이다.

$$|A_{i_1} \cap \cdots \cap A_{i_k}| = (n-k)!$$

이런 $k$ 개짜리 부분집합은 $\binom{n}{k}$ 개 있다.

### 공식 적용하기

포함배제 원리에 따라 다음을 얻는다.

$$\left|\bigcup_{i=1}^{n} A_i\right| = \sum_{k=1}^{n} (-1)^{k+1} \binom{n}{k} (n-k)!$$

$\binom{n}{k}(n-k)! = \frac{n!}{k!}$ 임을 써서 풀어 쓰면 다음과 같다.

$$\left|\bigcup_{i=1}^{n} A_i\right| = n! \left(\frac{1}{1!} - \frac{1}{2!} + \frac{1}{3!} - \cdots + (-1)^{n+1}\frac{1}{n!}\right)$$

### 완전순열의 개수

$$|B| = |\Omega| - \left|\bigcup_{i=1}^{n} A_i\right| = n! - n!\left(\frac{1}{1!} - \frac{1}{2!} + \cdots + (-1)^{n+1}\frac{1}{n!}\right)$$

$$\boxed{D_n = n!\left(1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \cdots + (-1)^n \frac{1}{n!}\right) = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}}$$

## e⁻¹ 과의 연결

$n \to \infty$ 일 때 합 $\sum_{k=0}^{n} \frac{(-1)^k}{k!}$ 은 $e^{-1}$ 로 수렴한다. 따라서 다음이 성립한다.

$$D_n \approx \frac{n!}{e}$$

더 정확히 말하면, 모든 $n \geq 1$ 에 대하여 $D_n$ 은 $n!/e$ 에 가장 가까운 정수이다.

무작위로 고른 순열이 완전순열일 확률은 다음과 같다.

$$\frac{D_n}{n!} = \sum_{k=0}^{n} \frac{(-1)^k}{k!} \xrightarrow{n \to \infty} e^{-1} \approx 0.3679$$

## 파이썬 구현

```python
from math import factorial, e, comb

def derangement_count(n):
    """
    포함배제 공식을 이용하여 {1, 2, ..., n} 의
    완전순열의 개수를 센다.
    
    매개변수
    ----------
    n : int
        집합의 크기.
    
    반환값
    -------
    int
        완전순열의 개수 D_n.
    """
    return sum((-1)**k * factorial(n) // factorial(k) for k in range(n + 1))

def derangement_count_via_ie(n):
    """
    포함배제를 단계별로 적용하여 완전순열을 센다.
    |Omega| - |union of A_i| 를 보여 준다.
    """
    omega = factorial(n)
    # 포함배제로 구한 |union A_i|
    union_size = sum(
        (-1)**(k+1) * comb(n, k) * factorial(n - k) 
        for k in range(1, n + 1)
    )
    return omega - union_size

# 작은 n에 대하여 완전순열의 개수 구하기
print("n | D_n | n! | D_n/n! | 1/e")
print("-" * 45)
for n in range(1, 11):
    d_n = derangement_count(n)
    n_fact = factorial(n)
    ratio = d_n / n_fact
    print(f"{n:2d} | {d_n:7d} | {n_fact:7d} | {ratio:.6f} | {1/e:.6f}")

# 두 방법이 일치하는지 확인하기
for n in range(1, 15):
    assert derangement_count(n) == derangement_count_via_ie(n)
print("\nBoth methods agree for n=1..14")

# 작은 n에 대하여 완전순열을 모두 늘어놓기
from itertools import permutations

def enumerate_derangements(n):
    """모든 완전순열을 하나하나 훑어 센다."""
    identity = list(range(1, n + 1))
    count = 0
    for perm in permutations(identity):
        if all(perm[i] != identity[i] for i in range(n)):
            count += 1
    return count

print("\nVerification by enumeration:")
for n in range(1, 9):
    d_formula = derangement_count(n)
    d_enum = enumerate_derangements(n)
    print(f"  n={n}: formula={d_formula}, enumeration={d_enum}, match={d_formula==d_enum}")
```

## 핵심 정리

짝맞추기 문제는 포함배제와 여집합 세기를 함께 쓰는 대표적인 보기이다. 정해진 점들을 고정하는 순열을 체계적으로 빼고 더하면 완전순열 공식 $D_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}$ 이 나온다. $D_n/n! \to 1/e$ 라는 놀라운 결과는 이산조합론을 지수함수와 이어 준다.

## 연습문제

**연습문제 1.**

**(a)** $\{1, 2, 3, 4, 5\}$ 의 완전순열의 개수 $D_5$ 를 구하여라.

**(b)** $\{1, 2, 3, 4, 5\}$ 의 순열을 무작위로 하나 고를 때 그것이 완전순열일 확률은 얼마인가?

??? success "연습문제 1 풀이"
    **(a)**

    $$
    D_5 = 5!\left(1 - 1 + \frac{1}{2} - \frac{1}{6} + \frac{1}{24} - \frac{1}{120}\right) = 120 \times \frac{11}{30} = 44
    $$

    **(b)** $P = \dfrac{D_5}{5!} = \dfrac{44}{120} = \dfrac{11}{30} \approx 0.3667$
