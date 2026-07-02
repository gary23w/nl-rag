---
title: "GNU Wget 1.25.0 Manual (part 2/6)"
source: https://www.gnu.org/software/wget/manual/wget.html
domain: wget
license: CC-BY-SA-4.0
tags: wget download, file download, recursive download, command-line http
fetched: 2026-07-02
part: 2/6
---

## 2 Invoking

By default, Wget is very simple to invoke. The basic syntax is:

```
wget [option]... [URL]...
```

Wget will simply download all the URLs specified on the command line. *URL* is a *Uniform Resource Locator*, as defined below.

However, you may wish to change some of the default parameters of Wget. You can do it two ways: permanently, adding the appropriate command to .wgetrc (see Startup File), or specifying it on the command line.

### 2.1 URL Format

*URL* is an acronym for Uniform Resource Locator. A uniform resource locator is a compact string representation for a resource available via the Internet. Wget recognizes the URL syntax as per RFC1738. This is the most widely used form (square brackets denote optional parts):

```
http://host[:port]/directory/file
ftp://host[:port]/directory/file
```

You can also encode your username and password within a URL:

```
ftp://user:password@host/path
http://user:password@host/path
```

Either *user* or *password*, or both, may be left out. If you leave out either the HTTP username or password, no authentication will be sent. If you leave out the FTP username, ‘anonymous’ will be used. If you leave out the FTP password, your email address will be supplied as a default password.1

**Important Note**: if you specify a password-containing URL on the command line, the username and password will be plainly visible to all users on the system, by way of `ps`. On multi-user systems, this is a big security risk. To work around it, use `wget -i -` and feed the URLs to Wget’s standard input, each on a separate line, terminated by C-d.

You can encode unsafe characters in a URL as ‘%xy’, `xy` being the hexadecimal representation of the character’s ASCII value. Some common unsafe characters include ‘%’ (quoted as ‘%25’), ‘:’ (quoted as ‘%3A’), and ‘@’ (quoted as ‘%40’). Refer to RFC1738 for a comprehensive list of unsafe characters.

Wget also supports the `type` feature for FTP URLs. By default, FTP documents are retrieved in the binary mode (type ‘i’), which means that they are downloaded unchanged. Another useful mode is the ‘a’ (*ASCII*) mode, which converts the line delimiters between the different operating systems, and is thus useful for text files. Here is an example:

```
ftp://host/directory/file;type=a
```

The two alternative variants of URL specifications are no longer supported because of security considerations:

FTP-only syntax (supported by `NcFTP`):

```
host:/dir/file
```

HTTP-only syntax (introduced by `Netscape`):

```
host[:port]/dir/file
```

These two alternative forms have been deprecated long time ago, and support is removed with version 1.22.0.

### 2.2 Option Syntax

Since Wget uses GNU getopt to process command-line arguments, every option has a long form along with the short one. Long options are more convenient to remember, but take time to type. You may freely mix different option styles, or specify options after the command-line arguments. Thus you may write:

```
wget -r --tries=10 http://fly.srk.fer.hr/ -o log
```

The space between the option accepting an argument and the argument may be omitted. Instead of ‘-o log’ you can write ‘-olog’.

You may put several options that do not require arguments together, like:

```
wget -drc URL
```

This is completely equivalent to:

```
wget -d -r -c URL
```

Since the options can be specified after the arguments, you may terminate them with ‘--’. So the following will try to download URL ‘-x’, reporting failure to log:

```
wget -o log -- -x
```

The options that accept comma-separated lists all respect the convention that specifying an empty list clears its value. This can be useful to clear the .wgetrc settings. For instance, if your .wgetrc sets `exclude_directories` to /cgi-bin, the following example will first reset it, and then set it to exclude /~nobody and /~somebody. You can also clear the lists in .wgetrc (see Wgetrc Syntax).

```
wget -X "" -X /~nobody,/~somebody
```

Most options that do not accept arguments are *boolean* options, so named because their state can be captured with a yes-or-no (“boolean”) variable. For example, ‘--follow-ftp’ tells Wget to follow FTP links from HTML files and, on the other hand, ‘--no-glob’ tells it not to perform file globbing on FTP URLs. A boolean option is either *affirmative* or *negative* (beginning with ‘--no’). All such options share several properties.

Unless stated otherwise, it is assumed that the default behavior is the opposite of what the option accomplishes. For example, the documented existence of ‘--follow-ftp’ assumes that the default is to *not* follow FTP links from HTML pages.

Affirmative options can be negated by prepending the ‘--no-’ to the option name; negative options can be negated by omitting the ‘--no-’ prefix. This might seem superfluous—if the default for an affirmative option is to not do something, then why provide a way to explicitly turn it off? But the startup file may in fact change the default. For instance, using `follow_ftp = on` in .wgetrc makes Wget *follow* FTP links by default, and using ‘--no-follow-ftp’ is the only way to restore the factory default from the command line.

### 2.3 Basic Startup Options

**‘-V’**

**‘--version’**

Display the version of Wget.

**‘-h’**

**‘--help’**

