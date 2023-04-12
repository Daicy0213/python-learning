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

    def __call__(self, *args, **kwargs):
        print("MyType call...")
        return super().__call__(*args, **kwargs)


class MyCls(object, metaclass=MyType):
    def __init__(self, name):
        print("MyCls init...")
        self.name = name


print("----------")
v1 = MyCls("Kobe")
print(v1)

"""
需要注意的是：
当MyCls的定义出现的时候，就已经调用了MyType中的new和init函数， 而不是等MyCls实例化之后才调用
而call函数则是在由MyCls()的时候被调用的,即MyCls在尝试实例化的时候创建的，可以利用这一特性，实现单例模式
另外还有一个大坑：
在元类中init和call函数中调用父类的函数（即super()），首个参数self可以省略
out:
MyType new...
MyType init...
----------
MyType call...
MyCls init...
<__main__.MyCls object at 0x105457dc0>
Kobe


"""
