# 🐍 Python Learning

> Python 学习笔记与练习代码仓库 —— 记录从 Python 基础、面向对象，到 NumPy、数据结构与算法的完整学习过程。

## 📖 简介

本仓库是我学习 Python 过程中的笔记与练习代码合集，包含：

- 跟随 **廖雪峰《Python 教程》** 编写的配套练习（覆盖语法、函数式编程、OOP、错误处理、并发、常用内建模块等）
- 系统的 **面向对象（OOP）** 与 **NumPy** 中文系列教程（Jupyter Notebook）
- 经典 **数据结构** 与 **算法** 的 Python 实现与练习
- 一些趣味小实验（抛硬币模拟、财富分布实验等）

## 📂 目录结构

| 目录 / 文件 | 内容说明 |
|------|---------|
| [Liaoxuefeng/](Liaoxuefeng/) | 廖雪峰《Python 教程》配套练习代码（按教程章节分目录） |
| [python_oop/](python_oop/) | 面向对象专题系列 Notebook，共 7 章（类与对象、封装、继承与 MRO、多态、魔术方法等） |
| [numpy_learning/](numpy_learning/) | NumPy 系列中文教程 Notebook，共 6 章，详见 [numpy_learning/README.md](numpy_learning/README.md) |
| [python_data_structure/](python_data_structure/) | 数据结构学习代码（链表、栈、队列、递归、树、二叉搜索树、图） |
| [AdvAlgAnal/](AdvAlgAnal/) | 高级算法分析练习（归并排序、逆序对、区间调度、0-1 背包等） |
| [algorithm_test/](algorithm_test/) | 算法测试（FHQ-Treap 实现与测试） |
| [test/](test/) | 趣味小实验（抛硬币、财富分布模拟等） |
| [InterviewTest.py](InterviewTest.py) | 面试题练习脚本 |

### 📘 Liaoxuefeng 子目录细分

| 子目录 | 核心内容 |
|--------|---------|
| `a_basic` | Python 基础：语法、函数、函数式编程（map/reduce/filter/sorted、闭包、装饰器）、模块、OOP 入门、类型注解 |
| `b_advance_oop` | 面向对象进阶：`__slots__`、`@property`、多重继承、定制类、枚举、元类（metaclass） |
| `c_error_processing` | 错误处理与调试：异常、断言、单元测试（unittest） |
| `d_io` | IO 编程：文件读写等 |
| `e_concurrent` | 并发编程：多线程、多进程、线程锁与线程池、生产者-消费者爬虫、协程、asyncio、分布式进程（master/worker） |
| `f_inside_module` | 常用内建模块：`datetime`、`collections`、`argparse`、`base64`、`hashlib`、`hmac`、`itertools`、`contextlib`、`re`、`timeit` |
| `h_mapreduce` | 实战练习：WordCount（mapreduce 思路的单词计数） |

## 🚀 快速开始

### 环境要求

- Python 3.10+
- 运行 Notebook 系列（`python_oop/`、`numpy_learning/`）需要 Jupyter 与 NumPy

```bash
pip install numpy jupyter
```

### 运行方式

```bash
# 运行普通 Python 脚本
python InterviewTest.py

# 打开 Notebook 系列
jupyter notebook
```

## 🔗 相关链接

- 廖雪峰《Python 教程》：https://liaoxuefeng.com/books/python/

## 📝 说明

- 本仓库为个人学习记录，代码注释与命名以中文为主，方便复习查阅
- `numpy_learning/tmp_io/`、`.ipynb_checkpoints/` 等为运行产生的临时文件，已通过 `.gitignore` 排除