Print a help message describing all of Wget’s command-line options.

**‘-b’**

**‘--background’**

Go to background immediately after startup. If no output file is specified via the ‘-o’, output is redirected to wget-log.

**‘-e *command*’ ¶**

**‘--execute *command*’**

Execute *command* as if it were a part of .wgetrc (see Startup File). A command thus invoked will be executed *after* the commands in .wgetrc, thus taking precedence over them. If you need to specify more than one wgetrc command, use multiple instances of ‘-e’.

### 2.4 Logging and Input File Options

**‘-o *logfile*’ ¶**

**‘--output-file=*logfile*’**

Log all messages to *logfile*. The messages are normally reported to standard error.

**‘-a *logfile*’ ¶**

**‘--append-output=*logfile*’**

Append to *logfile*. This is the same as ‘-o’, only it appends to *logfile* instead of overwriting the old log file. If *logfile* does not exist, a new file is created.

**‘-d’ ¶**

**‘--debug’**

Turn on debug output, meaning various information important to the developers of Wget if it does not work properly. Your system administrator may have chosen to compile Wget without debug support, in which case ‘-d’ will not work. Please note that compiling with debug support is always safe—Wget compiled with the debug support will *not* print any debug info unless requested with ‘-d’. See Reporting Bugs, for more information on how to use ‘-d’ for sending bug reports.

**‘-q’ ¶**

**‘--quiet’**

Turn off Wget’s output.

**‘-v’ ¶**

**‘--verbose’**

Turn on verbose output, with all the available data. The default output is verbose.

**‘-nv’**

**‘--no-verbose’**

Turn off verbose without being completely quiet (use ‘-q’ for that), which means that error messages and basic information still get printed.

**‘--report-speed=*type*’**

Output bandwidth as *type*. The only accepted value is ‘bits’.

**‘-i *file*’ ¶**

**‘--input-file=*file*’**

Read URLs from a local or external *file*. If ‘-’ is specified as *file*, URLs are read from the standard input. (Use ‘./-’ to read from a file literally named ‘-’.)

If this function is used, no URLs need be present on the command line. If there are URLs both on the command line and in an input file, those on the command lines will be the first ones to be retrieved. If ‘--force-html’ is not specified, then *file* should consist of a series of URLs, one per line.

However, if you specify ‘--force-html’, the document will be regarded as ‘html’. In that case you may have problems with relative links, which you can solve either by adding `<base href="*url*">` to the documents or by specifying ‘--base=*url*’ on the command line.

If the *file* is an external one, the document will be automatically treated as ‘html’ if the Content-Type matches ‘text/html’. Furthermore, the *file*’s location will be implicitly used as base href if none was specified.

If the *file* is a local file, on systems that support it, it will be opened with the `O_NONBLOCK` flag to allow non-blocking reads from the file. ‘Wget’ will attempt to continue reading from the file until EOF is reached or it is closed. This allows one to stream a list of files for retrieval where the list is dynamically generated during the execution of the process. Currently, this feature is not available on Windows platforms.

**‘--input-metalink=*file*’ ¶**

Downloads files covered in local Metalink *file*. Metalink version 3 and 4 are supported.

**‘--keep-badhash’ ¶**

Keeps downloaded Metalink’s files with a bad hash. It appends .badhash to the name of Metalink’s files which have a checksum mismatch, except without overwriting existing files.

**‘--metalink-over-http’ ¶**

Issues HTTP HEAD request instead of GET and extracts Metalink metadata from response headers. Then it switches to Metalink download. If no valid Metalink metadata is found, it falls back to ordinary HTTP download. Enables ‘Content-Type: application/metalink4+xml’ files download/processing.

**‘--metalink-index=*number*’ ¶**

Set the Metalink ‘application/metalink4+xml’ metaurl ordinal NUMBER. From 1 to the total number of “application/metalink4+xml” available. Specify 0 or ‘inf’ to choose the first good one. Metaurls, such as those from a ‘--metalink-over-http’, may have been sorted by priority key’s value; keep this in mind to choose the right NUMBER.

**‘--preferred-location’ ¶**

Set preferred location for Metalink resources. This has effect if multiple resources with same priority are available.

**‘--xattr’ ¶**

Enable use of file system’s extended attributes to save the original URL and the Referer HTTP header value if used.

Be aware that the URL might contain private information like access tokens or credentials.

**‘-F’ ¶**

**‘--force-html’**

When input is read from a file, force it to be treated as an HTML file. This enables you to retrieve relative links from existing HTML files on your local disk, by adding `<base href="*url*">` to HTML, or using the ‘--base’ command-line option.

**‘-B *URL*’ ¶**

**‘--base=*URL*’**

Resolves relative links using *URL* as the point of reference, when reading links from an HTML file specified via the ‘-i’/‘--input-file’ option (together with ‘--force-html’, or when the input file was fetched remotely from a server describing it as HTML). This is equivalent to the presence of a `BASE` tag in the HTML input file, with *URL* as the value for the `href` attribute.

For instance, if you specify ‘http://foo/bar/a.html’ for *URL*, and Wget reads ‘../baz/b.html’ from the input file, it would be resolved to ‘http://foo/baz/b.html’.

