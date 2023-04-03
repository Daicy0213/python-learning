import math

"""
函数
一. 函数定义
"""


# 求数字的绝对值
def my_abs(x):
    # 如果x不是整型或浮点型则抛出异常
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


# 可以将函数赋值给一个变量
r = move(100, 100, 60, math.pi / 6)
print(r)


# 一元二次方程的求根函数 ax^2 + bx + c =0 求x的值
def quadratic(a, b, c):
    temp = math.sqrt(b ** 2 - 4 * a * c)
    r1 = (-b + temp) / (2 * a)
    r2 = (-b - temp) / (2 * a)
    return r1, r2


print(quadratic(1, -4, 4))

"""
二. 函数的参数
"""


# 求平方或n次方, 设置默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print('2的平方 %d' % power(2))
print('2的三次方 %d' % power(2, 3))


# 可变参数, 求a^2 + b^2 + c^2 + .....
def calc(*nums):
    sum_value = 0
    for n in nums:
        sum_value = sum_value + power(n)
    return sum_value


print(calc(1, 2, 3))


# 关键字参数
def print_person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


extra = {'city': 'Beijing', 'job': 'Engineer'}
print_person('Kobe', 40, **extra)
