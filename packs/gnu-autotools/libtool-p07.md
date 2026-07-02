---
title: "Libtool (part 7/8)"
source: https://www.gnu.org/software/libtool/manual/libtool.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 7/8
---

## 15 Maintenance notes for libtool

This chapter contains information that the libtool maintainer finds important. It will be of no use to you unless you are considering porting libtool to new systems, or writing your own libtool.

### 15.1 Porting libtool to new systems

Before you embark on porting libtool to an unsupported system, it is worthwhile to send e-mail to the Libtool mailing list libtool@gnu.org, to make sure that you are not duplicating existing work.

If you find that any porting documentation is missing, please complain! Complaints with patches and improvements to the documentation, or to libtool itself, are more than welcome.

#### 15.1.1 Information sources

Once it is clear that a new port is necessary, you’ll generally need the following information:

**canonical system name**

You need the output of `config.guess` for this system, so that you can make changes to the libtool configuration process without affecting other systems.

**man pages for `ld` and `cc`**

These generally describe what flags are used to generate PIC, to create shared libraries, and to link against only static libraries. You may need to follow some cross references to find the information that is required.

**man pages for `ld.so`, `rtld`, or equivalent**

These are a valuable resource for understanding how shared libraries are loaded on the system.

**man page for `ldconfig`, or equivalent**

This page usually describes how to install shared libraries.

**output from ls -l /lib /usr/lib**

This shows the naming convention for shared libraries on the system, including what names should be symbolic links.

**any additional documentation**

Some systems have special documentation on how to build and install shared libraries.

If you know how to program the Bourne shell, then you can complete the port yourself; otherwise, you’ll have to find somebody with the relevant skills who will do the work. People on the libtool mailing list are usually willing to volunteer to help you with new ports, so you can send the information to them.

To do the port yourself, you’ll definitely need to modify the `libtool.m4` macros to make platform-specific changes to the configuration process. You should search that file for the `PORTME` keyword, which will give you some hints on what you’ll need to change. In general, all that is involved is modifying the appropriate configuration variables (see `libtool` script contents).

Your best bet is to find an already-supported system that is similar to yours, and make your changes based on that. In some cases, however, your system will differ significantly from every other supported system, and it may be necessary to add new configuration variables, and modify the `ltmain.in` script accordingly. Be sure to write to the mailing list before you make changes to `ltmain.in`, since they may have advice on the most effective way of accomplishing what you want.

#### 15.1.2 Porting inter-library dependencies support

Since version 1.2c, libtool has re-introduced the ability to do inter-library dependency on some platforms, thanks to a patch by Toshio Kuratomi badger@prtr-13.ucsc.edu. Here’s a shortened version of the message that contained his patch:

The basic architecture is this: in libtool.m4, the person who writes libtool makes sure ‘$deplibs’ is included in ‘$archive_cmds’ somewhere and also sets the variable ‘$deplibs_check_method’, and maybe ‘$file_magic_cmd’ when ‘deplibs_check_method’ is file_magic.

‘deplibs_check_method’ can be one of five things:

**‘file_magic [*regex*]’ ¶**

looks in the library link path for libraries that have the right libname. Then it runs ‘$file_magic_cmd’ on the library and checks for a match against the extended regular expression *regex*. When `file_magic_test_file` is set by libtool.m4, it is used as an argument to ‘$file_magic_cmd’ to verify whether the regular expression matches its output, and warn the user otherwise.

**‘pass_all’ ¶**

will pass everything without any checking. This may work on platforms where code is position-independent by default and inter-library dependencies are properly supported by the dynamic linker, for example, on DEC OSF/1 3 and 4.

**‘none’ ¶**

It causes deplibs to be reassigned ‘deplibs=""’. That way ‘archive_cmds’ can contain deplibs on all platforms, but not have deplibs used unless needed.

**‘unknown’ ¶**

is the default for all systems unless overridden in libtool.m4. It is the same as ‘none’, but it documents that we really don’t know what the correct value should be, and we welcome patches that improve it.

Then in ltmain.in we have the real workhorse: a little initialization and postprocessing (to setup/release variables for use with eval echo libname_spec etc.) and a case statement that decides the method that is being used. This is the real code… I wish I could condense it a little more, but I don’t think I can without function calls. I’ve mostly optimized it (moved things out of loops, etc.) but there is probably some fat left. I thought I should stop while I was ahead, work on whatever bugs you discover, etc. before thinking about more than obvious optimizations.

### 15.2 Tested platforms

This table describes when libtool was last known to be tested on platforms where it claims to support shared libraries:

```
-------------------------------------------------------
canonical host name          compiler  libtool results
  (tools versions)                     release
-------------------------------------------------------
alpha-dec-osf5.1		cc	 1.3e	  ok (1.910)
alpha-dec-osf4.0f               gcc      1.3e     ok (1.910)
alpha-dec-osf4.0f               cc       1.3e     ok (1.910)
alpha-dec-osf3.2                gcc      0.8      ok
alpha-dec-osf3.2                cc       0.8      ok
alpha-dec-osf2.1                gcc      1.2f     NS
alpha*-unknown-linux-gnu        gcc      1.3b     ok
  (egcs-1.1.2, GNU ld 2.9.1.0.23)
hppa2.0w-hp-hpux11.00           cc       1.2f     ok
hppa2.0-hp-hpux10.20            cc       1.3.2    ok
hppa1.1-hp-hpux10.20            gcc      1.2f     ok
hppa1.1-hp-hpux10.20            cc       1.3c     ok (1.821)
hppa1.1-hp-hpux10.10            gcc      1.2f     ok
hppa1.1-hp-hpux10.10            cc       1.2f     ok
hppa1.1-hp-hpux9.07             gcc      1.2f     ok
hppa1.1-hp-hpux9.07             cc       1.2f     ok
hppa1.1-hp-hpux9.05             gcc      1.2f     ok
hppa1.1-hp-hpux9.05             cc       1.2f     ok
hppa1.1-hp-hpux9.01             gcc      1.2f     ok
hppa1.1-hp-hpux9.01             cc       1.2f     ok
i*86-*-beos                     gcc      1.2f     ok
i*86-*-bsdi4.0.1                gcc      1.3c     ok
  (gcc-2.7.2.1)
i*86-*-bsdi4.0                  gcc      1.2f     ok
i*86-*-bsdi3.1                  gcc      1.2e     NS
i*86-*-bsdi3.0                  gcc      1.2e     NS
i*86-*-bsdi2.1                  gcc      1.2e     NS
i*86-pc-cygwin                  gcc      1.3b     NS
  (egcs-1.1 stock b20.1 compiler)
i*86-*-dguxR4.20MU01            gcc      1.2      ok
i*86-*-freebsd4.3		gcc      1.3e     ok (1.912)
i*86-*-freebsdelf4.0            gcc      1.3c     ok
  (egcs-1.1.2)
i*86-*-freebsdelf3.2            gcc      1.3c     ok
  (gcc-2.7.2.1)
i*86-*-freebsdelf3.1            gcc      1.3c     ok
  (gcc-2.7.2.1)
i*86-*-freebsdelf3.0            gcc      1.3c     ok
i*86-*-freebsd3.0               gcc      1.2e     ok
i*86-*-freebsd2.2.8             gcc      1.3c     ok
  (gcc-2.7.2.1)
i*86-*-freebsd2.2.6             gcc      1.3b     ok
  (egcs-1.1 & gcc-2.7.2.1, native ld)
i*86-*-freebsd2.1.5             gcc      0.5      ok
i*86-*-netbsd1.5                gcc      1.3e     ok (1.901)
  (egcs-1.1.2)
i*86-*-netbsd1.4                gcc      1.3c     ok
  (egcs-1.1.1)
i*86-*-netbsd1.4.3A             gcc      1.3e     ok (1.901)
i*86-*-netbsd1.3.3              gcc      1.3c     ok
  (gcc-2.7.2.2+myc2)
i*86-*-netbsd1.3.2              gcc      1.2e     ok
i*86-*-netbsd1.3I               gcc      1.2e     ok
  (egcs 1.1?)
i*86-*-netbsd1.2                gcc      0.9g     ok
i*86-*-linux-gnu		gcc	 1.3e	  ok (1.901)
  (Red Hat 7.0, gcc "2.96")
i*86-*-linux-gnu		gcc	 1.3e	  ok (1.911)
  (SuSE 7.0, gcc 2.95.2)
i*86-*-linux-gnulibc1           gcc      1.2f     ok
i*86-*-openbsd2.5               gcc      1.3c     ok
  (gcc-2.8.1)
i*86-*-openbsd2.4               gcc      1.3c     ok
  (gcc-2.8.1)
i*86-*-solaris2.7               gcc      1.3b     ok
  (egcs-1.1.2, native ld)
i*86-*-solaris2.6               gcc      1.2f     ok
i*86-*-solaris2.5.1             gcc      1.2f     ok
i*86-ncr-sysv4.3.03             gcc      1.2f     ok
i*86-ncr-sysv4.3.03             cc       1.2e     ok
  (cc -Hnocopyr)
i*86-pc-sco3.2v5.0.5		cc	 1.3c	  ok
i*86-pc-sco3.2v5.0.5		gcc	 1.3c	  ok
  (gcc 95q4c)
i*86-pc-sco3.2v5.0.5		gcc	 1.3c	  ok
  (egcs-1.1.2)
i*86-sco-sysv5uw7.1.1		gcc	 1.3e	  ok (1.901)
  (gcc-2.95.2, SCO linker)
i*86-UnixWare7.1.0-sysv5	cc	 1.3c	  ok
i*86-UnixWare7.1.0-sysv5	gcc	 1.3c	  ok
  (egcs-1.1.1)
m68k-next-nextstep3             gcc      1.2f     NS
m68k-sun-sunos4.1.1             gcc      1.2f     NS
  (gcc-2.5.7)
m88k-dg-dguxR4.12TMU01          gcc      1.2      ok
m88k-motorola-sysv4             gcc      1.3      ok
  (egcs-1.1.2)
mips-sgi-irix6.5                gcc      1.2f     ok
  (gcc-2.8.1)
mips-sgi-irix6.4                gcc      1.2f     ok
mips-sgi-irix6.3                gcc      1.3b     ok
  (egcs-1.1.2, native ld)
mips-sgi-irix6.3                cc       1.3b     ok
  (cc 7.0)
mips-sgi-irix6.2                gcc      1.2f     ok
mips-sgi-irix6.2                cc       0.9      ok
mips-sgi-irix5.3                gcc      1.2f     ok
  (egcs-1.1.1)
mips-sgi-irix5.3                gcc      1.2f     NS
  (gcc-2.6.3)
mips-sgi-irix5.3                cc       0.8      ok
mips-sgi-irix5.2                gcc      1.3b     ok
  (egcs-1.1.2, native ld)
mips-sgi-irix5.2                cc       1.3b     ok
  (cc 3.18)
mips-sni-sysv4			cc       1.3.5    ok
  (Siemens C-compiler)
mips-sni-sysv4			gcc      1.3.5    ok
  (gcc-2.7.2.3, GNU assembler 2.8.1, native ld)
mipsel-unknown-openbsd2.1       gcc      1.0      ok
powerpc-apple-darwin6.4         gcc      1.5      ok
(apple dev tools released 12/2002)
powerpc-ibm-aix4.3.1.0          gcc      1.2f     ok
  (egcs-1.1.1)
powerpc-ibm-aix4.2.1.0          gcc      1.2f     ok
  (egcs-1.1.1)
powerpc-ibm-aix4.1.5.0          gcc      1.2f     ok
  (egcs-1.1.1)
powerpc-ibm-aix4.1.5.0          gcc      1.2f     NS
  (gcc-2.8.1)
powerpc-ibm-aix4.1.4.0          gcc      1.0      ok
powerpc-ibm-aix4.1.4.0          xlc      1.0i     ok
rs6000-ibm-aix4.1.5.0           gcc      1.2f     ok
  (gcc-2.7.2)
rs6000-ibm-aix4.1.4.0           gcc      1.2f     ok
  (gcc-2.7.2)
rs6000-ibm-aix3.2.5             gcc      1.0i     ok
rs6000-ibm-aix3.2.5             xlc      1.0i     ok
sparc-sun-solaris2.8		gcc	 1.3e	  ok (1.913)
  (gcc-2.95.3 & native ld)
sparc-sun-solaris2.7            gcc      1.3e     ok (1.913)
  (gcc-2.95.3 & native ld)
sparc-sun-solaris2.6            gcc      1.3e     ok (1.913)
  (gcc-2.95.3 & native ld)
sparc-sun-solaris2.5.1          gcc      1.3e     ok (1.911)
sparc-sun-solaris2.5            gcc      1.3b     ok
  (egcs-1.1.2, GNU ld 2.9.1 & native ld)
sparc-sun-solaris2.5            cc       1.3b     ok
  (SC 3.0.1)
sparc-sun-solaris2.4            gcc      1.0a     ok
sparc-sun-solaris2.4            cc       1.0a     ok
sparc-sun-solaris2.3            gcc      1.2f     ok
sparc-sun-sunos4.1.4            gcc      1.2f     ok
sparc-sun-sunos4.1.4            cc       1.0f     ok
sparc-sun-sunos4.1.3_U1         gcc      1.2f     ok
sparc-sun-sunos4.1.3C           gcc      1.2f     ok
sparc-sun-sunos4.1.3            gcc      1.3b     ok
  (egcs-1.1.2, GNU ld 2.9.1 & native ld)
sparc-sun-sunos4.1.3            cc       1.3b     ok
sparc-unknown-bsdi4.0           gcc      1.2c     ok
sparc-unknown-linux-gnulibc1    gcc      1.2f     ok
sparc-unknown-linux-gnu         gcc      1.3b     ok
  (egcs-1.1.2, GNU ld 2.9.1.0.23)
sparc64-unknown-linux-gnu       gcc      1.2f     ok

Notes:
- "ok" means "all tests passed".
- "NS" means "Not Shared", but OK for static libraries
```

