import numpy as np

class Node():
    '''
        weights is a 1D array [w_1, w_2, ..., w_N]
    '''

    def __init__(self, state):
        self.state = state

    def sgn(self, num):
        if num < 0:
            return -1
        return 1  # >= 0

    def output(self, weights, inputs):  # sgn of field (h)
        return self.sgn(np.dot(weights, inputs))


class HopfieldNetwork():
    '''
        weights is a NxN matrix [[node_1_weights], ..., [node_N_weights]]
    '''

    def __init__(self, *nodes):
        self.nodes = nodes  # list of nodes in network
        
        # conditions for Hopfield network
        N = len(nodes)
        self.weights = np.zeros(shape=(N,N), dtype=int)  # NxN matrix
        for i in range(N):
            for j in range(N):
                if i == j:  # no pseudo edges
                    self.weights[i][i] = 0
                else:  # symmetric weights and satisfy Hebbian rule
                    self.weights[i][j] = nodes[i].state * nodes[j].state
                    self.weights[j][i] = nodes[i].state * nodes[j].state


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(-1)
    node3 = Node(1)

    hnet = HopfieldNetwork(node1, node2, node3)

    print hnet.weights





