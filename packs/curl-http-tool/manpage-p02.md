---
title: "curl (part 2/5)"
source: https://curl.se/docs/manpage.html
domain: curl-http-tool
license: CC-BY-SA-4.0
tags: curl http, http client, data transfer, command-line http
fetched: 2026-07-02
part: 2/5
---

## All options

--abstract-unix-socket <path>

(HTTP) Connect to the server through an abstract Unix domain socket, instead of using the network. Note: netstat shows the path of an abstract socket prefixed with "@", however the <path> argument should not have this leading character.

If --abstract-unix-socket is provided several times, the last set value is used.

Example:

```
curl --abstract-unix-socket socketpath https://example.com
```

See also --unix-socket.

--alt-svc <filename>

(HTTPS) Enable the alt-svc parser. If the filename points to an existing alt-svc cache file, that gets used. After a completed transfer, the cache is saved to the filename again if it has been modified.

Specify a "" filename (zero length) to avoid loading/saving and make curl handle the cache in memory.

You may want to restrict your umask to prevent other users on the same system to access the created file.

If this option is used several times, curl loads contents from all the files but the last one is used for saving.

--alt-svc can be used several times in a command line.

Example:

```
curl --alt-svc svc.txt https://example.com
```

See also --resolve and --connect-to.

--anyauth

(HTTP) Figure out authentication method automatically, and use the most secure one the remote site claims to support. This is done by first doing a request and checking the response-headers, thus possibly inducing an extra network round-trip. This option is used instead of setting a specific authentication method, which you can do with --basic, --digest, --ntlm, and --negotiate.

Using --anyauth is not recommended if you do uploads from stdin, since it may require data to be sent twice and then the client must be able to rewind. If the need should arise when uploading from stdin, the upload operation fails.

Used together with --user.

Example:

```
curl --anyauth --user me:pwd https://example.com
```

See also --proxy-anyauth, --basic and --digest.

-a, --append

(FTP SFTP) When used in an upload, this option makes curl append to the target file instead of overwriting it. If the remote file does not exist, it is created. Note that this flag is ignored by some SFTP servers (including OpenSSH).

Providing --append multiple times has no extra effect. Disable it again with --no-append.

Example:

```
curl --upload-file local --append ftp://example.com/
```

See also --range and --continue-at.

--aws-sigv4 <provider1[:prvdr2[:reg[:srv]]]>

(HTTP) Use AWS V4 signature authentication in the transfer.

The provider argument is a string that is used by the algorithm when creating outgoing authentication headers.

The region argument is a string that points to a geographic area of a resources collection (region-code) when the region name is omitted from the endpoint.

The service argument is a string that points to a function provided by a cloud (service-code) when the service name is omitted from the endpoint.

If --aws-sigv4 is provided several times, the last set value is used.

Example:

```
curl --aws-sigv4 "aws:amz:us-east-2:es" --user "key:secret" https://example.com
```

Added in 7.75.0. See also --basic and --user.

--basic

(HTTP) Use HTTP Basic authentication with the remote host. This method is the default and this option is usually pointless, unless you use it to override a previously set option that sets a different authentication method (such as --ntlm, --digest, or --negotiate).

Used together with --user.

Providing --basic multiple times has no extra effect. Disable it again with --no-basic.

Example:

```
curl -u name:password --basic https://example.com
```

See also --proxy-basic.

--ca-native

(TLS) Use the operating system's native CA store for certificate verification.

This option is independent of other CA certificate locations set at run time or build time. Those locations are searched in addition to the native CA store.

This option works with OpenSSL and its forks (BoringSSL, LibreSSL, etc) on Windows (Added in 7.71.0) and on Apple OS when libcurl is built with Apple SecTrust enabled. (Added in 8.17.0)

This option works with wolfSSL on Windows, Linux (Debian, Ubuntu, Gentoo, Fedora, RHEL), macOS, Android and iOS. (Added in 8.3.0)

This option works with GnuTLS (Added in 8.5.0) and also uses Apple SecTrust when libcurl is built with it. (Added in 8.17.0)

This option works with Rustls on Windows, macOS, Android and iOS. On Linux it is equivalent to using the Mozilla CA certificate bundle. When used with Rustls _only_ the native CA store is consulted, not other locations set at run time or build time. (Added in 8.13.0)

This option currently has no effect for Schannel. This is the native TLS library from Microsoft, that by default uses the native CA store for verification unless overridden by a CA certificate location setting.

Providing --ca-native multiple times has no extra effect. Disable it again with --no-ca-native.

Example:

```
curl --ca-native https://example.com
```

Added in 8.2.0. See also --cacert, --capath, --dump-ca-embed, --insecure and --proxy-ca-native.

--cacert <file>

(TLS) Use the specified certificate file to verify the peer. The file may contain multiple CA certificates. The certificate(s) must be in PEM format. Normally curl is built to use a default file for this, so this option is typically used to alter that default file.

curl recognizes the environment variable named 'CURL_CA_BUNDLE' if it is set and the TLS backend is not Schannel, and uses the given path as a path to a CA cert bundle. This option overrides that variable.

(Windows) curl automatically looks for a CA certs file named 'curl-ca-bundle.crt', either in the same directory as curl.exe, or in the Current Working Directory, or in any folder along your PATH.

curl 8.11.0 added a build-time option to disable this search behavior, and another option to restrict search to the application's directory.

(Schannel) This option is supported for Schannel in Windows 7 or later (added in 7.60.0). This option is supported for backward compatibility with other SSL engines; instead it is recommended to use Windows' store of root certificates (the default for Schannel).

If --cacert is provided several times, the last set value is used.

Example:

```
curl --cacert CA-file.txt https://example.com
```

See also --capath, --dump-ca-embed and --insecure.

--capath <dir>

(TLS) Use the specified certificate directory to verify the peer. If curl is built against OpenSSL, multiple paths can be provided by separating them with the appropriate platform-specific separator (e.g. "path1:path2:path3" on Unix-style platforms for "path1;path2;path3" on Windows).

The certificates must be in PEM format, and if curl is built against OpenSSL, the directory must have been processed using the c_rehash utility supplied with OpenSSL. Using --capath can allow OpenSSL-powered curl to make SSL-connections much more efficiently than using --cacert if the --cacert file contains many CA certificates.

If this option is set, the default capath value is ignored.

If --capath is provided several times, the last set value is used.

Example:

```
curl --capath /local/directory https://example.com
```

See also --cacert, --dump-ca-embed and --insecure.

-E, --cert <certificate[:password]>

(TLS) Use the specified client certificate file when getting a file with HTTPS, FTPS or another SSL-based protocol. The certificate must be PEM format. If the optional password is not specified, it is queried for on the terminal. Note that this option assumes a certificate file that is the private key and the client certificate concatenated. See --cert and --key to specify them independently.

In the <certificate> portion of the argument, you must escape the character ":" as "\:" so that it is not recognized as the password delimiter. Similarly, you must escape the double quote character as \" so that it is not recognized as an escape character.

If curl is built against OpenSSL, and the engine pkcs11 or pkcs11 provider is available, then a PKCS#11 URI (RFC 7512) can be used to specify a certificate located in a PKCS#11 device. A string beginning with "pkcs11:" is interpreted as a PKCS#11 URI. If a PKCS#11 URI is provided, then the --engine option is set as "pkcs11" if none was provided and the --cert-type option is set as "ENG" or "PROV" if none was provided (depending on OpenSSL version).

If curl is built against GnuTLS, a PKCS#11 URI can be used to specify a certificate located in a PKCS#11 device. A string beginning with "pkcs11:" is interpreted as a PKCS#11 URI.

(Schannel) Client certificates must be specified by a path expression to a certificate store. (Loading PFX is not supported; you can import it to a store first). You can use "<store location>\<store name>\<thumbprint>" to refer to a certificate in the system certificates store, for example, "CurrentUser\MY\934a7ac6f8a5d579285a74fa61e19f23ddfe8d7a". Thumbprint is usually a SHA-1 hex string which you can see in certificate details. Following store locations are supported: CurrentUser, LocalMachine, CurrentService, Services, CurrentUserGroupPolicy, LocalMachineGroupPolicy and LocalMachineEnterprise.

If --cert is provided several times, the last set value is used.

Example:

```
curl --cert certfile --key keyfile https://example.com
```

See also --cert-type, --key and --key-type.

--cert-status

(TLS) Verify the status of the server certificate by using the Certificate Status Request (aka. OCSP stapling) TLS extension.

If this option is enabled and the server sends an invalid (e.g. expired) response, if the response suggests that the server certificate has been revoked, or no response at all is received, the verification fails.

This support is currently only implemented in the OpenSSL and GnuTLS backends.

Providing --cert-status multiple times has no extra effect. Disable it again with --no-cert-status.

Example:

```
curl --cert-status https://example.com
```

See also --pinnedpubkey.

--cert-type <type>

(TLS) Set type of the provided client certificate. PEM, DER, ENG, PROV and P12 are recognized types.

The default type depends on the TLS backend and is usually PEM. For Schannel it is P12. If --cert is a pkcs11: URI then ENG or PROV is the default type (depending on OpenSSL version).

If --cert-type is provided several times, the last set value is used.

Example:

```
curl --cert-type PEM --cert file https://example.com
```

See also --cert, --key and --key-type.

--ciphers <list>

(TLS) Specify which cipher suites to use in the connection if it negotiates TLS 1.2 (1.1, 1.0). The list of ciphers suites must specify valid ciphers. Read up on cipher suite details on this URL:

https://curl.se/docs/ssl-ciphers.html

If --ciphers is provided several times, the last set value is used.

Example:

```
curl --ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256 https://example.com
```

See also --tls13-ciphers, --proxy-ciphers and --curves.

--compressed

(HTTP) Request a compressed response using one of the algorithms curl supports, and automatically decompress the content.

Response headers are not modified when saved, so if they are "interpreted" separately again at a later point they might appear to be saying that the content is (still) compressed; while in fact it has already been decompressed.

If this option is used and the server sends an unsupported encoding, curl reports an error. This is a request, not an order; the server may or may not deliver data compressed.

WARNING: when decompressing data, even tiny transfers might be expanded and generate a huge amount of bytes. You might want to limit using this option to only known and trusted sites using secure protocols, perhaps in combination with --max-filesize.

Providing --compressed multiple times has no extra effect. Disable it again with --no-compressed.

Example:

```
curl --compressed https://example.com
```

See also --compressed-ssh.

--compressed-ssh

(SCP SFTP) Enable SSH compression. This is a request, not an order; the server may or may not do it. This allows the data to be sent compressed over the wire, and automatically decompressed in the receiving end, to save bandwidth.

Providing --compressed-ssh multiple times has no extra effect. Disable it again with --no-compressed-ssh.

Example:

```
curl --compressed-ssh sftp://example.com/
```

See also --compressed.

-K, --config <file>

Specify a text file to read curl arguments from. The command line arguments found in the text file are used as if they were provided on the command line.

Options and their parameters must be specified on the same line in the file, separated by whitespace, colon, or the equals sign. Long option names can optionally be given in the config file without the initial double dashes and if so, the colon or equals characters can be used as separators. If the option is specified with one or two dashes, there can be no colon or equals character between the option and its parameter.

If the parameter contains whitespace or starts with a colon (:) or equals sign (=), it must be specified enclosed within double quotes ("like this"). Within double quotes the following escape sequences are available: \ \", \t, \n, \r and \v. A backslash preceding any other letter is ignored.

If the first non-blank column of a config line is a '#' character, that line is treated as a comment.

Only write one option per physical line in the config file. A single line is required to be no more than 10 megabytes (since 8.2.0).

Specify the filename to --config as minus "-" to make curl read the file from stdin.

Note that to be able to specify a URL in the config file, you need to specify it using the --url option, and not by writing the URL on its own line. It could look similar to this:

```
url = "https://curl.se/docs/"
 
# --- Example file ---
# this is a comment
url = "example.com"
output = "curlhere.html"
user-agent = "superagent/1.0"
 
# and fetch another URL too
url = "example.com/docs/manpage.html"
-O
referer = "http://nowhereatall.example.com/"
# --- End of example file ---
```

When curl is invoked, it (unless --disable is used) checks for a default config file and uses it if found, even when --config is used. The default config file is checked for in the following places in this order:

1) "$CURL_HOME/.curlrc"

2) "$XDG_CONFIG_HOME/curlrc" (Added in 7.73.0)

3) "$HOME/.curlrc"

4) Windows: "%USERPROFILE%\.curlrc"

5) Windows: "%APPDATA%\.curlrc"

6) Windows: "%USERPROFILE%\Application Data\.curlrc"

7) Non-Windows: use getpwuid to find the home directory

8) On Windows, if it finds no .curlrc file in the sequence described above, it checks for one in the same directory the curl executable is placed.

On Windows two filenames are checked per location: .curlrc and _curlrc, preferring the former. Older versions on Windows checked for _curlrc only.

--config can be used several times in a command line.

Example:

```
curl --config file.txt https://example.com
```

See also --disable.

--connect-timeout <seconds>

Maximum time in seconds that you allow curl's connection to take. This only limits the connection phase, so if curl connects within the given period it continues - if not it exits.

This option accepts decimal values. The decimal value needs to be provided using a dot (.) as decimal separator - not the local version even if it might be using another separator.

