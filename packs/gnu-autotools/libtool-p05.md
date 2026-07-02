---
title: "Libtool (part 5/8)"
source: https://www.gnu.org/software/libtool/manual/libtool.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 5/8
---

## 11 Using libltdl

Libtool provides a small library, called libltdl, that aims at hiding the various difficulties of dlopening libraries from programmers. It consists of a few headers and small C source files that can be distributed with applications that need dlopening functionality. On some platforms, whose dynamic linkers are too limited for a simple implementation of libltdl services, it requires GNU DLD, or it will only emulate dynamic linking with libtool’s dlpreopening mechanism.

libltdl supports currently the following dynamic linking mechanisms:

- `dlopen` (POSIX compliant systems, GNU/Linux, etc.)
- `shl_load` (HP-UX)
- `LoadLibrary` (Win16 and Win32)
- `load_add_on` (BeOS)
- `NSAddImage` or `NSLinkModule` (Darwin and Mac OS X)
- GNU DLD (emulates dynamic linking for static libraries)
- libtool’s dlpreopen (see Dlpreopening)

libltdl is licensed under the terms of the GNU Lesser General Public License, with the following exception:

> As a special exception to the GNU Lesser General Public License, if you distribute this file as part of a program or library that is built using GNU Libtool, you may include it under the same distribution terms that you use for the rest of that program.

### 11.1 How to use libltdl in your programs

The libltdl API is similar to the POSIX dlopen interface, which is very simple but powerful.

To use libltdl in your program you have to include the header file ltdl.h:

```
#include <ltdl.h>
```

The early releases of libltdl used some symbols that violated the POSIX namespace conventions. These symbols are now deprecated, and have been replaced by those described here. If you have code that relies on the old deprecated symbol names, defining ‘LT_NON_POSIX_NAMESPACE’ before you include ltdl.h provides conversion macros. Whichever set of symbols you use, the new API is not binary compatible with the last, so you will need to recompile your application to use this version of libltdl.

Note that libltdl is not well tested in a multithreaded environment, though the intention is that it should work (see Using libltdl in a multi threaded environment). If there are any issues, working around them is left as an exercise for the reader; contributions are certainly welcome.

The following macros are defined by including ltdl.h:

**Macro: **LT_PATHSEP_CHAR** ¶**

`LT_PATHSEP_CHAR` is the system-dependent path separator, that is, ‘;’ on Windows and ‘:’ everywhere else.

**Macro: **LT_DIRSEP_CHAR** ¶**

If `LT_DIRSEP_CHAR` is defined, it can be used as directory separator in addition to ‘/’. On Windows, this contains ‘\’.

The following types are defined in ltdl.h:

**Type: **lt_dlhandle** ¶**

`lt_dlhandle` is a module “handle”. Every lt_dlopened module has a handle associated with it.

**Type: **lt_dladvise** ¶**

`lt_dladvise` is used to control optional module loading modes. If it is not used, the default mode of the underlying system module loader is used.

**Type: **lt_dlsymlist** ¶**

`lt_dlsymlist` is a symbol list for dlpreopened modules (see Dlpreopening).

libltdl provides the following functions:

**Function: `int` **lt_dlinit** `(void)` ¶**

Initialize libltdl. This function must be called before using libltdl and may be called several times. Return 0 on success, otherwise the number of errors.

**Function: `int` **lt_dlexit** `(void)` ¶**

Shut down libltdl and close all modules. This function will only then shut down libltdl when it was called as many times as `lt_dlinit` has been successfully called. Return 0 on success, otherwise the number of errors.

**Function: `lt_dlhandle` **lt_dlopen** `(const char **filename*)` ¶**

Open the module with the file name *filename* and return a handle for it. `lt_dlopen` is able to open libtool dynamic modules, preloaded static modules, the program itself and native dynamic modules11.

Unresolved symbols in the module are resolved using its dependency libraries and, on some platforms, previously dlopened modules. If the executable using this module was linked with the -export-dynamic flag, then the global symbols in the executable will also be used to resolve references in the module.

If *filename* is `NULL` and the program was linked with -export-dynamic or -dlopen self, `lt_dlopen` will return a handle for the program itself, which can be used to access its symbols.

If libltdl cannot find the library and the file name *filename* does not have a directory component it will additionally look in the following search paths for the module (in the following order):

1. user-defined search path: This search path can be changed by the program using the functions `lt_dlsetsearchpath`, `lt_dladdsearchdir` and `lt_dlinsertsearchdir`.
2. libltdl’s search path: This search path is the value of the environment variable `LTDL_LIBRARY_PATH`.
3. system library search path: The system dependent library search path (e.g. on GNU/Linux it is `LD_LIBRARY_PATH`).

Each search path must be a list of absolute directories separated by `LT_PATHSEP_CHAR`, for example, `"/usr/lib/mypkg:/lib/foo"`. The directory names may not contain the path separator.

If the same module is loaded several times, the same handle is returned. If `lt_dlopen` fails for any reason, it returns `NULL`.

**Function: `lt_dlhandle` **lt_dlopenext** `(const char **filename*)` ¶**

The same as `lt_dlopen`, except that it tries to append different file name extensions to the file name. If the file with the file name *filename* cannot be found libltdl tries to append the following extensions:

1. the libtool archive extension .la
2. the extension used for native dynamically loadable modules on the host platform, e.g., .so, .sl, etc.

