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
        *   pattern is an array of -1 or 1 e.g. [-1, 1, -1, 1, 1]
        *   nodes states are either 1 or -1    
        *   weights is a NxN matrix [[node_1_weights], ..., [node_N_weights]]
    '''

    def __init__(self, *pattern):
        self.pattern = pattern  # list of nodes in network
        
        # conditions for Hopfield network
        N = len(self.pattern)
        self.weights = np.zeros(shape=(N,N), dtype=int)  # NxN matrix
        for i in range(N):
            for j in range(N):
                if i == j:  # no pseudo edges
                    self.weights[i][i] = 0
                else:  # symmetric weights and satisfy Hebbian rule
                    self.weights[i][j] = self.pattern[i] * self.pattern[j]
                    self.weights[j][i] = self.pattern[i] * self.pattern[j]

    def __str__(self):
        output_str = ''
        for node in self.nodes:
            output_str += str(node.state) + '  '
        return output_str

    def run(*input_states):
        # current states
        input_states = []
        for i in range(len(input_states)):
            self.states.append(input_states[i].state)

        assert len(input_states) == len(self.pattern)
        for generation in range(100):
            print 


    def next_generation():  # updates asynchronously
        for node_num, node in enumerate(self.nodes):
            node_weights = self.weights[node_num]
            self.states[node_num] = self.nodes[node_num].output(weights, self.states)



if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(-1)
    node3 = Node(1)

    hnet = HopfieldNetwork(node1, node2, node3)

    print hnet





