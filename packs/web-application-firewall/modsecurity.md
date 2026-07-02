---
title: "ModSecurity"
source: https://en.wikipedia.org/wiki/ModSecurity
domain: web-application-firewall
license: CC-BY-SA-4.0
tags: web application firewall, application firewall, modsecurity waf, reverse proxy filtering, http request smuggling
fetched: 2026-07-02
---

# ModSecurity

**ModSecurity**, sometimes called **Modsec**, is an open-source web application firewall (WAF). Originally designed as a module for the Apache HTTP Server, it has evolved to provide an array of Hypertext Transfer Protocol request and response filtering capabilities along with other security features across a number of different platforms including Apache HTTP Server, Microsoft IIS and Nginx. It is free software released under the Apache license 2.0.

The platform provides a rule configuration language known as 'SecRules' for real-time monitoring, logging, and filtering of Hypertext Transfer Protocol communications based on user-defined rules.

Although not its only configuration, ModSecurity is most commonly deployed to provide protections against generic classes of vulnerabilities using the OWASP ModSecurity Core Rule Set (CRS). This is an open-source set of rules written in ModSecurity's SecRules language. The project is part of OWASP, the Open Web Application Security Project. Several other rule sets are also available.

To detect threats, the ModSecurity engine is deployed embedded within the webserver or as a proxy server in front of a web application. This allows the engine to scan incoming and outgoing HTTP communications to the endpoint. Dependent on the rule configuration the engine will decide how communications should be handled which includes the capability to pass, drop, redirect, return a given status code, execute a script, and more.

## History

ModSecurity was first developed by Ivan Ristić, who wrote the module with the end goal of monitoring application traffic on the Apache HTTP Server. The first version was released in November 2002 which supported Apache HTTP Server 1.3.x. Starting in 2004 Ivan created Thinking Stone to continue work on the project full-time. While working on the version 2.0 rewrite Thinking Stone was bought by Breach Security, an American-Israeli security company, in September 2006. Ivan stayed on continuing the development of version 2.0 which was subsequently released in October 2006 at the OWASP AppSec conference in Seattle.

Ristić and Breach Security released another major rewrite, version 2.5, with major syntactic changes in February 2008. In December 2008 Ivan left Breach to found SSL Labs. Shortly after Ivan's departure from Breach Security, Trustwave Holdings acquired Breach in June 2010 and relicensed ModSecurity under the Apache license. Development continued and the new license allowed easier integration of ModSecurity into other products. As a result of this there was steady adoption of ModSecurity by various commercial products. The license change also precipitated easier porting of the software. Hence, Microsoft contributed an IIS port in August 2012 and the port for Nginx was released at Black Hat Briefings in 2012.

2017 saw the second edition of the handbook released, written by Christian Folini and Ivan Ristić. It covers ModSecurity up to version 2.9.2.

Being originally an Apache module, porting ModSecurity to other platforms was time-consuming and had high maintenance costs. As a result of this, a complete rewrite was started in December 2015. This new iteration, libmodsecurity, changes the underlying architecture, separating ModSecurity into a standalone engine that communicates with the web server via an API. This modular architecture-based WAF, which was announced for public use in January 2018, became libmodsecurity (ModSecurity version 3.0) and has supported connectors for Nginx and Apache.

In 2021, Trustwave Holdings, announce the End-of-Sale (EOS) of Trustwave support for ModSecurity effective August 1, 2021 and the End-of-Life (EOL) of support effective July 1, 2024. The maintenance of the ModSecurity code is given to the open-source community.