This lookup strategy was designed to allow programs that don’t have knowledge about native dynamic libraries naming conventions to be able to `dlopen` such libraries as well as libtool modules transparently.

**Function: `lt_dlhandle` **lt_dlopenadvise** `(const char **filename*, lt_dladvise *advise*)` ¶**

The same as `lt_dlopen`, except that it also requires an additional argument that may contain additional hints to the underlying system module loader. The *advise* parameter is opaque and can only be accessed with the functions documented below.

Note that this function does not change the content of *advise*, so unlike the other calls in this API takes a direct `lt_dladvise` type, and not a pointer to the same.

**Function: `int` **lt_dladvise_init** `(lt_dladvise **advise*)` ¶**

The *advise* parameter can be used to pass hints to the module loader when using `lt_dlopenadvise` to perform the loading. The *advise* parameter needs to be initialised by this function before it can be used. Any memory used by *advise* needs to be recycled with `lt_dladvise_destroy` when it is no longer needed.

On failure, `lt_dladvise_init` returns non-zero and sets an error message that can be retrieved with `lt_dlerror`.

**Function: `int` **lt_dladvise_destroy** `(lt_dladvise **advise*)` ¶**

Recycle the memory used by *advise*. For an example, see the documentation for `lt_dladvise_ext`.

On failure, `lt_dladvise_destroy` returns non-zero and sets an error message that can be retrieved with `lt_dlerror`.

**Function: `int` **lt_dladvise_ext** `(lt_dladvise **advise*)` ¶**

Set the `ext` hint on *advise*. Passing an *advise* parameter to `lt_dlopenadvise` with this hint set causes it to try to append different file name extensions like `lt_dlopenext`.

The following example is equivalent to calling `lt_dlopenext (filename)`:

```
lt_dlhandle
my_dlopenext (const char *filename)
{
  lt_dlhandle handle = 0;
  lt_dladvise advise;

  if (!lt_dladvise_init (&advise) && !lt_dladvise_ext (&advise))
    handle = lt_dlopenadvise (filename, advise);

  lt_dladvise_destroy (&advise);

  return handle;
}
```

On failure, `lt_dladvise_ext` returns non-zero and sets an error message that can be retrieved with `lt_dlerror`.

**Function: `int` **lt_dladvise_global** `(lt_dladvise **advise*)` ¶**

Set the `symglobal` hint on *advise*. Passing an *advise* parameter to `lt_dlopenadvise` with this hint set causes it to try to make the loaded module’s symbols globally available for resolving unresolved symbols in subsequently loaded modules.

If neither the `symglobal` nor the `symlocal` hints are set, or if a module is loaded without using the `lt_dlopenadvise` call in any case, then the visibility of the module’s symbols will be as per the default for the underlying module loader and OS. Even if a suitable hint is passed, not all loaders are able to act upon it in which case `lt_dlgetinfo` will reveal whether the hint was actually followed.

On failure, `lt_dladvise_global` returns non-zero and sets an error message that can be retrieved with `lt_dlerror`.

**Function: `int` **lt_dladvise_local** `(lt_dladvise **advise*)` ¶**

Set the `symlocal` hint on *advise*. Passing an *advise* parameter to `lt_dlopenadvise` with this hint set causes it to try to keep the loaded module’s symbols hidden so that they are not visible to subsequently loaded modules.

If neither the `symglobal` nor the `symlocal` hints are set, or if a module is loaded without using the `lt_dlopenadvise` call in any case, then the visibility of the module’s symbols will be as per the default for the underlying module loader and OS. Even if a suitable hint is passed, not all loaders are able to act upon it in which case `lt_dlgetinfo` will reveal whether the hint was actually followed.

On failure, `lt_dladvise_local` returns non-zero and sets an error message that can be retrieved with `lt_dlerror`.

**Function: `int` **lt_dladvise_resident** `(lt_dladvise **advise*)` ¶**

Set the `resident` hint on *advise*. Passing an *advise* parameter to `lt_dlopenadvise` with this hint set causes it to try to make the loaded module resident in memory, so that it cannot be unloaded with a later call to `lt_dlclose`.

On failure, `lt_dladvise_resident` returns non-zero and sets an error message that can be retrieved with `lt_dlerror`.

**Function: `int` **lt_dladvise_preload** `(lt_dladvise **advise*)` ¶**

Set the `preload` hint on *advise*. Passing an *advise* parameter to `lt_dlopenadvise` with this hint set causes it to load only preloaded modules, so that if a suitable preloaded module is not found, `lt_dlopenadvise` will return `NULL`.

**Function: `int` **lt_dlclose** `(lt_dlhandle *handle*)` ¶**

Decrement the reference count on the module *handle*. If it drops to zero and no other module depends on this module, then the module is unloaded. Return 0 on success.

**Function: `void *` **lt_dlsym** `(lt_dlhandle *handle*, const char **name*)` ¶**

Return the address in the module *handle*, where the symbol given by the null-terminated string *name* is loaded. If the symbol cannot be found, `NULL` is returned.

**Function: `const char *` **lt_dlerror** `(void)` ¶**

Return a human readable string describing the most recent error that occurred from any of libltdl’s functions. Return `NULL` if no errors have occurred since initialization or since it was last called.

**Function: `int` **lt_dladdsearchdir** `(const char **search_dir*)` ¶**

Append the search directory *search_dir* to the current user-defined library search path. Return 0 on success.

**Function: `int` **lt_dlinsertsearchdir** `(const char **before*, const char **search_dir*)` ¶**

