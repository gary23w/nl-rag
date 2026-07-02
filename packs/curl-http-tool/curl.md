---
title: "cURL"
source: https://en.wikipedia.org/wiki/CURL
domain: curl-http-tool
license: CC-BY-SA-4.0
tags: curl http, http client, data transfer, command-line http
fetched: 2026-07-02
---

# cURL

**cURL** (pronounced like "curl", /kɜːrl/) is a free and open-source computer program for transferring data to and from Internet servers. It can download resources identified by URLs from a web server over HTTP and supports a variety of other network protocols, URI schemes, multiple versions of HTTP, and proxying. The project consists of a library (**libcurl**) and command-line tool (**curl**), which have been widely ported to different computing platforms. It was created by Daniel Stenberg, who is still the lead developer of the project.

## History

The software was first released in 1996, originally named `httpget` and then became `urlget`, before adopting the current name of `curl`. The name stands for "Client and URL". The original author and lead developer is the Swedish developer Daniel Stenberg, who created curl to power part of an IRC bot, because he wanted to automatically provide currency exchange rates, fetched from a website, to users in an IRC chat room.

## Components

### libcurl

`libcurl` is a client-side URL transfer library that powers `curl`. It supports numerous internet protocols including DICT, FILE, FTP, FTPS, GOPHER, GOPHERS, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, MQTT, POP3, POP3S, RTMP, RTMPS, RTSP, SCP, SFTP, SMB, SMBS, SMTP, SMTPS, TELNET, TFTP, WS and WSS.

libcurl supports HTTP versions 0.9, 1.0, 1.1, HTTP/2 and HTTP/3 including h2c, prior-knowledge, dual-connect modes, and QUIC with 0-RTT handshakes.

The library provides features such as cookie handling, standard HTTP request methods (GET, POST, PUT, HEAD, multipart form uploads), and authentication mechanisms including Basic, Digest, NTLM, Negotiate, CRAM-MD5, SCRAM-SHA, Kerberos, Bearer tokens, AWS Sigv4, SASL, and reading credentials from .netrc.

`libcurl` supports a variety of security and transport features, including TLS 1.0-1.3, mutual authentication, STARTTLS, OCSP stapling, Encrypted Client Hello (ECH), False Start, key pinning, post-quantum readiness, session resumption, early data, session import/export, HSTS, Alt-Svc, Public Suffix List (PSL), entity tags (ETags), range requests, transfer compression (gzip, Brotli, zstd), custom headers, custom methods, and redirect following.

It also offers proxy and networking support, including SOCKS4, SOCKS5, HAProxy, and HTTP proxies with chaining and Unix domain sockets, as well as user-plus-password authentication. Advanced name-resolution features include DNS-over-HTTPS, custom DNS servers, host/port mappings, and DNS caching.

Additional functionality includes file transfer resume, FTP uploading, form-based HTTP upload, HTTPS certificates, and mechanisms for controlling and monitoring transfers such as configurable timeouts, automatic retries, rate limiting, and detection of stalled connections. The library also provides enhanced reporting features, including JSON-formatted metadata, content-disposition handling, IDN hostname display, and customizable transfer information.

The `libcurl` library is portable, as it builds and works identically on most platforms, including:

- AIX
- AmigaOS
- Android
- Azure Sphere OS
- BeOS
- BlackBerry Tablet OS and BlackBerry 10
- Cesium
- Darwin
- DOS
- Deos
- FreeBSD
- FreeRTOS
- HP-UX
- HURD
- iOS
- IRIX
- Linux
- macOS
- NetBSD
- NetWare
- OpenBSD
- OpenHarmony (HarmonyOS)
- OpenVMS
- OS/2
- QNX
- QNX Neutrino
- RISC OS
- RTEMS
- Solaris
- Symbian
- Tru64
- Ultrix
- UnixWare
- Windows
- VxWorks
- Zephyr

The `libcurl` library is thread-safe and IPv6 compatible. Bindings are available for more than 50 languages, including C, C++, Java, Julia (is bundled with), PHP and Python.

The `libcurl` library supports SSL/TLS through GnuTLS, mbedTLS, SChannel (on Windows), OpenSSL, BoringSSL, AWS-LC, QuicTLS, LibreSSL, AmiSSL, wolfSSL and rustls.

### curl

`curl` is a command-line tool for getting or sending data, including files, using URL syntax. `curl` provides an interface to the `libcurl` library; it supports every protocol `libcurl` supports.

`curl` supports HTTPS, and performs SSL or TLS certificate verification by default. When `curl` connects to a remote server via HTTPS, it will obtain the remote server certificate, then checks against its CA certificate store the validity of the remote server to ensure the remote server is the one it claims to be. Some `curl` packages are bundled with a CA certificate store file. There are several options to specify a CA certificate, such as `--cacert` and `--capath`. The `--cacert` option can be used to specify the location of the CA certificate store file.

Starting with Windows 10 version 1809, Windows ships with `curl.exe`. On Microsoft Windows, if a CA certificate file is not specified, curl will look for the `curl-ca-bundle.crt` file in the following locations, in the order given:

1. App's folder (where `curl.exe` is located)
2. Current working directory
3. `C:\Windows\System32` directory
4. `C:\Windows` directory
5. Directories specified in the `PATH` environment variable

`curl` will return an error message if the remote server is using a self-signed certificate, or if the remote server certificate is not signed by a CA listed in the CA cert file. `-k` or `--insecure` option can be used to skip certificate verification. Alternatively, if the remote server is trusted, the remote server CA certificate can be added to the CA certificate store file.

### tiny-curl

`tiny-curl` is a lightweight version of libcurl developed by wolfSSL Inc. for embedded and resource-constrained devices. It implements HTTPS functionality in roughly 100 KB of code on typical 32-bit architectures.

## Licensing

curl and libcurl are distributed under the MIT License. tiny-curl, a version of curl optimized for embedded systems and supported by wolfSSL, is available under both the GNU GPLv3-or-later and commercial licensing.

Rock-solid curl, the long-term support (LTS) edition, uses the same curl license by default, with an option for commercial licensing for organizations that require contractual support or warranty coverage.
