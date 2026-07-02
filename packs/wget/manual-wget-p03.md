---
title: "GNU Wget 1.25.0 Manual (part 3/6)"
source: https://www.gnu.org/software/wget/manual/wget.html
domain: wget
license: CC-BY-SA-4.0
tags: wget download, file download, recursive download, command-line http
fetched: 2026-07-02
part: 3/6
---

# GNU Wget 1.25.0 Manual

You will typically use this option when mirroring sites that require that you be logged in to access some or all of their content. The login process typically works by the web server issuing an HTTP cookie upon receiving and verifying your credentials. The cookie is then resent by the browser when accessing that part of the site, and so proves your identity.

Mirroring such a site requires Wget to send the same cookies your browser sends when communicating with the site. This is achieved by ‘--load-cookies’—simply point Wget to the location of the cookies.txt file, and it will send the same cookies your browser would send in the same situation. Different browsers keep textual cookie files in different locations:

**Netscape 4.x.**

The cookies are in ~/.netscape/cookies.txt.

**Mozilla and Netscape 6.x.**

Mozilla’s cookie file is also named cookies.txt, located somewhere under ~/.mozilla, in the directory of your profile. The full path usually ends up looking somewhat like ~/.mozilla/default/*some-weird-string*/cookies.txt.

**Internet Explorer.**

You can produce a cookie file Wget can use by using the File menu, Import and Export, Export Cookies. This has been tested with Internet Explorer 5; it is not guaranteed to work with earlier versions.

**Other browsers.**

If you are using a different browser to create your cookies, ‘--load-cookies’ will only work if you can locate or produce a cookie file in the Netscape format that Wget expects.

If you cannot use ‘--load-cookies’, there might still be an alternative. If your browser supports a “cookie manager”, you can use it to view the cookies used when accessing the site you’re mirroring. Write down the name and value of the cookie, and manually instruct Wget to send those cookies, bypassing the “official” cookie support:

```
wget --no-cookies --header "Cookie: name=value"
```

**‘--save-cookies *file*’ ¶**

Save cookies to *file* before exiting. This will not save cookies that have expired or that have no expiry time (so-called “session cookies”), but also see ‘--keep-session-cookies’.

**‘--keep-session-cookies’ ¶**

When specified, causes ‘--save-cookies’ to also save session cookies. Session cookies are normally not saved because they are meant to be kept in memory and forgotten when you exit the browser. Saving them is useful on sites that require you to log in or to visit the home page before you can access some pages. With this option, multiple Wget runs are considered a single browser session as far as the site is concerned.

Since the cookie file format does not normally carry session cookies, Wget marks them with an expiry timestamp of 0. Wget’s ‘--load-cookies’ recognizes those as session cookies, but it might confuse other browsers. Also note that cookies so loaded will be treated as other session cookies, which means that if you want ‘--save-cookies’ to preserve them again, you must use ‘--keep-session-cookies’ again.

**‘--ignore-length’ ¶**

Unfortunately, some HTTP servers (CGI programs, to be more precise) send out bogus `Content-Length` headers, which makes Wget go wild, as it thinks not all the document was retrieved. You can spot this syndrome if Wget retries getting the same document again and again, each time claiming that the (otherwise normal) connection has closed on the very same byte.

With this option, Wget will ignore the `Content-Length` header—as if it never existed.

**‘--header=*header-line*’ ¶**

Send *header-line* along with the rest of the headers in each HTTP request. The supplied header is sent as-is, which means it must contain name and value separated by colon, and must not contain newlines.

You may define more than one additional header by specifying ‘--header’ more than once.

```
wget --header='Accept-Charset: iso-8859-2' \
     --header='Accept-Language: hr'        \
       http://fly.srk.fer.hr/
```

Specification of an empty string as the header value will clear all previous user-defined headers.

As of Wget 1.10, this option can be used to override headers otherwise generated automatically. This example instructs Wget to connect to localhost, but to specify ‘foo.bar’ in the `Host` header:

```
wget --header="Host: foo.bar" http://localhost/
```

In versions of Wget prior to 1.10 such use of ‘--header’ caused sending of duplicate headers.

**‘--compression=*type*’ ¶**

Choose the type of compression to be used. Legal values are ‘auto’, ‘gzip’ and ‘none’.

If ‘auto’ or ‘gzip’ are specified, Wget asks the server to compress the file using the gzip compression format. If the server compresses the file and responds with the `Content-Encoding` header field set appropriately, the file will be decompressed automatically.

If ‘none’ is specified, wget will not ask the server to compress the file and will not decompress any server responses. This is the default.

Compression support is currently experimental. In case it is turned on, please report any bugs to `bug-wget@gnu.org`.

**‘--max-redirect=*number*’ ¶**

Specifies the maximum number of redirections to follow for a resource. The default is 20, which is usually far more than necessary. However, on those occasions where you want to allow more (or fewer), this is the option to use.

**‘--proxy-user=*user*’ ¶**

**‘--proxy-password=*password*’**

Specify the username *user* and password *password* for authentication on a proxy server. Wget will encode them using the `basic` authentication scheme.

