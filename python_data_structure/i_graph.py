"""有向图
使用邻接表来实现图
"""


class Vertex:
    """顶点类 Vertex
    """

    def __init__(self, key):
        self.id = key  # 顶点的id
        self.connectedTo = {}  # 相邻的顶点及对应权值

    def add_neighbor(self, nbr, weight=0):
        """顶点添加相邻顶点
        nbr: 相邻节点的id
        weight: 边的权重
        """
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def get_connections(self):
        """获取节点的所有连接, 返回一个dict
        """
        return self.connectedTo.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    """图类 Graph
    """

    def __init__(self):
        self.vert_list = {}  # 包含图中所有顶点
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vert_list

    def add_edge(self, f, t, weight=0):
        """添加边
        f: 源顶点
        t: 终点节点
        """
        if f not in self.vert_list:
            self.add_vertex(f)
        if t not in self.vert_list:
            self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], weight)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())


if __name__ == '__main__':
    g = Graph()
    for i in range(10):
        g.add_vertex(i)
    print(g.vert_list)

    # 添加的图为 min-cut作业中的钻石图
    g.add_edge(0, 1, 1)
    g.add_edge(0, 2, 2)
    g.add_edge(0, 3, 3)
    g.add_edge(0, 4, 4)
    g.add_edge(1, 5, 2)
    g.add_edge(2, 6, 3)
    g.add_edge(3, 7, 2)
    g.add_edge(4, 8, 2)
    g.add_edge(5, 9, 1)
    g.add_edge(6, 9, 2)
    g.add_edge(7, 9, 3)
    g.add_edge(8, 9, 4)

    for v in g:
        for w in v.get_connections():
            print("(%s , %s)" % (v.get_id(), w.get_id()))
