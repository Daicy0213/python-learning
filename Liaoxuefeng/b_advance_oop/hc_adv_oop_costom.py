"""
定制类
"""


class Fib(object):
    # 初始化两个计数器a，b
    def __init__(self):
        self.a, self.b = 0, 1

    # 实例本身就是迭代对象，故返回自己
    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration
        return self.a

    # 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
    def __getitem__(self, item):

        # 如果要使用切片则需要做判断
        if isinstance(item, int):
            a, b = 1, 1
            for i in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            result = []
            for x in range(stop):
                if x >= start:
                    result.append(a)
                a, b = b, a + b
            return result


fib = Fib()
print("Fib num:")
for x in fib:
    print(x)

print("Fib[5]:%d" % fib[5])

# 也可以使用list的切片方法
print(fib[5:10])

"""
__call__()还可以定义参数。
对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。

那么，怎么判断一个变量是对象还是函数呢？
其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例

"""


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('Michael')
s()
print(callable(Student))
print(callable(max))
print(callable([1, 2]))
