import numpy as np
import networkx as nx

def synthetic_powerLaw(n, a=2, kmin=1, seed=None):

    rng = np.random.default_rng(seed)

    degrees = []

    # generate power-law degrees
    for i in range(n):
        u = rng.uniform()
        k = round(np.e ** (np.log(u * (kmin ** (1 - a))) / (1 - a)))
        while(k > n):
            u = rng.uniform()
            k = round(np.e ** (np.log(u * (kmin ** (1 - a))) / (1 - a)))
        degrees.append(k)

    # sum of degree must be divisible by 2
    if sum(degrees) % 2 != 0:
        degrees[rng.integers(n)] += 1

    degrees.sort(reverse=True)

    # assign degree to nodes
    available_nodes = set()
    for i in range(n):
        available_nodes.add(i)

    # build graph
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for source in range(n):
        
        if source in available_nodes:
            available_nodes.remove(source)

        degree = degrees[source] - G.degree[source]
        degree = min(degree, len(available_nodes))
        targets = rng.choice(list(available_nodes), degree, replace=False)

        G.add_edges_from(zip([source] * degree, targets))

        for target in targets:
            # fulfill target degree, cannot be chosen anymore
            if G.degree[target] == degrees[target]:
                available_nodes.remove(target)

    G_degrees = [node_degree_pair[1] for node_degree_pair in G.degree]

    return G, np.sum(abs(np.array(G_degrees) - np.array(degrees)))
