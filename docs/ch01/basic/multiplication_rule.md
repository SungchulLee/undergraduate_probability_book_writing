# 곱셈 법칙

## 개요

**곱셈 법칙**(**세기의 원리** 또는 **곱의 법칙**이라고도 한다)은 조합론에서 가장 기본이 되는 도구이다. 어떤 절차를 차례로 이어지는 여러 단계로 쪼갤 수 있고, 각 단계에서 고를 수 있는 가짓수가 앞 단계에서 무엇을 골랐는지와 무관하다면, 전체 결과의 수는 각 단계의 가짓수를 모두 곱한 값이라는 것이다.

## 정리의 서술

어떤 실험이 차례로 이어지는 두 단계로 이루어져 있고,

- 1단계에서 일어날 수 있는 결과가 $m$ 가지
- 2단계에서 일어날 수 있는 결과가 $n$ 가지 (1단계의 결과가 무엇이든 상관없이)

라면, 이 둘을 합친 실험에서 일어날 수 있는 결과의 수는 다음과 같다.

$$m \times n$$

더 일반적으로, 실험이 차례로 이어지는 $k$ 개의 단계로 이루어져 있고 각 단계에서 일어날 수 있는 결과가 $n_1, n_2, \ldots, n_k$ 가지라면, 전체 결과의 수는 다음과 같다.

$$n_1 \times n_2 \times \cdots \times n_k$$

## 나무 그림으로 보는 뜻

곱셈 법칙은 **나무 그림**으로 볼 때 가장 자연스럽게 이해된다. 실험의 각 단계가 나무에서 가지가 갈라지는 한 층에 해당한다. 뿌리에서 잎까지 이르는 경로의 수가 곧 전체 가짓수이다.

### 예 — $A$ 에서 $C$ 까지 가는 경로의 수

중간 지점 $B$ 를 거쳐 $A$ 에서 $C$ 까지 가는 경로의 수를 세어 보자.

$$A \longrightarrow B \longrightarrow C$$

**$A$ 에서 $B$ 까지 가는 경로의 갈래:** $1$ 과 $2$ 로 이름 붙인 경로가 2개 있다고 하자.

**$B$ 에서 $C$ 까지 가는 경로의 갈래:** $a$, $b$, $c$ 로 이름 붙인 경로가 3개 있다고 하자.

나무 그림을 써서 $A$ 에서 $C$ 까지 가는 모든 경로를 늘어놓으면 다음과 같다.

| $A$ 에서 $B$ 까지의 경로 | $B$ 에서 $C$ 까지의 경로 | 이어 붙인 $A$ 에서 $C$ 까지의 경로 |
|:---:|:---:|:---:|
| 1 | $a$ | $1a$ |
| 1 | $b$ | $1b$ |
| 1 | $c$ | $1c$ |
| 2 | $a$ | $2a$ |
| 2 | $b$ | $2b$ |
| 2 | $c$ | $2c$ |

곱셈 법칙에 따라 다음을 얻는다.

$$A \text{ 에서 } C \text{ 까지 가는 경로의 수} = 2 \times 3 = 6$$

## 임원 뽑기 — 고전적인 응용

$n$ 명이 있고 이 가운데 **회장**, **부회장**, **총무**를 한 명씩 뽑는다고 하자(세 자리는 서로 다르다).

- **회장 뽑기:** $n$ 가지 (갈래의 수 $= n$)
- **부회장 뽑기:** $n - 1$ 가지 (갈래의 수 $= n - 1$)
- **총무 뽑기:** $n - 2$ 가지 (갈래의 수 $= n - 2$)

곱셈 법칙에 따라(나무 그림으로 보면) 다음을 얻는다.

$$\text{회장, 부회장, 총무를 뽑는 경우의 수} = n \times (n-1) \times (n-2)$$

이것이 바로 **순열**, 곧 순서를 따지는 뽑기이다. 뒤의 절에서 다룰 일반적인 순열 공식이 여기에서 출발한다.

## 파이썬 구현

```python
import itertools
from math import prod

def count_by_multiplication_rule(stage_counts):
    """
    곱셈 법칙을 적용한다.

    매개변수
    ----------
    stage_counts : list of int
        각 단계에서 고를 수 있는 가짓수.

    반환값
    -------
    int
        전체 결과의 수.
    """
    return prod(stage_counts)

# 예: A에서 C까지 가는 경로
paths_A_to_B = 2
paths_B_to_C = 3
total = count_by_multiplication_rule([paths_A_to_B, paths_B_to_C])
print(f"Number of paths from A to C: {total}")
# Output: Number of paths from A to C: 6

# 예: 10명 가운데 회장, 부회장, 총무 뽑기
n = 10
officers = count_by_multiplication_rule([n, n-1, n-2])
print(f"Number of ways to choose 3 officers from {n} people: {officers}")
# Output: Number of ways to choose 3 officers from 10 people: 720

# 모두 늘어놓아 확인하기
people = list(range(1, n+1))
ordered_triples = list(itertools.permutations(people, 3))
print(f"Verification by enumeration: {len(ordered_triples)}")
# Output: Verification by enumeration: 720
```

## 핵심 정리

곱셈 법칙은 복잡한 세기 문제를 더 단순한 세기 문제들의 이어짐으로 바꾸어 준다. 나무 그림은 눈으로 보는 증명이자 빠짐없이 늘어놓는 방법이기도 하다. 잎의 개수가 각 층에서 갈라지는 가짓수의 곱과 같기 때문이다.

## 연습문제

**연습문제 1.** 자동차 번호판이 알파벳 3개 뒤에 숫자 4개가 오는 꼴이라고 하자. 다음 각 경우에 서로 다른 번호판은 몇 개나 만들 수 있는가?

**(a)** 같은 글자나 숫자를 여러 번 써도 되는 경우

**(b)** 알파벳과 숫자를 모두 중복 없이 써야 하는 경우

??? success "연습문제 1 풀이"
    **(a)** $26^3 \times 10^4 = 175{,}760{,}000$

    **(b)** $26 \times 25 \times 24 \times 10 \times 9 \times 8 \times 7 = 78{,}624{,}000$
