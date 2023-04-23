"""有向图
使用邻接表来实现图
"""
from e_queue import Queue
from enum import Enum
from d_stack import Stack


class State(Enum):
    """关于顶点类中state的枚举类"""
    Untraversed = 0
    Traversing = 1
    Traversed = 2


class Vertex:
    """顶点类 Vertex
    """

    def __init__(self, key):
        self.id = key  # 顶点的id
        self._state = State.Untraversed  # 用于遍历的状态, 详见State枚举类
        self._depth = 0  # 遍历生成树的深度
        self.connectedTo = {}  # 相邻的顶点及对应权值

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, value):
        self._depth = value

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

    def __init__(self, directed=True):
        self.vert_list = {}  # 包含图中所有顶点
        self._directed = directed
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

        if not self._directed:  # 如果是无向图, 则添加双向的边
            self.vert_list[t].add_neighbor(self.vert_list[f], weight)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())


def reset_vertex(g):
    """重置顶点的深度和遍历标记的属性
    """
    for v in g:
        v.depth = 0
        v.state = State.Untraversed


def bfs(g, start):
    """宽度优先遍历
    g: 图类(class Graph)
    start: 开始顶点的id
    """
    reset_vertex(g)  # 重置遍历属性
    start = g.get_vertex(start)
    start.depth = 0
    vq = Queue()
    vq.enq(start)
    while vq.size() > 0:
        current = vq.deq()
        for nbr in current.get_connections():
            if nbr.state is State.Untraversed:
                nbr.state = State.Traversing
                nbr.depth = current.depth + 1
                vq.enq(nbr)
        current.state = State.Traversed
        print(current)


def dfs_stack(g, start):
    """深度优先遍历
    使用栈而非递归的形式进行遍历, 优点是相比递归, 栈的规模更加可估计
    g: 图类(class Graph)
    start: 开始顶点的id

    注意:
     State.Untraversed 表示即未入栈 也未访问
     State.Traversed 表示已经出栈且访问过
    """
    reset_vertex(g)  # 重置遍历属性
    start = g.get_vertex(start)
    start.depth = 0
    vs = Stack()  # 初始化顶点栈
    vs.push(start)
    while vs.size() > 0:
        current = vs.pop()
        if current.state is not State.Traversed:
            current.state = State.Traversed
            print(current)
        for nbr in current.get_connections():
            if nbr.state is State.Untraversed:
                vs.push(nbr)


def dfs_rec(g, start):
    """使用递归进行dfs遍历
    g: 图类(class Graph)
    start: 开始顶点的id
    """
    reset_vertex(g)  # 重置遍历属性
    current = g.get_vertex(start)
    for vertex in current.get_connections():
        if vertex.state is not State.Traversed:
            _dfs_rec_travel(vertex)


def _dfs_rec_travel(current):
    """递归函数
    v: 顶点类(class Vertex)
    """
    current.state = State.Traversed
    print(current)
    for vertex in current.get_connections():
        if vertex.state is not State.Traversed:
            _dfs_rec_travel(vertex)


if __name__ == '__main__':
    # 生成一个无向图
    g = Graph(directed=False)
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

    print("图的连接状态为:")
    for v in g:
        for w in v.get_connections():
            print("(%s , %s)" % (v.get_id(), w.get_id()))

    # 使用bfs由0点开始遍历
    print('bfs test:')
    bfs(g, 0)

    # 使用栈来进行dfs, 由0开始遍历
    print('dfs_stack test:')
    dfs_stack(g, 0)

    print('dfs_rec test:')
    # 使用递归来进行dfs, 由4开始遍历
    dfs_rec(g, 4)
