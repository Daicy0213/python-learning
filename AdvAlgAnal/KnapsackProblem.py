"""
动态规划(Dynamic Programming)-背包问题(Knapsack Problem)
背包问题是指, 给定一组物品, 每种物品都有自己的重量和价格, 在限定的总重量内, 我们如何选择, 才能使得物品的总价格最高.
"""
import numpy as np
import time as tm


def knapsack(weights, values, capacity):
    """
    weights 表示物品重量的数组
    values 表示物品价值的数组
    capacity 表示背包的最大容量
    n 表示有几件物品
    """
    n = len(weights)
    # 初始化二维数组dp, dp[]
    # 注意这里有个语法糖, 列表生成器可以用乘法来获取数组例如 a = [0] * 3 表示一个包含三个0元素的一维的数组
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # 填充dp数组
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # 不放入背包
            dp[i][w] = dp[i - 1][w]
            # 放入背包
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

    return dp[n][capacity]


# 示例1
weights = [2, 2, 3]
values = [6, 10, 12]
capacity = 5

result = knapsack(weights, values, capacity)
print("Maximum value:", result)

# 示例2
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

result = knapsack(weights, values, capacity)
print("Maximum value:", result)

# 示例3
# 生成长度为5000的随机整数数组
"""
start_time = tm.time()
random_integers_weight = np.random.randint(0, 100, 5000)
random_integers_values = np.random.randint(0, 20, 5000)
capacity = 15000
result = knapsack(random_integers_weight, random_integers_values, capacity)
end_time = tm.time()
execution_time = end_time - start_time
print("Maximum value:", result)
print(f"程序运行时间: {execution_time} 秒")
"""