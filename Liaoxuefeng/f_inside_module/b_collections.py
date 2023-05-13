"""collections库的使用
"""
from collections import namedtuple

"""ametuple
如果直接使用tuple定义一个二维坐标(1, 2), 很难看出这个tuple是用来表示一个坐标的
如果定义一个class来表示又有些小题大做, 那么就可以使用nametuple
"""
print("=" * 15, "nametuple", "=" * 15)
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)  # 1
print(p.y)  # 2
print(isinstance(p, Point))  # True
print(isinstance(p, tuple))  # True

# 同理可以使用nametuple来定义一个圆
Circle = namedtuple('Circle', ['x', 'y', 'r'])

"""deque
使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
"""
print("=" * 15, "deque", "=" * 15)
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

"""defaultdict
使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
"""
print("=" * 15, "defaultdict", "=" * 15)
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])  # key1存在
print(dd['key2'])  # key2不存在，返回默认值

"""ChainMap
ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。
什么时候使用ChainMap最合适？
举个例子：应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，还可以有默认参数。
我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数。
"""
print("=" * 15, "ChainMap", "=" * 15)
from collections import ChainMap
import os, argparse

# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
# 将参数转换为dict
command_line_args = {k: v for k, v in vars(namespace).items() if v}

# 将参数转化的dict, 系统环境dict, 默认的参数dict, 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

# 使用命令行python .\Liaoxuefeng\f_inside_module\b_collections.py -u bob -c yellow
# 打印:
# =============== ChainMap ===============
# color=yellow
# user=bob

"""Counter
Counter是一个简单的计数器，例如，统计字符出现的个数：
"""
print("=" * 15, "Counter", "=" * 15)
from collections import Counter

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
