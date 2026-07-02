---
title: "curl (part 5/5)"
source: https://curl.se/docs/manpage.html
domain: curl-http-tool
license: CC-BY-SA-4.0
tags: curl http, http client, data transfer, command-line http
fetched: 2026-07-02
part: 5/5
---

# curl

Example:

```
curl --verbose https://example.com
```

This option is mutually exclusive with --trace and --trace-ascii. See also --show-headers, --silent, --trace and --trace-ascii.

-V, --version

Display information about curl and the libcurl version it uses.

The first line includes the full version of curl, libcurl and other 3rd party libraries linked with the executable.

This line may contain one or more TLS libraries. curl can be built to support more than one TLS library which then makes curl - at start-up - select which particular backend to use for this invocation.

If curl supports more than one TLS library like this, the ones that are not selected by default are listed within parentheses. Thus, if you do not specify which backend to use (with the "CURL_SSL_BACKEND" environment variable) the one listed without parentheses is used. Such builds also have "MultiSSL" set as a feature.

The second line (starts with "Release-Date:") shows the release date.

The third line (starts with "Protocols:") shows all protocols that libcurl reports to support.

The fourth line (starts with "Features:") shows specific features libcurl reports to offer. Available features include:

alt-svc

Support for the Alt-Svc: header is provided.

AsynchDNS

This curl uses asynchronous name resolves. Asynchronous name resolves can be done using either the c-ares or the threaded resolver backends.

brotli

Support for automatic brotli compression over HTTP(S).

CharConv

curl was built with support for character set conversions (like EBCDIC)

Debug

This curl uses a libcurl built with Debug. This enables more error-tracking and memory debugging etc. For curl-developers only.

ECH

ECH support is present.

gsasl

The built-in SASL authentication includes extensions to support SCRAM because libcurl was built with libgsasl.

GSS-API

GSS-API is supported.

HSTS

HSTS support is present.

HTTP2

HTTP/2 support has been built-in.

HTTP3

HTTP/3 support has been built-in.

HTTPS-proxy

This curl is built to support HTTPS proxy.

IDN

This curl supports IDN - international domain names.

IPv6

You can use IPv6 with this.

Kerberos

Kerberos V5 authentication is supported.

Largefile

This curl supports transfers of large files, files larger than 2GB.

libz

Automatic decompression (via gzip, deflate) of compressed files over HTTP is supported.

MultiSSL

This curl supports multiple TLS backends.

NTLM

NTLM authentication is supported.

NTLM_WB

NTLM delegation to winbind helper is supported. This feature was removed from curl in 8.8.0.

PSL

PSL is short for Public Suffix List and means that this curl has been built with knowledge about "public suffixes".

SPNEGO

SPNEGO authentication is supported.

SSL

SSL versions of various protocols are supported, such as HTTPS, FTPS, POP3S and so on.

SSLS-EXPORT

This build supports TLS session export/import, like with the --ssl-sessions.

SSPI

SSPI is supported.

TLS-SRP

SRP (Secure Remote Password) authentication is supported for TLS.

Unicode

Unicode support on Windows.

UnixSockets

Unix sockets support is provided.

zstd

Automatic decompression (via zstd) of compressed files over HTTP is supported.

Example:

```
curl --version
```

See also --help and --manual.

--vlan-priority <priority>

Set VLAN priority as defined in IEEE 802.1Q.

This field is set on Ethernet level, and only works within a local network.

The valid range for <priority> is 0 to 7.

If --vlan-priority is provided several times, the last set value is used.

Example:

```
curl --vlan-priority 4 https://example.com
```

Added in 8.9.0. See also --ip-tos.

-w, --write-out <format>

Make curl display information on stdout after a completed transfer. The format is a string that may contain plain text mixed with any number of variables. The format can be specified as a literal "string", or you can have curl read the format from a file with "@filename" and to tell curl to read the format from stdin you write "@-".

The variables present in the output format are substituted by the value or text that curl thinks fit, as described below. All variables are specified as %{variable_name} and to output a normal % you write them as %%. You can output a newline by using \n, a carriage return with \r and a tab space with \t.

