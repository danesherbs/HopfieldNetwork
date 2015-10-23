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
        *   pattern is the set of states (1 or -1) that the network will remember
        *   weights is a NxN matrix [[node_1_weights], ..., [node_N_weights]]
    '''

    

    def __init__(self, *pattern):

        def sgn(num):
            if num < 0:
                return -1
            return 1  # >= 0

        self.state = map(lambda x: sgn(x), np.random.randint(-2, 2, size=len(pattern)))

        # conditions for Hopfield network
        N = len(pattern)
        self.weights = np.zeros(shape=(N,N), dtype=int)  # NxN matrix
        for i in range(N):
            for j in range(N):
                if i == j:  # no pseudo edges
                    self.weights[i][i] = 0
                else:  # symmetric weights and satisfy Hebbian rule
                    self.weights[i][j] = pattern[i] * pattern[j]
                    self.weights[j][i] = pattern[i] * pattern[j]

    # def __str__(self):
    #     output_str = ''
    #     for state in pattern:
    #         output_str += str(state) + '  '
    #     return output_str

    def run(*input_states):
        
        # initialise states
        input_states = []
        for i in range(len(input_states)):
            self.states.append(input_states[i].state)

        # see how network evolves over generations
        for generation in range(100):
            print "Hey!"
            next_generation()


    def next_generation():  # updates asynchronously
        for node_num, node in enumerate(self.nodes):
            node_weights = self.weights[node_num]
            self.states[node_num] = self.nodes[node_num].output(weights, self.states)



if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(-1)
    node3 = Node(1)

    hnet = HopfieldNetwork([1,1,1])

    print hnet





