"""
os标准库
os.getcwd()：返回当前工作目录。
os.chdir(path)：把path设为当前工作目录。
os.remove(path)：删除指定的文件，但是不能删除文件夹。
os.mkdir(path)：创建空目录。
os.makedirs(path1\path2\path3\.....)：创建多级目录，已有的话无法创建。
os.rmdir(path)：  删除一个目录，如果目录不为空，则会报错。
os.removedirs(path1/path2/path3/...)：递归删除目录,并递归到上一级目录，如果也为空，则也删除，以此类推。
os.listdir(path)：返回path目录下的文件和目录列表，包括隐藏文件。（无法返回子目录下的文件）。
os.stat(path)：获取文件/目录的信息，如文件大小、最后访问时间等。
os.path.isdir(path)：判断path是否为目录
os.path.isfile(path)：判断path是否为文件
os.path.exists(path)：判断指定路径的文件是否存在
os.path.dirname(path)：返回path的上一级目录
"""
import os
import sys

path = os.getcwd()

# getcwd()获取当前工作路径
print(os.getcwd())

# listdir()查找输入路径下的所有文件和目录, 类似ls
print(os.listdir(path))

# 返回上一级目录
path = os.path.dirname(path)

# 遍历该目录下的所有文件
for p, dirs, files in os.walk(path):
    print(p)
    print(dirs)
    print(files)
    print("")

# 获取系统名称 windows系统为"nt", Unix系统的所有分支(包括MacOS)均为"posix"
print(os.name)
# Linux系统为'linux', Windows为'win32', macos为'darwin'
print(sys.platform)
# 外部参数
# sys.argv[0]是被调用的脚本文件名或全路径
# sys.argv[1:]之后的元素就是我们从程序外部输入的，而非代码本身的，从外部运行程序并给参数，这也是我们在cmd里面运行的原因。
# 例如, 执行: python test.py a b c 则后续参数即为[a,b,c]
print(sys.argv)
# 环境变量
print(os.environ['PATH'])