The connection phase is considered complete when the DNS lookup and requested TCP, TLS or QUIC handshakes are done.

If --connect-timeout is provided several times, the last set value is used.

Examples:

```
curl --connect-timeout 20 https://example.com
curl --connect-timeout 3.14 https://example.com
```

See also --max-time.

--connect-to <HOST1:PORT1:HOST2:PORT2>

For a request intended for the "HOST1:PORT1" pair, connect to "HOST2:PORT2" instead. This option is only used to establish the network connection. It does NOT affect the hostname/port number that is used for TLS/SSL (e.g. SNI, certificate verification) or for the application protocols.

"HOST1" and "PORT1" may be empty strings, meaning any host or any port number. "HOST2" and "PORT2" may also be empty strings, meaning use the request's original hostname and port number.

A hostname specified to this option is compared as a string, so it needs to match the name used in the request URL. It can be either numerical such as "127.0.0.1" or the full hostname such as "example.org".

Example: redirect connects from the example.com hostname to 127.0.0.1 independently of port number:

```
curl --connect-to example.com::127.0.0.1: https://example.com/
```

Example: redirect connects from all hostnames to 127.0.0.1 independently of port number:

```
curl --connect-to ::127.0.0.1: http://example.com/
```

--connect-to can be used several times in a command line.

Example:

```
curl --connect-to example.com:443:example.net:8443 https://example.com
```

See also --resolve and --header.

-C, --continue-at <offset>

Resume a previous transfer from the given byte offset. The given offset is the exact number of bytes that are skipped, counting from the beginning of the source file before it is transferred to the destination. If used with uploads, the FTP server command SIZE is not used by curl.

Use "-C -" to instruct curl to automatically find out where/how to resume the transfer. It then uses the given output/input files to figure that out.

When using this option for HTTP uploads using POST or PUT, functionality is not guaranteed. The HTTP protocol has no standard interoperable resume upload and curl uses a set of headers for this purpose that once proved working for some servers and have been left for those who find that useful.

This command line option is mutually exclusive with --range: you can only use one of them for a single transfer.

The --no-clobber and --remove-on-error options cannot be used together with --continue-at.

If --continue-at is provided several times, the last set value is used.

Examples:

```
curl -C - https://example.com
curl -C 400 https://example.com
```

See also --range.

-b, --cookie <data|filename>

(HTTP) This option has two slightly separate cookie sending functions.

Either: pass the exact data to send to the HTTP server in the Cookie header. It is supposedly data previously received from the server in a "Set-Cookie:" line. The data should be in the format "NAME1=VALUE1; NAME2=VALUE2". When given a set of specific cookies, curl populates its cookie header with this content explicitly in all outgoing request(s). If multiple requests are done due to authentication, followed redirects or similar, they all get this cookie header passed on.

Or: If no "=" symbol is used in the argument, it is instead treated as a filename to read previously stored cookie from. This option also activates the cookie engine which makes curl record incoming cookies, which may be handy if you are using this in combination with the --location option or do multiple URL transfers on the same invoke.

If the filename is a single minus ("-"), curl reads the contents from stdin. If the filename is an empty string ("") and is the only cookie input, curl activates the cookie engine without any cookies.

The file format of the file to read cookies from should be plain HTTP headers (Set-Cookie style) or the Netscape/Mozilla cookie file format.

The file specified with --cookie is only used as input. No cookies are written to that file. To store cookies, use the --cookie-jar option.

If you use the Set-Cookie file format and do not specify a domain then the cookie is not sent since the domain never matches. To address this, set a domain in Set-Cookie line (doing that includes subdomains) or preferably: use the Netscape format.

Users often want to both read cookies from a file and write updated cookies back to a file, so using both --cookie and --cookie-jar in the same command line is common. curl ignores filenames specified with --cookie which do not exist or point to a directory.

If curl is built with PSL (Public Suffix List) support, it detects and discards cookies that are specified for such suffix domains that should not be allowed to have cookies. If curl is not built with PSL support, it has no ability to stop super cookies.

--cookie can be used several times in a command line.

Examples:

```
curl -b "" https://example.com
curl -b cookiefile https://example.com
curl -b cookiefile -c cookiefile https://example.com
curl -b name=Jane https://example.com
```

See also --cookie-jar and --junk-session-cookies.

-c, --cookie-jar <filename>

(HTTP) Specify to which file you want curl to write all cookies after a completed operation. curl writes all cookies from its in-memory cookie storage to the given file at the end of operations. Even if no cookies are known, a file is created so that it removes any formerly existing cookies from the file. The file uses the Netscape cookie file format. If you set the filename to a single minus, "-", the cookies are written to stdout.

The file specified with --cookie-jar is only used for output. No cookies are read from the file. To read cookies, use the --cookie option. Both options can specify the same file.

This command line option activates the cookie engine that makes curl record and use cookies. The --cookie option also activates it.

If the cookie jar cannot be created or written to, the whole curl operation does not fail or even report an error clearly. Using --verbose gets a warning displayed, but that is the only visible feedback you get about this possibly lethal situation.

You may want to restrict your umask to prevent other users on the same system to access the created file.

If --cookie-jar is provided several times, the last set value is used.

Examples:

```
curl -c store-here.txt https://example.com
curl -c store-here.txt -b read-these https://example.com
```

See also --cookie and --junk-session-cookies.

--create-dirs

When used in conjunction with the --output option, curl creates the necessary local directory hierarchy as needed. This option creates the directories mentioned with the --output option combined with the path possibly set with --output-dir. If the combined output filename uses no directory, or if the directories it mentions already exist, no directories are created.

Created directories are made with mode 0750 on Unix-style file systems.

To create remote directories when using FTP or SFTP, try --ftp-create-dirs.

Providing --create-dirs multiple times has no extra effect. Disable it again with --no-create-dirs.

Example:

```
curl --create-dirs --output local/dir/file https://example.com
```

See also --ftp-create-dirs and --output-dir.

--create-file-mode <mode>

(SFTP SCP FILE) When curl is used to create files remotely using one of the supported protocols, this option allows the user to set which 'mode' to set on the file at creation time, instead of the default 0644.

This option takes an octal number as argument.

If --create-file-mode is provided several times, the last set value is used.

Example:

```
curl --create-file-mode 0777 -T localfile sftp://example.com/new
```

Added in 7.75.0. See also --ftp-create-dirs.

--crlf

(FTP SMTP) Convert line feeds to carriage return plus line feeds in upload. Useful for MVS (OS/390).

Providing --crlf multiple times has no extra effect. Disable it again with --no-crlf.

Example:

```
curl --crlf -T file ftp://example.com/
```

See also --use-ascii.

--crlfile <file>

(TLS) Provide a file using PEM format with a Certificate Revocation List that may specify peer certificates that are to be considered revoked.

If --crlfile is provided several times, the last set value is used.

Example:

```
curl --crlfile rejects.txt https://example.com
```

See also --cacert and --capath.

--curves <list>

(TLS) Set specific curves to use during SSL session establishment according to RFC 8422, 5.1. Multiple algorithms can be provided by separating them with ":" (e.g. "X25519:P-521"). The parameter is available identically in the OpenSSL "s_client" and "s_server" utilities.

--curves allows a OpenSSL powered curl to make SSL-connections with exactly the (EC) curve requested by the client, avoiding nontransparent client/server negotiations.

If this option is set, the default curves list built into OpenSSL are ignored.

If --curves is provided several times, the last set value is used.

Example:

```
curl --curves X25519 https://example.com
```

Added in 7.73.0. See also --ciphers.

-d, --data <data>

(HTTP MQTT) Send the specified data in a POST request to the HTTP server, in the same way that a browser does when a user has filled in an HTML form and presses the submit button. This option makes curl pass the data to the server using the content-type application/x-www-form-urlencoded. Compared to --form.

--data-raw is almost the same but does not have a special interpretation of the @ character. To post data purely binary, you should instead use the --data-binary option. To URL-encode the value of a form field you may use --data-urlencode.

If any of these options is used more than once on the same command line, the data pieces specified are merged with a separating &-symbol. Thus, using '-d name=daniel -d skill=lousy' would generate a post chunk that looks like 'name=daniel&skill=lousy'.

If you start the data with the letter @, the rest should be a filename to read the data from, or - if you want curl to read the data from stdin. Posting data from a file named 'foobar' would thus be done with --data @foobar. When --data is told to read from a file like that, carriage returns, newlines and null bytes are stripped out. If you do not want the @ character to have a special interpretation use --data-raw instead.

The data for this option is passed on to the server exactly as provided on the command line. curl does not convert, change or improve it. It is up to the user to provide the data in the correct form.

--data can be used several times in a command line.

Examples:

```
curl -d "name=curl" https://example.com
curl -d "name=curl" -d "tool=cmdline" https://example.com
curl -d @filename https://example.com
```

This option is mutually exclusive with --form, --head and --upload-file. See also --data-binary, --data-urlencode and --data-raw.

--data-ascii <data>

(HTTP) This option is an alias for --data.

--data-ascii can be used several times in a command line.

Example:

```
curl --data-ascii @file https://example.com
```

See also --data-binary, --data-raw and --data-urlencode.

--data-binary <data>

(HTTP) Post data exactly as specified with no extra processing whatsoever.

If you start the data with the letter @, the rest should be a filename. "@-" makes curl read the data from stdin. Data is posted in a similar manner as --data does, except that newlines and carriage returns are preserved and conversions are never done.

Like --data the default content-type sent to the server is application/x-www-form-urlencoded. If you want the data to be treated as arbitrary binary data by the server then set the content-type to octet-stream: -H "Content-Type: application/octet-stream".

If this option is used several times, the ones following the first append data as described in --data.

--data-binary can be used several times in a command line.

Example:

```
curl --data-binary @filename https://example.com
```

See also --data-ascii.

--data-raw <data>

(HTTP) Post data similarly to --data but without the special interpretation of the @ character.

--data-raw can be used several times in a command line.

Examples:

```
curl --data-raw "hello" https://example.com
curl --data-raw "@at@at@" https://example.com
```

See also --data.

--data-urlencode <data>

(HTTP) Post data, similar to the other --data options with the exception that this performs URL-encoding.

To be CGI-compliant, the <data> part should begin with a name followed by a separator and a content specification. The <data> part can be passed to curl using one of the following syntaxes:

content

URL-encode the content and pass that on. Be careful so that the content does not contain any "=" or "@" symbols, as that makes the syntax match one of the other cases below.

=content

URL-encode the content and pass that on. The preceding "=" symbol is not included in the data.

name=content

URL-encode the content part and pass that on. Note that the name part is expected to be URL-encoded already.

@filename

load data from the given file (including any newlines), URL-encode that data and pass it on in the POST. Using "@-" makes curl read the data from stdin.

name@filename

load data from the given file (including any newlines), URL-encode that data and pass it on in the POST. The name part gets an equal sign appended, resulting in name=urlencoded-file-content. Note that the name is expected to be URL-encoded already.

--data-urlencode can be used several times in a command line.

Examples:

```
curl --data-urlencode name=val https://example.com
curl --data-urlencode =encodethis https://example.com
curl --data-urlencode name@file https://example.com
curl --data-urlencode @fileonly https://example.com
```

See also --data and --data-raw.

--delegation <LEVEL>

(GSS/kerberos) Set LEVEL what curl is allowed to delegate when it comes to user credentials.

none

Do not allow any delegation.

policy

Delegates if and only if the OK-AS-DELEGATE flag is set in the Kerberos service ticket, which is a matter of realm policy.

always

Unconditionally allow the server to delegate.

If --delegation is provided several times, the last set value is used.

Example:

```
curl --delegation "none" https://example.com
```

See also --insecure and --ssl.

--digest

(HTTP) Enable HTTP Digest authentication. This authentication scheme avoids sending the password over the wire in clear text. Use this in combination with the normal --user option to set username and password.

Providing --digest multiple times has no extra effect. Disable it again with --no-digest.

Example:

```
curl -u name:password --digest https://example.com
```

See also --user, --proxy-digest and --anyauth.

-q, --disable

If used as the first parameter on the command line, the curlrc config file is not read or used. See the --config for details on the default config file search path.

Providing --disable multiple times has no extra effect. Disable it again with --no-disable.

Example:

```
curl -q https://example.com
```

See also --config.

--disable-eprt

(FTP) Disable the use of the EPRT and LPRT commands when doing active FTP transfers. curl normally first attempts to use EPRT before using PORT, but with this option, it uses PORT right away. EPRT is an extension to the original FTP protocol, and does not work on all servers, but enables more functionality in a better way than the traditional PORT command.

--eprt can be used to explicitly enable EPRT again and --no-eprt is an alias for --disable-eprt.

If the server is accessed using IPv6, this option has no effect as EPRT is necessary then.

Disabling EPRT only changes the active behavior. If you want to switch to passive mode you need to not use --ftp-port or force it with --ftp-pasv.

Providing --disable-eprt multiple times has no extra effect. Disable it again with --no-disable-eprt.

Example:

```
curl --disable-eprt ftp://example.com/
```

See also --disable-epsv and --ftp-port.

--disable-epsv

(FTP) Disable the use of the EPSV command when doing passive FTP transfers. curl normally first attempts to use EPSV before PASV, but with this option, it does not try EPSV.

