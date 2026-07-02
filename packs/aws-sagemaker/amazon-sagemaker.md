---
title: "Amazon SageMaker"
source: https://en.wikipedia.org/wiki/Amazon_SageMaker
domain: aws-sagemaker
license: CC-BY-SA-4.0
tags: aws sagemaker, managed machine learning, ml training platform, model deployment service
fetched: 2026-07-02
---

# Amazon SageMaker

**Amazon SageMaker AI** is a cloud-based machine-learning platform that allows the creation, training, and deployment by developers of machine-learning (ML) models on the cloud. It can be used to deploy ML models on embedded systems and edge-devices. The platform was launched in November 2017.

## Capabilities

SageMaker enables developers to operate at a number of different levels of abstraction when training and deploying machine learning models. At its highest level of abstraction, SageMaker provides pre-trained ML models that can be deployed as-is. It offers a number of built-in ML algorithms that developers can train on their own data.

The platform features managed instances of TensorFlow and Apache MXNet, where developers can create their own ML algorithms from scratch. A developer may also connect their SageMaker-enabled ML models to other AWS services, such as the Amazon DynamoDB database for structured data storage, AWS Batch for offline batch processing, or Amazon Kinesis for real-time processing.

## Development interfaces

Various interfaces are available for developers to interact with SageMaker. A web API may remotely control a SageMaker server instance. While the web API is agnostic to the programming language used by the developer, Amazon provides SageMaker API bindings for a number of languages, including Python, JavaScript, Ruby, Java, and Go. SageMaker Python SDK is accessible through Anaconda's community-led conda-forge channel. SageMaker also provides managed Jupyter Notebook instances for interactively programming SageMaker and other applications.

In December 2025, new serverless customization in SageMaker AI was announced to interface with AI models like Amazon Nova, Llama, Qwen, DeepSeek and GPT-OSS.

## History and features

- 2017-11-29: SageMaker is launched at the AWS re:Invent conference.
- 2018-02-27: Managed TensorFlow and MXNet deep neural network training and inference are now supported within SageMaker.
- 2018-02-28: SageMaker automatically scales model inference to multiple server instances.
- 2018-07-13: Support is added for recurrent neural network training, word2vec training, multi-class linear learner training, and distributed deep neural network training in Chainer with Layer-wise Adaptive Rate Scaling (LARS).
- 2018-07-17: AWS Batch Transform enables high-throughput non-real-time machine learning inference in SageMaker.
- 2018-11-08: Support for training and inference of Object2Vec word embeddings.
- 2018-11-27: SageMaker Ground Truth "makes it much easier for developers to label their data using human annotators through Mechanical Turk, third-party vendors, or their own employees."
- 2018-11-28: SageMaker Reinforcement Learning (RL) "enables developers and data scientists to quickly and easily develop reinforcement learning models at scale."
- 2018-11-28: SageMaker Neo enables deep neural network models to be deployed from SageMaker to edge-devices such as smartphones and smart cameras.
- 2018-11-29: The AWS Marketplace for SageMaker is launched. The AWS Marketplace enables 3rd-party developers to buy and sell machine learning models that can be trained and deployed in SageMaker.
- 2019-01-27: SageMaker Neo is released as open-source software.
