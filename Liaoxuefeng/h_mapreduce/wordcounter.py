from functools import reduce
from collections import defaultdict
import re

# 输入文件内容
file_content = """Hi, this is John.
Hi, John. What is this?
This is not mine."""

# 1. 读取文件并进行拆分，并移除标点符号和转换为小写
def split_and_normalize(text):
    # 移除标点符号并转换为小写
    text = re.sub(r'[^\w\s]', '', text).lower()
    return text.split('\n')

lines = split_and_normalize(file_content)

# 2. Map阶段
def map_function(line):
    words = line.split()
    return [(word, 1) for word in words]

# 将每一行映射成键值对
mapped = map(map_function, lines)
# 展平列表
mapped = [item for sublist in mapped for item in sublist]

# 3. Shuffle和Sort阶段
def shuffle_sort(mapped):
    shuffle_sorted = defaultdict(list)
    for key, value in mapped:
        shuffle_sorted[key].append(value)
    return shuffle_sorted

shuffled_sorted = shuffle_sort(mapped)

# 4. Reduce阶段
def reduce_function(accumulator, current):
    key, values = current
    accumulator[key] = sum(values)
    return accumulator

reduced = reduce(reduce_function, shuffled_sorted.items(), {})

# 输出结果
for key, value in reduced.items():
    print(f'{key}: {value}')