--epsv can be used to explicitly enable EPSV again and --no-epsv is an alias for --disable-epsv.

If the server is an IPv6 host, this option has no effect as EPSV is necessary then.

Disabling EPSV only changes the passive behavior. If you want to switch to active mode you need to use --ftp-port.

Providing --disable-epsv multiple times has no extra effect. Disable it again with --no-disable-epsv.

Example:

```
curl --disable-epsv ftp://example.com/
```

See also --disable-eprt and --ftp-port.

--disallow-username-in-url

Exit with error if passed a URL containing a username. Probably most useful when the URL is being provided at runtime or similar.

Accepting and using credentials in a URL is normally considered a security hazard as they are easily leaked that way.

Providing --disallow-username-in-url multiple times has no extra effect. Disable it again with --no-disallow-username-in-url.

Example:

```
curl --disallow-username-in-url https://example.com
```

See also --proto.

--dns-interface <interface>

(DNS) Send outgoing DNS requests through the given interface. This option is a counterpart to --interface (which does not affect DNS). The supplied string must be an interface name (not an address).

If --dns-interface is provided several times, the last set value is used.

Example:

```
curl --dns-interface eth0 https://example.com
```

For --dns-interface to work, it requires that the underlying libcurl is built to support c-ares. See also --dns-ipv4-addr and --dns-ipv6-addr.

--dns-ipv4-addr <address>

(DNS) Bind to a specific IP address when making IPv4 DNS requests, so that the DNS requests originate from this address. The argument should be a single IPv4 address.

If --dns-ipv4-addr is provided several times, the last set value is used.

Example:

```
curl --dns-ipv4-addr 10.1.2.3 https://example.com
```

For --dns-ipv4-addr to work, it requires that the underlying libcurl is built to support c-ares. See also --dns-interface and --dns-ipv6-addr.

--dns-ipv6-addr <address>

(DNS) Bind to a specific IP address when making IPv6 DNS requests, so that the DNS requests originate from this address. The argument should be a single IPv6 address.

If --dns-ipv6-addr is provided several times, the last set value is used.

Example:

```
curl --dns-ipv6-addr 2a04:4e42::561 https://example.com
```

For --dns-ipv6-addr to work, it requires that the underlying libcurl is built to support c-ares. See also --dns-interface and --dns-ipv4-addr.

--dns-servers <addresses>

(DNS) Set the list of DNS servers to be used instead of the system default. The list of IP addresses should be separated with commas. Port numbers may also optionally be given, appended to the IP address separated with a colon.

If --dns-servers is provided several times, the last set value is used.

Examples:

```
curl --dns-servers 192.168.0.1,192.168.0.2 https://example.com
curl --dns-servers 10.0.0.1:53 https://example.com
```

For --dns-servers to work, it requires that the underlying libcurl is built to support c-ares. See also --dns-interface and --dns-ipv4-addr.

--doh-cert-status

(DNS) Same as --cert-status but used for DoH (DNS-over-HTTPS).

Verify the status of the DoH servers' certificate by using the Certificate Status Request (aka. OCSP stapling) TLS extension.

If this option is enabled and the DoH server sends an invalid (e.g. expired) response, if the response suggests that the server certificate has been revoked, or no response at all is received, the verification fails.

This support is currently only implemented in the OpenSSL and GnuTLS backends.

Providing --doh-cert-status multiple times has no extra effect. Disable it again with --no-doh-cert-status.

Example:

```
curl --doh-cert-status --doh-url https://doh.example https://example.com
```

Added in 7.76.0. See also --doh-insecure.

--doh-insecure

(DNS) By default, every connection curl makes to a DoH server is verified to be secure before the transfer takes place. This option tells curl to skip the verification step and proceed without checking.

WARNING: using this option makes the DoH transfer and name resolution insecure.

This option is equivalent to --insecure and --proxy-insecure but used for DoH (DNS-over-HTTPS) only.

Providing --doh-insecure multiple times has no extra effect. Disable it again with --no-doh-insecure.

Example:

```
curl --doh-insecure --doh-url https://doh.example https://example.com
```

Added in 7.76.0. See also --doh-url, --insecure and --proxy-insecure.

--doh-url <URL>

(DNS) Specify which DNS-over-HTTPS (DoH) server to use to resolve hostnames, instead of using the default name resolver mechanism. The URL must be HTTPS.

Some SSL options that you set for your transfer also apply to DoH since the name lookups take place over SSL. The certificate verification settings are not inherited but are controlled separately via --doh-insecure and --doh-cert-status.

By default, DoH is bypassed when initially looking up DNS records of the DoH server. You can specify the IP address(es) of the DoH server with --resolve to avoid this.

This option is unset if an empty string "" is used as the URL. (Added in 7.85.0)

If --doh-url is provided several times, the last set value is used.

Examples:

```
curl --doh-url https://doh.example https://example.com
curl --doh-url https://doh.example --resolve doh.example:443:192.0.2.1 https://example.com
```

See also --doh-insecure.

--dump-ca-embed

(TLS) Write the CA bundle embedded in curl to standard output, then quit.

If curl was not built with a default CA bundle embedded, the output is empty.

Providing --dump-ca-embed multiple times has no extra effect. Disable it again with --no-dump-ca-embed.

Example:

```
curl --dump-ca-embed
```

Added in 8.10.0. See also --ca-native, --cacert, --capath, --proxy-ca-native, --proxy-cacert and --proxy-capath.

-D, --dump-header <filename>

(HTTP FTP) Write the received protocol headers to the specified file. If no headers are received, the use of this option creates an empty file. Specify "-" as filename (a single minus) to have it written to stdout.

Starting in curl 8.10.0, specify "%" (a single percent sign) as filename writes the output to stderr.

When used in FTP, the FTP server response lines are considered being "headers" and thus are saved there.

Starting in curl 8.11.0, using the --create-dirs option can also create missing directory components for the path provided in --dump-header.

Having multiple transfers in one set of operations (i.e. the URLs in one --next clause), appends them to the same file, separated by a blank line.

If --dump-header is provided several times, the last set value is used.

Examples:

```
curl --dump-header store.txt https://example.com
curl --dump-header - https://example.com -o save
```

See also --output.

--ech <config>

(HTTPS) Specify how to do ECH (Encrypted Client Hello).

The values allowed for <config> can be:

false

Do not attempt ECH. The is the default.

grease

Send a GREASE ECH extension

true

Attempt ECH if possible, but do not fail if ECH is not attempted. (The connection fails if ECH is attempted but fails.)

hard

Attempt ECH and fail if that is not possible. ECH only works with TLS 1.3 and also requires using DoH or providing an ECHConfigList on the command line.

ecl:<b64val>

A base64 encoded ECHConfigList that is used for ECH.

pn:<name>

A name to use to over-ride the "public_name" field of an ECHConfigList (only available with OpenSSL TLS support)

Most ECH related errors cause error CURLE_ECH_REQUIRED (101).

If --ech is provided several times, the last set value is used.

Example:

```
curl --ech true https://example.com
```

Added in 8.8.0. See also --doh-url.

--egd-file <file>

(TLS) Deprecated option (added in 7.84.0). Prior to that it only had an effect on curl if built to use old versions of OpenSSL.

Specify the path name to the Entropy Gathering Daemon socket. The socket is used to seed the random engine for SSL connections.

If --egd-file is provided several times, the last set value is used.

Example:

```
curl --egd-file /random/here https://example.com
```

See also --random-file.

--engine <name>

(TLS) Select the OpenSSL crypto engine to use for cipher operations. Use "--engine list" to print a list of build-time supported engines. Note that not all (and possibly none) of the engines may be available at runtime.

The OpenSSL concept "engines" has been superseded by "providers" in OpenSSL 3, and this option should work fine to specify such as well.

If --engine is provided several times, the last set value is used.

Example:

```
curl --engine flavor https://example.com
```

See also --ciphers and --curves.

--etag-compare <file>

(HTTP) Make a conditional HTTP request for the specific ETag read from the given file by sending a custom If-None-Match header using the stored ETag.

For correct results, make sure that the specified file contains only a single line with the desired ETag. A non-existing or empty file is treated as an empty ETag.

Use the option --etag-save to first save the ETag from a response, and then use this option to compare against the saved ETag in a subsequent request.

Use this option with a single URL only.

If --etag-compare is provided several times, the last set value is used.

Example:

```
curl --etag-compare etag.txt https://example.com
```

Added in 7.68.0. See also --etag-save and --time-cond.

--etag-save <file>

(HTTP) Save an HTTP ETag to the specified file. An ETag is a caching related header, usually returned in a response. Use this option with a single URL only.

If no ETag is sent by the server, an empty file is created.

In many situations you want to use an existing etag in the request to avoid downloading the same resource again but also save the new etag if it has indeed changed, by using both etag options --etag-save and --etag-compare with the same filename, in the same command line.

Starting in curl 8.12.0, using the --create-dirs option can also create missing directory components for the path provided in --etag-save.

If --etag-save is provided several times, the last set value is used.

Example:

```
curl --etag-save storetag.txt https://example.com
```

Added in 7.68.0. See also --etag-compare.

--expect100-timeout <seconds>

(HTTP) Maximum time in seconds that you allow curl to wait for a 100-continue response when curl emits an Expects: 100-continue header in its request. By default curl waits one second. This option accepts decimal values. When curl stops waiting, it continues as if a response was received.

The decimal value needs to be provided using a dot (".") as decimal separator - not the local version even if it might be using another separator.

If --expect100-timeout is provided several times, the last set value is used.

Example:

```
curl --expect100-timeout 2.5 -T file https://example.com
```

See also --connect-timeout.

-f, --fail

(HTTP) Fail with error code 22 and with no response body output at all for HTTP transfers returning HTTP response codes at 400 or greater.

In normal cases when an HTTP server fails to deliver a document, it returns a body of text stating so (which often also describes why and more) and a 4xx HTTP response code. This command line option prevents curl from outputting that data and instead returns error 22 early. By default, curl does not consider HTTP response codes to indicate failure.

To get both the error code and also save the content, use --fail-with-body instead.

This method is not fail-safe and there are occasions where non-successful response codes slip through, especially when authentication is involved (response codes 401 and 407).

Providing --fail multiple times has no extra effect. Disable it again with --no-fail.

Example:

```
curl --fail https://example.com
```

This option is mutually exclusive with --fail-with-body. See also --fail-with-body and --fail-early.

--fail-early

Fail and exit on the first detected transfer error.

When curl is used to do multiple transfers on the command line, it attempts to operate on each given URL, one by one. By default, it ignores errors if there are more URLs given and the last URL's success determines the error code curl returns. Early failures are "hidden" by subsequent successful transfers.

Using this option, curl instead returns an error on the first transfer that fails, independent of the amount of URLs that are given on the command line. This way, no transfer failures go undetected by scripts and similar.

This option does not imply --fail, which causes transfers to fail due to the server's HTTP status code. You can combine the two options, however note --fail is not global and is therefore contained by --next.

This option is global and does not need to be specified for each use of --next.

Providing --fail-early multiple times has no extra effect. Disable it again with --no-fail-early.

Example:

```
curl --fail-early https://example.com https://two.example
```

See also --fail and --fail-with-body.

--fail-with-body

(HTTP) Return an error on server errors where the HTTP response code is 400 or greater). In normal cases when an HTTP server fails to deliver a document, it returns an HTML document stating so (which often also describes why and more). This option allows curl to output and save that content but also to return error 22.

This is an alternative option to --fail which makes curl fail for the same circumstances but without saving the content.

Providing --fail-with-body multiple times has no extra effect. Disable it again with --no-fail-with-body.

Example:

```
curl --fail-with-body https://example.com
```

This option is mutually exclusive with --fail. Added in 7.76.0. See also --fail and --fail-early.

--false-start

(TLS) No TLS backend currently supports this feature.

Use false start during the TLS handshake. False start is a mode where a TLS client starts sending application data before verifying the server's Finished message, thus saving a round trip when performing a full handshake.

Providing --false-start multiple times has no extra effect. Disable it again with --no-false-start.

Example:

```
curl --false-start https://example.com
```

See also --tcp-fastopen.

--follow

(HTTP) Instructs curl to follow HTTP redirects and to do the custom request method set with --request when following redirects as the HTTP specification says.

The method string set with --request is used in subsequent requests for the status codes 307 or 308, but may be reset to GET for 301, 302 and 303.

This is subtly different than --location, as that option always sets the custom method in all subsequent requests independent of response code.

Restrict which protocols a redirect is accepted to follow with --proto-redir.

When --netrc is used in combination with this option, credentials for the followed-to hosts may also be selected from that file.

Providing --follow multiple times has no extra effect. Disable it again with --no-follow.

Example:

```
curl -X POST --follow https://example.com
```

Added in 8.16.0. See also --request, --location, --proto-redir and --max-redirs.

-F, --form <name=content>

(HTTP SMTP IMAP) For the HTTP protocol family, emulate a filled-in form in which a user has pressed the submit button. This makes curl POST data using the Content-Type multipart/form-data according to RFC 2388.

For SMTP and IMAP protocols, this composes a multipart mail message to transmit.

This enables uploading of binary files etc. To force the 'content' part to be a file, prefix the filename with an @ sign. To get the content part from a file, prefix the filename with the symbol <. The difference between @ and < is then that @ makes a file get attached in the post as a file upload, while the < makes a text field and gets the contents for that text field from a file.