**‘--config=*FILE*’ ¶**

Specify the location of a startup file you wish to use instead of the default one(s). Use –no-config to disable reading of config files. If both –config and –no-config are given, –no-config is ignored.

**‘--rejected-log=*logfile*’**

Logs all URL rejections to *logfile* as comma separated values. The values include the reason of rejection, the URL and the parent URL it was found in.

### 2.5 Download Options

**‘--bind-address=*ADDRESS*’ ¶**

When making client TCP/IP connections, bind to *ADDRESS* on the local machine. *ADDRESS* may be specified as a hostname or IP address. This option can be useful if your machine is bound to multiple IPs.

**‘--bind-dns-address=*ADDRESS*’ ¶**

[libcares only] This address overrides the route for DNS requests. If you ever need to circumvent the standard settings from /etc/resolv.conf, this option together with ‘--dns-servers’ is your friend. *ADDRESS* must be specified either as IPv4 or IPv6 address. Wget needs to be built with libcares for this option to be available.

**‘--dns-servers=*ADDRESSES*’ ¶**

[libcares only] The given address(es) override the standard nameserver addresses, e.g. as configured in /etc/resolv.conf. *ADDRESSES* may be specified either as IPv4 or IPv6 addresses, comma-separated. Wget needs to be built with libcares for this option to be available.

**‘-t *number*’ ¶**

**‘--tries=*number*’**

Set number of tries to *number*. Specify 0 or ‘inf’ for infinite retrying. The default is to retry 20 times, with the exception of fatal errors like “connection refused” or “not found” (404), which are not retried.

**‘-O *file*’**

**‘--output-document=*file*’**

The documents will not be written to the appropriate files, but all will be concatenated together and written to *file*. If ‘-’ is used as *file*, documents will be printed to standard output, disabling link conversion. (Use ‘./-’ to print to a file literally named ‘-’.)

Use of ‘-O’ is *not* intended to mean simply “use the name *file* instead of the one in the URL;” rather, it is analogous to shell redirection: ‘wget -O file http://foo’ is intended to work like ‘wget -O - http://foo > file’; file will be truncated immediately, and *all* downloaded content will be written there.

For this reason, ‘-N’ (for timestamp-checking) is not supported in combination with ‘-O’: since *file* is always newly created, it will always have a very new timestamp. A warning will be issued if this combination is used.

Similarly, using ‘-r’ or ‘-p’ with ‘-O’ may not work as you expect: Wget won’t just download the first file to *file* and then download the rest to their normal names: *all* downloaded content will be placed in *file*. This was disabled in version 1.11, but has been reinstated (with a warning) in 1.11.2, as there are some cases where this behavior can actually have some use.

A combination with ‘-nc’ is only accepted if the given output file does not exist.

Note that a combination with ‘-k’ is only permitted when downloading a single document, as in that case it will just convert all relative URIs to external ones; ‘-k’ makes no sense for multiple URIs when they’re all being downloaded to a single file; ‘-k’ can be used only when the output is a regular file.

**‘-nc’ ¶**

**‘--no-clobber’**

If a file is downloaded more than once in the same directory, Wget’s behavior depends on a few options, including ‘-nc’. In certain cases, the local file will be *clobbered*, or overwritten, upon repeated download. In other cases it will be preserved.

When running Wget without ‘-N’, ‘-nc’, ‘-r’, or ‘-p’, downloading the same file in the same directory will result in the original copy of *file* being preserved and the second copy being named ‘*file*.1’. If that file is downloaded yet again, the third copy will be named ‘*file*.2’, and so on. (This is also the behavior with ‘-nd’, even if ‘-r’ or ‘-p’ are in effect.) When ‘-nc’ is specified, this behavior is suppressed, and Wget will refuse to download newer copies of ‘*file*’. Therefore, “`no-clobber`” is actually a misnomer in this mode—it’s not clobbering that’s prevented (as the numeric suffixes were already preventing clobbering), but rather the multiple version saving that’s prevented.

When running Wget with ‘-r’ or ‘-p’, but without ‘-N’, ‘-nd’, or ‘-nc’, re-downloading a file will result in the new copy simply overwriting the old. Adding ‘-nc’ will prevent this behavior, instead causing the original version to be preserved and any newer copies on the server to be ignored.

When running Wget with ‘-N’, with or without ‘-r’ or ‘-p’, the decision as to whether or not to download a newer copy of a file depends on the local and remote timestamp and size of the file (see Time-Stamping). ‘-nc’ may not be specified at the same time as ‘-N’.

A combination with ‘-O’/‘--output-document’ is only accepted if the given output file does not exist.

Note that when ‘-nc’ is specified, files with the suffixes ‘.html’ or ‘.htm’ will be loaded from the local disk and parsed as if they had been retrieved from the Web.

**‘--backups=*backups*’ ¶**

Before (over)writing a file, back up an existing file by adding a ‘.1’ suffix (‘_1’ on VMS) to the file name. Such backup files are rotated to ‘.2’, ‘.3’, and so on, up to *backups* (and lost beyond that).

