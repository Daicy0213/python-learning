"""
面向对象编程(一)
类/实例/访问限制

class后面紧接着是类名，即student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
"""


class Student(object):
    """注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，
    就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
    但self不需要传，python解释器自己会把实例变量传进去
    """

    def __init__(self, name, score, sex):
        self.name = name
        self.score = score
        self.__sex = sex

    def print_score(self):
        print('%s : %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            print("A")
        elif self.score >= 60:
            print("B")
        else:
            print("C")

    def get_sex(self):
        if self.__sex == 0:
            return "male"
        else:
            return "female"

    def set_sex(self, sex):
        self.__sex = sex


if __name__ == '__main__':
    kobe = Student("kobe", 81, 0)
    michael = Student("michael", 63, 0)
    print(kobe.score)
    kobe.print_score()
    kobe.get_grade()
    michael.print_score()
    # 外部代码还是可以自由地修改一个实例的name、score属性
    michael.score = 90
    michael.print_score()
    """
    如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，
    就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们给Student类添加一个私有变量属性sex
    
    在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，
    所以，不能用__name__、__score__这样的变量名。

    有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，
    意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

    双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
    不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
    如：
    >>> kobe._Student__name
    'kobe'
    
    但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
    总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。
    另外，如下写法也是错误的，
    
    表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！
    内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。
    
    >>> kobe = Student('kobe', 81)
    >>> kobe.get_name()
    'kobe'
    
    >>> kobe.__name = 'New Name' # 设置__name变量！不通过set方法设置私有变量，表面成功了，但其实设置的是另一个变量
    >>> kobe.__name
    'New Name'
    >>> bart.get_name() # get_name()内部返回self.__name
    'Bart Simpson'
    """
    print(michael.get_sex())
