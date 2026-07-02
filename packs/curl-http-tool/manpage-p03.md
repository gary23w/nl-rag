---
title: "curl (part 3/5)"
source: https://curl.se/docs/manpage.html
domain: curl-http-tool
license: CC-BY-SA-4.0
tags: curl http, http client, data transfer, command-line http
fetched: 2026-07-02
part: 3/5
---

# curl

Use the specified proxy.

The proxy string can be specified with a "protocol://" prefix. No protocol specified or http:// it is treated as an HTTP proxy. Use "socks4://", "socks4a://", "socks5://" or "socks5h://" to request a specific SOCKS version to be used.

Unix domain sockets are supported for socks proxy. Set localhost for the host part. e.g. socks5h://localhost/path/to/socket.sock

HTTPS proxy support works with the "https://" protocol prefix for OpenSSL and GnuTLS. It also works for mbedTLS, Rustls, Schannel and wolfSSL (added in 7.87.0).

Unrecognized and unsupported proxy protocol schemes cause an error.

If the port number is not specified in the proxy string, it is assumed to be 1080.

This option overrides existing environment variables that set the proxy to use. If there is an environment variable setting a proxy, you can set proxy to "" to override it.

All operations that are performed over an HTTP proxy are transparently converted to HTTP. It means that certain protocol specific operations might not be available. This is not the case if you can tunnel through the proxy, as one with the --proxytunnel option.

User and password that might be provided in the proxy string are URL decoded by curl. This allows you to pass in special characters such as @ by using %40 or pass in a colon with %3a.

The proxy host can be specified the same way as the proxy environment variables, including the protocol prefix ("http://") and the embedded user + password.

When a proxy is used, the active FTP mode as set with --ftp-port, cannot be used.

Doing FTP over an HTTP proxy without --proxytunnel makes curl do HTTP with an FTP URL over the proxy. For such transfers, common FTP specific options do not work, including --ssl-reqd and --ftp-ssl-control.

If --proxy is provided several times, the last set value is used.

Example:

```
curl --proxy http://proxy.example https://example.com
```

See also --socks5 and --proxy-basic.

--proxy-anyauth

Automatically pick a suitable authentication method when communicating with the given HTTP proxy. This might cause an extra request/response round-trip.

Example:

```
curl --proxy-anyauth --proxy-user user:passwd -x proxy https://example.com
```

See also --proxy, --proxy-basic and --proxy-digest.

--proxy-basic

Use HTTP Basic authentication when communicating with the given proxy. Use --basic for enabling HTTP Basic with a remote host. Basic is the default authentication method curl uses with proxies.

Providing --proxy-basic multiple times has no extra effect. Disable it again with --no-proxy-basic.

Example:

```
curl --proxy-basic --proxy-user user:passwd -x proxy https://example.com
```

See also --proxy, --proxy-anyauth and --proxy-digest.

--proxy-ca-native

(TLS) Use the operating system's native CA store for certificate verification of the HTTPS proxy.

This option is independent of other HTTPS proxy CA certificate locations set at run time or build time. Those locations are searched in addition to the native CA store.

Equivalent to --ca-native but used in HTTPS proxy context. Refer to --ca-native for TLS backend limitations.

Providing --proxy-ca-native multiple times has no extra effect. Disable it again with --no-proxy-ca-native.

Example:

```
curl --proxy-ca-native https://example.com
```

Added in 8.2.0. See also --ca-native, --cacert, --capath, --dump-ca-embed and --insecure.

--proxy-cacert <file>

Use the specified certificate file to verify the HTTPS proxy. The file may contain multiple CA certificates. The certificate(s) must be in PEM format.

This allows you to use a different trust for the proxy compared to the remote server connected to via the proxy.

Equivalent to --cacert but used in HTTPS proxy context.

If --proxy-cacert is provided several times, the last set value is used.

Example:

```
curl --proxy-cacert CA-file.txt -x https://proxy.example https://example.com
```

See also --proxy-capath, --cacert, --capath, --dump-ca-embed and --proxy.

--proxy-capath <dir>

Same as --capath but used in HTTPS proxy context.

Use the specified certificate directory to verify the proxy. Multiple paths can be provided by separating them with colon (":") (e.g. "path1:path2:path3"). The certificates must be in PEM format, and if curl is built against OpenSSL, the directory must have been processed using the c_rehash utility supplied with OpenSSL. Using --proxy-capath can allow OpenSSL-powered curl to make SSL-connections much more efficiently than using --proxy-cacert if the --proxy-cacert file contains many CA certificates.

If this option is set, the default capath value is ignored.

If --proxy-capath is provided several times, the last set value is used.

Example:

```
curl --proxy-capath /local/directory -x https://proxy.example https://example.com
```

See also --proxy-cacert, --proxy, --capath and --dump-ca-embed.

--proxy-cert <cert[:passwd]>

Use the specified client certificate file when communicating with an HTTPS proxy. The certificate must be PEM format. If the optional password is not specified, it is queried for on the terminal. Use --proxy-key to provide the private key.

This option is the equivalent to --cert but used in HTTPS proxy context.

If --proxy-cert is provided several times, the last set value is used.

Example:

```
curl --proxy-cert file -x https://proxy.example https://example.com
```

See also --proxy, --proxy-key and --proxy-cert-type.

--proxy-cert-type <type>

Set type of the provided client certificate when using HTTPS proxy. PEM, DER, ENG, PROV and P12 are recognized types.

The default type depends on the TLS backend and is usually PEM. For Schannel it is P12. If --proxy-cert is a pkcs11: URI then ENG or PROV is the default type (depending on OpenSSL version).

Equivalent to --cert-type but used in HTTPS proxy context.

If --proxy-cert-type is provided several times, the last set value is used.

Example:

```
curl --proxy-cert-type PEM --proxy-cert file -x https://proxy.example https://example.com
```

See also --proxy-cert and --proxy-key.

--proxy-ciphers <list>

(TLS) Same as --ciphers but used in HTTPS proxy context.

Specify which cipher suites to use in the connection to your HTTPS proxy when it negotiates TLS 1.2 (1.1, 1.0). The list of ciphers suites must specify valid ciphers. Read up on cipher suite details on this URL:

https://curl.se/docs/ssl-ciphers.html

If --proxy-ciphers is provided several times, the last set value is used.

Example:

```
curl --proxy-ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256 -x https://proxy.example https://example.com
```

See also --proxy-tls13-ciphers, --ciphers and --proxy.

--proxy-crlfile <file>

Provide filename for a PEM formatted file with a Certificate Revocation List that specifies peer certificates that are considered revoked when communicating with an HTTPS proxy.

Equivalent to --crlfile but only used in HTTPS proxy context.

