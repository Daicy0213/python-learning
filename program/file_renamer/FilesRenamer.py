import chardet
import os
import sys


"""批量文件重命名
可以使用pyinstaller库打包成可执行文件
"""
# names_path = 'C:/Users/37245/Desktop/newName.txt'
# folder_path = 'C:/Users/37245/Desktop/testfold'


# 检测文件编码格式
def detect_encoding(file_path: str) -> tuple:
    with open(file_path, 'rb') as f:
        raw_data = f.read()

    result = chardet.detect(raw_data)
    encoding = result['encoding']
    confidence = round(result['confidence'] * 100, 2)

    return encoding, confidence


# 替换特殊字符为空格
def replace_special_chars(s):
    special_chars = ['?', '/', '\\', '<', '>', '*', '|', '\t']
    for char in special_chars:
        s = s.replace(char, '  ')
    return s


if __name__ == '__main__':

    # 输入文件地址
    while True:
        try:
            print("请输入存有新文件名的文件地址\n 注意斜杠方向, 如: \"C:/Doc/newName.txt\" 即为合法地址")
            names_path = input()
            # 检测文件编码类型
            encoding = detect_encoding(names_path)
            break
        except FileNotFoundError as fnf:
            print("文件不存在, 请检查...")

    # 读取文件并打印新文件名
    names_count = 0  # 文件中新名称的计数器
    new_list = []
    with open(names_path, 'r', encoding=encoding[0]) as f:
        for line in f.readlines():
            name = line.strip()
            name = replace_special_chars(name)
            new_list.append(name)
            print(name)
            names_count += 1

    print("文件中共 %d 个新文件名" % names_count)

    while True:
        print("请输入需要修改的文件夹地址")
        folder_path = input()
        isdir = os.path.isdir(folder_path)
        if isdir:
            break
        else:
            print("输入地址有误")

    # 读取文件夹内的所有文件
    listfiles = os.listdir(folder_path)

    # 对文件名进行排序
    listfiles.sort()
    listfiles.sort(key=len)

    # 如果文件夹中仍有文件夹
    contain_dirs = [x for x in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, x))]
    if len(contain_dirs) != 0:
        print("输入的文件夹内有仍有其它文件夹, 将自动忽略")
        for e in contain_dirs:
            listfiles.remove(e)

    if len(listfiles) != len(new_list):
        print("新文件名数量与文件数量不一致, 将自动对齐")

        # 如果文件数量大于文件名数量, 则超出的部分不修改
        if len(listfiles) > len(new_list):
            diff = len(listfiles) - len(new_list)
            listfiles = listfiles[:-diff]

        # 如果文件名数量大于文件数量, 则超出的部分不修改
        if len(new_list) > len(listfiles):
            diff = len(new_list) - len(listfiles)
            new_list = new_list[:-diff]

    # 打印修改的文件名以确认
    print('修改列表:')
    for i in range(len(listfiles)):
        print(listfiles[i], '----->', new_list[i])

    while True:
        confirm = input('\n确认修改? \n取消修改程序将退出\n[y]:n \n')
        if confirm == 'y' or confirm == 'Y' or confirm == "":
            # 如果最后一位不是/的话, 则os.path.join()函数有可能生成xx/xx\这样斜杠不统一的情况
            if folder_path[-1] != '/':
                folder_path = folder_path + '/'
                for i in range(len(listfiles)):
                    old_name = os.path.join(folder_path, listfiles[i])
                    new_name = os.path.join(folder_path, new_list[i])
                    os.rename(old_name, new_name)
            print("修改完成")
            break
        elif confirm == 'n' or confirm == "N":
            print("程序退出")
            sys.exit()

    # 模拟system("pause")
    print("Press any key to end . . .")
    # input()
