# 합에 대한 기댓값의 선형성

## 되짚어 보기

7장에서 확률론에서 가장 강력한 도구인 **기댓값의 선형성**을 세웠다. 이 절에서는 그것을 확률변수의 합에 적용하는 데 초점을 맞추고, 뒤이어 나올 분산 공식들을 위한 발판을 마련한다.

!!! info "기댓값의 선형성"
    **임의의** 확률변수 $X_1, X_2, \ldots, X_n$ (서로 독립일 필요가 없다)과 상수 $a_1, \ldots, a_n$ 에 대하여 다음이 성립한다.

    $$
    E\left[\sum_{i=1}^n a_i X_i\right] = \sum_{i=1}^n a_i\,E[X_i]
    $$

여기서 열쇠가 되는 말은 **임의의**이다. 결합분포에 대해서는 아무런 가정도 필요하지 않다.

---

## 표본평균

$X_1, \ldots, X_n$ 을 공통의 평균 $\mu = E[X_i]$ 를 갖는 확률변수(i.i.d.일 필요는 없다)라 하자. 표본평균은 다음과 같다.

$$
\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i
$$

선형성에 따라 다음을 얻는다.

$$
E[\bar{X}_n] = \frac{1}{n}\sum_{i=1}^n E[X_i] = \frac{1}{n}(n\mu) = \mu
$$

표본평균은 종속 여부와 상관없이 모평균의 **불편**추정량이다.

---

## 예제

### 대칭 확률보행

$S_n = X_1 + X_2 + \cdots + X_n$ 이라 하자. 여기서 각 $X_i$ 는 같은 확률로 $+1$ 또는 $-1$ 의 값을 갖는다. 걸음들은 서로 종속일 수도 있다(예를 들어 증분들이 상관되어 있는 경우). 그래도 다음이 성립한다.

$$
E[S_n] = \sum_{i=1}^n E[X_i] = n \cdot 0 = 0
$$

### 가중 포트폴리오 수익률

어떤 포트폴리오의 가중치가 $w_1, \ldots, w_n$ 이고 $\sum w_i = 1$ 이라 하자. 자산 $i$ 의 기대수익률이 $\mu_i$ 라면 포트폴리오의 기대수익률은 다음과 같다.

$$
E[R_p] = E\left[\sum_{i=1}^n w_i R_i\right] = \sum_{i=1}^n w_i \mu_i
$$

이는 자산 수익률들이 서로 상관되어 있든 없든 성립한다.

### 고정점의 개수 (완전순열 다시 보기)

$\{1, 2, \ldots, n\}$ 의 순열 하나를 균등하게 무작위로 고른다. $D$ 를 고정점의 개수라 하자. $D = \sum_{i=1}^n \mathbf{1}_{X_i = i}$ 로 적으면 선형성에 따라 다음을 얻는다.

$$
E[D] = \sum_{i=1}^n P(X_i = i) = n \cdot \frac{1}{n} = 1
$$

이 지시확률변수들은 서로 종속이지만(어떤 원소가 고정점임을 알면 다른 원소들에 대한 정보가 생긴다) 선형성은 아무 문제 없이 쓸 수 있다.

---

## 선형성이 주지 않는 것

!!! warning "분산은 선형이 아니다"
    $E\!\left[\sum X_i\right] = \sum E[X_i]$ 는 언제나 성립하지만, 일반적으로 다음은 성립하지 않는다.

    $$
    \text{Var}\!\left(\sum_{i=1}^n X_i\right) \neq \sum_{i=1}^n \text{Var}(X_i)
    $$

    올바른 공식에는 공분산 항이 들어간다(9.3절). 공분산이 그토록 중요한 까닭이 바로 여기에 있다. 공분산은 합의 분산에서 생겨나는 여분의 항을 붙잡아 준다.

---

## 파이썬으로 확인하기

```python
import numpy as np

np.random.seed(42)
N = 500_000

# n=100 걸음의 확률보행 (걸음들이 상관되어 있어도 마찬가지)
n = 100
E_walk = 0  # 각 걸음의 평균은 0이다

# 몬테카를로: i.i.d. 걸음
walks = np.cumsum(np.random.choice([-1, 1], size=(N, n)), axis=1)
mc_mean = np.mean(walks[:, -1])
print(f"E[S_{n}] theory = {E_walk}")
print(f"E[S_{n}] Monte Carlo = {mc_mean:.4f}")

# 무작위 순열에서의 고정점
fixed_points = []
for _ in range(N):
    perm = np.random.permutation(n)
    fixed = np.sum(perm == np.arange(n))
    fixed_points.append(fixed)
print(f"\nE[fixed points] theory = 1")
print(f"E[fixed points] MC = {np.mean(fixed_points):.4f}")
```

## 연습문제

**연습문제 1.** 어떤 반의 $n = 25$ 명이 각자 독립적으로 일주일 가운데 가장 좋아하는 요일 하나를 (7일 위에 균등하게) 고른다. $S$ 를 가장 좋아하는 요일이 같은 학생 짝의 개수라 하자. 기댓값의 선형성을 써서 $E[S]$ 를 구하여라.

??? success "연습문제 1 풀이"
    순서를 따지지 않는 $\binom{25}{2} = 300$ 개의 짝 $(i, j)$ 각각에 대하여, 학생 $i$ 와 $j$ 가 좋아하는 요일이 같으면 $I_{ij} = 1$, 아니면 $0$ 이라 두자. 그러면 $E[I_{ij}] = 1/7$ 이므로 선형성에 따라 다음을 얻는다.

    $$
    E[S] = \binom{25}{2} \cdot \frac{1}{7} = \frac{300}{7} \approx 42.86
    $$