Security considerations similar to those with ‘--http-password’ pertain here as well.

**‘--referer=*url*’ ¶**

Include ‘Referer: *url*’ header in HTTP request. Useful for retrieving documents with server-side processing that assume they are always being retrieved by interactive web browsers and only come out properly when Referer is set to one of the pages that point to them.

**‘--save-headers’ ¶**

Save the headers sent by the HTTP server to the file, preceding the actual contents, with an empty line as the separator.

**‘-U *agent-string*’ ¶**

**‘--user-agent=*agent-string*’**

Identify as *agent-string* to the HTTP server.

The HTTP protocol allows the clients to identify themselves using a `User-Agent` header field. This enables distinguishing the WWW software, usually for statistical purposes or for tracing of protocol violations. Wget normally identifies as ‘Wget/*version*’, *version* being the current version number of Wget.

However, some sites have been known to impose the policy of tailoring the output according to the `User-Agent`-supplied information. While this is not such a bad idea in theory, it has been abused by servers denying information to clients other than (historically) Netscape or, more frequently, Microsoft Internet Explorer. This option allows you to change the `User-Agent` line issued by Wget. Use of this option is discouraged, unless you really know what you are doing.

Specifying empty user agent with ‘--user-agent=""’ instructs Wget not to send the `User-Agent` header in HTTP requests.

**‘--post-data=*string*’ ¶**

**‘--post-file=*file*’**

Use POST as the method for all HTTP requests and send the specified data in the request body. ‘--post-data’ sends *string* as data, whereas ‘--post-file’ sends the contents of *file*. Other than that, they work in exactly the same way. In particular, they *both* expect content of the form `key1=value1&key2=value2`, with percent-encoding for special characters; the only difference is that one expects its content as a command-line parameter and the other accepts its content from a file. In particular, ‘--post-file’ is *not* for transmitting files as form attachments: those must appear as `key=value` data (with appropriate percent-coding) just like everything else. Wget does not currently support `multipart/form-data` for transmitting POST data; only `application/x-www-form-urlencoded`. Only one of ‘--post-data’ and ‘--post-file’ should be specified.

Please note that wget does not require the content to be of the form `key1=value1&key2=value2`, and neither does it test for it. Wget will simply transmit whatever data is provided to it. Most servers however expect the POST data to be in the above format when processing HTML Forms.

When sending a POST request using the ‘--post-file’ option, Wget treats the file as a binary file and will send every character in the POST request without stripping trailing newline or formfeed characters. Any other control characters in the text will also be sent as-is in the POST request.

Please be aware that Wget needs to know the size of the POST data in advance. Therefore the argument to `--post-file` must be a regular file; specifying a FIFO or something like /dev/stdin won’t work. It’s not quite clear how to work around this limitation inherent in HTTP/1.0. Although HTTP/1.1 introduces *chunked* transfer that doesn’t require knowing the request length in advance, a client can’t use chunked unless it knows it’s talking to an HTTP/1.1 server. And it can’t know that until it receives a response, which in turn requires the request to have been completed – a chicken-and-egg problem.

Note: As of version 1.15 if Wget is redirected after the POST request is completed, its behaviour will depend on the response code returned by the server. In case of a 301 Moved Permanently, 302 Moved Temporarily or 307 Temporary Redirect, Wget will, in accordance with RFC2616, continue to send a POST request. In case a server wants the client to change the Request method upon redirection, it should send a 303 See Other response code.

This example shows how to log in to a server using POST and then proceed to download the desired pages, presumably only accessible to authorized users:

```
# Log in to the server.  This can be done only once.
wget --save-cookies cookies.txt \
     --post-data 'user=foo&password=bar' \
     http://example.com/auth.php

# Now grab the page or pages we care about.
wget --load-cookies cookies.txt \
     -p http://example.com/interesting/article.php
```

If the server is using session cookies to track user authentication, the above will not work because ‘--save-cookies’ will not save them (and neither will browsers) and the cookies.txt file will be empty. In that case use ‘--keep-session-cookies’ along with ‘--save-cookies’ to force saving of session cookies.

**‘--method=*HTTP-Method*’ ¶**

For the purpose of RESTful scripting, Wget allows sending of other HTTP Methods without the need to explicitly set them using ‘--header=Header-Line’. Wget will use whatever string is passed to it after ‘--method’ as the HTTP Method to the server.

**‘--body-data=*Data-String*’**

**‘--body-file=*Data-File*’**

Must be set when additional data needs to be sent to the server along with the Method specified using ‘--method’. ‘--body-data’ sends *string* as data, whereas ‘--body-file’ sends the contents of *file*. Other than that, they work in exactly the same way.

Currently, ‘--body-file’ is *not* for transmitting files as a whole. Wget does not currently support `multipart/form-data` for transmitting data; only `application/x-www-form-urlencoded`. In the future, this may be changed so that wget sends the ‘--body-file’ as a complete file instead of sending its contents to the server. Please be aware that Wget needs to know the contents of BODY Data in advance, and hence the argument to ‘--body-file’ should be a regular file. See ‘--post-file’ for a more detailed explanation. Only one of ‘--body-data’ and ‘--body-file’ should be specified.

If Wget is redirected after the request is completed, Wget will suspend the current method and send a GET request till the redirection is completed. This is true for all redirection response codes except 307 Temporary Redirect which is used to explicitly specify that the request method should *not* change. Another exception is when the method is set to `POST`, in which case the redirection rules specified under ‘--post-data’ are followed.

**‘--content-disposition’ ¶**

If this is set to on, experimental (not fully-functional) support for `Content-Disposition` headers is enabled. This can currently result in extra round-trips to the server for a `HEAD` request, and is known to suffer from a few bugs, which is why it is not currently enabled by default.

This option is useful for some file-downloading CGI programs that use `Content-Disposition` headers to describe what the name of a downloaded file should be.

When combined with ‘--metalink-over-http’ and ‘--trust-server-names’, a ‘Content-Type: application/metalink4+xml’ file is named using the `Content-Disposition` filename field, if available.

**‘--content-on-error’ ¶**

If this is set to on, wget will not skip the content when the server responds with a http status code that indicates error.

**‘--trust-server-names’ ¶**

If this is set, on a redirect, the local file name will be based on the redirection URL. By default the local file name is based on the original URL. When doing recursive retrieving this can be helpful because in many web sites redirected URLs correspond to an underlying file structure, while link URLs do not.

**‘--auth-no-challenge’ ¶**

If this option is given, Wget will send Basic HTTP authentication information (plaintext username and password) for all requests, just like Wget 1.10.2 and prior did by default.

Use of this option is not recommended, and is intended only to support some few obscure servers, which never send HTTP authentication challenges, but accept unsolicited auth info, say, in addition to form-based authentication.

**‘--retry-on-host-error’**

Consider host errors, such as “Temporary failure in name resolution”, as non-fatal, transient errors.

**‘--retry-on-http-error=*code[,code,...]*’**

Consider given HTTP response codes as non-fatal, transient errors. Supply a comma-separated list of 3-digit HTTP response codes as argument. Useful to work around special circumstances where retries are required, but the server responds with an error code normally not retried by Wget. Such errors might be 503 (Service Unavailable) and 429 (Too Many Requests). Retries enabled by this option are performed subject to the normal retry timing and retry count limitations of Wget.

Using this option is intended to support special use cases only and is generally not recommended, as it can force retries even in cases where the server is actually trying to decrease its load. Please use wisely and only if you know what you are doing.

### 2.8 HTTPS (SSL/TLS) Options

To support encrypted HTTP (HTTPS) downloads, Wget must be compiled with an external SSL library. The current default is GnuTLS. In addition, Wget also supports HSTS (HTTP Strict Transport Security). If Wget is compiled without SSL support, none of these options are available.

**‘--secure-protocol=*protocol*’ ¶**

Choose the secure protocol to be used. Legal values are ‘auto’, ‘SSLv2’, ‘SSLv3’, ‘TLSv1’, ‘TLSv1_1’, ‘TLSv1_2’, ‘TLSv1_3’ and ‘PFS’. If ‘auto’ is used, the SSL library is given the liberty of choosing the appropriate protocol automatically, which is achieved by sending a TLSv1 greeting. This is the default.

Specifying ‘SSLv2’, ‘SSLv3’, ‘TLSv1’, ‘TLSv1_1’, ‘TLSv1_2’ or ‘TLSv1_3’ forces the use of the corresponding protocol. This is useful when talking to old and buggy SSL server implementations that make it hard for the underlying SSL library to choose the correct protocol version. Fortunately, such servers are quite rare.

Specifying ‘PFS’ enforces the use of the so-called Perfect Forward Security cipher suites. In short, PFS adds security by creating a one-time key for each SSL connection. It has a bit more CPU impact on client and server. We use known to be secure ciphers (e.g. no MD4) and the TLS protocol. This mode also explicitly excludes non-PFS key exchange methods, such as RSA.

**‘--https-only’**

When in recursive mode, only HTTPS links are followed.

**‘--ciphers’**

Set the cipher list string. Typically this string sets the cipher suites and other SSL/TLS options that the user wish should be used, in a set order of preference (GnuTLS calls it ’priority string’). This string will be fed verbatim to the SSL/TLS engine (OpenSSL or GnuTLS) and hence its format and syntax is dependent on that. Wget will not process or manipulate it in any way. Refer to the OpenSSL or GnuTLS documentation for more information.

**‘--no-check-certificate’ ¶**

Don’t check the server certificate against the available certificate authorities. Also don’t require the URL host name to match the common name presented by the certificate.

As of Wget 1.10, the default is to verify the server’s certificate against the recognized certificate authorities, breaking the SSL handshake and aborting the download if the verification fails. Although this provides more secure downloads, it does break interoperability with some sites that worked with previous Wget versions, particularly those using self-signed, expired, or otherwise invalid certificates. This option forces an “insecure” mode of operation that turns the certificate verification errors into warnings and allows you to proceed.

If you encounter “certificate verification” errors or ones saying that “common name doesn’t match requested host name”, you can use this option to bypass the verification and proceed with the download. *Only use this option if you are otherwise convinced of the site’s authenticity, or if you really don’t care about the validity of its certificate.* It is almost always a bad idea not to check the certificates when transmitting confidential or important data. For self-signed/internal certificates, you should download the certificate and verify against that instead of forcing this insecure mode. If you are really sure of not desiring any certificate verification, you can specify –check-certificate=quiet to tell wget to not print any warning about invalid certificates, albeit in most cases this is the wrong thing to do.

**‘--certificate=*file*’ ¶**

Use the client certificate stored in *file*. This is needed for servers that are configured to require certificates from the clients that connect to them. Normally a certificate is not required and this switch is optional.

**‘--certificate-type=*type*’ ¶**

Specify the type of the client certificate. Legal values are ‘PEM’ (assumed by default) and ‘DER’, also known as ‘ASN1’.

**‘--private-key=*file*’**

Read the private key from *file*. This allows you to provide the private key in a file separate from the certificate.

**‘--private-key-type=*type*’**

Specify the type of the private key. Accepted values are ‘PEM’ (the default) and ‘DER’.

**‘--ca-certificate=*file*’**

Use *file* as the file with the bundle of certificate authorities (“CA”) to verify the peers. The certificates must be in PEM format.

Without this option Wget looks for CA certificates at the system-specified locations, chosen at OpenSSL installation time.

**‘--ca-directory=*directory*’ ¶**

Specifies directory containing CA certificates in PEM format. Each file contains one CA certificate, and the file name is based on a hash value derived from the certificate. This is achieved by processing a certificate directory with the `c_rehash` utility supplied with OpenSSL. Using ‘--ca-directory’ is more efficient than ‘--ca-certificate’ when many certificates are installed because it allows Wget to fetch certificates on demand.

Without this option Wget looks for CA certificates at the system-specified locations, chosen at OpenSSL installation time.

**‘--crl-file=*file*’ ¶**

Specifies a CRL file in *file*. This is needed for certificates that have been revocated by the CAs.

**‘--pinnedpubkey=file/hashes’ ¶**

Tells wget to use the specified public key file (or hashes) to verify the peer. This can be a path to a file which contains a single public key in PEM or DER format, or any number of base64 encoded sha256 hashes preceded by “sha256//” and separated by “;”

When negotiating a TLS or SSL connection, the server sends a certificate indicating its identity. A public key is extracted from this certificate and if it does not exactly match the public key(s) provided to this option, wget will abort the connection before sending or receiving any data.

**‘--random-file=*file*’ ¶**

[OpenSSL and LibreSSL only] Use *file* as the source of random data for seeding the pseudo-random number generator on systems without /dev/urandom.

On such systems the SSL library needs an external source of randomness to initialize. Randomness may be provided by EGD (see ‘--egd-file’ below) or read from an external source specified by the user. If this option is not specified, Wget looks for random data in `$RANDFILE` or, if that is unset, in $HOME/.rnd.

If you’re getting the “Could not seed OpenSSL PRNG; disabling SSL.” error, you should provide random data using some of the methods described above.

**‘--egd-file=*file*’ ¶**

[OpenSSL only] Use *file* as the EGD socket. EGD stands for *Entropy Gathering Daemon*, a user-space program that collects data from various unpredictable system sources and makes it available to other programs that might need it. Encryption software, such as the SSL library, needs sources of non-repeating randomness to seed the random number generator used to produce cryptographically strong keys.

OpenSSL allows the user to specify his own source of entropy using the `RAND_FILE` environment variable. If this variable is unset, or if the specified file does not produce enough randomness, OpenSSL will read random data from EGD socket specified using this option.

If this option is not specified (and the equivalent startup command is not used), EGD is never contacted. EGD is not needed on modern Unix systems that support /dev/urandom.

**‘--no-hsts’ ¶**

Wget supports HSTS (HTTP Strict Transport Security, RFC 6797) by default. Use ‘--no-hsts’ to make Wget act as a non-HSTS-compliant UA. As a consequence, Wget would ignore all the `Strict-Transport-Security` headers, and would not enforce any existing HSTS policy.

**‘--hsts-file=*file*’**

By default, Wget stores its HSTS database in ~/.wget-hsts. You can use ‘--hsts-file’ to override this. Wget will use the supplied file as the HSTS database. Such file must conform to the correct HSTS database format used by Wget. If Wget cannot parse the provided file, the behaviour is unspecified.

The Wget’s HSTS database is a plain text file. Each line contains an HSTS entry (ie. a site that has issued a `Strict-Transport-Security` header and that therefore has specified a concrete HSTS policy to be applied). Lines starting with a dash (`#`) are ignored by Wget. Please note that in spite of this convenient human-readability hand-hacking the HSTS database is generally not a good idea.

An HSTS entry line consists of several fields separated by one or more whitespace:

`<hostname> SP [<port>] SP <include subdomains> SP <created> SP <max-age>`

The *hostname* and *port* fields indicate the hostname and port to which the given HSTS policy applies. The *port* field may be zero, and it will, in most of the cases. That means that the port number will not be taken into account when deciding whether such HSTS policy should be applied on a given request (only the hostname will be evaluated). When *port* is different to zero, both the target hostname and the port will be evaluated and the HSTS policy will only be applied if both of them match. This feature has been included for testing/development purposes only. The Wget testsuite (in testenv/) creates HSTS databases with explicit ports with the purpose of ensuring Wget’s correct behaviour. Applying HSTS policies to ports other than the default ones is discouraged by RFC 6797 (see Appendix B "Differences between HSTS Policy and Same-Origin Policy"). Thus, this functionality should not be used in production environments and *port* will typically be zero. The last three fields do what they are expected to. The field *include_subdomains* can either be `1` or `0` and it signals whether the subdomains of the target domain should be part of the given HSTS policy as well. The *created* and *max-age* fields hold the timestamp values of when such entry was created (first seen by Wget) and the HSTS-defined value ’max-age’, which states how long should that HSTS policy remain active, measured in seconds elapsed since the timestamp stored in *created*. Once that time has passed, that HSTS policy will no longer be valid and will eventually be removed from the database.

If you supply your own HSTS database via ‘--hsts-file’, be aware that Wget may modify the provided file if any change occurs between the HSTS policies requested by the remote servers and those in the file. When Wget exits, it effectively updates the HSTS database by rewriting the database file with the new entries.

If the supplied file does not exist, Wget will create one. This file will contain the new HSTS entries. If no HSTS entries were generated (no `Strict-Transport-Security` headers were sent by any of the servers) then no file will be created, not even an empty one. This behaviour applies to the default database file (~/.wget-hsts) as well: it will not be created until some server enforces an HSTS policy.

Care is taken not to override possible changes made by other Wget processes at the same time over the HSTS database. Before dumping the updated HSTS entries on the file, Wget will re-read it and merge the changes.

Using a custom HSTS database and/or modifying an existing one is discouraged. For more information about the potential security threats arose from such practice, see section 14 "Security Considerations" of RFC 6797, specially section 14.9 "Creative Manipulation of HSTS Policy Store".

**‘--warc-file=*file*’**

Use *file* as the destination WARC file.

**‘--warc-header=*string*’**

Use *string* into as the warcinfo record.

**‘--warc-max-size=*size*’**

Set the maximum size of the WARC files to *size*.

**‘--warc-cdx’**

Write CDX index files.

**‘--warc-dedup=*file*’**

Do not store records listed in this CDX file.

**‘--no-warc-compression’**

Do not compress WARC files with GZIP.

**‘--no-warc-digests’**

Do not calculate SHA1 digests.

**‘--no-warc-keep-log’**

Do not store the log file in a WARC record.

**‘--warc-tempdir=*dir*’**

Specify the location for temporary files created by the WARC writer.

### 2.9 FTP Options

**‘--ftp-user=*user*’ ¶**

**‘--ftp-password=*password*’**

Specify the username *user* and password *password* on an FTP server. Without this, or the corresponding startup option, the password defaults to ‘-wget@’, normally used for anonymous FTP.

Another way to specify username and password is in the URL itself (see URL Format). Either method reveals your password to anyone who bothers to run `ps`. To prevent the passwords from being seen, store them in .wgetrc or .netrc, and make sure to protect those files from other users with `chmod`. If the passwords are really important, do not leave them lying in those files either—edit the files and delete them after Wget has started the download.

**‘--no-remove-listing’ ¶**

Don’t remove the temporary .listing files generated by FTP retrievals. Normally, these files contain the raw directory listings received from FTP servers. Not removing them can be useful for debugging purposes, or when you want to be able to easily check on the contents of remote server directories (e.g. to verify that a mirror you’re running is complete).

Note that even though Wget writes to a known filename for this file, this is not a security hole in the scenario of a user making .listing a symbolic link to /etc/passwd or something and asking `root` to run Wget in his or her directory. Depending on the options used, either Wget will refuse to write to .listing, making the globbing/recursion/time-stamping operation fail, or the symbolic link will be deleted and replaced with the actual .listing file, or the listing will be written to a .listing.*number* file.

Even though this situation isn’t a problem, though, `root` should never run Wget in a non-trusted user’s directory. A user could do something as simple as linking index.html to /etc/passwd and asking `root` to run Wget with ‘-N’ or ‘-r’ so the file will be overwritten.

**‘--no-glob’ ¶**

Turn off FTP globbing. Globbing refers to the use of shell-like special characters (*wildcards*), like ‘*’, ‘?’, ‘[’ and ‘]’ to retrieve more than one file from the same directory at once, like:

```
wget ftp://gnjilux.srk.fer.hr/*.msg
```

By default, globbing will be turned on if the URL contains a globbing character. This option may be used to turn globbing on or off permanently.

You may have to quote the URL to protect it from being expanded by your shell. Globbing makes Wget look for a directory listing, which is system-specific. This is why it currently works only with Unix FTP servers (and the ones emulating Unix `ls` output).

**‘--no-passive-ftp’ ¶**

Disable the use of the *passive* FTP transfer mode. Passive FTP mandates that the client connect to the server to establish the data connection rather than the other way around.

If the machine is connected to the Internet directly, both passive and active FTP should work equally well. Behind most firewall and NAT configurations passive FTP has a better chance of working. However, in some rare firewall configurations, active FTP actually works when passive FTP doesn’t. If you suspect this to be the case, use this option, or set `passive_ftp=off` in your init file.

**‘--preserve-permissions’ ¶**

Preserve remote file permissions instead of permissions set by umask.

**‘--retr-symlinks’ ¶**

By default, when retrieving FTP directories recursively and a symbolic link is encountered, the symbolic link is traversed and the pointed-to files are retrieved. Currently, Wget does not traverse symbolic links to directories to download them recursively, though this feature may be added in the future.

When ‘--retr-symlinks=no’ is specified, the linked-to file is not downloaded. Instead, a matching symbolic link is created on the local file system. The pointed-to file will not be retrieved unless this recursive retrieval would have encountered it separately and downloaded it anyway. This option poses a security risk where a malicious FTP Server may cause Wget to write to files outside of the intended directories through a specially crafted .LISTING file.

Note that when retrieving a file (not a directory) because it was specified on the command-line, rather than because it was recursed to, this option has no effect. Symbolic links are always traversed in this case.

### 2.10 FTPS Options

**‘--ftps-implicit’**

This option tells Wget to use FTPS implicitly. Implicit FTPS consists of initializing SSL/TLS from the very beginning of the control connection. This option does not send an `AUTH TLS` command: it assumes the server speaks FTPS and directly starts an SSL/TLS connection. If the attempt is successful, the session continues just like regular FTPS (`PBSZ` and `PROT` are sent, etc.). Implicit FTPS is no longer a requirement for FTPS implementations, and thus many servers may not support it. If ‘--ftps-implicit’ is passed and no explicit port number specified, the default port for implicit FTPS, 990, will be used, instead of the default port for the "normal" (explicit) FTPS which is the same as that of FTP, 21.

**‘--no-ftps-resume-ssl’**

Do not resume the SSL/TLS session in the data channel. When starting a data connection, Wget tries to resume the SSL/TLS session previously started in the control connection. SSL/TLS session resumption avoids performing an entirely new handshake by reusing the SSL/TLS parameters of a previous session. Typically, the FTPS servers want it that way, so Wget does this by default. Under rare circumstances however, one might want to start an entirely new SSL/TLS session in every data connection. This is what ‘--no-ftps-resume-ssl’ is for.

**‘--ftps-clear-data-connection’**

All the data connections will be in plain text. Only the control connection will be under SSL/TLS. Wget will send a `PROT C` command to achieve this, which must be approved by the server.

**‘--ftps-fallback-to-ftp’**

Fall back to FTP if FTPS is not supported by the target server. For security reasons, this option is not asserted by default. The default behaviour is to exit with an error. If a server does not successfully reply to the initial `AUTH TLS` command, or in the case of implicit FTPS, if the initial SSL/TLS connection attempt is rejected, it is considered that such server does not support FTPS.

### 2.11 Recursive Retrieval Options

**‘-r’**

**‘--recursive’**

Turn on recursive retrieving. See Recursive Download, for more details. The default maximum depth is 5.

**‘-l *depth*’**

**‘--level=*depth*’**

Set the maximum number of subdirectories that Wget will recurse into to *depth*. In order to prevent one from accidentally downloading very large websites when using recursion this is limited to a depth of 5 by default, i.e., it will traverse at most 5 directories deep starting from the provided URL. Set ‘-l 0’ or ‘-l inf’ for infinite recursion depth.

```
wget -r -l 0 http://site/1.html
```

Ideally, one would expect this to download just 1.html. but unfortunately this is not the case, because ‘-l 0’ is equivalent to ‘-l inf’—that is, infinite recursion. To download a single HTML page (or a handful of them), specify them all on the command line and leave away ‘-r’ and ‘-l’. To download the essential items to view a single HTML page, see ‘page requisites’.

**‘--delete-after’ ¶**

This option tells Wget to delete every single file it downloads, *after* having done so. It is useful for pre-fetching popular pages through a proxy, e.g.:

```
wget -r -nd --delete-after http://whatever.com/~popular/page/
```

The ‘-r’ option is to retrieve recursively, and ‘-nd’ to not create directories.

Note that ‘--delete-after’ deletes files on the local machine. It does not issue the ‘DELE’ command to remote FTP sites, for instance. Also note that when ‘--delete-after’ is specified, ‘--convert-links’ is ignored, so ‘.orig’ files are simply not created in the first place.

**‘-k’ ¶**

**‘--convert-links’**

After the download is complete, convert the links in the document to make them suitable for local viewing. This affects not only the visible hyperlinks, but any part of the document that links to external content, such as embedded images, links to style sheets, hyperlinks to non-HTML content, etc.

Each link will be changed in one of the two ways:

- The links to files that have been downloaded by Wget will be changed to refer to the file they point to as a relative link. Example: if the downloaded file /foo/doc.html links to /bar/img.gif, also downloaded, then the link in doc.html will be modified to point to ‘../bar/img.gif’. This kind of transformation works reliably for arbitrary combinations of directories.
- The links to files that have not been downloaded by Wget will be changed to include host name and absolute path of the location they point to. Example: if the downloaded file /foo/doc.html links to /bar/img.gif (or to ../bar/img.gif), then the link in doc.html will be modified to point to http://*hostname*/bar/img.gif.

