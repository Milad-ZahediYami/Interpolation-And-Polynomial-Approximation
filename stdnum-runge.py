from math import sqrt, sin, cos


def rung_kutta(f, x0, y0, h, n):
    vx = [0] * (n + 1)
    vy = [0] * (n + 1)
    vx[0] = x = x0
    vy[0] = y = y0
    for i in range(1, n + 1):
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        vx[i] = x = x0 + i * h
        vy[i] = y = y + (k1 + k2 + k2 + k3 + k3 + k4) / 6
    return vx, vy


def f1(x, y):
    return (1+x)/(1+y)


def f2(x, y):
    return (1/(x**2))*(sin(2*x)-2*x*y)

print("\nf1---\n")

vx, vy = rung_kutta(f1, 1, 2, 0.5, 2)
for x, y in list(zip(vx, vy)):
    print("%4.1f %10.5f %+12.4e" %
          (x, y, y - (sqrt(((x**2) + (2*x) + 6)) - 1)))

print("\nf2---\n")

vx, vy = rung_kutta(f2, 1, 2, 0.25, 4)
for x, y in list(zip(vx, vy)):
    print("%4.2f %10.5f %+12.4e" %
          (x, y, y - (((1/((2*x)**2))*(4 + cos(2) + cos(2*x))))))


# f1---

#  1.0    2.00000  +0.0000e+00
#  1.5    2.30478  -4.9320e-02
#  2.0    2.69751  -4.4147e-02

# f2---

# 1.00    2.00000  +2.0000e+00
# 1.25    1.40336  +9.5812e-01
# 1.50    1.01656  +7.2835e-01
# 1.75    0.73813  +5.2202e-01
# 2.00    0.52979  +3.4665e-01