**‘--no-netrc’ ¶**

Do not try to obtain credentials from .netrc file. By default .netrc file is searched for credentials in case none have been passed on command line and authentication is required.

**‘-c’ ¶**

**‘--continue’**

Continue getting a partially-downloaded file. This is useful when you want to finish up a download started by a previous instance of Wget, or by another program. For instance:

```
wget -c ftp://sunsite.doc.ic.ac.uk/ls-lR.Z
```

If there is a file named ls-lR.Z in the current directory, Wget will assume that it is the first portion of the remote file, and will ask the server to continue the retrieval from an offset equal to the length of the local file.

Note that you don’t need to specify this option if you just want the current invocation of Wget to retry downloading a file should the connection be lost midway through. This is the default behavior. ‘-c’ only affects resumption of downloads started *prior* to this invocation of Wget, and whose local files are still sitting around.

Without ‘-c’, the previous example would just download the remote file to ls-lR.Z.1, leaving the truncated ls-lR.Z file alone.

If you use ‘-c’ on a non-empty file, and the server does not support continued downloading, Wget will restart the download from scratch and overwrite the existing file entirely.

Beginning with Wget 1.7, if you use ‘-c’ on a file which is of equal size as the one on the server, Wget will refuse to download the file and print an explanatory message. The same happens when the file is smaller on the server than locally (presumably because it was changed on the server since your last download attempt)—because “continuing” is not meaningful, no download occurs.

On the other side of the coin, while using ‘-c’, any file that’s bigger on the server than locally will be considered an incomplete download and only `(length(remote) - length(local))` bytes will be downloaded and tacked onto the end of the local file. This behavior can be desirable in certain cases—for instance, you can use ‘wget -c’ to download just the new portion that’s been appended to a data collection or log file.

However, if the file is bigger on the server because it’s been *changed*, as opposed to just *appended* to, you’ll end up with a garbled file. Wget has no way of verifying that the local file is really a valid prefix of the remote file. You need to be especially careful of this when using ‘-c’ in conjunction with ‘-r’, since every file will be considered as an "incomplete download" candidate.

Another instance where you’ll get a garbled file if you try to use ‘-c’ is if you have a lame HTTP proxy that inserts a “transfer interrupted” string into the local file. In the future a “rollback” option may be added to deal with this case.

Note that ‘-c’ only works with FTP servers and with HTTP servers that support the `Range` header.

**‘--start-pos=*OFFSET*’ ¶**

Start downloading at zero-based position *OFFSET*. Offset may be expressed in bytes, kilobytes with the ‘k’ suffix, or megabytes with the ‘m’ suffix, etc.

‘--start-pos’ has higher precedence over ‘--continue’. When ‘--start-pos’ and ‘--continue’ are both specified, wget will emit a warning then proceed as if ‘--continue’ was absent.

Server support for continued download is required, otherwise ‘--start-pos’ cannot help. See ‘-c’ for details.

**‘--progress=*type*’ ¶**

Select the type of the progress indicator you wish to use. Legal indicators are “dot” and “bar”.

The “bar” indicator is used by default. It draws an ASCII progress bar graphics (a.k.a “thermometer” display) indicating the status of retrieval. If the output is not a TTY, the “dot” bar will be used by default.

Use ‘--progress=dot’ to switch to the “dot” display. It traces the retrieval by printing dots on the screen, each dot representing a fixed amount of downloaded data.

The progress *type* can also take one or more parameters. The parameters vary based on the *type* selected. Parameters to *type* are passed by appending them to the type sperated by a colon (:) like this: ‘--progress=*type*:*parameter1*:*parameter2*’.

When using the dotted retrieval, you may set the *style* by specifying the type as ‘dot:*style*’. Different styles assign different meaning to one dot. With the `default` style each dot represents 1K, there are ten dots in a cluster and 50 dots in a line. The `binary` style has a more “computer”-like orientation—8K dots, 16-dots clusters and 48 dots per line (which makes for 384K lines). The `mega` style is suitable for downloading large files—each dot represents 64K retrieved, there are eight dots in a cluster, and 48 dots on each line (so each line contains 3M). If `mega` is not enough then you can use the `giga` style—each dot represents 1M retrieved, there are eight dots in a cluster, and 32 dots on each line (so each line contains 32M).

With ‘--progress=bar’, there are currently two possible parameters, *force* and *noscroll*.

When the output is not a TTY, the progress bar always falls back to “dot”, even if ‘--progress=bar’ was passed to Wget during invocation. This behaviour can be overridden and the “bar” output forced by using the “force” parameter as ‘--progress=bar:force’.

By default, the ‘bar’ style progress bar scroll the name of the file from left to right for the file being downloaded if the filename exceeds the maximum length allotted for its display. In certain cases, such as with ‘--progress=bar:force’, one may not want the scrolling filename in the progress bar. By passing the “noscroll” parameter, Wget can be forced to display as much of the filename as possible without scrolling through it.

