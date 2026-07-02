---
title: "Documentation"
source: https://cuelang.org/docs/
domain: cue-language
license: CC-BY-SA-4.0
tags: cue language, cue configuration language, data validation config, cuelang schema
fetched: 2026-07-02
---

# Welcome to CUE!

CUE is an *open-source* data validation language with its roots in logic programming. It combines succinct yet clear syntax with powerful, flexible constraints that enable data, schema, and policy constraints to coexist seamlessly:

```cue
area:   length * width
area:   <100        // Must be less than 100.
width:  33.3 & >10  // Must be greater than 10.
length: 5 & !=width // Reject square areas.
```

```
$ cue vet -c example.cue
area: invalid value 166.5 (out of bound <100):
    ./example.cue:2:9
    ./example.cue:1:9
```

CUE supports and simplifies a wide variety of applications, such as data validation, configuration, querying, and code generation, with its underlying inference engine enabling data validation in code, and flexible generation pipelines.

## How to use this documentation

Browse through the different documentation sections, or use the search box in the top-right corner of each page. Here’s what you’ll find in each section:
