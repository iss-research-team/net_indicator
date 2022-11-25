import math

import networkx as nx

'''
现有指标
constraint，effective_size，efficiency，clustering_coefficient，degree_centrality，between_centrality，closeness_centrality，eigenvector_centrality
degree_centralization，betweenness_centralization，closeness_centralization, pagerank, grade_degree, ego_network_size
density，clustering_global
modularity，get_cluster_neighbor，cluster_degree，cluster_mediation
'''

def degree(graph, weight=False):
    if weight:
        return nx.degree(graph, weight='weight')
    else:
        return nx.degree(graph)


def constraint(graph, weight=False):
    """
    返回图中所有节点的约束度，以字典表示
    """
    if weight:
        return dict(nx.constraint(graph, weight='weight'))
    else:
        return dict(nx.constraint(graph))


def effective_size(graph, weight=False):
    """
    返回图中所有节点的结构洞有效规模，以字典表示
    """
    if weight:
        return dict(nx.effective_size(graph, weight='weight'))
    else:
        return dict(nx.effective_size(graph, weight='weight'))


def efficiency(graph, weight=False):
    """
    返回图中所有节点的结构洞效率，以字典表示
    """
    if weight:
        eff_dict = effective_size(graph, weight=True)
        nodes_number = graph.number_of_nodes()
        for key, value in eff_dict.items():
            eff_dict[key] = value / nodes_number
    else:
        eff_dict = effective_size(graph)
        nodes_number = graph.number_of_nodes()
        for key, value in eff_dict.items():
            eff_dict[key] = value / nodes_number
    return eff_dict


def grade_degree(graph, weight=False)
    ans = {}
    for node in graph.nodes:
        node_constraint = 0
        node_local_constraint =[]
        node_neighber_cnt = 0
        for node_neighber in set(nx.all_neighbors(graph,node)):
            if weight:
                local_constraint = nx.local_constraint(graph, node, node_neighber, weight)
            else:
                local_constraint = nx.local_constraint(graph, node, node_neighber)
            node_constraint +=local_constraint
            node_local_constraint.append(local_constraint)
            node_neighber_cnt += 1
        if node_neighber_cnt == 1:
            ans[node] = 1
            continue
        eff = node_constraint/node_neighber_cnt
        ans[node] = 0
        for item in node_local_constraint:
            ans[node] += (item/eff) * (math.log(item)*eff)
    return ans

def ego_network_size(graph, weight=False)
    ans = degree(graph, weight)
    for key, value in ans.items():
        ans[key] = value + 1
    return ans
def clustering_coefficient(graph, weight='weight'):
    """
    返回图中所有节点的聚类系数，以字典表示
    """
    if weight:
        return nx.clustering(graph, weight='weight')
    else:
        return nx.clustering(graph)


def pagerank(graph, weight=False)
    if weight:
        return nx.pagerank(graph, weight='weight')
    else:
        return nx.pagerank(graph)

def degree_centrality(graph)
    """
    返回图中所有节点的度中心度，以字典表示
    """
    return nx.degree_centrality(graph)


def between_centrality(graph, weight=False)
    """
    返回图中所有节点的中介中心度，以字典表示
    """
    if weight:
        return nx.betweenness_centrality(graph, weight='weight')
    else:
        return nx.betweenness_centrality(graph)


def closeness_centrality(graph)
    """
    返回图中所有节点的接近中心度，以字典表示
    """
    return nx.closeness_centrality(graph)


def eigenvector_centrality(graph, weight=False)
    """
    返回图中所有节点的特征向量中心度，以字典表示
    """
    if weight:
        return nx.eigenvector_centrality(graph, max_iter=5000, weight='weight')
    else:
        return nx.eigenvector_centrality(graph, max_iter=5000)


def degree_centralization(graph)
    ans_dict = degree_centrality(graph)
    value_max = 0
    value_sum = 0
    value_cnt = 0
    for key, value in ans_dict.items():
        value_sum += value
        value_max = max(value_max, value)
        value_cnt += 1
    return (value_max * value_cnt - value_sum)/(value_cnt - 2)


def betweenness_centralization(graph, weight=False)
    ans_dict = between_centrality(graph, weight=False)
    value_max = 0
    value_sum = 0
    value_cnt = 0
    for key, value in ans_dict.items():
        value_sum += value
        value_max = max(value_max, value)
        value_cnt += 1
    return (value_max * value_cnt - value_sum) / (value_cnt - 1)


def closeness_centralization(graph)
    ans_dict = closeness_centrality(graph)
    value_max = 0
    value_sum = 0
    value_cnt = 0
    for key, value in ans_dict.items():
        value_sum += value
        value_max = max(value_max, value)
        value_cnt += 1
    return (value_max * value_cnt - value_sum) *(2 * value_cnt -3)/ ((value_cnt - 2) * (value_cnt - 1))


def density(graph):
    """
    返回图的密度，以数值表示
    """
    return nx.density(graph)


def clustering_global(graph):
    """
    返回图的聚类系数，以数值表示
    """
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
