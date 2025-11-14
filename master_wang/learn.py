#https://python.igraph.org/en/stable/tutorial.html
import igraph as ig
import matplotlib.pyplot as plt

import itertools

#fig,ax = plt.subplots()
## 生成一个scale-free图
#g = ig.Graph.Barabasi(n=10, m=2)
#edges=g.get_edgelist()

## 为每个节点添加标签
#vertex_labels = [str(i) for i in range(len(g.vs))]

## 为每个节点设置颜色
#vertex_colors = ['blue' for _ in range(len(g.vs))]

#ig.plot(g, target=ax, vertex_label=vertex_labels, vertex_label_size=16,
        #vertex_color=vertex_colors, vertex_size=30, edge_width=2)

##ig.plot(g,target=ax)
#plt.savefig("ppppppot.jpg")



#print(edges)
#print("-----")

#for edge in edges:
 #   print(edge)




#first experiment#############
#这是什么函数生成的？g = ig.Graph.Barabasi(n=10, m=2)Generates a graph based on the Barabasi-Albert model.用的什么代码
g=ig.Graph(directed=False) #ok记住需要看看是有向图还是无向图(默认生成的是无向图)
#g.add_vertices(10)
#g.add_edges([(0, 1),(0, 2),(1, 2),(2, 3),(1, 3),(1, 4),(0, 4),(0, 5),(2, 5),(2, 6),(0, 6),(0, 7),(4, 7),(1, 8),(2, 8),(4, 9),(2, 9)])

g.add_vertices(5)
g.add_edges([(0, 1), (0, 2), (1, 3), (1, 4),(3,0)])


print(g)
print(g.is_connected())#记住要去测试这个图是不是连通图

fig,ax = plt.subplots()
edges=g.get_edgelist()

## 为每个节点添加标签
vertex_labels = [str(i) for i in range(len(g.vs))]

## 为每个节点设置颜色
vertex_colors = ['blue' for _ in range(len(g.vs))]

# ig.plot(g, target=ax, vertex_label=vertex_labels, vertex_label_size=16,
# vertex_color=vertex_colors, vertex_size=30, edge_width=2)
#图像需要写png才能输出，jpg似乎不行
ig.plot(g, "first_sf.png", vertex_label=vertex_labels, vertex_label_size=16,
vertex_color=vertex_colors, vertex_size=30, edge_width=2)

##ig.plot(g,target=ax)
#plt.savefig("first_sf.jpg")


print("ssss",g.assortativity_degree())
print("points",g.articulation_points())



#可以通过属性来记录图的属性
#(1)计算网络连通性
#no,先不抽象成方法，需要抽象的是遍历每一条可以增加的边然后试出来哪一条能够最大化优化这个把计算网络连通性抽象成方法 输入函数是图，输出函数是网络连通性
v_co=g.vertex_disjoint_paths() 
print("vertex_connectivity:",v_co)

#(2)计算边的连通性
e_co=g.edge_disjoint_paths()
print("edge_connectivity:",e_co)

#算完自己算一遍，免得算的和想的不一样
#(3)计算diameter，diameter与robustness成反比
diameter=g.diameter(directed=False)
print("diameter:",diameter)

#(4)计算average_distance   note：增加一个边，有可能average_distance会减小，减小是好的
av_dis=g.average_path_length()
print("average_distance",av_dis)




#求g的补集
g_complement=g.complementer(loops=False)
print(g_complement)
print("--------------------------------------------------------")
print(g_complement.get_edgelist())
missing_edges=g_complement.get_edgelist()






#--------------------------------------------------------------
#missing_edges = list(itertools.combinations(g.vs, 2))
#edge-connectivity
best_edge = None
best_e_co = 0
print(missing_edges)
print("-0----------")

#diameter(看看是有向图还是无向图)
best_edge_di=None
best_di_e=0

#g.average_path_length()
best_edge_average_distance=None
best_average_distance=0

for e in missing_edges:
    print(e)
    #g.add_edge(e[0].index,e[1].index)
    g.add_edge(e[0],e[1])
    e_co = g.edge_disjoint_paths()
    if e_co > best_e_co:
        best_e_co = e_co
        best_edge = e
        
    di_e=g.diameter(directed=False)    
    if di_e> best_di_e:
        best_di_e= di_e
        best_edge_di=e    
    
    average_distance=g.average_path_length()    
    if average_distance> best_average_distance:
        best_average_distance = average_distance    
        best_edge_average_distance=e
        
    g.delete_edges(e)
    
    
    

