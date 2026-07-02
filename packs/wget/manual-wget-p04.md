---
title: "GNU Wget 1.25.0 Manual (part 4/6)"
source: https://www.gnu.org/software/wget/manual/wget.html
domain: wget
license: CC-BY-SA-4.0
tags: wget download, file download, recursive download, command-line http
fetched: 2026-07-02
part: 4/6
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


## 4 Following Links

When retrieving recursively, one does not wish to retrieve loads of unnecessary data. Most of the time the users bear in mind exactly what they want to download, and want Wget to follow only specific links.

For example, if you wish to download the music archive from ‘fly.srk.fer.hr’, you will not want to download all the home pages that happen to be referenced by an obscure part of the archive.

Wget possesses several mechanisms that allows you to fine-tune which links it will follow.

### 4.1 Spanning Hosts

Wget’s recursive retrieval normally refuses to visit hosts different than the one you specified on the command line. This is a reasonable default; without it, every retrieval would have the potential to turn your Wget into a small version of google.

However, visiting different hosts, or *host spanning,* is sometimes a useful option. Maybe the images are served from a different server. Maybe you’re mirroring a site that consists of pages interlinked between three servers. Maybe the server has two equivalent names, and the HTML pages refer to both interchangeably.

**Span to any host—‘-H’**

The ‘-H’ option turns on host spanning, thus allowing Wget’s recursive run to visit any host referenced by a link. Unless sufficient recursion-limiting criteria are applied depth, these foreign hosts will typically link to yet more hosts, and so on until Wget ends up sucking up much more data than you have intended.

**Limit spanning to certain domains—‘-D’**

The ‘-D’ option allows you to specify the domains that will be followed, thus limiting the recursion only to the hosts that belong to these domains. Obviously, this makes sense only in conjunction with ‘-H’. A typical example would be downloading the contents of ‘www.example.com’, but allowing downloads from ‘images.example.com’, etc.:

```
wget -rH -Dexample.com http://www.example.com/
```

You can specify more than one address by separating them with a comma, e.g. ‘-Ddomain1.com,domain2.com’.

**Keep download off certain domains—‘--exclude-domains’**

If there are domains you want to exclude specifically, you can do it with ‘--exclude-domains’, which accepts the same type of arguments of ‘-D’, but will *exclude* all the listed domains. For example, if you want to download all the hosts from ‘foo.edu’ domain, with the exception of ‘sunsite.foo.edu’, you can do it like this:

```
wget -rH -Dfoo.edu --exclude-domains sunsite.foo.edu \
    http://www.foo.edu/
```

### 4.2 Types of Files

When downloading material from the web, you will often want to restrict the retrieval to only certain file types. For example, if you are interested in downloading GIFs, you will not be overjoyed to get loads of PostScript documents, and vice versa.

Wget offers two options to deal with this problem. Each option description lists a short name, a long name, and the equivalent command in .wgetrc.

**‘-A *acclist*’**

**‘--accept *acclist*’**

**‘accept = *acclist*’**

**‘--accept-regex *urlregex*’**

**‘accept-regex = *urlregex*’**

The argument to ‘--accept’ option is a list of file suffixes or patterns that Wget will download during recursive retrieval. A suffix is the ending part of a file, and consists of “normal” letters, e.g. ‘gif’ or ‘.jpg’. A matching pattern contains shell-like wildcards, e.g. ‘books*’ or ‘zelazny*196[0-9]*’.

So, specifying ‘wget -A gif,jpg’ will make Wget download only the files ending with ‘gif’ or ‘jpg’, i.e. GIFs and JPEGs. On the other hand, ‘wget -A "zelazny*196[0-9]*"’ will download only files beginning with ‘zelazny’ and containing numbers from 1960 to 1969 anywhere within. Look up the manual of your shell for a description of how pattern matching works.

Of course, any number of suffixes and patterns can be combined into a comma-separated list, and given as an argument to ‘-A’.

The argument to ‘--accept-regex’ option is a regular expression which is matched against the complete URL.

**‘-R *rejlist*’ ¶**

**‘--reject *rejlist*’**

**‘reject = *rejlist*’**

**‘--reject-regex *urlregex*’**

**‘reject-regex = *urlregex*’**

The ‘--reject’ option works the same way as ‘--accept’, only its logic is the reverse; Wget will download all files *except* the ones matching the suffixes (or patterns) in the list.

So, if you want to download a whole page except for the cumbersome MPEGs and .AU files, you can use ‘wget -R mpg,mpeg,au’. Analogously, to download all files except the ones beginning with ‘bjork’, use ‘wget -R "bjork*"’. The quotes are to prevent expansion by the shell.