Note that you can set the default style using the `progress` command in .wgetrc. That setting may be overridden from the command line. For example, to force the bar output without scrolling, use ‘--progress=bar:force:noscroll’.

**‘--show-progress’**

Force wget to display the progress bar in any verbosity.

By default, wget only displays the progress bar in verbose mode. One may however, want wget to display the progress bar on screen in conjunction with any other verbosity modes like ‘--no-verbose’ or ‘--quiet’. This is often a desired a property when invoking wget to download several small/large files. In such a case, wget could simply be invoked with this parameter to get a much cleaner output on the screen.

This option will also force the progress bar to be printed to stderr when used alongside the ‘--output-file’ option.

**‘-N’**

**‘--timestamping’**

Turn on time-stamping. See Time-Stamping, for details.

**‘--no-if-modified-since’**

Do not send If-Modified-Since header in ‘-N’ mode. Send preliminary HEAD request instead. This has only effect in ‘-N’ mode.

**‘--no-use-server-timestamps’**

Don’t set the local file’s timestamp by the one on the server.

By default, when a file is downloaded, its timestamps are set to match those from the remote file. This allows the use of ‘--timestamping’ on subsequent invocations of wget. However, it is sometimes useful to base the local file’s timestamp on when it was actually downloaded; for that purpose, the ‘--no-use-server-timestamps’ option has been provided.

**‘-S’ ¶**

**‘--server-response’**

Print the headers sent by HTTP servers and responses sent by FTP servers.

**‘--spider’ ¶**

When invoked with this option, Wget will behave as a Web *spider*, which means that it will not download the pages, just check that they are there. For example, you can use Wget to check your bookmarks:

```
wget --spider --force-html -i bookmarks.html
```

This feature needs much more work for Wget to get close to the functionality of real web spiders.

**‘-T seconds’ ¶**

**‘--timeout=*seconds*’**

Set the network timeout to *seconds* seconds. This is equivalent to specifying ‘--dns-timeout’, ‘--connect-timeout’, and ‘--read-timeout’, all at the same time.

When interacting with the network, Wget can check for timeout and abort the operation if it takes too long. This prevents anomalies like hanging reads and infinite connects. The only timeout enabled by default is a 900-second read timeout. Setting a timeout to 0 disables it altogether. Unless you know what you are doing, it is best not to change the default timeout settings.

All timeout-related options accept decimal values, as well as subsecond values. For example, ‘0.1’ seconds is a legal (though unwise) choice of timeout. Subsecond timeouts are useful for checking server response times or for testing network latency.

**‘--dns-timeout=*seconds*’ ¶**

Set the DNS lookup timeout to *seconds* seconds. DNS lookups that don’t complete within the specified time will fail. By default, there is no timeout on DNS lookups, other than that implemented by system libraries.

**‘--connect-timeout=*seconds*’ ¶**

Set the connect timeout to *seconds* seconds. TCP connections that take longer to establish will be aborted. By default, there is no connect timeout, other than that implemented by system libraries.

**‘--read-timeout=*seconds*’ ¶**

Set the read (and write) timeout to *seconds* seconds. The “time” of this timeout refers to *idle time*: if, at any point in the download, no data is received for more than the specified number of seconds, reading fails and the download is restarted. This option does not directly affect the duration of the entire download.

Of course, the remote server may choose to terminate the connection sooner than this option requires. The default read timeout is 900 seconds.

**‘--limit-rate=*amount*’ ¶**

Limit the download speed to *amount* bytes per second. Amount may be expressed in bytes, kilobytes with the ‘k’ suffix, or megabytes with the ‘m’ suffix. For example, ‘--limit-rate=20k’ will limit the retrieval rate to 20KB/s. This is useful when, for whatever reason, you don’t want Wget to consume the entire available bandwidth.

This option allows the use of decimal numbers, usually in conjunction with power suffixes; for example, ‘--limit-rate=2.5k’ is a legal value.

Note that Wget implements the limiting by sleeping the appropriate amount of time after a network read that took less time than specified by the rate. Eventually this strategy causes the TCP transfer to slow down to approximately the specified rate. However, it may take some time for this balance to be achieved, so don’t be surprised if limiting the rate doesn’t work well with very small files.

**‘-w *seconds*’ ¶**

**‘--wait=*seconds*’**

Wait the specified number of seconds between the retrievals. Use of this option is recommended, as it lightens the server load by making the requests less frequent. Instead of in seconds, the time can be specified in minutes using the `m` suffix, in hours using `h` suffix, or in days using `d` suffix.

Specifying a large value for this option is useful if the network or the destination host is down, so that Wget can wait long enough to reasonably expect the network error to be fixed before the retry. The waiting interval specified by this function is influenced by `--random-wait`, which see.

**‘--waitretry=*seconds*’ ¶**

If you don’t want Wget to wait between *every* retrieval, but only between retries of failed downloads, you can use this option. Wget will use *linear backoff*, waiting 1 second after the first failure on a given file, then waiting 2 seconds after the second failure on that file, up to the maximum number of *seconds* you specify.

By default, Wget will assume a value of 10 seconds.

**‘--random-wait’ ¶**

