# PythonLearning

## Python基础

### 数据类型

计算机顾名思义就是可以做数学计算的机器，因此，计算机程序理所当然地可以处理各种数值。但是，计算机能处理的远不止数值，还可以处理文本、图形、音频、视频、网页等各种各样的数据，不同的数据，需要定义不同的数据类型。在Python中，能够直接处理的数据类型有以下几种：



#### 整数

Python可以处理任意大小的整数，当然包括负整数，在程序中的表示方法和数学上的写法一模一样，例如：`1`，`100`，`-8080`，`0`，等等。

计算机由于使用二进制，所以，有时候用十六进制表示整数比较方便，十六进制用`0x`前缀和0-9，a-f表示，例如：`0xff00`，`0xa5b4c3d2`，等等。

对于很大的数，例如`10000000000`，很难数清楚0的个数。Python允许在数字中间以`_`分隔，因此，写成`10_000_000_000`和`10000000000`是完全一样的。十六进制数也可以写成`0xa1b2_c3d4`。



#### 浮点数

浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，比如，1.23x10<sup>9</sup>和12.3x10<sup>8</sup>是完全相等的。浮点数可以用数学写法，如`1.23`，`3.14`，`-9.01`，等等。但是对于很大或很小的浮点数，就必须用科学计数法表示，把10用e替代，1.23x10<sup>9</sup>就是`1.23e9`，或者`12.3e8`，0.000012可以写成`1.2e-5`，等等。

整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。



#### 字符串

字符串是以单引号`'`或双引号`"`括起来的任意文本，比如`'abc'`，`"xyz"`等等。请注意，`''`或`""`本身只是一种表示方式，不是字符串的一部分，因此，字符串`'abc'`只有`a`，`b`，`c`这3个字符。如果`'`本身也是一个字符，那就可以用`""`括起来，比如`"I'm OK"`包含的字符是`I`，`'`，`m`，空格，`O`，`K`这6个字符。

如果字符串内部既包含`'`又包含`"`怎么办？可以用转义字符`\`来标识，比如：

```
'I\'m \"OK\"!'
```

表示的字符串内容是：

```
I'm "OK"!
```

转义字符`\`可以转义很多字符，比如`\n`表示换行，`\t`表示制表符，字符`\`本身也要转义，所以`\\`表示的字符就是`\`，可以在Python的交互式命令行用`print()`打印字符串看看：

```
>>> print('I\'m ok.')
I'm ok.
>>> print('I\'m learning\nPython.')
I'm learning
Python.
>>> print('\\\n\\')
\
\
```

如果字符串里面有很多字符都需要转义，就需要加很多`\`，为了简化，Python还允许用`r''`表示`''`内部的字符串默认不转义，可以自己试试：

```
>>> print('\\\t\\')
\       \
>>> print(r'\\\t\\')
\\\t\\
```

如果字符串内部有很多换行，用`\n`写在一行里不好阅读，为了简化，Python允许用`'''...'''`的格式表示多行内容，可以自己试试：

```
>>> print('''line1
... line2
... line3''')
line1
line2
line3
```

上面是在交互式命令行内输入，注意在输入多行内容时，提示符由`>>>`变为`...`，提示你可以接着上一行输入，注意`...`是提示符，不是代码的一部分：

多行字符串`'''...'''`还可以在前面加上`r`使用，请自行测试



### 常量

所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量：

```
PI = 3.14159265359
```

但事实上`PI`仍然是一个变量，Python根本没有任何机制保证`PI`不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量`PI`的值，也没人能拦住你。

最后解释一下整数的除法为什么也是精确的。在Python中，有两种除法，一种除法是`/`：

```
>>> 10 / 3
3.3333333333333335
```

`/`除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：

```
>>> 9 / 3
3.0
```

还有一种除法是`//`，称为地板除，两个整数的除法仍然是整数：

```
>>> 10 // 3
3
```

你没有看错，整数的地板除`//`永远是整数，即使除不尽。要做精确的除法，使用`/`就可以。

