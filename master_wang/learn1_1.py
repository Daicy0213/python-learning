import igraph as ig




print("ff")
g= ig.Graph()
g.add_vertices(5)
g.add_edges([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 2)])
    
    
    
#XXX使用这个all_st_mincuts显示需要有向图？可以将有向图转成无向图    
#g.es['capacity'] = [1, 2, 3, 4, 5, 6]

## Define the source and target vertices
#source = 0
#target = 3

## Find all minimum cuts between the source and target vertices
#cuts = g.all_st_mincuts(source, target, capacity='capacity')

## Print the edges of each minimum cut
#for cut in cuts:
    #edges = g.get_edgelist()
    #cut_edges = [edges[i] for i in cut.partition[0]]
    #print(f"Minimum cut value: {cut.value}, cut edges: {cut_edges}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#TODO  快ok了
# Find the minimum cut of the graph
#hello: Cut(<igraph. Graph object at 0x7fa7a18629a8>,2.0,[2,3],[e,1,2,4])
hello = g.mincut(0, 3)
#mincut_value, partition = g.mincut(0, 3)
    
edges=g.get_edgelist()
    
#identify the edges that cross the minimum cut
cut_edges=[]
    
    
# for i,edge in enumerate(edges):
#     if partition[0] == edges[i][0]:
#             if partition[1]==edges[i][1]:
#                 cut_edges.append(edge)
for i, edge in enumerate(edges):
    if edge[0] in list(partition[0]) and edge[1] in list(partition[1]):
        cut_edges.append(edge)
    
    
    
# Print the minimum cut and the edges that belong to it
print(f"The minimum cut value is {mincut_value}")
print(f"The edges that belong to the minimum cut are {cut_edges}")
    
    
    
