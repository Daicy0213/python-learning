import chardet

file_path = 'C:/Users/37245/Desktop/newName.txt'
folder_path = 'C:/Users/37245\Desktop/testfold'


# 检测文件编码格式
def detect_encoding(file_path: str) -> tuple:
    with open(file_path, 'rb') as f:
        raw_data = f.read()

    result = chardet.detect(raw_data)
    encoding = result['encoding']
    confidence = round(result['confidence'] * 100, 2)

    return encoding, confidence


# 检测文件编码类型
encoding = detect_encoding(file_path)

names_count = 0  # 文件中新名称的计数器
new_list = []
# 读取文件并打印新文件名
with open(file_path, 'r', encoding=encoding[0]) as f:
    for line in f.readlines():
        name = line.strip()
        print(name)  # 把末尾的'\n'删掉
        new_list.append(name)
        names_count += 1

print("共 %d 个新文件名" % names_count)

# 对文件夹内的文件进行排序

# 模拟system("pause")
print("Press any key to end . . .")
input()
