"""
二. list与tuple
list的内部是使用数组实现的, 所以列表 append 比 insert 快,
"""
print('list与tuple')
# list使用中括号[]
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

"""zip对象
zip 函数能够把多个可迭代对象打包成一个元组构成的可迭代对象，它返回了一个 zip 对象，通过 tuple, list
可以得到相应的打包结果
"""
print('zip对象')
L1, L2, L3 = list('abc'), list('def'), list('hij')
print(list(zip(L1, L2, L3)))
print(tuple(zip(L1, L2, L3)))

for i, j, k in zip(L1, L2, L3):
    print(i, j, k)

"""enumerate方法
enumerate 是一种特殊的打包，它可以在迭代时绑定迭代元素的遍历序号
"""
print('enumerate方法')
L = list('abcd')
for index, value in enumerate(L):
    print(index, value)

print('使用zip对象也可以实现这样的功能:')
for index, value in zip(range(len(L)), L):
    print(index, value)
