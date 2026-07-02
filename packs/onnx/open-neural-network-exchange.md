---
title: "Open Neural Network Exchange"
source: https://en.wikipedia.org/wiki/Open_Neural_Network_Exchange
domain: onnx
license: CC-BY-SA-4.0
tags: onnx format, model interoperability, inference engine, neural network exchange
fetched: 2026-07-02
---

# Open Neural Network Exchange

The **Open Neural Network Exchange** (**ONNX**) [ˈɒnɪks] is an open-source artificial intelligence ecosystem of technology companies and research organizations that establish open standards for representing machine learning algorithms and software tools to enable a standard format for representing machine learning models. ONNX is available on GitHub.

## History

ONNX was originally named Toffee and was developed by the PyTorch team at Facebook. In September 2017 it was renamed to ONNX and announced by Facebook and Microsoft. Later, IBM, Huawei, Intel, AMD, Arm and Qualcomm announced support for the initiative.

In October 2017, Microsoft announced that it would add its Cognitive Toolkit and Project Brainwave platform to the initiative.

In November 2019 ONNX was accepted as graduate project in Linux Foundation AI.

In October 2020 Zetane Systems became a member of the ONNX ecosystem.

## Intent

The initiative targets:

### Framework interoperability

Enable developers to move machine learning models between different frameworks, which may be used at different stages of the development process, such as training, architecture design, or deployment on mobile devices.

### Shared optimization

Provide a common representation that can be used by hardware vendors and other developers to apply optimizations to artificial neural network models across multiple machine learning frameworks.

ONNX provides definitions of an extensible computation graph model, built-in operators and standard data types, focused on inferencing (evaluation).. The container format is Protocol Buffers.

Each computation dataflow graph is a list of nodes that form an acyclic graph. Nodes have inputs and outputs. Each node is a call to an operator. Metadata documents the graph. Built-in operators are to be available on each ONNX-supporting framework.

ONNX models can be trained in a single framework, such as PyTorch or TensorFlow, and then exported to ONNX. This format allows models to be transferred from the training framework to other environments for testing or deployment. Once a model is in ONNX format, it can be executed in different runtime systems or on various hardware platforms, such as GPUs or specialized AI accelerators. Using a common format enables the same model representation to be used across multiple systems and frameworks.
