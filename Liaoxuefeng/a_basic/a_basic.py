"""
Python基础
"""

"""
一. 数据类型: 整形(int)/浮点数(float)/字符串(str)/布尔值(bool)/空值(None)
"""
i = True
print(type(i))

# 两种除法
print('两种除法:')
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

"""match"""
args = ['gcc', 'hello.c', 'world.c']


# args = ['clean']
# args = ['gcc']

def func(args):
    match args:
        # 如果仅出现gcc，报错:
        case ['gcc']:
            print('gcc: missing source file(s).')
        # 出现gcc，且至少指定了一个文件:
        case ['gcc', file1, *files]:
            print('gcc compile: ' + file1 + ', ' + ', '.join(files))
        # 仅出现clean:
        case ['clean']:
            print('clean')
        case _:
            print('invalid command.')


func(args)  # 打印 gcc compile: hello.c, world.c
# case ['gcc', file1, *files]表示列表第一个字符串是'gcc'，第二个字符串绑定到变量file1，后面的任意个字符串绑定到*files

print(", ".join(("b",)))
print(", ".join(("b","c")))
