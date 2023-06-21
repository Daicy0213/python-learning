"""timeit模块
timeit是Python标准库内置的小工具，可以快速测试小段代码的性能。
timeit 函数：
timeit.timeit(stmt, setup,timer, number)
stmt: statement的缩写，你要测试的代码或者语句，纯文本，默认值是 "pass"
setup: 在运行stmt前的配置语句，纯文本，默认值也是 "pass"
timer: 计时器，一般忽略这个参数
number: stmt执行的次数，默认是1000000，一百万

注意区别jupyter中的 %timeit
%timeit 是 IPython 提供的一个魔术命令，用于测量代码的执行时间。
%timeit -r 5 -n 400 func(args) 表示对函数func(args)运行5次循环, 每次循环执行400次, 最后对所有计时结果取平均得到运行一遍代码的时间。
结果大致格式如下
705 µs ± 60.1 µs per loop (mean ± std. dev. of 5 runs, 400 loops each)
"""
import timeit
import random
import arrow  # 是一个用于处理日期和时间的强大 Python 第三方库


# 本地函数
def stupid1():
    return random.randint(1, 10)


# 依赖其他函数
def stupid2():
    return stupid1()


# 依赖其他包或者模块
def stupid3():
    return arrow.now()


print(timeit.timeit('stupid1()', setup='from __main__ import stupid1'))
print(timeit.timeit('stupid2()', setup='from __main__ import stupid2'))
print(timeit.timeit('stupid3()', setup='from __main__ import stupid3', number=100))
