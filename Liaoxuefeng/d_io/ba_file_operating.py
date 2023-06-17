"""
操作文件和目录
"""
import os

# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print("os name: \t\t\t", os.name)  # 操作系统类型
print("os env: \t\t\t", os.environ)  # 环境变量
print("os env.PATH: \t\t", os.environ.get('PATH'))
# 查看当前目录的绝对路径:
print("current abspath: \t", os.path.abspath('.'))
# 在当前目录下创建一个新目录，首先把新目录的完整路径表示出来:
dir_path = os.path.join(os.path.abspath('.'), 'testdir')
print(dir_path)
# 然后在创建目录
os.mkdir(dir_path)
# 删除目录
os.rmdir(dir_path)

"""
路径合并
把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
part-1/part-2
而Windows下会返回这样的字符串：
part-1\part-2
"""
join_path = os.path.join(os.path.abspath('.'), 'a_file_io.py')
print(join_path)
"""
路径拆分
同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
"""
print("split path:\t\t\t", os.path.split(join_path))

# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：

print("suffix:\t\t\t\t", os.path.splitext(join_path))

# 重命名
os.rename('./test.txt', 'test.py')

# 删除
# os.remove('test.py')

"""复制
但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。
幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
"""

# 查看上一级目录下的所有文件和文件夹(注意, 返回的是一个字符串列表)
print(os.listdir('..'))

# 判断一个文件是否是文件夹
print(os.path.isdir(join_path))
# 判断是否是文件
print(os.path.isfile(join_path))

""" 遍历一个目录下的所有文件
os.walk(top): 目录树生成器
对于目录树中以top为根的每个目录(包括top本身，但不包括'.'和'..')，产生一个3元组
    目录路径, 目录名, 文件名
"""


def traversal_all(path):
    file_paths = []
    for d_path, d_names, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(d_path, filename)
            file_paths.append(file_path)
    return file_paths


print(traversal_all('..'))

# 利用Python的特性来过滤文件。比如我们要列出上一级目录下的所有目录，只需要一行代码：
print([x for x in os.listdir('..') if os.path.isdir(os.path.join("..", x))])

# 要列出所有的.py文件，也只需一行代码：
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