The argument to ‘--accept-regex’ option is a regular expression which is matched against the complete URL.

The ‘-A’ and ‘-R’ options may be combined to achieve even better fine-tuning of which files to retrieve. E.g. ‘wget -A "*zelazny*" -R .ps’ will download all the files having ‘zelazny’ as a part of their name, but *not* the PostScript files.

Note that these two options do not affect the downloading of HTML files (as determined by a ‘.htm’ or ‘.html’ filename prefix). This behavior may not be desirable for all users, and may be changed for future versions of Wget.

Note, too, that query strings (strings at the end of a URL beginning with a question mark (‘?’) are not included as part of the filename for accept/reject rules, even though these will actually contribute to the name chosen for the local file. It is expected that a future version of Wget will provide an option to allow matching against query strings.

Finally, it’s worth noting that the accept/reject lists are matched *twice* against downloaded files: once against the URL’s filename portion, to determine if the file should be downloaded in the first place; then, after it has been accepted and successfully downloaded, the local file’s name is also checked against the accept/reject lists to see if it should be removed. The rationale was that, since ‘.htm’ and ‘.html’ files are always downloaded regardless of accept/reject rules, they should be removed *after* being downloaded and scanned for links, if they did match the accept/reject lists. However, this can lead to unexpected results, since the local filenames can differ from the original URL filenames in the following ways, all of which can change whether an accept/reject rule matches:

- If the local file already exists and ‘--no-directories’ was specified, a numeric suffix will be appended to the original name.
- If ‘--adjust-extension’ was specified, the local filename might have ‘.html’ appended to it. If Wget is invoked with ‘-E -A.php’, a filename such as ‘index.php’ will match be accepted, but upon download will be named ‘index.php.html’, which no longer matches, and so the file will be deleted.
- Query strings do not contribute to URL matching, but are included in local filenames, and so *do* contribute to filename matching.

This behavior, too, is considered less-than-desirable, and may change in a future version of Wget.

### 4.3 Directory-Based Limits

Regardless of other link-following facilities, it is often useful to place the restriction of what files to retrieve based on the directories those files are placed in. There can be many reasons for this—the home pages may be organized in a reasonable directory structure; or some directories may contain useless information, e.g. /cgi-bin or /dev directories.

Wget offers three different options to deal with this requirement. Each option description lists a short name, a long name, and the equivalent command in .wgetrc.

**‘-I *list*’**

**‘--include *list*’**

**‘include_directories = *list*’**

‘-I’ option accepts a comma-separated list of directories included in the retrieval. Any other directories will simply be ignored. The directories are absolute paths.

So, if you wish to download from ‘http://host/people/bozo/’ following only links to bozo’s colleagues in the /people directory and the bogus scripts in /cgi-bin, you can specify:

```
wget -I /people,/cgi-bin http://host/people/bozo/
```

**‘-X *list*’ ¶**

**‘--exclude *list*’**

**‘exclude_directories = *list*’**

‘-X’ option is exactly the reverse of ‘-I’—this is a list of directories *excluded* from the download. E.g. if you do not want Wget to download things from /cgi-bin directory, specify ‘-X /cgi-bin’ on the command line.

The same as with ‘-A’/‘-R’, these two options can be combined to get a better fine-tuning of downloading subdirectories. E.g. if you want to load all the files from /pub hierarchy except for /pub/worthless, specify ‘-I/pub -X/pub/worthless’.

**‘-np’ ¶**

**‘--no-parent’**

**‘no_parent = on’**

The simplest, and often very useful way of limiting directories is disallowing retrieval of the links that refer to the hierarchy *above* than the beginning directory, i.e. disallowing ascent to the parent directory/directories.

The ‘--no-parent’ option (short ‘-np’) is useful in this case. Using it guarantees that you will never leave the existing hierarchy. Supposing you issue Wget with:

```
wget -r --no-parent http://somehost/~luzer/my-archive/
```

You may rest assured that none of the references to /~his-girls-homepage/ or /~luzer/all-my-mpegs/ will be followed. Only the archive you are interested in will be downloaded. Essentially, ‘--no-parent’ is similar to ‘-I/~luzer/my-archive’, only it handles redirections in a more intelligent fashion.

**Note** that, for HTTP (and HTTPS), the trailing slash is very important to ‘--no-parent’. HTTP has no concept of a “directory”—Wget relies on you to indicate what’s a directory and what isn’t. In ‘http://foo/bar/’, Wget will consider ‘bar’ to be a directory, while in ‘http://foo/bar’ (no trailing slash), ‘bar’ will be considered a filename (so ‘--no-parent’ would be meaningless, as its parent is ‘/’).

### 4.4 Relative Links

When ‘-L’ is turned on, only the relative links are ever followed. Relative links are here defined those that do not refer to the web server root. For example, these links are relative:

```
<a href="foo.gif">
<a href="foo/bar.gif">
<a href="../foo/bar.gif">
```

These links are not relative:

```
<a href="/foo.gif">
<a href="/foo/bar.gif">
<a href="http://www.example.com/foo/bar.gif">
```

Using this option guarantees that recursive retrieval will not span hosts, even without ‘-H’. In simple cases it also allows downloads to “just work” without having to convert links.

This option is probably not very useful and might be removed in a future release.

### 4.5 Following FTP Links

The rules for FTP are somewhat specific, as it is necessary for them to be. FTP links in HTML documents are often included for purposes of reference, and it is often inconvenient to download them by default.

To have FTP links followed from HTML documents, you need to specify the ‘--follow-ftp’ option. Having done that, FTP links will span hosts regardless of ‘-H’ setting. This is logical, as FTP links rarely point to the same host where the HTTP server resides. For similar reasons, the ‘-L’ options has no effect on such downloads. On the other hand, domain acceptance (‘-D’) and suffix rules (‘-A’ and ‘-R’) apply normally.

Also note that followed links to FTP directories will not be retrieved recursively further.


## 5 Time-Stamping

One of the most important aspects of mirroring information from the Internet is updating your archives.

Downloading the whole archive again and again, just to replace a few changed files is expensive, both in terms of wasted bandwidth and money, and the time to do the update. This is why all the mirroring tools offer the option of incremental updating.

Such an updating mechanism means that the remote server is scanned in search of *new* files. Only those new files will be downloaded in the place of the old ones.

A file is considered new if one of these two conditions are met:

1. A file of that name does not already exist locally.
2. A file of that name does exist, but the remote file was modified more recently than the local file.

To implement this, the program needs to be aware of the time of last modification of both local and remote files. We call this information the *time-stamp* of a file.

The time-stamping in GNU Wget is turned on using ‘--timestamping’ (‘-N’) option, or through `timestamping = on` directive in .wgetrc. With this option, for each file it intends to download, Wget will check whether a local file of the same name exists. If it does, and the remote file is not newer, Wget will not download it.

If the local file does not exist, or the sizes of the files do not match, Wget will download the remote file no matter what the time-stamps say.

### 5.1 Time-Stamping Usage

The usage of time-stamping is simple. Say you would like to download a file so that it keeps its date of modification.

```
wget -S http://www.gnu.ai.mit.edu/
```

A simple `ls -l` shows that the timestamp on the local file equals the state of the `Last-Modified` header, as returned by the server. As you can see, the time-stamping info is preserved locally, even without ‘-N’ (at least for HTTP).

Several days later, you would like Wget to check if the remote file has changed, and download it if it has.

```
wget -N http://www.gnu.ai.mit.edu/
```

Wget will ask the server for the last-modified date. If the local file has the same timestamp as the server, or a newer one, the remote file will not be re-fetched. However, if the remote file is more recent, Wget will proceed to fetch it.

The same goes for FTP. For example:

```
wget "ftp://ftp.ifi.uio.no/pub/emacs/gnus/*"
```

(The quotes around that URL are to prevent the shell from trying to interpret the ‘*’.)

After download, a local directory listing will show that the timestamps match those on the remote server. Reissuing the command with ‘-N’ will make Wget re-fetch *only* the files that have been modified since the last download.

If you wished to mirror the GNU archive every week, you would use a command like the following, weekly:

```
wget --timestamping -r ftp://ftp.gnu.org/pub/gnu/
```

Note that time-stamping will only work for files for which the server gives a timestamp. For HTTP, this depends on getting a `Last-Modified` header. For FTP, this depends on getting a directory listing with dates in a format that Wget can parse (see FTP Time-Stamping Internals).

### 5.2 HTTP Time-Stamping Internals

Time-stamping in HTTP is implemented by checking of the `Last-Modified` header. If you wish to retrieve the file foo.html through HTTP, Wget will check whether foo.html exists locally. If it doesn’t, foo.html will be retrieved unconditionally.

If the file does exist locally, Wget will first check its local time-stamp (similar to the way `ls -l` checks it), and then send a `HEAD` request to the remote server, demanding the information on the remote file.

The `Last-Modified` header is examined to find which file was modified more recently (which makes it “newer”). If the remote file is newer, it will be downloaded; if it is older, Wget will give up.2

When ‘--backup-converted’ (‘-K’) is specified in conjunction with ‘-N’, server file ‘*X*’ is compared to local file ‘*X*.orig’, if extant, rather than being compared to local file ‘*X*’, which will always differ if it’s been converted by ‘--convert-links’ (‘-k’).

Arguably, HTTP time-stamping should be implemented using the `If-Modified-Since` request.

### 5.3 FTP Time-Stamping Internals

In theory, FTP time-stamping works much the same as HTTP, only FTP has no headers—time-stamps must be ferreted out of directory listings.

If an FTP download is recursive or uses globbing, Wget will use the FTP `LIST` command to get a file listing for the directory containing the desired file(s). It will try to analyze the listing, treating it like Unix `ls -l` output, extracting the time-stamps. The rest is exactly the same as for HTTP. Note that when retrieving individual files from an FTP server without using globbing or recursion, listing files will not be downloaded (and thus files will not be time-stamped) unless ‘-N’ is specified.

Assumption that every directory listing is a Unix-style listing may sound extremely constraining, but in practice it is not, as many non-Unix FTP servers use the Unixoid listing format because most (all?) of the clients understand it. Bear in mind that RFC959 defines no standard way to get a file list, let alone the time-stamps. We can only hope that a future standard will define this.

Another non-standard solution includes the use of `MDTM` command that is supported by some FTP servers (including the popular `wu-ftpd`), which returns the exact time of the specified file. Wget may support this command in the future.


## 6 Startup File

Once you know how to change default settings of Wget through command line arguments, you may wish to make some of those settings permanent. You can do that in a convenient way by creating the Wget startup file—.wgetrc.

Besides .wgetrc is the “main” initialization file, it is convenient to have a special facility for storing passwords. Thus Wget reads and interprets the contents of $HOME/.netrc, if it finds it. You can find .netrc format in your system manuals.

Wget reads .wgetrc upon startup, recognizing a limited set of commands.

### 6.1 Wgetrc Location

When initializing, Wget will look for a *global* startup file, /usr/local/etc/wgetrc by default (or some prefix other than /usr/local, if Wget was not installed there) and read commands from there, if it exists.

Then it will look for the user’s file. If the environmental variable `WGETRC` is set, Wget will try to load that file. Failing that, no further attempts will be made.

If `WGETRC` is not set, Wget will try to load $HOME/.wgetrc.

The fact that user’s settings are loaded after the system-wide ones means that in case of collision user’s wgetrc *overrides* the system-wide wgetrc (in /usr/local/etc/wgetrc by default). Fascist admins, away!

### 6.2 Wgetrc Syntax

The syntax of a wgetrc command is simple:

```
variable = value
```

The *variable* will also be called *command*. Valid *values* are different for different commands.

The commands are case-, underscore- and minus-insensitive. Thus ‘DIr__PrefiX’, ‘DIr-PrefiX’ and ‘dirprefix’ are the same. Empty lines, lines beginning with ‘#’ and lines containing white-space only are discarded.

Commands that expect a comma-separated list will clear the list on an empty command. So, if you wish to reset the rejection list specified in global wgetrc, you can do it with:

```
reject =
```

### 6.3 Wgetrc Commands

The complete set of commands is listed below. Legal values are listed after the ‘=’. Simple Boolean values can be set or unset using ‘on’ and ‘off’ or ‘1’ and ‘0’.

Some commands take pseudo-arbitrary values. *address* values can be hostnames or dotted-quad IP addresses. *n* can be any positive integer, or ‘inf’ for infinity, where appropriate. *string* values can be any non-empty string.

Most of these commands have direct command-line equivalents. Also, any wgetrc command can be specified on the command line using the ‘--execute’ switch (see Basic Startup Options.)

**accept/reject = *string***

Same as ‘-A’/‘-R’ (see Types of Files).

**add_hostdir = on/off**

Enable/disable host-prefixed file names. ‘-nH’ disables it.

**ask_password = on/off**

Prompt for a password for each connection established. Cannot be specified when ‘--password’ is being used, because they are mutually exclusive. Equivalent to ‘--ask-password’.

**auth_no_challenge = on/off**

If this option is given, Wget will send Basic HTTP authentication information (plaintext username and password) for all requests. See ‘--auth-no-challenge’.

**background = on/off**

Enable/disable going to background—the same as ‘-b’ (which enables it).

**backup_converted = on/off**

Enable/disable saving pre-converted files with the suffix ‘.orig’—the same as ‘-K’ (which enables it).

**backups = *number***

Use up to *number* backups for a file. Backups are rotated by adding an incremental counter that starts at ‘1’. The default is ‘0’.

**base = *string***

Consider relative URLs in input files (specified via the ‘input’ command or the ‘--input-file’/‘-i’ option, together with ‘force_html’ or ‘--force-html’) as being relative to *string*—the same as ‘--base=*string*’.

**bind_address = *address***

Bind to *address*, like the ‘--bind-address=*address*’.

**ca_certificate = *file***

Set the certificate authority bundle file to *file*. The same as ‘--ca-certificate=*file*’.

**ca_directory = *directory***

Set the directory used for certificate authorities. The same as ‘--ca-directory=*directory*’.

**cache = on/off**

When set to off, disallow server-caching. See the ‘--no-cache’ option.

**certificate = *file***

Set the client certificate file name to *file*. The same as ‘--certificate=*file*’.

**certificate_type = *string***

Specify the type of the client certificate, legal values being ‘PEM’ (the default) and ‘DER’ (aka ASN1). The same as ‘--certificate-type=*string*’.

**check_certificate = on/off**

If this is set to off, the server certificate is not checked against the specified client authorities. The default is “on”. The same as ‘--check-certificate’.

**connect_timeout = *n***

Set the connect timeout—the same as ‘--connect-timeout’.

**content_disposition = on/off**

Turn on recognition of the (non-standard) ‘Content-Disposition’ HTTP header—if set to ‘on’, the same as ‘--content-disposition’.

**trust_server_names = on/off**

If set to on, construct the local file name from redirection URLs rather than original URLs.

**continue = on/off**

If set to on, force continuation of preexistent partially retrieved files. See ‘-c’ before setting it.

**convert_links = on/off**

Convert non-relative links locally. The same as ‘-k’.

**cookies = on/off**

When set to off, disallow cookies. See the ‘--cookies’ option.

**cut_dirs = *n***

Ignore *n* remote directory components. Equivalent to ‘--cut-dirs=*n*’.

**debug = on/off**

Debug mode, same as ‘-d’.

**default_page = *string***

Default page name—the same as ‘--default-page=*string*’.

**delete_after = on/off**

Delete after download—the same as ‘--delete-after’.

**dir_prefix = *string***

Top of directory tree—the same as ‘-P *string*’.

**dirstruct = on/off**

Turning dirstruct on or off—the same as ‘-x’ or ‘-nd’, respectively.

**dns_cache = on/off**

Turn DNS caching on/off. Since DNS caching is on by default, this option is normally used to turn it off and is equivalent to ‘--no-dns-cache’.

**dns_timeout = *n***

Set the DNS timeout—the same as ‘--dns-timeout’.

**domains = *string***

Same as ‘-D’ (see Spanning Hosts).

**dot_bytes = *n***

Specify the number of bytes “contained” in a dot, as seen throughout the retrieval (1024 by default). You can postfix the value with ‘k’ or ‘m’, representing kilobytes and megabytes, respectively. With dot settings you can tailor the dot retrieval to suit your needs, or you can use the predefined *styles* (see Download Options).

**dot_spacing = *n***

Specify the number of dots in a single cluster (10 by default).

**dots_in_line = *n***

Specify the number of dots that will be printed in each line throughout the retrieval (50 by default).

**egd_file = *file***

Use *string* as the EGD socket file name. The same as ‘--egd-file=*file*’.

**exclude_directories = *string***

Specify a comma-separated list of directories you wish to exclude from download—the same as ‘-X *string*’ (see Directory-Based Limits).

**exclude_domains = *string***

Same as ‘--exclude-domains=*string*’ (see Spanning Hosts).

**follow_ftp = on/off**

Follow FTP links from HTML documents—the same as ‘--follow-ftp’.

**follow_tags = *string***

Only follow certain HTML tags when doing a recursive retrieval, just like ‘--follow-tags=*string*’.

**force_html = on/off**

If set to on, force the input filename to be regarded as an HTML document—the same as ‘-F’.

**ftp_password = *string***

Set your FTP password to *string*. Without this setting, the password defaults to ‘-wget@’, which is a useful default for anonymous FTP access.

This command used to be named `passwd` prior to Wget 1.10.

**ftp_proxy = *string***

Use *string* as FTP proxy, instead of the one specified in environment.

**ftp_user = *string***

Set FTP user to *string*.

This command used to be named `login` prior to Wget 1.10.

**glob = on/off**

Turn globbing on/off—the same as ‘--glob’ and ‘--no-glob’.

**header = *string***

Define a header for HTTP downloads, like using ‘--header=*string*’.

**compression = *string***

Choose the compression type to be used. Legal values are ‘auto’ (the default), ‘gzip’, and ‘none’. The same as ‘--compression=*string*’.

**adjust_extension = on/off**

Add a ‘.html’ extension to ‘text/html’ or ‘application/xhtml+xml’ files that lack one, a ‘.css’ extension to ‘text/css’ files that lack one, and a ‘.br’, ‘.Z’, ‘.zlib’ or ‘.gz’ to compressed files like ‘-E’. Previously named ‘html_extension’ (still acceptable, but deprecated).

**http_keep_alive = on/off**

Turn the keep-alive feature on or off (defaults to on). Turning it off is equivalent to ‘--no-http-keep-alive’.

**http_password = *string***

Set HTTP password, equivalent to ‘--http-password=*string*’.

**http_proxy = *string***

Use *string* as HTTP proxy, instead of the one specified in environment.

**http_user = *string***

Set HTTP user to *string*, equivalent to ‘--http-user=*string*’.

**https_only = on/off**

When in recursive mode, only HTTPS links are followed (defaults to off).

**https_proxy = *string***

Use *string* as HTTPS proxy, instead of the one specified in environment.

**ignore_case = on/off**

When set to on, match files and directories case insensitively; the same as ‘--ignore-case’.

**ignore_length = on/off**

When set to on, ignore `Content-Length` header; the same as ‘--ignore-length’.

**ignore_tags = *string***

Ignore certain HTML tags when doing a recursive retrieval, like ‘--ignore-tags=*string*’.

**include_directories = *string***

Specify a comma-separated list of directories you wish to follow when downloading—the same as ‘-I *string*’.

**iri = on/off**

When set to on, enable internationalized URI (IRI) support; the same as ‘--iri’.

**inet4_only = on/off**

Force connecting to IPv4 addresses, off by default. You can put this in the global init file to disable Wget’s attempts to resolve and connect to IPv6 hosts. Available only if Wget was compiled with IPv6 support. The same as ‘--inet4-only’ or ‘-4’.

**inet6_only = on/off**

Force connecting to IPv6 addresses, off by default. Available only if Wget was compiled with IPv6 support. The same as ‘--inet6-only’ or ‘-6’.

**input = *file***

Read the URLs from *string*, like ‘-i *file*’.

**keep_session_cookies = on/off**

When specified, causes ‘save_cookies = on’ to also save session cookies. See ‘--keep-session-cookies’.

**limit_rate = *rate***

Limit the download speed to no more than *rate* bytes per second. The same as ‘--limit-rate=*rate*’.

**load_cookies = *file***

Load cookies from *file*. See ‘--load-cookies *file*’.

**local_encoding = *encoding***

Force Wget to use *encoding* as the default system encoding. See ‘--local-encoding’.

**logfile = *file***

Set logfile to *file*, the same as ‘-o *file*’.

**max_redirect = *number***

Specifies the maximum number of redirections to follow for a resource. See ‘--max-redirect=*number*’.

**mirror = on/off**

Turn mirroring on/off. The same as ‘-m’.

**netrc = on/off**

Turn reading netrc on or off.

**no_clobber = on/off**

Same as ‘-nc’.

**no_parent = on/off**

Disallow retrieving outside the directory hierarchy, like ‘--no-parent’ (see Directory-Based Limits).

**no_proxy = *string***

Use *string* as the comma-separated list of domains to avoid in proxy loading, instead of the one specified in environment.

**output_document = *file***

Set the output filename—the same as ‘-O *file*’.

**page_requisites = on/off**

Download all ancillary documents necessary for a single HTML page to display properly—the same as ‘-p’.

**passive_ftp = on/off**

Change setting of passive FTP, equivalent to the ‘--passive-ftp’ option.

**password = *string***

Specify password *string* for both FTP and HTTP file retrieval. This command can be overridden using the ‘ftp_password’ and ‘http_password’ command for FTP and HTTP respectively.

**post_data = *string***

Use POST as the method for all HTTP requests and send *string* in the request body. The same as ‘--post-data=*string*’.

**post_file = *file***

Use POST as the method for all HTTP requests and send the contents of *file* in the request body. The same as ‘--post-file=*file*’.

**prefer_family = none/IPv4/IPv6**

When given a choice of several addresses, connect to the addresses with specified address family first. The address order returned by DNS is used without change by default. The same as ‘--prefer-family’, which see for a detailed discussion of why this is useful.

**private_key = *file***

Set the private key file to *file*. The same as ‘--private-key=*file*’.

**private_key_type = *string***

Specify the type of the private key, legal values being ‘PEM’ (the default) and ‘DER’ (aka ASN1). The same as ‘--private-type=*string*’.

**progress = *string***

Set the type of the progress indicator. Legal types are ‘dot’ and ‘bar’. Equivalent to ‘--progress=*string*’.

**protocol_directories = on/off**

When set, use the protocol name as a directory component of local file names. The same as ‘--protocol-directories’.

**proxy_password = *string***

Set proxy authentication password to *string*, like ‘--proxy-password=*string*’.

**proxy_user = *string***

Set proxy authentication user name to *string*, like ‘--proxy-user=*string*’.

**quiet = on/off**

Quiet mode—the same as ‘-q’.

**quota = *quota***

Specify the download quota, which is useful to put in the global wgetrc. When download quota is specified, Wget will stop retrieving after the download sum has become greater than quota. The quota can be specified in bytes (default), kbytes ‘k’ appended) or mbytes (‘m’ appended). Thus ‘quota = 5m’ will set the quota to 5 megabytes. Note that the user’s startup file overrides system settings.

