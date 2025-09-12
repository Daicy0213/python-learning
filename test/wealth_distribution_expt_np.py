import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

n = 1000
w = 100
epochs = 2000   # 总迭代轮数
step = 5       # 每帧模拟多少轮

np.random.seed(42)
wealth = np.full(n, w, dtype=int)

# 初始化绘图
fig, ax = plt.subplots()
bins = np.linspace(0, w*2, 50)  # 固定区间
hist_data, _, _ = ax.hist(wealth, bins=bins, color="skyblue", edgecolor="black")
ax.set_xlim(0, w*2)
ax.set_ylim(0, n//2)
ax.set_xlabel("Wealth")
ax.set_ylabel("Number of Players")
ax.set_title("Wealth Distribution Over Time")

def update(frame):
    global wealth
    # 模拟 step 轮
    for _ in range(step):
        givers = np.where(wealth > 0)[0]
        receivers = np.random.randint(0, n, size=len(givers))
        wealth[givers] -= 1
        np.add.at(wealth, receivers, 1)

    # 更新直方图
    ax.clear()
    ax.hist(wealth, bins=bins, color="skyblue", edgecolor="black")
    ax.set_xlim(0, w*2)
    ax.set_ylim(0, n//2)
    ax.set_xlabel("Wealth")
    ax.set_ylabel("Number of Players")
    ax.set_title(f"Wealth Distribution (epoch={frame*step})")

# 创建动画
ani = FuncAnimation(fig, update, frames=epochs//step, interval=200, repeat=False)

# 保存成视频 (需要安装 ffmpeg)
ani.save("wealth_distribution.mp4", writer="ffmpeg", fps=5)

plt.show()
