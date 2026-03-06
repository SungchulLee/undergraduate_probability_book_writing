# Random Points and the Unit Circle

## 100 Random Points in [0,1]^2

Generating random points uniformly in the unit square is straightforward: generate two independent $U(0,1)$ samples for the $x$- and $y$-coordinates.

**MATLAB:**

```matlab
clear all; close all; clc; rng('default')

n = 100;
x = rand(2, n);

plot(x(1,:), x(2,:), 'o')
```

**Python:**

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

n = 100
x = np.random.rand(2, n)

plt.figure()
plt.plot(x[0, :], x[1, :], 'o')
plt.xlabel('x'); plt.ylabel('y')
plt.title('100 random points in $[0,1]^2$')
plt.show()
```

The resulting scatter plot shows the characteristic appearance of uniformly distributed points — roughly evenly spread, but with natural random clustering and gaps.

## Points Inside the Unit Circle

A more interesting exercise: generate 100 uniform points on $[-1, 1]^2$ and classify them as inside or outside the unit circle $x^2 + y^2 = 1$.

**MATLAB:**

```matlab
clear all; close all; clc; rng('default')

n = 100;
x = 2*rand(2, n) - 1;

plot(x(1,:), x(2,:), 'o'); grid on; hold on

r2 = x(1,:).^2 + x(2,:).^2;
i = find(r2 <= 1);
plot(x(1,i), x(2,i), 'or')

xp = -1:0.01:1;
yp = sqrt(1 - xp.^2);
plot(xp, yp, '-r', xp, -yp, '-r')
```

**Python:**

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

n = 100
x = 2 * np.random.rand(2, n) - 1

r2 = x[0, :]**2 + x[1, :]**2
inside = r2 <= 1
outside = ~inside

plt.figure(figsize=(6, 6))
plt.plot(x[0, outside], x[1, outside], 'ob', label='Outside')
plt.plot(x[0, inside], x[1, inside], 'or', label='Inside')

theta = np.linspace(0, 2*np.pi, 200)
plt.plot(np.cos(theta), np.sin(theta), '-r')

plt.axis('equal'); plt.grid(True)
plt.title('Points inside the unit circle')
plt.legend()
plt.show()
```

## Connection to Monte Carlo Estimation of pi

The fraction of points falling inside the circle approximates the ratio of areas:

$$

\frac{\text{Area of circle}}{\text{Area of square}} = \frac{\pi \cdot 1^2}{(2)^2} = \frac{\pi}{4}

$$

Therefore, if $k$ out of $n$ points land inside the circle,

$$

\hat{\pi} = \frac{4k}{n}

$$

is a Monte Carlo estimate of $\pi$. By the Law of Large Numbers, $\hat{\pi} \to \pi$ as $n \to \infty$.
