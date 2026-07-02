---
title: "GNU Wget 1.25.0 Manual (part 1/6)"
source: https://www.gnu.org/software/wget/manual/wget.html
domain: wget
license: CC-BY-SA-4.0
tags: wget download, file download, recursive download, command-line http
fetched: 2026-07-02
part: 1/6
---

# Wget 1.25.0

This file documents the GNU Wget utility for downloading network data.

Copyright © 1996–2011, 2015, 2018–2024 Free Software Foundation, Inc.

Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled “GNU Free Documentation License”.


## 1 Overview

GNU Wget is a free utility for non-interactive download of files from the Web. It supports HTTP, HTTPS, and FTP protocols, as well as retrieval through HTTP proxies.

This chapter is a partial overview of Wget’s features.

- Wget is non-interactive, meaning that it can work in the background, while the user is not logged on. This allows you to start a retrieval and disconnect from the system, letting Wget finish the work. By contrast, most of the Web browsers require constant user’s presence, which can be a great hindrance when transferring a lot of data.
- Wget can follow links in HTML, XHTML, and CSS pages, to create local versions of remote web sites, fully recreating the directory structure of the original site. This is sometimes referred to as “recursive downloading.” While doing that, Wget respects the Robot Exclusion Standard (/robots.txt). Wget can be instructed to convert the links in downloaded files to point at the local files, for offline viewing.
- File name wildcard matching and recursive mirroring of directories are available when retrieving via FTP. Wget can read the time-stamp information given by both HTTP and FTP servers, and store it locally. Thus Wget can see if the remote file has changed since last retrieval, and automatically retrieve the new version if it has. This makes Wget suitable for mirroring of FTP sites, as well as home pages.
- Wget has been designed for robustness over slow or unstable network connections; if a download fails due to a network problem, it will keep retrying until the whole file has been retrieved. If the server supports regetting, it will instruct the server to continue the download from where it left off.
- Wget supports proxy servers, which can lighten the network load, speed up retrieval and provide access behind firewalls. Wget uses the passive FTP downloading by default, active FTP being an option.
- Wget supports IP version 6, the next generation of IP. IPv6 is autodetected at compile-time, and can be disabled at either build or run time. Binaries built with IPv6 support work well in both IPv4-only and dual family environments.
- Built-in features offer mechanisms to tune which links you wish to follow (see Following Links).
- The progress of individual downloads is traced using a progress gauge. Interactive downloads are tracked using a “thermometer”-style gauge, whereas non-interactive ones are traced with dots, each dot representing a fixed amount of data received (1KB by default). Either gauge can be customized to your preferences.
- Most of the features are fully configurable, either through command line options, or via the initialization file .wgetrc (see Startup File). Wget allows you to define *global* startup files (/usr/local/etc/wgetrc by default) for site settings. You can also specify the location of a startup file with the –config option. To disable the reading of config files, use –no-config. If both –config and –no-config are given, –no-config is ignored.
- Finally, GNU Wget is free software. This means that everyone may use it, redistribute it and/or modify it under the terms of the GNU General Public License, as published by the Free Software Foundation (see the file COPYING that came with GNU Wget, for details).
