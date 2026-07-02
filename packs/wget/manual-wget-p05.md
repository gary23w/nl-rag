---
title: "GNU Wget 1.25.0 Manual (part 5/6)"
source: https://www.gnu.org/software/wget/manual/wget.html
domain: wget
license: CC-BY-SA-4.0
tags: wget download, file download, recursive download, command-line http
fetched: 2026-07-02
part: 5/6
---

## 7 Examples

The examples are divided into three sections loosely based on their complexity.

### 7.1 Simple Usage

- Say you want to download a URL. Just type: wget http://fly.srk.fer.hr/
- But what will happen if the connection is slow, and the file is lengthy? The connection will probably fail before the whole file is retrieved, more than once. In this case, Wget will try getting the file until it either gets the whole of it, or exceeds the default number of retries (this being 20). It is easy to change the number of tries to 45, to insure that the whole file will arrive safely: wget --tries=45 http://fly.srk.fer.hr/jpg/flyweb.jpg
- Now let’s leave Wget to work in the background, and write its progress to log file log. It is tiring to type ‘--tries’, so we shall use ‘-t’. wget -t 45 -o log http://fly.srk.fer.hr/jpg/flyweb.jpg & The ampersand at the end of the line makes sure that Wget works in the background. To unlimit the number of retries, use ‘-t inf’.
- The usage of FTP is as simple. Wget will take care of login and password. wget ftp://gnjilux.srk.fer.hr/welcome.msg
- If you specify a directory, Wget will retrieve the directory listing, parse it and convert it to HTML. Try: wget ftp://ftp.gnu.org/pub/gnu/ links index.html

### 7.2 Advanced Usage

- You have a file that contains the URLs you want to download? Use the ‘-i’ switch: wget -i *file* If you specify ‘-’ as file name, the URLs will be read from standard input.
- Create a five levels deep mirror image of the GNU web site, with the same directory structure the original has, with only one try per document, saving the log of the activities to gnulog: wget -r https://www.gnu.org/ -o gnulog
- The same as the above, but convert the links in the downloaded files to point to local files, so you can view the documents off-line: wget --convert-links -r https://www.gnu.org/ -o gnulog
- Retrieve only one HTML page, but make sure that all the elements needed for the page to be displayed, such as inline images and external style sheets, are also downloaded. Also make sure the downloaded page references the downloaded links. wget -p --convert-links http://www.example.com/dir/page.html The HTML page will be saved to www.example.com/dir/page.html, and the images, stylesheets, etc., somewhere under www.example.com/, depending on where they were on the remote server.
- The same as the above, but without the www.example.com/ directory. In fact, I don’t want to have all those random server directories anyway—just save *all* those files under a download/ subdirectory of the current directory. wget -p --convert-links -nH -nd -Pdownload \ http://www.example.com/dir/page.html
- Retrieve the index.html of ‘www.lycos.com’, showing the original server headers: wget -S http://www.lycos.com/
- Save the server headers with the file, perhaps for post-processing. wget --save-headers http://www.lycos.com/ more index.html
- Retrieve the first two levels of ‘wuarchive.wustl.edu’, saving them to /tmp. wget -r -l2 -P/tmp ftp://wuarchive.wustl.edu/
- You want to download all the GIFs from a directory on an HTTP server. You tried ‘wget http://www.example.com/dir/*.gif’, but that didn’t work because HTTP retrieval does not support globbing. In that case, use: wget -r -l1 --no-parent -A.gif http://www.example.com/dir/ More verbose, but the effect is the same. ‘-r -l1’ means to retrieve recursively (see Recursive Download), with maximum depth of 1. ‘--no-parent’ means that references to the parent directory are ignored (see Directory-Based Limits), and ‘-A.gif’ means to download only the GIF files. ‘-A "*.gif"’ would have worked too.
- Suppose you were in the middle of downloading, when Wget was interrupted. Now you do not want to clobber the files already present. It would be: wget -nc -r https://www.gnu.org/
- If you want to encode your own username and password to HTTP or FTP, use the appropriate URL syntax (see URL Format). wget ftp://hniksic:mypassword@unix.example.com/.emacs Note, however, that this usage is not advisable on multi-user systems because it reveals your password to anyone who looks at the output of `ps`.
- You would like the output documents to go to standard output instead of to files? wget -O - http://jagor.srce.hr/ http://www.srce.hr/ You can also combine the two options and make pipelines to retrieve the documents from remote hotlists: wget -O - http://cool.list.com/ | wget --force-html -i -

