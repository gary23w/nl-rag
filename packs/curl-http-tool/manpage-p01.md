---
title: "curl (part 1/5)"
source: https://curl.se/docs/manpage.html
domain: curl-http-tool
license: CC-BY-SA-4.0
tags: curl http, http client, data transfer, command-line http
fetched: 2026-07-02
part: 1/5
---

# curl

Options

Bottom right handle resizes.

--abstract-unix-socket

--alt-svc

--anyauth

-a, --append

--aws-sigv4

--basic

--ca-native

--cacert

--capath

--cert-status

--cert-type

-E, --cert

--ciphers

--compressed-ssh

--compressed

-K, --config

--connect-timeout

--connect-to

-C, --continue-at

-c, --cookie-jar

-b, --cookie

--create-dirs

--create-file-mode

--crlf

--crlfile

--curves

--data-ascii

--data-binary

--data-raw

--data-urlencode

-d, --data

--delegation

--digest

--disable-eprt

--disable-epsv

-q, --disable

--disallow-username-in-url

--dns-interface

--dns-ipv4-addr

--dns-ipv6-addr

--dns-servers

--doh-cert-status

--doh-insecure

--doh-url

--dump-ca-embed

-D, --dump-header

--ech

--egd-file

--engine

--etag-compare

--etag-save

--expect100-timeout

--fail-early

--fail-with-body

-f, --fail

--false-start

--form-escape

--form-string

-F, --form

--ftp-account

--ftp-alternative-to-user

--ftp-create-dirs

--ftp-method

--ftp-pasv

-P, --ftp-port

--ftp-pret

--ftp-skip-pasv-ip

--ftp-ssl-ccc-mode

--ftp-ssl-ccc

--ftp-ssl-control

-G, --get

-g, --globoff

--happy-eyeballs-timeout-ms

--haproxy-clientip

--haproxy-protocol

-I, --head

-H, --header

-h, --help

--hostpubmd5

--hostpubsha256

--hsts

--http0.9

-0, --http1.0

--http1.1

--http2-prior-knowledge

--http2

--http3-only

--http3

--ignore-content-length

-k, --insecure

--interface

--ip-tos

--ipfs-gateway

-4, --ipv4

-6, --ipv6

--json

-j, --junk-session-cookies

--keepalive-cnt

--keepalive-time

--key-type

--key

--krb

--libcurl

--limit-rate

-l, --list-only

--local-port

--location-trusted

-L, --location

--login-options

--mail-auth

--mail-from

--mail-rcpt-allowfails

--mail-rcpt

-M, --manual

--max-filesize

--max-redirs

-m, --max-time

--metalink

--mptcp

--negotiate

--netrc-file

--netrc-optional

-n, --netrc

-:, --next

--no-alpn

-N, --no-buffer

--no-clobber

--no-keepalive

--no-npn

--no-progress-meter

--no-sessionid

--noproxy

--ntlm-wb

--ntlm

--oauth2-bearer

--output-dir

-o, --output

--parallel-immediate

--parallel-max

-Z, --parallel

--pass

--path-as-is

--pinnedpubkey

--post301

--post302

--post303

--preproxy

-#, --progress-bar

--proto-default

--proto-redir

--proto

--proxy-anyauth

--proxy-basic

--proxy-ca-native

--proxy-cacert

--proxy-capath

--proxy-cert-type

--proxy-cert

--proxy-ciphers

--proxy-crlfile

--proxy-digest

--proxy-header

--proxy-http2

--proxy-insecure

--proxy-key-type

--proxy-key

--proxy-negotiate

--proxy-ntlm

--proxy-pass

--proxy-pinnedpubkey

--proxy-service-name

--proxy-ssl-allow-beast

--proxy-ssl-auto-client-cert

--proxy-tls13-ciphers

--proxy-tlsauthtype

--proxy-tlspassword

--proxy-tlsuser

--proxy-tlsv1

-U, --proxy-user

-x, --proxy

--proxy1.0

-p, --proxytunnel

--pubkey

-Q, --quote

--random-file

-r, --range

--rate

--raw

-e, --referer

-J, --remote-header-name

--remote-name-all

-O, --remote-name

-R, --remote-time

--remove-on-error

--request-target

-X, --request

--resolve

--retry-all-errors

--retry-connrefused

--retry-delay

--retry-max-time

--retry

--sasl-authzid

--sasl-ir

--service-name

-S, --show-error

-i, --show-headers

-s, --silent

--skip-existing

--socks4

--socks4a

--socks5-basic

--socks5-gssapi-nec

--socks5-gssapi-service

--socks5-gssapi

--socks5-hostname

--socks5

-Y, --speed-limit

-y, --speed-time

--ssl-allow-beast

--ssl-auto-client-cert

--ssl-no-revoke

--ssl-reqd

--ssl-revoke-best-effort

--ssl-sessions

--ssl

-2, --sslv2

-3, --sslv3

--stderr

--styled-output

--suppress-connect-headers

