---
title: "Wget"
source: https://en.wikipedia.org/wiki/Wget
domain: wget
license: CC-BY-SA-4.0
tags: wget download, file download, recursive download, command-line http
fetched: 2026-07-02
---

# Wget

**GNU Wget** (or just **Wget**, formerly **Geturl**, also written as its package name, **wget**) is a computer program that retrieves content from web servers. It is part of the GNU Project. Its name derives from "World Wide Web" and "*get*", a HTTP request method. It supports downloading via HTTP, HTTPS, and FTP.

Its features include recursive download, conversion of links for offline viewing of local HTML, and support for proxies. It appeared in 1996, coinciding with the boom of popularity of the Web, causing its wide use among Unix users and distribution with most major Linux distributions. Wget is written in C, and can be easily installed on any Unix-like system. Wget has been ported to Microsoft Windows, macOS, OpenVMS, HP-UX, AmigaOS, MorphOS, and Solaris. Since version 1.14, Wget has been able to save its output in the web archiving standard WARC format.

## History

Wget descends from an earlier program named Geturl by the same author, the development of which commenced in late 1995. The name changed to Wget after the author became aware of an earlier Amiga program named GetURL, written by James Burton in AREXX.

Wget filled a gap in the inconsistent web-downloading software available in the mid-1990s. No single program could reliably use both HTTP and FTP to download files. Existing programs either supported FTP (such as NcFTP and dl) or were written in Perl, which was not yet ubiquitous. While Wget was inspired by features of some of the existing programs, it supported both HTTP and FTP and could be built using only the standard development tools found on every Unix system.

At that time many Unix users struggled behind extremely slow university and dial-up Internet connections, leading to a growing need for a downloading agent that could deal with transient network failures without assistance from the human operator.

## Features

### Robustness

Wget has been designed for robustness over slow or unstable network connections. If a download does not complete due to a network problem, Wget will automatically try to continue the download from where it left off, and repeat this until the whole file has been retrieved. It was one of the first clients to make use of the then-new `Range` HTTP header to support this feature.

### Recursive download

Wget can optionally work like a web crawler by extracting resources linked from HTML pages and downloading them in sequence, repeating the process recursively until all the pages have been downloaded or a maximum recursion depth specified by the user has been reached. The downloaded pages are saved in a directory structure resembling that on the remote server. This "recursive download" enables partial or complete mirroring of web sites via HTTP. Links in downloaded HTML pages can be adjusted to point to locally downloaded material for offline viewing. When performing this kind of automatic mirroring of web sites, Wget supports the Robots Exclusion Standard (unless the option `-e robots=off` is used).

Recursive download works with FTP as well, where Wget issues the `LIST` command to find which additional files to download, repeating this process for directories and files under the one specified in the top URL. Shell-like wildcards are supported when the download of FTP URLs is requested.

When downloading recursively over either HTTP or FTP, Wget can be instructed to inspect the timestamps of local and remote files, and download only the remote files newer than the corresponding local ones. This allows easy mirroring of HTTP and FTP sites, but is considered inefficient and more error-prone when compared to programs designed for mirroring from the ground up, such as rsync. On the other hand, Wget does not require special server-side software for this task.

### Non-interactiveness

Wget is non-interactive in the sense that, once started, it does not require user interaction and does not need to control a TTY, being able to log its progress to a separate file for later inspection. Users can start Wget and log off, leaving the program unattended. By contrast, most graphical or text user interface web browsers require the user to remain logged in and to manually restart failed downloads, which can be a great hindrance when transferring a lot of data.

### Portability

Written in a highly portable style of C with minimal dependencies on third-party libraries, Wget requires little more than a C compiler and a BSD-like interface to TCP/IP networking. Designed as a Unix program invoked from the Unix shell, the program has been ported to numerous Unix-like environments and systems, including Microsoft Windows via Cygwin, and macOS. It is also available as a native Microsoft Windows program as one of the GnuWin packages.

### Other features

