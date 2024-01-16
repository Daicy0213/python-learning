"""
贪心算法(Greedy Algorithm)-区间调度(Interval Scheduling)
区间调度问题是指, 如果给出多个形如[1,3]这样的闭区间, 求出其中最多有几个不交互的区间.
类似于今天举办了多个活动, 每个活动的区间可以用[start,end]来表示开始和结束时间, 需要求出今天最多可以参加多少个活动
这类问题在生活中比较常见, 类似安排学生课程表, 行程安排等等
"""


def interval_scheduling(intervals):
    # 根据结束时间排序
    intervals.sort(key=lambda x: x[1])

    selected_intervals = []
    # 将结束时间设置为负无穷
    end_time = float('-inf')

    for interval in intervals:
        start, end = interval
        if start >= end_time:
            selected_intervals.append(interval)
            end_time = end

    return selected_intervals


# Example usage:
intervals = [(2, 4), (3, 5), (1, 3), (5, 6), (4, 8)]
result = interval_scheduling(intervals)
print("Selected Intervals:", result)