Insert the search directory *search_dir* into the user-defined library search path, immediately before the element starting at address *before*. If *before* is ‘NULL’, then *search_dir* is appending as if `lt_dladdsearchdir` had been called. Return 0 on success.

**Function: `int` **lt_dlsetsearchpath** `(const char **search_path*)` ¶**

Replace the current user-defined library search path with *search_path*, which must be a list of absolute directories separated by `LT_PATHSEP_CHAR`. Return 0 on success.

**Function: `const char *` **lt_dlgetsearchpath** `(void)` ¶**

Return the current user-defined library search path.

**Function: `int` **lt_dlforeachfile** `(const char **search_path*, int (**func*) (const char **filename*, void * *data*), void * *data*)` ¶**

In some applications you may not want to load individual modules with known names, but rather find all of the modules in a set of directories and load them all during initialisation. With this function you can have libltdl scan the `LT_PATHSEP_CHAR`-delimited directory list in *search_path* for candidates, and pass them, along with *data* to your own callback function, *func*. If *search_path* is ‘NULL’, then search all of the standard locations that `lt_dlopen` would examine. This function will continue to make calls to *func* for each file that it discovers in *search_path* until one of these calls returns non-zero, or until the files are exhausted. ‘lt_dlforeachfile’ returns the value returned by the last call made to *func*.

For example you could define *func* to build an ordered *argv*-like vector of files using *data* to hold the address of the start of the vector.

**Function: `int` **lt_dlmakeresident** `(lt_dlhandle *handle*)` ¶**

Mark a module so that it cannot be ‘lt_dlclose’d. This can be useful if a module implements some core functionality in your project that would cause your code to crash if removed. Return 0 on success.

If you use ‘lt_dlopen (NULL)’ to get a *handle* for the running binary, that handle will always be marked as resident, and consequently cannot be successfully ‘lt_dlclose’d.

**Function: `int` **lt_dlisresident** `(lt_dlhandle *handle*)` ¶**

Check whether a particular module has been marked as resident, returning 1 if it has or 0 otherwise. If there is an error while executing this function, return -1 and set an error message for retrieval with `lt_dlerror`.

### 11.2 Creating modules that can be `dlopen`ed

Libtool modules are created like normal libtool libraries with a few exceptions:

You have to link the module with libtool’s -module switch, and you should link any program that is intended to dlopen the module with -dlopen *modulename.la* where possible, so that libtool can dlpreopen the module on platforms that do not support dlopening. If the module depends on any other libraries, make sure you specify them either when you link the module or when you link programs that dlopen it. If you want to disable versioning (see Library interface versions) for a specific module you should link it with the -avoid-version switch. Note that libtool modules don’t need to have a "lib" prefix. However, Automake 1.4 or higher is required to build such modules.

Usually a set of modules provide the same interface, i.e. exports the same symbols, so that a program can dlopen them without having to know more about their internals: In order to avoid symbol conflicts all exported symbols must be prefixed with "modulename_LTX_" (*modulename* is the name of the module). Internal symbols must be named in such a way that they won’t conflict with other modules, for example, by prefixing them with "_modulename_". Although some platforms support having the same symbols defined more than once it is generally not portable and it makes it impossible to dlpreopen such modules.

libltdl will automatically cut the prefix off to get the real name of the symbol. Additionally, it supports modules that do not use a prefix so that you can also dlopen non-libtool modules.

foo1.c gives an example of a portable libtool module. Exported symbols are prefixed with "foo1_LTX_", internal symbols with "_foo1_". Aliases are defined at the beginning so that the code is more readable.

```
/* aliases for the exported symbols */
#define foo  foo1_LTX_foo
#define bar  foo1_LTX_bar

/* a global variable definition */
int bar = 1;

/* a private function */
int _foo1_helper() {
  return bar;
}

/* an exported function */
int foo() {
  return _foo1_helper();
}
```

The Makefile.am contains the necessary rules to build the module foo1.la:

```
...
lib_LTLIBRARIES = foo1.la

foo1_la_SOURCES = foo1.c
foo1_la_LDFLAGS = -module
...
```

### 11.3 Using libltdl in a multi threaded environment

Libltdl provides a wrapper around whatever dynamic run-time object loading mechanisms are provided by the host system, many of which are themselves not thread safe. Consequently libltdl cannot itself be consistently thread safe.

If you wish to use libltdl in a multithreaded environment, then you must mutex lock around libltdl calls, since they may in turn be calling non-thread-safe system calls on some target hosts.

Some old releases of libtool provided a mutex locking API that was unusable with POSIX threads, so callers were forced to lock around all libltdl API calls anyway. That mutex locking API was next to useless, and is not present in current releases.

Some future release of libtool may provide a new POSIX thread compliant mutex locking API.

### 11.4 Data associated with loaded modules

Some of the internal information about each loaded module that is maintained by libltdl is available to the user, in the form of this structure:

**Type: `struct` **lt_dlinfo** { char *`filename`; char *`name`; int `ref_count`; int `is_resident`; int `is_symglobal`; int `is_symlocal`;} ¶**

`lt_dlinfo` is used to store information about a module. The `filename` attribute is a null-terminated character string of the real module file name. If the module is a libtool module then `name` is its module name (e.g. `"libfoo"` for `"dir/libfoo.la"`), otherwise it is set to `NULL`. The `ref_count` attribute is a reference counter that describes how often the same module is currently loaded. The remaining fields can be compared to any hints that were passed to `lt_dlopenadvise` to determine whether the underlying loader was able to follow them.

