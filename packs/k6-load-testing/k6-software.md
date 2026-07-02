---
title: "K6 (software)"
source: https://en.wikipedia.org/wiki/K6_(software)
domain: k6-load-testing
license: CC-BY-SA-4.0
tags: k6 load, load testing, performance testing, http requests
fetched: 2026-07-02
---

# K6 (software)

**K6** is an open-source load testing tool developed by Grafana Labs. It is designed to help developers and engineers test the performance and reliability of their systems, particularly APIs, microservices, and websites. K6 is both an HTTP load and functional test tool, written in Go and using the goja embedded JavaScript interpreter for test scripting purposes. Tests are written in ECMAScript 6 using the Babel transpiler. There is support for HTTP/2, TLS, test assertions, ramp up and down, duration, number of iterations etc. Standard metrics include reports to standard out but can include collectors that report to time-series databases which can be visualized in real-time. There is a Jenkins plugin that can be combined with thresholds (global pass/fail criteria).

## Features

- **Developer-friendly**: Uses JavaScript for scripting.
- **Extensible**: Can be extended with various modules and integrations.
- **Performance testing**: Supports stress, spike, and soak tests.
- **Automation-friendly**: Integrates with CI/CD pipelines for continuous testing.

## History

K6 was initially released by LoadImpact in 2017. LoadImpact was later rebranded into k6 in 2020. K6 was then acquired by Grafana Labs in 2021. It has since become a popular tool for performance testing in the developer community.

Grafana k6 1.0 was released on 2025-05-07 at GrafanaCON 2025.

## Example and usage

The below script executes a GET request on the Wikipedia homepage, checks whether the HTTP status code is 200 and if we are using the HTTP/2 protocol.

```mw
import http from "k6/http";
import { check } from "k6";

export default function() {
  check(http.get("https://www.wikipedia.org/"), {
    "status is 200": (r) => r.status == 200,
    "protocol is HTTP/2": (r) => r.proto == "HTTP/2.0",
  });
}
```

The above test case can be run with the command `$ k6 run http_2.js` where `http_2.js` is the filename in which the test case is saved in.
