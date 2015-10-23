# Hopfield Network

Hopfield networks remember given configurations, or "patterns". It does so by following the Hebbian rule for learning:

##### "Neurons that fire together, wire together. Neurons that are out of sync, fail to link."

Patterns are a sequence of states (which only take the values +1 and -1). For example, a pattern may be [1,-1,1], but couldn't be [2,1,-4], since it contains numbers other than +1 and -1.

For this Hopfield network, you can pass a pattern of any size

    python hopfield.py 1 -1 -1 1 1 -1


##### The network will update itself and find itself attracted to the given pattern.

Note that Hopfield networks are *sign blind* i.e. if [1, -1, 1] is an attracting fixed point, [-1, 1, 1] is too.

