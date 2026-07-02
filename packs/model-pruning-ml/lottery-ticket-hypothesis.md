---
title: "Lottery ticket hypothesis"
source: https://en.wikipedia.org/wiki/Lottery_ticket_hypothesis
domain: model-pruning-ml
license: CC-BY-SA-4.0
tags: neural network pruning, weight sparsification, structured pruning, lottery ticket hypothesis, network sparsity
fetched: 2026-07-02
---

# Lottery ticket hypothesis

In machine learning, the **lottery ticket hypothesis** is that artificial neural networks with random weights can contain a subnetwork which (entirely by chance) can be tuned to a similar performance as tuning the whole network.

The original statement of the hypothesis is:

> A randomly-initialized, dense neural network contains a subnetwork that is initialized such that—when trained in isolation—it can match the test accuracy of the original network after training for at most the same number of iterations.

The original algorithm is:

1. Randomily initialize dense network: weights $\theta _{0}$ .
2. Train for j iterations → weights $\theta _{j}$ .
3. Magnitude pruning: build a bitmask m by setting to 0 the lowest-magnitude weights in each layer (one-shot), or repeat train → prune across rounds to reach higher sparsity (iterative).
4. Reset surviving weights to initialization: use $m\odot \theta _{0}$ as the starting point. Here $\odot$ is elementwise multiplication.
5. Train the masked network $f\!\left(x;m\odot \theta _{0}\right)$ with the same optimizer, schedule, and data.
6. Declare "winning ticket" if it achieves comparable test accuracy in $\leq j$ iterations.

The term derived from considering the probability of a tunable subnetwork as the equivalent to a winning lottery ticket; the chance of any given ticket winning is tiny, but if you buy enough of them you are certain to win, and the number of possible subnetworks increases exponentially as the power set of the set of connections, making the number of possible subnetworks astronomical for any reasonably large network.

Such networks are a priori difficult to find, since before training, one does not know which of the exponentially many subnetwork would be "lottery tickets". However, after training, these lottery tickets can be discovered by the pruning algorithm.

It was found that during the original training of the initial dense network, the weights that would end up in the winning ticket change a lot, but the other weights change little.

It was found that if instead of $m\odot \theta _{0}$ , they re-sampled a different random initialization $\theta _{0}'$ , and used $m\odot \theta _{0}'$ instead, the trained $f\!\left(x;m\odot \theta _{0}'\right)$ would perform much worse. This indicates that what makes a ticket winning is both its connection graph and the precise initial weights of the connections.

## Subsequent work

Malach *et al.* proved a stronger version of the hypothesis, namely that a sufficiently overparameterized untuned network will typically contain a subnetwork that is *already* an approximation to the given goal, even before tuning. A similar result has been proven for the special case of convolutional neural networks.