Some web sites may perform log analysis to identify retrieval programs such as Wget by looking for statistically significant similarities in the time between requests. This option causes the time between requests to vary between 0.5 and 1.5 * *wait* seconds, where *wait* was specified using the ‘--wait’ option, in order to mask Wget’s presence from such analysis.

A 2001 article in a publication devoted to development on a popular consumer platform provided code to perform this analysis on the fly. Its author suggested blocking at the class C address level to ensure automated retrieval programs were blocked despite changing DHCP-supplied addresses.

The ‘--random-wait’ option was inspired by this ill-advised recommendation to block many unrelated users from a web site due to the actions of one.

**‘--no-proxy’ ¶**

Don’t use proxies, even if the appropriate `*_proxy` environment variable is defined.

See Proxies, for more information about the use of proxies with Wget.

**‘-Q *quota*’ ¶**

**‘--quota=*quota*’**

Specify download quota for automatic retrievals. The value can be specified in bytes (default), kilobytes (with ‘k’ suffix), or megabytes (with ‘m’ suffix).

Note that quota will never affect downloading a single file. So if you specify ‘wget -Q10k https://example.com/ls-lR.gz’, all of the ls-lR.gz will be downloaded. The same goes even when several URLs are specified on the command-line. The quota is checked only at the end of each downloaded file, so it will never result in a partially downloaded file. Thus you may safely type ‘wget -Q2m -i sites’—download will be aborted after the file that exhausts the quota is completely downloaded.

Setting quota to 0 or to ‘inf’ unlimits the download quota.

**‘--no-dns-cache’ ¶**

Turn off caching of DNS lookups. Normally, Wget remembers the IP addresses it looked up from DNS so it doesn’t have to repeatedly contact the DNS server for the same (typically small) set of hosts it retrieves from. This cache exists in memory only; a new Wget run will contact DNS again.

However, it has been reported that in some situations it is not desirable to cache host names, even for the duration of a short-running application like Wget. With this option Wget issues a new DNS lookup (more precisely, a new call to `gethostbyname` or `getaddrinfo`) each time it makes a new connection. Please note that this option will *not* affect caching that might be performed by the resolving library or by an external caching layer, such as NSCD.

If you don’t understand exactly what this option does, you probably won’t need it.

**‘--restrict-file-names=*modes*’ ¶**

Change which characters found in remote URLs must be escaped during generation of local filenames. Characters that are *restricted* by this option are escaped, i.e. replaced with ‘%HH’, where ‘HH’ is the hexadecimal number that corresponds to the restricted character. This option may also be used to force all alphabetical cases to be either lower- or uppercase.

By default, Wget escapes the characters that are not valid or safe as part of file names on your operating system, as well as control characters that are typically unprintable. This option is useful for changing these defaults, perhaps because you are downloading to a non-native partition, or because you want to disable escaping of the control characters, or you want to further restrict characters to only those in the ASCII range of values.

The *modes* are a comma-separated set of text values. The acceptable values are ‘unix’, ‘windows’, ‘nocontrol’, ‘ascii’, ‘lowercase’, and ‘uppercase’. The values ‘unix’ and ‘windows’ are mutually exclusive (one will override the other), as are ‘lowercase’ and ‘uppercase’. Those last are special cases, as they do not change the set of characters that would be escaped, but rather force local file paths to be converted either to lower- or uppercase.

When “unix” is specified, Wget escapes the character ‘/’ and the control characters in the ranges 0–31 and 128–159. This is the default on Unix-like operating systems.

When “windows” is given, Wget escapes the characters ‘\’, ‘|’, ‘/’, ‘:’, ‘?’, ‘"’, ‘*’, ‘<’, ‘>’, and the control characters in the ranges 0–31 and 128–159. In addition to this, Wget in Windows mode uses ‘+’ instead of ‘:’ to separate host and port in local file names, and uses ‘@’ instead of ‘?’ to separate the query portion of the file name from the rest. Therefore, a URL that would be saved as ‘www.xemacs.org:4300/search.pl?input=blah’ in Unix mode would be saved as ‘www.xemacs.org+4300/search.pl@input=blah’ in Windows mode. This mode is the default on Windows.

If you specify ‘nocontrol’, then the escaping of the control characters is also switched off. This option may make sense when you are downloading URLs whose names contain UTF-8 characters, on a system which can save and display filenames in UTF-8 (some possible byte values used in UTF-8 byte sequences fall in the range of values designated by Wget as “controls”).

The ‘ascii’ mode is used to specify that any bytes whose values are outside the range of ASCII characters (that is, greater than 127) shall be escaped. This can be useful when saving filenames whose encoding does not match the one used locally.

**‘-4’ ¶**

**‘--inet4-only’**

**‘-6’**

**‘--inet6-only’**

Force connecting to IPv4 or IPv6 addresses. With ‘--inet4-only’ or ‘-4’, Wget will only connect to IPv4 hosts, ignoring AAAA records in DNS, and refusing to connect to IPv6 addresses specified in URLs. Conversely, with ‘--inet6-only’ or ‘-6’, Wget will only connect to IPv6 hosts and ignore A records and IPv4 addresses.

