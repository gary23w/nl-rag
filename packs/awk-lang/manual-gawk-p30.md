---
title: "The GNU Awk User’s Guide (part 30/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 30/38
---

## Appendix B Installing `gawk`

This appendix provides instructions for installing `gawk` on the various platforms that are supported by the developers. The primary developer supports GNU/Linux (and Unix), whereas the other ports are contributed. See Reporting Problems and Bugs for the email addresses of the people who maintain the respective ports.

### B.1 The `gawk` Distribution

This section describes how to get the `gawk` distribution, how to extract it, and then what is in the various files and subdirectories.

#### B.1.1 Getting the `gawk` Distribution

There are two ways to get GNU software:

- Copy it from someone else who already has it.
- Retrieve `gawk` from the Internet host `ftp.gnu.org`, in the directory /gnu/gawk. Both anonymous `ftp` and `http` access are supported. If you have the `wget` program, you can use a command like the following: wget https://ftp.gnu.org/gnu/gawk/gawk-5.4.0.tar.gz

The GNU software archive is mirrored around the world. The up-to-date list of mirror sites is available from the main FSF website. Try to use one of the mirrors; they will be less busy, and you can usually find one closer to your site.

You may also retrieve the `gawk` source code from the official Git repository; for more information see Accessing The `gawk` Git Repository.

#### B.1.2 Extracting the Distribution

`gawk` is distributed as several `tar` files compressed with different compression programs: `gzip`, `bzip2`, and `xz`. For simplicity, the rest of these instructions assume you are using the one compressed with the GNU Gzip program (`gzip`).

Once you have the distribution (e.g., gawk-5.4.0.tar.gz), use `gzip` to expand the file and then use `tar` to extract it. You can use the following pipeline to produce the `gawk` distribution:

```
gzip -d -c gawk-5.4.0.tar.gz | tar -xvpf -
```

On a system with GNU `tar`, you can let `tar` do the decompression for you:

```
tar -xvpzf gawk-5.4.0.tar.gz
```

Extracting the archive creates a directory named gawk-5.4.0 in the current directory.

The distribution file name is of the form gawk-*V*.*R*.*P*.tar.gz. The *V* represents the major version of `gawk`, the *R* represents the current release of version *V*, and the *P* represents a *patch level*, meaning that minor bugs have been fixed in the release. The current patch level is 0, but when retrieving distributions, you should get the version with the highest version, release, and patch level. (Note, however, that patch levels greater than or equal to 60 denote “beta” or nonproduction software; you might not want to retrieve such a version unless you don’t mind experimenting.) If you are not on a Unix or GNU/Linux system, you need to make other arrangements for getting and extracting the `gawk` distribution. You should consult a local expert.

### B.2 Compiling and Installing `gawk` on Unix-Like Systems

Usually, you can compile and install `gawk` by typing only two commands. However, if you use an unusual system, you may need to configure `gawk` for your system yourself.

#### B.2.1 Compiling `gawk` for Unix-Like Systems

The normal installation steps should work on all modern commercial Unix-derived systems, GNU/Linux, BSD-based systems, and the Cygwin environment for MS-Windows.

After you have extracted the `gawk` distribution, `cd` to gawk-5.4.0. As with most GNU software, you configure `gawk` for your system by running the `configure` program. This program is a Bourne shell script that is generated automatically using GNU Autoconf. (The Autoconf software is described fully in *Autoconf—Generating Automatic Configuration Scripts*, which can be found online at the Free Software Foundation’s website.)

To configure `gawk`, simply run `configure`:

```
sh ./configure
```

This produces a Makefile and config.h tailored to your system. The config.h file describes various facts about your system. You might want to edit the Makefile to change the `CFLAGS` variable, which controls the command-line options that are passed to the C compiler (such as optimization levels or compiling for debugging).

Alternatively, you can add your own values for most `make` variables on the command line, such as `CC` and `CFLAGS`, when running `configure`:

```
CC=cc CFLAGS=-g sh ./configure
```

See the file INSTALL in the `gawk` distribution for all the details.

After you have run `configure` and possibly edited the Makefile, type:

```
make
```

Shortly thereafter, you should have an executable version of `gawk`. That’s all there is to it! To verify that `gawk` is working properly, run ‘make check’. All of the tests should succeed. If these steps do not work, or if any of the tests fail, check the files in the README_d directory to see if you’ve found a known problem. If the failure is not described there, send in a bug report (see Reporting Problems and Bugs).

