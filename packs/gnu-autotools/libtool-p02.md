---
title: "Libtool (part 2/8)"
source: https://www.gnu.org/software/libtool/manual/libtool.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 2/8
---

## 4 Invoking `libtool`

The `libtool` program has the following synopsis:

```
libtool [option]... [mode-arg]...
```

and accepts the following options:

**--config**

Display libtool configuration variables and exit.

**--debug**

Dump a trace of shell script execution to standard output. This produces a lot of output, so you may wish to pipe it to `less` (or `more`) or redirect to a file.

**-n**

**--dry-run**

Don’t create, modify, or delete any files, just show what commands would be executed by libtool.

**--features**

Display basic configuration options. This provides a way for packages to determine whether shared or static libraries will be built.

**--finish**

Same as --mode=finish.

**-h**

Display short help message.

**--help**

Display a help message and exit. If --mode=*mode* is specified, then detailed help for *mode* is displayed.

**--help-all**

Display help for the general options as well as detailed help for each operation mode, and exit.

**--mode=*mode***

Use *mode* as the operation mode. When using libtool from the command line, you can give just *mode* (or a unique abbreviation of it) as the first argument as a shorthand for the full --mode=*mode*. For example, the following are equivalent:

```
$ libtool --mode=execute --dry-run gdb prog.exe
$ libtool        execute --dry-run gdb prog.exe
$ libtool        exe     --dry-run gdb prog.exe
$ libtool        e       --dry-run gdb prog.exe
```

*mode* must be set to one of the following:

**compile**

Compile a source file into a libtool object.

**execute**

Automatically set the library path so that another program can use uninstalled libtool-generated programs or libraries.

**link**

Create a library or an executable.

**install**

Install libraries or executables.

**finish**

Complete the installation of libtool libraries on the system.

**uninstall**

Delete installed libraries or executables.

**clean**

Delete uninstalled libraries or executables.

**--tag=*tag***

Use configuration variables from tag *tag* (see Tags).

**--preserve-dup-deps**

Do not remove duplicate dependencies in libraries. When building packages with static libraries, the libraries may depend circularly on each other (shared libs can too, but for those it doesn’t matter), so there are situations, where -la -lb -la is required, and the second -la may not be stripped or the link will fail. In cases where these duplications are required, this option will preserve them, only stripping the libraries that libtool knows it can safely.

**--no-finish**

Do not execute finish_cmds (disabled by default). This option is for specifying that testing of local changes to shared libraries is being performed so that ldconfig will not alter the shared library cache, which is an issue observed on OpenBSD 7.5. This option should be combined with the usage of --mode=install and --mode=finish to have any effect. Prior to utilizing this option, the shared library cache must not contain links to the listed install directory for shared libraries undergoing testing; otherwise, it will have no useful effect. In OpenBSD, the shared library cache can be reordered to prefer directories for testing shared libraries over the directories already listed in the shared library cache with --reorder-cache=*shared_lib_dirs*.

**--reorder-cache=*shared_lib_dirs***

Reorder the shared library cache by providing the preferred directories (*shared_lib_dirs*) to link shared libraries from. The previous shared library cache is unconfigured, and the preferred directories are configured with the previous directories appended to the end (if not in the preferred directory list)5. This option is currently only available on OpenBSD where `make install` has been required before `make check` for the shared library cache to be updated.

This option is essentially a wrapper for executing `ldconfig`, and it should be used as an independent option before and after testing changes to shared libraries. Below are some usage examples:

```
$ libtool --reorder-cache=/tmp/testing
Original: /usr/lib /usr/X11R6/lib /usr/local/lib
Reordered: /tmp/testing /usr/lib /usr/X11R6/lib /usr/local/lib
$ libtool --reorder-cache=/usr/lib:/usr/X11R6/lib:/usr/local/lib
Original: /tmp/testing /usr/lib /usr/X11R6/lib /usr/local/lib
Reordered: /usr/lib /usr/X11R6/lib /usr/local/lib /tmp/testing
```

