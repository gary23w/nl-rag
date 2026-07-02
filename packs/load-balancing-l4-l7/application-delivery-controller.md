---
title: "Application delivery controller"
source: https://en.wikipedia.org/wiki/Application_delivery_controller
domain: load-balancing-l4-l7
license: CC-BY-SA-4.0
tags: layer 4 load balancing, layer 7 load balancing, reverse proxy, consistent hashing
fetched: 2026-07-02
---

# Application delivery controller

An **application delivery controller** (**ADC**) is a computer network device in a datacenter, often part of an application delivery network (ADN), that helps perform common tasks, such as those done by web accelerators to remove load from the web servers themselves. Many also provide load balancing. ADCs are often placed in the DMZ, between the outer firewall or router and a web farm.

## Features

An Application Delivery Controller (ADC) is a type of server that provides a variety of services designed to optimize the distribution of load being handled by backend content servers. An ADC directs web request traffic to optimal data sources in order to remove unnecessary load from web servers. To accomplish this, an ADC includes many OSI layer 3-7 services, including load-balancing.

ADCs are intended to be deployed within the DMZ of a computer server cluster hosting web applications and/or services. In this sense, an ADC can be envisioned as a drop-in load balancer replacement. But that is where the similarities end. When an ADC receives a web request from an external host, it enacts the following process (assuming all features exist and are enabled):

1. Serve as TLS endpoint for the cluster and decrypt incoming requests (HTTPS-only).
2. Examine the Request URI and determine the type of resource being requested.
3. Verify that the entity making the request is authorized to access the given URI.
4. Perform any URI translation, if applicable.
5. Lookup the pool of hosts associated with that resource type (e.g. image, stylesheet, HTML, etc).
6. In the case of login requests, the request may be translated, rather than simply forwarded, to an instance within a pool of authentication servers.
7. In the case of static objects, the ADC may serve the object directly from its own internal cache or direct it to a dedicated static object repository.
8. Maintain a table describing the health of the servers in every pool via one of several methods (e.g. average response time).
9. Forward the request to the server within the target pool with the best health score.

Features commonly found in ADCs include:

- Traffic Shaping
- SSL/TLS offloading
- Web Application Firewall
- DNS
- Reverse Proxy
- API Gateway
- HTTP Content Redirection
- Server Health Monitoring
- Payload Compression/Decompression
- A/B Testing
- Facilitation of zero-downtime server maintenance cycles (by temporarily removing servers being upgraded from their respective pool)
- Authorization & Access Control (but typically does not include Authentication)

In the context of Telco infrastructure, an ADC could provide access control services for a Gi-LAN area.

## History

Starting around 2004, first generation ADCs offered simple application acceleration and load balancing.

In 2006, ADCs began to mature when they began featuring advanced applications services such as compression, caching, connection multiplexing, traffic shaping, application layer security, SSL offload, and content switching, combined with services like server load balancing in an integrated services framework that optimized and secured business critical application flows.

By 2007, application acceleration products were available from many companies.

Until leaving the market in 2012, Cisco Systems offered application delivery controllers. Market leaders like F5 Networks, Radware, and Citrix had been gaining market share from Cisco in previous years.

The ADC market segment became fragmented into two general areas: 1) general network optimization; and 2) application/framework specific optimization. Both types of devices improve performance, but the latter is usually more aware of optimization strategies that work best with a particular application framework, focusing on ASP.NET or AJAX applications, for example.
