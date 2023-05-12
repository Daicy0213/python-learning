"""Type Hint 类型注释
 Type hints is a syntax introduced in Python 3.5 and above, which allows developers to specify type
 information in function parameters and return values to improve code readability, maintainability
 and stability.
 Type hint是Python 3.5版本及以上引入的一种语法，它允许开发人员在函数参数和返回值中指定类型信息，以提高代码的可读性、可维
 护性和稳定性。
 详情页: https://zhuanlan.zhihu.com/p/419955374
"""
from typing import List, Dict, Tuple
from collections.abc import Sequence as Seq

# 表示定义一个age变量, 其类型为int
age: int = 20


# name:str 表示这个函数参数的类型应该是字符串类型
# -> str代表这个函数的返回类型也应该是字符串类型
def greet(name: str) -> str:
    return "Hello, " + name


# 如果一个函数带有默认参数, 那么可以使用如下的写法
def add(first: int = 10, second: float = 5.5) -> float:
    return first + second


# 如果函数没有返回值
def return_none() -> None:
    pass


# 自定义一个Person对象
class Person:
    def __init__(self, name: str):
        self.name = name


def hello(p: Person) -> str:
    return f'Hello, {p.name}'


"""容器类型
# 参数1: 元素为 int 的列表
# 参数2: 键为字符串，值为 int 的字典
# 返回值: 包含两个元素的元组
"""


def mix(scores: List[int], ages: Dict[str, int]) -> Tuple[int, int]:
    return 0, 0


# 如果用的是 Python 3.9+ 版本，甚至连 typing 模块都不需要了，内置的容器类型就支持了复合注解：
def mix(scores: list[int], ages: dict[str, int]) -> tuple[int, int]:
    return 0, 0


"""
在某些情况下，不需要严格区分参数到底是列表还是元组（这种情况还蛮多的）。
这时候就可以将它们的特征抽象为更泛化的类型（泛型），比如 Sequence（序列）。
Python 3.8 之前的版本
from typing import Sequence as Seq1

def foo(seq: Seq1[str]):
    for item in seq:
        print(item)
Python 3.9+ 也可以这么写:
"""


def abstract_seq(seq: Seq[str]):
    for item in seq:
        print(item)


"""类型别名
有时候对象的类型可能会非常复杂，或者你希望给类型赋予一个有意义的名称，那么你可以这样定义类型的别名：
"""
from typing import Tuple

# 类型别名
Vector2D = Tuple[int, int]


def v2(vector: Vector2D):
    print(vector)


v2(vector=(1, 2))
# Output: (1, 2)


"""NewType
与类型别名有点类似的，是用 NewType 创建自定义类型：
"""
from typing import NewType

# 创建新类型 NewType(name, tp), 创建的类被认为是tp的子类
Vector3D = NewType('Vector3D', tuple[int, int, int])


def v3(vector: Vector3D):
    print(vector)


# 乍一眼看起来与前面的类型别名功能差不多，但不同的是 NewType 创建了原始类型的“子类”：

# 类型检查成功
# 类型别名和原始类型是等价的
v2(vector=(1, 2))

# 类型检查失败
# NewType创建的是原始类型的“子类”
v3(vector=(1, 2, 3))

# 类型检查成功
# 传入参数必须是 Vector3D 的“实例”
v_3d = Vector3D((4, 5, 6))
v3(vector=v_3d)

"""泛型
假设有一个函数，要求它既能够处理字符串，又能够处理数字。那么你可能很自然地想到了 Union 。
这样写有个很大的弊端，就是参数的类型可以混着用（比如 a: int 且 b:str ），即便你并不想具有这样的特性。看下面这个就明白了：
"""
from typing import Union

U = Union[str, int]


def union_str_int(a: U, b: U) -> List[U]:
    return [a, b]


# 通过
union_str_int('Joe', 19)

# 通过
union_str_int(19, 21)

# 通过
union_str_int('Joe', 'David')

"""
如果我们想要函数的第一个参数和第二个参数的类型是一致的, 但是它们既可以是int也可以是str
那么就可以使用泛型
"""
from typing import TypeVar

# 定义泛型 T
# T 必须是 str 或 int 其中一种
T = TypeVar('T', str, int)


def str_or_int(a: T, b: T) -> List[T]:
    return [a, b]


# 类型检查不通过
# 函数的参数必须为同一个类型"T"
str_or_int('Joe', 19)

# 通过
str_or_int(19, 21)

# 通过
str_or_int('Joe', 'David')