The output is by default written to standard output, but can be changed with %{stderr} and %output{}.

Output HTTP header values from the transfer's most recent server response by using %header{name} where name is the case insensitive name of the header (without the trailing colon). The header contents are exactly as delivered over the network but with leading and trailing whitespace and newlines stripped off (added in 7.84.0).

Select a specific target destination file to write the output to, by using %output{name} (added in curl 8.3.0) where name is the full filename. The output following that instruction is then written to that file. More than one %output{} instruction can be specified in the same write-out argument. If the filename cannot be created, curl leaves the output destination to the one used prior to the %output{} instruction. Use %output{>>name} to append data to an existing file.

This output is done independently of if the file transfer was successful or not.

If the specified action or output specified with this option fails in any way, it does not make curl return a (different) error.

NOTE: On Windows, the %-symbol is a special symbol used to expand environment variables. In batch files, all occurrences of % must be doubled when using this option to properly escape. If this option is used at the command prompt then the % cannot be escaped and unintended expansion is possible.

The variables available are:

certs

Output the certificate chain with details. Supported only by the OpenSSL, GnuTLS, Schannel and Rustls backends. (Added in 7.88.0)

conn_id

The connection identifier last used by the transfer. The connection id is unique number among all connections using the same connection cache. (Added in 8.2.0)

content_type

The Content-Type of the requested document, if there was any.

errormsg

The error message. (Added in 7.75.0)

exitcode

The numerical exit code of the transfer. (Added in 7.75.0)

filename_effective

The ultimate filename that curl writes out to. This is only meaningful if curl is told to write to a file with the --remote-name or --output option. It is most useful in combination with the --remote-header-name option.

ftp_entry_path

The initial path curl ended up in when logging on to the remote FTP server.

header{name}

The value of header "name" from the transfer's most recent server response. Unlike other variables, the variable name "header" is not in braces. For example "%header{date}". Refer to --write-out remarks. (Added in 7.84.0)

Starting with 8.17.0, output the contents of all header fields using a specific name - even for a whole redirect "chain" by appending ":all:[separator]" to the header name. The "[separator]" string (if not blank) is output between the headers if there are more than one. When more than one header is shown, they are output in the chronological order of appearance over the wire. To include a close brace ("}") in the separator, escape it with a backslash: "\}".

header_json

A JSON object with all HTTP response headers from the recent transfer. Values are provided as arrays, since in the case of multiple headers there can be multiple values. (Added in 7.83.0)

The header names provided in lowercase, listed in order of appearance over the wire. Except for duplicated headers. They are grouped on the first occurrence of that header, each value is presented in the JSON array.

http_code

The numerical response code that was found in the last retrieved HTTP(S) or FTP(s) transfer.

http_connect

The numerical code that was found in the last response (from a proxy) to a curl CONNECT request.

http_version

The http version that was effectively used.

json

A JSON object with all available keys except "header_json". (Added in 7.70.0)

local_ip

The IP address of the local end of the most recently done connection - can be either IPv4 or IPv6.

local_port

The local port number of the most recently done connection.

method

The http method used in the most recent HTTP request. (Added in 7.72.0)

num_certs

Number of server certificates received in the TLS handshake. Supported only by the OpenSSL, GnuTLS, Schannel and Rustls backends. (Added in 7.88.0)

num_connects

Number of new connects made in the recent transfer.

num_headers

The number of response headers in the most recent request (restarted at each redirect). Note that the status line IS NOT a header. (Added in 7.73.0)

num_redirects

Number of redirects that were followed in the request.

num_retries

Number of retries actually performed when "--retry" has been used. (Added in 8.9.0)

onerror

The rest of the output is only shown if the transfer returned a non-zero error. (Added in 7.75.0)

output{filename}

From this point on, the --write-out output is written to the filename specified in braces. The filename can be prefixed with ">>" to append to the file. Unlike other variables, the variable name "output" is not in braces. For example "%output{>>stats.txt}". Refer to --write-out remarks. (Added in 8.3.0)

proxy_ssl_verify_result