Because of this, local browsing works reliably: if a linked file was downloaded, the link will refer to its local name; if it was not downloaded, the link will refer to its full Internet address rather than presenting a broken link. The fact that the former links are converted to relative links ensures that you can move the downloaded hierarchy to another directory.

Note that only at the end of the download can Wget know which links have been downloaded. Because of that, the work done by ‘-k’ will be performed at the end of all the downloads.

**‘--convert-file-only’**

This option converts only the filename part of the URLs, leaving the rest of the URLs untouched. This filename part is sometimes referred to as the "basename", although we avoid that term here in order not to cause confusion.

It works particularly well in conjunction with ‘--adjust-extension’, although this coupling is not enforced. It proves useful to populate Internet caches with files downloaded from different hosts.

Example: if some link points to //foo.com/bar.cgi?xyz with ‘--adjust-extension’ asserted and its local destination is intended to be ./foo.com/bar.cgi?xyz.css, then the link would be converted to //foo.com/bar.cgi?xyz.css. Note that only the filename part has been modified. The rest of the URL has been left untouched, including the net path (`//`) which would otherwise be processed by Wget and converted to the effective scheme (ie. `http://`).

**‘-K’ ¶**

**‘--backup-converted’**

When converting a file, back up the original version with a ‘.orig’ suffix. Affects the behavior of ‘-N’ (see HTTP Time-Stamping Internals).

**‘-m’**

**‘--mirror’**

Turn on options suitable for mirroring. This option turns on recursion and time-stamping, sets infinite recursion depth and keeps FTP directory listings. It is currently equivalent to ‘-r -N -l inf --no-remove-listing’.

**‘-p’ ¶**

**‘--page-requisites’**

This option causes Wget to download all the files that are necessary to properly display a given HTML page. This includes such things as inlined images, sounds, and referenced stylesheets.

Ordinarily, when downloading a single HTML page, any requisite documents that may be needed to display it properly are not downloaded. Using ‘-r’ together with ‘-l’ can help, but since Wget does not ordinarily distinguish between external and inlined documents, one is generally left with “leaf documents” that are missing their requisites.

For instance, say document 1.html contains an `<IMG>` tag referencing 1.gif and an `<A>` tag pointing to external document 2.html. Say that 2.html is similar but that its image is 2.gif and it links to 3.html. Say this continues up to some arbitrarily high number.

If one executes the command:

```
wget -r -l 2 http://site/1.html
```

then 1.html, 1.gif, 2.html, 2.gif, and 3.html will be downloaded. As you can see, 3.html is without its requisite 3.gif because Wget is simply counting the number of hops (up to 2) away from 1.html in order to determine where to stop the recursion. However, with this command:

