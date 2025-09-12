"""一个财富分配的实验
假设有n个人, 每个人拥有的财富绝对平均, 初始值都为w.
实验将进行epoch轮, 每一轮每个人都将自己的1个财富值随机分配给另一个人.
财富值为0的情况下将使用两种策略:
1. 财富值为0的人将不再进行下一轮的分配.
2. 财富值为0的人将不能分配财富值给其他人, 但是可以接受其他人的财富值.
最后讲实验结果可视化.
"""
import numpy as np
import matplotlib.pyplot as plt

n = 1000
w = 100
epoch = 50000


class Player:

    def __init__(self, wealth):
        self.wealth = wealth

    def give(self):
        if self.wealth == 0:
            return
        else:
            self.wealth = self.wealth - 1
            id = np.random.randint(n)
            return id

    def get(self):
        self.wealth = self.wealth + 1

    def get_wealth(self):
        return self.wealth


if __name__ == '__main__':
    np.random.seed(42)
    l = [Player(w) for i in range(n)]
    for i in range(epoch):
        for j in range(n):
            idx = l[j].give()
            if idx is not None:
                l[idx].get()

    wealths = [l[i].get_wealth() for i in range(n)]
    plt.hist(wealths, bins=50, color="skyblue", edgecolor="black")
    plt.xlabel("Wealth")
    plt.ylabel("Number of Players")
    plt.title("Wealth Distribution")
    plt.show()