The result of the HTTPS proxy's SSL peer certificate verification that was requested. 0 means the verification was successful.

proxy_used

Returns 1 if the previous transfer used a proxy, otherwise 0. Useful for example to determine if a "NOPROXY" pattern matched the hostname or not. (Added in 8.7.0)

redirect_url

When an HTTP request was made without --location to follow redirects (or when --max-redirs is met), this variable shows the actual URL a redirect would have gone to.

referer

The Referer: header, if there was any. (Added in 7.76.0)

remote_ip

The remote IP address of the most recently done connection - can be either IPv4 or IPv6.

remote_port

The remote port number of the most recently done connection.

response_code

The numerical response code that was found in the last transfer (formerly known as "http_code").

scheme

The URL scheme (sometimes called protocol) that was effectively used.

size_delivered

The total amount of data that were saved or written to stdout. When --compressed is used, this is likely different than "size_download". Includes the headers in the count if --include is used.

size_download

The total amount of bytes that were downloaded. This is the size of the body/data that was transferred, excluding headers.

size_header

The total amount of bytes of the downloaded headers, as represented in HTTP/1-style header format.

size_request

The total amount of bytes that were sent in the HTTP request.

size_upload

The total amount of bytes that were uploaded. This is the size of the body/data that was transferred, excluding headers.

speed_download

The average download speed that curl measured for the complete download. Bytes per second.

speed_upload

The average upload speed that curl measured for the complete upload. Bytes per second.

ssl_verify_result

The result of the SSL peer certificate verification that was requested. 0 means the verification was successful.

stderr

From this point on, the --write-out output is written to standard error.

stdout

From this point on, the --write-out output is written to standard output. This is the default, but can be used to switch back after switching to stderr.

time{format}

Output the current UTC time using "strftime()" format. See TIME OUTPUT FORMAT below for details. (Added in 8.16.0)

time_appconnect

The time, in seconds, it took from the start until the SSL/SSH/etc connect/handshake to the remote host was completed.

time_connect

The time, in seconds, it took from the start until the TCP connect to the remote host (or proxy) was completed.

time_namelookup

The time, in seconds, it took from the start until the name resolving was completed.

time_posttransfer

The time, in seconds, it took from the start until the last byte is sent by libcurl. (Added in 8.10.0)

time_pretransfer

The time, in seconds, it took from the start until immediately before the file transfer was about to begin. This includes all pre-transfer commands and negotiations that are specific to the particular protocol(s) involved.

time_queue

The time, in seconds, the transfer was queued during its run. This adds the queue time for each redirect step that may have happened. Transfers may be queued for significant amounts of time when connection or parallel limits are in place. (Added in 8.12.0)

time_redirect

The time, in seconds, it took for all redirection steps including name lookup, connect, pretransfer and transfer before the final transaction was started. "time_redirect" shows the complete execution time for multiple redirections.

time_starttransfer

The time, in seconds, it took from the start until the first byte was received. This includes time_pretransfer and also the time the server needed to calculate the result.

time_total

The total time, in seconds, that the full operation lasted.

tls_earlydata

The amount of bytes that were sent as TLSv1.3 early data. This is 0 if this TLS feature was not used and negative if the data sent had been rejected by the server. The use of early data is enabled via the command line option "--tls-earlydata". (Added in 8.13.0)

url

The URL that was fetched. (Added in 7.75.0)

url.scheme

The scheme part of the URL that was fetched. (Added in 8.1.0)

url.user

The user part of the URL that was fetched. (Added in 8.1.0)

url.password

The password part of the URL that was fetched. (Added in 8.1.0)

url.options

The options part of the URL that was fetched. (Added in 8.1.0)

url.host

The host part of the URL that was fetched. (Added in 8.1.0)

url.port

The port number of the URL that was fetched. If no port number was specified and the URL scheme is known, that scheme's default port number is shown. (Added in 8.1.0)

url.path

The path part of the URL that was fetched. (Added in 8.1.0)

url.query

The query part of the URL that was fetched. (Added in 8.1.0)

url.fragment

The fragment part of the URL that was fetched. (Added in 8.1.0)

