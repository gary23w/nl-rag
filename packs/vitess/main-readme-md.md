---
title: "vitess/README.md at main · vitessio/vitess · GitHub"
source: https://github.com/vitessio/vitess/blob/main/README.md
domain: vitess
license: CC-BY-SA-4.0
tags: vitess, mysql sharding, database clustering, horizontal scaling
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

vitessio

/

vitess

Public

- Notifications You must be signed in to change notification settings
- Fork 2.4k
- Star

## Expand file tree

More file actions

More file actions

## Latest commit

## History

History

History

## File metadata and controls

57 lines (35 loc) · 3.14 KB

Outline

(Maven Central) (Coverage Status) (Go Report Card) (FOSSA Status) (CII Best Practices) (OpenSSF Scorecard)

# Vitess

Vitess is a cloud-native horizontally-scalable distributed database system that is built around MySQL. Vitess can achieve unlimited scaling through generalized sharding.

Vitess allows application code and database queries to remain agnostic to the distribution of data onto multiple database servers. With Vitess, you can even split and merge shards as your needs grow, with an atomic cutover step that takes only a few seconds.

Vitess was a core component of YouTube's database infrastructure from 2011, and grew to encompass tens of thousands of MySQL nodes. Starting in 2015, Vitess was adopted by many other large companies, including Slack, Square (now Block), and JD.com.

For more about Vitess, please visit vitess.io.

## Community

Vitess has a growing community.

If you are interested in contributing or participating in our monthly community meetings, please visit the Community page on our website.

We also maintain a roadmap on our website.

Follow our blog for low-frequency updates like new features and releases.

## Reporting a Problem, Issue, or Bug

To report a problem, create a GitHub issue.

For topics that are better discussed live, please join the Vitess Slack workspace. You may post any questions on the #general channel or join some of the special-interest channels.

## Security

### Reporting Security Vulnerabilities

To report a security vulnerability, please email vitess-maintainers.

See Security for a full outline of the security process.

### Security Audit

A third party security audit was performed by ADA Logics. Read the full report.

## License

Unless otherwise noted, the Vitess source files are distributed under the Apache Version 2.0 license found in the LICENSE file.

(FOSSA Status)