The following function will return a pointer to libltdl’s internal copy of this structure for the given *handle*:

**Function: `const lt_dlinfo *` **lt_dlgetinfo** `(lt_dlhandle *handle*)` ¶**

Return a pointer to a struct that contains some information about the module *handle*. The contents of the struct must not be modified. Return `NULL` on failure.

Furthermore, to save you from having to keep a list of the handles of all the modules you have loaded, these functions allow you to iterate over libltdl’s list of loaded modules:

**Type: **lt_dlinterface_id** ¶**

The opaque type used to hold the module interface details for each registered libltdl client.

**Type: `int` **lt_dlhandle_interface** `(lt_dlhandle *handle*, const char **id_string*)` ¶**

Functions of this type are called to check that a handle conforms to a library’s expected module interface when iterating over the global handle list. You should be careful to write a callback function of this type that can correctly identify modules that belong to this client, both to prevent other clients from accidentally finding your loaded modules with the iterator functions below, and vice versa. The best way to do this is to check that module *handle* conforms to the interface specification of your loader using `lt_dlsym`.

The callback may be given **every** module loaded by all the libltdl module clients in the current address space, including any modules loaded by other libraries such as libltdl itself, and should return non-zero if that module does not fulfill the interface requirements of your loader.

```
int
my_interface_cb (lt_dlhandle handle, const char *id_string)
{
  char *(*module_id) (void) = NULL;

  /* A valid my_module must provide all of these symbols.  */
  if (!((module_id = (char*(*)(void)) lt_dlsym ("module_version"))
        && lt_dlsym ("my_module_entrypoint")))
      return 1;

  if (strcmp (id_string, module_id()) != 0)
      return 1;

  return 0;
}
```

**Function: `lt_dlinterface_id` **lt_dlinterface_register** `(const char **id_string*, lt_dlhandle_interface **iface*)` ¶**

Use this function to register your interface validator with libltdl, and in return obtain a unique key to store and retrieve per-module data. You supply an *id_string* and *iface* so that the resulting `lt_dlinterface_id` can be used to filter the module handles returned by the iteration functions below. If *iface* is `NULL`, all modules will be matched.

**Function: `void` **lt_dlinterface_free** `(lt_dlinterface_id *iface*)` ¶**

Release the data associated with *iface*.

**Function: `int` **lt_dlhandle_map** `(lt_dlinterface_id *iface*, int (**func*) (lt_dlhandle *handle*, void * *data*), void * *data*)` ¶**

For each module that matches *iface*, call the function *func*. When writing the *func* callback function, the argument *handle* is the handle of a loaded module, and *data* is the last argument passed to `lt_dlhandle_map`. As soon as *func* returns a non-zero value for one of the handles, `lt_dlhandle_map` will stop calling *func* and immediately return that non-zero value. Otherwise 0 is eventually returned when *func* has been successfully called for all matching modules.

**Function: `lt_dlhandle` **lt_dlhandle_iterate** `(lt_dlinterface_id *iface*, lt_dlhandle *place*)` ¶**

Iterate over the module handles loaded by *iface*, returning the first matching handle in the list if *place* is `NULL`, and the next one on subsequent calls. If *place* is the last element in the list of eligible modules, this function returns `NULL`.

```
lt_dlhandle handle = 0;
lt_dlinterface_id iface = my_interface_id;

while ((handle = lt_dlhandle_iterate (iface, handle)))
  {
    ...
  }
```

**Function: `lt_dlhandle` **lt_dlhandle_fetch** `(lt_dlinterface_id *iface*, const char **module_name*)` ¶**

Search through the module handles loaded by *iface* for a module named *module_name*, returning its handle if found or else `NULL` if no such named module has been loaded by *iface*.

However, you might still need to maintain your own list of loaded module handles (in parallel with the list maintained inside libltdl) if there were any other data that your application wanted to associate with each open module. Instead, you can use the following API calls to do that for you. You must first obtain a unique interface id from libltdl as described above, and subsequently always use it to retrieve the data you stored earlier. This allows different libraries to each store their own data against loaded modules, without interfering with one another.

**Function: `void *` **lt_dlcaller_set_data** `(lt_dlinterface_id *key*, lt_dlhandle *handle*, void * *data*)` ¶**

Set *data* as the set of data uniquely associated with *key* and *handle* for later retrieval. This function returns the *data* previously associated with *key* and *handle* if any. A result of 0, may indicate that a diagnostic for the last error (if any) is available from `lt_dlerror()`.

For example, to correctly remove some associated data:

```
void *stale = lt_dlcaller_set_data (key, handle, 0);
if (stale != NULL)
  {
    free (stale);
  }
else
  {
    char *error_msg = lt_dlerror ();

    if (error_msg != NULL)
      {
        my_error_handler (error_msg);
        return STATUS_FAILED;
      }
  }
```

**Function: `void *` **lt_dlcaller_get_data** `(lt_dlinterface_id *key*, lt_dlhandle *handle*)` ¶**

Return the address of the data associated with *key* and *handle*, or else `NULL` if there is none.

Old versions of libltdl also provided a simpler, but similar, API based around `lt_dlcaller_id`. Unfortunately, it had no provision for detecting whether a module belonged to a particular interface as libltdl didn’t support multiple loaders in the same address space at that time. Those APIs are no longer supported as there would be no way to stop clients of the old APIs from seeing (and accidentally altering) modules loaded by other libraries.

