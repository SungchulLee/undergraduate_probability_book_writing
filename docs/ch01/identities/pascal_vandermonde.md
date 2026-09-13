# 파스칼 법칙과 반데르몽드 항등식

## 개요

조합 항등식은 같은 양을 서로 다른 두 방법으로 세는 데서 나오는 경우가 많다. 이 절에서는 이항계수에 관한 기본 항등식인 **파스칼 법칙**과 **반데르몽드 항등식**을 다룬다.

## 파스칼 법칙

### 정리의 서술

$$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$

### 조합적 증명

$n$ 명 가운데 $k$ 명으로 이루어진 위원회를 만든다고 하자. 한 사람 $X$ 를 고정하고 두 경우로 나눈다.

- **$X$ 가 위원회에 들어가는 경우:** 나머지 $k - 1$ 명을 다른 $n - 1$ 명에서 고른다: $\binom{n-1}{k-1}$
- **$X$ 가 위원회에 들어가지 않는 경우:** $k$ 명 모두를 다른 $n - 1$ 명에서 고른다: $\binom{n-1}{k}$

이 두 경우는 서로소이고 빠짐이 없으므로 덧셈 법칙에 따라 다음을 얻는다.

$$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$

파스칼 법칙에서 **파스칼 삼각형**이 만들어진다. 파스칼 삼각형에서는 각 수가 바로 위의 두 수의 합이다.

## 반데르몽드 항등식

### 정리의 서술

$$\binom{m + n}{k} = \sum_{\ell = \max(0, k-n)}^{\min(m, k)} \binom{m}{\ell} \binom{n}{k - \ell}$$

범위를 굳이 따지지 않아도 되는 경우에는(즉 $\ell > m$ 일 때 $\binom{m}{\ell} = 0$ 이고 $k - \ell > n$ 일 때 $\binom{n}{k-\ell} = 0$ 임을 쓰면) 다음과 같이 간단해진다.

$$\binom{m + n}{k} = \sum_{\ell=0}^{k} \binom{m}{\ell} \binom{n}{k - \ell}$$

### 조합적 증명 — 남자와 여자로 이루어진 위원회

남자 $m$ 명과 여자 $n$ 명으로 이루어진 모임에서 $k$ 명의 위원회를 뽑는다고 하자.

**방법 1 (바로 세기):** $m + n$ 명 전체에서 $k$ 명을 고른다: $\binom{m+n}{k}$

**방법 2 (남녀 구성으로 나누어 세기):** 남자 $\ell$ 명과 여자 $k - \ell$ 명을 고른다.

- 남자 $m$ 명에서 $\ell$ 명을 고른다: $\binom{m}{\ell}$
- 여자 $n$ 명에서 $k - \ell$ 명을 고른다: $\binom{n}{k-\ell}$
- 가능한 모든 $\ell$ 에 대하여 더한다: $\sum_\ell \binom{m}{\ell}\binom{n}{k-\ell}$

두 방법이 같은 것을 세므로 다음이 성립한다.

$$\binom{m+n}{k} = \sum_{\ell} \binom{m}{\ell} \binom{n}{k-\ell}$$

## 파이썬 구현

```python
from math import comb

def verify_pascal(n, k):
    """파스칼 법칙 C(n,k) = C(n-1,k-1) + C(n-1,k) 를 확인한다."""
    lhs = comb(n, k)
    rhs = comb(n - 1, k - 1) + comb(n - 1, k)
    return lhs, rhs, lhs == rhs

def verify_vandermonde(m, n, k):
    """반데르몽드 항등식 C(m+n, k) = sum_l C(m,l)*C(n,k-l) 을 확인한다."""
    lhs = comb(m + n, k)
    rhs = sum(comb(m, l) * comb(n, k - l) for l in range(k + 1))
    return lhs, rhs, lhs == rhs

# 파스칼 법칙 확인하기
for n in range(2, 8):
    for k in range(1, n):
        lhs, rhs, ok = verify_pascal(n, k)
        assert ok, f"Failed for n={n}, k={k}"
print("Pascal's rule verified for n=2..7, all valid k")

# 반데르몽드 항등식 확인하기
m, n, k = 5, 7, 4
lhs, rhs, ok = verify_vandermonde(m, n, k)
print(f"\nVandermonde: C({m}+{n}, {k}) = {lhs}")
print(f"Sum of C({m},l)*C({n},{k}-l) = {rhs}")
print(f"Match: {ok}")

# 항별로 뜯어 보기
print(f"\nBreakdown (m={m} men, n={n} women, committee of {k}):")
for l in range(k + 1):
    c_m = comb(m, l)
    c_n = comb(n, k - l)
    if c_m > 0 and c_n > 0:
        print(f"  {l} men, {k-l} women: C({m},{l})*C({n},{k-l}) = {c_m}*{c_n} = {c_m*c_n}")

# 파스칼 삼각형 만들기
print("\nPascal's Triangle (rows 0-7):")
for row in range(8):
    values = [comb(row, k) for k in range(row + 1)]
    print(f"  Row {row}: {values}")
```

## 핵심 정리

파스칼 법칙과 반데르몽드 항등식은 모두 "같은 것을 두 가지로 세기" 기법으로 깔끔하게 증명된다. 파스칼 법칙은 고정한 원소 하나가 들어가느냐 마느냐로 나누고, 반데르몽드 항등식은 서로소인 두 무리에서 몇 명씩 뽑느냐로 나눈다. 두 항등식 모두 조합론과 확률론의 기본 벽돌이다.

## 연습문제

**연습문제 1.** $m = 4$, $n = 6$, $k = 5$ 일 때 반데르몽드 항등식이 성립함을 확인하여라.

$$
\binom{10}{5} = \sum_{\ell=0}^{4} \binom{4}{\ell}\binom{6}{5-\ell}
$$

??? success "연습문제 1 풀이"

    $$
    \binom{4}{0}\binom{6}{5} + \binom{4}{1}\binom{6}{4} + \binom{4}{2}\binom{6}{3} + \binom{4}{3}\binom{6}{2} + \binom{4}{4}\binom{6}{1}
    $$

    $$
    = 1 \cdot 6 + 4 \cdot 15 + 6 \cdot 20 + 4 \cdot 15 + 1 \cdot 6 = 6 + 60 + 120 + 60 + 6 = 252
    $$

    그리고 $\binom{10}{5} = 252$ 이므로 항등식이 확인된다. $\square$

---

**연습문제 2.** 보통의 축구공(깎은 정이십면체)은 오각형 12개와 육각형 20개로 이루어져 있다.

**(a)** 오각형은 변이 5개, 육각형은 변이 6개이다. 두 번 세기를 이용하여 모서리의 총 개수를 구하여라.

**(b)** 각 꼭짓점에 면이 정확히 3개씩 모인다는 사실을 이용하여 꼭짓점의 개수를 구하여라.

??? success "연습문제 2 풀이"
    **(a)** 각 모서리는 정확히 두 면에 닿는다. 면마다 센 변의 총합은 $12 \times 5 + 20 \times 6 = 60 + 120 = 180$ 이다. 두 번 세기에 따라 모서리는 $E = 180 / 2 = 90$ 개이다.

    **(b)** 각 꼭짓점은 정확히 세 면이 함께 쓴다. 면마다 센 꼭짓점의 총합은 $12 \times 5 + 20 \times 6 = 180$ 이다. 꼭짓점마다 세 번씩 세어졌으므로 $V = 180 / 3 = 60$ 개이다.

    오일러 공식으로 확인하면 $V - E + F = 60 - 90 + 32 = 2$ 이다. $\square$