```
wget -r -l 2 -p http://site/1.html
```

all the above files *and* 3.html’s requisite 3.gif will be downloaded. Similarly,

```
wget -r -l 1 -p http://site/1.html
```

will cause 1.html, 1.gif, 2.html, and 2.gif to be downloaded. One might think that:

```
wget -r -l 0 -p http://site/1.html
```

would download just 1.html and 1.gif, but unfortunately this is not the case, because ‘-l 0’ is equivalent to ‘-l inf’—that is, infinite recursion. To download a single HTML page (or a handful of them, all specified on the command-line or in a ‘-i’ URL input file) and its (or their) requisites, simply leave off ‘-r’ and ‘-l’:

```
wget -p http://site/1.html
```

Note that Wget will behave as if ‘-r’ had been specified, but only that single page and its requisites will be downloaded. Links from that page to external documents will not be followed. Actually, to download a single page and all its requisites (even if they exist on separate websites), and make sure the lot displays properly locally, this author likes to use a few options in addition to ‘-p’:

```
wget -E -H -k -K -p http://site/document
```

To finish off this topic, it’s worth knowing that Wget’s idea of an external document link is any URL specified in an `<A>` tag, an `<AREA>` tag, or a `<LINK>` tag other than `<LINK REL="stylesheet">`.

