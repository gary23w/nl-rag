---
title: "kedro/README.md at main · kedro-org/kedro · GitHub"
source: https://github.com/kedro-org/kedro/blob/main/README.md
domain: kedro-pipelines
license: CC-BY-SA-4.0
tags: kedro framework, data science pipelines, reproducible pipelines, machine learning engineering
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

kedro-org

/

kedro

Public

- Notifications You must be signed in to change notification settings
- Fork 1k
- Star

## Expand file tree

More file actions

More file actions

## Latest commit

## History

History

History

## File metadata and controls

121 lines (80 loc) · 10.6 KB

Outline

(Kedro)

(Python version) (PyPI version) (Conda version) (License) (Slack Organisation) (Slack Archive) (GitHub Actions Workflow Status - Main) (GitHub Actions Workflow Status - Develop) (Documentation) (OpenSSF Best Practices) (Monthly downloads) (Total downloads)

(Powered by Kedro)

## What is Kedro?

Kedro is a toolbox for production-ready data engineering and data science pipelines. It uses software engineering best practices to help you create data engineering and data science pipelines that are reproducible, maintainable, and modular. You can find out more at kedro.org.

Kedro is an open-source Python framework hosted by the LF AI & Data Foundation.

## How do I install Kedro?

To install Kedro from the Python Package Index (PyPI) run:

```
uv pip install kedro
```

It is also possible to install Kedro using `conda`:

```
conda install -c conda-forge kedro
```

Our Get Started guide contains full installation instructions, and includes how to set up Python virtual environments.

### Installation from source

To access the latest Kedro version before its official release, install it from the `main` branch.

```
uv pip install git+https://github.com/kedro-org/kedro@main
```

## What are the main features of Kedro?

| Feature | What is this? |
|---|---|
| Project Template | A standard, modifiable and easy-to-use project template based on Cookiecutter Data Science. |
| Data Catalog | A series of lightweight data connectors used to save and load data across many different file formats and file systems, including local and network file systems, cloud object stores, and HDFS. The Data Catalog also includes data and model versioning for file-based systems. |
| Pipeline Abstraction | Automatic resolution of dependencies between pure Python functions and data pipeline visualisation using Kedro-Viz. |
| Coding Standards | Test-driven development using `pytest`, produce well-documented code using Sphinx, create linted code with support for `ruff` and make use of the standard Python logging library. |
| Flexible Deployment | Deployment strategies that include single or distributed-machine deployment as well as additional support for deploying on Argo, Prefect, Kubeflow, AWS Batch, and Databricks. |

## How do I use Kedro?

The Kedro documentation first explains how to install Kedro and then introduces key Kedro concepts.

You can then review the spaceflights tutorial to build a Kedro project for hands-on experience.

For new and intermediate Kedro users, there's a comprehensive section on how to visualise Kedro projects using Kedro-Viz.

*A pipeline visualisation generated using Kedro-Viz*

Additional documentation explains how to work with Kedro and Jupyter notebooks, and there are a set of advanced user guides for advanced for key Kedro features. We also recommend the API reference documentation for further information.

## Why does Kedro exist?

Kedro is built upon our collective best-practice (and mistakes) trying to deliver real-world ML applications that have vast amounts of raw unvetted data. We developed Kedro to achieve the following:

- To address the main shortcomings of Jupyter notebooks, one-off scripts, and glue-code because there is a focus on creating **maintainable data engineering and data science code**
- To enhance **team collaboration** when different team members have varied exposure to software engineering concepts
- To increase efficiency, because applied concepts like modularity and separation of concerns inspire the creation of **reusable analytics code**

Find out more about how Kedro can answer your use cases from the product FAQs on the Kedro website.

## The humans behind Kedro

The Kedro product team and a number of open source contributors from across the world maintain Kedro.

## Can I contribute?

Yes! We welcome all kinds of contributions. Check out our guide to contributing to Kedro.

## Where can I learn more?

There is a growing community around Kedro. We encourage you to ask and answer technical questions on Slack and bookmark the Linen archive of past discussions.

We keep a list of technical FAQs in the Kedro documentation and you can find a growing list of blog posts, videos and projects that use Kedro over on the `awesome-kedro` GitHub repository. If you have created anything with Kedro we'd love to include it on the list. Just make a PR to add it!

## How can I cite Kedro?

If you're an academic, Kedro can also help you, for example, as a tool to solve the problem of reproducible research. Use the "Cite this repository" button on our repository to generate a citation from the CITATION.cff file.

## Python version support policy

- The core Kedro Framework supports all Python versions that are actively maintained by the CPython core team. When a Python version reaches end of life, support for that version is dropped from Kedro. This is not considered a breaking change.
- The Kedro Datasets package follows the NEP 29 Python version support policy. This means that `kedro-datasets` generally drops Python version support before `kedro`. This is because `kedro-datasets` has a lot of dependencies that follow NEP 29 and the more conservative version support approach of the Kedro Framework makes it hard to manage those dependencies properly.

## ☕️ Kedro Coffee Chat 🔶

We appreciate our community and want to stay connected. For that, we offer a public Coffee Chat format where we share updates and cool stuff around Kedro once every two weeks and give you time to ask your questions live.

Check out the upcoming demo topics and dates at the Kedro Coffee Chat wiki page.

Follow our Slack announcement channel to see Kedro Coffee Chat announcements and access demo recordings.
