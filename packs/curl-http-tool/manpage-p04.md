---
title: "curl (part 4/5)"
source: https://curl.se/docs/manpage.html
domain: curl-http-tool
license: CC-BY-SA-4.0
tags: curl http, http client, data transfer, command-line http
fetched: 2026-07-02
part: 4/5
---

# curl

Enable automatic use of bold font styles when writing HTTP headers to the terminal. Use --no-styled-output to switch them off.

Styled output requires a terminal that supports bold fonts. This feature is not present on curl for Windows due to lack of this capability.

This option is global and does not need to be specified for each use of --next.

Providing --styled-output multiple times has no extra effect. Disable it again with --no-styled-output.

Example:

```
curl --styled-output -I https://example.com
```

See also --head and --verbose.

--suppress-connect-headers

When --proxytunnel is used and a CONNECT request is made, do not output proxy CONNECT response headers. This option is meant to be used with --dump-header or --show-headers which are used to show protocol headers in the output. It has no effect on debug options such as --verbose or --trace, or any statistics.

Providing --suppress-connect-headers multiple times has no extra effect. Disable it again with --no-suppress-connect-headers.

Example:

```
curl --suppress-connect-headers --show-headers -x proxy https://example.com
```

See also --dump-header, --show-headers and --proxytunnel.

--tcp-fastopen

Enable use of TCP Fast Open (RFC 7413). TCP Fast Open is a TCP extension that allows data to be sent earlier over the connection (before the final handshake ACK) if the client and server have been connected previously.

Providing --tcp-fastopen multiple times has no extra effect. Disable it again with --no-tcp-fastopen.

Example:

```
curl --tcp-fastopen https://example.com
```

See also --false-start.

--tcp-nodelay

Turn on the TCP_NODELAY option.

This option disables the Nagle algorithm on TCP connections. The purpose of this algorithm is to minimize the number of small packets on the network (where "small packets" means TCP segments less than the Maximum Segment Size for the network).

Maximizing the amount of data sent per TCP segment is good because it amortizes the overhead of the send. In some cases small segments may need to be sent without delay. This is less efficient than sending larger amounts of data at a time, and can contribute to congestion on the network if overdone.

curl sets this option by default and you need to explicitly switch it off if you do not want it on.

Providing --tcp-nodelay multiple times has no extra effect. Disable it again with --no-tcp-nodelay.

Example:

```
curl --tcp-nodelay https://example.com
```

See also --no-buffer.

-t, --telnet-option <opt=val>

(TELNET) Pass options to the telnet protocol. Supported options are:

TTYPE=<term>

Sets the terminal type.

XDISPLOC=<X display>

Sets the X display location.

NEW_ENV=<var,val>

Sets an environment variable.

--telnet-option can be used several times in a command line.

Example:

```
curl -t TTYPE=vt100 telnet://example.com/
```

See also --config.

--tftp-blksize <value>

(TFTP) Set the TFTP BLKSIZE option (must be 512 or larger). This is the block size that curl tries to use when transferring data to or from a TFTP server. By default 512 bytes are used.

If --tftp-blksize is provided several times, the last set value is used.

Example:

```
curl --tftp-blksize 1024 tftp://example.com/file
```

See also --tftp-no-options.

--tftp-no-options

(TFTP) Do not send TFTP options requests. This improves interop with some legacy servers that do not acknowledge or properly implement TFTP options. When this option is used --tftp-blksize is ignored.

Providing --tftp-no-options multiple times has no extra effect. Disable it again with --no-tftp-no-options.

Example:

```
curl --tftp-no-options tftp://192.168.0.1/
```

See also --tftp-blksize.

-z, --time-cond <time>

(HTTP FTP) Request a file that has been modified later than the given time and date, or one that has been modified before that time. The date expression can be all sorts of date strings or if it does not match any internal ones, it is treated as a filename and curl tries to get the modification date (mtime) from that file instead. See the curl_getdate man page for date expression details.

Start the date expression with a dash (-) to make it request for a document that is older than the given date/time, default is a document that is newer than the specified date/time.

If provided a non-existing file, curl outputs a warning about that fact and proceeds to do the transfer without a time condition.

If --time-cond is provided several times, the last set value is used.

Examples:

```
curl -z "Wed 01 Sep 2021 12:18:00" https://example.com
curl -z "-Wed 01 Sep 2021 12:18:00" https://example.com
curl -z file https://example.com
```

See also --etag-compare and --remote-time.

--tls-earlydata

(TLS) Enable the use of TLSv1.3 early data, also known as '0RTT' where possible. This has security implications for the requests sent that way.

This option can be used when curl is built to use GnuTLS, OpenSSL, quictls and wolfSSL as a TLS provider (but not AWS-LC, BoringSSL, or Rustls).

If a server supports this TLSv1.3 feature, and to what extent, is announced as part of the TLS "session" sent back to curl. Until curl has seen such a session in a previous request, early data cannot be used.

When a new connection is initiated with a known TLSv1.3 session, and that session announced early data support, the first request on this connection is sent before the TLS handshake is complete. While the early data is also encrypted, it is not protected against replays. An attacker can send your early data to the server again and the server would accept it.

If your request contacts a public server and only retrieves a file, there may be no harm in that. If the first request orders a refrigerator for you, it is probably not a good idea to use early data for it. curl cannot deduce what the security implications of your requests actually are and make this decision for you.

The amount of early data sent can be inspected by using the "--write-out" variable "tls_earlydata".

WARNING: this option has security implications. See above for more details.

Providing --tls-earlydata multiple times has no extra effect. Disable it again with --no-tls-earlydata.

Example:

```
curl --tls-earlydata https://example.com
```

Added in 8.11.0. See also --tlsv1.3, --tls-max and --ssl-sessions.

--tls-max <VERSION>

(TLS) Set the maximum allowed TLS version. The minimum acceptable version is set by tlsv1.0, tlsv1.1, tlsv1.2 or tlsv1.3.

If the connection is done without TLS, this option has no effect. This includes QUIC-using (HTTP/3) transfers.

default

Use up to the recommended TLS version.

1.0

Use up to TLSv1.0.

1.1

Use up to TLSv1.1.

1.2

Use up to TLSv1.2.

1.3

Use up to TLSv1.3.

If --tls-max is provided several times, the last set value is used.

Examples:

```
curl --tls-max 1.2 https://example.com
curl --tls-max 1.3 --tlsv1.2 https://example.com
```

For --tls-max to work, it requires that the underlying libcurl is built to support TLS. See also --tlsv1.0, --tlsv1.1, --tlsv1.2 and --tlsv1.3.

--tls13-ciphers <list>

(TLS) Set which cipher suites to use in the connection if it negotiates TLS 1.3. The list of ciphers suites must specify valid ciphers. Read up on TLS 1.3 cipher suite details on this URL:

https://curl.se/docs/ssl-ciphers.html

This option is used when curl is built to use OpenSSL 1.1.1 or later, wolfSSL, or mbedTLS 3.6.0 or later.

Before curl 8.10.0 with mbedTLS or wolfSSL, TLS 1.3 cipher suites were set by using the --ciphers option.

If --tls13-ciphers is provided several times, the last set value is used.

Example:

```
curl --tls13-ciphers TLS_AES_128_GCM_SHA256 https://example.com
```

See also --ciphers, --proxy-tls13-ciphers and --curves.

--tlsauthtype <type>

(TLS) Set TLS authentication type. Currently, the only supported option is "SRP", for TLS-SRP (RFC 5054). If --tlsuser and --tlspassword are specified but --tlsauthtype is not, then this option defaults to "SRP". This option works only if the underlying libcurl is built with TLS-SRP support, which requires OpenSSL or GnuTLS with TLS-SRP support.

If --tlsauthtype is provided several times, the last set value is used.

Example:

```
curl --tlsauthtype SRP https://example.com
```

See also --tlsuser.

--tlspassword <string>

(TLS) Set password to use with the TLS authentication method specified with --tlsauthtype. Requires that --tlsuser is set.

This option does not work with TLS 1.3.

If --tlspassword is provided several times, the last set value is used.

Example:

```
curl --tlspassword pwd --tlsuser user https://example.com
```

See also --tlsuser.

--tlsuser <name>

(TLS) Set username for use with the TLS authentication method specified with --tlsauthtype. Requires that --tlspassword also is set.

This option does not work with TLS 1.3.

If --tlsuser is provided several times, the last set value is used.

Example:

```
curl --tlspassword pwd --tlsuser user https://example.com
```

