import logging

"""
int()函数可能会抛出ValueError，所以我们用一个except捕获ValueError，用另一个except捕获ZeroDivisionError。
此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
"""
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

"""
Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：
https://docs.python.org/3/library/exceptions.html#exception-hierarchy
Python内置的logging模块可以非常容易地记录错误信息：
通过配置，logging还可以把错误记录到日志文件里，方便事后排查。
logging.basicConfig(level=logging.INFO)
它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。
同理，指定level=WARNING后，debug和info就不起作用了。
这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
"""
print('-' * 10)

logging.basicConfig(level=logging.INFO)


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    c = '0'
    try:
        bar(c)
    except Exception as e:
        logging.exception(e)
    finally:
        logging.debug('loging.info=======>c = %s' % c)  # 此行不会打印，因为level=logging.INFO
        logging.warning('loging.info=======>c = %s' % c)
        logging.info('loging.info=======>c = %s' % c)


main()

"""
定义一个error类
"""


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


foo('0')
