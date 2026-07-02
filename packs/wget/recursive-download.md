---
title: "Recursive Download (GNU Wget 1.25.0 Manual)"
source: https://www.gnu.org/software/wget/manual/html_node/Recursive-Download.html
domain: wget
license: CC-BY-SA-4.0
tags: wget download, file download, recursive download, command-line http
fetched: 2026-07-02
---

## 3 Recursive Download

GNU Wget is capable of traversing parts of the Web (or a single HTTP or FTP server), following links and directory structure. We refer to this as to *recursive retrieval*, or *recursion*.

With HTTP URLs, Wget retrieves and parses the HTML or CSS from the given URL, retrieving the files the document refers to, through markup like `href` or `src`, or CSS URI values specified using the ‘url()’ functional notation. If the freshly downloaded file is also of type `text/html`, `application/xhtml+xml`, or `text/css`, it will be parsed and followed further.

Recursive retrieval of HTTP and HTML/CSS content is *breadth-first*. This means that Wget first downloads the requested document, then the documents linked from that document, then the documents linked by them, and so on. In other words, Wget first downloads the documents at depth 1, then those at depth 2, and so on until the specified maximum depth.

The maximum *depth* to which the retrieval may descend is specified with the ‘-l’ option. The default maximum depth is five layers.

When retrieving an FTP URL recursively, Wget will retrieve all the data from the given directory tree (including the subdirectories up to the specified depth) on the remote server, creating its mirror image locally. FTP retrieval is also limited by the `depth` parameter. Unlike HTTP recursion, FTP recursion is performed depth-first.

By default, Wget will create a local directory tree, corresponding to the one found on the remote server.

Recursive retrieving can find a number of applications, the most important of which is mirroring. It is also useful for WWW presentations, and any other opportunities where slow network connections should be bypassed by storing the files locally.

You should be warned that recursive downloads can overload the remote servers. Because of that, many administrators frown upon them and may ban access from your site if they detect very fast downloads of big amounts of content. When downloading from Internet servers, consider using the ‘-w’ option to introduce a delay between accesses to the server. The download will take a while longer, but the server administrator will not be alarmed by your rudeness.

Of course, recursive download may cause problems on your machine. If left to run unchecked, it can easily fill up the disk. If downloading from local network, it can also take bandwidth on the system, as well as consume memory and CPU.

Try to specify the criteria that match the kind of download you are trying to achieve. If you want to download only one page, use ‘--page-requisites’ without any additional recursion. If you want to download things under one directory, use ‘-np’ to avoid downloading things from other directories. If you want to download all the files from one directory, use ‘-l 1’ to make sure the recursion depth never exceeds one. See Following Links, for more information about this.

Recursive retrieval should be used with care. Don’t say you were not warned.