**random_file = *file***

Use *file* as a source of randomness on systems lacking /dev/random.

**random_wait = on/off**

Turn random between-request wait times on or off. The same as ‘--random-wait’.

**read_timeout = *n***

Set the read (and write) timeout—the same as ‘--read-timeout=*n*’.

**reclevel = *n***

Recursion level (depth)—the same as ‘-l *n*’.

**recursive = on/off**

Recursive on/off—the same as ‘-r’.

**referer = *string***

Set HTTP ‘Referer:’ header just like ‘--referer=*string*’. (Note that it was the folks who wrote the HTTP spec who got the spelling of “referrer” wrong.)

**relative_only = on/off**

Follow only relative links—the same as ‘-L’ (see Relative Links).

**remote_encoding = *encoding***

Force Wget to use *encoding* as the default remote server encoding. See ‘--remote-encoding’.

**remove_listing = on/off**

If set to on, remove FTP listings downloaded by Wget. Setting it to off is the same as ‘--no-remove-listing’.

**restrict_file_names = unix/windows**

Restrict the file names generated by Wget from URLs. See ‘--restrict-file-names’ for a more detailed description.

**retr_symlinks = on/off**

When set to on, retrieve symbolic links as if they were plain files; the same as ‘--retr-symlinks’.

**retry_connrefused = on/off**

