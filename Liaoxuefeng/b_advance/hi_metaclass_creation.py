"""
The Creating Process of Object
__init__  __new__  __call__
"""


class MyClass:
    """
    __new__方法用于创建对象并返回对象，当返回对象时会自动调用__init__方法进行初始化。__new__方法是静态方法，而__init__是实例方法。
    """

    def __init__(self):
        print('MyCls init')

    def __new__(cls, *args, **kwargs):
        print("MyCls new")
        new_class = super().__new__(cls, *args, **kwargs)
        return new_class

    def __call__(self, *args, **kwargs):
        print("MyCls call")


my_class = MyClass()
my_class()  # 当使用 `对象()` 的形式时调用__call__方法
# out:
# MyCls new
# MyCls init
# MyCls call

"""
下面可以用以上的特性创建一个单例模式
"""


class Singleton(object):
    # 单例类中维护一个实例对象
    _instance = None

    # 当调用__new__创建对象时判断实例对象是否为空，如果为空则创建，如果不为空，则返回该单例类中维护的对象
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance


s1 = Singleton()
s2 = Singleton()
print(s1 is s2)

"""
下面可以实现一个工厂模式
"""


class Fruit(object):
    def __init__(self):
        pass

    def print_color(self):
        pass


class Apple(Fruit):
    def __init__(self):
        super().__init__()

    def print_color(self):
        print("apple is in red")


class Orange(Fruit):
    def __init__(self):
        super().__init__()

    def print_color(self):
        print("orange is in orange")


class FruitFactory(object):
    fruits = {"apple": Apple, "orange": Orange}

    def __new__(cls, name):
        if name in cls.fruits.keys():
            return cls.fruits[name]()
        else:
            return Fruit()


fruit1 = FruitFactory("apple")
fruit2 = FruitFactory("orange")
fruit1.print_color()
fruit2.print_color()
