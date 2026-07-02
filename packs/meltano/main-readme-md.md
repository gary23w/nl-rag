---
title: "meltano/README.md at main · meltano/meltano · GitHub"
source: https://github.com/meltano/meltano/blob/main/README.md
domain: meltano
license: CC-BY-SA-4.0
tags: meltano platform, dataops platform, elt orchestration, singer taps
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

meltano

/

meltano

Public

- Notifications You must be signed in to change notification settings
- Fork 248
- Star

## Expand file tree

More file actions

More file actions

## Latest commit

## History

History

History

## File metadata and controls

120 lines (90 loc) · 6.47 KB

Outline

# The declarative code-first data integration engine

### Say goodbye to writing, maintaining, and scaling your own API integrations. Unlock 600+ APIs and DBs and realize your wildest data and ML-powered product ideas.

## Integrations

Meltano Hub is the single source of truth to find any Meltano plugins as well as Singer taps and targets. Users are also able to add more plugins to the Hub and have them immediately discoverable and usable within Meltano. The Hub is lovingly curated by Meltano and the wider Meltano community.

## Installation

If you're ready to build your ideal data platform and start running data workflows across multiple tools, start by following the Installation guide to have Meltano up and running in your device.

### Docker Images

Meltano is available as Docker images on Docker Hub:

- **Slim images** (recommended): `meltano/meltano:latest-slim` - optimized size, includes cloud storage support
- **Full images**: `meltano/meltano:latest` - includes all database connectors and build tools

```highlight
# Quick start with slim image
docker run --rm meltano/meltano:latest-slim --version

# For projects needing MSSQL/PostgreSQL
docker run --rm meltano/meltano:latest --version
```

See our Containerization guide for detailed usage instructions.

## Documentation

Check out the "Getting Started" guide or find the full documentation at https://docs.meltano.com.

## Contributing

Meltano is a truly open-source project, built for and by its community. We happily welcome and encourage your contributions. Start by browsing through our issue tracker to add your ideas to the roadmap. If you're still unsure on what to contribute at the moment, you can always check out the list of open issues labeled as "Accepting Merge Requests".

For more information on how to contribute to Meltano, refer to our contribution guidelines.

## Community

We host weekly online events where you can engage with us directly. Check out more information in our Community page.

If you have any questions, want sneak peeks of features or would just like to say hello and network, join our community of over +2,500 data professionals!

👋 Join us on Slack!

## Responsible Disclosure Policy

Please refer to the responsible disclosure policy on our website.

## License

This code is distributed under the MIT license, see the LICENSE file.