Note: The vendor-distributed HP-UX `sed`(1) programs are horribly broken, and cannot handle libtool’s requirements, so users may report unusual problems. There is no workaround except to install a working `sed` (such as GNU `sed`) on these systems.

Note: The vendor-distributed NCR MP-RAS `cc` programs emits copyright on standard error that confuse tests on size of conftest.err. The workaround is to specify `CC` when run `configure` with CC='cc -Hnocopyr'.

### 15.3 Platform quirks

This section is dedicated to the sanity of the libtool maintainers. It describes the programs that libtool uses, how they vary from system to system, and how to test for them.

Because libtool is a shell script, it can be difficult to understand just by reading it from top to bottom. This section helps show why libtool does things a certain way. Combined with the scripts themselves, you should have a better sense of how to improve libtool, or write your own.

#### 15.3.1 Compilers

The only compiler characteristics that affect libtool are the flags needed (if any) to generate PIC objects. In general, if a C compiler supports certain PIC flags, then any derivative compilers support the same flags. Until there are some noteworthy exceptions to this rule, this section will document only C compilers.

The following C compilers have standard command line options, regardless of the platform:

**`gcc`**

This is the GNU C compiler, which is also the system compiler for many free operating systems (FreeBSD, GNU/Hurd, GNU/Linux, Lites, NetBSD, and OpenBSD, to name a few).

