# 중복이 있는 순열

## 개요

대상 가운데 **똑같은** 것(중복된 것)이 섞여 있으면 서로 다른 배열의 수는 $n!$ 보다 적다. 똑같은 대상끼리 자리를 바꾸어도 새로운 배열이 되지 않기 때문이다. **여럿 대 하나** 원리를 쓰면 올바른 개수를 깔끔하게 유도할 수 있다.

## 여럿 대 하나 원리

여럿 대 하나 원리는 두 집합 사이의 대응을 만들어 세는 강력한 기법이다.

**일대일:** $f: A \to B$ 가 일대일대응이면 $|B| = |A|$ 이다.

**여럿 대 하나:** $f: A \to B$ 가 $k$ 대 $1$ 인 전사함수라면($B$ 의 모든 원소가 정확히 $k$ 개의 원상을 가진다면) 다음이 성립한다.

$$|A| : |B| = k : 1 \quad \Rightarrow \quad |B| = \frac{|A|}{k}$$

**하나 대 여럿:** $A$ 의 모든 원소가 $B$ 의 원소 $k$ 개로 대응되면 $|A| = k|B|$ 이다.

## 예 — BOB으로 만드는 낱말

**1단계: 번호를 붙인다.** 두 개의 B를 서로 다른 것으로 보아 $B_1 O B_2$ 라 하자.

$B_1 O B_2$ (모두 서로 다르다)를 늘어놓는 방법의 수는 $3! = 6$ 이다.

**2단계: 번호를 뗀다.** 모든 배열을 적어 놓고 무슨 일이 일어나는지 살펴보자.

| 번호가 있을 때 | 번호를 뗐을 때 |
|:---:|:---:|
| $B_1 B_2 O$ | $BBO$ |
| $B_1 O B_2$ | $BOB$ |
| $B_2 B_1 O$ | $BBO$ |
| $B_2 O B_1$ | $BOB$ |
| $O B_1 B_2$ | $OBB$ |
| $O B_2 B_1$ | $OBB$ |

**3단계: 여럿 대 하나 원리를 적용한다.** 번호를 뗀 낱말 하나마다 번호가 붙은 배열이 정확히 $2! = 2$ 개씩 대응된다(두 B의 자리를 맞바꿀 수 있으므로). 즉 **2 대 1** 대응이다.

$$\text{BOB으로 만드는 낱말의 수} = \frac{3!}{2!} = \frac{6}{2} = 3$$

서로 다른 세 낱말은 $BBO$, $BOB$, $OBB$ 이다.

## 예 — BBOOO로 만드는 낱말

**1단계: 번호를 붙인다.** 글자를 모두 서로 다른 것으로 보아 $B_1 B_2 O_1 O_2 O_3$ 라 하자.

배열의 수는 $5! = 120$ 이다.

**2단계: 번호를 뗀다.** 낱말 하나마다 두 B끼리 자리를 바꾸는 방법이 $2!$ 가지, 세 O끼리 자리를 바꾸는 방법이 $3!$ 가지 있다.

예를 들어 낱말 $BBOOO$ 에는 번호가 붙은 배열이 $2! \times 3! = 12$ 개 대응된다.

$B_1 B_2 O_1 O_2 O_3$, $B_1 B_2 O_1 O_3 O_2$, $B_1 B_2 O_2 O_1 O_3$, $B_1 B_2 O_2 O_3 O_1$, $B_1 B_2 O_3 O_1 O_2$, $B_1 B_2 O_3 O_2 O_1$, $B_2 B_1 O_1 O_2 O_3$, $B_2 B_1 O_1 O_3 O_2$, $B_2 B_1 O_2 O_1 O_3$, $B_2 B_1 O_2 O_3 O_1$, $B_2 B_1 O_3 O_1 O_2$, $B_2 B_1 O_3 O_2 O_1$

**3단계: 여럿 대 하나 원리를 적용한다.** 이는 $(2! \cdot 3!)$ 대 $1$ 대응이다.

$$\text{BBOOO로 만드는 낱말의 수} = \frac{5!}{2! \cdot 3!} = \frac{120}{2 \cdot 6} = 10$$

## 일반 공식 — 다항계수

$n$ 개의 대상 가운데 1종류가 $n_1$ 개, 2종류가 $n_2$ 개, …, $m$ 종류가 $n_m$ 개씩 있고 같은 종류끼리는 구별되지 않는다고 하자($n_1 + n_2 + \cdots + n_m = n$). 이때 서로 다른 배열의 수는 **다항계수**로 주어진다.

$$\binom{n}{n_1 \; n_2 \; \cdots \; n_m} = \frac{n!}{n_1! \cdot n_2! \cdots n_m!}$$

이는 여럿 대 하나 원리에서 나온다. 모든 대상이 서로 다르다고 보고 $n!$ 가지 배열에서 출발한 다음, 각 묶음 안에서 구별되지 않는 자리바꿈을 없애기 위해 계승들의 곱으로 나누는 것이다.

## 파이썬 구현

```python
from math import factorial
from itertools import permutations

def permutations_with_repetition(word):
    """
    같은 글자가 섞여 있는 낱말의 서로 다른 순열의 개수를 센다.
    다항계수 n! / (n1! * n2! * ... * nm!) 를 이용한다.
    
    매개변수
    ----------
    word : str
        글자를 늘어놓을 대상이 되는 낱말.
    
    반환값
    -------
    int
        서로 다른 배열의 개수.
    """
    n = len(word)
    from collections import Counter
    counts = Counter(word)
    denominator = 1
    for c in counts.values():
        denominator *= factorial(c)
    return factorial(n) // denominator

# 예: BOB
word = "BOB"
result = permutations_with_repetition(word)
print(f"Distinct permutations of '{word}': {result}")
# Output: Distinct permutations of 'BOB': 3

# 모두 늘어놓아 확인하기
distinct = set(permutations(word))
print(f"Verification: {len(distinct)}")
print(f"Words: {sorted([''.join(p) for p in distinct])}")
# Output: Words: ['BBO', 'BOB', 'OBB']

# 예: BBOOO
word = "BBOOO"
result = permutations_with_repetition(word)
print(f"\nDistinct permutations of '{word}': {result}")
# Output: Distinct permutations of 'BBOOO': 10

distinct = set(permutations(word))
print(f"Verification: {len(distinct)}")
print(f"Words: {sorted([''.join(p) for p in distinct])}")
```

## 핵심 정리

여럿 대 하나 원리는 어려운 세기 문제를 쉬운 문제로 바꾸어 준다. 먼저 모든 대상이 서로 다르다고 보고 세고($n!$), 똑같은 대상 때문에 생기는 "같은" 배열의 수로 나누면 된다. 다항계수가 바로 여기에서 나온다.

## 연습문제

**연습문제 1.** 단어 MISSISSIPPI의 글자로 만들 수 있는 서로 다른 배열은 몇 가지인가?

??? success "연습문제 1 풀이"
    MISSISSIPPI는 글자가 11개이며 M(1개), I(4개), S(4개), P(2개)로 이루어져 있다.

    $$
    \frac{11!}{1! \cdot 4! \cdot 4! \cdot 2!} = \frac{39{,}916{,}800}{1 \cdot 24 \cdot 24 \cdot 2} = 34{,}650
    $$