### 7.3 Very Advanced Usage

- If you wish Wget to keep a mirror of a page (or FTP subdirectories), use ‘--mirror’ (‘-m’), which is the shorthand for ‘-r -l inf -N’. You can put Wget in the crontab file asking it to recheck a site each Sunday: crontab 0 0 * * 0 wget --mirror https://www.gnu.org/ -o /home/me/weeklog
- In addition to the above, you want the links to be converted for local viewing. But, after having read this manual, you know that link conversion doesn’t play well with timestamping, so you also want Wget to back up the original HTML files before the conversion. Wget invocation would look like this: wget --mirror --convert-links --backup-converted \ https://www.gnu.org/ -o /home/me/weeklog
- But you’ve also noticed that local viewing doesn’t work all that well when HTML files are saved under extensions other than ‘.html’, perhaps because they were served as index.cgi. So you’d like Wget to rename all the files served with content-type ‘text/html’ or ‘application/xhtml+xml’ to *name*.html. wget --mirror --convert-links --backup-converted \ --adjust-extension -o /home/me/weeklog \ https://www.gnu.org/ Or, with less typing: wget -m -k -K -E https://www.gnu.org/ -o /home/me/weeklog


## 8 Various

This chapter contains all the stuff that could not fit anywhere else.

### 8.1 Proxies

*Proxies* are special-purpose HTTP servers designed to transfer data from remote servers to local clients. One typical use of proxies is lightening network load for users behind a slow connection. This is achieved by channeling all HTTP and FTP requests through the proxy which caches the transferred data. When a cached resource is requested again, proxy will return the data from cache. Another use for proxies is for companies that separate (for security reasons) their internal networks from the rest of Internet. In order to obtain information from the Web, their users connect and retrieve remote data using an authorized proxy.

Wget supports proxies for both HTTP and FTP retrievals. The standard way to specify proxy location, which Wget recognizes, is using the following environment variables:

**`http_proxy`**

**`https_proxy`**

If set, the `http_proxy` and `https_proxy` variables should contain the URLs of the proxies for HTTP and HTTPS connections respectively.

**`ftp_proxy`**

This variable should contain the URL of the proxy for FTP connections. It is quite common that `http_proxy` and `ftp_proxy` are set to the same URL.

**`no_proxy`**

This variable should contain a comma-separated list of domain extensions proxy should *not* be used for. For instance, if the value of `no_proxy` is ‘.mit.edu’, proxy will not be used to retrieve documents from MIT.

In addition to the environment variables, proxy location and settings may be specified from within Wget itself.

**‘--no-proxy’**

**‘proxy = on/off’**

This option and the corresponding command may be used to suppress the use of proxy, even if the appropriate environment variables are set.

**‘http_proxy = *URL*’**

**‘https_proxy = *URL*’**

**‘ftp_proxy = *URL*’**

**‘no_proxy = *string*’**

These startup file variables allow you to override the proxy settings specified by the environment.

Some proxy servers require authorization to enable you to use them. The authorization consists of *username* and *password*, which must be sent by Wget. As with HTTP authorization, several authentication schemes exist. For proxy authorization only the `Basic` authentication scheme is currently implemented.

You may specify your username and password either through the proxy URL or through the command-line options. Assuming that the company’s proxy is located at ‘proxy.company.com’ at port 8001, a proxy URL location containing authorization data might look like this:

```
http://hniksic:mypassword@proxy.company.com:8001/
```

Alternatively, you may use the ‘proxy-user’ and ‘proxy-password’ options, and the equivalent .wgetrc settings `proxy_user` and `proxy_password` to set the proxy username and password.