Of course, once you’ve built `gawk`, it is likely that you will wish to install it. To do so, you need to run the command ‘make install’, as a user with the appropriate permissions. How to do this varies by system, but on many systems you can use the `sudo` command to do so. The command then becomes ‘sudo make install’. It is likely that you will be asked for your password, and you will have to have been set up previously as a user who is allowed to run the `sudo` command.

#### B.2.1.1 Building With MPFR

Use of the MPFR library with `gawk` is an optional feature: if you have the MPFR and GMP libraries already installed when you configure and build `gawk`, `gawk` automatically will be able to use them.

You can install these libraries from source code by fetching them from the GNU distribution site at `ftp.gnu.org`.

Most modern systems provide package managers which save you the trouble of building from source. They fetch and install the library header files and binaries for you. You will need to research how to do this for your particular system.

#### B.2.2 Shell Startup Files

The distribution contains shell startup files gawk.sh and gawk.csh, containing functions to aid in manipulating the `AWKPATH` and `AWKLIBPATH` environment variables. On a Fedora GNU/Linux system, these files should be installed in /etc/profile.d; on other platforms, the appropriate location may be different.

**`gawkpath_default`**

Reset the `AWKPATH` environment variable to its default value.

**`gawkpath_prepend`**

Add the argument to the front of the `AWKPATH` environment variable.

**`gawkpath_append`**

Add the argument to the end of the `AWKPATH` environment variable.

**`gawklibpath_default`**

Reset the `AWKLIBPATH` environment variable to its default value.

**`gawklibpath_prepend`**

Add the argument to the front of the `AWKLIBPATH` environment variable.

**`gawklibpath_append`**

Add the argument to the end of the `AWKLIBPATH` environment variable.

#### B.2.3 Additional Configuration Options

There are several additional options you may use on the `configure` command line when compiling `gawk` from scratch, including:

**`--disable-extensions`**

Disable the extension mechanism within `gawk`. With this option, it is not possible to use dynamic extensions. This also disables configuring and building the sample extensions in the extension directory.

This option may be useful for cross-compiling. The default action is to dynamically check if the extensions can be configured and compiled.

**`--disable-lint`**

Disable all lint checking within `gawk`. The --lint and --lint-old options (see Command-Line Options) are accepted, but silently do nothing. Similarly, setting the `LINT` variable (see Built-in Variables That Control `awk`) has no effect on the running `awk` program.

When used with the GNU Compiler Collection’s (GCC’s) automatic dead-code-elimination, this option cuts almost 23K bytes off the size of the `gawk` executable on GNU/Linux x86_64 systems. Results on other systems and with other compilers are likely to vary. Using this option may bring you some slight performance improvement.

> **CAUTION:** Using this option will cause some of the tests in the test suite to fail. This option may be removed at a later date.

**`--disable-mpfr`**

Skip checking for the MPFR and GMP libraries. This is useful mainly for the developers, to make sure nothing breaks if MPFR support is not available.

**`--disable-nls`**

Disable all message-translation facilities. This is usually not desirable, but it may bring you some slight performance improvement.

**`--enable-builtin-intdiv0`**

Add a new built-in function, `intdiv0()`, which generates integer division and remainder results at the same time. This is discussed more in Arbitrary-Precision Integer Arithmetic with `gawk`.

**`--enable-O3`**

Use the GCC option -O3 when compiling `gawk` instead of the standard -O2. The additional optimizations may improve `gawk`’s performance. However, in other projects, -O3 has been known to cause bugs, thus its use is not the default.

**`--enable-versioned-extension-dir`**

Use a versioned directory for extensions. The directory name will include the major and minor API versions in it. This makes it possible to keep extensions for different API versions on the same system without their conflicting with one another.

Use the command ‘./configure --help’ to see the full list of options supplied by `configure`.

#### B.2.4 The Configuration Process

This section is of interest only if you know something about using the C language and Unix-like operating systems.

The source code for `gawk` generally attempts to adhere to formal standards wherever possible. This means that `gawk` uses library routines that are specified by the ISO C standard and by the POSIX operating system interface standard. The `gawk` source code requires using an ISO C compiler (the 1999 standard).

