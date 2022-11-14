import json
import networkx as nx
import method
from single_layer_indicator_use_netwerkx import *


json_file_path = "where it locate"
graph = method.net_build(json_file_path)
graph_density = density(graph)
json_store_path = "where it store"
json.dump(graph_density, open(json_store_path, 'w', encoding='utf-8'),)