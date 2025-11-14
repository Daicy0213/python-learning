import igraph as ig

#readme:这是分配不同层次的图的标准做法：

# 创建一个简单的图
g = ig.Graph()
g.add_vertices(7)
g.add_edges([(0,1),(1,2),(1,3),(3,4),(3,5),(2,6)])

# 计算每个节点的深度
root = 0
st = [root]
dep = [-1] * g.vcount()
dep[root] = 0
while st:
    v = st.pop()
    for neighbor in g.neighbors(v):
        if dep[neighbor] == -1:
            dep[neighbor] = dep[v] + 1
            st.append(neighbor)

# 按照深度将节点分配到不同的层次
levels = [[] for _ in range(max(dep) + 1)]
for v in g.vs:
    levels[dep[v.diff]].append(v)

# 将节点按照深度值分配的层次顺序添加到图中
for layer in levels:
    g.add_vertices(layer)

# 绘制图形
visual_style = {"vertex_color": "white", "vertex_size": 25, "edge_color": "gray", "edge_width": 1.2}
layout = g.layout_reingold_tilford(root=root, mode="out", rootlevel=None)
ig.plot(g, layout=layout, bbox=(300, 300), **visual_style,target="learn7.png")