If --proxy-crlfile is provided several times, the last set value is used.

Example:

```
curl --proxy-crlfile rejects.txt -x https://proxy.example https://example.com
```

See also --crlfile and --proxy.

--proxy-digest

Use HTTP Digest authentication when communicating with the given proxy. Use --digest for enabling HTTP Digest with a remote host.

Providing --proxy-digest multiple times has no extra effect. Disable it again with --no-proxy-digest.

Example:

```
curl --proxy-digest --proxy-user user:passwd -x proxy https://example.com
```

See also --proxy, --proxy-anyauth and --proxy-basic.

--proxy-header <header/@file>

(HTTP) Extra header to include in the request when sending HTTP to a proxy. You may specify any number of extra headers. This is the equivalent option to --header but is for proxy communication only like in CONNECT requests when you want a separate header sent to the proxy to what is sent to the actual remote host.

curl makes sure that each header you add/replace is sent with the proper end-of-line marker, you should thus not add that as a part of the header content: do not add newlines or carriage returns, they only mess things up for you.

Headers specified with this option are not included in requests that curl knows are not to be sent to a proxy.

This option can take an argument in @filename style, which then adds a header for each line in the input file. Using @- makes curl read the headers from stdin.

This option can be used multiple times to add/replace/remove multiple headers.

--proxy-header can be used several times in a command line.

Examples:

```
curl --proxy-header "X-First-Name: Joe" -x http://proxy https://example.com
curl --proxy-header "User-Agent: surprise" -x http://proxy https://example.com
curl --proxy-header "Host:" -x http://proxy https://example.com
```

See also --proxy and --header.

--proxy-http2

(HTTP) Negotiate HTTP/2 with an HTTPS proxy. The proxy might still only offer HTTP/1 and then curl sticks to using that version.

This has no effect for any other kinds of proxies.

This option is mutually exclusive with "--proxy-http3".

Providing --proxy-http2 multiple times has no extra effect. Disable it again with --no-proxy-http2.

Example:

```
curl --proxy-http2 -x proxy https://example.com
```

For --proxy-http2 to work, it requires that the underlying libcurl is built to support HTTP/2. This option is mutually exclusive with --proxy-http3. Added in 8.1.0. See also --proxy.

--proxy-insecure

Same as --insecure but used in HTTPS proxy context.

Every secure connection curl makes is verified to be secure before the transfer takes place. This option makes curl skip the verification step with a proxy and proceed without checking.

When this option is not used for a proxy using HTTPS, curl verifies the proxy's TLS certificate before it continues: that the certificate contains the right name which matches the hostname and that the certificate has been signed by a CA certificate present in the cert store. See this online resource for further details: https://curl.se/docs/sslcerts.html

WARNING: using this option makes the transfer to the proxy insecure.

Providing --proxy-insecure multiple times has no extra effect. Disable it again with --no-proxy-insecure.

Example:

```
curl --proxy-insecure -x https://proxy.example https://example.com
```

See also --proxy and --insecure.

--proxy-key <key>

Specify the filename for your private key when using client certificates with your HTTPS proxy. This option is the equivalent to --key but used in HTTPS proxy context.

If --proxy-key is provided several times, the last set value is used.

Example:

```
curl --proxy-key here -x https://proxy.example https://example.com
```

See also --proxy-key-type and --proxy.

--proxy-key-type <type>

Specify the private key file type your --proxy-key provided private key uses. DER, PEM, and ENG are supported. If not specified, PEM is assumed.

Equivalent to --key-type but used in HTTPS proxy context.

If --proxy-key-type is provided several times, the last set value is used.

Example:

```
curl --proxy-key-type DER --proxy-key here -x https://proxy.example https://example.com
```

See also --proxy-key and --proxy.

--proxy-negotiate

Use HTTP Negotiate (SPNEGO) authentication when communicating with the given proxy. Use --negotiate for enabling HTTP Negotiate (SPNEGO) with a remote host.

Providing --proxy-negotiate multiple times has no extra effect.

Example:

```
curl --proxy-negotiate --proxy-user user:passwd -x proxy https://example.com
```

See also --proxy-anyauth, --proxy-basic and --proxy-service-name.

--proxy-ntlm

Use HTTP NTLM authentication when communicating with the given proxy. Use --ntlm for enabling NTLM with a remote host.

Providing --proxy-ntlm multiple times has no extra effect. Disable it again with --no-proxy-ntlm.

Example:

```
curl --proxy-ntlm --proxy-user user:passwd -x http://proxy https://example.com
```

See also --proxy-negotiate, --proxy-anyauth and --proxy-user.

--proxy-pass <phrase>

Passphrase for the private key for HTTPS proxy client certificate.

Equivalent to --pass but used in HTTPS proxy context.

If --proxy-pass is provided several times, the last set value is used.

Example:

```
curl --proxy-pass secret --proxy-key here -x https://proxy.example https://example.com
```

See also --proxy and --proxy-key.

--proxy-pinnedpubkey <hashes>

(TLS) Use the specified public key file (or hashes) to verify the proxy. This can be a path to a file which contains a single public key in PEM or DER format, or any number of base64 encoded sha256 hashes preceded by 'sha256//' and separated by ';'.

When negotiating a TLS or SSL connection, the server sends a certificate indicating its identity. A public key is extracted from this certificate and if it does not exactly match the public key provided to this option, curl aborts the connection before sending or receiving any data.

Before curl 8.10.0 this option did not work due to a bug.

If --proxy-pinnedpubkey is provided several times, the last set value is used.

Examples:

```
curl --proxy-pinnedpubkey keyfile https://example.com
curl --proxy-pinnedpubkey 'sha256//ce118b51897f4452dc' https://example.com
```

See also --pinnedpubkey and --proxy.

--proxy-service-name <name>

Set the service name for SPNEGO when doing proxy authentication.

If --proxy-service-name is provided several times, the last set value is used.

Example:

```
curl --proxy-service-name "shrubbery" -x proxy https://example.com
```

See also --service-name, --proxy and --proxy-negotiate.

--proxy-ssl-allow-beast

Do not work around a security flaw in the TLS1.0 protocol known as BEAST when communicating to an HTTPS proxy. If this option is not used, the TLS layer may use workarounds known to cause interoperability problems with some older server implementations.

This option only changes how curl does TLS 1.0 with an HTTPS proxy and has no effect on later TLS versions.

WARNING: this option loosens the TLS security, and by using this flag you ask for exactly that.

Equivalent to --ssl-allow-beast but used in HTTPS proxy context.

Providing --proxy-ssl-allow-beast multiple times has no extra effect. Disable it again with --no-proxy-ssl-allow-beast.

Example:

```
curl --proxy-ssl-allow-beast -x https://proxy.example https://example.com
```