- Wget supports download through proxies, which are widely deployed to provide web access inside company firewalls and to cache and quickly deliver frequently accessed content.
- It makes use of HTTP persistent connections where available.
- IPv6 is supported on systems that include the appropriate interfaces.
- SSL/TLS is supported for encrypted downloads using the OpenSSL or GnuTLS library.
- Files larger than 2 GiB are supported on 32-bit systems that include the appropriate interfaces.
- Download speed may be throttled to avoid using up all of the available bandwidth.
- Can save its output in the web archiving standard WARC format, deduplicating from an associated CDX file as required.

## Authors and copyright

GNU Wget was written by Hrvoje Nikšić with contributions by many other people, including Dan Harkless, Ian Abbott, and Mauro Tortonesi. Significant contributions are credited in the *AUTHORS* file included in the distribution, and all remaining ones are documented in the changelogs, also included with the program. Wget is currently maintained by Giuseppe Scrivano and Tim Rühsen.

The copyright to Wget belongs to the Free Software Foundation, whose policy is to require copyright assignments for all non-trivial contributions to GNU software.

### License

GNU Wget is distributed under the terms of the GNU General Public License, version 3 or later, with a special exception that allows distribution of binaries linked against the OpenSSL library. The text of the exception follows:

> Additional permission under GNU GPL version 3 section 7
> 
> If you modify this program, or any covered work, by linking or combining it with the OpenSSL project's OpenSSL library (or a modified version of that library), containing parts covered by the terms of the OpenSSL or SSLeay licenses, the Free Software Foundation grants you additional permission to convey the resulting work. Corresponding Source for a non-source form of such a combination shall include the source code for the parts of OpenSSL used as well as that of the covered work.

It is expected that the exception clause will be removed once Wget is modified to also link with the GnuTLS library.

Wget's documentation, in the form of a Texinfo reference manual, is distributed under the terms of the GNU Free Documentation License, version 1.2 or later. The man page usually distributed on Unix-like systems is automatically generated from a subset of the Texinfo manual and falls under the terms of the same license.

## Development

Wget is developed in an open fashion, most of the design decisions typically being discussed on the public mailing list followed by users and developers. Bug reports and patches are relayed to the same list.

### Source contribution

The preferred method of contributing to Wget's code and documentation is through source updates in the form of textual patches generated by the diff utility. Patches intended for inclusion in Wget are submitted to the mailing list where they are reviewed by the maintainers. Patches that pass the maintainers' scrutiny are installed in the sources. Instructions on patch creation as well as style guidelines are outlined on the project's wiki.

The source code can also be tracked via a remote version control repository that hosts revision history beginning with the 1.5.3 release. The repository is currently running Git. Prior to that, the source code had been hosted on (in reverse order): Bazaar, Mercurial, Subversion, and via CVS.

#### Release

When a sufficient number of features or bug fixes accumulate during development, Wget is released to the general public via the GNU FTP site and its mirrors. Being entirely run by volunteers, there is no external pressure to issue a release nor are there enforceable release deadlines.

Releases are numbered as versions of the form of *major.minor[.revision]*, such as *Wget 1.11* or *Wget 1.8.2*. An increase of the major version number represents large and possibly incompatible changes in Wget's behavior or a radical redesign of the code base. An increase of the minor version number designates addition of new features and bug fixes. A new revision indicates a release that, compared to the previous revision, only contains bug fixes. Revision zero is omitted, meaning that for example Wget 1.11 is the same as 1.11.0. Wget does not use the odd-even release number convention popularized by Linux.

#### Popular references

Wget makes an appearance in the 2010 Columbia Pictures motion picture release, *The Social Network*. The lead character, a somewhat fictionalized version of Facebook co-founder Mark Zuckerberg, uses Wget to aggregate student photos from various Harvard University housing-facility directories.

### Notable releases

The following releases represent notable milestones in Wget's development. Features listed next to each release are edited for brevity and do not constitute comprehensive information about the release, which is available in the *NEWS* file distributed with Wget.

