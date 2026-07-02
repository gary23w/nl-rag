---
title: "Getting Started"
source: https://www.jaegertracing.io/docs/latest/getting-started/
domain: jaeger-tracing
license: CC-BY-SA-4.0
tags: jaeger tracing, distributed tracing, trace span, request tracing
fetched: 2026-07-02
---

# Getting Started

Version

2.19

(latest)

1.76

(archive)

If you are new to distributed tracing, please check the Introduction page.

## All-in-one

The easiest way to run Jaeger is by starting it in a container:

```sh
docker run --rm --name jaeger \
  -p 16686:16686 \
  -p 4317:4317 \
  -p 4318:4318 \
  -p 5778:5778 \
  -p 9411:9411 \
  cr.jaegertracing.io/jaegertracing/jaeger:2.19.0
```

This runs the **all-in-one** configuration of Jaeger (see Architecture) that combines collector and query components in a single process and uses a transient in-memory storage for trace data. You can navigate to `http://localhost:16686` to access the Jaeger UI. See the APIs page for a full list of exposed ports.

In order to run Jaeger in other roles (see Architecture), an explicit configuration file (see Configuration) must be provided via the `--config` command line argument. When running in a container, the path to the config file must be mapped into the container file system (the `-v ...` mapping below):

```sh
docker run --rm --name jaeger \
  -p 16686:16686 \
  -p 4317:4317 \
  -p 4318:4318 \
  -p 5778:5778 \
  -p 9411:9411 \
  -v /path/to/local/config.yaml:/jaeger/config.yaml \
  cr.jaegertracing.io/jaegertracing/jaeger:2.19.0 \
  --config /jaeger/config.yaml
```

Your applications must be instrumented before they can send tracing data to Jaeger. We recommend using the

OpenTelemetry

instrumentation and SDKs.

## 🚗 HotROD Demo

HotROD (Rides on Demand) is a demo application that consists of several microservices and illustrates the use of OpenTelemetry and distributed tracing. A tutorial / walkthrough is available in the blog post: Take Jaeger for a HotROD ride.

Using this application you can:

- Discover architecture of the whole system via data-driven dependency diagram.
- View request timeline and errors; understand how the app works.
- Find sources of latency and lack of concurrency.
- Explore highly contextualized logging.
- Use baggage propagation to diagnose inter-request contention (queueing) and time spent in a service.
- Use open source libraries from `opentelemetry-contrib` to get vendor-neutral instrumentation for free.

We recommend running Jaeger and HotROD together via `docker compose`:

```bash
export JAEGER_VERSION=2.7.0 #Pick the newest version
git clone https://github.com/jaegertracing/jaeger.git jaeger
cd jaeger/examples/hotrod
docker compose up
# press Ctrl-C to exit
```

Then navigate to `http://localhost:8080`. See the README for other ways to run the demo.

## SPM

The Service Performance Monitoring (SPM) page has its own Quick Start that shows how to explore that aspect of Jaeger.

Last modified June 3, 2026:

Release 2.19.0 (#1103) (8af6e2e)
