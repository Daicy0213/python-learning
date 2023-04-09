from enum import Enum, unique

"""
枚举类
"""

# 定义枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
"""
value属性则是自动赋给成员的int常量，默认从1开始计数
Jan => Month.Jan , 1
Feb => Month.Feb , 2
....
"""


# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1)  # 结果 Weekday.Mon
print(Weekday.Tue.value)  # 结果 2
for name, member in Weekday.__members__.items():
    print(name, '=>', member)

"""
把Student的gender属性改造为枚举类型，可以避免使用字符串：
"""


@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