url.zoneid

The zone id part of the URL that was fetched. (Added in 8.1.0)

urle.scheme

The scheme part of the effective (last) URL that was fetched. (Added in 8.1.0)

urle.user

The user part of the effective (last) URL that was fetched. (Added in 8.1.0)

urle.password

The password part of the effective (last) URL that was fetched. (Added in 8.1.0)

urle.options

The options part of the effective (last) URL that was fetched. (Added in 8.1.0)

urle.host

The host part of the effective (last) URL that was fetched. (Added in 8.1.0)

urle.port

The port number of the effective (last) URL that was fetched. If no port number was specified, but the URL scheme is known, that scheme's default port number is shown. (Added in 8.1.0)

urle.path

The path part of the effective (last) URL that was fetched. (Added in 8.1.0)

urle.query

The query part of the effective (last) URL that was fetched. (Added in 8.1.0)

urle.fragment

The fragment part of the effective (last) URL that was fetched. (Added in 8.1.0)

urle.zoneid

The zone id part of the effective (last) URL that was fetched. (Added in 8.1.0)

urlnum

The URL index number of this transfer, 0-indexed. Unglobbed URLs share the same index number as the origin globbed URL. (Added in 7.75.0)

url_effective

The URL that was fetched last. This is most meaningful if you have told curl to follow location: headers.

xfer_id

The numerical identifier of the last transfer done. -1 if no transfer has been started yet for the handle. The transfer id is unique among all transfers performed using the same connection cache. (Added in 8.2.0)

TIME OUTPUT FORMAT

To show time with "%time{}" the characters within "{}" create a special format string that may contain special character sequences called conversion specifications. Each conversion specification starts with "%" and is followed by a character that instructs curl to output a particular time detail. All other characters used are displayed as-is.

The following conversion specification are available:

%a

The abbreviated name of the day of the week according to the current locale.

%A

The full name of the day of the week according to the current locale.

%b

The abbreviated month name according to the current locale.

%B

The full month name according to the current locale.

%c

The preferred date and time representation for the current locale. (In the POSIX locale this is equivalent to "%a %b %e %H:%M:%S %Y".)

%C

The century number (year/100) as a 2-digit integer.

%d

The day of the month as a decimal number (range 01 to 31).

%D

Equivalent to "%m/%d/%y". In international contexts, this format is ambiguous and should be avoided.)

%e

Like "%d", the day of the month as a decimal number, but a leading zero is replaced by a space.

%f

The number of microseconds elapsed of the current second. (This a curl special code and not a standard one.)

%F

Equivalent to "%Y-%m-%d" (the ISO 8601 date format).

%G

The ISO 8601 week-based year with century as a decimal number. The 4-digit year corresponding to the ISO week number (see "%V"). This has the same format and value as "%Y", except that if the ISO week number belongs to the previous or next year, that year is used instead.

%g

Like "%G", but without century, that is, with a 2-digit year (00-99).

%h

Equivalent to "%b".

%H

The hour as a decimal number using a 24-hour clock (range 00 to 23).

%I

The hour as a decimal number using a 12-hour clock (range 01 to 12).

%j

The day of the year as a decimal number (range 001 to 366).

%k

The hour (24-hour clock) as a decimal number (range 0 to 23); single digits are preceded by a blank.

%l

The hour (12-hour clock) as a decimal number (range 1 to 12); single digits are preceded by a blank.

%m

The month as a decimal number (range 01 to 12).

%M

The minute as a decimal number (range 00 to 59).

%p

Either "AM" or "PM" according to the given time value, or the corresponding strings for the current locale. Noon is treated as "PM" and midnight as "AM".

%P

Like "%p" but in lowercase: "am" or "pm" or a corresponding string for the current locale.

%r

The time in am or pm notation.

%R

The time in 24-hour notation ("%H:%M"). For a version including the seconds, see "%T" below.

%s

The number of seconds since the Epoch, 1970-01-01 00:00:00 +0000 (UTC).

%S

The second as a decimal number (range 00 to 60). (The range is up to 60 to allow for occasional leap seconds.) See "%f" for microseconds.

