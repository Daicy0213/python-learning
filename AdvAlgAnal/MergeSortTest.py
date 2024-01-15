"""
分治法(Divide-Conquer)-合并排序
"""


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # 递归地对左右两部分进行归并排序
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # 合并两个有序数组
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # 处理剩余的元素
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# 示例
arr = [12, 3, 11, 1, 13, 5, 6, 7]
print("原始数组:", arr)

# 调用归并排序函数
merge_sort(arr)

print("排序后的数组:", arr)