Read content from stdin instead of a file by using a single "-" as filename. This goes for both @ and < constructs. When stdin is used, the contents is buffered in memory first by curl to determine its size and allow a possible resend. Defining a part's data from a named non-regular file (such as a named pipe or similar) is not subject to buffering and is instead read at transmission time; since the full size is unknown before the transfer starts, such data is sent as chunks by HTTP and rejected by IMAP.

Example: send an image to an HTTP server, where 'profile' is the name of the form-field to which the file portrait.jpg is the input:

```
curl -F profile=@portrait.jpg https://example.com/upload.cgi
```

Example: send your name and shoe size in two text fields to the server:

```
curl -F name=John -F shoesize=11 https://example.com/
```

Example: send your essay in a text field to the server. Send it as a plain text field, but get the contents for it from a local file:

```
curl -F "story=<hugefile.txt" https://example.com/
```

You can also instruct curl what Content-Type to use by using "type=", in a manner similar to:

```
curl -F "web=@index.html;type=text/html" example.com
```

or

```
curl -F "name=daniel;type=text/foo" example.com
```

You can also explicitly change the name field of a file upload part by setting filename=, like this:

```
curl -F "file=@localfile;filename=nameinpost" example.com
```

If filename/path contains ',' or ';', it must be quoted by double-quotes like:

```
curl -F "file=@\"local,file\";filename=\"name;in;post\"" \
    https://example.com
```

or

```
curl -F 'file=@"local,file";filename="name;in;post"' \
    https://example.com
```

Note that if a filename/path is quoted by double-quotes, any double-quote or backslash within the filename must be escaped by backslash.

Quoting must also be applied to non-file data if it contains semicolons, leading/trailing spaces or leading double quotes:

```
curl -F 'colors="red; green; blue";type=text/x-myapp' \
   https://example.com
```

You can add custom headers to the field by setting headers=, like

```
curl -F "submit=OK;headers=\"X-submit-type: OK\"" example.com
```

or

```
curl -F "submit=OK;headers=@headerfile" example.com
```

The headers= keyword may appear more than once and above notes about quoting apply. When headers are read from a file, empty lines and lines starting with '#' are ignored; each header can be folded by splitting between two words and starting the continuation line with a space; embedded carriage-returns and trailing spaces are stripped. Here is an example of a header file contents:

```
# This file contains two headers.
X-header-1: this is a header
 
# The following header is folded.
X-header-2: this is
 another header
```

To support sending multipart mail messages, the syntax is extended as follows:

- name can be omitted: the equal sign is the first character of the argument,

- if data starts with '(', this signals to start a new multipart: it can be followed by a content type specification.

- a multipart can be terminated with a '=)' argument.

Example: the following command sends an SMTP mime email consisting in an inline part in two alternative formats: plain text and HTML. It attaches a text file:

```
curl -F '=(;type=multipart/alternative' \
     -F '=plain text message' \
     -F '= <body>HTML message</body>;type=text/html' \
     -F '=)' -F '=@textfile.txt' ... smtp://example.com
```

Data can be encoded for transfer using encoder=. Available encodings are binary and 8bit that do nothing else than adding the corresponding Content-Transfer-Encoding header, 7bit that only rejects 8-bit characters with a transfer error, quoted-printable and base64 that encodes data according to the corresponding schemes, limiting lines length to 76 characters.

Example: send multipart mail with a quoted-printable text message and a base64 attached file:

```
curl -F '=text message;encoder=quoted-printable' \
     -F '=@localfile;encoder=base64' ... smtp://example.com
```

--form can be used several times in a command line.

Example:

```
curl --form "name=curl" --form "file=@loadthis" https://example.com
```

This option is mutually exclusive with --data, --head and --upload-file. See also --data, --form-string and --form-escape.

--form-escape

(HTTP IMAP SMTP) Pass on names of multipart form fields and files using backslash-escaping instead of percent-encoding.

If --form-escape is provided several times, the last set value is used.

Example:

```
curl --form-escape -F 'field\name=curl' -F 'file=@load"this' https://example.com
```

Added in 7.81.0. See also --form.

--form-string <name=string>

(HTTP SMTP IMAP) Similar to --form except that the value string for the named parameter is used literally. Leading @ and < characters, and the ";type=" string in the value have no special meaning. Use this in preference to --form if there is any possibility that the string value may accidentally trigger the @ or < features of --form.

--form-string can be used several times in a command line.

Example:

```
curl --form-string "name=data" https://example.com
```

See also --form.

--ftp-account <data>

(FTP) When an FTP server asks for "account data" after username and password has been provided, this data is sent off using the ACCT command.

If --ftp-account is provided several times, the last set value is used.

Example:

```
curl --ftp-account "mr.robot" ftp://example.com/
```

See also --user.

--ftp-alternative-to-user <command>

(FTP) If authenticating with the USER and PASS commands fails, send this command. When connecting to Tumbleweed's Secure Transport server over FTPS using a client certificate, using "SITE AUTH" tells the server to retrieve the username from the certificate.

If --ftp-alternative-to-user is provided several times, the last set value is used.

Example:

```
curl --ftp-alternative-to-user "U53r" ftp://example.com
```

See also --ftp-account and --user.

--ftp-create-dirs

(FTP SFTP) When an FTP or SFTP URL/operation uses a path that does not currently exist on the server, the standard behavior of curl is to fail. Using this option, curl instead attempts to create missing directories.

Providing --ftp-create-dirs multiple times has no extra effect. Disable it again with --no-ftp-create-dirs.

Example:

```
curl --ftp-create-dirs -T file ftp://example.com/remote/path/file
```

See also --create-dirs.

--ftp-method <method>

(FTP) Control what method curl should use to reach a file on an FTP(S) server. The method argument should be one of the following alternatives:

multicwd

Do a single CWD operation for each path part in the given URL. For deep hierarchies this means many commands. This is how RFC 1738 says it should be done. This is the default but the slowest behavior.

nocwd

Do no CWD at all. curl does SIZE, RETR, STOR etc and gives the full path to the server for each of these commands. This is the fastest behavior.

singlecwd

Do one CWD with the full target directory and then operate on the file "normally" (like in the multicwd case). This is somewhat more standards compliant than "nocwd" but without the full penalty of "multicwd".

If --ftp-method is provided several times, the last set value is used.

Examples:

```
curl --ftp-method multicwd ftp://example.com/dir1/dir2/file
curl --ftp-method nocwd ftp://example.com/dir1/dir2/file
curl --ftp-method singlecwd ftp://example.com/dir1/dir2/file
```

See also --list-only.

--ftp-pasv

(FTP) Use passive mode for the data connection. Passive is the internal default behavior, but using this option can be used to override a previous --ftp-port option.

Reversing an enforced passive really is not doable but you must then instead enforce the correct --ftp-port again.

Passive mode means that curl tries the EPSV command first and then PASV, unless --disable-epsv is used.

Providing --ftp-pasv multiple times has no extra effect.

Example:

```
curl --ftp-pasv ftp://example.com/
```

This option is mutually exclusive with --ftp-port. See also --disable-epsv.

-P, --ftp-port <address>

(FTP) Reverse the default initiator/listener roles when connecting with FTP. This option makes curl use active mode. curl then commands the server to connect back to the client's specified address and port, while passive mode asks the server to setup an IP address and port for it to connect to. <address> should be one of:

interface

e.g. eth0 to specify which interface's IP address you want to use (Unix only)

IP address

e.g. 192.168.10.1 to specify the exact IP address

hostname

e.g. my.host.domain to specify the machine

-

make curl pick the same IP address that is already used for the control connection. This is the recommended choice.

Disable the use of PORT with --ftp-pasv. Disable the attempt to use the EPRT command instead of PORT by using --disable-eprt. EPRT is really PORT++.

You can also append ":[start]-[end]" to the right of the address, to tell curl what TCP port range to use. That means you specify a port range, from a lower to a higher number. A single number works as well, but do note that it increases the risk of failure since the port may not be available.

If --ftp-port is provided several times, the last set value is used.

Examples:

```
curl -P - ftp:/example.com
curl -P eth0 ftp:/example.com
curl -P 192.168.0.2 ftp:/example.com
```

See also --ftp-pasv and --disable-eprt.

--ftp-pret

(FTP) Send a PRET command before PASV (and EPSV). Certain FTP servers, mainly drftpd, require this non-standard command for directory listings as well as up and downloads in PASV mode.

Providing --ftp-pret multiple times has no extra effect. Disable it again with --no-ftp-pret.

Example:

```
curl --ftp-pret ftp://example.com/
```

See also --ftp-port and --ftp-pasv.

--ftp-skip-pasv-ip

(FTP) Do not use the IP address the server suggests in its response to curl's PASV command when curl connects the data connection. Instead curl reuses the same IP address it already uses for the control connection.

This option is enabled by default (added in 7.74.0).

This option has no effect if PORT, EPRT or EPSV is used instead of PASV.

Providing --ftp-skip-pasv-ip multiple times has no extra effect. Disable it again with --no-ftp-skip-pasv-ip.

Example:

```
curl --ftp-skip-pasv-ip ftp://example.com/
```

See also --ftp-pasv.

--ftp-ssl-ccc

(FTP) Use CCC (Clear Command Channel) Shuts down the SSL/TLS layer after authenticating. The rest of the control channel communication is unencrypted. This allows NAT routers to follow the FTP transaction. The default mode is passive.

Providing --ftp-ssl-ccc multiple times has no extra effect. Disable it again with --no-ftp-ssl-ccc.

Example:

```
curl --ftp-ssl-ccc ftps://example.com/
```

See also --ssl and --ftp-ssl-ccc-mode.

--ftp-ssl-ccc-mode <active/passive>

(FTP) Set the CCC mode. The passive mode does not initiate the shutdown, but instead waits for the server to do it, and does not reply to the shutdown from the server. The active mode initiates the shutdown and waits for a reply from the server.

Providing --ftp-ssl-ccc-mode multiple times has no extra effect. Disable it again with --no-ftp-ssl-ccc-mode.

Example:

```
curl --ftp-ssl-ccc-mode active --ftp-ssl-ccc ftps://example.com/
```

See also --ftp-ssl-ccc.

--ftp-ssl-control

(FTP) Require SSL/TLS for the FTP login, clear for transfer. Allows secure authentication, but non-encrypted data transfers for efficiency. Fails the transfer if the server does not support SSL/TLS.

If set, this option overrides --ssl.

Providing --ftp-ssl-control multiple times has no extra effect. Disable it again with --no-ftp-ssl-control.

Example:

```
curl --ftp-ssl-control ftp://example.com
```

See also --ssl.

-G, --get

(HTTP) When used, this option makes all data specified with --data, --data-binary or --data-urlencode to be used in an HTTP GET request instead of the POST request that otherwise would be used. curl appends the provided data to the URL as a query string.

If used in combination with --head, the POST data is instead appended to the URL with a HEAD request.

Providing --get multiple times has no extra effect. Disable it again with --no-get.

Examples:

```
curl --get https://example.com
curl --get -d "tool=curl" -d "age=old" https://example.com
curl --get -I -d "tool=curl" https://example.com
```

See also --data and --request.

-g, --globoff

Switch off the URL globbing function. When you set this option, you can specify URLs that contain the letters {}[] without having curl itself interpret them. Note that these letters are not normal legal URL contents but they should be encoded according to the URI standard.

curl detects numerical IPv6 addresses when used in URLs and excludes them from the treatment, so they can still be used without having to disable globbing.

Providing --globoff multiple times has no extra effect. Disable it again with --no-globoff.

Example:

```
curl -g "https://example.com/{[]}}}}"
```

See also --config and --disable.

--happy-eyeballs-timeout-ms <ms>

Set the timeout for Happy Eyeballs.

Happy Eyeballs is an algorithm that attempts to connect to both IPv4 and IPv6 addresses for dual-stack hosts, giving IPv6 a head-start of the specified number of milliseconds. If the IPv6 address cannot be connected to within that time, then a connection attempt is made to the IPv4 address in parallel. The first connection to be established is the one that is used.

The range of suggested useful values is limited. Happy Eyeballs RFC 6555 says "It is RECOMMENDED that connection attempts be paced 150-250 ms apart to balance human factors against network load." libcurl currently defaults to 200 ms. Firefox and Chrome currently default to 300 ms.

If --happy-eyeballs-timeout-ms is provided several times, the last set value is used.

Example:

```
curl --happy-eyeballs-timeout-ms 500 https://example.com
```

See also --max-time and --connect-timeout.

--haproxy-clientip <ip>

(HTTP) Set a client IP in HAProxy PROXY protocol v1 header at the beginning of the connection.

For valid requests, IPv4 addresses must be indicated as a series of exactly 4 integers in the range [0..255] inclusive written in decimal representation separated by exactly one dot between each other. Heading zeroes are not permitted in front of numbers in order to avoid any possible confusion with octal numbers. IPv6 addresses must be indicated as series of 4 hexadecimal digits (upper or lower case) delimited by colons between each other, with the acceptance of one double colon sequence to replace the largest acceptable range of consecutive zeroes. The total number of decoded bits must be exactly 128.

Otherwise, any string can be accepted for the client IP and get sent.

It replaces --haproxy-protocol if used, it is not necessary to specify both flags.

