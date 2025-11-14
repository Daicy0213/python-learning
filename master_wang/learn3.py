import igraph as ig


def dfs(graph, v, visited, parent, traversal_tree):
    visited[v] = True
    for u in graph.neighbors(v):
        if not visited[u]:
            print(traversal_tree)
            # traversal_tree.add_vertex(u)

            print(traversal_tree)
            # if parent is not None:
            #    traversal_tree.add_edge(parent, u)
            # dfs(graph, u, visited, traversal_tree.vs[-1].index, traversal_tree)

            traversal_tree.add_edge(v, u)  # 这里总出错，原因是当以root进入dfs时，第一个增加的边是root-->-1不能加入图
            print("sss22222")
            print(traversal_tree)
            print("ssss")
            dfs(graph, u, visited, traversal_tree.vs[-1].diff, traversal_tree)


def traverse_dfs(graph, root):
    traversal_tree = ig.Graph()
    # traversal_tree.add_vertex(root)
    # 这里直接增加travel tree顶点的数量
    traversal_tree.add_vertices(5)
    print(traversal_tree)

    dfs(graph, root, [False] * graph.vcount(), -1, traversal_tree)
    print(traversal_tree)
    return traversal_tree


# 创建一个简单图
g = ig.Graph()
g.add_vertices(5)
g.add_edges([(0, 1), (0, 2), (1, 3), (1, 4)])

# 从节点0开始进行深度优先遍历
traversal_tree = traverse_dfs(g, 0)
# TODO  this is a test
# 保存遍历树的图像 ok
traversal_tree.vs['label'] = traversal_tree.vs.indices
traversal_tree.write_svg('dfs_traversal_tree.svg')
vertex_labels = [str(i) for i in range(len(g.vs))]

layout = g.layout("kk")
visual_style = {"vertex_label": vertex_labels,
                "vertex_size": 30,
                "edge_width": 1,
                "layout": layout,
                "margin": 20}
ig.plot(traversal_tree, **visual_style, bbox=(300, 300), target="bfs_tree.png")

# 1记录每一个点的状态1st_x  st_x=0(unvisited ) ,1 ,2
# 2dep_x
# 3cv_x
# 4parent_x

# 列表推导(List Comprehension) 是一种数学家用来实现众所周知标记集合的Python方式
st = [0 for i in range(100)]
print(st)
dep = [0 for i in range(100)]

cv = [0 for i in range(100)]
pare = [0 for i in range(100)]
