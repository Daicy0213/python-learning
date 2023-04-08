"""
继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩展父类的功能。
回忆一下Animal类层次的设计，假设我们要实现以下4种动物：
Dog - 狗狗；
Bat - 蝙蝠；
Parrot - 鹦鹉；
Ostrich - 鸵鸟。
"""


class Animal(object):
    pass


# 现在，我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类：
class Runnable(object):
    """
    在Python中存在继承结构，对于父类而言可以获取所有的子类定义，通过“__init_subclass__()”特殊方法实现；
    """

    def __init_subclass__(cls, **kwargs):  # kwargs 可以在子类定义一些固定参数
        print("[子类初始化监听]cls=%s, kwargs=%s" % (cls, kwargs))

    """
    @classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，
    可以来调用类的属性，类的方法，实例化对象等。
    """

    @classmethod
    def run(cls):
        print('%s is Running...' % cls.__name__)


class Flyable(object):

    def __init_subclass__(cls, **kwargs):  # kwargs 可以在子类定义一些固定参数
        print("[子类初始化监听]cls=%s, kwargs=%s" % (cls, kwargs))

    @classmethod
    def fly(cls):
        print('%s is Flying...' % cls.__name__)


# 大类:
class Mammal(Animal):
    @classmethod
    def born(cls):
        print('%s born mammal' % cls.__name__)


class Bird(Animal):
    @classmethod
    def born(cls):
        print('%s born egg' % cls.__name__)


# 各种动物:
class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


class Parrot(Bird, Flyable):
    pass


class Ostrich(Bird, Runnable):
    pass


dog = Dog()
bat = Bat()
ostrich = Ostrich()
dog.run()
bat.fly()
ostrich.run()
dog.born()
bat.born()
ostrich.born()