%T

The time in 24-hour notation ("%H:%M:%S").

%u

The day of the week as a decimal, range 1 to 7, Monday being 1.

%U

The week number of the current year as a decimal number, range 00 to 53, starting with the first Sunday as the first day of week 01. See also "%V" and "%W".

%V

The ISO 8601 week number (see NOTES) of the current year as a decimal number, range 01 to 53, where week 1 is the first week that has at least 4 days in the new year. See also "%U" and "%W".

%w

The day of the week as a decimal, range 0 to 6, Sunday being 0. See also "%u".

%W

The week number of the current year as a decimal number, range 00 to 53, starting with the first Monday as the first day of week 01.

%x

The preferred date representation for the current locale without the time.

%X

The preferred time representation for the current locale without the date.

%y

The year as a decimal number without a century (range 00 to 99).

%Y

The year as a decimal number including the century.

%z

The "+hhmm" or "-hhmm" numeric timezone (that is, the hour and minute offset from UTC). As time is always UTC, this outputs "+0000".

%Z

The timezone name. For some reason "GMT".

%%

A literal "%" character.

If --write-out is provided several times, the last set value is used.

Example:

```
curl -w '%{response_code}\n' https://example.com
```

See also --verbose and --head.

--xattr

Store metadata in the extended file attributes.

When saving output to a file, tell curl to store file metadata in extended file attributes. Currently, "curl" is stored in the "creator" attribute, the URL is stored in the "xdg.origin.url" attribute and, for HTTP, the content type is stored in the "mime_type" attribute. If the file system does not support extended attributes, a warning is issued.

Providing --xattr multiple times has no extra effect. Disable it again with --no-xattr.

Example:

```
curl --xattr -o storage https://example.com
```

See also --remote-time, --write-out and --verbose.


## Files

~/.curlrc

Default config file, see --config for details.


## Environment

The environment variables can be specified in lower case or upper case. The lower case version has precedence. "http_proxy" is an exception as it is only available in lower case. (Note that some systems, like Windows, do not differentiate between environment variables using different case.)

Using an environment variable to set the proxy has the same effect as using the --proxy option.