Many Unix systems do not support all of either the ISO or the POSIX standards. The missing_d subdirectory in the `gawk` distribution contains replacement versions of those functions that are most likely to be missing.

The config.h file that `configure` creates contains definitions that describe features of the particular operating system where you are attempting to compile `gawk`. The three things described by this file are: what header files are available, so that they can be correctly included, what (supposedly) standard functions are actually available in your C libraries, and various miscellaneous facts about your operating system. For example, there may not be an `st_blksize` element in the `stat` structure. In this case, ‘HAVE_STRUCT_STAT_ST_BLKSIZE’ is undefined.

It is possible for your C compiler to lie to `configure`. It may do so by not exiting with an error when a library function is not available. To get around this, edit the custom.h file. Use an ‘#ifdef’ that is appropriate for your system, and either `#define` any constants that `configure` should have defined but didn’t, or `#undef` any constants that `configure` defined and should not have. The custom.h file is automatically included by the config.h file.

It is also possible that the `configure` program generated by Autoconf will not work on your system in some other fashion. If you do have a problem, the configure.ac file is the input for Autoconf. You may be able to change this file and generate a new version of `configure` that works on your system (see Reporting Problems and Bugs for information on how to report problems in configuring `gawk`). The same mechanism may be used to send in updates to configure.ac and/or custom.h.

#### B.2.5 Compiling from Git

Building `gawk` directly from the development source control repository is possible, but not recommended for everyday users, as the code may not be as stable as released versions are. If you really do want to do that, here are the steps:

```
git clone https://git.savannah.gnu.org/git/gawk.git
cd gawk
./bootstrap.sh && ./configure && make && make check
```

#### B.2.6 Building the Documentation

The generated Info documentation is included in the distribution `tar` files; you should not need to rebuild it. However, if it needs to be done, simply running `make` will do it, assuming that you have a recent enough version of `makeinfo` installed.

If you wish to build the PDF version of the manuals, you will need to have TeX installed, and possibly additional packages that provide the necessary fonts and tools, such as `dvi2pdf` and `ps2pdf`. You will also need GNU Troff (`groff`) installed in order to format the reference card and the manual page (see Contents of the `gawk` Distribution). Managing this process is beyond the scope of this Web page.

Assuming you have all you need, then the following commands produce the PDF versions of the documentation:

```
cd doc
make pdf
```

This creates PDF versions of all three Texinfo documents included in the distribution, as well as of the manual page and the reference card.

Similarly, if you have a recent enough version of `makeinfo`, you can make the HTML version of the manuals with:

```
cd doc
make html
```

This creates HTML versions of all three Texinfo documents included in the distribution.

### B.3 Installation on Other Operating Systems

This section describes how to install `gawk` on various non-Unix systems.

#### B.3.1 Installation on MS-Windows

This section covers installation and usage of `gawk` on Intel architecture machines running any version of MS-Windows. In this section, the term “Windows32” refers to any of Microsoft Windows 95/98/ME/NT/2000/XP/Vista/7/8/10/11.

See also the README_d/README.pc file in the distribution.

#### B.3.1.1 Installing a Prepared Distribution for MS-Windows Systems

The only supported binary distribution for MS-Windows systems is that provided by Eli Zaretskii’s “ezwinports” project. Install the compiled `gawk` from there. Note that to run that port, you need to have the libgcc_s_dw2-1.dll file installed on your system. This file is part of the GCC distribution, and should reside either in the same directory where you install gawk.exe or somewhere on your system’s `Path`. You can download this file from the MinGW site; look under the “MinGW.org Compiler Collection (GCC)” for the `LibGCC-1.DLL` download.

#### B.3.1.2 Compiling `gawk` for PC Operating Systems

`gawk` can be compiled for Windows32 using MinGW (Windows32). The file README_d/README.pc in the `gawk` distribution contains additional notes, and pc/Makefile contains important information on compilation options.

To build `gawk` for Windows32, copy the files in the pc directory (*except* for ChangeLog) to the directory with the rest of the `gawk` sources, then invoke `make` with the appropriate target name as an argument to build `gawk`. The Makefile copied from the pc directory contains a configuration section with comments and may need to be edited in order to work with your `make` utility.

