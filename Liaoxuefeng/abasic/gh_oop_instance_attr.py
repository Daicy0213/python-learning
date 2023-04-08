"""
实例属性和类属性

但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：
"""


# 给实例绑定属性的方法是通过实例变量，或者通过self变量：

class Student(object):
    def __init__(self, name):
        self.name = name


s = Student('Bob')
s.score = 90


# 但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：
# 当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。
class StudentClassName(object):
    name = 'Student'


s = StudentClassName()  # 创建实例s
# 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(s.name)  # 结果Student
print(StudentClassName.name)  # 打印类的name属性 结果Student
s.name = 'Michael'  # 给实例绑定name属性
print(s.name)  # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性 结果Michael
print(StudentClassName.name)  # 但是类属性并未消失，用Student.name仍然可以访问 结果Student
del s.name  # 如果删除实例的name属性
print(s.name)  # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了 结果Student


# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加
class StudentCount(object):
    count = 0

    def __init__(self, name):
        self.name = name
        StudentCount.count = StudentCount.count + 1


if StudentCount.count != 0:
    print('测试失败!')
else:
    bart = StudentCount('Bart')
    if StudentCount.count != 1:
        print('测试失败!')
    else:
        lisa = StudentCount('Bart')
        if StudentCount.count != 2:
            StudentCount('测试失败!')
        else:
            print('Students:', StudentCount.count)
            print('测试通过!')