The -fpic or -fPIC flags can be used to generate position-independent code. -fPIC is guaranteed to generate working code, but the code is slower on m68k, m88k, and SPARC chips. However, using -fpic on those chips imposes arbitrary size limits on the shared libraries.

The rest of this subsection lists compilers by the operating system that they are bundled with:

**`aix3*`**

**`aix4*`**

Most AIX compilers have no PIC flags, since AIX (with the exception of AIX for IA-64) runs on PowerPC and RS/6000 chips. 15

**`hpux10*`**

Use ‘+Z’ to generate PIC.

**`osf3*`**

Digital/UNIX 3.x does not have PIC flags, at least not on the PowerPC platform.

**`solaris2*`**

Use -KPIC to generate PIC.

**`sunos4*`**

Use -PIC to generate PIC.

#### 15.3.2 Reloadable objects

On all known systems, a reloadable object can be created by running ld -r -o *output*.o *input1*.o *input2*.o. This reloadable object may be treated as exactly equivalent to other objects.

#### 15.3.3 Multiple dependencies

On most modern platforms the order where dependent libraries are listed has no effect on object generation. In theory, there are platforms that require libraries that provide missing symbols to other libraries to be listed after those libraries whose symbols they provide.

Particularly, if a pair of static archives each resolve some of the other’s symbols, it might be necessary to list one of those archives both before and after the other one. Libtool does not currently cope with this situation well, since duplicate libraries are removed from the link line by default. Libtool provides the command line option --preserve-dup-deps to preserve all duplicate dependencies in cases where it is necessary.

#### 15.3.4 Archivers

On all known systems, building a static library can be accomplished by running ar cr lib*name*.a *obj1*.o *obj2*.o …, where the .a file is the output library, and each .o file is an object file.

On all known systems, if there is a program named `ranlib`, then it must be used to “bless” the created library before linking against it, with the ranlib lib*name*.a command. Some systems, like Irix, use the `ar ts` command, instead.

#### 15.3.5 Cross compiling

Most build systems support the ability to compile libraries and applications on one platform for use on a different platform, provided a compiler capable of generating the appropriate output is available. In such cross compiling scenarios, the platform where the libraries or applications are compiled is called the *build platform*, while the platform where the libraries or applications are intended to be used or executed is called the *host platform*. The GNU Build System in *The Automake Manual*, of which libtool is a part, supports cross compiling via arguments passed to the configure script: --build=... and --host=.... However, when the build platform and host platform are very different, libtool is required to make certain accommodations to support these scenarios.

In most cases, because the build platform and host platform differ, the cross-compiled libraries and executables can’t be executed or tested on the build platform where they were compiled. The testsuites of most build systems will often skip any tests that involve executing such foreign executables when cross-compiling. However, if the build platform and host platform are sufficiently similar, it is often possible to run cross-compiled applications. Libtool’s own testsuite often attempts to execute cross-compiled tests, but will mark any failures as *skipped* since the failure might simply be due to the differences between the two platforms.

In addition to cases where the host platform and build platform are extremely similar (e.g. ‘i586-pc-linux-gnu’ and ‘i686-pc-linux-gnu’), there is another case where cross-compiled host applications may be executed on the build platform. This is possible when the build platform supports an emulation or API-enhanced environment for the host platform. One example of this situation would be if the build platform were MinGW, and the host platform were Cygwin (or vice versa). Both of these platforms can actually operate within a single Windows instance, so Cygwin applications can be launched from a MinGW context, and vice versa—provided certain care is taken. Another example would be if the build platform were GNU/Linux on an x86 32bit processor, and the host platform were MinGW. In this situation, the Wine environment can be used to launch Windows applications from the GNU/Linux operating system; again, provided certain care is taken.

One particular issue occurs when a Windows platform such as MinGW, Cygwin, or MSYS is the host or build platform, while the other platform is a Unix-style system. In these cases, there are often conflicts between the format of the file names and paths expected within host platform libraries and executables, and those employed on the build platform.

This situation is best described using a concrete example: suppose the build platform is GNU/Linux with canonical triplet ‘i686-pc-linux-gnu’. Suppose further that the host platform is MinGW with canonical triplet ‘i586-pc-mingw32’. On the GNU/Linux platform there is a cross compiler following the usual naming conventions of such compilers, where the compiler name is prefixed by the host canonical triplet (or suitable alias). (For more information concerning canonical triplets and platform aliases, see Specifying Target Triplets in *The Autoconf Manual* and Canonicalizing in *The Autoconf Manual*) In this case, the C compiler is named ‘i586-pc-mingw32-gcc’.

