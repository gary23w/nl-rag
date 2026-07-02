---
title: "Model Context Protocol"
source: https://en.wikipedia.org/wiki/Model_Context_Protocol
domain: model-context-protocol
license: CC-BY-SA-4.0
tags: model context protocol, tool calling standard, json rpc interface, llm interoperability
fetched: 2026-07-02
---

# Model Context Protocol

The **Model Context Protocol** (**MCP**) is an open standard and open-source framework introduced by Anthropic in November 2024 to standardize the way artificial intelligence (AI) systems like large language models (LLMs) integrate and share data with external tools, systems, and data sources. MCP provides a standardized interface for reading files, executing functions, and handling contextual prompts. Following its announcement, the protocol was adopted by major AI providers, including OpenAI and Google DeepMind.

## Background

MCP was announced by Anthropic in November 2024 as an open standard for connecting AI assistants to data systems such as content repositories, business management tools, and development environments. The protocol was created at Anthropic by engineers David Soria Parra and Justin Spahr-Summers. It aims to address the challenge of information silos and legacy systems. Before MCP, developers often had to build custom connectors for each data source or tool, resulting in what Anthropic described as an "N×M" data integration problem.

Earlier stop-gap approaches—such as OpenAI's 2023 "function-calling" API and the ChatGPT plug-in framework—solved similar problems but required vendor-specific connectors. MCP re-uses the message-flow ideas of the Language Server Protocol (LSP).

In December 2025, Anthropic donated the MCP to the Agentic AI Foundation (AAIF), a directed fund under the Linux Foundation, co-founded by Anthropic, Block and OpenAI, with support from other companies.

## Features

MCP defines a standardized framework for integrating AI systems with external data sources and tools. MCP enables applications such as querying structured databases with plain language in the field of natural language data access.

The protocol distinguishes between *MCP hosts*, *MCP clients* and *MCP servers.* An MCP host is typically an AI agent that interacts with an LLM and requires services from one or more MCP servers. For each of these MCP servers, the MCP host will create a dedicated MCP client that communicates with that server. Client and host will typically run on the same machine, while the MCP servers may be local or remote.

Each server provides one or more tools or resources. Example tools are: access to a database, calculators, access to code repositories etc.; a resource might be a certain FAQ document. The MCP client asks its server for a list of tools and resources the server provides; the server replies with a natural-language description of the capabilities of each tool and the expected format to call the tool. This information is given to the LLM; if it requires the services of one of these tools, the MCP host will instruct the relevant MCP client to call the tool. The MCP server performs the tool action and returns the results, which the MCP host then injects into the LLM conversation. Client and server communicate using the JSON-RPC 2.0 transport protocol.

The protocol was released with software development kits (SDKs) in programming languages including Python, TypeScript, C# and Java and examples of MCP server implementations.

The protocol is used in AI-assisted software development tools. Integrated development environments (IDEs), coding platforms such as Replit, and code intelligence tools like Sourcegraph have adopted MCP to grant AI coding assistants real-time access to project context.

MCP Apps is an official extension to the Model Context Protocol built on mcp-ui. While the base MCP specification is restricted to text and structured data, MCP Apps standardizes the delivery of interactive user interfaces—such as dashboards, forms, and data visualizations—from MCP servers to host applications like Claude and ChatGPT.

## Adoption

In March 2025, OpenAI officially adopted the MCP, after having integrated the standard across its products, including the ChatGPT desktop app. In September 2025, OpenAI added support for MCP to ChatGPT apps. This allows for third-party access inside ChatGPT.

MCP can be integrated with Microsoft Semantic Kernel, and Azure OpenAI. MCP servers can be deployed to Cloudflare.

In April 2026, the AAIF held the MCP Dev Summit North America in New York City, drawing approximately 1,200 attendees.

## Reception

*The Verge* reported that MCP addresses a growing demand for AI agents that are contextually aware and capable of pulling from diverse sources.

In April 2025, security researchers released an analysis that concluded there are multiple outstanding security issues with MCP, including prompt injection and poisoned tools that allow for data exfiltration through other connected tools.

MCP has been likened to OpenAPI, a similar specification that aims to describe APIs.
