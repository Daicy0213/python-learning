"""
关于在两个函数中加入and关键字的问题
return method1 and method2(arg)
等于：
return method2(arg)
"""
print(int and float('1'))


def fn():
    return False


def fn1(s):
    return True


print(fn and fn1('1'))
