---
title: "AWS Lambda"
source: https://en.wikipedia.org/wiki/AWS_Lambda
domain: aws-lambda
license: CC-BY-SA-4.0
tags: aws lambda, serverless function, lambda function, function as a service
fetched: 2026-07-02
---

# AWS Lambda

**AWS Lambda** is an event-driven, serverless Function as a Service (FaaS) provided by Amazon as a part of Amazon Web Services. It is designed to enable developers to run code without provisioning or managing servers. It executes code in response to events and automatically manages the computing resources required by that code. It was introduced on November 13, 2014.

## Specification

Each AWS Lambda instance runs within a lightweight, isolated environment powered by Firecracker microVMs. These microVMs are initialized with a runtime environment based on Amazon Linux (Amazon Linux AMI or Amazon Linux 2). Firecracker provides hardware-virtualization-based isolation, aiming to achieve near-bare-metal performance with minimal overhead. AWS claims that, unlike traditional virtual machines, these microVMs launch in milliseconds, enabling rapid and secure function execution with a minimal memory footprint. The Amazon Linux AMI is specifically optimized for cloud-native and serverless workloads, aiming to provide a lightweight, secure, and performant runtime environment.

As of 2025, AWS Lambda supports Node.js, Python, Java, Go, .NET, Ruby and custom runtimes.

## Cold start performance and deployment considerations

Rust and Go generally exhibit lower cold start times in AWS Lambda compared to Java and C# because they compile to native static binaries, eliminating the need for a virtual machine (JVM or .NET CLR) and reducing runtime initialization overhead. Go has some minimal runtime initialization, including garbage collection and goroutine management, but its impact on cold start time is relatively low. Rust, which is fully ahead-of-time (AOT) compiled and does not require a runtime, often achieves the lowest cold start latency among supported languages.

Java and C# run on managed runtime environments, introducing additional cold start latency due to runtime initialization and Just-In-Time (JIT) compilation. However, modern optimizations have mitigated some of these challenges. .NET 7 and .NET 8 support Ahead-of-Time (AOT) compilation, reducing cold start times by precompiling code. Additionally, AWS Lambda SnapStart for Java 11 and 17 pre-warms and snapshots execution state, significantly decreasing cold start overhead for Java-based functions. Despite these optimizations, Rust and Go typically maintain lower cold start times due to their minimal runtime dependencies.

In long-running workloads, JIT compilation in Java and .NET may improve execution speed through dynamic optimizations. However, this benefit is workload-dependent, and Rust's AOT compilation often provides better performance consistency, particularly for CPU-bound tasks. For short-lived Lambda invocations, Rust and Go generally maintain more predictable performance, as JIT optimizations may not have sufficient time to take effect.

Historically, Rust and Go required additional effort in deployment due to cross-compilation and static linking challenges. Rust, in particular, often necessitates MUSL-based static linking for AWS Lambda compatibility. However, advancements in deployment tooling, including AWS Serverless Application Model (AWS SAM), GitHub Actions, and Lambda container images, have simplified this process. Go benefits from native static linking support, making its deployment process comparatively straightforward. AWS Lambda's support for container images further reduces runtime compatibility concerns, enabling the use of custom runtimes and dependencies.

## Features

### Concurrency Models

Reserved Concurrency sets a maximum number of concurrent executions for a specific function and reserves that capacity from the account's overall concurrency limit. However, it does not keep execution environments initialized or guarantee that any instances remain running when the function is idle.

Provisioned Concurrency, in contrast, maintains a specified number of pre-initialized execution environments, ensuring that the function does not experience cold starts and does not scale down to zero.

### Lambda Function URL

The Lambda Function URL gives Lambda a unique and permanent URL which can be accessed by authenticated and non-authenticated users alike.

### Lambda layer

AWS Lambda layer is a ZIP archive containing libraries, frameworks or custom code that can be added to AWS Lambda functions. As of December 2024, AWS Lambda layers have significant limitations:

- No semantic versioning support.
- Incompatibility with major security scanning tools.
- Contribution to Lambda's 250MB size limit.
- Impeded local testing.
- No tree-shaking optimizations.

## Portability

Migration from AWS Lambda to other AWS compute services, such as Amazon ECS, presents challenges due to tight integration with AWS Lambda's APIs, often referred to as service lock-in. Tools like AWS Lambda Web Adapter offer a pathway for portability by enabling developers to build web applications using familiar frameworks under a monolithic Lambda design pattern. However, this approach introduces limitations, including coarser-grained alerting and access controls, potential cold start delays with large dependencies, and limited suitability for non-HTTP APIs.

## Tools

AWS Lambda Powertools is an open-source library developed by AWS that provides utilities for AWS Lambda functions. The core utilities includes structured logging, metrics and tracing. It also offers other utilities for common use cases when developing AWS Lambda functions. It is available in Python, Java,. Net and TypeScript. As of March 2025, it also includes data masking support for Python.

## Threading and Scalability in AWS Lambda

As of March 2025, AWS Lambda supports limited vertical scaling by increasing the number of virtual central processing units (vCPUs) through memory allocation. However, it does not allow an increase in single-thread performance, as clock speed remains fixed. When a function is allocated only one vCPU, multiple threads share the same core, resulting in context switching rather than true parallel execution. As a result, multi-threading in single-vCPU environments is primarily beneficial for input/output (I/O)-bound workloads rather than computationally intensive tasks.

Allocating additional memory in AWS Lambda enables multiple vCPUs, allowing for parallel execution. However, the clock speed per core remains unchanged, limiting individual thread performance. This configuration makes AWS Lambda suitable for workloads that scale horizontally or leverage parallelism but less optimal for applications that require high single-thread performance.

## Security

In April 2022, researchers found cryptomining malware targeting AWS Lambda named "Denonia".