As described in Wrapper executables for uninstalled programs, for the MinGW host platform libtool uses a wrapper executable to set various environment variables before launching the actual program executable. Like the program executable, the wrapper executable is cross-compiled for the host platform (that is, for MinGW). As described above, ordinarily a host platform executable cannot be executed on the build platform, but in this case the Wine environment could be used to launch the MinGW application from GNU/Linux. However, the wrapper executable, as a host platform (MinGW) application, must set the `PATH` variable so that the true application’s dependent libraries can be located—but the contents of the `PATH` variable must be structured for MinGW. Libtool must use the Wine file name mapping facilities to determine the correct value so that the wrapper executable can set the `PATH` variable to point to the correct location.

For example, suppose we are compiling an application in /var/tmp on GNU/Linux, using separate source code and build directories:

| /var/tmp/foo-1.2.3/app/ | (application source code) |
|---|---|
| /var/tmp/foo-1.2.3/lib/ | (library source code) |
| /var/tmp/BUILD/app/ | (application build objects here) |
| /var/tmp/BUILD/lib/ | (library build objects here) |

Since the library will be built in /var/tmp/BUILD/lib, the wrapper executable (which will be in /var/tmp/BUILD/app) must add that directory to `PATH` (actually, it must add the directory named *objdir* under /var/tmp/BUILD/lib, but we’ll ignore that detail for now). However, Windows does not have a concept of Unix-style file or directory names such as /var/tmp/BUILD/lib. Therefore, Wine provides a mapping from Windows file names such as C:\Program Files to specific Unix-style file names. Wine also provides a utility that can be used to map Unix-style file names to Windows file names.

In this case, the wrapper executable should actually add the value

```
Z:\var\tmp\BUILD\lib
```

to the `PATH`. libtool contains support for path conversions of this type, for a certain limited set of build and host platform combinations. In this case, libtool will invoke Wine’s `winepath` utility to ensure that the correct `PATH` value is used. See File name conversion.

#### 15.3.6 File name conversion

In certain situations, libtool must convert file names and paths between formats appropriate to different platforms. Usually this occurs when cross-compiling, and affects only the ability to launch host platform executables on the build platform using an emulation or API-enhancement environment such as Wine. Failure to convert paths (see File Name Conversion Failure) will cause a warning to be issued, but rarely causes the build to fail—and should have no effect on the compiled products, once installed properly on the host platform. For more information, see Cross compiling.

However, file name conversion may also occur in another scenario: when using a Unix emulation system on Windows (such as Cygwin or MSYS), combined with a native Windows compiler such as MinGW or MSVC. Only a limited set of such scenarios are currently supported; in other cases file name conversion is skipped. The lack of file name conversion usually means that uninstalled executables can’t be launched, but only rarely causes the build to fail (see File Name Conversion Failure).

libtool supports file name conversion in the following scenarios:

| build platform | host platform | Notes |
|---|---|---|
| MinGW (MSYS) | MinGW (Windows) | see Native MinGW File Name Conversion |
| Cygwin | MinGW (Windows) | see Cygwin/Windows File Name Conversion |
| Unix + Wine | MinGW (Windows) | Requires Wine. See Unix/Windows File Name Conversion. |
| MinGW (MSYS) | Cygwin | Requires `LT_CYGPATH`. See LT_CYGPATH. Provided for testing purposes only. |
| Unix + Wine | Cygwin | Requires both Wine and `LT_CYGPATH`, but does not yet work with Cygwin 1.7.7 and Wine-1.2. See Unix/Windows File Name Conversion, and LT_CYGPATH. |

#### 15.3.6.1 File Name Conversion Failure

In most cases, file name conversion is not needed or attempted. However, when libtool detects that a specific combination of build and host platform does require file name conversion, it is possible that the conversion may fail. In these cases, you may see a warning such as the following:

```
Could not determine the host file name corresponding to
  `... a file name ...'
Continuing, but uninstalled executables may not work.
```

or

```
Could not determine the host path corresponding to
  `... a path ...'
Continuing, but uninstalled executables may not work.
```

This should not cause the build to fail. At worst, it means that the wrapper executable will specify file names or paths appropriate for the build platform. Since those are not appropriate for the host platform, the uninstalled executables would not operate correctly, even when the wrapper executable is launched via the appropriate emulation or API-enhancement (e.g. Wine). Simply install the executables on the host platform, and execute them there.

#### 15.3.6.2 Native MinGW File Name Conversion

MSYS is a Unix emulation environment for Windows, and is specifically designed such that in normal usage it *pretends* to be MinGW or native Windows, but understands Unix-style file names and paths, and supports standard Unix tools and shells. Thus, “native” MinGW builds are actually an odd sort of cross-compile, from an MSYS Unix emulation environment “pretending” to be MinGW, to actual native Windows.

When an MSYS shell launches a native Windows executable (as opposed to other *MSYS* executables), it uses a system of heuristics to detect any command-line arguments that contain file names or paths. It automatically converts these file names from the MSYS (Unix-like) format, to the corresponding Windows file name, before launching the executable. However, this auto-conversion facility is only available when using the MSYS runtime library. The wrapper executable itself is a MinGW application (that is, it does not use the MSYS runtime library). The wrapper executable must set `PATH` to, and call `_spawnv` with, values that have already been converted from MSYS format to Windows. Thus, when libtool writes the source code for the wrapper executable, it must manually convert MSYS paths to Windows format, so that the Windows values can be hard-coded into the wrapper executable.

