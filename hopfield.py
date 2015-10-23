import numpy as np
import sys

class Node():
    '''
        weights is a 1D array [w_1, w_2, ..., w_N]
    '''

    def __init__(self, state):
        self.state = state

    def __str__(self):
        return str(self.state)

    def sgn(self, num):
        if num < 0:
            return -1
        return 1  # >= 0

    def output(self, weights, inputs):  # sgn of field (h)
        weighted_output = self.sgn(np.dot(weights, inputs))
        self.state = weighted_output
        return weighted_output


class HopfieldNetwork():
    '''
        *   pattern is an array of states (e.g. [1,-1,-1,1]) that the network will remember
        *   weights is a NxN matrix [[node_1_weights], ..., [node_N_weights]]
    '''

    def __init__(self, pattern):

        self.pattern = pattern
        self.N = len(pattern)

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

    def sgn(self, num):
        if num < 0:
            return -1
        return 1  # >= 0

    def asynchronous_update(self, states, nodes):  # updates asynchronously
        for node_num, node in enumerate(nodes):
            print
            print "UPDATE NODE", node_num
            node_weights = self.weights[node_num]
            print "Weights:\t", node_weights
            print "Inputs:\t\t", states
            print "Field:\t\t", self.sgn(np.dot(node_weights, states))
            states[node_num] = nodes[node_num].output(node_weights, states)
        print "END STATE:\t", states
        return states, nodes

    def synchronous_update(self, states, nodes):  # updates asynchronously
        print
        print "NEW GENERATION"
        old_states = states[:]
        for node_num, node in enumerate(nodes):
            node_weights = self.weights[node_num]
            print "Weights:\t", node_weights
            print "State:\t\t", states
            print "Old state:\t", old_states
            print "Field:\t\t", self.sgn(np.dot(node_weights, old_states))
            states[node_num] = nodes[node_num].output(node_weights, old_states)
        print "END STATE:\t", states

        return states, nodes

    def run(self, method='asynchronously'):
        # generate a random array of states (size N)
        states = map(lambda x: self.sgn(x), np.random.randint(-2, 2, size=self.N))

        # construct list of Nodes with random states
        nodes = []
        for state in states:
            nodes.append(Node(state))
        
        # see how network evolves over generations
        print "RANDOM INITIAL STATE"
        print states
        for _ in xrange(500):
            if (states == self.pattern) or (states == [-x for x in self.pattern]):
                break  # reached fixed point
            if method == 'asynchronously':
                states, nodes = self.asynchronous_update(states, nodes)
            else:
                states, nodes = self.synchronous_update(states, nodes)
        print
        print "END STATE"
        print states
        print

if __name__ == '__main__':
    pattern = map(int,sys.argv[1:])
    hnet = HopfieldNetwork(pattern)
    hnet.run()