Neither options should be needed normally. By default, an IPv6-aware Wget will use the address family specified by the host’s DNS record. If the DNS responds with both IPv4 and IPv6 addresses, Wget will try them in sequence until it finds one it can connect to. (Also see `--prefer-family` option described below.)

These options can be used to deliberately force the use of IPv4 or IPv6 address families on dual family systems, usually to aid debugging or to deal with broken network configuration. Only one of ‘--inet6-only’ and ‘--inet4-only’ may be specified at the same time. Neither option is available in Wget compiled without IPv6 support.

**‘--prefer-family=none/IPv4/IPv6’**

When given a choice of several addresses, connect to the addresses with specified address family first. The address order returned by DNS is used without change by default.

This avoids spurious errors and connect attempts when accessing hosts that resolve to both IPv6 and IPv4 addresses from IPv4 networks. For example, ‘www.kame.net’ resolves to ‘2001:200:0:8002:203:47ff:fea5:3085’ and to ‘203.178.141.194’. When the preferred family is `IPv4`, the IPv4 address is used first; when the preferred family is `IPv6`, the IPv6 address is used first; if the specified value is `none`, the address order returned by DNS is used without change.

Unlike ‘-4’ and ‘-6’, this option doesn’t inhibit access to any address family, it only changes the *order* in which the addresses are accessed. Also note that the reordering performed by this option is *stable*—it doesn’t affect order of addresses of the same family. That is, the relative order of all IPv4 addresses and of all IPv6 addresses remains intact in all cases.

**‘--retry-connrefused’**

Consider “connection refused” a transient error and try again. Normally Wget gives up on a URL when it is unable to connect to the site because failure to connect is taken as a sign that the server is not running at all and that retries would not help. This option is for mirroring unreliable sites whose servers tend to disappear for short periods of time.

**‘--user=*user*’ ¶**

**‘--password=*password*’**

Specify the username *user* and password *password* for both FTP and HTTP file retrieval. These parameters can be overridden using the ‘--ftp-user’ and ‘--ftp-password’ options for FTP connections and the ‘--http-user’ and ‘--http-password’ options for HTTP connections.

**‘--ask-password’**

Prompt for a password for each connection established. Cannot be specified when ‘--password’ is being used, because they are mutually exclusive.

**‘--use-askpass=*command*’**

Prompt for a user and password using the specified command. If no command is specified then the command in the environment variable WGET_ASKPASS is used. If WGET_ASKPASS is not set then the command in the environment variable SSH_ASKPASS is used.

You can set the default command for use-askpass in the .wgetrc. That setting may be overridden from the command line.

**‘--no-iri’ ¶**

Turn off internationalized URI (IRI) support. Use ‘--iri’ to turn it on. IRI support is activated by default.

You can set the default state of IRI support using the `iri` command in .wgetrc. That setting may be overridden from the command line.

**‘--local-encoding=*encoding*’ ¶**

Force Wget to use *encoding* as the default system encoding. That affects how Wget converts URLs specified as arguments from locale to UTF-8 for IRI support.

Wget use the function `nl_langinfo()` and then the `CHARSET` environment variable to get the locale. If it fails, ASCII is used.

You can set the default local encoding using the `local_encoding` command in .wgetrc. That setting may be overridden from the command line.

**‘--remote-encoding=*encoding*’ ¶**

Force Wget to use *encoding* as the default remote server encoding. That affects how Wget converts URIs found in files from remote encoding to UTF-8 during a recursive fetch. This options is only useful for IRI support, for the interpretation of non-ASCII characters.

For HTTP, remote encoding can be found in HTTP `Content-Type` header and in HTML `Content-Type http-equiv` meta tag.

You can set the default encoding using the `remoteencoding` command in .wgetrc. That setting may be overridden from the command line.

**‘--unlink’ ¶**

Force Wget to unlink file instead of clobbering existing file. This option is useful for downloading to the directory with hardlinks.

### 2.6 Directory Options

**‘-nd’**

**‘--no-directories’**

Do not create a hierarchy of directories when retrieving recursively. With this option turned on, all files will get saved to the current directory, without clobbering (if a name shows up more than once, the filenames will get extensions ‘.n’).

**‘-x’**

**‘--force-directories’**

The opposite of ‘-nd’—create a hierarchy of directories, even if one would not have been created otherwise. E.g. ‘wget -x http://fly.srk.fer.hr/robots.txt’ will save the downloaded file to fly.srk.fer.hr/robots.txt.

**‘-nH’**

**‘--no-host-directories’**

Disable generation of host-prefixed directories. By default, invoking Wget with ‘-r http://fly.srk.fer.hr/’ will create a structure of directories beginning with fly.srk.fer.hr/. This option disables such behavior.

**‘--protocol-directories’**

Use the protocol name as a directory component of local file names. For example, with this option, ‘wget -r http://*host*’ will save to ‘http/*host*/...’ rather than just to ‘*host*/...’.

**‘--cut-dirs=*number*’ ¶**