- Geturl 1.0, released January 1996, was the first publicly available release. The first English-language announcement can be traced to a Usenet news posting, which probably refers to Geturl 1.3.4 released in June.
- Wget 1.4.0, released November 1996, was the first version to use the name *Wget*. It was also the first release distributed under the terms of the GNU GPL, Geturl having been distributed under an ad hoc no-warranty license.
- Wget 1.4.3, released February 1997, was the first version released as part of the GNU project with the copyright assigned to the FSF.
- Wget 1.5.3, released September 1998, was a milestone in the program's popularity. This version was bundled with many Linux based distributions, which exposed the program to a much wider audience.
- Wget 1.6, released December 1999, incorporated many bug fixes for the (by then stale) 1.5.3 release, largely thanks to the effort of Dan Harkless.
- Wget 1.7, released June 2001, introduced SSL support, cookies, and persistent connections.
- Wget 1.8, released December 2001, added bandwidth throttling, new progress indicators, and the breadth-first traversal of the hyperlink graph.
- Wget 1.9, released October 2003, included experimental IPv6 support, and ability to POST data to HTTP servers.
- Wget 1.10, released June 2005, introduced large file support, IPv6 support on dual-family systems, NTLM authorization, and SSL improvements. The maintainership was picked up by Mauro Tortonesi.
- Wget 1.11, released January 2008, moved to version 3 of the GNU General Public License, and added preliminary support for the `Content-Disposition` header, which is often used by CGI scripts to indicate the name of a file for downloading. Security-related improvements were also made to the HTTP authentication code. Micah Cowan took over maintainership of the project.
- Wget 1.12, released September 2009, added support for parsing URLs from CSS content on the web, and for handling Internationalized Resource Identifiers.
- Wget 1.13, released August 2011, supports HTTP/1.1, fixed some portability issues, and used the GnuTLS library by default for secure connections.
- Wget 1.14, released August 2012, improved support for TLS and added support for RFC 2617 Digest Access Authentication.
- Wget 1.15, released January 2014, added `--https-only` and support for `Perfect-Forward` Secrecy.
- Wget 1.16, released October 2014, changed the default progress bar output, closed CVE-2014-4877, added support for libpsl to verify cookie domains, and introduced—start-pos to allow starting downloads from a specified position.
- Wget 1.17, released November 2015, removed FTP passive to active fallback due to privacy concerns, added support for FTPS and for `--if-modified-since`.
- Wget 1.18, released June 2016, resolved the CVE-2016-4971 issue, and added the `--bind-dns-address` and `--dns-servers` options.
- Wget 1.19, released February 2017, added new options for processing a Metalink file; version 1.19.1 added the `--retry-on-http-error` option to retry a download if the Web server responds with a given HTTP status code.
- Wget 1.20, released November 2018, added `--retry-on-host-error` for more reliability and `--accept-regex`, `--reject-regex` options for recursive FTP retrievals.

## Wget2

GNU Wget2 2.0.0 was released on 26 September 2021. It is licensed under the GPL-3.0-or-later license, and is wrapped around Libwget which is under the LGPL-3.0-or-later license. It has many improvements in comparison to Wget, particularly, in many cases Wget2 downloads much faster than Wget1.x due to support of the following protocols and technologies:

- HTTP/2,
- HTTP compression,
- parallel connections,
- use of If-Modified-Since HTTP header,
- TCP Fast Open.

Screenshot of GWget 1.0.4 in

Fedora

v12 with

GNOME

v2.28.2 installed

### GWget

GWget is a free software graphical user interface for Wget. It is developed by David Sedeño Fernández based on the GNOME software stack. GWget supports all of the main features that Wget does, as well as parallel downloads.

### Cliget

Cliget is an open source Firefox addon downloader that uses Curl, Wget and Aria2. It is developed by Zaid Abdulla.

## Clones

There exist clones of GNU Wget intended for embedded systems, which are often limited in memory and storage. They support its most basic options, usually limited to downloading.

- OpenWrt uclient-fetch
- BusyBox wget
- ToyBox wget