The Makefile supports a number of targets for building various Windows32 versions. A list of targets is printed if the `make` command is given without a target. As an example, to build a native MS-Windows binary of `gawk` using the MinGW tools, type ‘make mingw32’.

If you are building with MinGW using anything other than pc/Makefile, be sure to pass the -D__USE_MINGW_ANSI_STDIO command-line option to GCC. This is necessary for correct operation of Gawk on Windows, in particular for displaying translated messages.

#### B.3.1.3 Using `gawk` on PC Operating Systems

Information in this section applies to the MinGW port of `gawk` for MS-Windows. See Using `gawk` In The Cygwin Environment for information about the Cygwin port.

The MS-Windows version of `gawk` searches for program files as described in The `AWKPATH` Environment Variable. However, semicolons (rather than colons) separate elements in the `AWKPATH` variable. If `AWKPATH` is not set or is empty, then the default search path is ‘.;d:/usr/lib/awk;c:/lib/awk;c:/gnu/lib/awk’.

Similarly, the `AWKLIBPATH` environment variable, which tells `gawk` where to look for dynamic extensions (see Writing Extensions for `gawk`), also uses semicolons to separate directories. If not set in the environment, the default value hard-coded into `gawk` is ‘d:/usr/lib/gawk/ext-*api-version*’, where *api-version* is the version of gawk API version for which `gawk` was compiled (see API Version Constants and Variables).

MS-Windows traditionally supported internationalization and localization via *codepages*. Each Windows locale specifies a system-wide codepage, which defines both the non-ASCII characters supported by Windows and their encoding into small integer values. Most Windows locales use a single-byte encoding; the notable exceptions are CJK (Chinese, Japanese, and Korean) codepages which use one or two bytes for each non-ASCII character. Recent versions of MS-Windows also support Unicode and the UTF-8 encoding, but introduction of this support is slow: as of this writing, setting UTF-8 as the system-wide codepage on Windows is still considered an experimental feature, which by default is turned off. The Windows designation of the UTF-8 encoding is known as *codepage 65001*.

The MinGW build of `gawk` for MS-Windows supports multibyte characters according to the codepage defined by the current system locale, and it also includes (starting with version 5.4) reasonable support for text encoded in UTF-8. When the system’s codepage is anything other than 65001, `gawk` uses the functions from the MS-Windows C runtime library to convert between multibyte and wide-character representation of text, and for character classification and collation; this is in most cases limited to characters inside the Unicode Basic Multilingual Plane (BMP), due to the limitations of the Windows runtime. By contrast, if the system’s codepage is set to 65001, `gawk` attempts to support the full range of Unicode codepoints, including the BMP and all the 16 Supplementary Planes defined by Unicode, by using its own conversion and classification routines instead of those in the Windows C runtime. (This might still fail to work as well as it does on modern POSIX systems, because these routines rely on the character database data included with your Windows installation.)

When codepage 65001 is used, `gawk` uses UTF-8 to encode multibyte text, and converts between UTF-8 and 32-bit Unicode codepoints internally. Thus on Windows, to make sure `awk` programs written for POSIX systems which handle multibyte non-ASCII text work correctly on MS-Windows, you should use codepage 65001.

As a special feature, `gawk` version 5.4 and later will use UTF-8 internally even when the system-wide codepage is something other than 65001, if `gawk` detects that the Windows terminal window in which it runs uses codepage 65001 for console output. (Unlike on POSIX systems, Windows users can change the console encoding independently of the system-wide locale’s encoding.) To switch the Windows terminal to using UTF-8 encoding, type ‘chcp 65001’ at the Windows shell’s prompt. This causes `gawk` on Windows to support the full range of Unicode characters even without changing the system-wide locale’s codepage. We recommend that you use codepage 65001 on Windows 11 and later systems, where the Windows terminal supports UTF-8 quite well.

Note that `gawk` on Windows will still treat all input data as single-byte characters when invoked with the -b command-line option (see Command-Line Options), or when running under the `"C"` locale (i.e., when the `LC_ALL` environment variable is set to the value ‘C’ by typing ‘set LC_ALL=C’ at the shell prompt before invoking `gawk`). This overrides the codepage-defined encoding of text.

Under MS-Windows, `gawk` (and many other text programs) silently translates end-of-line ‘\r\n’ to ‘\n’ on input and ‘\n’ to ‘\r\n’ on output. A special `BINMODE` variable (c.e.) allows control over these translations and is interpreted as follows:

