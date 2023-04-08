"""
为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数
"""
import time


class Student(object):

    def __init__(self):
        self._score = None

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


"""
以上的方法略显复杂, Python内置的@property装饰器就是负责把一个方法变成属性调用的(使用@property的方法可以直接作为该实体的属性)：
下面的birth是可读写属性，而因为没有@age.setter, 所以age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
"""


class StudentPro(object):
    def __init__(self):
        self._score = None
        self._birth = None

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        year = time.localtime(time.time())[0]
        return year - self._birth


print('------------time库------------')
t = time.gmtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", t))
localtime = time.localtime(time.time())
print(localtime)
print(localtime[0])

print('------------oop-readonly------------')
s = StudentPro()
# s = StudentPro # 注意这样写完全没有实体化对象, 而是作为一个类
# s.birth = int(input("Enter birth:"))
# s.score = int(input("Enter score:"))
s.birth = 2023
s.score = 100
try:
    s.age = 25
except AttributeError as e:
    print("无法设置私有变量age")

print(s.score)
print(s.age)

"""
练习
请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
"""


class Screen(object):
    def __init__(self):
        self._width = None
        self._height = None

    def __str__(self):
        return "Class Screen: %s x %s, resolution %s" % (self._width, self._height, self.resolution)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._height * self._width


screen = Screen()
screen.width = 1920
screen.height = 1080
print("{0} x {1} screen resolution is {2}".format(screen.width, screen.height, screen.resolution))
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
print(screen)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
