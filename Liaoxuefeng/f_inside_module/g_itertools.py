"""itertools
Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
"""
import itertools
import time
import threading


# count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。
# 1
# 2
# 3
# .....
def count_infinity():
    naturals = itertools.count(1)
    for n in naturals:
        time.sleep(1)
        print(n)


thread = threading.Thread(target=count_infinity())
t
