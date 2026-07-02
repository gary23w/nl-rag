---
title: "Web server (part 2/2)"
source: https://en.wikipedia.org/wiki/Web_server
domain: chi-router-go
license: CC-BY-SA-4.0
tags: chi router golang, go http router, golang lightweight router, chi middleware stack
fetched: 2026-07-02
part: 2/2
---

## Load limits

A web server (program installation) usually has pre-defined **load limits** for each combination of operating conditions, also because it is limited by OS resources and because it can handle only a limited number of concurrent client connections (usually between 2 and several tens of thousands for each active web server process, see also the C10k problem and the C10M problem).

When a web server is near to or over its load limits, it gets **overloaded** and so it may become **unresponsive**.

### Causes of overload

At any time web servers can be overloaded due to one or more of the following causes:

- **Excess legitimate web traffic**. Thousands or even millions of clients connecting to the website in a short amount of time (e.g., the Slashdot effect).
- Distributed Denial of Service attacks. A denial-of-service attack (DoS attack) or distributed denial-of-service attack (DDoS attack) is an attempt to make a computer or network resource unavailable to its intended users.
- Computer worms that sometimes cause abnormal traffic because of millions of infected computers (not coordinated among them).
- XSS worms can cause high traffic because of millions of infected browsers or web servers.
- Internet bots Traffic not filtered or limited on large websites with very few network resources (e.g., bandwidth) or hardware resources (CPUs, RAM, disks).
- Internet (network) slowdowns (e.g., due to packet losses) so that client requests are served more slowly and the number of connections increases so much that server limits are reached.
- Web servers, **serving dynamic content**, **waiting for slow responses coming from back-end computers** (e.g., databases), maybe because of too many queries mixed with too many inserts or updates of DB data; in these cases web servers have to wait for back-end data responses before replying to HTTP clients but during these waits too many new client connections or requests arrive and so they become overloaded.
- Web servers (computers) **partial unavailability**. This can happen because of required or urgent maintenance or upgrade, hardware or software failures such as back-end (e.g., database) failures; in these cases the remaining web servers may get too much traffic and become overloaded.

### Symptoms of overload

The symptoms of an overloaded web server are usually the following ones:

- Requests are served with (possibly long) delays (from one second to a few hundred seconds).
- The web server returns an HTTP error code, such as 500, 502, 503, 504, 408, or even an intermittent 404.
- The web server refuses or resets (interrupts) TCP connections before it returns any content.
- In very rare cases, the web server returns only a part of the requested content. This behavior can be considered a bug, even if it usually arises as a symptom of overload.

### Anti-overload techniques

To partially overcome above average load limits and to prevent overload, most popular websites use common techniques like the following ones:

- Tuning OS parameters for hardware capabilities and usage.
- Tuning web servers parameters to improve their security and performances.
- Deploying **web cache** techniques (not only for static contents but, whenever possible, for dynamic contents too).
- Managing network traffic, by using:
  - Firewalls to block unwanted traffic coming from bad IP sources or having bad patterns;
  - HTTP traffic managers to drop, redirect or rewrite requests having bad HTTP patterns;
  - Bandwidth management and traffic shaping, in order to smooth down peaks in network usage.
- Using different domain names, IP addresses and computers to serve different kinds (static and dynamic) of content; the aim is to **separate** big or huge files (`download.*`) (that domain might be replaced also by a CDN) from small and medium-sized files (`static.*`) and from main dynamic site (maybe where some contents are stored in a backend database) (`www.*`); the idea is to be able to efficiently serve big or huge (over 10 – 1000 MB) files (maybe throttling downloads) and to fully cache small and medium-sized files, without affecting performances of dynamic site under heavy load, by using different settings for each (group) of web server computers:
  - `https://download.example.com`
  - `https://static.example.com`
  - `https://www.example.com`
- Using many web servers (computers) that are grouped together behind a load balancer so that they act or are seen as one big web server.
- Adding more hardware resources (i.e., RAM, fast disks) to each computer.
- Using more efficient computer programs for web servers (see also: software efficiency).
- Using the most efficient **Web Server Gateway Interface** to process dynamic requests (spawning one or more external programs every time a dynamic page is retrieved, kills performances).
- Using other programming techniques and workarounds, especially if dynamic content is involved, to speed up the HTTP responses (i.e., by avoiding dynamic calls to retrieve objects, such as style sheets, images and scripts), that never change or change very rarely, by copying that content to static files once and then keeping them synchronized with dynamic content.
- Using latest efficient versions of HTTP (e.g., beyond using common HTTP/1.1 also by enabling HTTP/2 and maybe HTTP/3 too, whenever available web server software has reliable support for the latter two protocols) in order to reduce a lot the number of TCP/IP connections started by each client and the size of data exchanged (because of more compact HTTP headers representation and maybe data compression). This may not prevent overloads of RAM and CPU caused by the need for encryption. It may also not address overloads caused by excessively large files uploaded at high speed, because they are optimized for concurrency.

Below are the latest statistics of the market share of all sites of the top web servers on the Internet by Netcraft.

| Date | nginx (Nginx, Inc.) | Apache (ASF) | OpenResty (OpenResty Software Foundation) | Cloudflare Server (Cloudflare, Inc.) | IIS (Microsoft) | GWS (Google) | Others |
|---|---|---|---|---|---|---|---|
| October 2021 | 34.95% | 24.63% | 6.45% | 4.87% | 4.00% (*) | 4.00% (*) | Less than 22% |
| February 2021 | 34.54% | 26.32% | 6.36% | 5.0% | 6.5% | 3.90% | Less than 18% |
| February 2020 | 36.48% | 24.5% | 4.00% | 3.0% | 14.21% | 3.18% | Less than 15% |
| February 2019 | 25.34% | 26.16% | N/A | N/A | 28.42% | 1.66% | Less than 19% |
| February 2018 | 24.32% | 27.45% | N/A | N/A | 34.50% | 1.20% | Less than 13% |
| February 2017 | 19.42% | 20.89% | N/A | N/A | 43.16% | 1.03% | Less than 15% |
| February 2016 | 16.61% | 32.80% | N/A | N/A | 29.83% | 2.21% | Less than 19% |

NOTE: (*) percentage rounded to integer number, because its decimal values are not publicly reported by source page (only its rounded value is reported in graph).
