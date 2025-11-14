import igraph

# create a graph
g = igraph.Graph.Famous("petersen")

# iterate over all pairs of vertices
for s in range(g.vcount()):
    for t in range(s+1, g.vcount()):
        # calculate the minimum cut
        cut_value, partition = g.minimum_cut(s, t)

        # find the edges that cross the cut
        cut_edges = [(i, j) for i in partition[0] for j in partition[1] if g.are_connected(i, j)]

        # print the cut edges
        print(f"Minimum cut between vertices {s} and {t}: {cut_edges}")
