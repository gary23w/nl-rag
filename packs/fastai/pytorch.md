---
title: "PyTorch"
source: https://en.wikipedia.org/wiki/PyTorch
domain: fastai
license: CC-BY-SA-4.0
tags: fastai library, transfer learning, high level api, training deep networks, pytorch wrapper
fetched: 2026-07-02
---

# PyTorch

**PyTorch** is an open-source deep learning library, originally developed by Meta Platforms and currently developed with support from the Linux Foundation. The successor to Torch, PyTorch provides a high-level API that builds upon optimised, low-level implementations of deep learning algorithms and architectures, such as the Transformer, or SGD. Notably, this API simplifies model training and inference to a few lines of code. PyTorch allows for automatic parallelization of training and, internally, implements CUDA bindings that speed training further by leveraging GPU resources.

PyTorch utilises the tensor as a fundamental data type, similarly to NumPy. Training is facilitated by a reversed automatic differentiation system, Autograd, that constructs a directed acyclic graph of the operations (and their arguments) executed by a model during its forward pass. With a loss, backpropagation is then undertaken.

As of 2025, PyTorch remains one of the most popular deep learning libraries, alongside others such as TensorFlow and Keras. It can be installed using Anaconda package managers. A number of commercial deep learning systems are built on top of PyTorch, including ChatGPT, Tesla Autopilot, Uber's Pyro, and Hugging Face's Transformers.

## History

In 2001, Torch was written and released under a GPL by the Idiap Research Institute. It was a machine-learning library written in C++ and CUDA, supporting methods including neural networks, support vector machines (SVM), hidden Markov models, etc. Around 2010, it was rewritten by Ronan Collobert, Clement Farabet and Koray Kavuckuoglu. This was known as Torch7 or LuaTorch. This was written so that the backend was in C and the frontend was in Lua. In mid-2016, some developers refactored it to decouple the frontend and the backend, with strong influence from torch-autograd and Chainer. In turn, torch-autograd was influenced by HIPS/autograd. Development on Torch7 ceased in 2018 and was subsumed by the PyTorch project.

Meta (formerly known as Facebook) operates both PyTorch and Convolutional Architecture for Fast Feature Embedding (Caffe2), but models defined by the two frameworks were mutually incompatible. The Open Neural Network Exchange (ONNX) project was created by Meta and Microsoft in September 2017 to decouple deep learning frameworks from hardware-specific runtimes, allowing models to be converted between frameworks and optimized for execution providers like NVIDIA’s TensorRT. Caffe2 was merged into PyTorch at the end of March 2018. In September 2022, Meta announced that PyTorch would be governed by the independent PyTorch Foundation, a newly created subsidiary of the Linux Foundation.

PyTorch 2.0 was released on 15 March 2023, introducing TorchDynamo, a Python-level compiler that makes code run up to two times faster, along with significant improvements in training and inference performance across major cloud platforms.

## PyTorch tensors

PyTorch defines a class called Tensor (`torch.Tensor`) to store and operate on homogeneous multidimensional rectangular arrays of numbers. PyTorch supports various sub-types of multi-dimensional arrays, or Tensors. PyTorch Tensors are similar to NumPy Arrays, but can also be operated on by a CUDA-capable NVIDIA GPU. PyTorch has also been developing support for other GPU platforms, for example, AMD's ROCm and Apple's Metal Framework.

## PyTorch neural networks

PyTorch defines a module called nn (`torch.nn`) to describe neural networks and to support training. This module offers a comprehensive collection of building blocks for neural networks, including various layers and activation functions, enabling the construction of complex models. Networks are built by inheriting from the `torch.nn` module and defining the sequence of operations in the `forward()` function.

## PyTorch Serialized File Format

Pytorch can save and load models using its own file format, which is a ZIP64 archive containing the model weights in a Python pickle file, and other information such as the byte order. The file extensions .pt and .pth are commonly used for these files.

## Example

The following program shows the low-level functionality of the library with a simple example.

```mw
import torch
dtype = torch.float
device = torch.device("cpu")  # Execute all calculations on the CPU
# device = torch.device("cuda:0")  # Executes all calculations on the GPU

# Create a tensor and fill it with random numbers
a = torch.randn(2, 3, device=device, dtype=dtype)
print(a)
# Output: tensor([[-1.1884,  0.8498, -1.7129],
#                  [-0.8816,  0.1944,  0.5847]])

b = torch.randn(2, 3, device=device, dtype=dtype)
print(b)
# Output: tensor([[ 0.7178, -0.8453, -1.3403],
#                  [ 1.3262,  1.1512, -1.7070]])

print(a * b)
# Output: tensor([[-0.8530, -0.7183,  2.58],
#                  [-1.1692,  0.2238, -0.9981]])

print(a.sum()) 
# Output: tensor(-2.1540)

print(a[1, 2])  # Output of the element in the third column of the second row (zero-based)
# Output: tensor(0.5847)

print(a.max())
# Output: tensor(0.8498)
```

The following code block defines a neural network with linear layers using the `nn` module.

```mw
from torch import nn # Import the nn sub-module from PyTorch

class NeuralNetwork(nn.Module):  # Neural networks are defined as classes
    def __init__(self):  # Layers and variables are defined in the __init__ method
        super().__init__()  # Must be in every network.
        self.flatten = nn.Flatten()   # Construct a flattening layer.
        self.linear_relu_stack = nn.Sequential(  # Construct a stack of layers.
            nn.Linear(28 * 28, 512),  # Linear Layers have an input and output shape
            nn.ReLU(),  # ReLU is one of many activation functions provided by nn
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10), 
        )

    def forward(self, x):  # This function defines the forward pass.
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits
```
