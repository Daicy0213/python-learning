"""
Python基础
"""

"""
一. 数据类型: 整形(int)/浮点数(float)/字符串(str)/布尔值(bool)/空值(None)
"""
i = True
print(type(i))

# 两种除法
print(9 / 3)
print(10 // 3)

# 次方
print(2 ** 5)
print(pow(2, 5))

# encode与decode函数
s = '中文'
print(s.encode('utf-8'))
print(s.encode('utf-8').decode('utf-8', errors='ignore'))
print()

# 字符串的格式化的三种方法
# 方法一: 占位符
print('Hello, %s' % s)

"""
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数
"""

print('%2d%02d' % (3, 1))
print('%.2f' % 3.1415926)

# 方法二: format函数
print('Hello, {0}, 成绩提升了 {1:.1f}%, 恭喜获得{2}'.format('小明', 17.125, '个人进步奖'))

# 方法三: 使用以f开头的字符串，称之为f-string
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')
print('')

"""
二. list与tuple
"""
print('list与tuple')
classmates = ['Michael', 'Bob', 'Tracy']
# 如果tuple中只有一个元素, 应该在后面添加逗号以区别小括号的优先计算符号的作用
first_season = ('Spring',)
# list中还可以可以添加list, list不要求元素为单一类型
classmates.append(["Kobe", 24])
classmates.insert(2, "Jordan")
# 可以使用pop(i)来删除指定位置的元素
classmates.pop(1)
print(type(first_season))
for e in classmates:
    print(e)
print()

"""
三. dict和set
dict使用的是伪随机探测(pseudo-random probing)的散列表(hash table)作为字典的底层数据结构, 时间复杂度为O(1)
伪随机探测即随机选择一个数字作为冲突的地址
set也是使用的散列表作为底层数据结构
另外还有frozenset作为一个不可变的集合
"""
print('遍历循环dict')
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
for name in d.keys():
    print("%s : %d" % (name, d[name]))
# 判断是否存在, 若不存在则再添加一个k-v
if "Kobe" not in d:
    d['Kobe'] = 81
print("Kobe : %d" % d["Kobe"])

s = {1, 1, 2, 2, 3, 3}
print(type(s))
print('遍历循环set')
for a in s:
    print(a)
print()