#### 15.3.6.3 Cygwin/Windows File Name Conversion

Cygwin provides a Unix emulation environment for Windows. As part of that emulation, it provides a file system mapping that presents the Windows file system in a Unix-compatible manner. Cygwin also provides a utility `cygpath` that can be used to convert file names and paths between the two representations. In a correctly configured Cygwin installation, `cygpath` is always present, and is in the `PATH`.

Libtool uses `cygpath` to convert from Cygwin (Unix-style) file names and paths to Windows format when the build platform is Cygwin and the host platform is MinGW.

When the host platform is Cygwin, but the build platform is MSYS or some Unix system, libtool also uses `cygpath` to convert from Windows to Cygwin format (after first converting from the build platform format to Windows format; See Native MinGW File Name Conversion, and Unix/Windows File Name Conversion.) Because the build platform is not Cygwin, `cygpath` is not (and should not be) in the `PATH`. Therefore, in this configuration the environment variable `LT_CYGPATH` is required. See LT_CYGPATH.

#### 15.3.6.4 Unix/Windows File Name Conversion

Wine provides an interpretation environment for some Unix platforms where Windows applications can be executed. It provides a mapping between the Unix file system and a virtual Windows file system used by the Windows programs. For the file name conversion to work, Wine must be installed and properly configured on the build platform, and the `winepath` application must be in the build platform’s `PATH`. In addition, on 32bit GNU/Linux it is usually helpful if the binfmt extension is enabled.

#### 15.3.6.5 LT_CYGPATH

For some cross-compile configurations (where the host platform is Cygwin), the `cygpath` program is used to convert file names from the build platform notation to the Cygwin form (technically, this conversion is from Windows notation to Cygwin notation; the conversion from the build platform format to Windows notation is performed via other means). However, because the `cygpath` program is not (and should not be) in the `PATH` on the build platform, `LT_CYGPATH` must specify the full build platform file name (that is, the full Unix or MSYS file name) of the `cygpath` program.

The reason `cygpath` should not be in the build platform `PATH` is twofold: first, `cygpath` is usually installed in the same directory as many other Cygwin executables, such as `sed`, `cp`, etc. If the build platform environment had this directory in its `PATH`, then these Cygwin versions of common Unix utilities might be used in preference to the ones provided by the build platform itself, with deleterious effects. Second, especially when Cygwin-1.7 or later is used, multiple Cygwin installations can coexist within the same Windows instance. Each installation will have separate “mount tables” specified in *CYGROOT-N*/etc/fstab. These *mount tables* control how that instance of Cygwin will map Windows file names and paths to Cygwin form. Each installation’s `cygpath` utility automatically deduces the appropriate /etc/fstab file. Since each *CYGROOT-N*/etc/fstab mount table may specify different mappings, it matters what `cygpath` is used.

Note that `cygpath` is a Cygwin application; to execute this tool from Unix requires a working and properly configured Wine installation, as well as enabling the GNU/Linux `binfmt` extension. Furthermore, the Cygwin `setup.exe` tool should have been used, via Wine, to properly install Cygwin into the Wine file system (and registry).

Unfortunately, Wine support for Cygwin is intermittent. Recent releases of Cygwin (1.7 and above) appear to require more Windows API support than Wine provides (as of Wine version 1.2); most Cygwin applications fail to execute. This includes `cygpath` itself. Hence, it is best *not* to use the LT_CYGPATH machinery in libtool when performing Unix to Cygwin cross-compiles. Similarly, it is best *not* to enable the GNU/Linux binfmt support in this configuration, because while Wine will fail to execute the compiled Cygwin applications, it will still exit with status zero. This tends to confuse build systems and test suites (including libtool’s own testsuite, resulting in spurious reported failures). Wine support for the older Cygwin-1.5 series appears satisfactory, but the Cygwin team no longer supports Cygwin-1.5. It is hoped that Wine will eventually be improved such that Cygwin-1.7 will again operate correctly under Wine. Until then, libtool will report warnings as described in see File Name Conversion Failure in these scenarios.

However, `LT_CYGPATH` is also used for the MSYS to Cygwin cross compile scenario, and operates as expected.

#### 15.3.6.6 Cygwin to MinGW Cross

There are actually three different scenarios that could all legitimately be called a “Cygwin to MinGW” cross compile. The current (and standard) definition is when there is a compiler that produces native Windows libraries and applications, but which itself is a Cygwin application, just as would be expected in any other cross compile setup.

However, historically there were two other definitions, which we will refer to as the *fake* one, and the *lying* one.

In the *fake* Cygwin to MinGW cross compile case, you actually use a native MinGW compiler, but you do so from within a Cygwin environment:

```
export PATH="/c/MinGW/bin:${PATH}"
configure --build=i686-pc-cygwin \
	--host=mingw32 \
	NM=/c/MinGW/bin/nm.exe
```

