---
title: "HTTP request smuggling"
source: https://en.wikipedia.org/wiki/HTTP_request_smuggling
domain: http-request-smuggling
license: CC-BY-SA-4.0
tags: http request smuggling, content length transfer encoding, proxy desynchronization, request boundary parsing
fetched: 2026-07-02
---

# HTTP request smuggling

**HTTP request smuggling** (**HRS**) is a security exploit on the HTTP protocol that takes advantage of an inconsistency between the interpretation of `Content-Length` and `Transfer-Encoding` headers between HTTP server implementations in a HTTP proxy server chain. HRS was first discovered in 2005 by Linhart et al.

The Transfer-Encoding header works by defining a directive on how to interpret the body of the HTTP request, with the common and necessary directive for this attack being the chunked transfer encoding. When the Transfer-Encoding header is present, the Content-Length header is supposed to be omitted. Working similarly but with a different syntax, the Content-Length header works by specifying the size in bytes of the body as a value in the header itself. Vulnerabilities arise when both of these headers are included in a malicious HTTP request, bypassing security functions meant to prevent malicious HTTP queries to the server by causing either the front-end or back-end server to incorrectly interpret the request.

## Types

### CL.TE

In this type of HTTP request smuggling, the front end processes the request using Content-Length header while backend processes the request using Transfer-Encoding header. The attack would be carried out with the first part of the request declaring a zero length chunk. The front end server seeing this would only read the first part of the request and unintentionally pass the second part to the back end server. Once passed through to the back end server, it would be treated as the next request and processed, carrying out the attackers hidden request.

### TE.CL

In this type of HTTP request smuggling, the front end processes request using Transfer-Encoding header while backend processes the request using Content-Length header. In this attack, a hacker would declare the valid length of the first chunk, which houses the malicious request and then declare a second chunk with a length of 0. When the front end server sees the second chunk with a length of 0 it believes the request to be complete and passes it along to the back end server. The back end server processes the request using the Content-Length header, however, and as a result the malicious request left in the first chunk go unprocessed until they are treating as being at the start of next request in the sequence and are carried out.

### TE.TE

In this type of HTTP request smuggling, the front end and backend both process the request using Transfer-Encoding header, but the header can be obfuscated in a way (for example by nonstandard whitespace formatting or duplicate headers) that makes one of the servers but not the other one ignore it. Obscuring the header may take the form of adding in an incorrect character, such as Transfer-Encoding: xchunked, or an unusual new line character between 'Transfer-Encoding' and ': chunked'. If one of the front of back end servers still processes these obfuscated HTTP requests, then the rest of the attack will be similar to how CL.TE or TE.CL attacks work.

## Prevention

The best prevention to these attacks would clearly be if frontend and backend servers interpreted HTTP requests the same way. However, this is usually not an option as load balancers support backend servers run on distinct platforms, using different software. Most variants of this attack can be prevented by using HTTP/2, as it uses a different method to determine the length of a request. Another method of avoiding the attack is for the frontend server to normalize HTTP requests before passing them to the backend, ensuring that they get interpreted in the same way. Configuring a web application firewall is another good way to prevent HRS attacks as many feature technology that identify attack attempts and either blocks or sanitize the suspicious incoming requests.

Grenfeldt et al. (2021) found that most front-end web servers (e.g. proxy servers) provided the parsing features for hindering in practice, all the known HRS attacks on the back-end web servers. Huang et al. (2022) proposed a method using Flask so to implement suitable parsing features that prevent HRS attacks, from a front-end program or web server.
