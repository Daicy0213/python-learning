import igraph
import matplotlib.pyplot as plt
# 创建一个无向图
g = igraph.Graph()
g.add_vertices(5)
g.add_edges([(0, 1), (0, 2), (1, 2), (2, 3), (3, 4)])

# 设置顶点名称
g.vs["label"] = ["A", "B", "C", "D", "E"]

# 进行BFS
bfs_tree = g.bfs(0, mode=igraph.OUT)

# 将BFS树保存为图像
layout = g.layout("kk")
print(bfs_tree)
visual_style = {"vertex_label": g.vs["label"],
                "vertex_size": 30,
                "edge_width": 1,
                "layout": layout,
                "margin": 20}
igraph.plot(bfs_tree, **visual_style, bbox=(300, 300),target="bfs_treess.png")

#igraph.plot(bfs_tree, **visual_style).show()
## 为每个节点添加标签
#vertex_labels = [str(i) for i in range(len(g.vs))]

## 为每个节点设置颜色
#vertex_colors = ['blue' for _ in range(len(g.vs))]

#ig.plot(g, target=ax, vertex_label=vertex_labels, vertex_label_size=16,
        #vertex_color=vertex_colors, vertex_size=30, edge_width=2)

##ig.plot(g,target=ax)
#plt.savefig("ppppppot.jpg")

#plt.savefig("kkk")

#ig.plot(g, target=ax, vertex_label=vertex_labels, vertex_label_size=16,
        #vertex_color=vertex_colors, vertex_size=30, edge_width=2)

##ig.plot(g,target=ax)
#plt.savefig("ppppppot.jpg")