"""
分治法(Divide-Conquer)-逆序对数量（Count Inversions）
统计数组中逆序排列的所有数字对
例如[1,2,3]中没有逆序数
[1,3,2]中有1对逆序数,即 [3,2]
[4,2,3,1]中有5对, 即[4,3],[4,2],[4,1],[2,1],[3,1]
"""

'''逆序数对计数

'''


def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    '''
    left 表示左半边数组, inv_left 表示左边数组的逆序对数
    right 表示右半边数组, inv_right 表示右边数组的逆序对数
    merged 表示合并排序后的数组, inv_merged 表示合并后的逆序对数
    '''
    left, inv_left = count_inversions(arr[:mid])
    right, inv_right = count_inversions(arr[mid:])
    merged, inv_merge = merge_and_count(left, right)

    return merged, inv_left + inv_right + inv_merge


def merge_and_count(left, right):
    merged = []
    inv_count = 0
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv_count += len(left) - i

    merged += left[i:]
    merged += right[j:]

    return merged, inv_count


# Example usage:
arr = [4, 2, 3, 1]
# arr = [1, 5, 4, 8, 10, 2, 6, 9, 12, 11, 3, 7]
sorted_arr, inversions = count_inversions(arr)
print("Original Array:", arr)
print("Sorted Array:", sorted_arr)
print("Number of Inversions:", inversions)
