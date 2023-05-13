"""argparse
在命令行程序中，经常需要获取命令行参数。Python内置的sys.argv保存了完整的参数列表，我们可以从中解析出需要的参数：
# copy.py
import sys
print(sys.argv)
source = sys.argv[1]
target = sys.argv[2]
>>['copy.py', 'source.txt', 'copy.txt']

这种方式能应付简单的参数，但参数稍微复杂点，比如可以使用-d复制目录，使用--filename *.py过滤文件名等，解析起来就非常麻烦。
为了简化参数解析，我们可以使用内置的argparse库，定义好各个参数类型后，它能直接返回有效的参数。

假设我们想编写一个备份MySQL数据库的命令行程序，需要输入的参数如下：
host参数：表示MySQL主机名或IP，不输入则默认为localhost；
port参数：表示MySQL的端口号，int类型，不输入则默认为3306；
user参数：表示登录MySQL的用户名，必须输入；
password参数：表示登录MySQL的口令，必须输入；
gz参数：表示是否压缩备份文件，不输入则默认为False；
outfile参数：表示备份文件保存在哪，必须输入。

其中，outfile是位置参数，而其他则是类似--user root这样的“关键字”参数。
用argparse来解析参数，一个完整的示例如下：
"""
import argparse


def main():
    # 定义一个ArgumentParser实例:
    parser = argparse.ArgumentParser(
        prog='backup',  # 程序名
        description='Backup MySQL database.',  # 描述
        epilog='Copyright(r), 2023'  # 说明信息
    )
    # 定义位置参数:
    parser.add_argument('outfile')
    # 定义关键字参数:
    parser.add_argument('--host', default='localhost')
    # 此参数必须为int类型:
    parser.add_argument('--port', default='3306', type=int)
    # 允许用户输入简写的-u:
    parser.add_argument('-u', '--user', required=True)
    parser.add_argument('-p', '--password', required=True)
    parser.add_argument('--database', required=True)
    # gz参数不跟参数值，因此指定action='store_true'，意思是出现-gz表示True:
    parser.add_argument('-gz', '--gzcompress', action='store_true', required=False, help='Compress backup files by gz.')

    # 解析参数:
    args = parser.parse_args()

    # 打印参数:
    print('parsed args:')
    print(f'outfile = {args.outfile}')
    print(f'host = {args.host}')
    print(f'port = {args.port}')
    print(f'user = {args.user}')
    print(f'password = {args.password}')
    print(f'database = {args.database}')
    print(f'gzcompress = {args.gzcompress}')


"""
一. 错误
如果不使用命令行运行, 而是使用main函数直接运行, 则会报错: 
usage: backup [-h] [--host HOST] [--port PORT] -u USER -p PASSWORD --database
              DATABASE [-gz]
              outfile
backup: error: the following arguments are required: outfile, -u/--user, -p/--password, --database

二. 正确方式
在终端使用 .\Liaoxuefeng\f_inside_module\c_argparse.py -u root -p hello --database testdb backup.sql
则打印:
parsed args:
outfile = backup.sql
host = localhost
port = 3306
user = root
password = hello
database = testdb
gzcompress = False

三. 打印帮助文档
终端使用: .\Liaoxuefeng\f_inside_module\c_argparse.py -h
打印:
usage: backup [-h] [--host HOST] [--port PORT] -u USER -p PASSWORD --database DATABASE [-gz] outfile

Backup MySQL database.

positional arguments:
  outfile

options:
  -h, --help            show this help message and exit
  --host HOST
  --port PORT
  -u USER, --user USER
  -p PASSWORD, --password PASSWORD
  --database DATABASE
  -gz, --gzcompress     Compress backup files by gz.

Copyright(r), 2023
"""
if __name__ == '__main__':
    main()