If --haproxy-clientip is provided several times, the last set value is used.

Example:

```
curl --haproxy-clientip $IP
```

Added in 8.2.0. See also --proxy.

--haproxy-protocol

(HTTP) Send a HAProxy PROXY protocol v1 header at the beginning of the connection. This is used by some load balancers and reverse proxies to indicate the client's true IP address and port.

This option is primarily useful when sending test requests to a service that expects this header.

Providing --haproxy-protocol multiple times has no extra effect. Disable it again with --no-haproxy-protocol.

Example:

```
curl --haproxy-protocol https://example.com
```

See also --proxy.

-I, --head

(HTTP FTP FILE) Fetch the headers only. HTTP-servers feature the command HEAD which this uses to get nothing but the header of a document. When used on an FTP or FILE URL, curl displays the file size and last modification time only.

Providing --head multiple times has no extra effect. Disable it again with --no-head.

Example:

```
curl -I https://example.com
```

See also --get, --verbose and --trace-ascii.

-H, --header <header/@file>

(HTTP IMAP SMTP) Extra header to include in information sent. When used within an HTTP request, it is added to the regular request headers.

For an IMAP or SMTP MIME uploaded mail built with --form options, it is prepended to the resulting MIME document, effectively including it at the mail global level. It does not affect raw uploaded mails.

You may specify any number of extra headers. Note that if you should add a custom header that has the same name as one of the internal ones curl would use, your externally set header is used instead of the internal one. This allows you to make even trickier stuff than curl would normally do. You should not replace internally set headers without knowing perfectly well what you are doing. Remove an internal header by giving a replacement without content on the right side of the colon, as in: -H "Host:". If you send the custom header with no-value then its header must be terminated with a semicolon, such as -H "X-Custom-Header;" to send "X-Custom-Header:".

curl makes sure that each header you add/replace is sent with the proper end-of-line marker, you should thus not add that as a part of the header content: do not add newlines or carriage returns, they only mess things up for you. curl passes on the verbatim string you give it without any filter or other safe guards. That includes white space and control characters.

This option can take an argument in @filename style, which then adds a header for each line in the input file. Using @- makes curl read the header file from stdin.

Please note that most anti-spam utilities check the presence and value of several MIME mail headers: these are "From:", "To:", "Date:" and "Subject:" among others and should be added with this option.

You need --proxy-header to send custom headers intended for an HTTP proxy.

Passing on a "Transfer-Encoding: chunked" header when doing an HTTP request with a request body, makes curl send the data using chunked encoding.

WARNING: headers set with this option are set in all HTTP requests - even after redirects are followed, like when told with --location. This can lead to the header being sent to other hosts than the original host, so sensitive headers should be used with caution combined with following redirects.

"Authorization:" and "Cookie:" headers are explicitly not passed on in HTTP requests when following redirects to other origins, unless --location-trusted is used.

--header can be used several times in a command line.

Examples:

```
curl -H "X-First-Name: Joe" https://example.com
curl -H "User-Agent: yes-please/2000" https://example.com
curl -H "Host:" https://example.com
curl -H @headers.txt https://example.com
```

See also --user-agent, --referer and --proxy-header.

-h, --help <subject>

Usage help. Provide help for the subject given as an optional argument.

If no argument is provided, curl displays the most important command line arguments.

The argument can either be a category or a command line option. When a category is provided, curl shows all command line options within the given category. Specify category "all" to list all available options.

If "category" is specified, curl displays all available help categories.

If the provided subject is instead an existing command line option, specified either in its short form with a single dash and a single letter, or in the long form with two dashes and a longer name, curl displays a help text for that option in the terminal.

The help output is extensive for some options.

If the provided command line option is not known, curl says so.

Examples:

```
curl --help all
curl --help --insecure
curl --help -f
```

See also --verbose.

--hostpubmd5 <md5>

(SFTP SCP) Pass a string containing 32 hexadecimal digits. The string should be the 128 bit MD5 checksum of the remote host's public key, curl refuses the connection with the host unless the checksums match.

If --hostpubmd5 is provided several times, the last set value is used.

Example:

```
curl --hostpubmd5 e5c1c49020640a5ab0f2034854c321a8 sftp://example.com/
```

See also --hostpubsha256.

--hostpubsha256 <sha256>

(SFTP SCP) Pass a string containing a Base64-encoded SHA256 hash of the remote host's public key. curl refuses the connection with the host unless the hashes match.

If --hostpubsha256 is provided several times, the last set value is used.

Example:

```
curl --hostpubsha256 NDVkMTQxMGQ1ODdmMjQ3MjczYjAyOTY5MmRkMjVmNDQ= sftp://example.com/
```

Added in 7.80.0. See also --hostpubmd5.

--hsts <filename>

(HTTPS) Enable HSTS for the transfer. If the filename points to an existing HSTS cache file, that is used. After a completed transfer, the cache is saved to the filename again if it has been modified. If you run multiple curl invokes at the same time using the same HSTS cache file, they might interfere with each other in possibly undesired ways.

If curl is told to use "http://" for a transfer involving a hostname that exists in the HSTS cache, it upgrades the transfer to use HTTPS. Each HSTS cache entry has an individual lifetime after which the upgrade is no longer performed.

Specify a "" filename (zero length) to avoid loading/saving and make curl handle HSTS in memory.

You may want to restrict your umask to prevent other users on the same system to access the created file.

If this option is used several times, curl loads contents from all the files but the last one is used for saving.

Since curl 8.20.0, curl keeps no more than the most recently added 10,000 unique HSTS hostnames.

--hsts can be used several times in a command line.

Example:

```
curl --hsts cache.txt https://example.com
```

Added in 7.74.0. See also --proto.

--http0.9

(HTTP) Accept an HTTP version 0.9 response.

HTTP/0.9 is a response without headers and therefore you can also connect with this to non-HTTP servers and still get a response since curl transparently downgrades - if allowed.

HTTP/0.9 is disabled by default (added in 7.66.0)

Providing --http0.9 multiple times has no extra effect. Disable it again with --no-http0.9.

Example:

```
curl --http0.9 https://example.com
```

See also --http1.1, --http2 and --http3.

-0, --http1.0

(HTTP) Use HTTP version 1.0 instead of using its internally preferred HTTP version.

Providing --http1.0 multiple times has no extra effect.

Example:

```
curl --http1.0 https://example.com
```

This option is mutually exclusive with --http1.1, --http2, --http2-prior-knowledge and --http3. See also --http0.9 and --http1.1.

--http1.1

(HTTP) Use HTTP version 1.1. This is the default with "http://" URLs.

Providing --http1.1 multiple times has no extra effect.

Example:

```
curl --http1.1 https://example.com
```

This option is mutually exclusive with --http1.0, --http2, --http2-prior-knowledge and --http3. See also --http1.0 and --http0.9.

--http2

(HTTP) Use HTTP/2.

For HTTPS, this means curl negotiates HTTP/2 in the TLS handshake. curl does this by default.

For HTTP, this means curl attempts to upgrade the request to HTTP/2 using the Upgrade: request header.

When curl uses HTTP/2 over HTTPS, it does not itself insist on TLS 1.2 or higher even though that is required by the specification. A user can add this version requirement with --tlsv1.2.

Providing --http2 multiple times has no extra effect.

Example:

```
curl --http2 https://example.com
```

For --http2 to work, it requires that the underlying libcurl is built to support HTTP/2. This option is mutually exclusive with --http1.1, --http1.0, --http2-prior-knowledge and --http3. See also --http1.1, --http3, --no-alpn and --proxy-http2.

--http2-prior-knowledge

(HTTP) Issue a non-TLS HTTP request using HTTP/2 directly without HTTP/1.1 Upgrade. It requires prior knowledge that the server supports HTTP/2 straight away. HTTPS requests still do HTTP/2 the standard way with negotiated protocol versions in the TLS handshake.

Since 8.10.0 if this option is set for an HTTPS request then the application layer protocol version (ALPN) offered to the server is only HTTP/2. Prior to that both HTTP/1.1 and HTTP/2 were offered.

Providing --http2-prior-knowledge multiple times has no extra effect. Disable it again with --no-http2-prior-knowledge.

Example:

```
curl --http2-prior-knowledge https://example.com
```

For --http2-prior-knowledge to work, it requires that the underlying libcurl is built to support HTTP/2. This option is mutually exclusive with --http1.1, --http1.0, --http2 and --http3. See also --http2 and --http3.

--http3

(HTTP) Attempt HTTP/3 to the host in the URL, but fallback to earlier HTTP versions if the HTTP/3 connection establishment fails or is slow. HTTP/3 is only available for HTTPS and not for HTTP URLs.

This option allows a user to avoid using the Alt-Svc method of upgrading to HTTP/3 when you know or suspect that the target speaks HTTP/3 on the given host and port.

When asked to use HTTP/3, curl issues a separate attempt to use older HTTP versions with a slight delay, so if the HTTP/3 transfer fails or is slow, curl still tries to proceed with an older HTTP version. The fallback performs the regular negotiation between HTTP/1 and HTTP/2.

Use --http3-only for similar functionality without a fallback.

curl cannot do HTTP/3 over any proxy.

Providing --http3 multiple times has no extra effect.

Example:

```
curl --http3 https://example.com
```

For --http3 to work, it requires that the underlying libcurl is built to support HTTP/3. This option is mutually exclusive with --http1.1, --http1.0, --http2, --http2-prior-knowledge and --http3-only. Added in 7.66.0. See also --http1.1 and --http2.

--http3-only

(HTTP) Instruct curl to use HTTP/3 to the host in the URL, with no fallback to earlier HTTP versions. HTTP/3 can only be used for HTTPS and not for HTTP URLs. For HTTP, this option triggers an error.

This option allows a user to avoid using the Alt-Svc method of upgrading to HTTP/3 when you know that the target speaks HTTP/3 on the given host and port.

This option makes curl fail if a QUIC connection cannot be established, it does not attempt any other HTTP versions on its own. Use --http3 for similar functionality with a fallback.

Providing --http3-only multiple times has no extra effect.

Example:

```
curl --http3-only https://example.com
```

For --http3-only to work, it requires that the underlying libcurl is built to support HTTP/3. This option is mutually exclusive with --http1.1, --http1.0, --http2, --http2-prior-knowledge and --http3. Added in 7.88.0. See also --http1.1, --http2 and --http3.

--ignore-content-length

(FTP HTTP) For HTTP, ignore the Content-Length header. This is particularly useful for servers running Apache 1.x, which reports incorrect Content-Length for files larger than 2 gigabytes.

For FTP, this makes curl skip the SIZE command to figure out the size before downloading a file.

Providing --ignore-content-length multiple times has no extra effect. Disable it again with --no-ignore-content-length.

Example:

```
curl --ignore-content-length https://example.com
```

See also --ftp-skip-pasv-ip.

-k, --insecure

(TLS SFTP SCP) By default, every secure connection curl makes is verified to be secure before the transfer takes place. This option makes curl skip the verification step and proceed without checking.

When this option is not used for protocols using TLS, curl verifies the server's TLS certificate before it continues: that the certificate contains the right name which matches the hostname used in the URL and that the certificate has been signed by a CA certificate present in the cert store. See this online resource for further details: https://curl.se/docs/sslcerts.html

For SFTP and SCP, this option makes curl skip the known_hosts verification. known_hosts is a file normally stored in the user's home directory in the ".ssh" subdirectory, which contains hostnames and their public keys.

WARNING: using this option makes the transfer insecure.

When curl uses secure protocols it trusts responses and allows for example HSTS and Alt-Svc information to be stored and used subsequently. Using --insecure can make curl trust and use such information from malicious servers.

Providing --insecure multiple times has no extra effect. Disable it again with --no-insecure.

Example:

```
curl --insecure https://example.com
```

See also --proxy-insecure, --cacert and --capath.

--interface <name>

Perform the operation using a specified interface. You can enter interface name, IP address or hostname. If you prefer to be specific, you can use the following special syntax:

if!<name>

Interface name. If the provided name does not match an existing interface, curl returns with error 45.

host!<name>

IP address or hostname.

ifhost!<interface>!<host>

Interface name and IP address or hostname. This syntax requires libcurl 8.9.0 or later.

If the provided name does not match an existing interface, curl returns with error 45.

curl does not support using network interface names for this option on Windows.

That name resolve operation if a hostname is provided does not use DNS-over-HTTPS even if --doh-url is set.

On Linux this option can be used to specify a VRF (Virtual Routing and Forwarding) device, but the binary then needs to either have the CAP_NET_RAW capability set or to be run as root.

If --interface is provided several times, the last set value is used.

Examples:

```
curl --interface eth0 https://example.com
curl --interface "host!10.0.0.1" https://example.com
curl --interface "if!enp3s0" https://example.com
```

See also --dns-interface.

--ip-tos <string>

Set Type of Service (TOS) for IPv4 or Traffic Class for IPv6.

The values allowed for <string> can be a numeric value between 1 and 255 or one of the following:

CS0, CS1, CS2, CS3, CS4, CS5, CS6, CS7, AF11, AF12, AF13, AF21, AF22, AF23, AF31, AF32, AF33, AF41, AF42, AF43, EF, VOICE-ADMIT, ECT1, ECT0, CE, LE, LOWCOST, LOWDELAY, THROUGHPUT, RELIABILITY, MINCOST

