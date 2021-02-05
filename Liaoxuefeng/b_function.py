"""
函数
"""
import math

"""
一. 函数定义
"""


# 求数字的绝对值
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# my_abs("A")

# python中虽然看起来函数可以返回多个值, 但其实只是将返回值装入一个tuple中
# 例如如下函数表示一个物体在坐标系中的移动, x和y表示当前坐标, 沿着角度angle方向移动距离为step的一次位移, 返回值为移动后的坐标
def move(x, y, step, angle=0.0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


r = move(100, 100, 60, math.pi / 6)
print(r)


# 一元二次方程的求根函数
def quadratic(a, b, c):
    temp = math.sqrt(b ** 2 - 4 * a * c)
    r1 = (-b + temp) / (2 * a)
    r2 = (-b - temp) / (2 * a)
    return r1, r2


print(quadratic(1, -4, 4))

"""
二. 函数的参数
"""