### 11.5 How to create and register new module loaders

Sometimes libltdl’s many ways of gaining access to modules are not sufficient for the purposes of a project. You can write your own loader, and register it with libltdl so that `lt_dlopen` will be able to use it.

Writing a loader involves writing at least three functions that can be called by `lt_dlopen`, `lt_dlsym` and `lt_dlclose`. Optionally, you can provide a finalisation function to perform any cleanup operations when `lt_dlexit` executes, and a symbol prefix string that will be prepended to any symbols passed to `lt_dlsym`. These functions must match the function pointer types below, after which they can be allocated to an instance of `lt_user_dlloader` and registered.

Registering the loader requires that you choose a name for it, so that it can be recognised by `lt_dlloader_find` and removed with `lt_dlloader_remove`. The name you choose must be unique, and not already in use by libltdl’s builtin loaders:

**"dlopen"**

The system dynamic library loader, if one exists.

**"dld"**

The GNU dld loader, if libdld was installed when libltdl was built.

**"dlpreload"**

The loader for `lt_dlopen`ing of preloaded static modules.

The prefix "dl" is reserved for loaders supplied with future versions of libltdl, so you should not use that for your own loader names.

The following types are defined in ltdl.h:

**Type: **lt_module** ¶**

`lt_module` is a dlloader dependent module. The dynamic module loader extensions communicate using these low level types.

**Type: **lt_dlloader** ¶**

`lt_dlloader` is a handle for module loader types.

**Type: **lt_user_data** ¶**

`lt_user_data` is used for specifying loader instance data.

**Type: `struct` **lt_user_dlloader** {const char *`sym_prefix`; lt_module_open *`module_open`; lt_module_close *`module_close`; lt_find_sym *`find_sym`; lt_dlloader_exit *`dlloader_exit`; } ¶**

If you want to define a new way to open dynamic modules, and have the `lt_dlopen` API use it, you need to instantiate one of these structures and pass it to `lt_dlloader_add`. You can pass whatever you like in the *dlloader_data* field, and it will be passed back as the value of the first parameter to each of the functions specified in the function pointer fields.

**Type: `lt_module` **lt_module_open** `(const char **filename*)` ¶**

The type of the loader function for an `lt_dlloader` module loader. The value set in the dlloader_data field of the `struct lt_user_dlloader` structure will be passed into this function in the *loader_data* parameter. Implementation of such a function should attempt to load the named module, and return an `lt_module` suitable for passing in to the associated `lt_module_close` and `lt_sym_find` function pointers. If the function fails it should return `NULL`, and set the error message with `lt_dlseterror`.

**Type: `int` **lt_module_close** `(lt_user_data *loader_data*, lt_module *module*)` ¶**

The type of the unloader function for a user defined module loader. Implementation of such a function should attempt to release any resources tied up by the *module* module, and then unload it from memory. If the function fails for some reason, set the error message with `lt_dlseterror` and return non-zero.

**Type: `void *` **lt_find_sym** `(lt_module *module*, const char **symbol*)` ¶**

The type of the symbol lookup function for a user defined module loader. Implementation of such a function should return the address of the named *symbol* in the module *module*, or else set the error message with `lt_dlseterror` and return `NULL` if lookup fails.

**Type: `int` **lt_dlloader_exit** `(lt_user_data *loader_data*)` ¶**

The type of the finalisation function for a user defined module loader. Implementation of such a function should free any resources associated with the loader, including any user specified data in the `dlloader_data` field of the `lt_user_dlloader`. If non-`NULL`, the function will be called by `lt_dlexit`, and `lt_dlloader_remove`.

For example:

```
int
register_myloader (void)
{
  lt_user_dlloader dlloader;

  /* User modules are responsible for their own initialisation. */
  if (myloader_init () != 0)
    return MYLOADER_INIT_ERROR;

  dlloader.sym_prefix    = NULL;
  dlloader.module_open   = myloader_open;
  dlloader.module_close  = myloader_close;
  dlloader.find_sym      = myloader_find_sym;
  dlloader.dlloader_exit = myloader_exit;
  dlloader.dlloader_data = (lt_user_data)myloader_function;

  /* Add my loader as the default module loader. */
  if (lt_dlloader_add (lt_dlloader_next (NULL), &dlloader,
                       "myloader") != 0)
    return ERROR;

  return OK;
}
```

Note that if there is any initialisation required for the loader, it must be performed manually before the loader is registered – libltdl doesn’t handle user loader initialisation.

Finalisation *is* handled by libltdl however, and it is important to ensure the `dlloader_exit` callback releases any resources claimed during the initialisation phase.

libltdl provides the following functions for writing your own module loaders:

**Function: `int` **lt_dlloader_add** `(lt_dlloader **place*, lt_user_dlloader **dlloader*, const char **loader_name*)` ¶**

Add a new module loader to the list of all loaders, either as the last loader (if *place* is `NULL`), else immediately before the loader passed as *place*. *loader_name* will be returned by `lt_dlloader_name` if it is subsequently passed a newly registered loader. These *loader_name*s must be unique, or `lt_dlloader_remove` and `lt_dlloader_find` cannot work. Returns 0 for success.

```
/* Make myloader be the last one. */
if (lt_dlloader_add (NULL, myloader) != 0)
  perror (lt_dlerror ());
```

**Function: `int` **lt_dlloader_remove** `(const char **loader_name*)` ¶**

