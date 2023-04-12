"""
file-like Object
像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
"""

file_pic = '../../Optimal pruned tree-cut mapping-based fast shielding for large-scale networks.assets' \
           '/image-20230409163047641.png'
file_txt = '../../min-cut/data.txt'
file_write_test = '../test.txt'

# 二进制文件
# 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
f = open(file_pic, 'rb')
print(f.read(10))
# 使用gbk编码读取文件，仅读取8个字符
f = open(file_txt, 'r', encoding='gbk', errors='ignore')
print(f.read(8))
# 写文件
# w+：打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。
# 如果该文件不存在，创建新文件（但不可以创建文件夹）。
with open(file_write_test, 'w+') as f:
    f.write('Hello, world!')