When set to on, consider “connection refused” a transient error—the same as ‘--retry-connrefused’.

**robots = on/off**

Specify whether the norobots convention is respected by Wget, “on” by default. This switch controls both the /robots.txt and the ‘nofollow’ aspect of the spec. See Robot Exclusion, for more details about this. Be sure you know what you are doing before turning this off.

**save_cookies = *file***

Save cookies to *file*. The same as ‘--save-cookies *file*’.

**save_headers = on/off**

Same as ‘--save-headers’.

**secure_protocol = *string***

Choose the secure protocol to be used. Legal values are ‘auto’ (the default), ‘SSLv2’, ‘SSLv3’, and ‘TLSv1’. The same as ‘--secure-protocol=*string*’.

**server_response = on/off**

Choose whether or not to print the HTTP and FTP server responses—the same as ‘-S’.

**show_all_dns_entries = on/off**

When a DNS name is resolved, show all the IP addresses, not just the first three.

**span_hosts = on/off**

Same as ‘-H’.

**spider = on/off**

Same as ‘--spider’.

**strict_comments = on/off**

Same as ‘--strict-comments’.

**timeout = *n***

Set all applicable timeout values to *n*, the same as ‘-T *n*’.

**timestamping = on/off**

Turn timestamping on/off. The same as ‘-N’ (see Time-Stamping).

