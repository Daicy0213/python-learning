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
# 使用[*变量]的方式就是表示可以传入任意多个参数, 本质上是将这些参数打包为一个元组
def calc(*nums):
    sum_value = 0
    for n in nums:
        sum_value = sum_value + power(n)
    return sum_value

# 本质上传入的参数是一个元组 nums = (1, 2, 3)
print(calc(1, 2, 3))
# 也可以把list作为可变参数传入
ns = [1, 2, 3, 4]
print(calc(*ns))


# 关键字参数 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def print_person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


extra = {'city': 'Beijing', 'job': 'Engineer'}
print_person('Kobe', 40, **extra)


# 递归函数 求阶乘
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(10))


"""汉诺塔问题(hanoi)
我们需要将柱子a上的圆盘移动到柱子c上, 其中圆盘数量为n, 且要求:
1. 每次只能移动柱子最顶端的一个圆盘；
2. 每个柱子上，小圆盘永远要位于大圆盘之上；

我们将a柱定义为起始柱, b柱定义为辅助柱, c柱定义为目标柱。

实际上, 解决汉诺塔问题是有规律可循的：
当起始柱上只有 1 个圆盘时，我们可以很轻易地将它移动到目标柱上；
当起始柱上有 2 个圆盘时，移动过程是：先将起始柱上的 1 个圆盘移动到辅助柱上，
    然后将起始柱上遗留的圆盘移动到目标柱上，
    最后将辅助柱上的圆盘移动到目标柱上。
当起始柱上有 3 个圆盘时，移动过程和 2 个圆盘的情况类似：先将起始柱上的 2 个圆盘移动到辅助柱上，
    然后将起始柱上遗留的圆盘移动到目标柱上，
    最后将辅助柱上的圆盘移动到目标柱上。
"""
def move(n, a, b, c):
    if n == 1:
        print(a, '----->', c)
    else:
        move(n - 1, a, c, b)  # 将前n-1个圆盘移动到辅助柱子上
        move(1, a, b, c)  # 将起始柱上的最后一个圆盘移动到目标柱上
        move(n - 1, b, a, c) # 将辅助柱上的n-1个圆盘移动到目标柱上


print("汉诺塔问题")
move(3, 'A', 'B', 'C')
