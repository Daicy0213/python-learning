#import igraph

#g = igraph.Graph()
#g.add_vertices(5)
#g.add_edges([(0,1), (1,2), (2,3), (3,4), (4,0)])
#layout = g.layout('circle')
#igraph.plot(g, layout=layout, vertex_label="ss",target="ssss.png")



import igraph as ig

# 创建无向图
g = ig.Graph([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 3), (2, 4)])

# 设置节点名称
g.vs["name"] = ["A", "B", "C", "D", "E"]

# 运行BFS算法
bfs_tree = g.bfs(0, mode=ig.OUT)

# 将遍历树保存为图像
layout = g.layout("kk")  # 设置图像布局
ig.plot(bfs_tree, layout=layout, bbox=(300, 300), vertex_label=g.vs["name"],target="learn5.png")