See also --tlspassword.

-1, --tlsv1

(TLS) Use at least TLS version 1.x when negotiating with a remote TLS server. That means TLS version 1.0 or higher

Providing --tlsv1 multiple times has no extra effect.

Example:

```
curl --tlsv1 https://example.com
```

For --tlsv1 to work, it requires that the underlying libcurl is built to support TLS. This option is mutually exclusive with --tlsv1.1, --tlsv1.2 and --tlsv1.3. See also --http1.1 and --http2.

--tlsv1.0

(TLS) Force curl to use TLS version 1.0 or later when connecting to a remote TLS server.

In old versions of curl this option was documented to allow _only_ TLS 1.0. That behavior was inconsistent depending on the TLS library. Use --tls-max if you want to set a maximum TLS version.

Providing --tlsv1.0 multiple times has no extra effect.

Example:

```
curl --tlsv1.0 https://example.com
```

See also --tlsv1.3.

--tlsv1.1

(TLS) Force curl to use TLS version 1.1 or later when connecting to a remote TLS server.

In old versions of curl this option was documented to allow _only_ TLS 1.1. That behavior was inconsistent depending on the TLS library. Use --tls-max if you want to set a maximum TLS version.

Providing --tlsv1.1 multiple times has no extra effect.

Example:

```
curl --tlsv1.1 https://example.com
```

See also --tlsv1.3 and --tls-max.

--tlsv1.2

(TLS) Force curl to use TLS version 1.2 or later when connecting to a remote TLS server.

In old versions of curl this option was documented to allow _only_ TLS 1.2. That behavior was inconsistent depending on the TLS library. Use --tls-max if you want to set a maximum TLS version.

Providing --tlsv1.2 multiple times has no extra effect.

Example:

```
curl --tlsv1.2 https://example.com
```

See also --tlsv1.3 and --tls-max.

--tlsv1.3

(TLS) Force curl to use TLS version 1.3 or later when connecting to a remote TLS server.

If the connection is done without TLS, this option has no effect. This includes QUIC-using (HTTP/3) transfers.

Note that TLS 1.3 is not supported by all TLS backends.

Providing --tlsv1.3 multiple times has no extra effect.

Example:

```
curl --tlsv1.3 https://example.com
```

See also --tlsv1.2 and --tls-max.

--tr-encoding

(HTTP) Request a compressed Transfer-Encoding response using one of the algorithms curl supports, and uncompress the data while receiving it.

This method was once intended to be the way to do automatic data compression for HTTP but for all practical purposes using Content-Encoding as done with --compressed has superseded transfer encoding. The --tr-encoding option is therefore often not be one you want.

Providing --tr-encoding multiple times has no extra effect. Disable it again with --no-tr-encoding.

Example:

```
curl --tr-encoding https://example.com
```

See also --compressed.

--trace <file>

Save a full trace dump of all incoming and outgoing data, including descriptive information, in the given output file. Use "-" as filename to have the output sent to stdout. Use "%" as filename to have the output sent to stderr.

Note that verbose output of curl activities and network traffic might contain sensitive data, including usernames, credentials or secret data content. Be aware and be careful when sharing trace logs with others.

This option is global and does not need to be specified for each use of --next.

If --trace is provided several times, the last set value is used.

Example:

```
curl --trace log.txt https://example.com
```

This option is mutually exclusive with --verbose and --trace-ascii. See also --trace-ascii, --trace-config, --trace-ids and --trace-time.

--trace-ascii <file>

Save a full trace dump of all incoming and outgoing data, including descriptive information, in the given output file. Use "-" as filename to have the output sent to stdout. Use "%" as filename to send the output to stderr.

This is similar to --trace, but leaves out the hex part and only shows the ASCII part of the dump. It makes smaller output that might be easier to read for untrained humans.

Note that verbose output of curl activities and network traffic might contain sensitive data, including usernames, credentials or secret data content. Be aware and be careful when sharing trace logs with others.

This option is global and does not need to be specified for each use of --next.

If --trace-ascii is provided several times, the last set value is used.

Example:

```
curl --trace-ascii log.txt https://example.com
```

This option is mutually exclusive with --trace and --verbose. See also --verbose and --trace.

--trace-config <string>

Set configuration for trace output. A comma-separated list of components where detailed output can be made available from. Names are case-insensitive. Specify 'all' to enable all trace components.

