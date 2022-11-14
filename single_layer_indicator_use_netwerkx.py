import networkx as nx:


# 单个节点约束度,返回字典
def constraint(graph):
    return nx.constraint(graph)

# 单个节点结构洞有效规模，返回字典
def effective_size(graph)
    return nx.effective_size(graph)

# 单个节点结构洞效率，返回字典
def efficiency(graph):
    eff_dict = effective_size(graph)
    nodes_number = graph.number_of_nodes()
    for key, value in eff_dict:
        eff_dict[key] = value / nodes_number
    return eff_dict

# 单个节点聚类系数,返回字典
def clustering_coefficient(graph):
    return nx.clustering(graph)

# 整网密度，返回值
def density(graph):
    return nx.density(graph)

# 整网聚类系数，返回值
def clustering_global(graph):
    return nx.transitivity(graph)
