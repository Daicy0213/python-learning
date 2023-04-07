"""
对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
鸭子类型（duck typing）:是动态类型的一种风格，不是由继承特定的类或实现特定的接口，而是当前的方法和属性的集合决定，
鸭子类型中关注的不是对象的类型本身，而是他如何使用。
Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。
但是，许多对象，只要有read()方法，都被视为“file-like object“。
许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。
"""


class Disk:
    def read(self):
        print('disk read')
        self.write()

    def write(self):
        print('disk write')


class Text:
    def read(self):
        print('text read')
        self.write()

    def write(self):
        print('text write')


def duck_demo(obj):
    obj.read()


disk = Disk()
text = Text()

duck_demo(disk)
duck_demo(text)

"""
如上述所示，Disk和Text具有都实现了read()和write()方法,duck_demo()方法可以看做是一个通知型接口，由该函数确定调用对象的哪个方法

鸭子类型特点：
变量绑定的类型具有不确定性
函数可以接收任意类型的参数
调用方法时不检查提供的参数类型
调用是否成功由参数的方法和属性确定
调用不成功抛出错误
"""
