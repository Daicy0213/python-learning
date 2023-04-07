"""
在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
而被继承的class称为基类、父类或超类（Base class、Super class）。
"""


class Animal(object):
    def run(self):
        print('Animal is running...')

    def run_twice(self):
        self.run()
        self.run()


class Dog(Animal):
    # 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。
    # 这样，我们就获得了继承的另一个好处：多态。
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    pass


if __name__ == '__main__':
    dog = Dog()
    dog.run()
    print('--------run twice--------')
    # 可以直接调用父类的方法
    dog.run_twice()