### 8.2 Distribution

Like all GNU utilities, the latest version of Wget can be found at the master GNU archive site ftp.gnu.org, and its mirrors. For example, Wget 1.25.0 can be found at https://ftp.gnu.org/pub/gnu/wget/wget-1.25.0.tar.gz

### 8.3 Web Site

The official web site for GNU Wget is at https//www.gnu.org/software/wget/. However, most useful information resides at “The Wget Wgiki”, http://wget.addictivecode.org/.

### 8.4 Mailing Lists

#### Primary List

The primary mailinglist for discussion, bug-reports, or questions about GNU Wget is at bug-wget@gnu.org. To subscribe, send an email to bug-wget-join@gnu.org, or visit https://lists.gnu.org/mailman/listinfo/bug-wget.

You do not need to subscribe to send a message to the list; however, please note that unsubscribed messages are moderated, and may take a while before they hit the list—**usually around a day**. If you want your message to show up immediately, please subscribe to the list before posting. Archives for the list may be found at https://lists.gnu.org/archive/html/bug-wget/.

An NNTP/Usenettish gateway is also available via Gmane. You can see the Gmane archives at http://news.gmane.org/gmane.comp.web.wget.general. Note that the Gmane archives conveniently include messages from both the current list, and the previous one. Messages also show up in the Gmane archives sooner than they do at https://lists.gnu.org.

#### Obsolete Lists

Previously, the mailing list wget@sunsite.dk was used as the main discussion list, and another list, wget-patches@sunsite.dk was used for submitting and discussing patches to GNU Wget.

Messages from wget@sunsite.dk are archived at

- https://www.mail-archive.com/wget%40sunsite.dk/ and at
- http://news.gmane.org/gmane.comp.web.wget.general (which also continues to archive the current list, bug-wget@gnu.org).

Messages from wget-patches@sunsite.dk are archived at

- http://news.gmane.org/gmane.comp.web.wget.patches.

### 8.5 Internet Relay Chat

In addition to the mailinglists, we also have a support channel set up via IRC at `irc.freenode.org`, `#wget`. Come check it out!

### 8.6 Reporting Bugs

