
import networkx as nx


def build_graph(rules):
    G = nx.DiGraph()
    for condition, result in rules:
        G.add_edge(condition, result)
    return G