See also --ssl-allow-beast and --proxy.

--proxy-ssl-auto-client-cert

Same as --ssl-auto-client-cert but used in HTTPS proxy context.

This is only supported by Schannel.

Providing --proxy-ssl-auto-client-cert multiple times has no extra effect. Disable it again with --no-proxy-ssl-auto-client-cert.

Example:

```
curl --proxy-ssl-auto-client-cert -x https://proxy.example https://example.com
```

Added in 7.77.0. See also --ssl-auto-client-cert and --proxy.

--proxy-tls13-ciphers <list>

(TLS) Same as --tls13-ciphers but used in HTTPS proxy context.

Specify which cipher suites to use in the connection to your HTTPS proxy when it negotiates TLS 1.3. The list of ciphers suites must specify valid ciphers. Read up on TLS 1.3 cipher suite details on this URL:

https://curl.se/docs/ssl-ciphers.html

This option is used when curl is built to use OpenSSL 1.1.1 or later, Schannel, wolfSSL, or mbedTLS 3.6.0 or later.

Before curl 8.10.0 with mbedTLS or wolfSSL, TLS 1.3 cipher suites were set by using the --proxy-ciphers option.

If --proxy-tls13-ciphers is provided several times, the last set value is used.

Example:

```
curl --proxy-tls13-ciphers TLS_AES_128_GCM_SHA256 -x proxy https://example.com
```

See also --proxy-ciphers, --tls13-ciphers and --proxy.

--proxy-tlsauthtype <type>

Set TLS authentication type with HTTPS proxy. The only supported option is "SRP", for TLS-SRP (RFC 5054). This option works only if the underlying libcurl is built with TLS-SRP support.

Equivalent to --tlsauthtype but used in HTTPS proxy context.

If --proxy-tlsauthtype is provided several times, the last set value is used.

Example:

```
curl --proxy-tlsauthtype SRP -x https://proxy.example https://example.com
```

See also --proxy, --proxy-tlsuser and --proxy-tlspassword.

--proxy-tlspassword <string>

Set password to use with the TLS authentication method specified with --proxy-tlsauthtype when using HTTPS proxy. Requires that --proxy-tlsuser is set.

This option does not work with TLS 1.3.

Equivalent to --tlspassword but used in HTTPS proxy context.

If --proxy-tlspassword is provided several times, the last set value is used.

Example:

```
curl --proxy-tlspassword passwd -x https://proxy.example https://example.com
```

See also --proxy and --proxy-tlsuser.

--proxy-tlsuser <name>

Set username for use for HTTPS proxy with the TLS authentication method specified with --proxy-tlsauthtype. Requires that --proxy-tlspassword also is set.

This option does not work with TLS 1.3.

If --proxy-tlsuser is provided several times, the last set value is used.

Example:

```
curl --proxy-tlsuser smith -x https://proxy.example https://example.com
```

See also --proxy and --proxy-tlspassword.

--proxy-tlsv1

Use at least TLS version 1.x when negotiating with an HTTPS proxy. That means TLS version 1.0 or higher

Equivalent to --tlsv1 but for an HTTPS proxy context.

Providing --proxy-tlsv1 multiple times has no extra effect.

Example:

```
curl --proxy-tlsv1 -x https://proxy.example https://example.com
```

See also --proxy.

-U, --proxy-user <user:password>

Specify the username and password to use for proxy authentication.

If you use a Windows SSPI-enabled curl binary and do either Negotiate or NTLM authentication then you can tell curl to select the username and password from your environment by specifying a single colon with this option: "-U :".

On systems where it works, curl hides the given option argument from process listings. This is not enough to protect credentials from possibly getting seen by other users on the same system as they still are visible for a moment before being cleared. Such sensitive data should be retrieved from a file instead or similar and never used in clear text in a command line.

If --proxy-user is provided several times, the last set value is used.

Example:

```
curl --proxy-user smith:secret -x proxy https://example.com
```

See also --proxy-pass.

--proxy1.0 <host[:port]>

Use the specified HTTP 1.0 proxy. If the port number is not specified, it is assumed at port 1080.

The only difference between this and the HTTP proxy option --proxy, is that attempts to use CONNECT through the proxy specifies an HTTP 1.0 protocol instead of the default HTTP 1.1.

Providing --proxy1.0 multiple times has no extra effect.

Example:

```
curl --proxy1.0 http://proxy https://example.com
```

See also --proxy, --socks5 and --preproxy.

-p, --proxytunnel

When an HTTP proxy is used --proxy, this option makes curl tunnel the traffic through the proxy. The tunnel approach is made with the HTTP proxy CONNECT request and requires that the proxy allows direct connection to the remote port number curl wants to tunnel through to.

To suppress proxy CONNECT response headers when curl is set to output headers use --suppress-connect-headers.

Providing --proxytunnel multiple times has no extra effect. Disable it again with --no-proxytunnel.

Example:

```
curl --proxytunnel -x http://proxy https://example.com
```

See also --proxy.

--pubkey <key>

(SFTP SCP) Public key filename. Allows you to provide your public key in this separate file.

curl attempts to automatically extract the public key from the private key file, so passing this option is generally not required. Note that this public key extraction requires libcurl to be linked against a copy of libssh2 1.2.8 or higher that is itself linked against OpenSSL.

If --pubkey is provided several times, the last set value is used.

Example:

```
curl --pubkey file.pub sftp://example.com/
```

See also --pass.

-Q, --quote <command>

(FTP SFTP) Send an arbitrary command to the remote FTP or SFTP server. Quote commands are sent BEFORE the transfer takes place (immediately after the initial PWD command in an FTP transfer, to be exact). To make commands take place after a successful transfer, prefix them with a dash '-'.

(FTP only) To make commands be sent after curl has changed the working directory, immediately before the file transfer command(s), prefix the command with a '+'.

You may specify any number of commands.

By default curl stops at first failure. To make curl continue even if the command fails, prefix the command with an asterisk (*). Otherwise, if the server returns failure for one of the commands, the entire operation is aborted.

You must send syntactically correct FTP commands as RFC 959 defines to FTP servers, or one of the commands listed below to SFTP servers.

SFTP is a binary protocol. Unlike for FTP, curl interprets SFTP quote commands itself before sending them to the server. Filenames must be provided within double quotes to embed spaces, backslashes, quotes or double quotes. Within double quotes the following escape sequences are available for that purpose: \ \", and \'.

Following is the list of all supported SFTP quote commands:

atime date file

The atime command sets the last access time of the file named by the file operand. The date expression can be all sorts of date strings, see the curl_getdate man page for date expression details. (Added in 7.73.0)

chgrp group file

The chgrp command sets the group ID of the file named by the file operand to the group ID specified by the group operand. The group operand is a decimal integer group ID.