**use_server_timestamps = on/off**

If set to ‘off’, Wget won’t set the local file’s timestamp by the one on the server (same as ‘--no-use-server-timestamps’).

**tries = *n***

Set number of retries per URL—the same as ‘-t *n*’.

**use_proxy = on/off**

When set to off, don’t use proxy even when proxy-related environment variables are set. In that case it is the same as using ‘--no-proxy’.

**user = *string***

Specify username *string* for both FTP and HTTP file retrieval. This command can be overridden using the ‘ftp_user’ and ‘http_user’ command for FTP and HTTP respectively.

**user_agent = *string***

User agent identification sent to the HTTP Server—the same as ‘--user-agent=*string*’.

**verbose = on/off**

Turn verbose on/off—the same as ‘-v’/‘-nv’.

**wait = *n***

Wait *n* seconds between retrievals—the same as ‘-w *n*’.

**wait_retry = *n***

Wait up to *n* seconds between retries of failed retrievals only—the same as ‘--waitretry=*n*’. Note that this is turned on by default in the global wgetrc.

### 6.4 Sample Wgetrc

This is the sample initialization file, as given in the distribution. It is divided in two section—one for global usage (suitable for global startup file), and one for local usage (suitable for $HOME/.wgetrc). Be careful about the things you change.

Note that almost all the lines are commented out. For a command to have any effect, you must remove the ‘#’ character at the beginning of its line.