**‘--strict-comments’ ¶**

Turn on strict parsing of HTML comments. The default is to terminate comments at the first occurrence of ‘-->’.

According to specifications, HTML comments are expressed as SGML *declarations*. Declaration is special markup that begins with ‘<!’ and ends with ‘>’, such as ‘<!DOCTYPE ...>’, that may contain comments between a pair of ‘--’ delimiters. HTML comments are “empty declarations”, SGML declarations without any non-comment text. Therefore, ‘<!--foo-->’ is a valid comment, and so is ‘<!--one-- --two-->’, but ‘<!--1--2-->’ is not.

On the other hand, most HTML writers don’t perceive comments as anything other than text delimited with ‘<!--’ and ‘-->’, which is not quite the same. For example, something like ‘<!------------>’ works as a valid comment as long as the number of dashes is a multiple of four (!). If not, the comment technically lasts until the next ‘--’, which may be at the other end of the document. Because of this, many popular browsers completely ignore the specification and implement what users have come to expect: comments delimited with ‘<!--’ and ‘-->’.

Until version 1.9, Wget interpreted comments strictly, which resulted in missing links in many web pages that displayed fine in browsers, but had the misfortune of containing non-compliant comments. Beginning with version 1.9, Wget has joined the ranks of clients that implements “naive” comments, terminating each comment at the first occurrence of ‘-->’.

