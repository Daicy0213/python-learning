"""
获取对象信息
"""
import types

"""
types中的常量 以及 type()函数的用法
"""


def fn():
    pass


print("Is type fn is Functional Type: ", type(fn) == types.FunctionType)
print("Is type fn abs is BuiltinMethod Type: ", type(abs) == types.BuiltinMethodType)
print('Is type lambda is Lambda Type', type(lambda x: x) == types.LambdaType)
print(types.GeneratorType)

"""
isinstance()函数的用法
"""
print(isinstance(b'a', bytes))
print(isinstance(u'a', bytes))

# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

"""
dir()函数的用法
如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
"""
print('print \'abc\'\'s all method and attribute:\n', dir('abc'))

"""
类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
"""