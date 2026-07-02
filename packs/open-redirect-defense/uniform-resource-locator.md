---
title: "URL - Wikipedia"
source: https://en.wikipedia.org/wiki/Uniform_Resource_Locator
domain: open-redirect-defense
license: CC-BY-SA-4.0
tags: open redirect vulnerability, unvalidated redirect, url forwarding abuse, redirect allowlist
fetched: 2026-07-02
---

# URL

(Redirected from

Uniform Resource Locator

)

A **uniform resource locator** (**URL**), colloquially known as a **web address**, is a reference to a resource on the World Wide Web. A URL specifies the location of a resource on a computer network and a mechanism for retrieving it. A URL is a specific type of Uniform Resource Identifier (URI), although many people use the two terms interchangeably. A URL is most commonly used to reference a web page (HTTP/HTTPS) but is also used for file transfer (FTP), email (mailto), database access (JDBC), and many other applications.

Most web browsers display the URL of a web page above the page in an address bar. As an example of a web page URL, `https://www.example.com/index.html` indicates protocol `https`, hostname `www.example.com`, and file name `index.html`.

## History

The Uniform Resource Locator was defined in RFC 1738 in 1994 by Tim Berners-Lee, the inventor of the World Wide Web, and the URI working group of the Internet Engineering Task Force (IETF), as an outcome of collaboration started at the IETF Living Documents birds of a feather session in 1992.

The format combines the pre-existing system of domain names (created in 1985) with file path syntax, where slashes are used to separate directory and filenames. Conventions already existed where server names could be prefixed to complete file paths, preceded by a double slash (`//`).

Berners-Lee later expressed regret at the use of dots to separate the parts of the domain name within URIs, wishing he had used slashes throughout, and also said that, given the colon following the first component of a URI, the two slashes before the domain name were unnecessary.

Early WorldWideWeb collaborators, including Berners-Lee, originally proposed the use of UDIs: Universal Document Identifiers. An early (1993) draft of the HTML Specification referred to "Universal" Resource Locators. This was dropped some time between June 1994 and October 1994. In his book *Weaving the Web*, Berners-Lee emphasizes his preference for the original inclusion of "universal" in the expansion rather than the word "uniform", to which it was later changed, and he gives a brief account of the contention that led to the change.

## Syntax

Every HTTP URL conforms to the syntax of a generic URI. The URI generic syntax consists of five *components* organized hierarchically in order of decreasing significance from left to right:

```mw
URI = scheme ":" ["//" authority] path ["?" query] ["#" fragment]
```

A component is *undefined* if it has an associated delimiter and the delimiter does not appear in the URI; the scheme and path components are always defined. A component is *empty* if it has no characters; the scheme component is always non-empty.

The authority component consists of *subcomponents*:

```mw
authority = [userinfo "@"] host [":" port]
```

This is represented in a syntax diagram as:

The URI comprises:

- A non-empty **scheme** component followed by a colon (`:`), consisting of a sequence of characters beginning with a letter and followed by any combination of letters, digits, plus (`+`), period (`.`), or hyphen (`-`). Although schemes are case-insensitive, the canonical form is lowercase and documents that specify schemes must do so with lowercase letters. Examples of popular schemes include `http`, `https`, `ftp`, `mailto`, `file`, `data` and `irc`. URI schemes should be registered with the Internet Assigned Numbers Authority (IANA), although non-registered schemes are used in practice.
- An optional **authority** component preceded by two slashes (`//`), comprising:
  - An optional **userinfo** subcomponent followed by an at symbol (`@`), that may consist of a user name and an optional password preceded by a colon (`:`). Use of the format `username:password` in the userinfo subcomponent is deprecated for security reasons. Applications should not render as clear text any data after the first colon (`:`) found within a userinfo subcomponent unless the data after the colon is the empty string (indicating no password).
  - A **host** subcomponent, consisting of either a registered name (including but not limited to a hostname) or an IP address. IPv4 addresses must be in dot-decimal notation, and IPv6 addresses must be enclosed in brackets (`[]`).
  - An optional **port** subcomponent preceded by a colon (`:`), consisting of decimal digits.
- A **path** component, consisting of a sequence of path segments separated by a slash (`/`). A path is always defined for a URI, though the defined path may be empty (zero length). A segment may also be empty, resulting in two consecutive slashes (`//`) in the path component. A path component may resemble or map exactly to a file system path but does not always imply a relation to one. If an authority component is defined, then the path component must either be empty or begin with a slash (`/`). If an authority component is undefined, then the path cannot begin with an empty segment—that is, with two slashes (`//`)—since the following characters would be interpreted as an authority component.

By convention, in

http

and

https

URIs, the last part of a

path

is named

pathinfo

and it is optional. It is composed by zero or more path segments that do not refer to an existing physical resource name (e.g. a file, an internal module program or an executable program) but to a logical part (e.g. a command or a qualifier part) that has to be passed separately to the first part of the path that identifies an executable module or program managed by a

web server

; this is often used to select dynamic content (a document, etc.) or to tailor it as requested (see also:

CGI

and PATH_INFO, etc.).

Example:

URI:

"http://www.example.com/questions/3456/my-document"

where:

"/questions"

is the first part of the

path

(an executable module or program) and

"/3456/my-document"

is the second part of the

path

named

pathinfo

, which is passed to the executable module or program named

"/questions"

to select the requested document.

An

http

or

https

URI containing a

pathinfo

part without a

query

part may also be referred to as a '

clean URL

,' whose last part may be a '

slug

.'

| Query delimiter | Example |
|---|---|
| Ampersand (`&`) | `key1=value1&key2=value2` |
| Semicolon (`;`) | `key1=value1;key2=value2` |

- An optional **query** component preceded by a question mark (`?`), consisting of a query string of non-hierarchical data. Its syntax is not well defined, but by convention is most often a sequence of attribute–value pairs separated by a delimiter.
- An optional **fragment** component preceded by a hash (`#`). The fragment contains a fragment identifier providing direction to a secondary resource, such as a section heading in an article identified by the remainder of the URI. When the primary resource is an HTML document, the fragment is often an `id` attribute of a specific element, and web browsers will scroll this element into view.

A web browser will usually dereference a URL by performing an HTTP request to the specified host, by default on port number 80. URLs using the `https` scheme require that requests and responses be made over a secure connection to the website.

## Internationalized URL

Internet users are distributed throughout the world using a wide variety of languages and alphabets, and expect to be able to create URLs in their own local alphabets. An Internationalized Resource Identifier (IRI) is a form of URL that includes Unicode characters. All modern browsers support IRIs. The parts of the URL requiring special treatment for different alphabets are the domain name and path.

The domain name in the IRI is known as an Internationalized Domain Name (IDN). Web and Internet software automatically convert the domain name into punycode usable by the Domain Name System; for example, the Chinese URL `http://例子.卷筒纸` becomes `http://xn--fsqu00a.xn--3lr804guic/`. The `xn--` indicates that the character was not originally ASCII.

The URL path name can also be specified by the user in the local writing system. If not already encoded, it is converted to UTF-8, and any characters not part of the basic URL character set are escaped as hexadecimal using percent-encoding; for example, the Japanese URL `http://example.com/引き割り.html` becomes `http://example.com/%E5%BC%95%E3%81%8D%E5%89%B2%E3%82%8A.html`. The target computer decodes the address and displays the page.

## Protocol-relative URLs

Protocol-relative links (PRL), also known as protocol-relative URLs (PRURL), are URLs that have no protocol specified. For example, `//example.com` will use the protocol of the current page, typically HTTP or HTTPS.