If, for whatever reason, you want strict comment parsing, use this option to turn it on.

### 2.12 Recursive Accept/Reject Options

**‘-A *acclist* --accept *acclist*’**

**‘-R *rejlist* --reject *rejlist*’**

Specify comma-separated lists of file name suffixes or patterns to accept or reject (see Types of Files). Note that if any of the wildcard characters, ‘*’, ‘?’, ‘[’ or ‘]’, appear in an element of *acclist* or *rejlist*, it will be treated as a pattern, rather than a suffix. In this case, you have to enclose the pattern into quotes to prevent your shell from expanding it, like in ‘-A "*.mp3"’ or ‘-A '*.mp3'’.

**‘--accept-regex *urlregex*’**

**‘--reject-regex *urlregex*’**

Specify a regular expression to accept or reject the complete URL.

**‘--regex-type *regextype*’**

Specify the regular expression type. Possible types are ‘posix’ or ‘pcre’. Note that to be able to use ‘pcre’ type, wget has to be compiled with libpcre support.

**‘-D *domain-list*’**

**‘--domains=*domain-list*’**

Set domains to be followed. *domain-list* is a comma-separated list of domains. Note that it does *not* turn on ‘-H’.

**‘--exclude-domains *domain-list*’**

Specify the domains that are *not* to be followed (see Spanning Hosts).

