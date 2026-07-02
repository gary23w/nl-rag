---
title: "TensorRT"
source: https://en.wikipedia.org/wiki/TensorRT
domain: tensorrt-llm
license: CC-BY-SA-4.0
tags: tensorrt inference, gpu kernel optimization, half precision inference, cuda acceleration
fetched: 2026-07-02
---

# TensorRT

**TensorRT** is a software development kit (SDK) and inference optimization runtime developed by Nvidia for deploying trained deep learning and machine learning models on graphics processing units (GPUs). It can import models from frameworks such as PyTorch, TensorFlow, and ONNX, and compile them into optimized runtime engines for low-latency and high-throughput inference.

In current Nvidia documentation, the TensorRT name is also used for a broader product family that includes the core TensorRT SDK, TensorRT-LLM, and TensorRT-RTX. The core SDK is primarily a proprietary Nvidia product, although Nvidia also maintains Apache-licensed open-source TensorRT repositories and related companion projects.

## History

TensorRT was available as part of Nvidia's deep learning software stack by 2017, when it was described as a high-performance inference engine for deploying trained neural networks on Nvidia GPUs. In 2018, Google announced integration of Nvidia TensorRT with TensorFlow 1.7, describing TensorRT as a library that optimizes deep learning models for inference and creates a runtime for deployment on GPUs in production environments.

## Overview

The core of TensorRT is a C++ library that takes a trained network, consisting of a network definition and trained parameters, and produces a highly optimized runtime engine for inference on Nvidia GPUs. TensorRT provides both C++ and Python APIs, and models can either be expressed directly through its network definition API or imported through its ONNX parser.

According to Nvidia's documentation, TensorRT performs graph-level and kernel-level optimizations such as layer fusion and selection of efficient implementations for supported operations. Current documentation also describes support for dynamic shapes, mixed-precision execution modes including FP32, FP16, BF16, FP8, and INT8, and specialized optimizations for transformer and large language model workloads.

TensorRT engines can be generated through the TensorRT APIs or with the *trtexec* command-line utility. Nvidia's quick-start documentation describes deployment workflows based on ONNX conversion, runtime APIs, and direct engine deserialization for C++ and Python applications.

## Licensing and open-source components

The licensing model around TensorRT is split between a proprietary core SDK and a set of open-source repositories and tools. The packaged TensorRT software distributed by Nvidia is governed by the Nvidia Software License Agreement. At the same time, Nvidia maintains a public TensorRT repository on GitHub under the Apache License 2.0.

Official TensorRT documentation also directs users to the TensorRT open-source software repository for quick-start code and samples. The architecture documentation describes related tooling such as Polygraphy for debugging and constant folding, as well as ONNX-GraphSurgeon for modifying ONNX graphs before deployment with TensorRT. TensorRT also supports a plugin mechanism for custom layers and unsupported operations.

## Product family

Nvidia's current documentation groups several inference products under the TensorRT name. In that documentation, the core SDK is distinguished as **TensorRT (Enterprise)**, while related offerings include TensorRT-LLM for large language model inference and TensorRT-RTX for consumer RTX GPUs.

### TensorRT-LLM

**TensorRT-LLM** is a related open-source toolkit for optimizing and serving large language models on Nvidia GPUs. Nvidia describes it as providing a Python API to define LLMs and build TensorRT engines optimized for LLM workloads.

According to Nvidia's product-family documentation, TensorRT-LLM supports multi-GPU and multi-node execution, in-flight batching, paged KV cacheing, and quantization methods such as FP8, INT8, and INT4 for higher-throughput model serving. The TensorRT-LLM codebase is published on GitHub under the Apache License 2.0.

Because Nvidia documents TensorRT-LLM as a separate member of the TensorRT product family, it is typically treated as a related but distinct software project rather than as a single feature of the base TensorRT SDK.