In addition to trace component names, specify "ids" and "time" to avoid extra --trace-ids or --trace-time parameters.

See the curl_global_trace man page for more details.

This option is global and does not need to be specified for each use of --next.

--trace-config can be used several times in a command line.

Example:

```
curl --trace-config ids,http/2 https://example.com
```

Added in 8.3.0. See also --verbose and --trace.

--trace-ids

Prepend the transfer and connection identifiers to each trace or verbose line that curl displays.

The identifiers are unique numbers assigned to each connection and transfer to allow a user to better understand which transfer and connection each verbose output line refers to.

This option is global and does not need to be specified for each use of --next.

Providing --trace-ids multiple times has no extra effect. Disable it again with --no-trace-ids.

Example:

```
curl --trace-ids --trace-ascii output https://example.com
```

Added in 8.2.0. See also --trace and --verbose.

--trace-time

Prepend a time stamp to each trace or verbose line that curl displays.

This option is global and does not need to be specified for each use of --next.

Providing --trace-time multiple times has no extra effect. Disable it again with --no-trace-time.

Example:

```
curl --trace-time --trace-ascii output https://example.com
```

See also --trace and --verbose.

--unix-socket <path>

(HTTP) Connect to the server through this Unix domain socket, instead of using the network.

To connect to a proxy over Unix domain socket, see --proxy.

If --unix-socket is provided several times, the last set value is used.

Example:

```
curl --unix-socket socket-path https://example.com
```

See also --abstract-unix-socket.

-T, --upload-file <file>

Upload the specified local file to the remote URL.

If there is no file part in the specified URL, curl appends the local file name to the end of the URL before the operation starts. You must use a trailing slash ("/") on the last directory to prove to curl that there is no filename or curl thinks that your last directory name is the remote filename to use.

When putting the local filename at the end of the URL, curl ignores what is on the left side of any slash ("/") or backslash ("\\") used in the filename and only appends what is on the right side of the rightmost such character.

Use the filename "-" (a single dash) to use stdin instead of a given file. Alternately, the filename "." (a single period) may be specified instead of "-" to use stdin in non-blocking mode to allow reading server output while stdin is being uploaded.

If this option is used with an HTTP(S) URL, the PUT method is used.

You can specify one --upload-file for each URL on the command line. Each --upload-file + URL pair specifies what to upload and to where. curl also supports globbing of the --upload-file argument, meaning that you can upload multiple files to a single URL by using the same URL globbing style supported in the URL. Example:

```
curl --upload-file 'file{1,2,3}' ftp://ftp.example/
```

Since curl 8.21.0, you can use parts of the upload filename when it uses globbing by setting a glob name and referencing that in the same way you reference named URL globs. For example, if you upload three files to a single fixed HTTP URL and want to save the corresponding responses in separate files:

```
curl -T 'file{<num>1,2,3}' \
  https://upload.example/ -o 'response-#<num>'
```

When uploading to an SMTP server (aka "sending email"): the uploaded data is assumed to be RFC 5322 formatted. It has to feature the necessary set of headers and mail body formatted correctly by the user as curl does not transcode nor encode it further in any way.

--upload-file is associated with a single URL. Use it once per URL when you use several URLs in a command line.

Examples:

```
curl -T file https://example.com
curl -T "img[1-1000].png" ftp://ftp.example.com/
curl --upload-file "{file1,file2}" https://example.com
curl -T file -T file2 https://example.com https://example.com
```

See also --get, --head, --request and --data.

--upload-flags <flags>

(IMAP) Specify additional behavior to apply to uploaded files. Flags are specified as either a single flag value or a comma-separated list of flag values. These values are case-sensitive and may be negated by prepending them with a '-' character. Currently the following flag values are accepted: answered, deleted, draft, flagged, and seen. The currently accepted flag values are used to set flags on IMAP uploads.

If --upload-flags is provided several times, the last set value is used.

Example:

```
curl --upload-flags Flagged,!Seen --upload-file local/dir/file https://example.com
```

Added in 8.13.0. See also --upload-file.

--url <url/file>

Specify a URL to fetch or send data to.

