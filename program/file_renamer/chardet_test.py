import chardet

""" 检查文件编码的代码
使用pyinstaller将py文件打包为exe可执行文件
-F 表示生成单个可执行文件
-D –onedir 创建一个目录，包含exe文件，但会依赖很多文件（默认选项）
-w 表示去掉控制台窗口，这在GUI界面时非常有用。不过如果是命令行程序的话那就把这个选项删除吧
-c –console, –nowindowed 使用控制台，无界面(默认)
-p 表示你自己自定义需要加载的类路径，一般情况下用不到
-i 表示可执行文件的图标
其他参数，可以通过pyinstaller --help查看

进入python需要打包的脚本所在目录，然后执行下面的命令即可：
```pyinstaller -F test.py```

带ICO图标制作
需要用到ICO图标，大家可以网上搜索“ICO 在线生成”，可以直接点击ICO图标制作在上面制作、然后保存以ico_name.ico为列
```pyinstaller -F -i ico_name.ico test.py```


去dos窗口方法
tkinter 工程 运用 pyinstaller 打包成exe，运行exe文件的时候，会弹出一个dos命令窗口，这个窗口可以看到一些打印信息
如果想只运行tkinter 页面，去掉dos窗口需要在打包的时候 加上 -w 参数
```pyinstaller -F test.py -w```

生成exe文件后，打开速度慢问题: 
1. 改用-D参数
2. 使用 Enigma Virtual Box 将文件夹压缩成一个exe文件
"""


def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()

    result = chardet.detect(raw_data)
    encoding = result['encoding']
    confidence = round(result['confidence'] * 100, 2)

    return encoding, confidence


# 'C:/Users/37245/Desktop/newName.txt'
# 文件路径
file_path = input('文件路径')

# 检测文件编码
encoding, confidence = detect_encoding(file_path)

print(f"File encoding: {encoding}")
print(f"Confidence: {confidence}%")

# 模拟system("pause")
print("Press any key to continue . . .")
input()
