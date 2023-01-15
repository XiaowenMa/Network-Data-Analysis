import networkx as nx
from networkx.utils import py_random_state
import numpy as np

def KH_model(n, m, Pt=0, seed=None, initial_graph=None):
    '''
    Implementation of Petter Holme and Beom Jun Kim's
    scale-free network with tunable clustering. 

    Dependency: NetworkX https://networkx.org/
                NumPy https://numpy.org/doc/stable/index.html

    Original Paper: https://arxiv.org/pdf/cond-mat/0110452.pdf
    '''

    np.random.seed(seed)

    #initial error checking and setup taken from: 
    #https://networkx.org/documentation/stable/reference/generated/networkx.generators.random_graphs.barabasi_albert_graph.html
    if m < 1 or m >= n:
        raise nx.NetworkXError(
            f"Barabási–Albert network must have m >= 1 and m < n, m = {m}, n = {n}"
        )

    if initial_graph is None:
        # Default initial graph : star graph on (m + 1) nodes
        G = nx.star_graph(m)
    else:
        if len(initial_graph) < m or len(initial_graph) > n:
            raise nx.NetworkXError(
                f"Barabási–Albert initial graph needs between m={m} and n={n} nodes"
            )
        G = initial_graph.copy()

    # List of existing nodes, with nodes repeated once for each adjacent edge; used for selecting edges
    repeated_nodes = [n for n, d in G.degree() for _ in range(d)]
    
    # main loop for adding one vertex and m edges each iteration
    source = len(G)
    while source < n:
        
        # generate all potential nodes to connect
        potential_targets = set()
        while len(potential_targets) < m:
            x = np.random.choice(repeated_nodes)
            potential_targets.add(x)
        potential_targets = list(potential_targets)
        target_idx = 0

        v_to_connect = set() # track connected node to avoid duplicate
        prev_v = None # track the vertex 

        # add edges
        while len(v_to_connect) < m:

            # first step must be PA
            if prev_v == None:
                prev_v = potential_targets[target_idx]
                target_idx += 1
                v_to_connect.add(prev_v)
            else:

                if(np.random.uniform() > Pt):

                    #avoid duplicate; since we generated m vertices, no worry about out-of-bound
                    while potential_targets[target_idx] in v_to_connect:
                        target_idx += 1

                    prev_v = potential_targets[target_idx]
                    target_idx += 1
                    v_to_connect.add(prev_v)
                else:
                    # get valid neighbors to connect to; need to check for duplicate
                    neighbors = [n for n in G[prev_v] if n not in v_to_connect and n != source]

                    # special case: no valid neighbors, perform a PA step instead
                    if(len(neighbors) == 0):
                        prev_v = None
                        continue
                    
                    # randomly select a neighbor
                    v_to_connect.add(np.random.choice(neighbors))

            targets = list(v_to_connect)
            # Add edges to m nodes from the source.
            G.add_edges_from(zip([source] * m, targets))
            # Add one node to the list for each new edge just created.
            repeated_nodes.extend(targets)
            # And the new node "source" has m edges to add to the list.
            repeated_nodes.extend([source] * m)

        source += 1

    return G