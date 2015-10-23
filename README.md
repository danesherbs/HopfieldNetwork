# Hopfield Network

Hopfield networks remember given configurations, or "patterns". It does so by following the Hebbian rule for learning:

##### "Neurons that fire together, wire together. Neurons that are out of sync, fail to link."

Patterns are a sequence of states (which only take the values +1 and -1). For example, a pattern may be [1,-1,1], but couldn't be [2,1,-4], since it contains numbers other than +1 and -1.

For this Hopfield network, you can pass a pattern of any size

    python hopfield.py 1 -1 -1 1 1 -1

A random sequence of states will be generated. The network's job is to get from this sequence of states **to your pattern** (without looking at it -- *that would be cheating*!)

The network will then update each node according to simple rules, and arrive at your pattern.

```
RANDOM INITIAL STATE
[1, 1, -1, 1, 1, -1]

UPDATE NODE 0
Weights:	[ 0 -1 -1  1  1 -1]
Inputs:		[1, 1, -1, 1, 1, -1]
Field:		1

UPDATE NODE 1
Weights:	[-1  0  1 -1 -1  1]
Inputs:		[1, 1, -1, 1, 1, -1]
Field:		-1

UPDATE NODE 2
Weights:	[-1  1  0 -1 -1  1]
Inputs:		[1, -1, -1, 1, 1, -1]
Field:		-1

UPDATE NODE 3
Weights:	[ 1 -1 -1  0  1 -1]
Inputs:		[1, -1, -1, 1, 1, -1]
Field:		1

UPDATE NODE 4
Weights:	[ 1 -1 -1  1  0 -1]
Inputs:		[1, -1, -1, 1, 1, -1]
Field:		1

UPDATE NODE 5
Weights:	[-1  1  1 -1 -1  0]
Inputs:		[1, -1, -1, 1, 1, -1]
Field:		-1
END STATE:	[1, -1, -1, 1, 1, -1]

END STATE
[1, -1, -1, 1, 1, -1]
```



Note that Hopfield networks are **sign blind** i.e. if [1, -1, 1] is an attracting fixed point, [-1, 1, 1] is too.

