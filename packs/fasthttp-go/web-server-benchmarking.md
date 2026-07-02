---
title: "Web server benchmarking"
source: https://en.wikipedia.org/wiki/Web_server_benchmarking
domain: fasthttp-go
license: CC-BY-SA-4.0
tags: fasthttp go, go high performance http, fasthttp server, fasthttp request handler
fetched: 2026-07-02
---

# Web server benchmarking

**Web server benchmarking** is the process of estimating a web server performance in order to find if the server can serve sufficiently high workload.

## Key parameters

The performance is usually measured in terms of:

- Number of requests that can be served per second (depending on the type of request, etc.);
- Latency response time in milliseconds for each new connection or request;
- Throughput in bytes per second (depending on file size, cached or not cached content, available network bandwidth, etc.).

The measurements must be performed under a varying load of clients and requests per client.

## Tools for benchmarking

Load testing (stress/performance testing) a web server can be performed using automation/analysis tools such as:

- Apache JMeter, an open-source Java load testing tool
- ApacheBench (or ab), a command line program bundled with Apache HTTP Server
- Siege, an open-source web-server load testing and benchmarking tool
- Wrk, an open-source C load testing tool
- Locust, an open-source Python load testing tool

## Web application benchmarks

Web application benchmarks measure the performance of application servers and database servers used to host web applications. TPC-W was a common benchmark emulating an online bookstore with synthetic workload generation.
