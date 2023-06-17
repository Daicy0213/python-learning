import chardet


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
