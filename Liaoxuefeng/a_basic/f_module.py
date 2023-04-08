#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行
# 第2行注释表示.py文件本身使用标准UTF-8编码；

""" a standard module """  # 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途
# 比如__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用
# Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量
__author__ = 'Daicy'

import sys  # 导入模块


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__
# 而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
# 在命令行输入 python .\f_module.py
# 打印Hello, world!
# 输入 python .\f_module.py Michael
# 则打印Hello, Michael!
if __name__ == '__main__':
    test()