chmod mode file

The chmod command modifies the file mode bits of the specified file. The mode operand is an octal integer mode number.

chown user file

The chown command sets the owner of the file named by the file operand to the user ID specified by the user operand. The user operand is a decimal integer user ID.

ln source_file target_file

The ln and symlink commands create a symbolic link at the target_file location pointing to the source_file location.

mkdir directory_name

The mkdir command creates the directory named by the directory_name operand.

mtime date file

The mtime command sets the last modification time of the file named by the file operand. The date expression can be all sorts of date strings, see the curl_getdate man page for date expression details. (Added in 7.73.0)

pwd

The pwd command returns the absolute path name of the current working directory.

rename source target

The rename command renames the file or directory named by the source operand to the destination path named by the target operand.

rm file

The rm command removes the file specified by the file operand.

rmdir directory

The rmdir command removes the directory entry specified by the directory operand, provided it is empty.

symlink source_file target_file

See ln.

--quote can be used several times in a command line.

Example:

```
curl --quote "DELE file" ftp://example.com/foo
```

See also --request.

--random-file <file>

Deprecated option. This option is ignored (added in 7.84.0). Prior to that it only had an effect on curl if built to use old versions of OpenSSL.

Specify the path name to file containing random data. The data may be used to seed the random engine for SSL connections.

If --random-file is provided several times, the last set value is used.

Example:

```
curl --random-file rubbish https://example.com
```

See also --egd-file.

-r, --range <range>

(HTTP FTP SFTP FILE) Retrieve a byte range (i.e. a partial document) from an HTTP/1.1, FTP or SFTP server or a local FILE. Ranges can be specified in a number of ways.

0-499

specifies the first 500 bytes

500-999

specifies the second 500 bytes

-500

specifies the last 500 bytes

9500-

specifies the bytes from offset 9500 and forward

0-0,-1

specifies the first and last byte only(*)(HTTP)

100-199,500-599

specifies two separate 100-byte ranges(*) (HTTP)

(*) = NOTE that if specifying multiple ranges and the server supports it then it replies with a multiple part response that curl returns as-is. It contains meta information in addition to the requested bytes. Parsing or otherwise transforming this response is the responsibility of the caller.

Only digit characters (0-9) are valid in the 'start' and 'stop' fields of the 'start-stop' range syntax. If a non-digit character is given in the range, the server's response is unspecified, depending on the server's configuration.

Many HTTP/1.1 servers do not have this feature enabled, so that when you attempt to get a range, curl instead gets the whole document.

FTP and SFTP range downloads only support the simple 'start-stop' syntax (optionally with one of the numbers omitted). FTP use depends on the extended FTP command SIZE.

When using this option for HTTP uploads using POST or PUT, functionality is not guaranteed. The HTTP protocol has no standard interoperable resume upload and curl uses a set of headers for this purpose that once proved working for some servers and have been left for those who find that useful.

This command line option is mutually exclusive with --continue-at: you can only use one of them for a single transfer.

If --range is provided several times, the last set value is used.

Example:

```
curl --range 22-44 https://example.com
```

See also --continue-at and --append.

--rate <max request rate>

Specify the maximum transfer frequency you allow curl to use - in number of transfer starts per time unit (sometimes called request rate). Without this option, curl starts the next transfer as fast as possible.

If given several URLs and a transfer completes faster than the allowed rate, curl waits until the next transfer is started to maintain the requested rate. This option has no effect when --parallel is used.

The request rate is provided as "N/U" where N is an integer number and U is a time unit. Supported units are 's' (second), 'm' (minute), 'h' (hour) and 'd' /(day, as in a 24 hour unit). The default time unit, if no "/U" is provided, is number of transfers per hour.

If curl is told to allow 10 requests per minute, it does not start the next request until 6 seconds have elapsed since the previous transfer was started.

This function uses millisecond resolution. If the allowed frequency is set more than 1000 per second, it instead runs unrestricted.

When retrying transfers, enabled with --retry, the separate retry delay logic is used and not this setting.

Starting in version 8.10.0, you can specify the number of time units in the rate expression. Make curl do no more than 5 transfers per 15 seconds with "5/15s" or limit it to 3 transfers per 4 hours with "3/4h". No spaces allowed.

This option is global and does not need to be specified for each use of --next.

If --rate is provided several times, the last set value is used.

Examples:

```
curl --rate 2/s https://example.com ...
curl --rate 3/h https://example.com ...
curl --rate 14/m https://example.com ...
```

Added in 7.84.0. See also --limit-rate and --retry-delay.

--raw

(HTTP) When used, it disables all internal HTTP decoding of content or transfer encodings and instead makes them passed on unaltered, raw.

Providing --raw multiple times has no extra effect. Disable it again with --no-raw.

Example:

```
curl --raw https://example.com
```

See also --tr-encoding.

-e, --referer <URL>

(HTTP) Set the referrer URL in the HTTP request. This can also be set with the --header flag of course. When used with --location you can append ";auto"" to the --referer URL to make curl automatically set the previous URL when it follows a Location: header. The ";auto" string can be used alone, even if you do not set an initial --referer.

If --referer is provided several times, the last set value is used.

Examples:

```
curl --referer "https://fake.example" https://example.com
curl --referer "https://fake.example;auto" -L https://example.com
curl --referer ";auto" -L https://example.com
```

See also --user-agent and --header.

-J, --remote-header-name

(HTTP) Tell the --remote-name option to use the server-specified Content-Disposition filename instead of extracting a filename from the URL. If the server-provided filename contains a path, that is stripped off before the filename is used.

The file is saved in the current directory, or in the directory specified with --output-dir.

If the server specifies a filename and a file with that name already exists in the destination directory, it is not overwritten and an error occurs - unless you allow it by using the --clobber option. If the server does not specify a filename then this option has no effect.

There is no attempt to decode %-sequences (yet) in the provided filename, so this option may provide you with rather unexpected filenames.

This feature uses the name from the "filename" field, it does not yet support the "filename*" field (filenames with explicit character sets).

Starting in 8.19.0, curl falls back and uses the filename extracted from the last redirect header if no "Content-Disposition:" header provides a filename.

WARNING: Exercise judicious use of this option, especially on Windows. A rogue server could send you the name of a DLL or other file that could be loaded automatically by Windows or some third party software.

Providing --remote-header-name multiple times has no extra effect. Disable it again with --no-remote-header-name.

Example:

```
curl -OJ https://example.com/file
```

See also --remote-name.

-O, --remote-name

Write output to a local file named like the remote file we get. (Only the file part of the remote file is used, the path is cut off.)

The file is saved in the current working directory. If you want the file saved in a different directory, make sure you change the current working directory before invoking curl with this option or use --output-dir.

