import igraph as ig

# 创建一个空的igraph对象
g = ig.Graph()

for i in range(6):
    
    g.add_vertex(i+1)
    print(g.vs)
    print(g)




# 绘制图形
