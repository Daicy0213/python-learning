# https://networkx.org/documentation/stable/tutorial.html
import networkx as nx

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_nodes_from([
    (4, {"color": "red"}),
    (5, {"color": "green"}),
])

# nodes from one graph can be incorporated into another

H = nx.path_graph(10)
G.add_nodes_from(H)
print(G.nodes)
print(G.edges)

# G.add_edge(1,2)
# G.add_node(H)


print("-------------")
G.add_edges_from(H.edges)
print(G.nodes)
print(G.edges)
#
print("--------------------------------------------------------")

G.clear()
G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam")  # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')

print("--------------------------------------------------------")

print(G.nodes)
print(G.edges)

DG = nx.DiGraph()
DG.add_edge(2, 1)
DG.add_edge(1, 3)
DG.add_edge(2, 4)
DG.add_edge(1, 2)
assert list(DG.successors(2)) == [1, 4]
assert list(DG.edges) == [(2, 1), (2, 4), (1, 3), (1, 2)]

# They are also dict-like in that you can look up node and edge
# data attributes via the views and iterate with data attributes 
# using methods .items(), .data(). If you want a specific container 
# type instead of a view, you can specify one. Here we use lists, 
# though sets, dicts, tuples and other containers may be better 
# in other contexts.


print(list(G.nodes))
print(set(G.nodes))

print(dict(G.nodes))

print(tuple(G.nodes))

print("222--------------------------------------------------------")
# out put
print(G.edges([2, 'm']))

# https://networkx.org/documentation/stable/tutorial.html
# Using the graph constructors
# https://www.osgeo.cn/networkx/tutorial.html#

# 每个图，节点和边都可以在关联的属性字典中保存键值属性对，那么就可以给每个ee
G = nx.Graph(day="Friday")
print(G.graph)

G.graph['day'] = "monday"
print(G.graph)

# Node attributes
G.add_node(1, time='5pm')
G.add_nodes_from([3], time='2pm')
print(G.nodes[1])
G.nodes[1]['room'] = 714
print("sss", G.nodes._data())

print(f"sss", G.nodes._data())

# edge Attributes
G.add_edge(1, 2, weight=4.7)
G.add_edges_from([(3, 4), (4, 5)], color='red')
G.add_edges_from([(1, 2, {'color': 'blue'}), (2, 3, {'weight': 8})])
G[1][2]['weight'] = 4.7
G.edges[3, 4]['weight'] = 4.2

print(G.nodes._data())


# Python类型注解，你需要知道的都在这里了

# https://zhuanlan.zhihu.com/p/419955374
def say(name: str) -> str:
    return f'Hello {name}'


age: int = 20


class Person:
    def __init__(self, name: str):
        self.name = name


def hello1(p: Person) -> str:
    return f'Hello, {p.name}'


# 如果要避免循环导入或者注解早于对象定义的情况，可以用字符串代替类型：
def hello(p: 'Person') -> str:
    return f'Hello, {p.name}'


# 列表、字典、元组等包含元素的复合类型，用简单的 list，dict，tuple 不能够明确说明内部元素的具体类型。
# 因此要用到 typing 模块提供的复合注解功能：

from typing import List, Dict, Tuple


# 参数1: 元素为 int 的列表
# 参数2: 键为字符串，值为 int 的字典
# 返回值: 包含两个元素的元组
def mix(scores: List[int], ages: Dict[str, int]) -> Tuple[int, int]:
    return (0, 0)


# 在某些情况下，不需要严格区分参数到底是列表还是元组（这种情况还蛮多的）。
# 这时候就可以将它们的特征抽象为更泛化的类型（泛型），比如 Sequence（序列）。
from typing import Sequence as Seq1


def foo(seq: Seq1[str]):
    for item in seq:
        print(item)


# 类型别名
# 有时候对象的类型可能会非常复杂，
# 或者你希望给类型赋予一个有意义的名称，那么你可以这样定义类型的别名：

from typing import Tuple