```
$ libtool --reorder-cache=/tmp/testing
Original: /usr/lib /usr/X11R6/lib /usr/local/lib
Reordered: /tmp/testing /usr/lib /usr/X11R6/lib /usr/local/lib
$ rm -rf /tmp/testing
$ libtool --reorder-cache=/usr/lib:/usr/X11R6/lib:/usr/local/lib
Original: /tmp/testing /usr/lib /usr/X11R6/lib /usr/local/lib
Reordered: /usr/lib /usr/X11R6/lib /usr/local/lib
```

```
$ libtool --reorder-cache=/tmp/testing:/usr/local/lib:/home/user/dir
Original: /usr/lib /usr/X11R6/lib /usr/local/lib
Reordered: /tmp/testing /usr/local/lib /home/user/dir /usr/lib /usr/X11R6/lib
$ libtool --reorder-cache=/usr/lib /usr/X11R6/lib /usr/local/lib
Original: /tmp/testing /usr/local/lib /home/user/dir /usr/lib /usr/X11R6/lib
Reordered: /usr/lib /usr/X11R6/lib /usr/local/lib /tmp/testing /home/user/dir
```

**--quiet**

**--silent**

Do not print out any progress or informational messages.

**-v**

**--verbose**

Print out progress and informational messages (enabled by default), as well as additional messages not ordinarily seen by default.

**--no-quiet**

**--no-silent**

Print out the progress and informational messages that are seen by default. This option has no effect on whether the additional messages seen in --verbose mode are shown.

**--no-verbose**

Do not print out any additional informational messages beyond those ordinarily seen by default. This option has no effect on whether the ordinary progress and informational messages enabled by --no-quiet are shown.

Thus, there are now three different message levels (not counting --debug), depending on whether the normal messages and/or the additional verbose messages are displayed. Note that there is no mechanism to display verbose messages, without also displaying normal messages.

****default****

Normal messages are displayed, verbose messages are not displayed. In addition to being the default mode, it can be forcibly achieved by using both option --no-verbose and either option --no-silent or option --no-quiet.

****silent****

Neither normal messages nor verbose messages are displayed. This mode can be achieved using either option --silent or option --quiet.

****verbose****

Both normal messages and verbose messages are displayed. This mode can be achieved using either option -v or option --verbose.

**--version**

Print libtool version information and exit.

**-W**

**--warnings=*CATEGORY***

Report the warnings falling in category *CATEGORY*. The default category is `all`. To disable warnings, use the category `none`.