因为`//`除法只取结果的整数部分，所以Python还提供一个余数运算，可以得到两个整数相除的余数：

```
>>> 10 % 3
1
```

无论整数做`//`除法还是取余数，结果永远是整数，所以，整数运算结果永远是精确的。



## 面向对象(OOP)























## type() 和 metaclass

[python中的metaclass_进击的怒汉的博客-CSDN博客](https://blog.csdn.net/jiguanglong/article/details/93204314)

### 1. 一切皆对象

#### 1.1类也是对象

在大多数编程语言中，类就是一组用来描述如何生成一个对象的代码段，在Python中这一点仍然成立。但是，Python中的类还远不止如此。类同样也是一种对象。只要你使用关键字class，Python解释器在执行的时候就会创建一个对象。下面的代码段：

```python
class MyClass(object):
    pass
```

将在内存中创建一个对象，名字就是MyClass。这个对象（类）自身拥有创建对象（类实例）的能力，而这就是为什么它是一个类的原因。但是，它的本质仍然是一个对象，于是你可以对它做如下的操作： 

你可以将它赋值给一个变量， 你可以拷贝它， 你可以为它增加属性， 你可以将它作为函数参数进行传递。

> **在 python 中有两种对象：**
>
> - 类型（类，新的版本中类和类型是一样的）对象：可以被实例化和继承
> - 非类型（实例）对象：不可以被实例和继承
>
> **python 中一切皆为对象：**
>
> 在python里，`int`整形是对象，整数`2`也是对象，你定义的函数啊，类啊都是对象，你定义的变量也是对象。总之，你在python里能用到的都可以称之为对象。



> **前置知识**
>
> `__init__`函数并不是真正意义上的构造函数，`__init__`方法做的事情是在对象创建好之后初始化变量。真正创建实例的是`__new__`方法.
>
> `__new__`方法用于创建对象并返回对象，当返回对象时会自动调用`__init__`方法进行初始化。`__new__`方法是静态方法，而`__init__`是实例方法。
>
> 





#### 1.2 type和object

明白了python中一切皆对象之后，再了解一下python中对象之间的两种关系

> **面向对象体系中的两种关系：**
>
> - 父子关系：通常描述为“子类是一种父类”
> - 类型实例关系：这种关系存在于两个对象中，其中一个对象（实例）是另一个对象（类型）的具体实现。

python中万物皆对象，一个python对象可能拥有两个属性，`__class__` 和 `__bases__`，`__class__` 表示这个对象是谁创建的，`__bases__` 表示一个类的父类是谁们。__class__和type()函数效果一样。

```python
class MyClass:
    pass
 
MyClass.__class__
#Out: type
MyClass.__bases__
#Out: (object,)
int.__class__
#Out: type
int.__bases__
#Out: (object,)
object.__class__  #object是type的实例，object创建自type
#Out: type
object.__bases__  #object没有超类，它本身是所以对象的超类
#Out: ()
type.__class__    #type创建自本身
#Out: type
type.__bases__    #type继承自object，即object是type的超类
#Out: (object,)  
```

> - **type为对象的顶点，所有对象都创建自type。**
> - **object为类继承的顶点，所有类都继承自object。**



#### 1.3 元类、类、实例

- object是所有类的超类，而且type也是继承自object；所有对象创建自type，而且object也是type的实例。
- “type是object的类型，同时，object又是type的超类”，那到底是先有object还是先有type呢？这就像“先有鸡还是先有蛋问题”。
- object和type是python中的两个源对象，事实上，它们是互相依赖对方来定义，所以它们不能分开而论。
- 通过这两个源对象可以繁育出一堆对象：list、tuple、dict等。**元类就是这些类的类，这些类是元类的实例。**

```python
l1=list()
l1.__class__      #l是list的实例
#Out: list
list.__class__   #list是type的实例
#Out: type
 
l1.__bases__      #实例没有超类
#AttributeError: 'list' object has no attribute '__bases__'
list.__bases__   
#Out: (object,)
 
l2=[1,2,3]        #l1是利用"类型名()"的方式创建实例，l2是利用python内置类型创造实例，比l1的创建速度要快
```



### 2. Metaclass

#### 2.1 type--“造物的上帝”

就像str是用来创建字符串对象的类，int是用来创建整数对象的类，而type就是创建类对象的类。

类本身不过是一个名为 type 类的实例。在 Python的类型世界里，type这个类就是造物的上帝。

用户自定义类，只不过是type类的__call__运算符的重载。当我们定义一个类的语句结束时，

真正发生的情况，是 Python 调用 type 的__call__运算符。简单来说，当你定义一个类时，写成下面时：

```python
class MyClass:
  data = 1
```

Python 真正执行的是下面这段代码：

```python
class = type(classname, superclasses, attributedict)
```

这里等号右边的type(classname, superclasses, attributedict)，就是 type 的__call__运算符重载，它会进一步调用：

```python
type.__new__(typeclass, classname, superclasses, attributedict)
type.__init__(class, classname, superclasses, attributedict)
```

当然，这一切都可以通过代码验证，比如下面这段代码示例:

``` python
class MyClass:
    data = 1
    
instance = MyClass()
MyClass, instance
#Out: (__main__.MyClass, <__main__.MyClass at 0x4eac358>)
 
MyClass = type('MyClass', (), {'data': 1})
instance = MyClass()
MyClass, instance
#Out: (__main__.MyClass, <__main__.MyClass at 0x4f915c0>)
 
instance.data
#Out: 1
```

由此可见，正常的 MyClass 定义，和手工去调用 type运算符的结果是一样的。

#### 2.2 **metaclass属性**

metaclass 是 type 的子类，通过替换 type的__call__运算符重载机制，“超越变形”正常的类。

其实，理解了以上几点，我们就会明白，正是 Python 的类创建机制，给了 metaclass 大展身手的机会。

**一旦你把一个类型 MyClass 的 metaclass 设置成 MyMeta，MyClass 就不再由原生的 type创建，而是会调用 MyMeta 的call运算符重载。**

```python
class MyMeta(type):
    def __new__(cls, *args, **kwargs):
        print('===>MyMeta.__new__')
        print(cls.__name__)
        return super().__new__(cls, *args, **kwargs)
 
    def __init__(self, classname, superclasses, attributedict):
        super().__init__(classname, superclasses, attributedict)
        print('===>MyMeta.__init__')
        print(self.__name__)
        print(attributedict)
        print(self.tag)
 
    def __call__(self, *args, **kwargs):
        print('===>MyMeta.__call__')
        obj = self.__new__(self, *args, **kwargs)
        self.__init__(self, *args, **kwargs)
        return obj
 
    
class Foo(object, metaclass=MyMeta):
    tag = '!Foo'
 
    def __new__(cls, *args, **kwargs):
        print('===>Foo.__new__')
        return super().__new__(cls)
 
    def __init__(self, name):
        print('===>Foo.__init__')
        self.name = name
 
 
print('test start')
foo = Foo('test')
print('test end')
 
#输出
#===>MyMeta.__new__
#MyMeta
#===>MyMeta.__init__
#Foo
#{'tag': '!Foo', '__module__': '__main__', '__init__': <function Foo.__init__ at 0x00000000010F7950>, '__new__': <function Foo.__new__ at 0x00000000010F78C8>, '__qualname__': 'Foo'}
#!Foo
#test start
#===>MyMeta.__call__
#===>Foo.__new__
#===>Foo.__init__
#test end
```

在创建Foo类的时候，python做了如下操作。 

1. Foo中有metaclass这个属性吗？如果是，Python会在内存中通过metaclass创建一个名字为Foo的类对象（我说的是类对象，请紧跟我的思路）。
2. 如果Python没有找到metaclass，它会继续在父类中寻找metaclass属性，并尝试做和前面同样的操作。
3. 如果Python在任何父类中都找不到metaclass，它就会在模块层次中去寻找metaclass，并尝试做同样的操作。
4. 如果还是找不到metaclass,Python就会用内置的type来创建这个类对象。

现在的问题就是，你可以在metaclass中放置些什么代码呢？
答案就是：可以创建一个类的东西。那么什么可以用来创建一个类呢？type，或者任何使用到type或者子类化type的东西都可以。用类实现可以（比如上面这个例子），用函数实现也可以。但是metaclass必须返回一个类。

```python
def MyMetaFunction(classname, superclasses, attributedict):
    attributedict['year'] = 2019
    return type(classname, superclasses, attributedict)
 
 
class Foo(object, metaclass=MyMetaFunction):
    tag = '!Foo'
 
    def __new__(cls, *args, **kwargs):
        print('===>Foo.__new__')
        return super().__new__(cls)
 
    def __init__(self, name):
        print('===>Foo.__init__')
        self.name = name
 
 
print('test start')
foo = Foo('test')
print('name:%s,tag:%s,year:%s' % (foo.name, foo.tag, foo.year))
print('test end')
 
#输出
#test start
#===>Foo.__new__
#===>Foo.__init__
#name:test,tag:!Foo,year:2019
#test end
```

> **把上面的例子运行完之后就会明白很多了，正常情况下我们在父类中是不能对子类的属性进行操作，但是元类可以。换种方式理解：元类、装饰器、类装饰器都可以归为元编程(引用自 python-cook-book 中的一句话)。** 

### 3. 应用

#### 3.1 实现ORM

我们通过创建一个类似Django中的ORM来熟悉一下元类的使用，通过元类用来创建API是非常好的选择，使用元类的编写很复杂但使用者可以非常简洁的调用API

```python
#一、首先定义Field类，它负责保存数据库表的字段名和字段类型
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.colmun_type = column_type
 
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
 
class StringField(Field):
    def __init__(self, name):
        super().__init__(name, 'varchar(100)')
 
class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, 'bigint')
 
#二、定义元类，控制Model对象的创建
class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return super().__new__(cls, name, bases, attrs)
        mappings = dict()
        for k,v in attrs.items():
            #保持类属性和列的映射关系到mappings字典
            if isinstance(v,Field):
                print('Found mapping:%s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.keys(): #将类属性移除，是定义的类字段不污染User类属性，只在实例中可以访问这些key
            attrs.pop(k)
        attrs['__table__'] = name.lower()  #假设表名为类名的小写，创建类时添加一个__table__属性
        attrs['__mappings__'] = mappings #保持属性和列的关系映射，创建类时添加一个__mappings__属性
        return super().__new__(cls, name, bases, attrs)
 
#三、Model基类
class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value
 
    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__,','.join(fields),','.join(params))
        print('SQL:%s' % sql)
        print('ARGS:%s' % str(args))
 
#我们想创建类似Django的ORM，只要定义字段就可以实现对数据库表和字段的操作
#最后、我们使用定义好的ORM接口，使用起来非常简单
class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
 
user = User(id=1,name='Job',email='job@test.com',password='pw')
user.save()
 
#输出
#Found mapping:password==><StringField:password>
#Found mapping:id==><IntegerField:id>
#Found mapping:email==><StringField:email>
#Found mapping:name==><StringField:username>
#SQL:insert into user (email,id,password,username) values (?,?,?,?)
#ARGS:['job@test.com', 1, 'pw', 'Job']
```

#### 3.2 单例

依照Python官方文档的说法，__new__方法主要是当你继承一些不可变的class时(比如int, str, tuple)， 提供给你一个自定义这些类的实例化过程的途径。还有就是实现自定义的metaclass。

简单来说，单例模式的原理就是通过在类属性中添加一个单例判定位ins_flag，通过这个flag判断是否已经被实例化过了,如果被实例化过了就返回该实例。

##### 1）、__new__方法实现单例

```python
 class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):     #_instance是类(Singleton)对象的一个属性
            cls._instance= super().__new__(cls, *args, **kwargs)
        return cls._instance #类的__new__方法之后，必须生成本类的实例(注意是“本类”的实例)才能自动调用本类的__init__方法进行初始化，否则不会自动调用__init__
 
class SubSingleton(Singleton):
    pass
 
 
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)
 
ss1 = SubSingleton()
ss2 = SubSingleton()
print(ss1 is ss2)
 
#输出
#True
#True
```

因为重写`__new__`方法，所以继承至Singleton的类，在不重写`__new__`的情况下都将是单例模式。 `_instance`（单下划线开头）属性换成`__instance`（双下划线开头）会得到不一样的结果，将无法实现单例模式，如果`__instance`（双下划线开头）属性就变成了私有的(其实变成了_Singleton__instance)。

##### 2）、元类实现单例

```python
class SingletonMeta(type):
    def __init__(self,*args,**kwargs):
        self.__instance = None    #这是一个私有属性来保存属性，而不会污染Singleton类（其实还是会污染，只是无法直接通过__instance属性访问）
        super().__init__(*args,**kwargs)
        
    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
        return self.__instance
 
 
class Singleton(metaclass=SingletonMeta): #在代码执行到这里的时候，元类中的__new__方法和__init__方法其实已经被执行了，而不是在Singleton实例化的时候执行。且仅会执行一次。
    pass
 
 
class SubSingleton(metaclass=SingletonMeta):
    pass
 
 
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)
 
ss1 = SubSingleton()
ss2 = SubSingleton()
print(ss1 is ss2)
 
#输出
#True
#True
```

> - 我们知道元类(SingletonMeta)生成的实例是一个类(Singleton),而这里我们仅仅需要对这个实例(Singleton)增加一个属性(__instance)来判断和保存生成的单例。想想也知道为一个类添加一个属性当然是在__init__中实现了。
> - 关于`__call__`方法的调用，因为Singleton是SingletonMeta的一个实例。所以Singleton()这样的方式就调用了SingletonMeta的`__call__`方法。

#### 3.3 动态加载

[YAML](https://so.csdn.net/so/search?q=YAML&spm=1001.2101.3001.7020)是一个家喻户晓的 Python 工具，可以方便地序列化 / 逆序列化结构数据。YAMLObject 的一个超越变形能力，就是它的任意子类支持序列化和反序列化（serialization & deserialization）。比如说下面这段代码（https://pyyaml.org/wiki/PyYAMLDocumentation）：

```python
class Monster(yaml.YAMLObject):
  yaml_tag = u'!Monster'
  def __init__(self, name, hp, ac, attacks):
    self.name = name
    self.hp = hp
    self.ac = ac
    self.attacks = attacks
  def __repr__(self):
    return "%s(name=%r, hp=%r, ac=%r, attacks=%r)" % (
       self.__class__.__name__, self.name, self.hp, self.ac,      
       self.attacks)
 
yaml.load("""
--- !Monster
name: Cave spider
hp: [2,6]    # 2d6
ac: 16
attacks: [BITE, HURT]
""")
 
Monster(name='Cave spider', hp=[2, 6], ac=16, attacks=['BITE', 'HURT'])
 
print yaml.dump(Monster(
    name='Cave lizard', hp=[3,6], ac=16, attacks=['BITE','HURT']))
 
# 输出
!Monster
ac: 16
attacks: [BITE, HURT]
hp: [3, 6]
name: Cave lizard
```

这里 YAMLObject 的特异功能体现在哪里呢？

你看，调用统一的 yaml.load()，就能把任意一个 yaml 序列载入成一个 Python Object；而调用统一的 yaml.dump()，就能把一个 YAMLObject 子类序列化。对于 load() 和 dump() 的使用者来说，他们完全不需要提前知道任何类型信息，这让超动态配置编程成了可能。听大神说在他的实战经验中，许多大型项目都需要应用这种超动态配置的理念。

比方说，在一个智能语音助手的大型项目中，我们有 1 万个语音对话场景，每一个场景都是不同团队开发的。作为智能语音助手的核心团队成员，我不可能去了解每个子场景的实现细节。

在动态配置实验不同场景时，经常是今天我要实验场景 A 和 B 的配置，明天实验 B 和 C 的配置，光配置文件就有几万行量级，工作量不可谓不小。而应用这样的动态配置理念，我就可以让引擎根据我的文本配置文件，动态加载所需要的 Python 类。

对于 YAML 的使用者，这一点也很方便，你只要简单地继承 yaml.YAMLObject，就能让你的 Python Object 具有序列化和逆序列化能力。是不是相比普通 Python 类，有一点“变态”，有一点“超越”？

YAML 的这种动态序列化 / 逆序列化功能正是用metaclass 实现的。

我们这里只看 YAMLObject 的 load() 功能。简单来说，我们需要一个全局的注册器，让 YAML 知道，序列化文本中的 !Monster 需要载入成 Monster 这个 Python 类型。

一个很自然的想法就是，那我们建立一个全局变量叫 registry，把所有需要逆序列化的 YAMLObject，都注册进去。比如下面这样：

```python
registry = {}

def add_constructor(target_class):
    registry[target_class.yaml_tag] = target_class
```

 然后，在 Monster 类定义后面加上下面这行代码：

```python
add_constructor(Monster)
```

 但这样的缺点也很明显，对于 YAML 的使用者来说，每一个 YAML 的可逆序列化的类 Foo 定义后，都需要加上一句话，add_constructor(Foo)。这无疑给开发者增加了麻烦，也更容易出错，毕竟开发者很容易忘了这一点。

那么，更优的实现方式是什么样呢？如果你看过 YAML 的源码，就会发现，正是 metaclass 解决了这个问题。

```python
# Python 2/3 相同部分
class YAMLObjectMetaclass(type):
  def __init__(cls, name, bases, kwds):
    super(YAMLObjectMetaclass, cls).__init__(name, bases, kwds)
    if 'yaml_tag' in kwds and kwds['yaml_tag'] is not None:
      cls.yaml_loader.add_constructor(cls.yaml_tag, cls.from_yaml)
  # 省略其余定义
 
# Python 3
class YAMLObject(metaclass=YAMLObjectMetaclass):
  yaml_loader = Loader
  # 省略其余定义
 
# Python 2
class YAMLObject(object):
  __metaclass__ = YAMLObjectMetaclass
  yaml_loader = Loader
  # 省略其余定义
```

你可以发现，YAMLObject 把 metaclass 都声明成了YAMLObjectMetaclass，利用 YAMLObjectMetaclass 的__init__方法，为所有 YAMLObject 子类偷偷执行add_constructor()。在 YAMLObjectMetaclass 中，下面这行代码就是魔法发生的地方：

```python
cls.yaml_loader.add_constructor(cls.yaml_tag, cls.from_yaml) 
```

YAML 应用 metaclass，拦截了所有 YAMLObject 子类的定义。也就说说，在你定义任何 YAMLObject 子类时，Python 会强行插入运行下面这段代码，把我们之前想要的add_constructor(Foo)给自动加上。

```python
cls.yaml_loader.add_constructor(cls.yaml_tag, cls.from_yaml)
```

所以 YAML 的使用者，无需自己去手写add_constructor(Foo) 。怎么样，是不是其实并不复杂？

### 4.总结

正常情况下我们在父类中是不能对子类的属性进行操作，但是元类可以，这就使得程序代码的维护变得困难。metaclass 是 Python 的黑魔法之一，在掌握它之前不要轻易尝试。感觉上python的规范原则很松，但这也使得python更灵活，对代码的编写理应由程序员自己负责，自己写的代码还是得自己负责啊。

**元类、装饰器、类装饰器都可以归为元编程，它们之间有一些相似点，还是在实际的应用中选择比较，使用合适的工具进行编程吧。**