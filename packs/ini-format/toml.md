---
title: "TOML"
source: https://en.wikipedia.org/wiki/TOML
domain: ini-format
license: CC-BY-SA-4.0
tags: ini file format, ini configuration, key-value config, windows configuration file
fetched: 2026-07-02
---

# TOML

**Tom's Obvious, Minimal Language** (**TOML**, originally **Tom's Own Markup Language**) is a file format for configuration files. It is designed to be easy to read and write by being *minimal* (unlike the more-complex YAML) and by using human-readable syntax. The project standardizes the implementation of the ubiquitous INI file format (which it has largely supplanted), removing ambiguity from its interpretation. Originally created by Tom Preston-Werner, the TOML specification is open source. TOML is used in a number of software projects and is implemented by all popular programming languages.

## Syntax

Among other constructs, TOML's syntax primarily consists of key-value pairs, section names in square brackets, and comments delimited by a leading `#`. TOML's syntax is a superset of the INI format. Contrary to the INI format, which comprises multiple competing variants as a result of ad-hoc parsers, TOML has a formally agreed-upon syntax.

TOML supports the following data types: string, integer, float, boolean, datetime, array, and table.

### Example

```mw
# This is a TOML document.

title = "TOML Example"

[database]
server = "192.168.1.1"
ports = [ 8000, 8001, 8002 ]
connection_max = 5000
enabled = true

# Line breaks are okay when inside arrays
hosts = [
  "alpha",
  "omega"
]

[servers]

  # Indentation (tabs and/or spaces) is allowed, but not required
  [servers.alpha]
  ip = "10.0.0.1"
  dc = "eqdc10"

  [servers.beta]
  ip = "10.0.0.2"
  dc = "eqdc10"
```

## Notable uses

TOML is used in a variety of settings, such as:

- Jekyll (a static site generator) configuration `_config.toml` (although configuration through YAML is also supported)
- Hugo (a static site generator) configuration `hugo.toml` (although configuration through JSON and YAML is also supported)
- Python 3 package manifests `pyproject.toml`
- Rust package manifests `Cargo.toml`
- Julia project settings `Project.toml` and package manifests `Manifest.toml`
- Blender add-on manifests `blender_manifest.toml`
- Gradle version catalogs `libs.versions.toml`
- Taplo configurations `.taplo.toml` and `taplo.toml`
- Prettier configurations `.prettierrc.toml`