- If `BINMODE` is `"r"` or one, then binary mode is set on read (i.e., no translations on reads).
- If `BINMODE` is `"w"` or two, then binary mode is set on write (i.e., no translations on writes).
- If `BINMODE` is `"rw"` or `"wr"` or three, binary mode is set for both read and write.
- `BINMODE=*non-null-string*` is the same as ‘BINMODE=3’ (i.e., no translations on reads or writes). However, `gawk` issues a warning message if the string is not one of `"rw"` or `"wr"`.

The modes for standard input and standard output are set one time only (after the command line is read, but before processing any of the `awk` program). Setting `BINMODE` for standard input or standard output is accomplished by using an appropriate ‘-v BINMODE=*N*’ option on the command line. `BINMODE` is set at the time a file or pipe is opened and cannot be changed midstream.

On POSIX-compatible systems, this variable’s value has no effect. Thus, if you think your program will run on multiple different systems and that you may need to use `BINMODE`, you should simply set it (in the program or on the command line) unconditionally, and not worry about the operating system on which your program is running.

The name `BINMODE` was chosen to match `mawk` (see Other Freely Available `awk` Implementations). `mawk` and `gawk` handle `BINMODE` similarly; however, `mawk` adds a ‘-W BINMODE=*N*’ option and an environment variable that can set `BINMODE`, `RS`, and `ORS`. The files binmode[1-3].awk (under gnu/lib/awk in some of the prepared binary distributions) have been chosen to match `mawk`’s ‘-W BINMODE=*N*’ option. These can be changed or discarded; in particular, the setting of `RS` giving the fewest “surprises” is open to debate. `mawk` uses ‘RS = "\r\n"’ if binary mode is set on read, which is appropriate for files with the MS-DOS-style end-of-line.

To illustrate, the following examples set binary mode on writes for standard output and other files, and set `ORS` as the “usual” MS-DOS-style end-of-line:

```
gawk -v BINMODE=2 -v ORS="\r\n" ...
```

or:

```
gawk -v BINMODE=w -f binmode2.awk ...
```

These give the same result as the ‘-W BINMODE=2’ option in `mawk`. The following changes the record separator to `"\r\n"` and sets binary mode on reads, but does not affect the mode on standard input:

```
gawk -v RS="\r\n" -e "BEGIN { BINMODE = 1 }" ...
```

or:

```
gawk -f binmode1.awk ...
```

With proper quoting, in the first example the setting of `RS` can be moved into the `BEGIN` rule.

Under MS-Windows, the MinGW port of `gawk` supports both the ‘|&’ operator and TCP/IP networking (see Using `gawk` for Network Programming).

#### B.3.1.4 Using `gawk` In The Cygwin Environment

`gawk` can be built and used “out of the box” under MS-Windows if you are using the Cygwin environment. This environment provides an excellent simulation of GNU/Linux, using Bash, GCC, GNU Make, and other GNU programs. Compilation and installation for Cygwin is the same as for a Unix system:

```
tar -xvpzf gawk-5.4.0.tar.gz
cd gawk-5.4.0
./configure
make && make check
```

When compared to GNU/Linux on the same system, the ‘configure’ step on Cygwin takes considerably longer. However, it does finish, and then the ‘make’ proceeds as usual.

You may also install `gawk` using the regular Cygwin installer. In general Cygwin supplies the latest released version.

Recent versions of Cygwin open all files in binary mode. This means that you should use ‘RS = "\r?\n"’ in order to be able to handle standard MS-Windows text files with carriage-return plus line-feed line endings.

The Cygwin environment supports both the ‘|&’ operator and TCP/IP networking (see Using `gawk` for Network Programming).

#### B.3.1.5 Using `gawk` In The MSYS Environment

In the MSYS environment under MS-Windows, `gawk` automatically uses binary mode for reading and writing files. Thus, there is no need to use the `BINMODE` variable.

This can cause problems with other Unix-like components that have been ported to MS-Windows that expect `gawk` to do automatic translation of `"\r\n"`, because it won’t.

Under MSYS2, compilation using the standard ‘./configure && make’ recipe works “out of the box.”

#### B.3.2 Compiling and Installing `gawk` on OpenVMS