**‘--follow-ftp’ ¶**

Follow FTP links from HTML documents. Without this option, Wget will ignore all the FTP links.

**‘--follow-tags=*list*’ ¶**

Wget has an internal table of HTML tag / attribute pairs that it considers when looking for linked documents during a recursive retrieval. If a user wants only a subset of those tags to be considered, however, he or she should be specify such tags in a comma-separated *list* with this option.

**‘--ignore-tags=*list*’**

This is the opposite of the ‘--follow-tags’ option. To skip certain HTML tags when recursively looking for documents to download, specify them in a comma-separated *list*.

In the past, this option was the best bet for downloading a single page and its requisites, using a command-line like:

```
wget --ignore-tags=a,area -H -k -K -r http://site/document
```

However, the author of this option came across a page with tags like `<LINK REL="home" HREF="/">` and came to the realization that specifying tags to ignore was not enough. One can’t just tell Wget to ignore `<LINK>`, because then stylesheets will not be downloaded. Now the best bet for downloading a single page and its requisites is the dedicated ‘--page-requisites’ option.

**‘--ignore-case’ ¶**

Ignore case when matching files and directories. This influences the behavior of -R, -A, -I, and -X options, as well as globbing implemented when downloading from FTP sites. For example, with this option, ‘-A "*.txt"’ will match ‘file1.txt’, but also ‘file2.TXT’, ‘file3.TxT’, and so on. The quotes in the example are to prevent the shell from expanding the pattern.

**‘-H’**

**‘--span-hosts’**

Enable spanning across hosts when doing recursive retrieving (see Spanning Hosts).

**‘-L’**

**‘--relative’**

Follow relative links only. Useful for retrieving a specific home page without any distractions, not even those from the same hosts (see Relative Links).

**‘-I *list*’**

**‘--include-directories=*list*’**

Specify a comma-separated list of directories you wish to follow when downloading (see Directory-Based Limits). Elements of *list* may contain wildcards.

**‘-X *list*’**

**‘--exclude-directories=*list*’**

Specify a comma-separated list of directories you wish to exclude from download (see Directory-Based Limits). Elements of *list* may contain wildcards.

**‘-np’**

**‘--no-parent’**

Do not ever ascend to the parent directory when retrieving recursively. This is a useful option, since it guarantees that only the files *below* a certain hierarchy will be downloaded. See Directory-Based Limits, for more details.

### 2.13 Exit Status

Wget may return one of several error codes if it encounters problems.

**0**

No problems occurred.

**1**

Generic error code.

**2**

Parse error—for instance, when parsing command-line options, the ‘.wgetrc’ or ‘.netrc’...

**3**

File I/O error.

**4**

Network failure.

**5**

SSL verification failure.

**6**

Username/password authentication failure.

**7**

Protocol errors.

**8**

Server issued an error response.

With the exceptions of 0 and 1, the lower-numbered exit codes take precedence over higher-numbered ones, when multiple types of errors are encountered.

In versions of Wget prior to 1.12, Wget’s exit status tended to be unhelpful and inconsistent. Recursive downloads would virtually always return 0 (success), regardless of any issues encountered, and non-recursive fetches only returned the status corresponding to the most recently-attempted download.