The current `libtool` implementation is done with a shell script that needs to be invoked by the shell that `configure` chose for configuring `libtool` (see config.status Invocation in *The Autoconf Manual*). This shell is set in the she-bang (‘#!’) line of the `libtool` script. Using a different shell may cause undefined behavior.

The *mode-args* are a variable number of arguments, depending on the selected operation mode. In general, each *mode-arg* is interpreted by programs libtool invokes, rather than libtool itself.

### 4.1 Compile mode

For *compile* mode, *mode-args* is a compiler command to be used in creating a “standard” object file. These arguments should begin with the name of the C compiler, and contain the -c compiler flag so that only an object file is created.

Libtool determines the name of the output file by removing the directory component from the source file name, then substituting the source code suffix (e.g. ‘.c’ for C source code) with the library object suffix, ‘.lo’.

If shared libraries are being built, any necessary PIC generation flags are substituted into the compilation command.

The following components of *mode-args* are treated specially:

**-o**

Note that the -o option is now fully supported. It is emulated on the platforms that don’t support it (by locking and moving the objects), so it is really easy to use libtool, just with minor modifications to your Makefiles. Typing for example

```
libtool --mode=compile gcc -c foo/x.c -o foo/x.lo
```

will do what you expect.

Note, however, that, if the compiler does not support -c and -o, it is impossible to compile foo/x.c without overwriting an existing ./x.o. Therefore, if you do have a source file ./x.c, make sure you introduce dependencies in your Makefile to make sure ./x.o (or ./x.lo) is re-created after any sub-directory’s x.lo:

```
x.o x.lo: foo/x.lo bar/x.lo
```

This will also ensure that make won’t try to use a temporarily corrupted x.o to create a program or library. It may cause needless recompilation on platforms that support -c and -o together, but it’s the only way to make it safe for those that don’t.

**-no-suppress**

If both PIC and non-PIC objects are being built, libtool will normally suppress the compiler output for the PIC object compilation to save showing very similar, if not identical duplicate output for each object. If the -no-suppress option is given in compile mode, libtool will show the compiler output for both objects.

**-prefer-pic**

Libtool will try to build only PIC objects.

**-prefer-non-pic**

Libtool will try to build only non-PIC objects.

**-shared**

Even if Libtool was configured with --enable-static, the object file Libtool builds will not be suitable for static linking. Libtool will signal an error if it was configured with --disable-shared, or if the host does not support shared libraries.

**-static**

Even if libtool was configured with --disable-static, the object file Libtool builds **will** be suitable for static linking.

**-Wc,*flag***

**-Xcompiler *flag***

Pass a flag directly to the compiler. With `-Wc,`, multiple flags may be separated by commas, whereas `-Xcompiler` passes through commas unchanged.

### 4.2 Link mode

*Link* mode links together object files (including library objects) to form another library or to create an executable program.

*mode-args* consist of a command using the C compiler to create an output file (with the -o flag) from several object files.

The following components of *mode-args* are treated specially:

**-all-static ¶**

If *output-file* is a program, then do not link it against any shared libraries at all. If *output-file* is a library, then only create a static library. In general, this flag cannot be used together with ‘disable-static’ (see The `LT_INIT` macro).

**-avoid-version**

Tries to avoid versioning (see Library interface versions) for libraries and modules, i.e. no version information is stored and no symbolic links are created. If the platform requires versioning, this option has no effect.

**-bindir**

Pass the absolute name of the directory for installing executable programs (see Directory Variables in *The GNU Coding Standards*). `libtool` may use this value to install shared libraries there on systems that do not provide for any library hardcoding and use the directory of a program and the `PATH` variable as library search path. This is typically used for DLLs on Windows or other systems using the PE (Portable Executable) format. On other systems, -bindir is ignored. The default value used is *libdir*/../bin for libraries installed to *libdir*. You should not use -bindir for modules.

**-dlopen *file***

Same as -dlpreopen *file*, if native dlopening is not supported on the host platform (see Dlopened modules) or if the program is linked with -static, -static-libtool-libs, or -all-static. Otherwise, no effect. If *file* is `self` Libtool will make sure that the program can `dlopen` itself, either by enabling -export-dynamic or by falling back to -dlpreopen self.

**-dlpreopen *file***

Link *file* into the output program, and add its symbols to the list of preloaded symbols (see Dlpreopening). If *file* is `self`, the symbols of the program itself will be added to preloaded symbol lists. If *file* is `force` Libtool will make sure that a preloaded symbol list is always *defined*, regardless of whether it’s empty or not.

**-export-dynamic**

Allow symbols from *output-file* to be resolved with `dlsym` (see Dlopened modules).

**-export-symbols *symfile***

Tells the linker to export only the symbols listed in *symfile*. The symbol file should end in .sym and must contain the name of one symbol per line. This option has no effect:

- on static libraries, and
- on shared libraries on some platforms, such as AIX and Haiku.

By default all symbols are exported.

**-export-symbols-regex *regex***

Same as -export-symbols, except that only symbols matching the regular expression *regex* are exported. By default all symbols are exported.

**-L*libdir***

Search *libdir* for required libraries that have already been installed.

**-l*name***

*output-file* requires the installed library lib*name*. This option is required even when *output-file* is not an executable.

**-module**

Creates a library that can be dlopened (see Dlopened modules). This option doesn’t work for programs. Module names don’t need to be prefixed with ‘lib’. In order to prevent name clashes, however, lib*name* and *name* must not be used at the same time in your package.

**-no-fast-install**

Disable fast-install mode for the executable *output-file*. Useful if the program won’t be necessarily installed.

**-no-install**

Link an executable *output-file* that can’t be installed and therefore doesn’t need a wrapper script on systems that allow hardcoding of library paths. Useful if the program is only used in the build tree, e.g., for testing or generating other files.

**-no-undefined**

Declare that *output-file* does not depend on any libraries other than the ones listed on the command line, i.e., after linking, it will not have unresolved symbols. Some platforms require all symbols in shared libraries to be resolved at library creation (see Inter-library dependencies), and using this parameter allows `libtool` to assume that this will not happen.

**-o *output-file***

Create *output-file* from the specified objects and libraries.

**-objectlist *file***

Use a list of object files found in *file* to specify objects.

**-os2dllname *name***

Use this to change the DLL base name on OS/2 to *name*, to keep within the 8 character base name limit on this system.

**-precious-files-regex *regex***

Prevents removal of files from the temporary output directory whose names match this regular expression. You might specify ‘\.bbg?$’ to keep those files created with `gcc -ftest-coverage` for example.

**-release *release***

Specify that the library was generated by release *release* of your package, so that users can easily tell what versions are newer than others. Be warned that no two releases of your package will be binary compatible if you use this flag. If you want binary compatibility, use the -version-info flag instead (see Library interface versions).

**-rpath *libdir***

If *output-file* is a library, it will eventually be installed in *libdir*. If *output-file* is a program, add *libdir* to the run-time path of the program. On platforms that don’t support hardcoding library paths into executables and only search PATH for shared libraries, such as when *output-file* is a Windows (or other PE platform) DLL, the .la control file will be installed in *libdir*, but see -bindir above for the eventual destination of the .dll or other library file itself.

**-R *libdir***

If *output-file* is a program, add *libdir* to its run-time path. If *output-file* is a library, add -R*libdir* to its *dependency_libs*, so that, whenever the library is linked into a program, *libdir* will be added to its run-time path.

**-shared**

If *output-file* is a program, then link it against any uninstalled shared libtool libraries (this is the default behavior). If *output-file* is a library, then only create a shared library. In the later case, libtool will signal an error if it was configured with --disable-shared, or if the host does not support shared libraries.

**-shrext *suffix***

If *output-file* is a libtool library, replace the system’s standard file name extension for shared libraries with *suffix* (most systems use .so here). This option is helpful in certain cases where an application requires that shared libraries (typically modules) have an extension other than the default one. Please note you must supply the full file name extension including any leading dot.

**-static**

If *output-file* is a program, then do not link it against any uninstalled shared libtool libraries. If *output-file* is a library, then only create a static library.

**-static-libtool-libs**

If *output-file* is a program, then do not link it against any shared libtool libraries. If *output-file* is a library, then only create a static library.

**-version-info *current*[:*revision*[:*age*]]**

If *output-file* is a libtool library, use interface version information *current*, *revision*, and *age* to build it (see Library interface versions). Do **not** use this flag to specify package release information, rather see the -release flag.

**-version-number *major*[:*minor*[:*revision*]]**

If *output-file* is a libtool library, compute interface version information so that the resulting library uses the specified major, minor and revision numbers. This is designed to permit libtool to be used with existing projects where identical version numbers are already used across operating systems. New projects should use the -version-info flag instead.

**-weak *libname***

if *output-file* is a libtool library, declare that it provides a weak *libname* interface. This is a hint to libtool that there is no need to append *libname* to the list of dependency libraries of *output-file*, because linking against *output-file* already supplies the same interface (see Linking with dlopened modules).

**-Wc,*flag***

**-Xcompiler *flag***

Pass a linker-specific flag directly to the compiler. With `-Wc,`, multiple flags may be separated by commas, whereas `-Xcompiler` passes through commas unchanged.

**-Wa,*flag***

**-Xassembler *flag***

Pass a linker-specific flag directly to the assembler. With `-Wa,`, multiple flags may be separated by commas, whereas `-Xassembler` passes through commas unchanged.

**-Wl,*flag***

**-Xlinker *flag***

Pass a linker-specific flag directly to the linker.

**-XCClinker *flag***

Pass a link-specific flag to the compiler driver (`CC`) during linking.

If the *output-file* ends in .la, then a libtool library is created, which must be built only from library objects (.lo files). The -rpath option is required. In the current implementation, libtool libraries may not depend on other uninstalled libtool libraries (see Inter-library dependencies).

If the *output-file* ends in .a, then a standard library is created using `ar` and possibly `ranlib`.

If *output-file* ends in .o or .lo, then a reloadable object file is created from the input files (generally using ‘ld -r’). This method is often called *partial linking*.

Otherwise, an executable program is created.

### 4.3 Execute mode

For *execute* mode, the library path is automatically set, then a program is executed.

The first of the *mode-args* is treated as a program name, with the rest as arguments to that program.

The following components of *mode-args* are treated specially:

**-dlopen *file***

Add the directory containing *file* to the library path.

This mode sets the library path environment variable according to any -dlopen flags.

If any of the *args* are libtool executable wrappers, then they are translated into the name of their corresponding uninstalled binary, and any of their required library directories are added to the library path.

### 4.4 Install mode

In *install* mode, libtool interprets most of the elements of *mode-args* as an installation command beginning with `cp`, or a BSD-compatible `install` program.

The following components of *mode-args* are treated specially:

**-inst-prefix-dir *inst-prefix-dir***

When installing into a temporary staging area, rather than the final `prefix`, this argument is used to reflect the temporary path, in much the same way `automake` uses `DESTDIR`. For instance, if `prefix` is /usr/local, but *inst-prefix-dir* is /tmp, then the object will be installed under /tmp/usr/local/. If the installed object is a libtool library, then the internal fields of that library will reflect only `prefix`, not *inst-prefix-dir*:

```
# Directory that this library needs to be installed in:
libdir='/usr/local/lib'
```

not

```
# Directory that this library needs to be installed in:
libdir='/tmp/usr/local/lib'
```

`inst-prefix` is also used to ensure that if the installed object must be relinked upon installation, that it is relinked against the libraries in *inst-prefix-dir*/`prefix`, not `prefix`.

In truth, this option is not really intended for use when calling libtool directly; it is automatically used when `libtool --mode=install` calls `libtool --mode=relink`. Libtool does this by analyzing the destination path given in the original `libtool --mode=install` command and comparing it to the expected installation path established during `libtool --mode=link`.

Thus, end-users need change nothing, and `automake`-style `make install DESTDIR=/tmp` will Just Work(tm) most of the time. For systems where fast installation cannot be turned on, relinking may be needed. In this case, a ‘DESTDIR’ install will fail.

Currently it is not generally possible to install into a temporary staging area that contains needed third-party libraries that are not yet visible at their final location.

The rest of the *mode-args* are interpreted as arguments to the `cp` or `install` command.

The command is run, and any necessary unprivileged post-installation commands are also completed.

### 4.5 Finish mode

*Finish* mode has two functions. One is to help system administrators install libtool libraries so that they can be located and linked into user programs. To invoke this functionality, pass the name of a library directory as *mode-arg*. Running this command may require superuser privileges, and the --dry-run option may be useful.

The second is to facilitate transferring libtool libraries to a native compilation environment after they were built in a cross-compilation environment. Cross-compilation environments may rely on recent libtool features, and running libtool in finish mode will make it easier to work with older versions of libtool. This task is performed whenever the *mode-arg* is a .la file.

### 4.6 Uninstall mode

*Uninstall* mode deletes installed libraries, executables and objects.

The first *mode-arg* is the name of the program to use to delete files (typically `/bin/rm`).

The remaining *mode-args* are either flags for the deletion program (beginning with a ‘-’), or the names of files to delete.

### 4.7 Clean mode

*Clean* mode deletes uninstalled libraries, executables, objects and libtool’s temporary files associated with them.

The first *mode-arg* is the name of the program to use to delete files (typically `/bin/rm`).

The remaining *mode-args* are either flags for the deletion program (beginning with a ‘-’), or the names of files to delete.
