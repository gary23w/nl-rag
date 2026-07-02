---
title: "Directory traversal attack"
source: https://en.wikipedia.org/wiki/Directory_traversal_attack
domain: path-traversal-defense
license: CC-BY-SA-4.0
tags: directory traversal, path traversal defense, canonical path resolution, file access control
fetched: 2026-07-02
---

# Directory traversal attack

A **directory traversal**, **path traversal**, or **dot-dot-slash** attack exploits insufficient security validation or sanitization of user-supplied file names, such that characters representing "traverse to parent directory" are passed through to the operating system's file system API. An affected application can be exploited to gain unauthorized access to the file system.

## Examples

### In PHP

A typical example of a vulnerable application in PHP code is:

```mw
<?php
$template = "red.php";
if (isset($_COOKIE["TEMPLATE"])) {
    $template = $_COOKIE["TEMPLATE"];
}
include "/home/users/phpguru/templates/" . $template;
```

An attack against this system could be to send the following HTTP request:

```mw
GET /vulnerable.php HTTP/1.0
Cookie: TEMPLATE=../../../../../../../../../etc/passwd
```

The server would then generate a response such as:

```mw
HTTP/1.0 200 OK
Content-Type: text/html
Server: Apache

root:fi3sED95ibqR6:0:1:System Operator:/:/bin/ksh 
daemon:*:1:1::/tmp: 
phpguru:f8fk3j1OIf31.:182:100:Developer:/home/users/phpguru/:/bin/csh
```

The repeated `../` characters after `/home/users/phpguru/templates/` have caused `include()` to traverse to the root directory, and then include the Unix password file `/etc/passwd`.

Unix `/etc/passwd` is a common file used to demonstrate directory traversal, as it is often used by crackers to try cracking the passwords. However, in more recent Unix systems, the `/etc/passwd` file does not contain the hashed passwords, and they are instead located in the `/etc/shadow` file, which cannot be read by unprivileged users on the machine. Even in that case, though, reading `/etc/passwd` does still show a list of user accounts, which could then become a starting point for further attacks.

### Zip Slip vulnerability

Another example is the "Zip Slip" vulnerability that affects several archive file formats like ZIP.

## Variations

Directory traversal in its simplest form uses the `../` pattern. Some common variations are listed below:

### Microsoft Windows

Microsoft Windows and DOS directory traversal uses the `..\` or `../` patterns.

Each partition has a separate root directory (labeled `C:\` where C could be any partition), and there is no common root directory above that. This means that for most directory vulnerabilities on Windows, attacks are limited to a single partition.

Directory traversal has been the cause of numerous Microsoft vulnerabilities.

### Percent encoding in URIs

Some web applications attempt to prevent directory traversal by scanning the path of a request URI for patterns such as `../`. This check is sometimes mistakenly performed before percent-decoding, causing URIs containing patterns like `%2e%2e/` to be accepted despite being decoded into `../` before actual use.

#### Double encoding

Percent decoding may accidentally be performed multiple times; once before validation, but again afterwards, making the application vulnerable to Double percent-encoding attacks in which illegal characters are replaced by their double-percent-encoded form in order to bypass security countermeasures. For example, in a double percent-encoding attack, `../` may be replaced by its double-percent-encoded form `%252E%252E%252F`. This kind of vulnerability notably affected versions 5.0 and earlier of Microsoft's IIS web server software.

#### UTF-8

A badly implemented UTF-8 decoder may accept characters encoded using more bytes than necessary, leading to overlong encodings, such as `%c0%ae` instead of `%2e` to represent `.`. This is specifically forbidden by the UTF-8 standard, but has still led to directory traversal vulnerabilities in software such as the IIS web server.

### Archives

Some archive formats like zip allow for directory traversal attacks: files in the archive can be written such that they overwrite files on the filesystem by backtracking. Code that extracts archive files can be written to check that the paths of the files in the archive do not engage in path traversal.

## Prevention

A possible algorithm for preventing directory traversal would be to:

1. Process URI requests that do not result in a file request, e.g., executing a hook into user code, before continuing below.
2. When a URI request for a file/directory is to be made, build a full path to the file/directory if it exists, and normalize all characters (e.g., `%20` converted to spaces).
3. It is assumed that a 'Document Root' fully qualified, normalized, path is known, and this string has a length *N*. Assume that no files outside this directory can be served.
4. Ensure that the first *N* characters of the fully qualified path to the requested file is exactly the same as the 'Document Root'.
5. If so, allow the file to be returned.
6. If not, return an error, since the request is clearly out of bounds from what the web-server should be allowed to serve.

Using a hard-coded predefined file extension to suffix the path does not necessarily limit the scope of the attack to files of that file extension.

```mw
<?php
include $_GET["file"] . ".html";
```

The user can use the NULL character (indicating the end of the string) in order to bypass everything after the `$_GET`. (This is PHP-specific.)