If the given URL is missing a scheme (such as "http://" or "ftp://" etc) curl guesses which scheme to use based on the hostname. If the outermost subdomain name matches DICT, FTP, IMAP, LDAP, POP3 or SMTP case insensitively, then that protocol is used, otherwise it assumes HTTP. Scheme guessing can be avoided by providing a full URL including the scheme, or disabled by setting a default protocol, see --proto-default for details.

To control where the contents of a retrieved URL is written instead of the default stdout, use the --output or the --remote-name options. When retrieving multiple URLs in a single invoke, each provided URL needs its own dedicated destination option unless --remote-name-all is used.

On Windows, "file://" accesses can be converted to network accesses by the operating system.

Starting in curl 8.13.0, curl can be told to download URLs provided in a text file, one URL per line. It is done with "--url @filename": so instead of a URL, you specify a filename prefixed with the "@" symbol. It can be told to load the list of URLs from stdin by providing an argument like "@-".

When downloading URLs given in a file, it implies using --remote-name for each provided URL. The URLs are full, there is no globbing applied or done on these. Features such as --skip-existing work fine in combination with this.

Lines in the URL file that start with "#" are treated as comments and are skipped.

--url can be used several times in a command line.

Examples:

```
curl --url https://example.com
curl --url @file
```

See also --next, --config, --path-as-is and --disallow-username-in-url.

--url-query <data>

Add a piece of data, usually a name + value pair, to the end of the URL query part. The syntax is identical to that used for --data-urlencode with one extension:

If the argument starts with a '+' (plus), the rest of the string is provided as-is unencoded.

The query part of a URL is the one following the question mark on the right end.

--url-query can be used several times in a command line.

Examples:

```
curl --url-query name=val https://example.com
curl --url-query =encodethis http://example.net/foo
curl --url-query name@file https://example.com
curl --url-query @fileonly https://example.com
curl --url-query "+name=%20foo" https://example.com
```

Added in 7.87.0. See also --data-urlencode and --get.

-B, --use-ascii

(FTP LDAP TFTP) Enable ASCII transfer mode. For FTP, this can also be enforced by using a URL that ends with ";type=A". For TFTP, this can also be enforced by using a URL that ends with ";mode=netascii". This option causes data sent to stdout to be in text mode for Win32 systems.

Providing --use-ascii multiple times has no extra effect. Disable it again with --no-use-ascii.

Example:

```
curl -B ftp://example.com/README
```

See also --crlf and --data-ascii.

-u, --user <user:password>

Specify the username and password to use for server authentication. Overrides --netrc and --netrc-optional.

If you specify only the username, curl prompts for a password.

The username and passwords are split up on the first colon, which makes it impossible to use a colon in the username with this option. The password can, still.

On systems where it works, curl hides the given option argument from process listings. This is not enough to protect credentials from possibly getting seen by other users on the same system as they still are visible for a moment before being cleared. Such sensitive data should be retrieved from a file instead or similar and never used in clear text in a command line.

When using Kerberos V5 with a Windows based server you should include the Windows domain name in the username, in order for the server to successfully obtain a Kerberos Ticket. If you do not, then the initial authentication handshake may fail.

When using NTLM, the username can be specified without the domain, if there is a single domain and forest in your setup for example.

To specify the domain name use either Down-Level Logon Name or UPN (User Principal Name) formats. For example, EXAMPLE\user and user@example.com respectively.

If you use a Windows SSPI-enabled curl binary and perform Kerberos V5, Negotiate, NTLM or Digest authentication then you can tell curl to select the username and password from your environment by specifying a single colon with this option: "-u :".

If --user is provided several times, the last set value is used.

Example:

```
curl -u user:secret https://example.com
```

See also --netrc and --config.

-A, --user-agent <name>

(HTTP) Specify the User-Agent string to send to the HTTP server. To encode blanks in the string, surround the string with single or double quote marks. This header can also be set with the --header or the --proxy-header options.

If you give an empty argument to --user-agent (""), it removes the header completely from the request. If you prefer a blank header, you can set it to a single space (" ").

By default, curl uses curl/VERSION, such as User-Agent: curl/8.21.1.

If --user-agent is provided several times, the last set value is used.

Example:

```
curl -A "Agent 007" https://example.com
```

See also --header and --proxy-header.

--variable <[%]name=text/@file>

Set a variable with "name=content" or "name@file" (where "file" can be stdin if set to a single dash ("-")). The name is a case sensitive identifier that must consist of no other letters than a-z, A-Z, 0-9 or underscore. The specified content is then associated with this identifier.

