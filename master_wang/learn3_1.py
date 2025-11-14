import igraph as ig

#note:那么直接通过深度遍历也可以，直接深度遍历，只不过把cv值借用一下，这个过程和形成边不同  也就是不要回边
#为什么我们直接借用包不行呢，因为有回边，如果没有回边就可以有树结构。或者重新遍历，但是要保证遍历顺序一样
#TODO:再找找那个树形结构的包，如果不行就重新遍历，把cv值放上去，然后自己想办法
#TODO：增加连接的边
#TOD

#TODO  将3_2的结合到3_1然后


#TODO:目前做的是将所有的边都放到travel_tree，然后深度遍历树利用new_travelsal?有必要吗   可以优化，暂时不优化




def dfs(graph, v, st, dep,cv,pare, traversal_tree):
    #断言根节点的状态为0
    
    #设置v的状态为1
    st[v]=1
    #深度值是有一个起点，那么这个起点在main里确认，那么这里就不用确认
    #cv值在哪里初始化？
    
    #pare值怎么办？在main里确认，这里只用确认u的parent是v
    
    for u in graph.neighbors(v):
        if (st[u]==0):
            dep[u]=dep[v]+1
            pare[u]=v
            traversal_tree.add_edge(v,u)
            dfs(graph, u, st, dep, cv,pare, traversal_tree)
            cv[v]=cv[v]+cv[u]
            
            print(traversal_tree)
            #traversal_tree.add_vertex(u)
            
            #if parent is not None:
            #    traversal_tree.add_edge(parent, u)
            #dfs(graph, u, visited, traversal_tree.vs[-1].index, traversal_tree)
        if (st[u]==1):
            #其实这里不是加1,而是加u,v边的容量
            cv[u]=cv[u]-1
            cv[v]=cv[v]+1
            if(pare[v]!=u):
                traversal_tree.add_edge(v, u)   #这里总出错，原因是当以root进入dfs时，第一个增加的边是root-->-1不能加入图 
            print("sss22222")
            print(traversal_tree)
            print("ssss")
    
    print(cv)
    st[v]=2

def traverse_dfs(graph, root):
    n=graph.vcount()
    st=[0 for i in range(n)]
    print(st)
    # dep=[0 for i in range(n)]

    cv=[0 for i in range(n)]
    pare=[0 for i in range(n)]
    
    
    traversal_tree = ig.Graph(directed=False)
    #traversal_tree.add_vertex(root)
    #这里直接增加travel tree顶点的数量
    traversal_tree.add_vertices(n)
    print(traversal_tree)
    
    
    
    dfs(graph, root, st,dep, cv,pare, traversal_tree)
    
    
    # 按照深度值将节点分配到不同的层次
    levels = [[] for _ in range(max(dep) + 1)]
    for v in traversal_tree.vs:
        levels[dep[v.diff]].append(v)
    
    #TO
    #为什么要增加new_traversal_tree呢？因为如果直接用原图的话，那么点的数量会溢出
    new_traversal=ig.Graph(directed=False)
    
    # 将节点按照深度值分配的层次顺序添加到图中
    for layer in levels:        
        new_traversal.add_vertices(layer)
        print(new_traversal)
    
    #记住igraph.add_vertex()或者igraph.add_vertices()增加的时候一定要确认括号里是index
    # 还是一个vertex object，者会导致不同。如果增加的是vertex类则大部分不会出错。
    # 增加index的时候有可能会溢出，也就是增加一个点只会在类中增加一个索引
    
    #如何将割值放到图像里面
    
    for i in range(0, len(levels)):
        for v in levels[i]:
            for u in traversal_tree.neighbors(v):
                #if dep[u] == dep[v.index] - 1:
                if dep[u]==dep[v.diff]+1:
                    new_traversal.add_edge(u, v)
                if dep[u]<dep[v.diff]-1:
                    new_traversal.add_edge(u,v)
                #如果两个点的深度相差超过1那么一定是回边，此时需要弄成虚线（），然后呢
                    
    
    print(cv)
    print(new_traversal)
    print("------------")
    return new_traversal

# 创建一个简单图
g = ig.Graph(directed=False)
g.add_vertices(5)
g.add_edges([(0, 1), (0, 2), (1, 3), (1, 4),(3,0)])
#g.add_edges([(0, 1), (1,4), (2, 3), (1, 3),(0,3)])
dep=[0 for i in range(5)]

#g = ig.Graph.Barabasi(n=10, m=2)
#print(g)

# 从节点0开始进行深度优先遍历
traversal_tree = traverse_dfs(g, 0)



# 保存遍历树的图像 ok
#获得所有点的id的办法
traversal_tree.vs['label'] = traversal_tree.vs.indices
#traversal_tree.write_svg('dfs_traversal_tree.svg')
id_labels=[str(i) for i in range(len(traversal_tree.vs))]

vertex_labels = [f'{id_labels[i]}\n{dep[i]}' for i in range(traversal_tree.vcount())]
#vertex_labels = [str(i) for i in range(len(g.vs))]

layout = g.layout("kk")


#这里是能用的
visual_style = {"vertex_label": vertex_labels,
                "vertex_size": 30,
                "edge_width": 1,
                "layout": layout,
                "margin": 20}
ig.plot(traversal_tree, **visual_style, bbox=(1000, 1000),target="bfs_tree.png")


# visual_style = {"vertex_color": "white", "vertex_size": 25, "edge_color": "gray", "edge_width": 1.2}
# layout = g.layout_reingold_tilford(root=0, mode="out", rootlevel=None)
# ig.plot(g, vertex_label=vertex_labels,layout=layout, bbox=(300, 300), **visual_style,target="learn3_1.png")

visual_style = {"vertex_color": "white", "vertex_size": 25, "edge_color": "gray", "edge_width": 1.2}
layout = traversal_tree.layout_reingold_tilford(root=0, mode="out", rootlevel=None)
ig.plot(traversal_tree, vertex_label=vertex_labels,layout=layout, bbox=(300, 300), **visual_style,target="learn3_1.png")


#1记录每一个点的状态1st_x  st_x=0(unvisited ) ,1 ,2
#2dep_x  
#3cv_x 
#4parent_x 

#列表推导(List Comprehension) 是一种数学家用来实现众所周知标记集合的Python方式


#1把st当做全局变量，如果

#用几个图验证下计算的对不对
#利用igraph有了图结构生成深度遍历树  或者回边用虚线也可以  用newbign
#unfold_tree(sources=None, mode=OUT) 

#直接吧数据给gpt，让他提方案