```
###
### Sample Wget initialization file .wgetrc
###


## You can use this file to change the default behaviour of wget or to

## avoid having to type many many command-line options. This file does

## not contain a comprehensive list of commands -- look at the manual

## to find out what you can put into this file. You can find this here:

##   $ info wget.info 'Startup File'

## Or online here:

##   https://www.gnu.org/software/wget/manual/wget.html#Startup-File
##

## Wget initialization file can reside in /usr/local/etc/wgetrc

## (global, for all users) or $HOME/.wgetrc (for a single user).
##

## To use the settings in this file, you will have to uncomment them,

## as well as change them, in most cases, as the values on the

## commented-out lines are the default values (e.g. "off").
##

## Command are case-, underscore- and minus-insensitive.

## For example ftp_proxy, ftp-proxy and ftpproxy are the same.

##

## Global settings (useful for setting up in /usr/local/etc/wgetrc).

## Think well before you change them, since they may reduce wget's

## functionality, and make it behave contrary to the documentation:
##

# You can set retrieve quota for beginners by specifying a value
# optionally followed by 'K' (kilobytes) or 'M' (megabytes).  The
# default quota is unlimited.
#quota = inf

# You can lower (or raise) the default number of retries when
# downloading a file (default is 20).
#tries = 20

# Lowering the maximum depth of the recursive retrieval is handy to
# prevent newbies from going too "deep" when they unwittingly start
# the recursive retrieval.  The default is 5.
#reclevel = 5

# By default Wget uses "passive FTP" transfer where the client
# initiates the data connection to the server rather than the other
# way around.  That is required on systems behind NAT where the client
# computer cannot be easily reached from the Internet.  However, some
# firewalls software explicitly supports active FTP and in fact has
# problems supporting passive transfer.  If you are in such
# environment, use "passive_ftp = off" to revert to active FTP.
#passive_ftp = off

# The "wait" command below makes Wget wait between every connection.
# If, instead, you want Wget to wait only between retries of failed
# downloads, set waitretry to maximum number of seconds to wait (Wget
# will use "linear backoff", waiting 1 second after the first failure
# on a file, 2 seconds after the second failure, etc. up to this max).
#waitretry = 10

##

## Local settings (for a user to set in his $HOME/.wgetrc).  It is

## *highly* undesirable to put these settings in the global file, since

## they are potentially dangerous to "normal" users.
##

## Even when setting up your own ~/.wgetrc, you should know what you

## are doing before doing so.
##

# Set this to on to use timestamping by default:
#timestamping = off

# It is a good idea to make Wget send your email address in a `From:'
# header with your request (so that server administrators can contact
# you in case of errors).  Wget does *not* send `From:' by default.
#header = From: Your Name <username@site.domain>