Remove the loader identified by the unique name, *loader_name*. Before this can succeed, all modules opened by the named loader must have been closed. Returns 0 for success, otherwise an error message can be obtained from `lt_dlerror`.

```
/* Remove myloader. */
if (lt_dlloader_remove ("myloader") != 0)
  perror (lt_dlerror ());
```

**Function: `lt_dlloader *` **lt_dlloader_next** `(lt_dlloader **place*)` ¶**

Iterate over the module loaders, returning the first loader if *place* is `NULL`, and the next one on subsequent calls. The handle is for use with `lt_dlloader_add`.

```
/* Make myloader be the first one. */
if (lt_dlloader_add (lt_dlloader_next (NULL), myloader) != 0)
  return ERROR;
```

**Function: `lt_dlloader *` **lt_dlloader_find** `(const char **loader_name*)` ¶**

Return the first loader with a matching *loader_name* identifier, or else `NULL`, if the identifier is not found.

The identifiers that may be used by libltdl itself, if the host architecture supports them are *dlopen*12, *dld* and *dlpreload*.

```
/* Add a user loader as the next module loader to be tried if
   the standard dlopen loader were to fail when lt_dlopening. */
if (lt_dlloader_add (lt_dlloader_find ("dlopen"), myloader) != 0)
  return ERROR;
```

**Function: `const char *` **lt_dlloader_name** `(lt_dlloader **place*)` ¶**

Return the identifying name of *place*, as obtained from `lt_dlloader_next` or `lt_dlloader_find`. If this function fails, it will return `NULL` and set an error for retrieval with `lt_dlerror`.

**Function: `lt_user_data *` **lt_dlloader_data** `(lt_dlloader **place*)` ¶**

Return the address of the `dlloader_data` of *place*, as obtained from `lt_dlloader_next` or `lt_dlloader_find`. If this function fails, it will return `NULL` and set an error for retrieval with `lt_dlerror`.

#### 11.5.1 Error handling within user module loaders

**Function: `int` **lt_dladderror** `(const char **diagnostic*)` ¶**

This function allows you to integrate your own error messages into `lt_dlerror`. Pass in a suitable diagnostic message for return by `lt_dlerror`, and an error identifier for use with `lt_dlseterror` is returned.

If the allocation of an identifier fails, this function returns -1.

```
int myerror = lt_dladderror ("doh!");
if (myerror < 0)
  perror (lt_dlerror ());
```

**Function: `int` **lt_dlseterror** `(int *errorcode*)` ¶**

When writing your own module loaders, you should use this function to raise errors so that they are propagated through the `lt_dlerror` interface. All of the standard errors used by libltdl are declared in ltdl.h, or you can add more of your own with `lt_dladderror`. This function returns 0 on success.

```
if (lt_dlseterror (LTDL_ERROR_NO_MEMORY) != 0)
  perror (lt_dlerror ());
```

### 11.6 How to distribute libltdl with your package

Even though libltdl is installed together with libtool, you may wish to include libltdl in the distribution of your package, for the convenience of users of your package that don’t have libtool or libltdl installed, or if you are using features of a very new version of libltdl that you don’t expect your users to have yet. In such cases, you must decide what flavor of libltdl you want to use: a convenience library or an installable libtool library.

The most simplistic way to add `libltdl` to your package is to copy all the libltdl source files to a subdirectory within your package and to build and link them along with the rest of your sources. To help you do this, the m4 macros for Autoconf are available in ltdl.m4. You must ensure that they are available in aclocal.m4 before you run Autoconf13. Having made the macros available, you must add a call to the ‘LTDL_INIT’ macro (after the call to ‘LT_INIT’) to your package’s configure.ac to perform the configure time checks required to build the library correctly. Unfortunately, this method has problems if you then try to link the package binaries with an installed libltdl, or a library that depends on libltdl, because of the duplicate symbol definitions. For example, ultimately linking against two different versions of libltdl, or against both a local convenience library and an installed libltdl is bad. Ensuring that only one copy of the libltdl sources are linked into any program is left as an exercise for the reader.

**Macro: **LT_CONFIG_LTDL_DIR** *(*directory*)* ¶**

Declare *directory* to be the location of the `libltdl` source files, for `libtoolize --ltdl` to place them. See Invoking `libtoolize`, for more details. Provided that you add an appropriate `LT_CONFIG_LTDL_DIR` call in your configure.ac before calling `libtoolize`, the appropriate `libltdl` files will be installed automatically.

**Macro: **LTDL_INIT** *(*options*)* ¶**

**Macro: **LT_WITH_LTDL** ¶**

**Macro: **AC_WITH_LTDL** ¶**

`AC_WITH_LTDL` and `LT_WITH_LTDL` are deprecated names for older versions of this macro; `autoupdate` will update your configure.ac file.

This macro adds the following options to the `configure` script:

**--with-ltdl-include *installed-ltdl-header-dir***

The `LTDL_INIT` macro will look in the standard header file locations to find the installed `libltdl` headers. If `LTDL_INIT` can’t find them by itself, the person who builds your package can use this option to tell `configure` where the installed `libltdl` headers are.

**--with-ltdl-lib *installed-ltdl-library-dir***

Similarly, the person building your package can use this option to help `configure` find the installed libltdl.la.

**--with-included-ltdl**

If there is no installed `libltdl`, or in any case if the person building your package would rather use the `libltdl` sources shipped with the package in the subdirectory named by `LT_CONFIG_LTDL_DIR`, they should pass this option to `configure`.

