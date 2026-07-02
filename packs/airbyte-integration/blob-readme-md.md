---
title: "airbyte/README.md at master · airbytehq/airbyte · GitHub"
source: https://github.com/airbytehq/airbyte/blob/master/README.md
domain: airbyte-integration
license: CC-BY-SA-4.0
tags: airbyte platform, data integration platform, elt pipeline, data connectors
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

airbytehq

/

airbyte

Public

- Notifications You must be signed in to change notification settings
- Fork 5.2k
- Star

## Expand file tree

More file actions

More file actions

## Latest commit

## History

History

History

## File metadata and controls

93 lines (65 loc) · 8.47 KB

Outline

(Airbyte)

*Open-source data movement for ELT pipelines and AI agents — from APIs, databases & files to warehouses, lakes, and AI applications*

(Test) (Release) (Slack) (YouTube Channel Views) (Build) (License) (License)

We believe that only an **open-source solution to data movement** can cover the long tail of data sources while empowering data engineers to customize existing connectors. Our ultimate vision is to help you move data from any source to any destination — whether that destination is a data warehouse, a data lake, or an AI agent. Airbyte provides a catalog of 600+ connectors for APIs, databases, data warehouses, data lakes, and AI applications.

(Airbyte Connections UI) *Screenshot taken from Airbyte Cloud*.

### Pick the right Airbyte Platform for the job

- **Moving data into warehouses, lakes, or databases (ELT / ETL)** → use Airbyte Open Source (this repo) or Airbyte Cloud. 600+ connectors for APIs, databases, data warehouses, and data lakes.
- **Giving AI agents, LLMs, or MCP clients real-time access to business data** (CRMs, support tools, SaaS APIs, databases) → use Airbyte Agents, the managed data and context layer for AI agents, or the open-source Agent SDK (`uv pip install airbyte-agent-sdk`) to embed type-safe connectors as LLM tools. Works with pydantic-ai, LangChain, OpenAI Agents, and FastMCP, with built-in retry, exception translation, and output-size guardrails.

### Getting Started — Data Movement (ELT)

For moving data into warehouses, lakes, and databases:

- Deploy Airbyte Open Source or set up Airbyte Cloud to start centralizing your data.
- Create connectors in minutes with our no-code Connector Builder or low-code CDK.
- Explore popular use cases in our tutorials.
- Orchestrate Airbyte syncs with Airflow, Dagster, Kestra, or the Airbyte API.

Try it out yourself with our demo app, visit our full documentation, and learn more about recent announcements. See our registry for a full list of connectors already available in Airbyte or Airbyte Cloud.

### Getting Started — AI Agents

For building AI agents that need real-time business data:

- Read the Airbyte Agents documentation to use the managed product.
- Or install the open-source Agent SDK: `uv pip install airbyte-agent-sdk`. Works with pydantic-ai, LangChain, OpenAI Agents, and FastMCP — see the SDK README for examples of turning a connector call into an LLM tool.

### Join the Airbyte Community

The Airbyte community can be found in the Airbyte Community Slack, where you can ask questions and voice ideas. You can also ask for help in our Airbyte Forum. Airbyte's roadmap is publicly viewable on GitHub.

For videos and blogs on data engineering and building your data stack, check out Airbyte's Content Hub, YouTube, and sign up for our newsletter.

### Contributing

If you've found a problem with Airbyte, please open a GitHub issue. To contribute to Airbyte and see our Code of Conduct, please see the contributing guide. We have a list of good first issues that contain bugs that have a relatively limited scope. This is a great place to get started, gain experience, and get familiar with our contribution process.

#### PR Permission Requirements

When submitting a pull request, please ensure that Airbyte maintainers have write access to your branch. This allows us to apply formatting fixes and dependency updates directly, significantly speeding up the review and approval process.

To enable write access on your PR from Airbyte maintainers, please check the "Allow edits from maintainers" box when submitting from your PR. You must also create your PR from a fork in your **personal GitHub account** rather than an organization account, or else you will not see this option. The requirement to create from your personal fork is based on GitHub's additional security restrictions for PRs created from organization forks. For more information about the GitHub security model, please see the GitHub documentation page regarding PRs from forks.

For more details on contribution requirements, please see our contribution workflow documentation.

### Security

Airbyte takes security issues very seriously. **Please do not file GitHub issues or post on our public forum for security vulnerabilities**. Email `security@airbyte.io` if you believe you have uncovered a vulnerability. In the message, try to provide a description of the issue and ideally a way of reproducing it. The security team will get back to you as soon as possible.

Airbyte Enterprise also offers additional security features (among others) on top of Airbyte open-source.

### License

See the LICENSE file for licensing information, and our FAQ for any questions you may have on that topic.

### Thank You

Airbyte would not be possible without the support and assistance of other open-source tools and companies! Visit our thank you page to learn more about how we build Airbyte.