# You can set up other headers, like Accept-Language.  Accept-Language
# is *not* sent by default.
#header = Accept-Language: en

# You can set the default proxies for Wget to use for http, https, and ftp.
# They will override the value in the environment.
#https_proxy = http://proxy.yoyodyne.com:18023/
#http_proxy = http://proxy.yoyodyne.com:18023/
#ftp_proxy = http://proxy.yoyodyne.com:18023/

# If you do not want to use proxy at all, set this to off.
#use_proxy = on

# You can customize the retrieval outlook.  Valid options are default,
# binary, mega and micro.
#dot_style = default

# Setting this to off makes Wget not download /robots.txt.  Be sure to
# know *exactly* what /robots.txt is and how it is used before changing
# the default!
#robots = on

# It can be useful to make Wget wait between connections.  Set this to
# the number of seconds you want Wget to wait.
#wait = 0

# You can force creating directory structure, even if a single is being
# retrieved, by setting this to on.
#dirstruct = off

# You can turn on recursive retrieving by default (don't do this if
# you are not sure you know what it means) by setting this to on.
#recursive = off

# To always back up file X as X.orig before converting its links (due
# to -k / --convert-links / convert_links = on having been specified),
# set this variable to on:
#backup_converted = off

# To have Wget follow FTP links from HTML files by default, set this
# to on:
#follow_ftp = off

# To try ipv6 addresses first:
#prefer-family = IPv6

# Set default IRI support state
#iri = off

# Force the default system encoding
#localencoding = UTF-8

# Force the default remote server encoding
#remoteencoding = UTF-8

# Turn on to prevent following non-HTTPS links when in recursive mode
#httpsonly = off

# Tune HTTPS security (auto, SSLv2, SSLv3, TLSv1, PFS)
#secureprotocol = auto
```