--tcp-fastopen

--tcp-nodelay

-t, --telnet-option

--tftp-blksize

--tftp-no-options

-z, --time-cond

--tls-earlydata

--tls-max

--tls13-ciphers

--tlsauthtype

--tlspassword

--tlsuser

--tlsv1.0

--tlsv1.1

--tlsv1.2

--tlsv1.3

-1, --tlsv1

--tr-encoding

--trace-ascii

--trace-config

--trace-ids

--trace-time

--trace

--unix-socket

-T, --upload-file

--upload-flags

--url-query

--url

-B, --use-ascii

-A, --user-agent

-u, --user

--variable

-v, --verbose

-V, --version

--vlan-priority

-w, --write-out

--xattr

curl

/

Docs

/

Tool

/

man page

# curl man page

Related:

FAQ

File a bug about this man page

HTTP Scripting

Tutorial

When options were added


## Name

curl - transfer a URL


## Synopsis

curl [options / URLs]


## Description

curl is a tool for transferring data from or to a server using URLs. It supports these protocols: DICT, FILE, FTP, FTPS, GOPHER, GOPHERS, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, MQTT, MQTTS, POP3, POP3S, RTSP, SCP, SFTP, SMB, SMBS, SMTP, SMTPS, TELNET, TFTP, WS and WSS.

curl is powered by libcurl for all transfer-related features. See libcurl for details.


## Url

The URL syntax is protocol-dependent. You can find a detailed description in RFC 3986.

If you provide a URL without a leading "protocol://" scheme, curl guesses what protocol you want. It then defaults to HTTP but assumes others based on often-used hostname prefixes. For example, for hostnames starting with "ftp." curl assumes you want FTP.

You can specify any amount of URLs on the command line. They are fetched in a sequential manner in the specified order unless you use --parallel. You can specify command line options and URLs mixed and in any order on the command line.

curl attempts to reuse connections when doing multiple transfers, so that getting many files from the same server does not use multiple connects and setup handshakes. This improves speed. Connection reuse can only be done for URLs specified for a single command line invocation and cannot be performed between separate curl runs.

Everything provided on the command line that is not a command line option or its argument, curl assumes is a URL and treats it as such.


## Globbing

You can specify multiple URLs or parts of URLs by writing lists within braces or ranges within brackets. We call this "globbing".

Provide a list with three different names like this:

```
https://fun.example/{one,two,three}.jpg
 
sftp://{one,two,three}.example/README
```

Do sequences of alphanumeric series by using [] as in:

```
ftp://ftp.example.com/file[1-100].txt
```

With leading zeroes:

```
ftp://ftp.example.com/file[001-100].txt
```

With letters through the alphabet:

```
ftp://ftp.example.com/file[a-z].txt
```

Nested sequences are not supported, but you can use several ones next to each other:

```
https://example.com/archive[1996-1999]/vol[1-4]/part{a,b,c}.html
```

You can specify a step counter for the ranges to get every Nth number or letter:

```
https://example.com/file[1-100:10].txt
 
https://example.com/file[a-z:2].txt
```

When using [] or {} sequences when invoked from a command line prompt, you probably have to put the full URL within double quotes to avoid the shell from interfering with it. This also goes for other characters treated special, like for example '&', '?' and '*'.

The separate globbing components can be referenced in the --output option to allow pieces to be reused in the target filename.

Starting in curl 8.21.0, the separate globbing parts can be named and referenced by their names. The case sensitive alphanumeric name is set enclosed within angle brackets after the opening character. Examples:

```
https://fun.example/{<number>one,two,three}.jpg
 
ftp://ftp.example.com/file[<range>1-100].txt
```

Setting the same glob name twice is an error.

Switch off globbing with --globoff.


## Variables

curl supports command line variables (added in 8.3.0). Set variables with --variable name=content or --variable name@file (where "file" can be stdin if set to a single dash (-)).

Variable contents can be expanded in option parameters using "{{name}}" if the option name is prefixed with "--expand-". This gets the contents of the variable "name" inserted, or a blank if the name does not exist as a variable. Insert "{{" verbatim in the string by prefixing it with a backslash, like "\{{".

You can access and expand environment variables by importing them with "--variable %name". This imports the variable called "name" but exits with an error if that environment variable is not already set. To provide a default value in case it is not already set, use "--variable %name=content" or "--variable %name@content".

Example: get the USER environment variable and expand into the URL, fail if USER is not set:

```
--variable '%USER'
--expand-url = "https://example.com/api/{{USER}}/method"
```

When expanding variables, curl supports a set of functions that can make the variable contents more convenient to use. It can trim leading and trailing white space with "trim", output the contents as a JSON quoted string with "json", URL encode the string with "url", base64 encode it with "b64" and base64 decode it with "64dec". To apply functions to a variable expansion, add them colon separated to the right side of the variable. Variable content holding null bytes that are not encoded when expanded causes an error.