In this way, the build system “knows” that you are cross compiling, and the file name conversion logic will be used. However, because the tools (`mingw32-gcc`, `nm`, `ar`) used are actually native Windows applications, they will not understand any Cygwin (that is, Unix-like) absolute file names passed as command line arguments (and, unlike MSYS, Cygwin does not automatically convert such arguments). However, so long as only relative file names are used in the build system, and non-Windows-supported Unix idioms such as symlinks and mount points are avoided, this scenario should work.

If you must use absolute file names, you will have to force Libtool to convert file names for the toolchain in this case, by doing the following before you run configure:

```
export lt_cv_to_tool_file_cmd=func_convert_file_cygwin_to_w32
```

In the *lying* Cygwin to MinGW cross compile case, you lie to the build system:

```
export PATH="/c/MinGW/bin:${PATH}"
configure --build=i686-pc-mingw32 \
	--host=i686-pc-mingw32 \
	--disable-dependency-tracking
```

and claim that the build platform is MinGW, even though you are actually running under *Cygwin* and not MinGW. In this case, libtool does *not* know that you are performing a cross compile, and thinks instead that you are performing a native MinGW build. However, as described in (see Native MinGW File Name Conversion), that scenario triggers an “MSYS to Windows” file name conversion. This, of course, is the wrong conversion since we are actually running under Cygwin. Also, the toolchain is expecting Windows file names (not Cygwin) but unless told so Libtool will feed Cygwin file names to the toolchain in this case. To force the correct file name conversions in this situation, you should do the following *before* running configure:

```
export lt_cv_to_host_file_cmd=func_convert_file_cygwin_to_w32
export lt_cv_to_tool_file_cmd=func_convert_file_cygwin_to_w32
```

Note that this relies on internal implementation details of libtool, and is subject to change. Also, `--disable-dependency-tracking` is required, because otherwise the MinGW GCC will generate dependency files that contain Windows file names. This, in turn, will confuse the Cygwin `make` program, which does not accept Windows file names:

```
Makefile:1: *** target pattern contains no `%'.  Stop.
```

There have also always been a number of other details required for the *lying* case to operate correctly, such as the use of so-called *identity mounts*:

```
# cygwin-root/etc/fstab
D:/foo    /foo     some_fs binary 0 0
D:/bar    /bar     some_fs binary 0 0
E:/grill  /grill   some_fs binary 0 0
```

In this way, top-level directories of each drive are available using identical names within Cygwin.

Note that you also need to ensure that the standard Unix directories (like /bin, /lib, /usr, /etc) appear in the root of a drive. This means that you must install Cygwin itself into the C:/ root directory (or D:/, or E:/, etc)—instead of the recommended installation into C:/cygwin/. In addition, all file names used in the build system must be relative, symlinks should not be used within the source or build directory trees, and all -M* options to `gcc` except -MMD must be avoided.

This is quite a fragile setup, but it has been in historical use, and so is documented here.

#### 15.3.7 Windows DLLs

This topic describes a couple of ways to portably create Windows Dynamic Link Libraries (DLLs). Libtool knows how to create DLLs using GNU tools and using Microsoft tools.

A typical library has a “hidden” implementation with an interface described in a header file. On just about every system, the interface could be something like this:

Example foo.h:

```
#ifndef FOO_H
#define FOO_H

int one (void);
int two (void);
extern int three;

#endif /* FOO_H */
```

And the implementation could be something like this:

Example foo.c:

```
#include "foo.h"

int one (void)
{
  return 1;
}

int two (void)
{
  return three - one ();
}

