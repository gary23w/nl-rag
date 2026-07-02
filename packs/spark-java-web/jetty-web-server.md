---
title: "Jetty (web server)"
source: https://en.wikipedia.org/wiki/Jetty_(web_server)
domain: spark-java-web
license: CC-BY-SA-4.0
tags: spark java framework, java microframework, jvm expressive routes, sparkjava embedded jetty
fetched: 2026-07-02
---

# Jetty (web server)

**Eclipse Jetty** is a Java web server and Jakarta Servlet container. While web servers are usually associated with serving documents to people, Jetty is now often used for machine to machine communications, usually within larger software frameworks. Jetty is developed as a free and open source project as part of the Eclipse Foundation. The web server is used in products such as Apache ActiveMQ, Alfresco, Scalatra, Apache Geronimo, Apache Maven, Apache Spark, Google App Engine, Eclipse, FUSE, iDempiere, Twitter's Streaming API and Zimbra. Jetty is also the server in open source projects such as Lift, Eucalyptus, OpenNMS, Red5, Hadoop and I2P. Jetty supports the latest Java Servlet API (with JSP support) as well as protocols HTTP/2 and WebSocket.

## Overview

Jetty started as an independent open-source project in 1995. In 2009 Jetty moved to Eclipse. Jetty often provides support for web services in an embedded Java application and it is already a component of the Eclipse IDE. It provides support for a wide variety of specifications and protocols including JASPI, JMX, JNDI, OSGi, WebSocket, HTTP/2, and more.

## History

Originally developed by software engineer Greg Wilkins, Jetty was an HTTP server component of Mort Bay Server. It was originally called IssueTracker (its original application) and then MBServler (Mort Bay Servlet server). Neither of these were much liked, so Jetty was finally picked.

Jetty was started in 1995 and was hosted by MortBay, creating version 1.x and 2.x, until 2000. From 2000 to 2005, Jetty was hosted by sourceforge.net where version 3.x, 4.x, and 5.x were produced. In 2005, the entire Jetty project moved to codehaus.org. As of 2009, the core components of Jetty have been moved to Eclipse.org, and Codehaus.org continued to provide integrations, extensions, and packaging of Jetty versions 7.x and 8.x (not 9.x) In 2016, the main repository of Jetty moved to GitHub, where it is still developed under the Eclipse IP Process.

| Version | Home | Min Java Version | Protocols | Servlet Version | JSP Version | Status |
|---|---|---|---|---|---|---|
| 12.0.x | Eclipse | 17 | HTTP/1.1 RFC7230, HTTP/2 RFC7540, WebSocket RFC6455/JSR356, FastCGI, JakartaEE Namespace | 3.1, 4.0, 5.0, 6.0 | 2.3, 3.0, 3.1 | Stable |
| 11.0.x | Eclipse | 11 | HTTP/1.1 RFC7230, HTTP/2 RFC7540, WebSocket RFC6455/JSR356, FastCGI, JakartaEE Namespace | 5.0 | 3.0 | EOL / Security Only |
| 10.0.x | Eclipse | 11 | HTTP/1.1 RFC7230, HTTP/2 RFC7540, WebSocket RFC6455/JSR356, FastCGI | 4.0 | 2.3 | EOL / Security Only |
| 9.4.x | Eclipse | 1.8 | HTTP/1.1 RFC7230, HTTP/2 RFC7540, WebSocket RFC6455/JSR356, FastCGI | 3.1 | 2.3 | EOL / Security Only |
| 9.3.x | Eclipse | 1.8 | HTTP/1.1 RFC7230, HTTP/2 RFC7540, WebSocket RFC6455/JSR356, FastCGI | 3.1 | 2.3 | Deprecated |
| 9.2.x | Eclipse | 1.7 | HTTP/1.1 RFC2616, WebSocket RFC6455, SPDY v3 | 3.1 | 2.3 | Deprecated |
| 9.1.x | Eclipse | 1.7 | HTTP/1.1 RFC2616 | 3.1 | 2.3 | Deprecated |
| 9.0.x | Eclipse | 1.7 | HTTP/1.1 RFC2616 | 3.1-beta | 2.3 | Deprecated |
| 8.x | Eclipse/Codehaus | 1.6 | HTTP/1.1 RFC2616, WebSocket RFC6455, SPDY v3 | 3.0 | 2.2 | Venerable |
| 7.x | Eclipse/Codehaus | 1.5 | HTTP/1.1 RFC2616, WebSocket RFC6455, SPDY v3 | 2.5 | 2.1 | Venerable |
| 6.x | Codehaus | 1.4–1.5 | HTTP/1.1 RFC2616 | 2.5 | 2.0 | Antique |
| 5.x | SourceForge | 1.2–1.5 | HTTP/1.1 RFC2616 | 2.4 | 2.0 | Relic |
| 4.x | SourceForge | 1.2, J2ME | HTTP/1.1 RFC2616 | 2.3 | 1.2 | Ancient |
| 3.x | SourceForge | 1.2 | HTTP/1.1 RFC2068 | 2.2 | 1.1 | Fossilized |
| 2.x | Mortbay | 1.1 | HTTP/1.0 RFC1945 | 2.1 | 1.0 | Legendary |
| 1.x | Mortbay | 1.0 | HTTP/1.0 RFC1945 | - | - | Mythical |
