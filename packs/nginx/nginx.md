---
title: "nginx"
source: https://en.wikipedia.org/wiki/Nginx
domain: nginx
license: BSD-2-Clause / CC-BY-SA-4.0
tags: nginx, nginx reverse proxy, nginx conf
fetched: 2026-07-02
---

# nginx

**nginx** (pronounced "engine x" /ˌɛndʒɪnˈɛks/ *EN-jin-EKS*, stylized as **NGINX**) is a web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache. The software was created by Russian developer Igor Sysoev and publicly released in 2004. nginx is free and open-source software, released under the terms of the 2-clause BSD license. A large fraction of web servers use nginx, often as a load balancer.

A company of the same name (Nginx, Inc.) was founded in 2011 to provide support and *NGINX Plus* paid software. In March 2019, the company was acquired by F5 for $670 million.

## Popularity

As of April 2025, W3Tech's web server count of all web sites ranked nginx first with 33.8%. Apache was second at 26.4% and Cloudflare Server third at 23.4%. As of March 2020, Netcraft estimated that nginx served 20.11% of the million busiest websites with Cloudflare a little ahead at 22.99%. Apache at 17.83% and Microsoft Internet Information Services at 4.16% rounded out the top four servers for the busiest websites. Some of Netcraft's other statistics show nginx ahead of Apache.

A 2018 survey of Docker usage found that nginx was the most commonly deployed technology in Docker containers. In OpenBSD version 5.2 (November 2012), nginx became part of the OpenBSD base system, providing an alternative to the system's fork of Apache 1.3, which it was intended to replace, but later in version 5.7 (November 2014) it was removed in favor of OpenBSD's own httpd(8).

## Features

nginx may be configured to serve static web content or to act as a proxy server.

nginx can be deployed to also serve dynamic content on the network using FastCGI, SCGI handlers for scripts, WSGI application servers or Phusion Passenger modules, and can serve as a software load balancer.

nginx uses an asynchronous event-driven approach, rather than threads, to handle requests. Nginx's modular event-driven architecture can provide predictable performance under high loads.

### HTTP proxy and Web server features

- Ability to handle more than 10,000 simultaneous connections with a low memory footprint (~2.5 MB per 10k inactive HTTP keep-alive connections)
- Handling of static files, index files and auto-indexing
- Reverse proxy with caching
- Load balancing with in-band health checks
- TLS/SSL with SNI and OCSP stapling support, via OpenSSL
- FastCGI, SCGI, uWSGI support with caching
- gRPC support since March 2018, version 1.13.10
- Name- and IP address-based virtual servers
- IPv6-compatible
- WebSockets since 1.3.13, including acting as a reverse proxy and load balancing of WebSocket applications
- HTTP/1.1 Upgrade (101 Switching Protocols)
- HTTP/2 protocol support
- HTTP/3 protocol support (experimental since 1.25.0)
- url rewriting and redirection
- Automatic issuance and renewal of TLS certificates using the ACME protocol

### Mail proxy features

- TLS/SSL support
- STARTTLS support
- SMTP, POP3, and IMAP proxy
- Requires authentication using an external HTTP server or by an authentication script

Other features include upgrading executable and configuration without client connections loss, and a module-based architecture with both core and third-party module support.

The paid Plus product includes additional features such as advanced load balancing and access to an expanded suite of metrics for performance monitoring.

## nginx in comparison to Apache

nginx was written with an explicit goal of being faster than the Apache web server. While nginx initially outperformed, Apache has offered similar performance since version 2.4. This former performance boost came at a cost of decreased flexibility, such as the ability to override system-wide access settings on a per-file basis (Apache accomplishes this with an .htaccess file, while nginx has no such feature built in).

Formerly, adding third-party modules to nginx required recompiling the application from source with the modules statically linked. This was partially overcome in version 1.9.11 in February 2016, with the addition of dynamic module loading. However, the modules still must be compiled at the same time as nginx, and not all modules are compatible with this system; some require the older static linking process.

## NGINX Unit

NGINX Unit is an open-source web application server, released in 2017 by Nginx, Inc. to target multi-language microservices-based applications. The initial release supported applications written in Go, PHP, and Python. By version 1.11.0, the support was extended to Java, Node.js, Perl, and Ruby applications; other features include dynamic configuration, request routing, and load balancing. NGINX Unit was archived by its maintainers in October of 2025 and is no longer receiving any updates.

## History

### 2000s

Igor Sysoev began development of nginx in 2002. Originally, nginx was developed to solve the C10k problem, and to fill the needs of multiple websites including the Rambler search engine and portal, for which it was serving 500 million requests per day by September 2008.

### 2010s

Nginx, Inc. was founded in July 2011 by Sysoev and Maxim Konovalov to provide commercial products and support for the software.

In October 2011, Nginx, Inc. raised $3 million from BV Capital, Runa Capital, and MSD Capital, Michael Dell's venture fund.

The company announced commercial support options for companies using nginx in production. Nginx, Inc. offered commercial support in February 2012, and paid NGINX Plus subscription in August 2013. Support packages focus on installation, configuration, performance improvement, etc. Support includes proactive notifications about major changes, security patches, updates and patches. Nginx, Inc. also offers consulting services to assist customers in custom configuration or adding additional features.

In October 2013, Nginx, Inc. raised a $10 million series B investment round led by New Enterprise Associates. That round included previous investors, as well as Aaron Levie, CEO and founder of Box.com. In December 2014, Nginx, Inc. raised a $20 million series B1 round led by New Enterprise Associates, with participation from e.ventures (formerly *BV Capital*), Runa Capital, Index Ventures and Nginx's own CEO Gus Robertson.

In September 2017, Nginx, Inc. announced an API management tool, NGINX Controller, which would build off of their API Gateway, NGINX Plus. In October 2017, Nginx, Inc. announced general available NGINX Amplify SaaS providing monitoring and analytics capabilities for nginx.

In June 2018, Nginx, Inc. raised $43 million in Series C Funding in a round led by Goldman Sachs "to Accelerate Application Modernization and Digital Transformation for Enterprises".

On 11 March 2019, F5 acquired Nginx, Inc. for US$670 million.

On 12 December 2019, it was reported that the Moscow offices of Nginx, Inc. had been raided by police, and that Sysoev and Konovalov had been detained. The raid was conducted under a search warrant connected to a copyright claim over nginx by Rambler—which asserts that it owns all rights to the code because it was written while Sysoev was an employee of the company. On 16 December 2019, Russian state lender Sberbank, which owns 46.5 percent of Rambler, called an extraordinary meeting of Rambler's board of directors asking Rambler's management team to request Russian law enforcement agencies cease pursuit of the criminal case, and begin talks with Nginx, Inc. and with F5.

### 2020s

On 18 January 2022, F5 announced that Igor Sysoev was leaving Nginx, Inc. and F5.

In late 2022, **Angie**, an open source fork of nginx, was released by some of the former nginx developers. Igor Sysoev is not actively involved in this project.

In February 2024, Maxim Dounin, one of nginx's core developers, created a nginx fork called **freenginx**. In the open letter announcing the creation, Maxim Dounin criticised F5's interference with nginx's development.