http_proxy [protocol://]<host>[:port]

Sets the proxy server to use for HTTP.

HTTPS_PROXY [protocol://]<host>[:port]

Sets the proxy server to use for HTTPS.

[url-protocol]_PROXY [protocol://]<host>[:port]

Sets the proxy server to use for [url-protocol], where the protocol is a protocol that curl supports and as specified in a URL. FTP, FTPS, POP3, IMAP, SMTP, LDAP, etc.

ALL_PROXY [protocol://]<host>[:port]

Sets the proxy server to use if no protocol-specific proxy is set.

NO_PROXY <comma-separated list of hosts/domains>

list of hostnames that should not go through any proxy. If set to an asterisk '*' only, it matches all hosts. Each name in this list is matched as either a domain name which contains the hostname, or the hostname itself.

This environment variable disables use of the proxy even when specified with the --proxy option. That is

```
NO_PROXY=direct.example.com curl -x http://proxy.example.com
https://direct.example.com
```

accesses the target URL directly, and

```
NO_PROXY=direct.example.com curl -x http://proxy.example.com
https://somewhere.example.com
```

accesses the target URL through the proxy.

The list of hostnames can also include numerical IP addresses, and IPv6 versions should then be given without enclosing brackets.

IP addresses can be specified using CIDR notation: an appended slash and number specifies the number of "network bits" out of the address to use in the comparison (added in 7.86.0). For example "192.168.0.0/16" would match all addresses starting with "192.168".

APPDATA <directory>

On Windows, this variable is used when trying to find the home directory. If the primary home variables are all unset.

COLUMNS <terminal width>

If set, the specified number of characters is used as the terminal width when the alternative progress-bar is shown. If not set, curl tries to figure it out using other ways.

CURL_CA_BUNDLE <file>

If set, it is used as the --cacert value. This environment variable is ignored if Schannel is used as the TLS backend.

CURL_HOME <directory>

If set, is the first variable curl checks when trying to find its home directory. If not set, it continues to check XDG_CONFIG_HOME

CURL_SSL_BACKEND <TLS backend>

If curl was built with support for "MultiSSL", meaning that it has built-in support for more than one TLS backend, this environment variable can be set to the case insensitive name of the particular backend to use when curl is invoked. Setting a name that is not a built-in alternative makes curl stay with the default.

SSL backend names (case-insensitive): gnutls, mbedtls, openssl, rustls, schannel, wolfssl

HOME <directory>

If set, this is used to find the home directory when that is needed. Like when looking for the default .curlrc. CURL_HOME and XDG_CONFIG_HOME have preference.

NETRC <path>

If set, this is used to find the ".netrc" file. It overrides all other netrc file location mechanisms and should be set to the full file path. (Added in curl 8.16.0)

QLOGDIR <directory>

If curl was built with HTTP/3 support, setting this environment variable to a local directory makes curl produce qlogs in that directory, using file names named after the destination connection id (in hex). Do note that these files can become rather large. Works with the ngtcp2 and quiche QUIC backends.

SHELL

Used on VMS when trying to detect if using a DCL or a Unix shell.

SSL_CERT_DIR <directory>

If set, it is used as the --capath value. This environment variable is ignored if Schannel is used as the TLS backend.

SSL_CERT_FILE <path>

If set, it is used as the --cacert value. This environment variable is ignored if Schannel is used as the TLS backend.

SSLKEYLOGFILE <path>

If you set this environment variable to a filename, curl stores TLS secrets from its connections in that file when invoked to enable you to analyze the TLS traffic in real time using network analyzing tools such as Wireshark. This works with the following TLS backends: OpenSSL, LibreSSL (TLS 1.2 max), BoringSSL, GnuTLS, wolfSSL and Rustls.

USERPROFILE <directory>

On Windows, this variable is used when trying to find the home directory. If the other, primary, variables are all unset. If set, curl uses the path "$USERPROFILE\Application Data".

XDG_CONFIG_HOME <directory>

If CURL_HOME is not set, this variable is checked when looking for a default .curlrc file.


## Proxy protocol prefixes

The proxy string may be specified with a "protocol://" prefix to specify alternative proxy protocols.

If no protocol is specified in the proxy string or if the string does not match a supported one, the proxy is treated as an HTTP proxy.

The supported proxy protocol prefixes are as follows:

http://

Makes it use it as an HTTP proxy. The default if no scheme prefix is used.

https://

Makes it treated as an HTTPS proxy.

socks4://

Makes it the equivalent of --socks4

socks4a://

Makes it the equivalent of --socks4a

socks5://

Makes it the equivalent of --socks5

socks5h://

Makes it the equivalent of --socks5-hostname


## Exit codes

There are a bunch of different error codes and their corresponding error messages that may appear under error conditions. At the time of this writing, the exit codes are:

0

Success. The operation completed successfully according to the instructions.

1

Unsupported protocol. This build of curl has no support for this protocol.

2

Failed to initialize.

3

URL malformed. The syntax was not correct.

4

A feature or option that was needed to perform the desired request was not enabled or was explicitly disabled at build-time. To make curl able to do this, you probably need another build of libcurl.

5

Could not resolve proxy. The given proxy host could not be resolved.

6

Could not resolve host. The given remote host could not be resolved.

7

Failed to connect to host.

8

Weird server reply. The server sent data curl could not parse.

9

FTP access denied. The server denied login or denied access to the particular resource or directory you wanted to reach. Most often you tried to change to a directory that does not exist on the server.

10

FTP accept failed. While waiting for the server to connect back when an active FTP session is used, an error code was sent over the control connection or similar.

11

FTP weird PASS reply. curl could not parse the reply sent to the PASS request.

12

During an active FTP session while waiting for the server to connect back to curl, the timeout expired.

13

FTP weird PASV reply, curl could not parse the reply sent to the PASV request.

14

FTP weird 227 format. curl could not parse the 227-line the server sent.

15

FTP cannot use host. Could not resolve the host IP we got in the 227-line.

16

HTTP/2 error. A problem was detected in the HTTP2 framing layer. This is somewhat generic and can be one out of several problems, see the error message for details.

17

FTP could not set binary. Could not change transfer method to binary.

18

Partial file. Only a part of the file was transferred.

19

FTP could not download/access the given file, the RETR (or similar) command failed.

21

FTP quote error. A quote command returned error from the server.

22

HTTP page not retrieved. The requested URL was not found or returned another error with the HTTP error code being 400 or above. This return code only appears if --fail is used.

23

Write error. curl could not write data to a local file system or similar.

25

Failed starting the upload. For FTP, the server typically denied the STOR command.

26

Read error. Various reading problems.

27

Out of memory. A memory allocation request failed.

28

Operation timeout. The specified time-out period was reached according to the conditions.

30

FTP PORT failed. The PORT command failed. Not all FTP servers support the PORT command, try doing a transfer using PASV instead.

31

FTP could not use REST. The REST command failed. This command is used for resumed FTP transfers.

33

HTTP range error. The range "command" did not work.

34

HTTP post error. Internal post-request generation error.

35

SSL connect error. The SSL handshaking failed.

36

Bad download resume. Could not continue an earlier aborted download.

37

FILE could not read file. Failed to open the file. Permissions?

38

LDAP cannot bind. LDAP bind operation failed.

39

LDAP search failed.

41

Function not found. A required LDAP function was not found.

42

Aborted by callback. An application told curl to abort the operation.

43

Internal error. A function was called with a bad parameter.

45

Interface error. A specified outgoing interface could not be used.

47

Too many redirects. When following redirects, curl hit the maximum amount.

48

Unknown option specified to libcurl. This indicates that you passed a weird option to curl that was passed on to libcurl and rejected. Read up in the manual.

49

Malformed telnet option.

52

The server did not reply anything, which here is considered an error.

53

SSL crypto engine not found.

54

Cannot set SSL crypto engine as default.

55

Failed sending network data.

56

Failure in receiving network data.

58

Problem with the local certificate.

59

Could not use specified SSL cipher.

60

Peer certificate cannot be authenticated with known CA certificates.

61

Unrecognized transfer encoding.

63

Maximum file size exceeded.

64

Requested FTP SSL level failed.

65

Sending the data requires a rewind that failed.

66

Failed to initialize SSL Engine.

67

The username, password, or similar was not accepted and curl failed to log in.

68

File not found on TFTP server.

69

Permission problem on TFTP server.

70

Out of disk space on TFTP server.

71

Illegal TFTP operation.

72

Unknown TFTP transfer ID.

73

File already exists (TFTP).

74

No such user (TFTP).

77

Problem reading the SSL CA cert (path? access rights?).

78

The resource referenced in the URL does not exist.

79

An unspecified error occurred during the SSH session.

80

Failed to shut down the SSL connection.

82

Could not load CRL file, missing or wrong format.

83

Issuer check failed.

84

The FTP PRET command failed.

85

Mismatch of RTSP CSeq numbers.

86

Mismatch of RTSP Session Identifiers.

87

Unable to parse FTP file list.

88

FTP chunk callback reported error.

89

No connection available, the session is queued.

90

SSL public key does not match pinned public key.

91

Invalid SSL certificate status.

92

Stream error in HTTP/2 framing layer.

93

An API function was called from inside a callback.

94

An authentication function returned an error.

95

A problem was detected in the HTTP/3 layer. This is somewhat generic and can be one out of several problems, see the error message for details.

96

QUIC connection error. This error may be caused by an SSL library error. QUIC is the protocol used for HTTP/3 transfers.

97

Proxy handshake error.

98

A client-side certificate is required to complete the TLS handshake.

99

Poll or select returned fatal error.

100

A value or data field grew larger than allowed.

XX

More error codes might appear here in future releases. The existing ones are meant to never change.


## Bugs

If you experience any problems with curl, submit an issue in the project's bug tracker on GitHub: https://github.com/curl/curl/issues


## Authors

Daniel Stenberg is the main author, but the whole list of contributors is found in the separate THANKS file.


## Www

https://curl.se/
