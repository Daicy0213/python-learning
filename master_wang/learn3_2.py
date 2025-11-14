import igraph as ig
#readme 画图专用
#learn3_2可以通过深度来画图
# 创建一个有5个点的图形对象
g = ig.Graph(n=5)

# 添加边
g.add_edges([(0,1), (0,2), (1,3), (1,4), (3,0)])

# 设置节点的深度
depths = [0,1,1,2,2]
g.vs["depth"] = depths

# 创建一个布局对象，将树状图显示为垂直结构
layout = ig.Layout([(i, -d) for i, d in enumerate(depths)])

# 将树状图绘制到屏幕上
visual_style = {"vertex_label": g.vs.indices,
                "vertex_color": "white",
                "edge_color": "gray",
                "vertex_size": 30,
                "vertex_label_dist": 1,
                "vertex_label_size": 10,
                "bbox": (400, 400),
                "margin": 20,
                "background": "white"}
ig.plot(g, "tree.png", layout=layout, **visual_style)