Example: get the contents of a file called $HOME/.secret into a variable called "fix". Make sure that the content is trimmed and percent-encoded when sent as POST data:

```
--variable %HOME
--expand-variable fix@{{HOME}}/.secret
--expand-data "{{fix:trim:url}}"
https://example.com/
```

Command line variables and expansions were added in 8.3.0.


## Output

If not told otherwise, curl writes the received data to stdout. It can be instructed to instead save that data into a local file, using the --output or --remote-name options. If curl is given multiple URLs to transfer on the command line, it similarly needs multiple options for where to save them.

curl does not parse or otherwise "understand" the content it gets or writes as output. It does no encoding or decoding, unless explicitly asked to with dedicated command line options.


## Protocols

curl supports numerous protocols, or put in URL terms: schemes. Your particular build may not support them all.

DICT

Lets you lookup words using online dictionaries.

FILE

Read or write local files. curl does not support accessing "file://" URL remotely, but when running on Microsoft Windows using the native UNC approach works. Only absolute paths.

FTP(S)

curl supports the File Transfer Protocol with a lot of tweaks and levers. With or without using TLS.

GOPHER(S)

Retrieve files.

HTTP(S)

curl supports HTTP with numerous options and variations. It can speak HTTP version 0.9, 1.0, 1.1, 2 and 3 depending on build options and the correct command line options.

IMAP(S)

Using the mail reading protocol, curl can download emails for you. With or without using TLS.

LDAP(S)

curl can do directory lookups for you, with or without TLS.

MQTT

curl supports MQTT version 3. Downloading over MQTT equals subscribing to a topic while uploading/posting equals publishing on a topic. MQTT over TLS is not supported (yet).

POP3(S)

Downloading from a pop3 server means getting an email. With or without using TLS.

RTSP

curl supports RTSP 1.0 downloads.

SCP

curl supports SSH version 2 scp transfers.

SFTP

curl supports SFTP (draft 5) done over SSH version 2.

SMB(S)

curl supports SMB version 1 for upload and download.

SMTP(S)

Uploading contents to an SMTP server means sending an email. With or without TLS.

TELNET

Fetching a telnet URL starts an interactive session where it sends what it reads on stdin and outputs what the server sends it.

TFTP

curl can do TFTP downloads and uploads.

WS(S)

WebSocket done over HTTP/1. WSS implies that it works over HTTPS.


## Progress meter

curl normally displays a progress meter during operations, indicating the amount of transferred data, transfer speeds and estimated time left, etc. The progress meter displays the transfer rate in bytes per second. The used suffixes ("k" for kilo, "M" for mega, "G" for giga, "T" for tera, "P" for peta and "E" for exa) are 1024 based. For example 1k is 1024 bytes. 1M is 1048576 bytes. Strictly speaking this makes the units kibibyte and mebibyte etc.

curl displays this data to the terminal by default, so if you invoke curl to do an operation and it is about to write data to the terminal, it disables the progress meter as otherwise it would mess up the output mixing progress meter and response data.

If you want a progress meter for HTTP POST or PUT requests, you need to redirect the response output to a file, using shell redirect (>), --output or similar.

This does not apply to FTP upload as that operation does not spit out any response data to the terminal.

If you prefer a progress bar instead of the regular meter, --progress-bar is your friend. You can also disable the progress meter completely with the --silent option.


## Version

This man page describes curl 8.21.1. If you use a later version, chances are this man page does not fully document it. If you use an earlier version, this document tries to include version information about which specific version that introduced changes.

You can always learn which the latest curl version is by running

```
curl https://curl.se/info
```

The online version of this man page is always showing the latest incarnation: https://curl.se/docs/manpage.html


## Options

Options start with one or two dashes. Many of the options require an additional value next to them. If provided text does not start with a dash, it is presumed to be and treated as a URL.

The short "single-dash" form of the options, -d for example, may be used with or without a space between it and its value, although a space is a recommended separator. The long double-dash form, --data for example, requires a space between it and its value.

Short version options that do not need any additional values can be used immediately next to each other, like for example you can specify all the options -O, -L and -v at once as -OLv.

In general, all boolean options are enabled with --option and yet again disabled with --no-option. That is, you use the same option name but prefix it with "no-". In this list we mostly show the --option version of them.

When --next is used, it resets the parser state and you start again with a clean option state, except for the options that are global. Global options retain their values and meaning even after --next.

If the long option name ends with an equals sign ("="), the argument is the text following on its right side. (Added in 8.16.0)

The first argument that is exactly two dashes ("--"), marks the end of options; any argument after the end of options is interpreted as a URL argument even if it starts with a dash.

curl does little to no verification of the contents of command line arguments. Passing in "creative octets" like newlines might trigger unexpected results.

The following options are global: --fail-early, --libcurl, --parallel-immediate, --parallel-max-host, --parallel-max, --parallel, --progress-bar, --rate, --show-error, --stderr, --styled-output, --trace-ascii, --trace-config, --trace-ids, --trace-time, --trace and --verbose.
