---
title: "Ollama"
source: https://en.wikipedia.org/wiki/Ollama
domain: ollama
license: CC-BY-SA-4.0
tags: ollama runner, local llm, model quantization, on device inference, open weights model
fetched: 2026-07-02
---

# Ollama

**Ollama** is an open-source software platform for running and managing large language models on local computers and through hosted cloud models. It provides a command-line interface, a native GUI, a local REST API, model-management tools, and integrations for using open-weight models with coding assistants and other applications.

## History

Ollama was first released in 2023. The project became associated with the growth of local large language model software, allowing users to download and run models such as Llama, Gemma, Mistral, Qwen, gpt-oss and DeepSeek models from a local machine.

In 2025 and 2026, Ollama added additional application and cloud features, including hosted cloud models, web search support, tool and coding-agent integrations, and support for using Ollama with applications such as Claude Code, Codex, OpenCode, Copilot CLI, and OpenClaw. In March 2026, Ollama announced preview support for Apple silicon.

## Features

Ollama includes tools for downloading, running, importing, and managing large language models. Users can run models from the command line, interact with them through a local HTTP API, or use client libraries for programming languages such as Python and JavaScript.

The project provides a REST API for chat and model-management functions, with the default local service commonly exposed on port 11434. Ollama also distributes an official Docker image and provides model libraries and documentation for running supported models.

Ollama uses the llama.cpp backend for local model inference. It supports a model-library format that allows users to pull, run, and manage model variants by name.

Meanwhile, the project's downloadable software is being explored as a back-end platform for low-code/no-code self-hosting of LLMs, potentially allowing natural language processing use cases to become more accessible to nontechnical end users.

Ollama also has experimental support for image generation, using models such as Flux, on macOS, with Windows and Linux support expected in the future.

## Security

Because Ollama is commonly used to run local or self-hosted AI models, security researchers have examined risks from misconfigured public deployments. In January 2026, *The Hacker News* reported on research by SentinelOne and Censys that found many Ollama servers were exposed to the public internet, mainly by binding to the "any" port 0.0.0.0 which on an inadequately-secured system would allow access from other local or remote devices despite the fact that Ollama is intended to run locally by default.