The remote filename to use for saving is extracted from the given URL, nothing else, and if it already exists it is overwritten. If you want the server to be able to choose the filename refer to --remote-header-name which can be used in addition to this option. If the server chooses a filename and that name already exists it is not overwritten.

There is no URL decoding done on the filename. If it has %20 or other URL encoded parts of the name, they end up as-is as filename.

You may use this option as many times as the number of URLs you have.

Before curl 8.10.0, curl returned an error if the URL ended with a slash, which means that there is no filename part in the URL. Starting in 8.10.0, curl sets the filename to the last directory part of the URL or if that also is missing to "curl_response" (without extension) for this situation.

--remote-name is associated with a single URL. Use it once per URL when you use several URLs in a command line.

Examples:

```
curl -O https://example.com/filename
curl -O https://example.com/filename -O https://example.com/file2
```

See also --remote-name-all, --output-dir and --remote-header-name.

--remote-name-all

Change the default action for all given URLs to be dealt with as if --remote-name were used for each one. If you want to disable that for a specific URL after --remote-name-all has been used, you must use "-o -" or --no-remote-name.

Providing --remote-name-all multiple times has no extra effect. Disable it again with --no-remote-name-all.

Example:

```
curl --remote-name-all ftp://example.com/file1 ftp://example.com/file2
```

See also --remote-name.

-R, --remote-time

Make curl attempt to figure out the timestamp of the remote file that is getting downloaded, and if that is available make the local file get that same timestamp.

Providing --remote-time multiple times has no extra effect. Disable it again with --no-remote-time.

Example:

```
curl --remote-time -o foo https://example.com
```

See also --remote-name and --time-cond.

--remove-on-error

Remove the output file if an error occurs. If curl returns an error when told to save output in a local file. This prevents curl from leaving a partial file in the case of an error during transfer.

If the output is not a regular file, this option has no effect.

The --continue-at option cannot be used together with --remove-on-error.

Providing --remove-on-error multiple times has no extra effect. Disable it again with --no-remove-on-error.

Example:

```
curl --remove-on-error -o output https://example.com
```

Added in 7.83.0. See also --fail.

-X, --request <method>

Change the method to use when starting the transfer.

curl passes on the verbatim string you give it in the request without any filter or other safe guards. That includes white space and control characters.

HTTP

Specifies a custom request method to use when communicating with the HTTP server. The specified request method is used instead of the method otherwise used (which defaults to GET). Read the HTTP 1.1 specification for details and explanations. Common additional HTTP requests include PUT and DELETE, while related technologies like WebDAV offers PROPFIND, COPY, MOVE and more.

Normally you do not need this option. All sorts of GET, HEAD, POST and PUT requests are rather invoked by using dedicated command line options.

This option only changes the actual word used in the HTTP request, it does not alter the way curl behaves. For example if you want to make a proper HEAD request, using -X HEAD does not suffice. You need to use the --head option.

If --location is used, the method string you set with --request is used for all requests, which may cause unintended side-effects when curl does not change request method according to the HTTP 30x response codes - and similar. Consider using --follow instead in combination with --request.

FTP

Specifies a custom FTP command to use instead of LIST when doing file lists with FTP.

POP3

Specifies a custom POP3 command to use instead of LIST or RETR.

IMAP

Specifies a custom IMAP command to use instead of LIST.

SMTP

Specifies a custom SMTP command to use instead of HELP or VRFY.

If --request is provided several times, the last set value is used.

Examples:

```
curl --request "DELETE" https://example.com
curl -X NLST ftp://example.com/
```

See also --request-target and --follow.

--request-target <path>

(HTTP) Use an alternative target (path) instead of using the path as provided in the URL. Particularly useful when wanting to issue HTTP requests without leading slash or other data that does not follow the regular URL pattern, like "OPTIONS *".

curl passes on the verbatim string you give it in the request without any filter or other safe guards. That includes white space and control characters.

If --request-target is provided several times, the last set value is used.

Example:

```
curl --request-target "*" -X OPTIONS https://example.com
```

See also --request.

--resolve <[+]host:port:addr[,addr]...>

Provide a custom address for a specific host and port pair. Using this, you can make the curl requests(s) use a specified address and prevent the otherwise normally resolved address to be used. Consider it a sort of /etc/hosts alternative provided on the command line. The port number should be the number used for the specific protocol the host is used for. It means you need several entries if you want to provide addresses for the same host but different ports.

By specifying "*" as host you can tell curl to resolve any host and specific port pair to the specified address. Wildcard is resolved last so any --resolve with a specific host and port is used first.

The provided address set by this option is used even if --ipv4 or --ipv6 is set to make curl use another IP version.

By prefixing the host with a '+' you can make the entry time out after curl's default timeout (1 minute). Note that this only makes sense for long running parallel transfers with a lot of files. In such cases, if this option is used curl tries to resolve the host as it normally would once the timeout has expired.

Provide IPv6 addresses within [brackets].

To redirect connects from a specific hostname or any hostname, independently of port number, consider the --connect-to option.

Support for resolving with wildcard was added in 7.64.0.

Support for the '+' prefix was added in 7.75.0.

Support for specifying the host component as an IPv6 address was added in 8.13.0.

--resolve can be used several times in a command line.

Examples:

```
curl --resolve example.com:443:127.0.0.1 https://example.com
curl --resolve example.com:443:[2001:db8::252f:efd6] https://example.com
```

See also --connect-to and --alt-svc.

--retry <num>

If a transient error is returned when curl tries to perform a transfer, it retries this number of times before giving up. Setting the number to 0 makes curl do no retries (which is the default). Transient error means either: a timeout, an FTP 4xx response code or an HTTP 408, 429, 500, 502, 503, 504, 522 or 524 response code.

When curl is about to retry a transfer, it first waits one second and then for all forthcoming retries it doubles the waiting time until it reaches 10 minutes, which then remains the set fixed delay time between the rest of the retries. By using --retry-delay you disable this exponential backoff algorithm. See also --retry-max-time to limit the total time allowed for retries.

curl complies with the Retry-After: response header if one was present to know when to issue the next retry (added in 7.66.0).

If --retry is provided several times, the last set value is used.

Example:

```
curl --retry 7 https://example.com
```

See also --retry-max-time, --retry-connrefused and --retry-delay.

--retry-all-errors

Retry on any error. This option is used together with --retry.

This option is the "sledgehammer" of retrying. Do not use this option by default (for example in your curlrc), there may be unintended consequences such as sending or receiving duplicate data. Do not use with redirected input or output. You might be better off handling your unique problems in a shell script. Please read the example below.