Ignore *number* directory components. This is useful for getting a fine-grained control over the directory where recursive retrieval will be saved.

Take, for example, the directory at ‘ftp://ftp.xemacs.org/pub/xemacs/’. If you retrieve it with ‘-r’, it will be saved locally under ftp.xemacs.org/pub/xemacs/. While the ‘-nH’ option can remove the ftp.xemacs.org/ part, you are still stuck with pub/xemacs. This is where ‘--cut-dirs’ comes in handy; it makes Wget not “see” *number* remote directory components. Here are several examples of how ‘--cut-dirs’ option works.

```
No options        -> ftp.xemacs.org/pub/xemacs/
-nH               -> pub/xemacs/
-nH --cut-dirs=1  -> xemacs/
-nH --cut-dirs=2  -> .

--cut-dirs=1      -> ftp.xemacs.org/xemacs/
...
```

If you just want to get rid of the directory structure, this option is similar to a combination of ‘-nd’ and ‘-P’. However, unlike ‘-nd’, ‘--cut-dirs’ does not lose with subdirectories—for instance, with ‘-nH --cut-dirs=1’, a beta/ subdirectory will be placed to xemacs/beta, as one would expect.

**‘-P *prefix*’ ¶**

**‘--directory-prefix=*prefix*’**

Set directory prefix to *prefix*. The *directory prefix* is the directory where all other files and subdirectories will be saved to, i.e. the top of the retrieval tree. The default is ‘.’ (the current directory).

### 2.7 HTTP Options

**‘--default-page=*name*’ ¶**

Use *name* as the default file name when it isn’t known (i.e., for URLs that end in a slash), instead of index.html.

**‘-E’ ¶**

**‘--adjust-extension’**

If a file of type ‘application/xhtml+xml’ or ‘text/html’ is downloaded and the URL does not end with the regexp ‘\.[Hh][Tt][Mm][Ll]?’, this option will cause the suffix ‘.html’ to be appended to the local filename. This is useful, for instance, when you’re mirroring a remote site that uses ‘.asp’ pages, but you want the mirrored pages to be viewable on your stock Apache server. Another good use for this is when you’re downloading CGI-generated materials. A URL like ‘http://site.com/article.cgi?25’ will be saved as article.cgi?25.html.

Note that filenames changed in this way will be re-downloaded every time you re-mirror a site, because Wget can’t tell that the local *X*.html file corresponds to remote URL ‘*X*’ (since it doesn’t yet know that the URL produces output of type ‘text/html’ or ‘application/xhtml+xml’.

As of version 1.12, Wget will also ensure that any downloaded files of type ‘text/css’ end in the suffix ‘.css’, and the option was renamed from ‘--html-extension’, to better reflect its new behavior. The old option name is still acceptable, but should now be considered deprecated.

As of version 1.19.2, Wget will also ensure that any downloaded files with a `Content-Encoding` of ‘br’, ‘compress’, ‘deflate’ or ‘gzip’ end in the suffix ‘.br’, ‘.Z’, ‘.zlib’ and ‘.gz’ respectively.

At some point in the future, this option may well be expanded to include suffixes for other types of content, including content types that are not parsed by Wget.

**‘--http-user=*user*’ ¶**

**‘--http-password=*password*’**

Specify the username *user* and password *password* on an HTTP server. According to the type of the challenge, Wget will encode them using either the `basic` (insecure), the `digest`, or the Windows `NTLM` authentication scheme.

Another way to specify username and password is in the URL itself (see URL Format). Either method reveals your password to anyone who bothers to run `ps`. To prevent the passwords from being seen, use the ‘--use-askpass’ or store them in .wgetrc or .netrc, and make sure to protect those files from other users with `chmod`. If the passwords are really important, do not leave them lying in those files either—edit the files and delete them after Wget has started the download.

**‘--no-http-keep-alive’ ¶**

Turn off the “keep-alive” feature for HTTP downloads. Normally, Wget asks the server to keep the connection open so that, when you download more than one document from the same server, they get transferred over the same TCP connection. This saves time and at the same time reduces the load on the server.

This option is useful when, for some reason, persistent (keep-alive) connections don’t work for you, for example due to a server bug or due to the inability of server-side scripts to cope with the connections.

**‘--no-cache’ ¶**

Disable server-side cache. In this case, Wget will send the remote server appropriate directives (‘Cache-Control: no-cache’ and ‘Pragma: no-cache’) to get the file from the remote service, rather than returning the cached version. This is especially useful for retrieving and flushing out-of-date documents on proxy servers.

Caching is allowed by default.

**‘--no-cookies’ ¶**

Disable the use of cookies. Cookies are a mechanism for maintaining server-side state. The server sends the client a cookie using the `Set-Cookie` header, and the client responds with the same cookie upon further requests. Since cookies allow the server owners to keep track of visitors and for sites to exchange this information, some consider them a breach of privacy. The default is to use cookies; however, *storing* cookies is not on by default.

**‘--load-cookies *file*’ ¶**

Load cookies from *file* before the first HTTP retrieval. *file* is a textual file in the format originally used by Netscape’s cookies.txt file.
