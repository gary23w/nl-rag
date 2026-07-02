---
title: "vLLM"
source: https://en.wikipedia.org/wiki/VLLM
domain: vllm
license: CC-BY-SA-4.0
tags: vllm engine, llm inference, paged attention, throughput serving, gpu batching
fetched: 2026-07-02
---

# vLLM

**vLLM** is an open-source software framework for inference and serving of large language models and related multimodal models. Originally developed at the University of California, Berkeley's Sky Computing Lab, the project is centered on *PagedAttention*, a memory-management method for transformer key–value caches, and supports features such as continuous batching, distributed inference, quantization, and OpenAI-compatible APIs.

## History

vLLM was introduced in 2023 by researchers affiliated with the Sky Computing Lab at UC Berkeley. Its core ideas were described in the 2023 paper *Efficient Memory Management for Large Language Model Serving with PagedAttention*, which presented the system as a high-throughput and memory-efficient serving engine for large language models.

According to a project maintainer, the "v" in vLLM originally referred to "virtual", inspired by virtual memory.

PyTorch's project page states that the University of California, Berkeley contributed vLLM to the Linux Foundation in July 2024. In 2025, the PyTorch Foundation announced that vLLM had become a Foundation-hosted project.

In January 2026, *TechCrunch* reported that the creators of vLLM had launched the startup Inferact to commercialize the project, raising $150 million in seed funding.

## Architecture

According to its 2023 paper, vLLM was designed to improve the efficiency of large language model serving by reducing memory waste in the key–value cache used during transformer inference. The paper introduced *PagedAttention*, an algorithm inspired by virtual memory and paging techniques in operating systems, and described vLLM as using block-level memory management and request scheduling to increase throughput while maintaining similar latency.

The project documentation and repository describe support for continuous batching, chunked prefill, speculative decoding, prefix caching, quantization, and multiple forms of distributed inference. PyTorch has described vLLM as a high-throughput, memory-efficient inference and serving engine that supports a range of hardware back ends, including NVIDIA and AMD GPUs, Google TPUs, AWS Trainium, and Intel processors.