int three = 3;
```

When using contemporary GNU tools to create the Windows DLL, the above code will work there too, thanks to its auto-import/auto-export features. But that is not the case when using older GNU tools or perhaps more interestingly when using proprietary tools. In those cases the code will need additional decorations on the interface symbols with `__declspec(dllimport)` and `__declspec(dllexport)` depending on whether the library is built or it’s consumed and how it’s built and consumed. However, it should be noted that it would have worked also with Microsoft tools, if only the variable `three` hadn’t been there, due to the fact the Microsoft tools will automatically import functions (but sadly not variables) and Libtool will automatically export non-static symbols as described next.

With Microsoft tools, Libtool digs through the object files that make up the library, looking for non-static symbols to automatically export. I.e., Libtool with Microsoft tools tries to mimic the auto-export feature of contemporary GNU tools. It should be noted that the GNU auto-export feature is turned off when an explicit `__declspec(dllexport)` is seen. The GNU tools do this to not make more symbols visible for projects that have already taken the trouble to decorate symbols. There is no similar way to limit what symbols are visible in the code when Libtool is using Microsoft tools. In order to limit symbol visibility in that case you need to use one of the options -export-symbols or -export-symbols-regex.

No matching help with auto-import is provided by Libtool, which is why variables must be decorated to import them from a DLL for everything but contemporary GNU tools. As stated above, functions are automatically imported by both contemporary GNU tools and Microsoft tools, but for other proprietary tools the auto-import status of functions is unknown.

When the objects that form the library are built, there are generally two copies built for each object. One copy is used when linking the DLL and one copy is used for the static library. On Windows systems, a pair of defines are commonly used to discriminate how the interface symbols should be decorated. The first define is ‘-DDLL_EXPORT’, which is automatically provided by Libtool when `libtool` builds the copy of the object that is destined for the DLL. The second define is ‘-DLIBFOO_BUILD’ (or similar), which is often added by the package providing the library and is used when building the library, but not when consuming the library.

However, the matching double compile is not performed when consuming libraries. It is therefore not possible to reliably distinguish if the consumer is importing from a DLL or if it is going to use a static library.

With contemporary GNU tools, auto-import often saves the day, but see the GNU ld documentation and its --enable-auto-import option for some corner cases when it does not (see Options specific to i386 PE targets in *Using ld, the GNU linker*).

With Microsoft tools you typically get away with always compiling the code such that variables are expected to be imported from a DLL and functions are expected to be found in a static library. The tools will then automatically import the function from a DLL if that is where they are found. If the variables are not imported from a DLL as expected, but are found in a static library that is otherwise pulled in by some function, the linker will issue a warning (LNK4217) that a locally defined symbol is imported, but it still works. In other words, this scheme will not work to only consume variables from a library. There is also a price connected to this liberal use of imports in that an extra indirection is introduced when you are consuming the static version of the library. That extra indirection is unavoidable when the DLL is consumed, but it is not needed when consuming the static library.

For older GNU tools and other proprietary tools there is no generic way to make it possible to consume either of the DLL or the static library without user intervention, the tools need to be told what is intended. One common assumption is that if a DLL is being built (‘DLL_EXPORT’ is defined) then that DLL is going to consume any dependent libraries as DLLs. If that assumption is made everywhere, it is possible to select how an end-user application is consuming libraries by adding a single flag ‘-DDLL_EXPORT’ when a DLL build is required. This is of course an all or nothing deal, either everything as DLLs or everything as static libraries.

To sum up the above, the header file of the foo library needs to be changed into something like this:

Modified foo.h:

```
#ifndef FOO_H
#define FOO_H

#if defined _WIN32 && !defined __GNUC__
# ifdef LIBFOO_BUILD
#  ifdef DLL_EXPORT
#   define LIBFOO_SCOPE            __declspec (dllexport)
#   define LIBFOO_SCOPE_VAR extern __declspec (dllexport)
#  endif
# elif defined _MSC_VER
#  define LIBFOO_SCOPE
#  define LIBFOO_SCOPE_VAR  extern __declspec (dllimport)
# elif defined DLL_EXPORT
#  define LIBFOO_SCOPE             __declspec (dllimport)
#  define LIBFOO_SCOPE_VAR  extern __declspec (dllimport)
# endif
#endif
#ifndef LIBFOO_SCOPE
# define LIBFOO_SCOPE
# define LIBFOO_SCOPE_VAR extern
#endif

LIBFOO_SCOPE     int one (void);
LIBFOO_SCOPE     int two (void);
LIBFOO_SCOPE_VAR int three;

#endif /* FOO_H */
```

When the targets are limited to contemporary GNU tools and Microsoft tools, the above can be simplified to the following:

Simplified foo.h:

```
#ifndef FOO_H
#define FOO_H

#if defined _WIN32 && !defined __GNUC__ && !defined LIBFOO_BUILD
# define LIBFOO_SCOPE_VAR extern __declspec (dllimport)
#else
# define LIBFOO_SCOPE_VAR extern
#endif

int one (void);
int two (void);
LIBFOO_SCOPE_VAR int three;

#endif /* FOO_H */
```

This last simplified version can of course only work when Libtool is used to build the DLL, as no symbols would be exported otherwise (i.e., when using Microsoft tools).

It should be noted that there are various projects that attempt to relax these requirements by various low level tricks, but they are not discussed here. Examples are FlexDLL and edll.

### 15.5 Cheap tricks

Here are a few tricks that you can use to make maintainership easier:

- When people report bugs, ask them to use the --config, --debug, or --features flags, if you think they will help you. These flags are there to help you get information directly, rather than having to trust second-hand observation.
- Rather than reconfiguring libtool every time I make a change to `ltmain.in`, I keep a permanent `libtool` script in my `PATH`, which sources `ltmain.in` directly. The following steps describe how to create such a script, where `/home/src/libtool` is the directory containing the libtool source tree, `/home/src/libtool/libtool` is a libtool script that has been configured for your platform, and `~/bin` is a directory in your `PATH`: trick$ cd ~/bin trick$ sed 's%^\(macro_version=\).*$%\1@VERSION@%; s%^\(macro_revision=\).*$%\1@package_revision@%; /^# ltmain\.sh/q' /home/src/libtool/libtool > libtool trick$ echo '. /home/src/libtool/ltmain.in' >> libtool trick$ chmod +x libtool trick$ libtool --version ltmain.sh (GNU @PACKAGE@@TIMESTAMP@) @VERSION@ Copyright (C) 2014 Free Software Foundation, Inc. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. trick$

The output of the final ‘libtool --version’ command shows that the `ltmain.in` script is being used directly. Now, modify `~/bin/libtool` or `/home/src/libtool/ltmain.in` directly in order to test new changes without having to rerun `configure`.
