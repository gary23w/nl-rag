---
title: "getting-started/README.md at master · singer-io/getting-started · GitHub"
source: https://github.com/singer-io/getting-started/blob/master/README.md
domain: singer-taps
license: CC-BY-SA-4.0
tags: singer spec, singer taps, data extraction protocol, etl connectors
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

singer-io

/

getting-started

Public

- Notifications You must be signed in to change notification settings
- Fork 140
- Star

## Expand file tree

More file actions

More file actions

## Latest commit

## History

History

History

## File metadata and controls

50 lines (46 loc) · 2.92 KB

Outline

# Singer

Singer is an open source standard for moving data between databases, web APIs, files, queues, and just about anything else you can think of. The Singer spec describes how data extraction scripts — called “Taps” — and data loading scripts — called “Targets” — should communicate using a standard JSON-based data format over stdout. By conforming to this spec, Taps and Targets can be used in any combination to move data from any source to any destination.

Join the Singer Slack channel to get help from members of the Singer community.

## Docs

- Singer Specification
  - Synopsis
  - Input
    - Config
    - State
    - Example Invocations
  - Output
    - RECORD Message
    - SCHEMA Message
    - STATE Message
  - Example
  - Versioning
- Running and Developing Singer Taps and Targets
  - Running Singer with Python
  - Developing a Tap
  - Developing a Target
- Config and State
  - Config File
  - State File
- Discovery Mode
  - Schemas
  - The Catalog
  - Metadata
- Sync Mode
  - Streams
  - Replication Method
  - Stream/Field Selection
  - Metric Messages
- Best Practices for Building a Singer Tap
  - Rate Limiting
  - Memory Constraints
  - Dates
  - Logging and Exception Handling
  - Module Structure
  - Schemas
  - Code Quality
  - Dependency Versioning
- FAQ
  - How do I prevent dependency conflicts between my tap and target?

Copyright © 2018 Stitch