This subsection describes how to compile and install `gawk` under OpenVMS.

#### B.3.2.1 Compiling `gawk` on OpenVMS

To compile `gawk` under OpenVMS, there is a descrip.mms for use with `MMK` or `MMS` as the equivalent of a makefile. `MMS` requires a DCL symbol for the hardware type such ‘"__x86_64__ = "TRUE"’ to properly build.

```
$ __x86_64__ == "TRUE"
$ MMS/DESCRIPTION=[.vms]descrip.mms gawk
```

or:

```
$ MMK/DESCRIPTION=[.vms]descrip.mms gawk
```

`MMK` is an open source, free, near-clone of `MMS` and can better handle ODS-5 volumes with upper- and lowercase file names. `MMK` is available from https://github.com/endlesssoftware/mmk.

With ODS-5 volumes and extended parsing enabled, the case of the target parameter may need to be exact.

`gawk` has been tested using these VMS Software, Inc. Community editions:

- VSI C x86-64 V7.6-001 (GEM 50YAN) on OpenVMS x86_64 V9.2-3
- HP C V7.3-010 on OpenVMS Alpha V8.4-2L1.
- HP C V7.3-020 on OpenVMS IA64 V8.4-2L3.121

Due to HPE cancelling the Hobbyist licensing program, no more testing is being done on older releases of OpenVMS.

See The OpenVMS GNV Project for information on building `gawk` as a PCSI kit that is compatible with the GNV product.

#### B.3.2.2 Compiling `gawk` Dynamic Extensions on OpenVMS

The extensions that have been ported to OpenVMS can be built using one of the following commands:

```
$ __x86_64__ == "TRUE"
$ MMS/DESCRIPTION=[.vms]descrip.mms extensions
```

or:

```
$ MMK/DESCRIPTION=[.vms]descrip.mms extensions
```

`gawk` uses `AWKLIBPATH` as either an environment variable or a logical name to find the dynamic extensions.

Dynamic extensions need to be compiled with the same compiler options for floating-point, pointer size, and symbol name handling as were used to compile `gawk` itself. X86_64, Alpha, and Itanium should use IEEE floating point. The pointer size is 32 bits, and the symbol name handling should be exact case with CRC shortening for symbols longer than 32 bits.

```
/name=(as_is,short)
/float=ieee/ieee_mode=denorm_results
```

Compile-time macros need to be defined before the first OpenVMS-supplied header file is included, as follows:

```
#if (__CRTL_VER >= 70200000)
#define _LARGEFILE 1
#endif

#ifdef __CRTL_VER
#if __CRTL_VER >= 80200000
#define _USE_STD_STAT 1
#endif
#endif
```

If you are writing your own extensions to run on OpenVMS, you must supply these definitions yourself. The config.h file created when building `gawk` on OpenVMS does this for you; if instead you use that file or a similar one, then you must remember to include it before any OpenVMS-supplied header files.

#### B.3.2.3 Installing `gawk` on OpenVMS

To use `gawk`, all you need is a “foreign” command, which is a `DCL` symbol whose value begins with a dollar sign. For example:

```
$ GAWK :== $disk1:[gnubin]gawk
```

Substitute the actual location of `gawk.exe` for ‘$disk1:[gnubin]’. The symbol should be placed in the login.com of any user who wants to run `gawk`, so that it is defined every time the user logs on. Alternatively, the symbol may be placed in the system-wide sylogin.com procedure, which allows all users to run `gawk`.

If your `gawk` was installed by a PCSI kit into the GNV$GNU: directory tree, the program will be known as GNV$GNU:[bin]gnv$gawk.exe and the help file will be GNV$GNU:[vms_help]gawk.hlp.

The PCSI kit also installs a GNV$GNU:[vms_bin]gawk_verb.cld file that can be used to add `gawk` and `awk` as DCL commands.

For just the current process you can use:

```
$ set command gnv$gnu:[vms_bin]gawk_verb.cld
```

Or the system manager can use GNV$GNU:[vms_bin]gawk_verb.cld to add the `gawk` and `awk` commands to the system-wide ‘DCLTABLES’.

The DCL syntax is documented in the gawk.hlp file.

Optionally, the gawk.hlp entry can be loaded into an OpenVMS help library:

```
$ LIBRARY/HELP sys$help:helplib [.vms]gawk.hlp
```