If --ip-tos is provided several times, the last set value is used.

Example:

```
curl --ip-tos CS5 https://example.com
```

Added in 8.9.0. See also --tcp-nodelay and --vlan-priority.

--ipfs-gateway <URL>

(IPFS) Specify which gateway to use for IPFS and IPNS URLs. Not specifying this instead makes curl check if the IPFS_GATEWAY environment variable is set, or if a "~/.ipfs/gateway" file holding the gateway URL exists.

If you run a local IPFS node, this gateway is by default available under "http://localhost:8080". A full example URL would look like:

```
curl --ipfs-gateway http://localhost:8080 \
   ipfs://bafybeigagd5nmnn2iys2f3
```

There are many public IPFS gateways. See for example: https://ipfs.github.io/public-gateway-checker/

If you opt to go for a remote gateway you need to be aware that you completely trust the gateway. This might be fine in local gateways that you host yourself. With remote gateways there could potentially be malicious actors returning you data that does not match the request you made, inspect or even interfere with the request. You may not notice this when using curl. A mitigation could be to go for a "trustless" gateway. This means you locally verify the data. Consult the docs page on trusted vs trustless: https://docs.ipfs.tech/reference/http/gateway/#trusted-vs-trustless

If --ipfs-gateway is provided several times, the last set value is used.

Example:

```
curl --ipfs-gateway https://example.com ipfs://
```

Added in 8.4.0. See also --help and --manual.

-4, --ipv4

Request only IPv4 addresses when resolving hostnames, and not for example any IPv6.

Providing --ipv4 multiple times has no extra effect.

Example:

```
curl --ipv4 https://example.com
```

This option is mutually exclusive with --ipv6. See also --http1.1 and --http2.

-6, --ipv6

Request only IPv6 addresses when resolving hostnames, and not for example any IPv4.

Your resolver may still respond to an IPv6-only resolve request by returning IPv6 addresses that contain "mapped" IPv4 addresses for compatibility purposes. macOS is known to do this.

Providing --ipv6 multiple times has no extra effect.

Example:

```
curl --ipv6 https://example.com
```

This option is mutually exclusive with --ipv4. See also --http1.1 and --http2.

--json <data>

(HTTP) Send the specified JSON data in a POST request to the HTTP server. --json works as a shortcut for passing on these three options:

```
--data-binary [arg]
--header "Content-Type: application/json"
--header "Accept: application/json"
```

There is no verification that the passed in data is actual JSON or that the syntax is correct.

If you start the data with the letter @, the rest should be a filename to read the data from, or a single dash (-) if you want curl to read the data from stdin. Posting data from a file named 'foobar' would thus be done with --json @foobar and to instead read the data from stdin, use --json @-.

If this option is used more than once on the same command line, the additional data pieces are concatenated to the previous before sending.

The headers this option sets can be overridden with --header as usual.

--json can be used several times in a command line.

Examples:

```
curl --json '{ "drink": "coffee" }' https://example.com
curl --json '{ "drink":' --json ' "coffee" }' https://example.com
curl --json @prepared https://example.com
curl --json @- https://example.com < json.txt
```

This option is mutually exclusive with --form, --head and --upload-file. Added in 7.82.0. See also --data-binary and --data-raw.

-j, --junk-session-cookies

(HTTP) When curl is told to read cookies from a given file, this option makes it discard all session cookies. This has the same effect as if a new session is started. Typical browsers discard session cookies when they are closed down.

Session cookies are cookies without a set expiry time. They are meant to only last for "a session".

Providing --junk-session-cookies multiple times has no extra effect. Disable it again with --no-junk-session-cookies.

Example:

```
curl --junk-session-cookies -b cookies.txt https://example.com
```

See also --cookie and --cookie-jar.

--keepalive-cnt <integer>

Set the maximum number of keepalive probes TCP should send but get no response before dropping the connection. This option is usually used in conjunction with --keepalive-time.

This option is supported on Linux, *BSD/macOS, Windows >=10.0.16299, Solaris 11.4, and recent AIX, HP-UX and more. This option has no effect if --no-keepalive is used.

If unspecified, the option defaults to 9.

If --keepalive-cnt is provided several times, the last set value is used.

Example:

```
curl --keepalive-cnt 3 https://example.com
```

Added in 8.9.0. See also --keepalive-time and --no-keepalive.

--keepalive-time <seconds>

Set the time a connection needs to remain idle before sending keepalive probes and the time between individual keepalive probes. It is currently effective on operating systems offering the "TCP_KEEPIDLE" and "TCP_KEEPINTVL" socket options (meaning Linux, *BSD/macOS, Windows, Solaris, and recent AIX, HP-UX and more). Keepalive is used by the TCP stack to detect broken networks on idle connections. The number of missed keepalive probes before declaring the connection down is OS dependent and is commonly 8 (*BSD/macOS/AIX), 9 (Linux/AIX) or 5/10 (Windows), and this number can be changed by specifying the curl option "keepalive-cnt". Note that this option has no effect if --no-keepalive is used.

If unspecified, the option defaults to 60 seconds.

If --keepalive-time is provided several times, the last set value is used.

Example:

```
curl --keepalive-time 20 https://example.com
```

See also --no-keepalive, --keepalive-cnt and --max-time.

--key <key>

(TLS SCP SFTP) Private key filename. Allows you to provide your private key in this separate file. For SSH, if not specified, curl tries the following candidates in order: "~/.ssh/id_rsa", "~/.ssh/id_dsa", "./id_rsa", "./id_dsa".

If curl is built against OpenSSL library, and the engine pkcs11 or pkcs11 provider is available, then a PKCS#11 URI (RFC 7512) can be used to specify a private key located in a PKCS#11 device. A string beginning with "pkcs11:" is interpreted as a PKCS#11 URI. If a PKCS#11 URI is provided, then the --engine option is set as "pkcs11" if none was provided and the --key-type option is set as "ENG" or "PROV" if none was provided (depending on OpenSSL version).

If curl is built against Schannel then this option is ignored for TLS protocols (HTTPS, etc). That backend expects the private key to be already present in the keychain or PKCS#12 file containing the certificate.

If --key is provided several times, the last set value is used.

Example:

```
curl --cert certificate --key here https://example.com
```

See also --key-type and --cert.

--key-type <type>

(TLS) Private key file type. Specify which type your --key provided private key is. DER, PEM, and ENG are supported. If not specified, PEM is assumed.

If --key-type is provided several times, the last set value is used.

Example:

```
curl --key-type DER --key here https://example.com
```

See also --key.

--knownhosts <file>

(SCP SFTP) When doing SCP and SFTP transfers, curl automatically checks a database containing identification for all hosts it has ever been used with to verify that the host it connects to is the same as previously. Host keys are stored in such a known hosts file. curl uses the ~/.ssh/known_hosts in the user's home directory by default.

This option lets a user specify a specific file to check the host against.

The known hosts check can be disabled with --insecure, but that makes the transfer insecure and is strongly discouraged.

If --knownhosts is provided several times, the last set value is used.

Example:

```
curl --knownhosts filename --key here https://example.com
```

Added in 8.17.0. See also --hostpubsha256, --hostpubmd5, --insecure and --key.

--krb <level>

(FTP) Deprecated option (added in 8.17.0). It has no function anymore.

Enable Kerberos authentication and use. The level must be entered and should be one of "clear", "safe", "confidential", or "private". Should you use a level that is not one of these, "private" is used.

If --krb is provided several times, the last set value is used.

Example:

```
curl --krb clear ftp://example.com/
```

For --krb to work, it requires that the underlying libcurl is built to support Kerberos. See also --delegation and --ssl.

--libcurl <file>

Append this option to any ordinary curl command line, and you get libcurl-using C source code written to the file that does the equivalent of what your command-line operation does.

This option is global and does not need to be specified for each use of --next.

If --libcurl is provided several times, the last set value is used.

Example:

```
curl --libcurl client.c https://example.com
```

See also --verbose.

--limit-rate <speed>

Specify the maximum transfer rate you want curl to use - for both downloads and uploads. This feature is useful if you have a limited pipe and you would like your transfer not to use your entire bandwidth. To make it slower than it otherwise would be.

The given speed is measured in bytes/second, unless a suffix is appended. Appending 'k' or 'K' counts the number as kilobytes, 'm' or 'M' makes it megabytes etc. The supported suffixes (k, M, G, T, P) are 1024-based. For example 1k is 1024. Examples: 200K, 3m and 1G.

The rate limiting logic works on averaging the transfer speed to no more than the set threshold over a period of multiple seconds.

If you also use the --speed-limit option, that option takes precedence and might cripple the rate-limiting slightly, to help keep the speed-limit logic working.

Starting in curl 8.19.0, the rate can be specified using a fraction as in "2.5M" for two and a half megabytes per second. It only works with a period (".") delimiter, independent of what your locale might prefer.

If --limit-rate is provided several times, the last set value is used.

Examples:

```
curl --limit-rate 123.45K https://example.com
curl --limit-rate 1000 https://example.com
curl --limit-rate 10M https://example.com
curl --limit-rate 200K --max-time 60 https://example.com
```

See also --rate, --speed-limit and --speed-time.

-l, --list-only

(FTP POP3 SFTP FILE) When listing an FTP directory, force a name-only view. Maybe particularly useful if the user wants to machine-parse the contents of an FTP directory since the normal directory view does not use a standard look or format. When used like this, the option causes an NLST command to be sent to the server instead of LIST.

Note: Some FTP servers list only files in their response to NLST; they do not include subdirectories and symbolic links.

When listing an SFTP directory, this switch forces a name-only view, one per line. This is especially useful if the user wants to machine-parse the contents of an SFTP directory since the normal directory view provides more information than filenames.

When retrieving a specific email from POP3, this switch forces a LIST command to be performed instead of RETR. This is particularly useful if the user wants to see if a specific message-id exists on the server and what size it is.

For FILE, this option has no effect yet as directories are always listed in this mode.

Note: When combined with --request, this option can be used to send a UIDL command instead, so the user may use the email's unique identifier rather than its message-id to make the request.

Providing --list-only multiple times has no extra effect. Disable it again with --no-list-only.

Example:

```
curl --list-only ftp://example.com/dir/
```

See also --quote and --request.

--local-port <range>

Set a preferred single number or range (FROM-TO) of local port numbers to use for the connection(s). Note that port numbers by nature are a scarce resource so setting this range to something too narrow might cause unnecessary connection setup failures.

If --local-port is provided several times, the last set value is used.

Example:

```
curl --local-port 1000-3000 https://example.com
```

See also --globoff.

-L, --location

(HTTP) If the server reports that the requested page has moved to a different location (indicated with a Location: header and a 3XX response code), this option makes curl redo the request to the new place. If used together with --show-headers or --head, headers from all requested pages are shown.

When authentication is provided on the command line (for example --user or --oauth2-bearer), or when sending a cookie with "-H Cookie:", curl only sends its credentials to the initial host. If a redirect takes curl to a different host, it does not get the credentials passed on. See --location-trusted on how to change this. When --netrc is used in combination with this option, credentials for the followed-to hosts may also be selected from that file.

Limit the amount of redirects to follow by using the --max-redirs option.

When curl follows a redirect and if the request is a POST, it sends the following request with a GET if the HTTP response was 301, 302, or 303. If the response code was any other 3xx code, curl resends the following request using the same unmodified method.

You can tell curl to not change POST requests to GET after a 30x response by using the dedicated options for that: --post301, --post302 and --post303.

The method set with --request overrides the method curl would otherwise select to use.

Restrict which protocols a redirect is accepted to follow with --proto-redir.

Providing --location multiple times has no extra effect. Disable it again with --no-location.

Example:

```
curl -L https://example.com
```

See also --resolve, --alt-svc, --follow, --proto-redir and --max-redirs.

--location-trusted

(HTTP) Instruct curl to follow HTTP redirects like --location, but permit curl to send credentials and other secrets along to other hosts than the initial one.

This may or may not introduce a security breach if the site redirects you to a site to which you send this sensitive data to. Another host means that one or more of hostname, protocol scheme or port number changed.

This option also allows curl to pass long cookies set explicitly with --header.

Providing --location-trusted multiple times has no extra effect. Disable it again with --no-location-trusted.

Examples:

```
curl --location-trusted -u user:password https://example.com
curl --location-trusted -H "Cookie: session=abc" https://example.com
```

See also --user and --follow.

--login-options <options>

(IMAP LDAP POP3 SMTP) Specify the login options to use during server authentication.

You can use login options to specify protocol specific options that may be used during authentication. At present only IMAP, POP3 and SMTP support login options. For more information about login options please see RFC 2384, RFC 5092 and the IETF draft https://datatracker.ietf.org/doc/html/draft-earhart-url-smtp-00

Since 8.2.0, IMAP supports the login option "AUTH=+LOGIN". With this option, curl uses the plain (not SASL) "LOGIN IMAP" command even if the server advertises SASL authentication. Care should be taken in using this option, as it sends your password over the network in plain text. This does not work if the IMAP server disables the plain "LOGIN" (e.g. to prevent password snooping).

If --login-options is provided several times, the last set value is used.

Example:

```
curl --login-options 'AUTH=*' imap://example.com
```

See also --user.

--mail-auth <address>

