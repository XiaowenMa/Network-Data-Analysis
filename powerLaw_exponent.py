import numpy as np
import itertools

def powerLaw_exponent(degrees, kmin=1):
    '''
    Estimate the power law exponent using the CCDF
    of degree and 

    expected input: a list of degree of each node in the graph

    '''

    # get sorted degree distribution
    degrees_set = list(set(degrees))
    degrees_set.sort()
    degrees_proportion = [degrees.count(degree)/len(degrees) for degree in degrees_set]


    # get CCDF
    culmulative_density = degrees_proportion[:] # copy by value, not reference
    culmulative_density.reverse()

    culmulative_density = list(itertools.accumulate(culmulative_density))
    culmulative_density.reverse()

    culmulative_density = np.log(culmulative_density)

    # Find x = log(k / kmin)
    X = np.ones((len(degrees_set), 2))
    for i in range(len(degrees_set)):
        X[i][0] = np.log(degrees_set[i] / kmin)

    # solve least square problem
    m, _ = np.linalg.lstsq(X, culmulative_density, rcond=None)[0]

    # return exponent
    return 1-m