You are welcome to submit bug reports via the GNU Wget bug tracker (see https://savannah.gnu.org/bugs/?func=additem&group=wget) or to our mailing list bug-wget@gnu.org.

Visit https://lists.gnu.org/mailman/listinfo/bug-wget to get more info (how to subscribe, list archives, ...).

Before actually submitting a bug report, please try to follow a few simple guidelines.

1. Please try to ascertain that the behavior you see really is a bug. If Wget crashes, it’s a bug. If Wget does not behave as documented, it’s a bug. If things work strange, but you are not sure about the way they are supposed to work, it might well be a bug, but you might want to double-check the documentation and the mailing lists (see Mailing Lists).
2. Try to repeat the bug in as simple circumstances as possible. E.g. if Wget crashes while downloading ‘wget -rl0 -kKE -t5 --no-proxy http://example.com -o /tmp/log’, you should try to see if the crash is repeatable, and if will occur with a simpler set of options. You might even try to start the download at the page where the crash occurred to see if that page somehow triggered the crash. Also, while I will probably be interested to know the contents of your .wgetrc file, just dumping it into the debug message is probably a bad idea. Instead, you should first try to see if the bug repeats with .wgetrc moved out of the way. Only if it turns out that .wgetrc settings affect the bug, mail me the relevant parts of the file.
3. Please start Wget with ‘-d’ option and send us the resulting output (or relevant parts thereof). If Wget was compiled without debug support, recompile it—it is *much* easier to trace bugs with debug support on. Note: please make sure to remove any potentially sensitive information from the debug log before sending it to the bug address. The `-d` won’t go out of its way to collect sensitive information, but the log *will* contain a fairly complete transcript of Wget’s communication with the server, which may include passwords and pieces of downloaded data. Since the bug address is publicly archived, you may assume that all bug reports are visible to the public.
4. If Wget has crashed, try to run it in a debugger, e.g. gdb `which wget` core and type `where` to get the backtrace. This may not work if the system administrator has disabled core files, but it is safe to try.

### 8.7 Portability

Like all GNU software, Wget works on the GNU system. However, since it uses GNU Autoconf for building and configuring, and mostly avoids using “special” features of any particular Unix, it should compile (and work) on all common Unix flavors.

Various Wget versions have been compiled and tested under many kinds of Unix systems, including GNU/Linux, Solaris, SunOS 4.x, Mac OS X, OSF (aka Digital Unix or Tru64), Ultrix, *BSD, IRIX, AIX, and others. Some of those systems are no longer in widespread use and may not be able to support recent versions of Wget. If Wget fails to compile on your system, we would like to know about it.

Thanks to kind contributors, this version of Wget compiles and works on 32-bit Microsoft Windows platforms. It has been compiled successfully using MS Visual C++ 6.0, Watcom, Borland C, and GCC compilers. Naturally, it is crippled of some features available on Unix, but it should work as a substitute for people stuck with Windows. Note that Windows-specific portions of Wget are not guaranteed to be supported in the future, although this has been the case in practice for many years now. All questions and problems in Windows usage should be reported to Wget mailing list at wget@sunsite.dk where the volunteers who maintain the Windows-related features might look at them.

Support for building on MS-DOS via DJGPP has been contributed by Gisle Vanem; a port to VMS is maintained by Steven Schweda, and is available at https://antinode.info/dec/sw/wget.html.

### 8.8 Signals

Since the purpose of Wget is background work, it catches the hangup signal (`SIGHUP`) and ignores it. If the output was on standard output, it will be redirected to a file named wget-log. Otherwise, `SIGHUP` is ignored. This is convenient when you wish to redirect the output of Wget after having started it.

```
$ wget http://www.gnus.org/dist/gnus.tar.gz &
...
$ kill -HUP %%
SIGHUP received, redirecting output to `wget-log'.
```

Other than that, Wget will not try to interfere with signals in any way. C-c, `kill -TERM` and `kill -KILL` should kill it alike.


## 9 Appendices

This chapter contains some references I consider useful.

### 9.1 Robot Exclusion

It is extremely easy to make Wget wander aimlessly around a web site, sucking all the available data in progress. ‘wget -r *site*’, and you’re set. Great? Not for the server admin.

As long as Wget is only retrieving static pages, and doing it at a reasonable rate (see the ‘--wait’ option), there’s not much of a problem. The trouble is that Wget can’t tell the difference between the smallest static page and the most demanding CGI. A site I know has a section handled by a CGI Perl script that converts Info files to HTML on the fly. The script is slow, but works well enough for human users viewing an occasional Info file. However, when someone’s recursive Wget download stumbles upon the index page that links to all the Info files through the script, the system is brought to its knees without providing anything useful to the user (This task of converting Info files could be done locally and access to Info documentation for all installed GNU software on a system is available from the `info` command).

To avoid this kind of accident, as well as to preserve privacy for documents that need to be protected from well-behaved robots, the concept of *robot exclusion* was invented. The idea is that the server administrators and document authors can specify which portions of the site they wish to protect from robots and those they will permit access.

The most popular mechanism, and the *de facto* standard supported by all the major robots, is the “Robots Exclusion Standard” (RES) written by Martijn Koster et al. in 1994. It specifies the format of a text file containing directives that instruct the robots which URL paths to avoid. To be found by the robots, the specifications must be placed in /robots.txt in the server root, which the robots are expected to download and parse.

Although Wget is not a web robot in the strictest sense of the word, it can download large parts of the site without the user’s intervention to download an individual page. Because of that, Wget honors RES when downloading recursively. For instance, when you issue:

```
wget -r http://www.example.com/
```

First the index of ‘www.example.com’ will be downloaded. If Wget finds that it wants to download more documents from that server, it will request ‘http://www.example.com/robots.txt’ and, if found, use it for further downloads. robots.txt is loaded only once per each server.

Until version 1.8, Wget supported the first version of the standard, written by Martijn Koster in 1994 and available at http://www.robotstxt.org/orig.html. As of version 1.8, Wget has supported the additional directives specified in the internet draft ‘<draft-koster-robots-00.txt>’ titled “A Method for Web Robots Control”. The draft, which has as far as I know never made to an RFC, is available at http://www.robotstxt.org/norobots-rfc.txt.

This manual no longer includes the text of the Robot Exclusion Standard.

The second, less known mechanism, enables the author of an individual document to specify whether they want the links from the file to be followed by a robot. This is achieved using the `META` tag, like this:

```
<meta name="robots" content="nofollow">
```

This is explained in some detail at http://www.robotstxt.org/meta.html. Wget supports this method of robot exclusion in addition to the usual /robots.txt exclusion.

If you know what you are doing and really really wish to turn off the robot exclusion, set the `robots` variable to ‘off’ in your .wgetrc. You can achieve the same effect from the command line using the `-e` switch, e.g. ‘wget -e robots=off *url*...’.

### 9.2 Security Considerations

When using Wget, you must be aware that it sends unencrypted passwords through the network, which may present a security problem. Here are the main issues, and some solutions.

1. The passwords on the command line are visible using `ps`. The best way around it is to use `wget -i -` and feed the URLs to Wget’s standard input, each on a separate line, terminated by C-d. Another workaround is to use .netrc to store passwords; however, storing unencrypted passwords is also considered a security risk.
2. Using the insecure *basic* authentication scheme, unencrypted passwords are transmitted through the network routers and gateways.
3. The FTP passwords are also in no way encrypted. There is no good solution for this at the moment.
4. Although the “normal” output of Wget tries to hide the passwords, debugging logs show them, in all forms. This problem is avoided by being careful when you send debug logs (yes, even when you send them to me).

### 9.3 Contributors

GNU Wget was written by Hrvoje Nikšić hniksic@xemacs.org,

However, the development of Wget could never have gone as far as it has, were it not for the help of many people, either with bug reports, feature proposals, patches, or letters saying “Thanks!”.

Special thanks goes to the following people (no particular order):

- Dan Harkless—contributed a lot of code and documentation of extremely high quality, as well as the `--page-requisites` and related options. He was the principal maintainer for some time and released Wget 1.6.
- Ian Abbott—contributed bug fixes, Windows-related fixes, and provided a prototype implementation of the breadth-first recursive download. Co-maintained Wget during the 1.8 release cycle.
- The dotsrc.org crew, in particular Karsten Thygesen—donated system resources such as the mailing list, web space, FTP space, and version control repositories, along with a lot of time to make these actually work. Christian Reiniger was of invaluable help with setting up Subversion.
- Heiko Herold—provided high-quality Windows builds and contributed bug and build reports for many years.
- Shawn McHorse—bug reports and patches.
- Kaveh R. Ghazi—on-the-fly `ansi2knr`-ization. Lots of portability fixes.
- Gordon Matzigkeit—.netrc support.
- Zlatko Čalušić, Tomislav Vujec and Dražen Kačar—feature suggestions and “philosophical” discussions.
- Darko Budor—initial port to Windows.
- Antonio Rosella—help and suggestions, plus the initial Italian translation.
- Tomislav Petrović, Mario Mikočević—many bug reports and suggestions.
- Françis Pinard—many thorough bug reports and discussions.
- Karl Eichwalder—lots of help with internationalization, Makefile layout and many other things.
- Junio Hamano—donated support for Opie and HTTP `Digest` authentication.
- Mauro Tortonesi—improved IPv6 support, adding support for dual family systems. Refactored and enhanced FTP IPv6 code. Maintained GNU Wget from 2004–2007.
- Christopher G. Lewis—maintenance of the Windows version of GNU WGet.
- Gisle Vanem—many helpful patches and improvements, especially for Windows and MS-DOS support.
- Ralf Wildenhues—contributed patches to convert Wget to use Automake as part of its build process, and various bugfixes.
- Steven Schubiger—Many helpful patches, bugfixes and improvements. Notably, conversion of Wget to use the Gnulib quotes and quoteargs modules, and the addition of password prompts at the console, via the Gnulib getpasswd-gnu module.
- Ted Mielczarek—donated support for CSS.
- Saint Xavier—Support for IRIs (RFC 3987).
- Tim Rühsen—Loads of helpful patches, especially fuzzing support and Continuous Integration. Maintainer since 2014.
- Darshit Shah—Many helpful patches. Community support on various platforms. Maintainer since 2014.
- People who provided donations for development—including Brian Gough.

The following people have provided patches, bug/build reports, useful suggestions, beta testing services, fan mail and all the other things that make maintenance so much fun:

Tim Adam, Adrian Aichner, Martin Baehr, Dieter Baron, Roger Beeman, Dan Berger, T. Bharath, Christian Biere, Paul Bludov, Daniel Bodea, Mark Boyns, John Burden, Julien Buty, Wanderlei Cavassin, Gilles Cedoc, Tim Charron, Noel Cragg, Kristijan Čonkaš, John Daily, Andreas Damm, Ahmon Dancy, Andrew Davison, Bertrand Demiddelaer, Alexander Dergachev, Andrew Deryabin, Ulrich Drepper, Marc Duponcheel, Damir Džeko, Alan Eldridge, Hans-Andreas Engel, Aleksandar Erkalović, Andy Eskilsson, João Ferreira, Christian Fraenkel, David Fritz, Mike Frysinger, Charles C. Fu, FUJISHIMA Satsuki, Masashi Fujita, Howard Gayle, Marcel Gerrits, Lemble Gregory, Hans Grobler, Alain Guibert, Mathieu Guillaume, Aaron Hawley, Jochen Hein, Karl Heuer, Madhusudan Hosaagrahara, HIROSE Masaaki, Ulf Harnhammar, Gregor Hoffleit, Erik Magnus Hulthen, Richard Huveneers, Jonas Jensen, Larry Jones, Simon Josefsson, Mario Jurić, Hack Kampbjørn, Const Kaplinsky, Goran Kezunović, Igor Khristophorov, Robert Kleine, KOJIMA Haime, Fila Kolodny, Alexander Kourakos, Martin Kraemer, Sami Krank, Jay Krell, Σίμος Ξενιτέλλης (Simos KSenitellis), Christian Lackas, Hrvoje Lacko, Daniel S. Lewart, Nicolás Lichtmeier, Dave Love, Alexander V. Lukyanov, Thomas Lußnig, Andre Majorel, Aurelien Marchand, Matthew J. Mellon, Jordan Mendelson, Ted Mielczarek, Robert Millan, Lin Zhe Min, Jan Minar, Tim Mooney, Keith Moore, Adam D. Moss, Simon Munton, Charlie Negyesi, R. K. Owen, Jim Paris, Kenny Parnell, Leonid Petrov, Simone Piunno, Andrew Pollock, Steve Pothier, Jan Přikryl, Marin Purgar, Csaba Ráduly, Keith Refson, Bill Richardson, Tyler Riddle, Tobias Ringstrom, Jochen Roderburg, Juan José Rodríguez, Maciej W. Rozycki, Edward J. Sabol, Heinz Salzmann, Robert Schmidt, Nicolas Schodet, Benno Schulenberg, Andreas Schwab, Steven M. Schweda, Chris Seawood, Pranab Shenoy, Dennis Smit, Toomas Soome, Tage Stabell-Kulo, Philip Stadermann, Daniel Stenberg, Sven Sternberger, Markus Strasser, John Summerfield, Szakacsits Szabolcs, Mike Thomas, Philipp Thomas, Mauro Tortonesi, Dave Turner, Gisle Vanem, Rabin Vincent, Russell Vincent, Željko Vrba, Charles G Waldman, Douglas E. Wegscheid, Ralf Wildenhues, Joshua David Williams, Benjamin Wolsey, Saint Xavier, YAMAZAKI Makoto, Jasmin Zainul, Bojan Ždrnja, Kristijan Zimmer, Xin Zou.

Apologies to all who I accidentally left out, and many thanks to all the subscribers of the Wget mailing list.