If the --with-included-ltdl is not passed at configure time, and an installed `libltdl` is not found14, then `configure` will exit immediately with an error that asks the user to either specify the location of an installed `libltdl` using the --with-ltdl-include and --with-ltdl-lib options, or to build with the `libltdl` sources shipped with the package by passing --with-included-ltdl.

If an installed `libltdl` is found, then `LIBLTDL` is set to the link flags needed to use it, and `LTDLINCL` to the preprocessor flags needed to find the installed headers, and `LTDLDEPS` will be empty. Note, however, that no version checking is performed. You should manually check for the `libltdl` features you need in configure.ac:

```
LT_INIT([dlopen])
LTDL_INIT

# The lt_dladvise_init symbol was added with libtool-2.2
if test yes != "$with_included_ltdl"; then
  save_CFLAGS=$CFLAGS
  save_LDFLAGS=$LDFLAGS
  CFLAGS="$CFLAGS $LTDLINCL"
  LDFLAGS="$LDFLAGS $LIBLTDL"
  AC_CHECK_LIB([ltdl], [lt_dladvise_init],
                [],
        [AC_MSG_ERROR([installed libltdl is too old])])
  LDFLAGS=$save_LDFLAGS
  CFLAGS=$save_CFLAGS
fi
```

*options* may include no more than one of the following build modes depending on how you want your project to build `libltdl`: ‘nonrecursive’, ‘recursive’, or ‘subproject’. In order for `libtoolize` to detect this option correctly, if you supply one of these arguments, they must be given literally (i.e., macros or shell variables that expand to the correct ltdl mode will not work).

**‘nonrecursive’**

This is how the Libtool project distribution builds the `libltdl` we ship and install. If you wish to use Automake to build `libltdl` without invoking a recursive make to descend into the `libltdl` subdirectory, then use this option. You will need to set your configuration up carefully to make this work properly, and you will need releases of Autoconf and Automake that support `subdir-objects` and `LIBOBJDIR` properly. In your configure.ac, add:

```
AM_INIT_AUTOMAKE([subdir-objects])
AC_CONFIG_HEADERS([config.h])
LT_CONFIG_LTDL_DIR([libltdl])
LT_INIT([dlopen])
LTDL_INIT([nonrecursive])
```

You *have to* use a config header, but it may have a name different than config.h.

Also, add the following near the top of your Makefile.am:

```
AM_CPPFLAGS =
AM_LDFLAGS =

BUILT_SOURCES =
EXTRA_DIST =
CLEANFILES =
MOSTLYCLEANFILES =

include_HEADERS =
noinst_LTLIBRARIES =
lib_LTLIBRARIES =
EXTRA_LTLIBRARIES =

include libltdl/ltdl.mk
```

Unless you build no other libraries from this Makefile.am, you will also need to change `lib_LTLIBRARIES` to assign with ‘+=’ so that the `libltdl` targets declared in ltdl.mk are not overwritten.

**‘recursive’**

This build mode still requires that you use Automake, but (in contrast with ‘nonrecursive’) uses the more usual device of starting another `make` process in the libltdl subdirectory. To use this mode, you should add to your configure.ac:

```
AM_INIT_AUTOMAKE
AC_CONFIG_HEADERS([config.h])
LT_CONFIG_LTDL_DIR([libltdl])
LT_INIT([dlopen])
LTDL_INIT([recursive])
AC_CONFIG_FILES([libltdl/Makefile])
```

Again, you *have to* use a config header, but it may have a name different than config.h if you like.

Also, add this to your Makefile.am:

```
SUBDIRS = libltdl
```

**‘subproject’**

This mode is the default unless you explicitly add `recursive` or `nonrecursive` to your `LTDL_INIT` options; `subproject` is the only mode supported by previous releases of libltdl. Even if you do not use Autoconf in the parent project, then, in ‘subproject’ mode, still `libltdl` contains all the necessary files to configure and build itself – you just need to arrange for your build system to call libltdl/configure with appropriate options, and then run `make` in the `libltdl` subdirectory.

If you *are* using Autoconf and Automake, then you will need to add the following to your configure.ac:

```
LT_CONFIG_LTDL_DIR([libltdl])
LTDL_INIT
```

and to Makefile.am:

```
SUBDIRS = libltdl
```

Aside from setting the libltdl build mode, there are other keywords that you can pass to `LTDL_INIT` to modify its behavior when --with-included-ltdl has been given:

**‘convenience’**

This is the default unless you explicitly add `installable` to your `LTDL_INIT` options.

This keyword will cause options to be passed to the `configure` script in the subdirectory named by `LT_CONFIG_LTDL_DIR` to cause it to be built as a convenience library. If you’re not using automake, you will need to define `top_build_prefix`, `top_builddir`, and `top_srcdir` in your makefile so that `LIBLTDL`, `LTDLDEPS`, and `LTDLINCL` expand correctly.

One advantage of the convenience library is that it is not installed, so the fact that you use `libltdl` will not be apparent to the user, and it won’t overwrite a pre-installed version of `libltdl` the system might already have in the installation directory. On the other hand, if you want to upgrade `libltdl` for any reason (e.g. a bugfix) you’ll have to recompile your package instead of just replacing the shared installed version of `libltdl`. However, if your programs or libraries are linked with other libraries that use such a pre-installed version of `libltdl`, you may get linker errors or run-time crashes. Another problem is that you cannot link the convenience library into more than one libtool library, then link a single program with those libraries, because you may get duplicate symbols. In general you can safely use the convenience library in programs that don’t depend on other libraries that might use `libltdl` too.