print("The best edge to add is: ", best_edge)
print("It increases the edge-disjoint paths by: ", best_e_co)


print("The best edge for diameter to add is  ", best_edge_di)
print("It increases the edge-disjoint paths by: ", best_di_e)

print("The best edge for average_distance to add is  ",  best_edge_average_distance)
print("It increases the best_average_distance: ", best_average_distance)

# 计算最小割
min_cuts = g.mincut(0,3)
#TODO:先用这个算一下  可能是边的序号？
print("mincut",min_cuts)

# 遍历所有点对，输出最小割值和割集
# 遍历所有最小割，输出最小割值和割集
for i, cut in enumerate(min_cuts):
    
    print("Min-cut", i + 1)
    for j, component in enumerate(cut):
        print("Component", j + 1)
        print("Min-cut value:", component.value)
        print("Min-cut set:", component.partition)
        print("===")

# 将图对象转换为表格
table = ig.summary(g)
print(table)

print("ss")




#what we do
#1利用igraph生成所有的节点对的最小割   也就是说从具体细节关注（如果我直接算出全局的最小，有用吗？没用，我需要的是哪里最小
# ）  关注每一个点的最小割。

#1 detail  (1)生成原图所有节点对的最小割每一个都算出来列一个表格，然后增加边后再列一个表格，看哪个最小割能够变大。


#2利用treemaster生成预处理的含有割值的树

#3不行还是得找数学方法  如果没有数学方法，就像盲人摸象

#g=ig.Graph()
#g.add_vertices(6)
#g.add_edges([(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 5), (5, 3)])
#ig.plot(g,target=ax)
#plt.savefig("ppppppot.jpg")



#增加图
#生成一个度数为几，什么类型的图 去论文里面找
#这必须是一个固定的图，只能一次生成后然后保存


#fsln的图分别是 1random graph   2 scale-free图  


##老师生成Erdős-Rényi随机图
##Erdős-Rényi随机图是一个简单的随机图模型，它的生成方式是在n个节点中，每对节点有一定的概率p相连，可以使用igraph库的erdos_renyi_game函数来生成这种随机图。例如，生成一个包含10个节点，每对节点有0.3的概率相连的随机图，可以使用以下代码：
#g = ig.Graph.Erdos_Renyi(n=10, p=0.3)
#ig.plot(g,target=ax)
#plt.savefig("sf10_3")
#print(g)


#n=100  m=10 也就是说我想生成100个顶点，一共10个边的图，我计算概率p
#n=int(n)   p=2.0*10/(100*100)  这个概率就是说相当于100个去连另外
#100个，每个连接的概率是p，老师这边用的是p  
#还要确定它一定是一个连通图，因为如果不是连通图就无法深度遍历

#在哪里把0顶点去了呢





#去看看老师是怎么生成的











#a=[5,7,6,3,4,1,2]
#b=sorted(a) #使用sorted，保留原列表，不改变列表a的值
#print(a)
#print(b)



#L=[('b',2),('a',1),('c',3),('d',4)]
##newL=sorted(L,cmp=lambda x,y:cmp(x[1],y[1]))
#newL=sorted(L, key=lambda x: x[1])
#print(L)
#print(newL)


## 4、按年龄升序
#students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
#sorted(students, key=lambda s: s[2])
## 结果：
##[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
## 5、按年龄降序
#sorted(students, key=lambda s: s[2], reverse=True)
## 结果：
##[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]


## ===========一般用法：===========
## 1、过滤出列表中的所有奇数
#def is_odd(n):
	#return n % 2 == 1
		 
#newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#print(list(newlist))
#print(newlist)
## 结果： [1, 3, 5, 7, 9]

## ===========匿名函数用法：===========
## 2、将列表[1, 2, 3]中能够被3整除的元素过滤出来
#newlist = filter(lambda x: x % 3 == 0, [1, 2, 3])
#print(list(newlist))
## 结果： [3]


##Looking up vertices by names
