import json
import networkx as nx

# 根据json数据构建networkx,graoh网络
def net_build(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as f:
        net_data = json.loads(f.read())

    num_nodes = len(net_data['nodes'])
    nodes_index = net_data['nodes']
    num_edges = len(net_data['links'])
    print('节点数：', num_nodes, '连接数：', num_edges)
    names = [k for k in range(num_nodes)]
    edges = [(net_data['links'][k]['source'], net_data['links'][k]['target']) for k in range(num_edges)]

    g = nx.Graph()
    g.add_nodes_from(nodes_index)
    g.add_edges_from(edges)

    return g