---
title: "great_expectations/README.md at develop · fivetran/great_expectations · GitHub"
source: https://github.com/great-expectations/great_expectations/blob/develop/README.md
domain: great-expectations-deep
license: CC-BY-SA-4.0
tags: great expectations, data quality framework, data validation tool, data pipeline testing
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

fivetran

/

great_expectations

Public

- Notifications You must be signed in to change notification settings
- Fork 1.8k
- Star

## Expand file tree

More file actions

More file actions

## Latest commit

## History

History

History

## File metadata and controls

61 lines (41 loc) · 4.64 KB

Outline

(Python Versions) (PyPI) (PyPI Downloads) (Build Status) (pre-commit.ci Status) (codecov) (DOI) (Twitter Follow) (Slack Status) (Contributors) (Ruff)

## About GX Core

GX Core combines the collective wisdom of thousands of community members with a proven track record in data quality deployments worldwide, wrapped into a super-simple package for data teams.

Its powerful technical tools start with Expectations: expressive and extensible unit tests for your data. Expectations foster collaboration by giving teams a common language to express data quality tests in an intuitive way. You can automatically generate documentation for each set of validation results, making it easy for everyone to stay on the same page. This not only simplifies your data quality processes, but helps preserve your organization’s institutional knowledge about its data.

Learn more about how data teams are using GX Core in our featured case studies.

## Integration support policy

GX Core supports Python `3.10` through `3.13`. Experimental support for Python `3.14` and later can be enabled by setting a `GX_PYTHON_EXPERIMENTAL` environment variable when installing `great_expectations`.

For data sources and other integrations that GX supports, see the compatibility reference for additional information.

## Get started

GX recommends deploying GX Core within a virtual environment. For more information about getting started with GX Core, see Introduction to GX Core.

1. Run the following command in an empty base directory inside a Python virtual environment to install GX Core: pip install great_expectations
2. Run the following command to import the `great_expectations module` and create a Data Context: import great_expectations as gx context = gx.get_context()

## Get support from GX and the community

They are listed in the order in which GX is prioritizing the support issues:

1. Issues and PRs in the GX GitHub repository
2. Questions posted to the GX Core Discourse forum
3. Questions posted to the GX Slack community channel

## Contribute

We truly value the contributions of our community and always welcome pull requests. PRs are encouraged for both bug fixes and new features. For feature requests, we ask that you first open an issue for discussion to ensure the feature fits within the vision for GX Core and to align on the approach so that your time and effort are well spent. Thank you for being a crucial part of GX Core!

## Code of conduct

Everyone interacting in GX Core project codebases, Discourse forums, Slack channels, and email communications is expected to adhere to the GX Community Code of Conduct.