(SMTP) Specify a single address. This is used to specify the authentication address (identity) of a submitted message that is being relayed to another server.

If --mail-auth is provided several times, the last set value is used.

Example:

```
curl --mail-auth user@example.com -T mail smtp://example.com/
```

See also --mail-rcpt and --mail-from.

--mail-from <address>

(SMTP) Specify a single address that the given mail should get sent from.

If --mail-from is provided several times, the last set value is used.

Example:

```
curl --mail-from user@example.com -T mail smtp://example.com/
```

See also --mail-rcpt and --mail-auth.

--mail-rcpt <address>

(SMTP) Specify a single email address, username or mailing list name. Repeat this option several times to send to multiple recipients.

When performing an address verification (VRFY command), the recipient should be specified as the username or username and domain (as per Section 3.5 of RFC 5321).

When performing a mailing list expand (EXPN command), the recipient should be specified using the mailing list name, such as "Friends" or "London-Office".

--mail-rcpt can be used several times in a command line.

Example:

```
curl --mail-rcpt user@example.net smtp://example.com
```

See also --mail-rcpt-allowfails.

--mail-rcpt-allowfails

(SMTP) When sending data to multiple recipients, by default curl aborts SMTP conversation if at least one of the recipients causes RCPT TO command to return an error.

The default behavior can be changed by passing --mail-rcpt-allowfails command-line option which makes curl ignore errors and proceed with the remaining valid recipients.

If all recipients trigger RCPT TO failures and this flag is specified, curl still aborts the SMTP conversation and returns the error received from to the last RCPT TO command.

Providing --mail-rcpt-allowfails multiple times has no extra effect. Disable it again with --no-mail-rcpt-allowfails.

Example:

```
curl --mail-rcpt-allowfails --mail-rcpt dest@example.com smtp://example.com
```

Added in 7.69.0. See also --mail-rcpt.

-M, --manual

Manual. Display the huge help text.

Example:

```
curl --manual
```

See also --verbose, --libcurl and --trace.

--max-filesize <bytes>

(FTP HTTP MQTT) When set to a non-zero value, it specifies the maximum size (in bytes) of a file to download. If the file requested is larger than this value, the transfer does not start and curl returns with exit code 63.

Setting the maximum value to zero disables the limit.

A unit suffix letter can be used. Appending 'k' or 'K' counts the number as kilobytes, 'm' or 'M' makes it megabytes etc. The supported suffixes (k, M, G, T, P) are 1024-based. Examples: 200K, 3m and 1G.

NOTE: before curl 8.4.0, when the file size is not known prior to download, for such files this option has no effect even if the file transfer ends up being larger than this given limit.

Starting with curl 8.4.0, this option aborts the transfer if it reaches the threshold during transfer.

Starting in curl 8.19.0, the maximum size can be specified using a fraction as in "2.5M" for two and a half megabytes. It only works with a period (".") delimiter, independent of what your locale might prefer.

Since 8.20.0, this option also stops ongoing transfers that would reach this threshold due to automatic decompression using --compressed.

If --max-filesize is provided several times, the last set value is used.

Examples:

```
curl --max-filesize 100K https://example.com
curl --max-filesize 2.6M https://example.com
```

See also --limit-rate.

--max-redirs <num>

(HTTP) Set the maximum number of redirections to follow. When --location or --follow are used, this option prevents curl from following too many redirects. By default the limit is set to 50 redirects. Set this option to -1 to make it unlimited.

If --max-redirs is provided several times, the last set value is used.

Example:

```
curl --max-redirs 3 --location https://example.com
```

See also --location and --follow.

-m, --max-time <seconds>

Set the maximum time in seconds that you allow each transfer to take. Prevents your batch jobs from hanging for hours due to slow networks or links going down. This option accepts decimal values.

If you enable retrying the transfer (--retry) then the maximum time counter is reset each time the transfer is retried. You can use --retry-max-time to limit the retry time.

The decimal value needs to be provided using a dot (.) as decimal separator - not the local version even if it might be using another separator.

If --max-time is provided several times, the last set value is used.

Examples:

```
curl --max-time 10 https://example.com
curl --max-time 2.92 https://example.com
```

See also --connect-timeout and --retry-max-time.

--metalink

This option was previously used to specify a Metalink resource. Metalink support is disabled in curl for security reasons (added in 7.78.0).

If --metalink is provided several times, the last set value is used.

Example:

```
curl --metalink file https://example.com
```

See also --parallel.

--mptcp

Enable the use of Multipath TCP (MPTCP) for connections. MPTCP is an extension to the standard TCP that allows multiple TCP streams over different network paths between the same source and destination. This can enhance bandwidth and improve reliability by using multiple paths simultaneously.

MPTCP is beneficial in networks where multiple paths exist between clients and servers, such as mobile networks where a device may switch between WiFi and cellular data or in wired networks with multiple Internet Service Providers.

This option is currently only supported on Linux starting from kernel 5.6. Only TCP connections are modified, hence this option does not affect HTTP/3 (QUIC) or UDP connections.

The server curl connects to must also support MPTCP. If not, the connection seamlessly falls back to TCP.

Providing --mptcp multiple times has no extra effect. Disable it again with --no-mptcp.

Example:

```
curl --mptcp https://example.com
```

Added in 8.9.0. See also --tcp-fastopen.

--negotiate

(HTTP) Enable Negotiate (SPNEGO) authentication.

This option requires a library built with GSS-API or SSPI support. Use --version to see if your curl supports GSS-API/SSPI or SPNEGO.

When using this option, you must also provide a fake --user option to activate the authentication code properly. Sending a '-u :' is enough as the username and password from the --user option are not actually used.

Providing --negotiate multiple times has no extra effect. Disable it again with --no-negotiate.

Example:

```
curl --negotiate -u : https://example.com
```

See also --basic, --ntlm, --anyauth and --proxy-negotiate.

-n, --netrc

Make curl scan the .netrc file in the user's home directory for login name and password. This is typically used for FTP on Unix. If used with HTTP, curl enables user authentication. See netrc(5) and ftp(1) for details on the file format. curl does not complain if that file does not have the right permissions (it should be neither world- nor group-readable). The environment variable "HOME" is used to find the home directory. If the "NETRC" environment variable is set, that filename is used as the netrc file. (Added in 8.16.0)

If --netrc-file is used, that overrides all other ways to figure out the file.

The netrc file provides credentials for a hostname independent of which protocol and port number that are used.

On Windows two filenames in the home directory are checked: .netrc and _netrc, preferring the former. Older versions on Windows checked for _netrc only.

A quick and simple example of how to setup a .netrc to allow curl to access the machine host.example.com with username "myself" and password "secret" could look similar to:

```
machine host.example.com
login myself
password secret
```

curl also supports the "default" keyword. This is the same as machine name except that default matches any name. There can be only one "default" token, and it must be after all machine tokens.

When providing a username in the URL and a .netrc file, curl looks for the password for that specific user for the given host if such an entry appears in the file before a "generic" "machine" entry without "login" specified.

Providing --netrc multiple times has no extra effect. Disable it again with --no-netrc.

Example:

```
curl --netrc https://example.com
```

This option is mutually exclusive with --netrc-file and --netrc-optional. See also --netrc-file, --config and --user.

--netrc-file <filename>

Set the netrc file to use. Similar to --netrc, except that you also provide the path (absolute or relative).

It abides by --netrc-optional if specified.

If --netrc-file is provided several times, the last set value is used.

Example:

```
curl --netrc-file netrc https://example.com
```

This option is mutually exclusive with --netrc. See also --netrc, --user and --config.

--netrc-optional

Similar to --netrc, but this option makes the .netrc usage optional and not mandatory as the --netrc option does.

Providing --netrc-optional multiple times has no extra effect. Disable it again with --no-netrc-optional.

Example:

```
curl --netrc-optional https://example.com
```

This option is mutually exclusive with --netrc. See also --netrc-file.

-:, --next

Use a separate operation for the following URL and associated options. This allows you to send several URL requests, each with their own specific options, for example, such as different usernames or custom requests for each.

--next resets all local options and only global ones have their values survive over to the operation following the --next instruction. Global options include --verbose, --trace, --trace-ascii and --fail-early.

For example, you can do both a GET and a POST in a single command line:

```
curl www1.example.com --next -d postthis www2.example.com
```

--next can be used several times in a command line.

Examples:

```
curl https://example.com --next -d postthis www2.example.com
curl -I https://example.com --next https://example.net/
```

See also --parallel and --config.

--no-alpn

(HTTPS) Disable the ALPN TLS extension. ALPN is enabled by default if libcurl was built with an SSL library that supports ALPN. ALPN is used by a libcurl that supports HTTP/2 to negotiate HTTP/2 support with the server during https sessions.

Note that this is the negated option name documented. You can use --alpn to enable ALPN.

Providing --no-alpn multiple times has no extra effect. Disable it again with --alpn.

Example:

```
curl --no-alpn https://example.com
```

For --no-alpn to work, it requires that the underlying libcurl is built to support TLS. See also --no-npn and --http2.

-N, --no-buffer

Disable the buffering of the output stream. In normal work situations, curl uses a standard buffered output stream that has the effect that it outputs the data in chunks, not necessarily exactly when the data arrives. Using this option disables that buffering.

Note that this is the negated option name documented. You can use --buffer to enable buffering again.

Providing --no-buffer multiple times has no extra effect. Disable it again with --buffer.

Example:

```
curl --no-buffer https://example.com
```

See also --progress-bar.

--no-clobber

When used in conjunction with the --output, --remote-header-name, --remote-name, or --remote-name-all options, curl avoids overwriting files that already exist. Instead, a dot and a number gets appended to the name of the file that would be created, up to filename.100 after which it does not create any file.

Note that this is the negated option name documented. You can thus use --clobber to enforce the clobbering, even if --remote-header-name is specified.

The --continue-at option cannot be used together with --no-clobber.

Providing --no-clobber multiple times has no extra effect. Disable it again with --clobber.

Example:

```
curl --no-clobber --output local/dir/file https://example.com
```

Added in 7.83.0. See also --output and --remote-name.

--no-keepalive

Disable the use of keepalive messages on the TCP connection. curl otherwise enables them by default.

Note that this is the negated option name documented. You can thus use --keepalive to enforce keepalive.

Providing --no-keepalive multiple times has no extra effect. Disable it again with --keepalive.

Example:

```
curl --no-keepalive https://example.com
```

See also --keepalive-time and --keepalive-cnt.

--no-npn

(HTTPS) curl never uses NPN, this option has no effect (added in 7.86.0).

Disable the NPN TLS extension. NPN is enabled by default if libcurl was built with an SSL library that supports NPN. NPN is used by a libcurl that supports HTTP/2 to negotiate HTTP/2 support with the server during https sessions.

Providing --no-npn multiple times has no extra effect. Disable it again with --npn.

Example:

```
curl --no-npn https://example.com
```

For --no-npn to work, it requires that the underlying libcurl is built to support TLS. See also --no-alpn and --http2.

--no-progress-meter

Option to switch off the progress meter output without muting or otherwise affecting warning and informational messages like --silent does.

Note that this is the negated option name documented. You can thus use --progress-meter to enable the progress meter again.

Providing --no-progress-meter multiple times has no extra effect. Disable it again with --progress-meter.

Example:

```
curl --no-progress-meter -o store https://example.com
```

Added in 7.67.0. See also --verbose and --silent.

--no-sessionid

(TLS) Disable curl's use of SSL session-ID caching. By default all transfers are done using the cache. Note that while nothing should ever get hurt by attempting to reuse SSL session-IDs, there seem to be broken SSL implementations in the wild that may require you to disable this in order for you to succeed.

Note that this is the negated option name documented. You can thus use --sessionid to enforce session-ID caching.

Providing --no-sessionid multiple times has no extra effect. Disable it again with --sessionid.

Example:

```
curl --no-sessionid https://example.com
```

See also --insecure.

--noproxy <no-proxy-list>

Comma-separated list of hosts for which not to use a proxy, if one is specified. The only wildcard is a single "*" character, which matches all hosts, and effectively disables the proxy. Each name in this list is matched as either a domain which contains the hostname, or the hostname itself. For example, "local.com" would match "local.com", "local.com:80", and "www.local.com", but not "www.notlocal.com".

To use international hostnames in this list, add the punycode version of the hostname.

This option overrides the environment variables that disable the proxy ("no_proxy" and "NO_PROXY"). If there is an environment variable disabling a proxy, you can set the no proxy list to "" to override it.

IP addresses specified to this option can be provided using CIDR notation (added in 7.86.0): an appended slash and number specifies the number of network bits out of the address to use in the comparison. For example "192.168.0.0/16" would match all addresses starting with "192.168".

If --noproxy is provided several times, the last set value is used.

Example:

```
curl --noproxy "www.example" https://example.com
```

See also --proxy.

--ntlm

(HTTP) Use NTLM authentication. The NTLM authentication method was designed by Microsoft and is used by IIS web servers. It is a proprietary protocol, reverse-engineered by clever people and implemented in curl based on their efforts. This kind of behavior should not be endorsed, you should encourage everyone who uses NTLM to switch to a public and documented authentication method instead, such as Digest.

If you want to enable NTLM for your proxy authentication, then use --proxy-ntlm.

Providing --ntlm multiple times has no extra effect. Disable it again with --no-ntlm.