Setting the same variable name again overwrites the old contents with the new.

The contents of a variable can be referenced in a later command line option when that option name is prefixed with "--expand-", and the name is used as "{{name}}".

--variable can import environment variables into the name space. Opt to either require the environment variable to be set or provide a default value for the variable in case it is not already set.

--variable %name imports the variable called "name" but exits with an error if that environment variable is not already set. To provide a default value if the environment variable is not set, use --variable %name=content or --variable %name@content. Note that on some systems - but not all - environment variables are case insensitive.

Added in curl 8.12.0: you can get a byte range from the source by appending "[start-end]" to the variable name, where start and end are byte offsets to include from the contents. For example, asking for offset "2-10" means offset two to offset ten, inclusive, resulting in 9 bytes in total. "2-2" means a single byte at offset 2. Not providing a second number implies to the end of data. The start offset cannot be larger than the end offset. Asking for a range that is outside of the file size makes the variable contents empty. For example, getting the first one hundred bytes from a given file:

```
curl --variable "fraction[0-99]@filename"
```

Given a byte range that has no data results in an empty string. Asking for a range that is larger than the content makes curl use the piece of the data that exists.

To assign a variable using contents from another variable, use --expand-variable. Like for example assigning a new variable using contents from two other:

```
curl --expand-variable "user={{firstname}} {{lastname}}"
```

When expanding variables, curl supports a set of functions that can make the variable contents more convenient to use. You apply a function to a variable expansion by adding a colon and then list the desired functions in a comma-separated list that is evaluated in a left-to-right order. Variable content holding null bytes that are not encoded when expanded causes an error.

Available functions:

trim

removes all leading and trailing white space.

Example:

```
curl --expand-url https://example.com/{{var:trim}}
```

json

outputs the content using JSON string quoting rules.

Example:

```
curl --expand-data {{data:json}} https://example.com
```

url

shows the content URL (percent) encoded.

Example:

```
curl --expand-url https://example.com/{{path:url}}
```

b64

expands the variable base64 encoded

Example:

```
curl --expand-url https://example.com/{{var:b64}}
```

64dec

decodes a base64 encoded character sequence. If the sequence is not possible to decode, it instead outputs "[64dec-fail]"

Example:

```
curl --expand-url https://example.com/{{var:64dec}}
```

(Added in 8.13.0)

--variable can be used several times in a command line.

Example:

```
curl --variable name=smith --expand-url "https://example.com/{{name}}"
```

Added in 8.3.0. See also --config.

-v, --verbose

Make curl output verbose information during the operation. Useful for debugging and seeing what's going on under the hood. Verbose output lines are prefixed with letters:

>

header sent by curl

<

header received by curl

}

data sent by curl

{

data received by curl

*

additional info provided by curl. Text that adds explanations what goes on and about choices curl does.

If you only want HTTP headers in the output, --show-headers or --dump-header might be more suitable options.

Since curl 8.10, mentioning this option several times in the same argument increases the level of the trace output. As before, a single --verbose or --no-verbose reverts any additions by previous "-vv" again. This means that "-vv -v" is equivalent to a single -v. This avoids unwanted verbosity when the option is mentioned in the command line and curl config files.

Using it twice, e.g. "-vv", outputs time (--trace-time) and transfer ids (--trace-ids), as well as enabling tracing for all protocols (--trace-config protocol).

Adding a third verbose outputs transfer content (--trace-ascii %) and enables tracing of more components (--trace-config read,write,ssl).

A fourth time adds tracing of all network components. (--trace-config network).

Any addition of the verbose option after that has no effect.

If you think this option does not give you the right details, consider using --trace or --trace-ascii instead. Or use it only once and use --trace-config to trace the specific components you wish to see.

Note that verbose output of curl activities and network traffic might contain sensitive data, including usernames, credentials or secret data content. Be aware and be careful when sharing trace logs with others.

When the output contains protocol headers, those lines might include carriage return (ASCII code 13) characters, even on platforms that otherwise normally only use linefeed to signify line separations - as curl shows the exact contents arriving from the server.

This option is global and does not need to be specified for each use of --next.

Providing --verbose multiple times has no extra effect. Disable it again with --no-verbose.