WARNING: For server compatibility curl attempts to retry failed flaky transfers as close as possible to how they were started, but this is not possible with redirected input or output. For example, before retrying it removes output data from a failed partial transfer that was written to an output file. However this is not true of data redirected to a | pipe or > file, which are not reset. We strongly suggest you do not parse or record output via redirect in combination with this option, since you may receive duplicate data.

By default curl does not return an error for transfers with an HTTP response code that indicates an HTTP error, if the transfer was successful. For example, if a server replies 404 Not Found and the reply is fully received then that is not an error. When --retry is used then curl retries on some HTTP response codes that indicate transient HTTP errors, but that does not include most 4xx response codes such as 404. If you want to retry on all response codes that indicate HTTP errors (4xx and 5xx) then combine with --fail.

Providing --retry-all-errors multiple times has no extra effect. Disable it again with --no-retry-all-errors.

Example:

```
curl --retry 5 --retry-all-errors https://example.com
```

Added in 7.71.0. See also --retry.

--retry-connrefused

In addition to the other conditions, also consider ECONNREFUSED as a transient error for --retry. This option is used together with --retry. Normally, a refused connection is not considered a transient error and therefore would not otherwise trigger a retry.

Providing --retry-connrefused multiple times has no extra effect. Disable it again with --no-retry-connrefused.

Example:

```
curl --retry-connrefused --retry 7 https://example.com
```

See also --retry and --retry-all-errors.

--retry-delay <seconds>

Make curl sleep this amount of time before each retry when a transfer has failed with a transient error (it changes the default backoff time algorithm between retries). This option is only interesting if --retry is also used. Setting this delay to zero makes curl use the default backoff time.

By default, curl uses an exponentially increasing timeout between retries.

Starting in curl 8.16.0, this option accepts a time as decimal number for parts of seconds. The decimal value needs to be provided using a dot (.) as decimal separator - not the local version even if it might be using another separator.

If --retry-delay is provided several times, the last set value is used.

Example:

```
curl --retry-delay 5 --retry 7 https://example.com
```

See also --retry and --retry-max-time.

--retry-max-time <seconds>

The retry timer is reset before the first transfer attempt. Retries are done as usual (see --retry) as long as the timer has not reached this given limit. Notice that if the timer has not reached the limit, the request is made and while performing, it may take longer than this given time period. To limit a single request's maximum time, use --max-time. Set this option to zero to not timeout retries.

The retry timer starts immediately before the first transfer attempt and includes time spent sleeping between retries (such as delays defined by --retry-delay). Before each new retry is started, curl checks whether the elapsed time has reached the specified limit. If it has, no further retries are performed.

A transfer that has already started is allowed to run to completion even if this makes the total wall clock time exceed the limit. Use --max-time to also cap the duration of each individual transfer attempt.

Starting in curl 8.16.0, this option accepts a time as decimal number for parts of seconds. The decimal value needs to be provided using a dot (.) as decimal separator - not the local version even if it might be using another separator.

If --retry-max-time is provided several times, the last set value is used.

Example:

```
curl --retry-max-time 30 --retry 10 https://example.com
```

See also --retry and --retry-delay.

--sasl-authzid <identity>

(LDAP IMAP POP3 SMTP) Use this authorization identity (authzid), during SASL PLAIN authentication, in addition to the authentication identity (authcid) as specified by --user.

If the option is not specified, the server derives the authzid from the authcid, but if specified, and depending on the server implementation, it may be used to access another user's inbox, that the user has been granted access to, or a shared mailbox for example.

If --sasl-authzid is provided several times, the last set value is used.

Example:

```
curl --sasl-authzid zid imap://example.com/
```

Added in 7.66.0. See also --login-options.

--sasl-ir

(LDAP IMAP POP3 SMTP) Enable initial response in SASL authentication. Such an "initial response" is a message sent by the client to the server after the client selects an authentication mechanism.

Providing --sasl-ir multiple times has no extra effect. Disable it again with --no-sasl-ir.

Example:

```
curl --sasl-ir imap://example.com/
```

See also --sasl-authzid.

--service-name <name>

Set the service name for SPNEGO.

If --service-name is provided several times, the last set value is used.

Example:

```
curl --service-name sockd/server https://example.com
```

See also --negotiate and --proxy-service-name.

-S, --show-error

When used with --silent, it makes curl show an error message if it fails.

This option is global and does not need to be specified for each use of --next.

Providing --show-error multiple times has no extra effect. Disable it again with --no-show-error.

Example:

```
curl --show-error --silent https://example.com
```

See also --no-progress-meter.

-i, --show-headers

(HTTP FTP) Show response headers in the output. HTTP response headers can include things like server name, cookies, date of the document, HTTP version and more. With non-HTTP protocols, the "headers" are other server communication.

This option makes the response headers get saved in the same stream/output as the data. --dump-header exists to save headers in a separate stream.

When HTTP headers are output to a tty, curl may use escape codes to make the header field names appear in bold and URLs in "Location:" headers be especially marked as such. Disable the use of terminal escape codes with --no-styled-output. (This means using the --styled-output option with a "--no-" prefix to disable it.)

To view the request headers, consider the --verbose option.

Prior to 7.75.0 curl did not print the headers if --fail was used in combination with this option and there was an error reported by the server.

This option was called --include before 8.10.0. The previous name remains functional.

Providing --show-headers multiple times has no extra effect. Disable it again with --no-show-headers.

Example:

```
curl -i https://example.com
```

See also --verbose and --dump-header.

--sigalgs <list>

(TLS) Set specific signature algorithms to use during SSL session establishment according to RFC 5246, 7.4.1.4.1.

An algorithm can use either a signature algorithm and a hash algorithm pair separated by a "+" (e.g. "ECDSA+SHA224"), or its TLS 1.3 signature scheme name (e.g. "ed25519").

Multiple algorithms can be provided by separating them with ":" (e.g. "DSA+SHA256:rsa_pss_pss_sha256"). The parameter is available as "-sigalgs" in the OpenSSL "s_client" and "s_server" utilities.

"--sigalgs" allows a OpenSSL powered curl to make SSL-connections with exactly the signature algorithms requested by the client, avoiding nontransparent client/server negotiations.

If this option is set, the default signature algorithm list built into OpenSSL are ignored.

If --sigalgs is provided several times, the last set value is used.

Example:

```
curl --sigalgs ecdsa_secp256r1_sha256 https://example.com
```

Added in 8.14.0. See also --ciphers.

-s, --silent

Silent or quiet mode. Do not show progress meter, warning messages or error messages. Makes curl mute. It still outputs the data you ask for, potentially even to the terminal/stdout unless you redirect it.

Use --show-error in addition to this option to disable progress meter but still show error messages.

Providing --silent multiple times has no extra effect. Disable it again with --no-silent.

Example:

```
curl -s https://example.com
```

See also --verbose, --stderr and --no-progress-meter.

--skip-existing

If there is a local file present when a download is requested, the operation is skipped. Note that curl cannot know if the local file was previously downloaded fine, or if it is incomplete etc, it knows if there is a filename present in the file system or not and it skips the transfer if it is.

Providing --skip-existing multiple times has no extra effect. Disable it again with --no-skip-existing.

Example:

```
curl --skip-existing --output local/dir/file https://example.com
```

Added in 8.10.0. See also --output, --remote-name and --no-clobber.

--socks4 <host[:port]>

Use the specified SOCKS4 proxy. If the port number is not specified, it is assumed at port 1080. Using this socket type makes curl resolve the hostname and pass the address on to the proxy.

To specify the proxy on a Unix domain socket, use localhost for host and append the absolute path to the domain socket. For example: "socks4://localhost/path/to/socket.sock" (the scheme may be omitted).

This option overrides any previous use of --proxy, as they are mutually exclusive.

This option is superfluous since you can specify a socks4 proxy with --proxy using a "socks4://" protocol prefix.

--preproxy can be used to specify a SOCKS proxy at the same time proxy is used with an HTTP/HTTPS proxy. In such a case, curl first connects to the SOCKS proxy and then connects (through SOCKS) to the HTTP or HTTPS proxy.

If --socks4 is provided several times, the last set value is used.

Example:

```
curl --socks4 hostname:4096 https://example.com
```

This option is mutually exclusive with --proxy, --socks4a, --socks5 and --socks5-hostname. See also --socks4a, --socks5 and --socks5-hostname.

--socks4a <host[:port]>

Use the specified SOCKS4a proxy. If the port number is not specified, it is assumed at port 1080. This asks the proxy to resolve the hostname.

To specify the proxy on a Unix domain socket, use localhost for host and append the absolute path to the domain socket. For example: "socks4a://localhost/path/to/socket.sock" (the scheme may be omitted).

This option overrides any previous use of --proxy, as they are mutually exclusive.

This option is superfluous since you can specify a socks4a proxy with --proxy using a "socks4a://" protocol prefix.

--preproxy can be used to specify a SOCKS proxy at the same time --proxy is used with an HTTP/HTTPS proxy. In such a case, curl first connects to the SOCKS proxy and then connects (through SOCKS) to the HTTP or HTTPS proxy.

If --socks4a is provided several times, the last set value is used.

Example:

```
curl --socks4a hostname:4096 https://example.com
```

This option is mutually exclusive with --proxy, --socks4, --socks5 and --socks5-hostname. See also --socks4, --socks5 and --socks5-hostname.

--socks5 <host[:port]>

Use the specified SOCKS5 proxy - but resolve the hostname locally. If the port number is not specified, it is assumed at port 1080.

To specify the proxy on a Unix domain socket, use localhost for host and append the absolute path to the domain socket. For example: "socks5://localhost/path/to/socket.sock" (the scheme may be omitted).

This option overrides any previous use of --proxy, as they are mutually exclusive.

This option is superfluous since you can specify a socks5 proxy with --proxy using a "socks5://" protocol prefix.

--preproxy can be used to specify a SOCKS proxy at the same time --proxy is used with an HTTP/HTTPS proxy. In such a case, curl first connects to the SOCKS proxy and then connects (through SOCKS) to the HTTP or HTTPS proxy.

This option does not work with FTPS or LDAP.

If --socks5 is provided several times, the last set value is used.

Examples:

```
curl --socks5 proxy.example:7000 https://example.com
curl --socks5 localhost/path/unix-domain https://example.com
```

This option is mutually exclusive with --proxy, --socks4, --socks4a and --socks5-hostname. See also --socks5-hostname and --socks4a.

--socks5-basic

Use username/password authentication when connecting to a SOCKS5 proxy. The username/password authentication is enabled by default. Use --socks5-gssapi to force GSS-API authentication to SOCKS5 proxies.

Providing --socks5-basic multiple times has no extra effect.

Example:

```
curl --socks5-basic --socks5 hostname:4096 https://example.com
```

See also --socks5.

--socks5-gssapi

(GSS/kerberos) Use GSS-API authentication when connecting to a SOCKS5 proxy. The GSS-API authentication is enabled by default (if curl is compiled with GSS-API support). Use --socks5-basic to force username/password authentication to SOCKS5 proxies.

Providing --socks5-gssapi multiple times has no extra effect. Disable it again with --no-socks5-gssapi.

Example:

```
curl --socks5-gssapi --socks5 hostname:4096 https://example.com
```

See also --socks5.

--socks5-gssapi-nec

(GSS/kerberos) As part of the GSS-API negotiation a protection mode is negotiated. RFC 1961 says in section 4.3/4.4 it should be protected, but the NEC reference implementation does not. The option --socks5-gssapi-nec allows the unprotected exchange of the protection mode negotiation.

Providing --socks5-gssapi-nec multiple times has no extra effect. Disable it again with --no-socks5-gssapi-nec.

Example:

```
curl --socks5-gssapi-nec --socks5 hostname:4096 https://example.com
```

See also --socks5.

--socks5-gssapi-service <name>

Set the service name for a socks server. Default is rcmd/server-fqdn.

If --socks5-gssapi-service is provided several times, the last set value is used.

Example:

```
curl --socks5-gssapi-service sockd --socks5 hostname:4096 https://example.com
```

See also --socks5.

--socks5-hostname <host[:port]>

Use the specified SOCKS5 proxy (and let the proxy resolve the hostname). If the port number is not specified, it is assumed at port 1080.

To specify the proxy on a Unix domain socket, use localhost for host and append the absolute path to the domain socket. For example: "socks5h://localhost/path/to/socket.sock" (the scheme may be omitted).

This option overrides any previous use of --proxy, as they are mutually exclusive.

This option is superfluous since you can specify a socks5 hostname proxy with --proxy using a "socks5h://" protocol prefix.

--preproxy can be used to specify a SOCKS proxy at the same time --proxy is used with an HTTP/HTTPS proxy. In such a case, curl first connects to the SOCKS proxy and then connects (through SOCKS) to the HTTP or HTTPS proxy.

If --socks5-hostname is provided several times, the last set value is used.

Example:

```
curl --socks5-hostname proxy.example:7000 https://example.com
```

This option is mutually exclusive with --proxy, --socks4, --socks4a and --socks5. See also --socks5 and --socks4a.

-Y, --speed-limit <speed>

If a transfer is slower than this set speed (in bytes per second) for a given number of seconds, it gets aborted. The time period is set with --speed-time and is 30 seconds by default.

If --speed-limit is provided several times, the last set value is used.

Example:

```
curl --speed-limit 300 --speed-time 10 https://example.com
```