Example:

```
curl --ntlm -u user:password https://example.com
```

For --ntlm to work, it requires that the underlying libcurl is built to support TLS. See also --proxy-ntlm.

--ntlm-wb

(HTTP) Deprecated option (added in 8.8.0).

Enabled NTLM much in the style --ntlm does, but handed over the authentication to a separate executable that was executed when needed.

Providing --ntlm-wb multiple times has no extra effect.

Example:

```
curl --ntlm-wb -u user:password https://example.com
```

See also --ntlm and --proxy-ntlm.

--oauth2-bearer <token>

(IMAP LDAP POP3 SMTP HTTP) Specify the Bearer Token for OAUTH 2.0 server authentication. The Bearer Token is used in conjunction with the username which can be specified as part of the --url or --user options.

The Bearer Token and username are formatted according to RFC 6750.

If --oauth2-bearer is provided several times, the last set value is used.

Example:

```
curl --oauth2-bearer "mF_9.B5f-4.1JqM" https://example.com
```

See also --basic, --ntlm and --digest.

--out-null

Discard all response output of a transfer silently. This is the more efficient and portable version of

```
curl https://host.example -o /dev/null
```

The transfer is done in full, all data is received and checked, but the bytes are not written anywhere.

--out-null is associated with a single URL. Use it once per URL when you use several URLs in a command line.

Example:

```
curl "https://example.com" --out-null
```

Added in 8.16.0. See also --output, --remote-name, --remote-name-all and --remote-header-name.

-o, --output <file>

Write output to the given file instead of stdout. If you are using globbing in the URL to fetch multiple documents, you should quote the URL and you can use "#" followed by a number in the filename. That variable gets replaced with the current glob text. Like in:

```
curl "http://{one,two}.example.com" -o "file_#1.txt"
```

or use several variables like:

```
curl "http://{site,host}.host[1-5].example" -o "#1_#2"
```

You may use this option as many times as the number of URLs you have. For example, if you specify two URLs on the same command line, you can use it like this:

```
curl -o aa example.com -o bb example.net
```

and the order of the -o options and the URLs does not matter, only that the first -o is for the first URL and so on, so the above command line can also be written as

```
curl example.com example.net -o aa -o bb
```

See also the --create-dirs option to create the local directories dynamically. Specifying the output as '-' (a single dash) passes the output to stdout.

To suppress response bodies, you can redirect output to /dev/null:

```
curl example.com -o /dev/null
```

Or for Windows:

```
curl example.com -o nul
```

Or, even more efficient and portable, use

```
curl example.com --out-null
```

Specify the filename as single minus to force the output to stdout, to override curl's internal binary output in terminal prevention:

```
curl https://example.com/jpeg -o -
```

Note that the binary output may be caused by the response being compressed, in which case you may want to use the --compressed option.

Since curl 8.21.0, the separate globbing parts can be named and referenced by their names. The case sensitive alphanumeric name is set enclosed within angle brackets after the opening character. Examples:

```
curl "https://fun.example/{<num>one,two}.jpg" -o "save-#<num>"
 
curl "ftp://ftp.example/file[<range>1-100].txt" \
  -o "save-#<range>.txt"
```

Referencing a named glob that is not set, causes an error.

Since curl 8.21.0, you can use parts of the upload filename when it uses globbing by setting a glob name and referencing it the same way you reference named URL globs. For example, if you upload three files to a single fixed HTTP URL and want to save the corresponding responses in separate files:

```
curl -T 'file{<num>1,2,3}' \
  https://upload.example/ -o 'response-#<num>'
```

--output is associated with a single URL. Use it once per URL when you use several URLs in a command line.

Examples:

```
curl -o file https://example.com
curl "http://{one,two}.example.com" -o "file_#1.txt"
curl "http://{site,host}.host[1-5].example" -o "#1_#2"
curl -o file https://example.com -o file2 https://example.net
```

See also --out-null, --remote-name, --remote-name-all, --remote-header-name and --compressed.

--output-dir <dir>

Specify the directory in which files should be stored, when --remote-name or --output are used.

The given output directory is used for all URLs and output options on the command line, up until the first --next.

If the specified target directory does not exist, the operation fails unless --create-dirs is also used.

If --output-dir is provided several times, the last set value is used.

Example:

```
curl --output-dir "tmp" -O https://example.com
```

Added in 7.73.0. See also --remote-name and --remote-header-name.

-Z, --parallel

Make curl perform all transfers in parallel as compared to the regular serial manner. Parallel transfer means that curl runs up to N concurrent transfers simultaneously and if there are more than N transfers to handle, it starts new ones when earlier transfers finish.

With parallel transfers, the progress meter output is different from when doing serial transfers, as it then displays the transfer status for multiple transfers in a single line.

The maximum amount of concurrent transfers is set with --parallel-max and it defaults to 50.

This option is global and does not need to be specified for each use of --next.

Providing --parallel multiple times has no extra effect. Disable it again with --no-parallel.

Example:

```
curl --parallel https://example.com -o file1 https://example.com -o file2
```

Added in 7.66.0. See also --next, --verbose, --parallel-max and --parallel-immediate.

--parallel-immediate

When doing parallel transfers, this option instructs curl to prefer opening up more connections in parallel at once rather than waiting to see if new transfers can be added as multiplexed streams on another connection.

By default, without this option set, curl prefers to wait a little and multiplex new transfers over existing connections. It keeps the number of connections low at the expense of risking a slightly slower transfer startup.

This option is global and does not need to be specified for each use of --next.

Providing --parallel-immediate multiple times has no extra effect. Disable it again with --no-parallel-immediate.

Example:

```
curl --parallel-immediate -Z https://example.com -o file1 https://example.com -o file2
```

Added in 7.68.0. See also --parallel and --parallel-max.

--parallel-max <num>

When asked to do parallel transfers, using --parallel, this option controls the maximum amount of transfers to do simultaneously.

The default is 50. 65535 is the largest supported value.

This option is global and does not need to be specified for each use of --next.

If --parallel-max is provided several times, the last set value is used.

Example:

```
curl --parallel-max 100 -Z https://example.com ftp://example.com/
```

Added in 7.66.0. See also --parallel and --parallel-max-host.

--parallel-max-host <num>

When asked to do parallel transfers, using --parallel, this option controls the maximum amount of concurrent connections curl is allowed to do to the same protocol + hostname + port number target.

The limit is enforced by libcurl and queued "internally", which means that transfers that are waiting for an available connection still look like started transfers in the progress meter.

The default is 0 (unlimited). 65535 is the largest supported value.

This option is global and does not need to be specified for each use of --next.

If --parallel-max-host is provided several times, the last set value is used.

Example:

```
curl --parallel-max-host 5 -Z https://example.com ftp://example.com/
```

Added in 8.16.0. See also --parallel and --parallel-max.

--pass <phrase>

(TLS SCP SFTP) Passphrase for the private key used for SSH or TLS.

If --pass is provided several times, the last set value is used.

Example:

```
curl --pass secret --key file https://example.com
```

See also --key and --user.

--path-as-is

Do not handle sequences of /../ or /./ in the given URL path. Normally curl squashes or merges them according to standards but with this option set you tell it not to do that.

Providing --path-as-is multiple times has no extra effect. Disable it again with --no-path-as-is.

Example:

```
curl --path-as-is https://example.com/../../etc/passwd
```

See also --request-target.

--pinnedpubkey <hashes>

(TLS) Use the specified public key file (or hashes) to verify the peer. This can be a path to a file which contains a single public key in PEM or DER format, or any number of base64 encoded sha256 hashes preceded by 'sha256//' and separated by ';'.

When negotiating a TLS or SSL connection, the server sends a certificate indicating its identity. A public key is extracted from this certificate and if it does not exactly match the public key provided to this option, curl aborts the connection before sending or receiving any data.

This option is independent of option --insecure. If you use both options together then the peer is still verified by public key.

PEM/DER support:

OpenSSL and GnuTLS, wolfSSL, mbedTLS, Schannel

sha256 support:

OpenSSL, GnuTLS and wolfSSL, mbedTLS, Schannel

Other SSL backends not supported.

If --pinnedpubkey is provided several times, the last set value is used.

Examples:

```
curl --pinnedpubkey keyfile https://example.com
curl --pinnedpubkey 'sha256//ce118b51897f4452dc' https://example.com
```

See also --hostpubsha256.

--post301

(HTTP) Respect RFC 7231/6.4.2 and do not convert POST requests into GET requests when following a 301 redirect. The non-RFC behavior is ubiquitous in web browsers, so curl does the conversion by default to maintain consistency. A server may require a POST to remain a POST after such a redirection. This option is meaningful only when using --location.

Providing --post301 multiple times has no extra effect. Disable it again with --no-post301.

Example:

```
curl --post301 --location -d "data" https://example.com
```

See also --post302, --post303 and --location.

--post302

(HTTP) Respect RFC 7231/6.4.3 and do not convert POST requests into GET requests when following a 302 redirect. The non-RFC behavior is ubiquitous in web browsers, so curl does the conversion by default to maintain consistency. A server may require a POST to remain a POST after such a redirection. This option is meaningful only when using --location.

Providing --post302 multiple times has no extra effect. Disable it again with --no-post302.

Example:

```
curl --post302 --location -d "data" https://example.com
```

See also --post301, --post303 and --location.

--post303

(HTTP) Violate RFC 7231/6.4.4 and do not convert POST requests into GET requests when following 303 redirect. A server may require a POST to remain a POST after a 303 redirection. This option is meaningful only when using --location.

Providing --post303 multiple times has no extra effect. Disable it again with --no-post303.

Example:

```
curl --post303 --location -d "data" https://example.com
```

See also --post302, --post301 and --location.

--preproxy <[protocol://]host[:port]>

Use the specified SOCKS proxy before connecting to an HTTP or HTTPS --proxy. In such a case curl first connects to the SOCKS proxy and then connects (through SOCKS) to the HTTP or HTTPS proxy. Hence pre proxy.

The pre proxy string should be specified with a "protocol://" prefix to specify alternative proxy protocols. Use "socks4://", "socks4a://", "socks5://" or "socks5h://" to request the specific SOCKS version to be used. No protocol specified makes curl default to SOCKS4.

If the port number is not specified in the proxy string, it is assumed to be 1080.

User and password that might be provided in the proxy string are URL decoded by curl. This allows you to pass in special characters such as @ by using %40 or pass in a colon with %3a.

If --preproxy is provided several times, the last set value is used.

Example:

```
curl --preproxy socks5://proxy.example -x http://http.example https://example.com
```

See also --proxy and --socks5.

-#, --progress-bar

Make curl display transfer progress as a simple progress bar instead of the standard, more informational, meter.

This progress bar draws a single line of '#' characters across the screen and shows a percentage if the transfer size is known. For transfers without a known size, there is a space ship (-=o=-) that moves back and forth but only while data is being transferred, with a set of flying hash sign symbols on top.

This option is global and does not need to be specified for each use of --next.

Providing --progress-bar multiple times has no extra effect. Disable it again with --no-progress-bar.

Example:

```
curl -# -O https://example.com
```

See also --styled-output.

--proto <protocols>

Limit what protocols to allow for transfers. Protocols are evaluated left to right, are comma separated, and are each a protocol name or 'all', optionally prefixed by zero or more modifiers. Available modifiers are:

+

Permit this protocol in addition to protocols already permitted (this is the default if no modifier is used).

-

Deny this protocol, removing it from the list of protocols already permitted.

=

Permit only this protocol (ignoring the list already permitted), though subject to later modification by subsequent entries in the comma separated list.

For example: --proto -ftps uses the default protocols, but disables ftps

--proto -all,https,+http only enables http and https

--proto =http,https also only enables http and https

Unknown and disabled protocols produce a warning. This allows scripts to safely rely on being able to disable potentially dangerous protocols, without relying upon support for that protocol being built into curl to avoid an error.

This option can be used multiple times, in which case the effect is the same as concatenating the protocols into one instance of the option.

If --proto is provided several times, the last set value is used.

Example:

```
curl --proto =http,https,sftp https://example.com
```

See also --proto-redir and --proto-default.

--proto-default <protocol>

Use protocol for any provided URL missing a scheme. The case-insensitive name should be given without any "://" suffix.

An unknown or unsupported protocol causes error CURLE_UNSUPPORTED_PROTOCOL.

This option does not change the default proxy protocol (http).

Without this option set, curl guesses protocol based on the hostname, see --url for details.

The default protocol cannot be set to "ipfs" or "ipns". Those schemes need to be used explicitly in the URL.

If --proto-default is provided several times, the last set value is used.

Example:

```
curl --proto-default https ftp.example.com
```

See also --proto and --proto-redir.

--proto-redir <protocols>

Limit what protocols to allow on redirects. Protocols denied by --proto are not overridden by this option. See --proto for how protocols are represented.

Example, allow only HTTP and HTTPS on redirect:

```
curl --proto-redir -all,http,https --follow http://example.com
```

By default curl only allows HTTP, HTTPS, FTP and FTPS on redirects . Specifying all or +all enables all protocols on redirects, which is not good for security.

If --proto-redir is provided several times, the last set value is used.

Example:

```
curl --proto-redir =http,https --follow https://example.com
```

See also --proto and --follow.

-x, --proxy <[protocol://]host[:port]>
