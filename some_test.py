import networkx as nx


nodes_index = [1, 2]
edges = [(1, 2)]

g = nx.Graph()
g.add_nodes_from(nodes_index)
g.add_edges_from(edges)
nodes = g
# for v in g.nodes:
#     print(v)
C = nx.constraint(g, [1])
print(C)