**‘installable’**

This keyword will pass options to the `configure` script in the subdirectory named by `LT_CONFIG_LTDL_DIR` to cause it to be built as an installable library. If you’re not using automake, you will need to define `top_build_prefix`, `top_builddir` and `top_srcdir` in your makefile so that `LIBLTDL`, `LTDLDEPS`, and `LTDLINCL` are expanded properly.

Be aware that you could overwrite another `libltdl` already installed to the same directory if you use this option.

Whatever method you use, ‘LTDL_INIT’ will define the shell variable `LIBLTDL` to the link flag that you should use to link with `libltdl`, the shell variable `LTDLDEPS` to the files that can be used as a dependency in Makefile rules, and the shell variable `LTDLINCL` to the preprocessor flag that you should use to compile programs that include ltdl.h. So, when you want to link a program with libltdl, be it a convenience, installed or installable library, just use ‘$(LTDLINCL)’ for preprocessing and compilation, and ‘$(LIBLTDL)’ for linking.

- If your package is built using an installed version of `libltdl`, `LIBLTDL` will be set to the compiler flags needed to link against the installed library, `LTDLDEPS` will be empty, and `LTDLINCL` will be set to the compiler flags needed to find the `libltdl` header files.
- If your package is built using the convenience libltdl, `LIBLTDL` and `LTDLDEPS` will be the pathname for the convenience version of libltdl (starting with ‘${top_builddir}/’ or ‘${top_build_prefix}’) and `LTDLINCL` will be -I followed by the directory that contains ltdl.h (starting with ‘${top_srcdir}/’).
- If an installable version of the included `libltdl` is being built, its pathname starting with ‘${top_builddir}/’ or ‘${top_build_prefix}’, will be stored in `LIBLTDL` and `LTDLDEPS`, and `LTDLINCL` will be set just like in the case of convenience library.

You should probably also use the ‘dlopen’ option to `LT_INIT` in your configure.ac, otherwise libtool will assume no dlopening mechanism is supported, and revert to dlpreopening, which is probably not what you want. Avoid using the -static, -static-libtool-libs, or -all-static switches when linking programs with libltdl. This will not work on all platforms, because the dlopening functions may not be available for static linking.

The following example shows you how to embed an installable libltdl in your package. In order to use the convenience variant, just replace the `LTDL_INIT` option ‘installable’ with ‘convenience’. We assume that libltdl was embedded using ‘libtoolize --ltdl’.

configure.ac:

```
...
# Name the subdirectory that contains libltdl sources
LT_CONFIG_LTDL_DIR([libltdl])

# Configure libtool with dlopen support if possible
LT_INIT([dlopen])

# Enable building of the installable libltdl library
LTDL_INIT([installable])
...
```

Makefile.am:

```
...
SUBDIRS = libltdl

AM_CPPFLAGS = $(LTDLINCL)

myprog_LDFLAGS = -export-dynamic
myprog_LDADD = $(LIBLTDL) -dlopen self -dlopen foo1.la
myprog_DEPENDENCIES = $(LTDLDEPS) foo1.la
...
```

**Macro: **LTDL_INSTALLABLE** ¶**

**Macro: **AC_LIBLTDL_INSTALLABLE** ¶**

These macros are deprecated, the ‘installable’ option to `LTDL_INIT` should be used instead.

**Macro: **LTDL_CONVENIENCE** ¶**

**Macro: **AC_LIBLTDL_CONVENIENCE** ¶**

These macros are deprecated, the ‘convenience’ option to `LTDL_INIT` should be used instead.


## 12 Libtool’s trace interface

This section describes macros whose sole purpose is to be traced using Autoconf’s --trace option (see The Autoconf Manual in *The Autoconf Manual*) to query the Libtool configuration of a project. These macros are called by Libtool internals and should never be called by user code; they should only be traced.

**Macro: **LT_SUPPORTED_TAG** *(*tag*)* ¶**

This macro is called once for each language enabled in the package. Its only argument, *tag*, is the tag-name corresponding to the language (see Tags).

You can therefore retrieve the list of all tags enabled in a project using the following command:

```
autoconf --trace 'LT_SUPPORTED_TAG:$1'
```


## 13 Frequently Asked Questions about libtool

This chapter covers some questions that often come up on the mailing lists.

### 13.1 Why does libtool strip link flags when creating a library?

When creating a shared library, but not when compiling or creating a program, `libtool` drops some flags from the command line provided by the user. This is done because flags unknown to `libtool` may interfere with library creation or require additional support from `libtool`, and because omitting flags is usually the conservative choice for a successful build.

If you encounter flags that you think are useful to pass, as a work-around you can prepend flags with `-Wc,` or `-Xcompiler` to allow them to be passed through to the compiler driver (see Link mode). Another possibility is to add flags already to the compiler command at `configure` run time:

```
./configure CC='gcc -m64'
```

If you think `libtool` should let some flag through by default, here’s how you can test such an inclusion: grab the Libtool development tree, edit the ltmain.in file in the libltdl/config subdirectory to pass through the flag (search for ‘Flags to be passed through’), re-bootstrap and build with the flags in question added to `LDFLAGS`, `CFLAGS`, `CXXFLAGS`, etc. on the `configure` command line as appropriate. Run the testsuite as described in the README file and report results to the Libtool bug reporting address bug-libtool@gnu.org.
