import networkx as nx


nodes_index = [1, 2]
edges = [(1, 2)]

g = nx.Graph()
g.add_nodes_from(nodes_index)
g.add_edges_from(edges)
constraint_dict = nx.constraint(g)
print(constraint_dict)
print(nx.clustering(g))
print(nx.transitivity(g))
print(g.number_of_nodes())
print(nx.density(g))
print(nx.effective_size(g))