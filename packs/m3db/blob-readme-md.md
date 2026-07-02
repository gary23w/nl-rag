---
title: "m3/README.md at master · m3db/m3 · GitHub"
source: https://github.com/m3db/m3/blob/master/README.md
domain: m3db
license: CC-BY-SA-4.0
tags: m3db, distributed time series database, m3 metrics platform, prometheus monitoring
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

m3db

/

m3

Public

- Notifications You must be signed in to change notification settings
- Fork 463
- Star

## Expand file tree

More file actions

More file actions

## Latest commit

## History

History

History

## File metadata and controls

131 lines (89 loc) · 3.74 KB

Outline

# M3

(GoDoc) (Build Status) (FOSSA Status)

(M3 Logo)

Distributed TSDB and Query Engine, Prometheus Sidecar, Metrics Aggregator, and more such as Graphite storage and query engine.

## Table of Contents

- More Information
- Install
  - Dependencies
- Usage
- Contributing

## More Information

- Documentation
- Contributing
- Slack
- Forum (Google Group)

### Community Meetings

You can find recordings of past meetups here: https://vimeo.com/user/120001164/folder/2290331.

## Install

### Dependencies

The simplest and quickest way to try M3 is to use Docker, read the M3 quickstart section for other options.

This example uses jq to format the output of API calls. It is not essential for using M3DB.

## Usage

The below is a simplified version of the M3 quickstart guide, and we suggest you read that for more details.

1. Start a Container

```highlight
docker run -p 7201:7201 -p 7203:7203 --name m3db -v $(pwd)/m3db_data:/var/lib/m3db quay.io/m3db/m3dbnode:v1.0.0
```

1. Create a Placement and Namespace

```highlight
#!/bin/bash
curl -X POST http://localhost:7201/api/v1/database/create -d '{
  "type": "local",
  "namespaceName": "default",
  "retentionTime": "12h"
}' | jq .
```

1. Ready a Namespace

```highlight
curl -X POST http://localhost:7201/api/v1/services/m3db/namespace/ready -d '{
  "name": "default"
}' | jq .
```

1. Write Metrics

```highlight
#!/bin/bash
curl -X POST http://localhost:7201/api/v1/json/write -d '{
  "tags": 
    {
      "__name__": "third_avenue",
      "city": "new_york",
      "checkout": "1"
    },
    "timestamp": '\"$(date "+%s")\"',
    "value": 3347.26
}'
```

1. Query Results

**Linux**

```highlight
curl -X "POST" -G "http://localhost:7201/api/v1/query_range" \
  -d "query=third_avenue" \
  -d "start=$(date "+%s" -d "45 seconds ago")" \
  -d "end=$( date +%s )" \
  -d "step=5s" | jq .  
```

**macOS/BSD**

```highlight
curl -X "POST" -G "http://localhost:7201/api/v1/query_range" \
  -d "query=third_avenue > 6000" \
  -d "start=$(date -v -45S "+%s")" \
  -d "end=$( date +%s )" \
  -d "step=5s" | jq .
```

## Contributing

You can ask questions and give feedback in the following ways:

- Create a GitHub issue
- In the public M3 Slack
- In the M3 forum (Google Group)

M3 welcomes pull requests, read contributing guide to help you get setup for building and contributing to M3.

This project is released under the Apache License, Version 2.0.
