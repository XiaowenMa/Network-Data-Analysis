import numpy as np
import networkx as nx

def cluster_synthetic_powerLaw(n, a=2, kmin=1, seed=None, Pt=0):

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

    available_nodes = set()
    for i in range(n):
        available_nodes.add(i)

    neighbor_link = [min(round(degree * Pt), degree - 1) for degree in degrees]
    random_link = [a - b for a, b in zip(degrees, neighbor_link)]

    # build graph
    G = nx.Graph()
    G.add_nodes_from(range(n))

    # add random link
    for source in range(n):
        
        degree = random_link[source] - G.degree[source]
        degree = min(degree, len(available_nodes))
        if(degree <= 0): 
            continue

        available_nodes.remove(source)
        targets = rng.choice(list(available_nodes), degree, replace=False)
        available_nodes.add(source)

        G.add_edges_from(zip([source] * degree, targets))

        for target in targets:
            # fulfill target degree, cannot be chosen anymore
            if G.degree[target] == degrees[target]:
                available_nodes.remove(target)

    # add neighboring links
    for source in range(n):
        
        if source in available_nodes:
            available_nodes.remove(source)
        else:
            continue

        if(G.degree[source] >= degrees[source]):
            continue

        degree = neighbor_link[source] 


        if(degree <= 0): 
            continue
        
        neighbors = []
        for node in G[source]:
            for node2 in G[node]:
                if node2 in available_nodes:
                    neighbors.append(node2)
        
        degree = min(len(neighbors), degree)
        targets = rng.choice(list(neighbors), degree, replace=False)

        G.add_edges_from(zip([source] * degree, targets))

        for target in neighbors:
            # fulfill target degree, cannot be chosen anymore
            if G.degree[target] == degrees[target] and target in available_nodes:
                available_nodes.remove(target)

    G_degrees = [node_degree_pair[1] for node_degree_pair in G.degree]

    return G, np.sum(abs(np.array(G_degrees) - np.array(degrees)))
