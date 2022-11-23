import networkx as nx


# 单个节点约束度,返回字典
def constraint(graph, weight=False):
    """
    说明
    :param graph:
    :return:
    """
    if weight:
        return dict(nx.constraint(graph, weight='weight'))
    else:
        return dict(nx.constraint(graph))


# 单个节点结构洞有效规模，返回字典
def effective_size(graph):
    return dict(nx.effective_size(graph, weight='weight'))


# 单个节点结构洞效率，返回字典
def efficiency(graph):
    eff_dict = effective_size(graph)
    nodes_number = graph.number_of_nodes()
    for key, value in eff_dict.items():
        eff_dict[key] = value / nodes_number
    return eff_dict


# 单个节点聚类系数,返回字典
def clustering_coefficient(graph):
    return nx.clustering(graph, weight='weight')


# 整网密度，返回值
def density(graph):
    return nx.density(graph)


# 整网聚类系数，返回值
def clustering_global(graph):
    return nx.transitivity(graph)


# Modularity
def modularity(graph, communities, weight=False):
    if weight:
        return nx.algorithms.community.modularity(graph, communities, weight='weight')
    else:
        return nx.algorithms.community.modularity(graph, communities)


def get_cluster_neighbor(graph, c):
    """
    计算子群的邻居
    :param graph:
    :param c:
    :return:
    """
    n_neighbor_list = [set(graph.neighbors(node)) for node in c]
    c_neighbor = set()
    for _ in n_neighbor_list:
        c_neighbor = c_neighbor.union(_)
    return c_neighbor


def cluster_degree(graph, communities):
    """
    将子群看做一个节点计算子群的度
    :return:
    """
    num_cluster = len(communities)
    answer = dict()
    for i in range(num_cluster):
        degree = 0
        c_neighbor = get_cluster_neighbor(graph, communities[i])
        for j in range(num_cluster):
            if i == j:
                continue
            degree += len(c_neighbor & communities[j])
        answer[i] = degree

    return answer


def cluster_mediation(graph, communities, weight=False):
    """
    参考文献：
    Gould, R. V. and R. M. Fernandez (1989).
    "Structures of Mediation: A Formal Approach to Brokerage in Transaction Networks."
    Sociological Methodology 19: 89-126.
    每个节点有五个值
    wi,wo,boi,bio,bo

    :return:
    """
    num_node = graph.number_of_nodes()
    node_list = list(graph.nodes)

    n2c = dict()
    for i, c, in enumerate(communities):
        for n in c:
            n2c[n] = i

    node_wi = dict(zip([i for i in range(num_node)], [0 for i in range(num_node)]))
    node_wo = dict(zip([i for i in range(num_node)], [0 for i in range(num_node)]))
    node_boi = dict(zip([i for i in range(num_node)], [0 for i in range(num_node)]))
    node_bio = dict(zip([i for i in range(num_node)], [0 for i in range(num_node)]))
    node_bo = dict(zip([i for i in range(num_node)], [0 for i in range(num_node)]))

    for j in node_list:
        for i in node_list:
            if i == j:
                continue
            for k in node_list:
                if k == j:
                    continue
                if not graph.has_edge(i, j) or not graph.has_edge(j, k):
                    continue
                mi = n2c[i]
                mj = n2c[j]
                mk = n2c[k]
                if weight:
                    w = graph[i][j]['weight'] * graph[j][k]['weight']
                else:
                    w = 1

                if mi == mj == mk:
                    node_wi[j] += w
                elif mi == mk != mj:
                    node_wo[j] += w
                elif mi == mj != mk:
                    node_bio[j] += w
                elif mi != mj == mk:
                    node_boi[j] += w
                else:
                    node_bo[j] += w

    return node_wi, node_wo, node_bio, node_boi, node_bo
