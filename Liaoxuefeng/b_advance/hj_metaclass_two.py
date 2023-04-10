"""
关于元类的另一个例子
"""


class MyType(type):
    def __init__(self, *args, **kwargs):
        print("MyType init...")
        super(MyType, self).__init__(*args, **kwargs)

    def __new__(cls, *args, **kwargs):
        print("MyType new...")
        return super().__new__(cls, *args, **kwargs)

    # 通过call --> new --> init
    def __call__(self, *args, **kwargs):
        print("MyType call...")
        # 1.调用创建的类的 __new__ 方法去创建对象
        empty_obj = self.__new__(self)

        # 2.调用创建的类的 __init__ 方法去初始化
        self.__init__(empty_obj, *args, **kwargs)
        return empty_obj


class MyCls(object, metaclass=MyType):
    def __init__(self, name):
        print("MyCls init...")
        self.name = name


v1 = MyCls("Kobe")
print(v1)

"""
out:
MyType new...
MyType init...
MyType call...
MyCls init...
<__main__.MyCls object at 0x105457dc0>
Kobe


"""