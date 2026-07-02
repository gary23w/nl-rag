---
title: "Reverse proxy"
source: https://en.wikipedia.org/wiki/Reverse_proxy
domain: http-request-smuggling
license: CC-BY-SA-4.0
tags: http request smuggling, content length transfer encoding, proxy desynchronization, request boundary parsing
fetched: 2026-07-02
---

# Reverse proxy

In computer networks, a **reverse proxy** or surrogate server is a proxy server that appears to any client to be an ordinary web server, but in reality merely acts as an intermediary that forwards the client's requests to one or more ordinary web servers. Reverse proxies help increase scalability, performance, resilience, and security, but they also carry a number of risks.

Companies that run web servers often set up reverse proxies to facilitate the communication between an Internet user's browser and the web servers. An important advantage of doing so is that the web servers can be hidden behind a firewall on a company-internal network, and only the reverse proxy needs to be directly exposed to the Internet. Reverse proxy servers are implemented in popular open-source web servers. Dedicated reverse proxy servers are used by some of the biggest websites on the Internet.

A reverse proxy is capable of tracking IP addresses of requests that are relayed through it as well as reading and/or modifying any non-encrypted traffic. However, this implies that anyone who has compromised the server could do so as well.

Reverse proxies differ from forward proxies, which are used when the client is restricted to a private, internal network and asks a forward proxy to retrieve resources from the public Internet.

## Uses

Large websites and content delivery networks use reverse proxies, together with other techniques, to balance the load between internal servers. Reverse proxies can keep a cache of static content, which further reduces the load on these internal servers and the internal network. It is also common for reverse proxies to add features such as compression or TLS encryption to the communication channel between the client and the reverse proxy.

Reverse proxies can inspect HTTP headers, which, for example, allows them to present a single IP address to the Internet while relaying requests to different internal servers based on the URL of the HTTP request.

Reverse proxies can hide the existence and characteristics of origin servers. This can make it more difficult to determine the actual location of the origin server / website and, for instance, more challenging to initiate legal action such as takedowns or block access to the website, as the IP address of the website may not be immediately apparent. Additionally, the reverse proxy may be located in a different jurisdiction with different legal requirements, further complicating the takedown process.

Application firewall features can protect against common web-based attacks, like a denial-of-service attack (DoS) or distributed denial-of-service attacks (DDoS). Without a reverse proxy, removing malware or initiating takedowns (while simultaneously dealing with the attack) on one's own site, for example, can be difficult.

In the case of secure websites, a web server may not perform TLS encryption itself, but instead offload the task to a reverse proxy that may be equipped with TLS acceleration hardware. (See TLS termination proxy.)

A reverse proxy can distribute the load from incoming requests to several servers, with each server supporting its own application area. In the case of reverse proxying web servers, the reverse proxy may have to rewrite the URL in each incoming request in order to match the relevant internal location of the requested resource.

A reverse proxy can reduce load on its origin servers by caching static content and dynamic content, known as web acceleration. Proxy caches of this sort can often satisfy a considerable number of website requests, greatly reducing the load on the origin server(s).

A reverse proxy can optimize content by compressing it in order to speed up loading times.

In a technique named "spoon-feeding", a dynamically generated page can be produced in its entirety and served to the reverse proxy, which can feed the page to the client as the connection allows. The program that generates the page need not remain open, thus releasing server resources during the possibly extended time the client requires to complete the transfer.

Reverse proxies can operate wherever multiple web-servers must be accessible via a single public IP address. The web servers listen on different ports in the same machine, with the same local IP address or, possibly, on different machines with different local IP addresses. The reverse proxy analyzes each incoming request and delivers it to the right server within the local area network.

Reverse proxies can perform A/B testing and multivariate testing without requiring application code to handle the logic of which version is served to a client.

A reverse proxy can add access authentication to a web server that does not have any authentication.

## Risks

When the transit traffic is encrypted and the reverse proxy needs to filter/cache/compress or otherwise modify or improve the traffic, the proxy first must decrypt and re-encrypt communications. This requires the proxy to possess the TLS certificate and its corresponding private key, extending the number of systems that can have access to non-encrypted data and making it a more valuable target for attackers.

The vast majority of external data breaches happen either when hackers succeed in abusing an existing reverse proxy that was intentionally deployed by an organization, or when hackers succeed in converting an existing Internet-facing server into a reverse proxy server. Compromised or converted systems allow external attackers to specify where they want their attacks proxied to, enabling their access to internal networks and systems.

Applications that were developed for the internal use of a company are not typically hardened to public standards and are not necessarily designed to withstand all hacking attempts. When an organization allows external access to such internal applications via a reverse proxy, they might unintentionally increase their own attack surface and invite hackers.

If a reverse proxy is not configured to filter attacks or it does not receive daily updates to keep its attack signature database up to date, a zero-day vulnerability can pass through unfiltered, enabling attackers to gain control of the system(s) that are behind the reverse proxy server.

Giving the reverse proxy of a third party access to private keys (for caching or optimizing content) places the entire triad of confidentiality, integrity and availability in the hands of the third party who operates the proxy.

A reverse proxy is a single point of failure for the back-end services it fronts: an outage caused by misconfiguration, a denial-of-service attack, or a software fault can make every fronted service unreachable to outside clients, even when the back-end services themselves remain healthy. For example, a 2020 outage at Cloudflare briefly took down major sites and services that relied on its reverse-proxy edge, including Discord.
