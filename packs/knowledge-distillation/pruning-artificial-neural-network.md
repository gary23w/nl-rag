---
title: "Pruning (artificial neural network)"
source: https://en.wikipedia.org/wiki/Pruning_(artificial_neural_network)
domain: knowledge-distillation
license: CC-BY-SA-4.0
tags: knowledge distillation, teacher student, model compression, soft labels, network pruning
fetched: 2026-07-02
---

# Pruning (artificial neural network)

In deep learning, **pruning** is the practice of removing parameters from an existing artificial neural network. The goal of this process is to reduce the size (parameter count) of the neural network (and therefore the computational resources required to run it) whilst maintaining accuracy. This can be compared to the biological process of synaptic pruning which takes place in mammalian brains during development.

## Node (neuron) pruning

A basic algorithm for pruning is as follows:

1. Evaluate the importance of each neuron.
2. Rank the neurons according to their importance (assuming there is a clearly defined measure for "importance").
3. Remove the least important neuron.
4. Check a termination condition (to be determined by the user) to see whether to continue pruning.

## Edge (weight) pruning

Most work on neural network pruning does not remove full neurons or layers (structured pruning). Instead, it focuses on removing the most insignificant weights (unstructured pruning), namely, setting their values to zero. This can either be done globally by comparing weights from all layers in the network or locally by comparing weights in each layer separately.

Different metrics can be used to measure the importance of each weight. Weight magnitude as well as combinations of weight and gradient information are commonly used metrics.

Early work suggested also to change the values of non-pruned weights.

## When to prune the neural network?

Pruning can be applied at three different stages: before training, during training, or after training. When pruning is performed during or after training, additional fine-tuning epochs are typically required. Each approach involves different trade-offs between accuracy and computational cost.