See also --speed-time, --limit-rate and --max-time.

-y, --speed-time <seconds>

If a transfer runs slower than speed-limit bytes per second during a speed-time period, the transfer is aborted. If speed-time is used, the default speed-limit is 1 unless set with --speed-limit.

This option controls transfers (in both directions) but does not affect slow connects etc. If this is a concern for you, try the --connect-timeout option.

If --speed-time is provided several times, the last set value is used.

Example:

```
curl --speed-limit 300 --speed-time 10 https://example.com
```

See also --speed-limit and --limit-rate.

--ssl

(FTP IMAP POP3 SMTP LDAP) Warning: this is considered an insecure option. Consider using --ssl-reqd instead to be sure curl upgrades to a secure connection.

Try to use SSL/TLS for the connection - often referred to as STARTTLS or STLS because of the involved commands. Reverts to a non-secure connection if the server does not support SSL/TLS. See also --ftp-ssl-control and --ssl-reqd for different levels of encryption required.

This option is handled in LDAP (added in 7.81.0). It is fully supported by the OpenLDAP backend and ignored by the generic ldap backend.

Please note that a server may close the connection if the negotiation fails.

If set, this option overrides --ftp-ssl-control.

This option was formerly known as --ftp-ssl. That option name can still be used but might be removed in a future version.

Providing --ssl multiple times has no extra effect. Disable it again with --no-ssl.

Example:

```
curl --ssl pop3://example.com/
```

See also --ssl-reqd, --insecure and --ciphers.

--ssl-allow-beast

(TLS) Do not work around a security flaw in the TLS1.0 protocol known as BEAST. If this option is not used, the TLS layer may use workarounds known to cause interoperability problems with some older server implementations.

This option only changes how curl does TLS 1.0 and has no effect on later TLS versions.

WARNING: this option loosens the TLS security, and by using this flag you ask for exactly that.

Providing --ssl-allow-beast multiple times has no extra effect. Disable it again with --no-ssl-allow-beast.

Example:

```
curl --ssl-allow-beast https://example.com
```

See also --proxy-ssl-allow-beast and --insecure.

--ssl-auto-client-cert

(TLS) (Schannel) Automatically locate and use a client certificate for authentication, when requested by the server. Since the server can request any certificate that supports client authentication in the OS certificate store it could be a privacy violation and unexpected.

Providing --ssl-auto-client-cert multiple times has no extra effect. Disable it again with --no-ssl-auto-client-cert.

Example:

```
curl --ssl-auto-client-cert https://example.com
```

Added in 7.77.0. See also --proxy-ssl-auto-client-cert.

--ssl-no-revoke

(TLS) (Schannel) Disable certificate revocation checks. WARNING: this option loosens the SSL security, and by using this flag you ask for exactly that.

Providing --ssl-no-revoke multiple times has no extra effect. Disable it again with --no-ssl-no-revoke.

Example:

```
curl --ssl-no-revoke https://example.com
```

See also --crlfile.

--ssl-reqd

(FTP IMAP POP3 SMTP LDAP) Require SSL/TLS for the connection - often referred to as STARTTLS or STLS because of the involved commands. Terminates the connection if the transfer cannot be upgraded to use SSL/TLS.

This option is handled in LDAP (added in 7.81.0). It is fully supported by the OpenLDAP backend and rejected by the generic ldap backend if explicit TLS is required.

This option is unnecessary if you use a URL scheme that in itself implies immediate and implicit use of TLS, like for FTPS, IMAPS, POP3S, SMTPS and LDAPS. Such a transfer always fails if the TLS handshake does not work.

This option was formerly known as --ftp-ssl-reqd.

Providing --ssl-reqd multiple times has no extra effect. Disable it again with --no-ssl-reqd.

Example:

```
curl --ssl-reqd ftp://example.com
```

See also --ssl and --insecure.

--ssl-revoke-best-effort

(TLS) (Schannel) Ignore certificate revocation checks when they failed due to missing/offline distribution points for the revocation check lists.

Providing --ssl-revoke-best-effort multiple times has no extra effect. Disable it again with --no-ssl-revoke-best-effort.

Example:

```
curl --ssl-revoke-best-effort https://example.com
```

Added in 7.70.0. See also --crlfile and --insecure.

--ssl-sessions <filename>

(TLS) **WARNING**: this option is experimental. Do not use in production.

Use the given file to load SSL session tickets into curl's cache before starting any transfers. At the end of a successful curl run, the cached SSL sessions tickets are saved to the file, replacing any previous content.

The file does not have to exist, but curl reports an error if it is unable to create it. Unused loaded tickets are saved again, unless they get replaced or purged from the cache for space reasons.

Using a session file allows "--tls-earlydata" to send the first request in "0-RTT" mode, should an SSL session with the feature be found. Note that a server may not support early data. Also note that early data does not provide forward secrecy, e.g. is not as secure.

The SSL session tickets are stored as base64 encoded text, each ticket on its own line. The hostnames are cryptographically salted and hashed. While this prevents someone from easily seeing the hosts you contacted, they could still check if a specific hostname matches one of the values.

This feature requires that the underlying libcurl was built with the experimental SSL session import/export feature (SSLS-EXPORT) enabled.

If --ssl-sessions is provided several times, the last set value is used.

Example:

```
curl --ssl-sessions sessions.txt https://example.com
```

Added in 8.12.0. See also --tls-earlydata.

-2, --sslv2

(SSL) This option previously asked curl to use SSLv2, but is now ignored (added in 7.77.0). SSLv2 is widely considered insecure (see RFC 6176).

Providing --sslv2 multiple times has no extra effect.

Example:

```
curl --sslv2 https://example.com
```

For --sslv2 to work, it requires that the underlying libcurl is built to support TLS. This option is mutually exclusive with --sslv3, --tlsv1, --tlsv1.1 and --tlsv1.2. See also --http1.1 and --http2.

-3, --sslv3

(SSL) This option previously asked curl to use SSLv3, but is now ignored (added in 7.77.0). SSLv3 is widely considered insecure (see RFC 7568).

Providing --sslv3 multiple times has no extra effect.

Example:

```
curl --sslv3 https://example.com
```

For --sslv3 to work, it requires that the underlying libcurl is built to support TLS. This option is mutually exclusive with --sslv2, --tlsv1, --tlsv1.1 and --tlsv1.2. See also --http1.1 and --http2.

--stderr <file>

Redirect all writes to stderr to the specified file instead. If the filename is a plain '-', it is instead written to stdout.

This option is global and does not need to be specified for each use of --next.

If --stderr is provided several times, the last set value is used.

Example:

```
curl --stderr output.txt https://example.com
```

See also --verbose and --silent.

--styled-output
