from types import MethodType

"""
正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
"""


class Student(object):
    pass


"""
然后，尝试给实例绑定一个属性：
"""
s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性
print(s.name)  # Michael


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)  # 调用实例方法
print(s.age)  # 测试结果 25

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的

try:
    s2 = Student()  # 创建新的实例
    s2.set_age(25)  # 尝试调用方法
except AttributeError as e:
    print("无法调用set_age")
"""
为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
self.score = score
但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。
如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性，而不可以使用其他方法给实例增加其他属性。
为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
"""


class StudentCtrl(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = StudentCtrl()
s.name = 'Michael'
s.age = 25
try:
    s.score = 99
except AttributeError as a:
    print(a)
print(s.name)
print(s.age)
