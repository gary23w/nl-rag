---
title: "JAX (software)"
source: https://en.wikipedia.org/wiki/JAX_(software)
domain: jax-ml
license: CC-BY-SA-4.0
tags: jax library, autograd differentiation, just in time compilation, numpy vectorization, accelerator computing
fetched: 2026-07-02
---

# JAX (software)

**JAX** is a Python library for accelerator-oriented array computation and program transformation, designed for high-performance numerical computing and large-scale machine learning. It is developed by Google with contributions from Nvidia and other community contributors.

It is described as bringing together a modified version of the automatic differentiation system autograd and OpenXLA's XLA (Accelerated Linear Algebra). It is designed to follow the structure and workflow of NumPy as closely as possible and works with various existing frameworks such as TensorFlow and PyTorch. The primary features of JAX are:

1. Providing a unified NumPy-like interface to computations that run on CPU, GPU, or TPU, in local or distributed settings.
2. Built-in Just-In-Time (JIT) compilation via OpenXLA, an open-source machine learning compiler ecosystem.
3. Efficient evaluation of gradients via its automatic differentiation transformations.
4. Automatic vectorization to efficiently map functions over arrays representing batches of inputs.

## Libraries using Jax

- Flax
- Equinox
- Optax
- Diffrax
