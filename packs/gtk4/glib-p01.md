---
title: "GLib (part 1/3)"
source: https://docs.gtk.org/glib/
domain: gtk4
license: CC-BY-SA-4.0
tags: gtk4 toolkit, gtk widgets, gnome application, libadwaita styling
fetched: 2026-07-02
part: 1/3
---

### Namespace

# GLib – 2.0

GLib is a general-purpose, portable utility library, which provides many useful data types, macros, type conversions, string utilities, file utilities, a mainloop abstraction, and so on.

| *Version* | 2.89.0 |
|---|---|
| *Authors* | GLib Development Team |
| *License* | LGPL-2.1-or-later |
| *Website* | https://www.gtk.org |
| *Source* | https://gitlab.gnome.org/GNOME/glib/ |

#### Build

| C headers | `glib.h` |
|---|---|
| pkg-config files | `glib-2.0` |

| **GModule** | Portable API for dynamically loading modules |
|---|---|
|   | Browse documentation |
| **GObject** | The base type system library |
|   | Browse documentation |
| **GIO** | GObject Interfaces and Objects, Networking, IPC, and I/O |
|   | Browse documentation |

#### Additional documentation

- Building GLib
- Compiling GLib Applications
- Cross-compiling the GLib package
- Running GLib Applications
- Writing GLib Applications
- Support and Bug Reports
- GVariant Format Strings
- GVariant Text Format
- Character Set Conversions
- Internationalization
- String Utilities
- Basic Types
- Macros
- Conversion Macros
- Automatic Cleanup
- Memory Allocation
- Memory Slices
- Error Reporting
- Message Logging
- Warnings and Assertions
- File Utilities
- Hostname Utilities
- Miscellaneous Utilities
- The Main Event Loop
- Reference Counting
- Testing Framework
- Atomic Operations
- Bounds-checking Integer Arithmetic
- Threads
- Spawning Processes
- Random Numbers
- Numerical Definitions
- Simple XML Subset Parser
- Base64 Encoding
- Commandline Option Parser
- Data Structures
- Keyed Data Lists and Datasets
- Shell Utilities
- GUuid
- Unicode
- Version Information
- Deprecated Thread API

#### Structs

| Allocator | deprecated: 2.10 |
|---|---|
| Array | Contains the public fields of a `GArray`. |
| AsyncQueue | An opaque data structure which represents an asynchronous queue. |
| BookmarkFile | `GBookmarkFile` lets you parse, edit or create files containing bookmarks. since: 2.12 |
| ByteArray | Contains the public fields of a `GByteArray`. |
| Bytes | A simple reference counted data type representing an immutable sequence of zero or more bytes from an unspecified origin. since: 2.32 |
| Cache | A `GCache` allows sharing of complex data structures, in order to save system resources. deprecated: 2.32 |
| Checksum | GLib provides a generic API for computing checksums (or ‘digests’) for a sequence of arbitrary bytes, using various hashing algorithms like MD5, SHA-1 and SHA-256. Checksums are commonly used in various environments and specifications. since: 2.16 |
| Completion | `GCompletion` provides support for automatic completion of a string using any group of target strings. It is typically used for file name completion as is common in many UNIX shells. deprecated: 2.26 |
| Cond | The `GCond` struct is an opaque data structure that represents a condition. Threads can block on a `GCond` if they find a certain condition to be false. If other threads change the state of this condition they signal the `GCond`, and that causes the waiting threads to be woken up. |
| Data | An opaque data structure that represents a keyed data list. |
| Date | `GDate` is a struct for calendrical calculations. |
| DateTime | `GDateTime` is a structure that combines a Gregorian date and time into a single structure. since: 2.26 |
| DebugKey | Associates a string with a bit flag. Used in g_parse_debug_string(). |
| Dir | An opaque structure representing an opened directory. |
| Error | The `GError` structure contains information about an error that has occurred. |
| HashTable | The `GHashTable` struct is an opaque data structure to represent a Hash Table. It should only be accessed via the following functions. |
| HashTableIter | A GHashTableIter structure represents an iterator that can be used to iterate over the elements of a `GHashTable`. GHashTableIter structures are typically allocated on the stack and then initialized with g_hash_table_iter_init(). |
| Hmac | HMACs should be used when producing a cookie or hash based on data and a key. Simple mechanisms for using SHA1 and other algorithms to digest a key and data together are vulnerable to various security issues. HMAC uses algorithms like SHA1 in a secure way to produce a digest of a key and data. since: 2.30 |
| Hook | The `GHook` struct represents a single hook function in a `GHookList`. |
| HookList | The `GHookList` struct represents a list of hook functions. |
| IConv | The GIConv struct wraps an `iconv()` conversion descriptor. It contains private data and should only be accessed using the following functions. |
| IOChannel | The `GIOChannel` data type aims to provide a portable method for using file descriptors, pipes, and sockets, and integrating them into the main event loop (see `GMainContext`). Currently, full support is available on UNIX platforms; support for Windows is only partially complete. |
| IOFuncs | A table of functions used to handle different types of `GIOChannel` in a generic way. |
| KeyFile | `GKeyFile` parses .ini-like config files. |
| List | The `GList` struct is used for each element in a doubly-linked list. |
| LogField | Structure representing a single field in a structured log entry. See `g_log_structured()` for details. since: 2.50 |
| MainContext | The `GMainContext` struct is an opaque data type representing a set of sources to be handled in a main loop. |
| MainLoop | The `GMainLoop` struct is an opaque data type representing the main event loop of a GLib or GTK application. |
| MappedFile | The `GMappedFile` represents a file mapping created with g_mapped_file_new(). It has only private members and should not be accessed directly. |
| MarkupParseContext | A parse context is used to parse a stream of bytes that you expect to contain marked-up text. |
| MarkupParser | Any of the fields in `GMarkupParser` can be `NULL`, in which case they will be ignored. Except for the `error` function, any of these callbacks can set an error; in particular the `G_MARKUP_ERROR_UNKNOWN_ELEMENT`, `G_MARKUP_ERROR_UNKNOWN_ATTRIBUTE`, and `G_MARKUP_ERROR_INVALID_CONTENT` errors are intended to be set from these callbacks. If you set an error from a callback, `g_markup_parse_context_parse()` will report that error back to its caller. |
| MatchInfo | An opaque struct used to return information about matches to a `GRegex`. |
| MemChunk | deprecated: 2.10 |
| MemVTable | A set of functions used to perform memory allocation. The same `GMemVTable` must be used for all allocations in the same program; a call to g_mem_set_vtable(), if it exists, should be prior to any use of GLib. |
| Node | The `GNode` struct represents one node in a n-ary tree. |
| Once | A `GOnce` struct controls a one-time initialization function. Any one-time initialization function must have its own unique `GOnce` struct. since: 2.4 |
| OptionContext | A `GOptionContext` struct defines which options are accepted by the commandline option parser. The struct has only private fields and should not be directly accessed. |
| OptionEntry | `G_OPTION_ARG_NONE`: %gboolean `G_OPTION_ARG_STRING`: %gchar* `G_OPTION_ARG_INT`: %gint `G_OPTION_ARG_FILENAME`: %gchar* `G_OPTION_ARG_STRING_ARRAY`: %gchar** `G_OPTION_ARG_FILENAME_ARRAY`: %gchar** `G_OPTION_ARG_DOUBLE`: %gdouble. |
| OptionGroup | A `GOptionGroup` struct defines the options in a single group. The struct has only private fields and should not be directly accessed. |
| PathBuf | `GPathBuf` is a helper type that allows you to easily build paths from individual elements, using the platform specific conventions for path separators. since: 2.76 |
| PatternSpec | A `GPatternSpec` struct is the ‘compiled’ form of a glob-style pattern. |
| PollFD | Represents a file descriptor, which events to poll for, and which events occurred. |
| Private | The `GPrivate` struct is an opaque data structure to represent a thread-local data key. It is approximately equivalent to the pthread_setspecific()/pthread_getspecific() APIs on POSIX and to TlsSetValue()/TlsGetValue() on Windows. |
| PtrArray | Contains the public fields of a `GPtrArray`. |
| Queue | Contains the public fields of a Queue. |
| Rand | The GRand struct is an opaque data structure. It should only be accessed through the g_rand_* functions. |
| RecMutex | The GRecMutex struct is an opaque data structure to represent a recursive mutex. It is similar to a `GMutex` with the difference that it is possible to lock a GRecMutex multiple times in the same thread without deadlock. When doing so, care has to be taken to unlock the recursive mutex as often as it has been locked. since: 2.32 |
| Regex | A `GRegex` is a compiled form of a regular expression. since: 2.14 |
| Relation | A `GRelation` is a table of data which can be indexed on any number of fields, rather like simple database tables. A `GRelation` contains a number of records, called tuples. Each record contains a number of fields. Records are not ordered, so it is not possible to find the record at a particular index. deprecated: 2.26 |
| RWLock | The GRWLock struct is an opaque data structure to represent a reader-writer lock. It is similar to a `GMutex` in that it allows multiple threads to coordinate access to a shared resource. since: 2.32 |
| Scanner | `GScanner` provides a general-purpose lexical scanner. |
| ScannerConfig | Specifies the `GScanner` parser configuration. Most settings can be changed during the parsing phase and will affect the lexical parsing of the next unpeeked token. |
| Sequence | The `GSequence` struct is an opaque data type representing a sequence data type. |
| SequenceIter | The `GSequenceIter` struct is an opaque data type representing an iterator pointing into a `GSequence`. |
| SList | The `GSList` struct is used for each element in the singly-linked list. |
| Source | The `GSource` struct is an opaque data type representing an event source. |
| SourceCallbackFuncs | The `GSourceCallbackFuncs` struct contains functions for managing callback objects. |
| SourceFuncs | The `GSourceFuncs` struct contains a table of functions used to handle event sources in a generic manner. |
| StatBuf | A type corresponding to the appropriate struct type for the `stat()` system call, depending on the platform and/or compiler being used. |
| StaticMutex | A `GStaticMutex` works like a `GMutex`. |
| StaticPrivate | A `GStaticPrivate` works almost like a `GPrivate`, but it has one significant advantage. It doesn’t need to be created at run-time like a `GPrivate`, but can be defined at compile-time. This is similar to the difference between `GMutex` and `GStaticMutex`. |
| StaticRecMutex | A `GStaticRecMutex` works like a `GStaticMutex`, but it can be locked multiple times by one thread. If you enter it n times, you have to unlock it n times again to let other threads lock it. An exception is the function g_static_rec_mutex_unlock_full(): that allows you to unlock a `GStaticRecMutex` completely returning the depth, (i.e. the number of times this mutex was locked). The depth can later be used to restore the state of the `GStaticRecMutex` by calling g_static_rec_mutex_lock_full(). In GLib 2.32, `GStaticRecMutex` has been deprecated in favor of `GRecMutex`. |
| StaticRWLock | The `GStaticRWLock` struct represents a read-write lock. A read-write lock can be used for protecting data that some portions of code only read from, while others also write. In such situations it is desirable that several readers can read at once, whereas of course only one writer may write at a time. deprecated: 2.32 |
| String | A `GString` is an object that handles the memory management of a C string. |
| StringChunk | `GStringChunk` provides efficient storage of groups of strings. |
| StrvBuilder | `GStrvBuilder` is a helper object to build a `NULL`-terminated string arrays. since: 2.68 |
| TestCase | An opaque structure representing a test case. |
| TestConfig |   |
| TestLogBuffer |   |
| TestLogMsg |   |
| TestSuite | An opaque structure representing a test suite. |
| Thread | The `GThread` struct represents a running thread. This struct is returned by `g_thread_new()` or g_thread_try_new(). You can obtain the `GThread` struct representing the current thread by calling g_thread_self(). |
| ThreadFunctions | This function table is no longer used by `g_thread_init()` to initialize the thread system. |
| ThreadPool | The `GThreadPool` struct represents a thread pool. |
| Timer | `GTimer` records a start time, and counts microseconds elapsed since that time. |
| TimeVal | Represents a precise time, with seconds and microseconds. deprecated: 2.62 |
| TimeZone | A `GTimeZone` represents a time zone, at no particular point in time. since: 2.26 |
| TrashStack | A `GTrashStack` is an efficient way to keep a stack of unused allocated memory chunks. Each memory chunk is required to be large enough to hold a `gpointer`. This allows the stack to be maintained without any space overhead, since the stack pointers can be stored inside the memory chunks. deprecated: 2.48 |
| Tree | The GTree struct is an opaque data structure representing a balanced binary tree. It should be accessed only by using the following functions. |
| TreeNode | An opaque type which identifies a specific node in a `GTree`. since: 2.68 |
| Tuples | The `GTuples` struct is used to return records (or tuples) from the `GRelation` by g_relation_select(). It only contains one public member - the number of records that matched. To access the matched records, you must use g_tuples_index(). deprecated: 2.26 |
| Uri | The `GUri` type and related functions can be used to parse URIs into their components, and build valid URIs from individual components. since: 2.66 |
| UriParamsIter | Many URI schemes include one or more attribute/value pairs as part of the URI value. For example `scheme://server/path?query=string&is=there` has two attributes – `query=string` and `is=there` – in its query part. since: 2.66 |
| Variant | `GVariant` is a variant datatype; it can contain one or more values along with information about the type of the values. since: 2.24 |
| VariantBuilder | A utility type for constructing container-type `GVariant` instances. |
| VariantDict | `GVariantDict` is a mutable interface to `GVariant` dictionaries. since: 2.40 |
| VariantIter | `GVariantIter` is an opaque data structure and can only be accessed using the following functions. |
| VariantType | A type in the `GVariant` type system. since: 2.24 |

#### Unions

| DoubleIEEE754 | The `GFloatIEEE754` and `GDoubleIEEE754` unions are used to access the sign, mantissa and exponent of IEEE floats and doubles. These unions are defined as appropriate for a given platform. IEEE floats and doubles are supported (used for storage) by at least Intel, PPC and Sparc. |
|---|---|
| FloatIEEE754 | The `GFloatIEEE754` and `GDoubleIEEE754` unions are used to access the sign, mantissa and exponent of IEEE floats and doubles. These unions are defined as appropriate for a given platform. IEEE floats and doubles are supported (used for storage) by at least Intel, PPC and Sparc. |
| Mutex | The `GMutex` struct is an opaque data structure to represent a mutex (mutual exclusion). It can be used to protect data against shared access. |
| TokenValue | A union holding the value of the token. |

#### Aliases

| DateDay | Integer representing a day of the month; between 1 and 31. |
|---|---|
| DateYear | Integer type representing a year. |
| MainContextPusher | Opaque type. See `g_main_context_pusher_new()` for details. |
| MutexLocker | Opaque type. See `g_mutex_locker_new()` for details. |
| Pid | A type which is used to hold a process identification. |
| Quark | A GQuark is a non-zero integer which uniquely identifies a particular string. |
| RecMutexLocker | Opaque type. See `g_rec_mutex_locker_new()` for details. |
| RefString | A typedef for a reference-counted string. A pointer to a `GRefString` can be treated like a standard `char*` array by all code, but can additionally have `g_ref_string_*()` methods called on it. `g_ref_string_*()` methods cannot be called on `char*` arrays not allocated using g_ref_string_new(). |
| RWLockReaderLocker | Opaque type. See `g_rw_lock_reader_locker_new()` for details. |
| RWLockWriterLocker | Opaque type. See `g_rw_lock_writer_locker_new()` for details. |
| Strv | A typedef alias for gchar**. This is mostly useful when used together with `g_auto()`. |
| Time | Simply a replacement for `time_t`. It has been deprecated since it is not equivalent to `time_t` on 64-bit platforms with a 64-bit `time_t`. deprecated: 2.62 |
| TimeSpan | A value representing an interval of time, in microseconds. |

#### Enumerations

| ChecksumType | The hashing algorithm to be used by `GChecksum` when performing the digest of some data. since: 2.16 |
|---|---|
| DateDMY | This enumeration isn’t used in the API, but may be useful if you need to mark a number as a day, month, or year. |
| DateMonth | Enumeration representing a month; values are `G_DATE_JANUARY`, `G_DATE_FEBRUARY`, etc. `G_DATE_BAD_MONTH` is the invalid value. |
| DateWeekday | Enumeration representing a day of the week; `G_DATE_MONDAY`, `G_DATE_TUESDAY`, etc. `G_DATE_BAD_WEEKDAY` is an invalid weekday. |
| ErrorType | The possible errors, used in the `v_error` field of `GTokenValue`, when the token is a `G_TOKEN_ERROR`. |
| IOError | `GIOError` is only used by the deprecated functions g_io_channel_read(), g_io_channel_write(), and g_io_channel_seek(). |
| IOStatus | Statuses returned by most of the `GIOFuncs` functions. |
| LogWriterOutput | Return values from `GLogWriterFuncs` to indicate whether the given log entry was successfully handled by the writer, or whether there was an error in handling it (and hence a fallback writer should be used). since: 2.50 |
| NormalizeMode | Defines how a Unicode string is transformed in a canonical form, standardizing such issues as whether a character with an accent is represented as a base character and combining accent or as a single precomposed character. Unicode strings should generally be normalized before comparing them. |
| OnceStatus | The possible statuses of a one-time initialization function controlled by a `GOnce` struct. since: 2.4 |
| OptionArg | The `GOptionArg` enum values determine which type of extra argument the options expect to find. If an option expects an extra argument, it can be specified in several ways; with a short option: `-x arg`, with a long option: `--name arg` or combined in a single argument: `--name=arg`. |
| SeekType | An enumeration specifying the base position for a `g_io_channel_seek_position()` operation. |
| SliceConfig |   |
| TestFileType | The type of file to return the filename for, when used with `g_test_build_filename()`. since: 2.38 |
| TestLogType |   |
| TestResult |   |
| ThreadPriority | Thread priorities. deprecated: 2.32 |
| TimeType | Disambiguates a given time in two ways. |
| TokenType | The possible types of token returned from each `g_scanner_get_next_token()` call. |
| TraverseType | Specifies the type of traversal performed by g_tree_traverse(), `g_node_traverse()` and g_node_find(). |
| UnicodeBreakType | These are the possible line break classifications. |
| UnicodeScript | The `GUnicodeScript` enumeration identifies different writing systems. The values correspond to the names as defined in the Unicode standard. The enumeration has been added in GLib 2.14, and is interchangeable with `PangoScript`. |
| UnicodeType | These are the possible character classifications from the Unicode specification. See Unicode Character Database. |
| UserDirectory | These are logical ids for special directories which are defined depending on the platform used. You should use `g_get_user_special_dir()` to retrieve the full path associated to the logical id. since: 2.14 |
| VariantClass | The range of possible top-level types of `GVariant` instances. since: 2.24 |

#### Bitfields

| AsciiType |   |
|---|---|
| FileSetContentsFlags | Flags to pass to `g_file_set_contents_full()` to affect its safety and performance. since: 2.66 |
| FileTest | A test to perform on a file using g_file_test(). |
| FormatSizeFlags | Flags to modify the format of the string returned by g_format_size_full(). |
| HookFlagMask | Flags used internally in the `GHook` implementation. |
| IOCondition | A bitwise combination representing a condition to watch for on an event source. |
| IOFlags | Specifies properties of a `GIOChannel`. Some of the flags can only be read with g_io_channel_get_flags(), but not changed with g_io_channel_set_flags(). |
| KeyFileFlags | Flags which influence the parsing. |
| LogLevelFlags | Flags specifying the level of log messages. |
| MainContextFlags | Flags to pass to `g_main_context_new_with_flags()` which affect the behaviour of a `GMainContext`. since: 2.72 |
| MarkupCollectType | A mixed enumerated type and flags field. You must specify one type (string, strdup, boolean, tristate). Additionally, you may optionally bitwise OR the type with the flag `G_MARKUP_COLLECT_OPTIONAL`. |
| MarkupParseFlags | Flags that affect the behaviour of the parser. |
| OptionFlags | Flags which modify individual options. |
| RegexCompileFlags | Flags specifying compile-time options. since: 2.14 |
| RegexMatchFlags | Flags specifying match-time options. since: 2.14 |
| SpawnFlags | Flags passed to g_spawn_sync(), `g_spawn_async()` and g_spawn_async_with_pipes(). |
| TestSubprocessFlags | Flags to pass to `g_test_trap_subprocess()` to control input and output. |
| TestTrapFlags | Flags to pass to `g_test_trap_fork()` to control input and output. deprecated: 2.38 |
| TraverseFlags | Specifies which nodes are visited during several of the tree functions, including `g_node_traverse()` and g_node_find(). |
| UriFlags | Flags that describe a URI. since: 2.66 |
| UriHideFlags | Flags describing what parts of the URI to hide in g_uri_to_string_partial(). Note that `G_URI_HIDE_PASSWORD` and `G_URI_HIDE_AUTH_PARAMS` will only work if the `GUri` was parsed with the corresponding flags. since: 2.66 |
| UriParamsFlags | Flags modifying the way parameters are handled by `g_uri_parse_params()` and `GUriParamsIter`. since: 2.66 |

#### Error Domains

| BookmarkFileError | Error codes returned by bookmark file parsing. |
|---|---|
| ConvertError | Error codes returned by character set conversion routines. |
| FileError | Values corresponding to `errno` codes returned from file operations on UNIX. Unlike `errno` codes, GFileError values are available on all systems, even Windows. The exact meaning of each code depends on what sort of file operation you were performing; the UNIX documentation gives more details. The following error code descriptions come from the GNU C Library manual, and are under the copyright of that manual. |
| IOChannelError | Error codes returned by `GIOChannel` operations. |
| KeyFileError | Error codes returned by key file parsing. |
| MarkupError | Error codes returned by markup parsing. |
| NumberParserError | Error codes returned by functions converting a string to a number. since: 2.54 |
| OptionError | Error codes returned by option parsing. |
| RegexError | Error codes returned by regular expressions functions. since: 2.14 |
| ShellError | Error codes returned by shell functions. |
| SpawnError | Error codes returned by spawning processes. |
| ThreadError | Possible errors of thread related functions. |
| UriError | Error codes returned by `GUri` methods. since: 2.66 |
| VariantParseError | Error codes returned by parsing text-format GVariants. |

#### Callbacks

| CacheDestroyFunc | Specifies the type of the `value_destroy_func` and `key_destroy_func` functions passed to g_cache_new(). The functions are passed a pointer to the `GCache` key or `GCache` value and should free any memory and other resources associated with it. deprecated: 2.32 |
|---|---|
| CacheDupFunc | Specifies the type of the `key_dup_func` function passed to g_cache_new(). The function is passed a key (**not** a value as the prototype implies) and should return a duplicate of the key. deprecated: 2.32 |
| CacheNewFunc | Specifies the type of the `value_new_func` function passed to g_cache_new(). It is passed a `GCache` key and should create the value corresponding to the key. deprecated: 2.32 |
| ChildWatchFunc | Prototype of a `GChildWatchSource` callback, called when a child process has exited. |
| ClearHandleFunc | Specifies the type of function passed to `g_clear_handle_id()` The implementation is expected to free the resource identified by `handle_id`; for instance, if `handle_id` is a `GSource` ID, `g_source_remove()` can be used. since: 2.56 |
| CompareDataFunc | Specifies the type of a comparison function used to compare two values. The function should return a negative integer if the first value comes before the second, 0 if they are equal, or a positive integer if the first value comes after the second. |
| CompareFunc | Specifies the type of a comparison function used to compare two values. The function should return a negative integer if the first value comes before the second, 0 if they are equal, or a positive integer if the first value comes after the second. |
| CompletionFunc | Specifies the type of the function passed to g_completion_new(). It should return the string corresponding to the given target item. This is used when you use data structures as `GCompletion` items. deprecated: 2.26 |
| CompletionStrncmpFunc | Specifies the type of the function passed to g_completion_set_compare(). This is used when you use strings as `GCompletion` items. deprecated: 2.26 |
| CopyFunc | A function of this signature is used to copy the node data when doing a deep-copy of a tree. since: 2.4 |
| DataForeachFunc | Specifies the type of function passed to g_dataset_foreach(). It is called with each `GQuark` id and associated data element, together with the `user_data` parameter supplied to g_dataset_foreach(). |
| DestroyNotify | Specifies the type of function which is called when a data element is destroyed. It is passed the pointer to the data element and should free any memory and resources allocated for it. |
| DuplicateFunc | The type of functions that are used to ‘duplicate’ an object. What this means depends on the context, it could just be incrementing the reference count, if `data` is a ref-counted object. |
| EqualFunc | Specifies the type of a function used to test two values for equality. The function should return `TRUE` if both values are equal and `FALSE` otherwise. |
| EqualFuncFull | Specifies the type of a function used to test two values for equality. The function should return `TRUE` if both values are equal and `FALSE` otherwise. since: 2.74 |
| ErrorClearFunc | Specifies the type of function which is called when an extended error instance is freed. It is passed the error pointer about to be freed, and should free the error’s private data fields. since: 2.68 |
| ErrorCopyFunc | Specifies the type of function which is called when an extended error instance is copied. It is passed the pointer to the destination error and source error, and should copy only the fields of the private data from `src_error` to `dest_error`. since: 2.68 |
| ErrorInitFunc | Specifies the type of function which is called just after an extended error instance is created and its fields filled. It should only initialize the fields in the private data, which can be received with the generated `*_get_private()` function. since: 2.68 |
| FreeFunc | Declares a type of function which takes an arbitrary data pointer argument and has no return value. It is not currently used in GLib or GTK. |
| Func | Specifies the type of functions passed to `g_list_foreach()` and g_slist_foreach(). |
| HashFunc | Specifies the type of the hash function which is passed to `g_hash_table_new()` when a `GHashTable` is created. |
| HFunc | Specifies the type of the function passed to g_hash_table_foreach(). It is called with each key/value pair, together with the `user_data` parameter which is passed to g_hash_table_foreach(). |
| HookCheckFunc | Defines the type of a hook function that can be invoked by g_hook_list_invoke_check(). |
| HookCheckMarshaller | Defines the type of function used by g_hook_list_marshal_check(). |
| HookCompareFunc | Defines the type of function used to compare `GHook` elements in g_hook_insert_sorted(). |
| HookFinalizeFunc | Defines the type of function to be called when a hook in a list of hooks gets finalized. |
| HookFindFunc | Defines the type of the function passed to g_hook_find(). |
| HookFunc | Defines the type of a hook function that can be invoked by g_hook_list_invoke(). |
| HookMarshaller | Defines the type of function used by g_hook_list_marshal(). |
| HRFunc | Specifies the type of the function passed to `g_hash_table_find()`, `g_hash_table_foreach_remove()`, and `g_hash_table_foreach_steal()`. |
| IOFunc | Specifies the type of function passed to `g_io_add_watch()` or g_io_add_watch_full(), which is called when the requested condition on a `GIOChannel` is satisfied. |
| LogFunc | Specifies the prototype of log handler functions. |
| LogWriterFunc | Writer function for log entries. A log entry is a collection of one or more `GLogFields`, using the standard field names from journal specification. See `g_log_structured()` for more information. since: 2.50 |
| NodeForeachFunc | Specifies the type of function passed to g_node_children_foreach(). The function is called with each child node, together with the user data passed to g_node_children_foreach(). |
| NodeTraverseFunc | Specifies the type of function passed to g_node_traverse(). The function is called with each of the nodes visited, together with the user data passed to g_node_traverse(). If the function returns `TRUE`, then the traversal is stopped. |
| OptionArgFunc | The type of function to be passed as callback for `G_OPTION_ARG_CALLBACK` options. |
| OptionErrorFunc | The type of function to be used as callback when a parse error occurs. |
| OptionParseFunc | The type of function that can be called before and after parsing. |
| PollFunc | Specifies the type of function passed to g_main_context_set_poll_func(). The semantics of the function should match those of the `poll()` system call. |
| PrintFunc | Specifies the type of the print handler functions. These are called with the complete formatted string to output. |
| RegexEvalCallback | A callback passed to `g_regex_replace_eval()`. since: 2.14 |
| ScannerMsgFunc | Specifies the type of the message handler function. |
| SequenceIterCompareFunc | A `GSequenceIterCompareFunc` is a function used to compare iterators. It must return zero if the iterators compare equal, a negative value if `a` comes before `b`, and a positive value if `b` comes before `a`. |
| SourceDisposeFunc | Dispose function for `source`. See `g_source_set_dispose_function()` for details. since: 2.64 |
| SourceDummyMarshal | This is just a placeholder for `GClosureMarshal`, which cannot be used here for dependency reasons. |
| SourceFunc | Specifies the type of function passed to `g_timeout_add()`, `g_timeout_add_full()`, `g_idle_add()`, and `g_idle_add_full()`. |
| SourceFuncsCheckFunc | Checks if the source is ready to be dispatched. since: 2.82 |
| SourceFuncsDispatchFunc | Dispatches the source callback. since: 2.82 |
| SourceFuncsFinalizeFunc | Finalizes the source. since: 2.82 |
| SourceFuncsPrepareFunc | Checks the source for readiness. since: 2.82 |
| SourceOnceFunc | A source function that is only called once before being removed from the main context automatically. since: 2.74 |
| SpawnChildSetupFunc | Specifies the type of the setup function passed to g_spawn_async(), `g_spawn_sync()` and g_spawn_async_with_pipes(), which can, in very limited ways, be used to affect the child’s execution. |
| TestDataFunc | The type used for test case functions that take an extra pointer argument. since: 2.28 |
| TestFixtureFunc | The type used for functions that operate on test fixtures. since: 2.28 |
| TestFunc | The type used for test case functions. since: 2.28 |
| TestLogFatalFunc | Specifies the prototype of fatal log handler functions. since: 2.22 |
| ThreadFunc | Specifies the type of the `func` functions passed to `g_thread_new()` or g_thread_try_new(). |
| TranslateFunc | The type of functions which are used to translate user-visible strings, for output. |
| TraverseFunc | Specifies the type of function passed to g_tree_traverse(). It is passed the key and value of each node, together with the `user_data` parameter passed to g_tree_traverse(). If the function returns `TRUE`, the traversal is stopped. |
| TraverseNodeFunc | Specifies the type of function passed to g_tree_foreach_node(). It is passed each node, together with the `user_data` parameter passed to g_tree_foreach_node(). If the function returns `TRUE`, the traversal is stopped. since: 2.68 |
| VoidFunc | Declares a type of function which takes no arguments and has no return value. It is used to specify the type function passed to g_atexit(). |

#### Functions

access

A wrapper for the POSIX `access()` function. This function is used to test a pathname for one or several of read, write or execute permissions, or just existence.

since: 2.8

aligned_alloc

This function is similar to g_malloc(), allocating (`n_blocks` * `n_block_bytes`) bytes, but care is taken to align the allocated memory to with the given alignment value. Additionally, it will detect possible overflow during multiplication.

since: 2.72

aligned_alloc0

This function is similar to g_aligned_alloc(), but it will also clear the allocated memory before returning it.

since: 2.72

aligned_free

Frees the memory allocated by g_aligned_alloc().

since: 2.72

aligned_free_sized

Frees the memory pointed to by `mem`, assuming it is has the given `size` and `alignment`.

since: 2.76

ascii_digit_value

Determines the numeric value of a character as a decimal digit. If the character is not a decimal digit according to `g_ascii_isdigit()`, `-1` is returned.

ascii_dtostr

Converts a `gdouble` to a string, using the ‘.’ as decimal point.

ascii_formatd

Converts a `gdouble` to a string, using the ‘.’ as decimal point. To format the number you pass in a `printf()`-style format string. Allowed conversion specifiers are ‘e’, ‘E’, ‘f’, ‘F’, ‘g’ and ‘G’.

ascii_strcasecmp

Compare two strings, ignoring the case of ASCII characters.

ascii_strdown

Converts all upper case ASCII letters to lower case ASCII letters, with semantics that exactly match `g_ascii_tolower()`.

ascii_string_to_signed

A convenience function for converting a string to a signed number.

since: 2.54

ascii_string_to_unsigned

A convenience function for converting a string to an unsigned number.

since: 2.54

ascii_strncasecmp

Compare `s1` and `s2`, ignoring the case of ASCII characters and any characters after the first `n` in each string. If either string is less than `n` bytes long, comparison will stop at the first nul byte encountered.

ascii_strtod

Converts a string to a floating point value.

ascii_strtoll

Converts a string to a `gint64` value.

since: 2.12

ascii_strtoull

Converts a string to a `guint64` value.

since: 2.2

ascii_strup

Converts all lower case ASCII letters to upper case ASCII letters, with semantics that exactly match `g_ascii_toupper()`.

ascii_tolower

Convert a character to ASCII lower case. If the character is not an ASCII upper case letter, it is returned unchanged.

ascii_toupper

Convert a character to ASCII upper case. If the character is not an ASCII lower case letter, it is returned unchanged.

ascii_xdigit_value

Determines the numeric value of a character as a hexadecimal digit. If the character is not a hex digit according to `g_ascii_isxdigit()`, `-1` is returned.

assert_warning

assertion_message

assertion_message_cmpint

assertion_message_cmpnum

assertion_message_cmpstr

assertion_message_cmpstrv

assertion_message_error

assertion_message_expr

Internal function used to print messages from the public `g_assert()` and `g_assert_not_reached()` macros.

atexit

Specifies a function to be called at normal program termination.

deprecated: 2.32

atomic_int_add

Atomically adds `val` to the value of `atomic`.

since: 2.4

atomic_int_and

Performs an atomic bitwise ‘and’ of the value of `atomic` and `val`, storing the result back in `atomic`.

since: 2.30

atomic_int_compare_and_exchange

Compares `atomic` to `oldval` and, if equal, sets it to `newval`. If `atomic` was not equal to `oldval` then no change occurs.

since: 2.4

atomic_int_compare_and_exchange_full

Compares `atomic` to `oldval` and, if equal, sets it to `newval`. If `atomic` was not equal to `oldval` then no change occurs. In any case the value of `atomic` before this operation is stored in `preval`.

since: 2.74

atomic_int_dec_and_test

Decrements the value of `atomic` by 1.

since: 2.4

atomic_int_exchange

Sets the `atomic` to `newval` and returns the old value from `atomic`.

since: 2.74

atomic_int_exchange_and_add

This function existed before `g_atomic_int_add()` returned the prior value of the integer (which it now does). It is retained only for compatibility reasons. Don’t use this function in new code.

deprecated: 2.30 since: 2.4

atomic_int_get

Gets the current value of `atomic`.

since: 2.4

atomic_int_inc

Increments the value of `atomic` by 1.

since: 2.4

atomic_int_or

Performs an atomic bitwise ‘or’ of the value of `atomic` and `val`, storing the result back in `atomic`.

since: 2.30

atomic_int_set

Sets the value of `atomic` to `newval`.

since: 2.4

atomic_int_xor

Performs an atomic bitwise ‘xor’ of the value of `atomic` and `val`, storing the result back in `atomic`.

since: 2.30

atomic_pointer_add

Atomically adds `val` to the value of `atomic`.

since: 2.30

atomic_pointer_and

Performs an atomic bitwise ‘and’ of the value of `atomic` and `val`, storing the result back in `atomic`.

since: 2.30

atomic_pointer_compare_and_exchange

Compares `atomic` to `oldval` and, if equal, sets it to `newval`. If `atomic` was not equal to `oldval` then no change occurs.

since: 2.4

atomic_pointer_compare_and_exchange_full

Compares `atomic` to `oldval` and, if equal, sets it to `newval`. If `atomic` was not equal to `oldval` then no change occurs. In any case the value of `atomic` before this operation is stored in `preval`.

since: 2.74

atomic_pointer_exchange

Sets the `atomic` to `newval` and returns the old value from `atomic`.

since: 2.74

atomic_pointer_get

Gets the current value of `atomic`.

since: 2.4

atomic_pointer_or

Performs an atomic bitwise ‘or’ of the value of `atomic` and `val`, storing the result back in `atomic`.

since: 2.30

atomic_pointer_set

Sets the value of `atomic` to `newval`.

since: 2.4

atomic_pointer_xor

Performs an atomic bitwise ‘xor’ of the value of `atomic` and `val`, storing the result back in `atomic`.

since: 2.30

atomic_rc_box_acquire

Atomically acquires a reference on the data pointed by `mem_block`.

since: 2.58

atomic_rc_box_alloc

Allocates `block_size` bytes of memory, and adds atomic reference counting semantics to it.

since: 2.58

atomic_rc_box_alloc0

Allocates `block_size` bytes of memory, and adds atomic reference counting semantics to it.

since: 2.58

atomic_rc_box_dup

Allocates a new block of data with atomic reference counting semantics, and copies `block_size` bytes of `mem_block` into it.

since: 2.58

atomic_rc_box_get_size

Retrieves the size of the reference counted data pointed by `mem_block`.

since: 2.58

atomic_rc_box_release

Atomically releases a reference on the data pointed by `mem_block`.

since: 2.58

atomic_rc_box_release_full

Atomically releases a reference on the data pointed by `mem_block`.

since: 2.58

atomic_ref_count_compare

Atomically compares the current value of `arc` with `val`.

since: 2.58

atomic_ref_count_dec

Atomically decreases the reference count.

since: 2.58

atomic_ref_count_inc

Atomically increases the reference count.

since: 2.58

atomic_ref_count_init

Initializes a reference count variable to 1.

since: 2.58

base64_decode

Decode a sequence of Base-64 encoded text into binary data. Note that the returned binary data is not necessarily zero-terminated, so it should not be used as a character string.

since: 2.12

base64_decode_inplace

Decode a sequence of Base-64 encoded text into binary data by overwriting the input data.

since: 2.20

base64_decode_step

Incrementally decode a sequence of binary data from its Base-64 stringified representation. By calling this function multiple times you can convert data in chunks to avoid having to have the full encoded data in memory.

since: 2.12

base64_encode

Encode a sequence of binary data into its Base-64 stringified representation.

since: 2.12

base64_encode_close

Flush the status from a sequence of calls to g_base64_encode_step().

since: 2.12

base64_encode_step

Incrementally encode a sequence of binary data into its Base-64 stringified representation. By calling this function multiple times you can convert data in chunks to avoid having to have the full encoded data in memory.

since: 2.12

basename

Gets the name of the file without any leading directory components. It returns a pointer into the given file name string.

deprecated: 2.2

bit_lock

Sets the indicated `lock_bit` in `address`. If the bit is already set, this call will block until `g_bit_unlock()` unsets the corresponding bit.

since: 2.24

bit_lock_and_get

Sets the indicated `lock_bit` in `address` and atomically returns the new value.

since: 2.86

bit_nth_lsf

Find the position of the first bit set in `mask`, searching from (but not including) `nth_bit` upwards. Bits are numbered from 0 (least significant) to sizeof(#gulong) * 8 - 1 (31 or 63, usually). To start searching from the 0th bit, set `nth_bit` to -1.

bit_nth_msf

Find the position of the first bit set in `mask`, searching from (but not including) `nth_bit` downwards. Bits are numbered from 0 (least significant) to sizeof(#gulong) * 8 - 1 (31 or 63, usually). To start searching from the last bit, set `nth_bit` to -1 or GLIB_SIZEOF_LONG * 8.

bit_storage

Gets the number of bits used to hold `number`, e.g. if `number` is 4, 3 bits are needed.

bit_trylock

Sets the indicated `lock_bit` in `address`, returning `TRUE` if successful. If the bit is already set, returns `FALSE` immediately.

since: 2.24

bit_unlock

Clears the indicated `lock_bit` in `address`. If another thread is currently blocked in `g_bit_lock()` on this same bit then it will be woken up.

since: 2.24

bit_unlock_and_set

This is like `g_bit_unlock()` but also atomically sets `address` to `val`.

since: 2.86

blow_chunks

deprecated: 2.10

build_filename

Creates a filename from a series of elements using the correct separator for the current platform.

build_filename_valist

Creates a filename from a list of elements using the correct separator for the current platform.

since: 2.56

build_filenamev

Creates a filename from a vector of elements using the correct separator for the current platform.

since: 2.8

build_path

Creates a path from a series of elements using `separator` as the separator between elements.

build_pathv

Behaves exactly like g_build_path(), but takes the path elements as a string array, instead of variadic arguments.

since: 2.8

canonicalize_filename

Gets the canonical file name from `filename`. All triple slashes are turned into single slashes, and all `..` and `.`s resolved against `relative_to`.

since: 2.58

chdir

A wrapper for the POSIX `chdir()` function. The function changes the current directory of the process to `path`.

since: 2.8

check_version

Checks that the GLib library in use is compatible with the given version.

since: 2.6

child_watch_add

Sets a function to be called when the child indicated by `pid` exits, at a default priority, `G_PRIORITY_DEFAULT`.

since: 2.4

child_watch_add_full

Sets a function to be called when the child indicated by `pid` exits, at the priority `priority`.

since: 2.4

child_watch_source_new

Creates a new child watch source.

since: 2.4

chmod

A wrapper for the POSIX `chmod()` function. The `chmod()` function is used to set the permissions of a file system object.

since: 2.8

clear_error

If `err` or `*err` is `NULL`, does nothing. Otherwise, calls `g_error_free()` on `*err` and sets `*err` to `NULL`.

clear_fd

If `fd_ptr` points to a file descriptor, close it and return whether closing it was successful, like g_close(). If `fd_ptr` points to a negative number, return `TRUE` without closing anything. In both cases, set `fd_ptr` to `-1` before returning.

since: 2.76

clear_handle_id

Clears a numeric handler, such as a `GSource` ID.

since: 2.56

clear_list

Clears a pointer to a `GList`, freeing it and, optionally, freeing its elements using `destroy`.

since: 2.64

clear_pointer

Clears a reference to a variable.

since: 2.34

clear_slist

Clears a pointer to a `GSList`, freeing it and, optionally, freeing its elements using `destroy`.

since: 2.64

close

This wraps the `close()` call. In case of error, %errno will be preserved, but the error will also be stored as a `GError` in `error`. In case of success, %errno is undefined.

since: 2.36

compute_checksum_for_bytes

Computes the checksum for a binary `data`. This is a convenience wrapper for g_checksum_new(), `g_checksum_get_string()` and g_checksum_free().

since: 2.34

compute_checksum_for_data

Computes the checksum for a binary `data` of `length`. This is a convenience wrapper for g_checksum_new(), `g_checksum_get_string()` and g_checksum_free().

since: 2.16

compute_checksum_for_string

Computes the checksum of a string.

since: 2.16

compute_hmac_for_bytes

Computes the HMAC for a binary `data`. This is a convenience wrapper for g_hmac_new(), `g_hmac_get_string()` and g_hmac_unref().

since: 2.50

compute_hmac_for_data

Computes the HMAC for a binary `data` of `length`. This is a convenience wrapper for g_hmac_new(), `g_hmac_get_string()` and g_hmac_unref().

since: 2.30

compute_hmac_for_string

Computes the HMAC for a string.

since: 2.30

convert

Converts a string from one character set to another.

convert_error_quark

convert_with_fallback

Converts a string from one character set to another, possibly including fallback sequences for characters not representable in the output. Note that it is not guaranteed that the specification for the fallback sequences in `fallback` will be honored. Some systems may do an approximate conversion from `from_codeset` to `to_codeset` in their `iconv()` functions, in which case GLib will simply return that approximate conversion.

convert_with_iconv

Converts a string from one character set to another.

creat

A wrapper for the POSIX `creat()` function. The `creat()` function is used to convert a pathname into a file descriptor, creating a file if necessary.

since: 2.8

datalist_clear

Frees all the data elements of the datalist. The data elements’ destroy functions are called if they have been set.

datalist_foreach

Calls the given function for each data element of the datalist. The function is called with each data element’s `GQuark` id and data, together with the given `user_data` parameter. Note that this function is NOT thread-safe. So unless `datalist` can be protected from any modifications during invocation of this function, it should not be called.

datalist_get_data

Gets a data element, using its string identifier. This is slower than `g_datalist_id_get_data()` because it compares strings.

datalist_get_flags

Gets flags values packed in together with the datalist. See g_datalist_set_flags().

since: 2.8

datalist_id_dup_data

This is a variant of `g_datalist_id_get_data()` which returns a ‘duplicate’ of the value. `dup_func` defines the meaning of ‘duplicate’ in this context, it could e.g. take a reference on a ref-counted object.

since: 2.34

datalist_id_get_data

Retrieves the data element corresponding to `key_id`.

datalist_id_remove_multiple

Removes multiple keys from a datalist.

since: 2.74

datalist_id_remove_no_notify

Removes an element, without calling its destroy notification function.

datalist_id_replace_data

Compares the member that is associated with `key_id` in `datalist` to `oldval`, and if they are the same, replace `oldval` with `newval`.

since: 2.34

datalist_id_set_data_full

Sets the data corresponding to the given `GQuark` id, and the function to be called when the element is removed from the datalist. Any previous data with the same key is removed, and its destroy function is called.

datalist_init

Resets the datalist to `NULL`. It does not free any memory or call any destroy functions.

datalist_set_flags

Turns on flag values for a data list. This function is used to keep a small number of boolean flags in an object with a data list without using any additional space. It is not generally useful except in circumstances where space is very tight. (It is used in the base `GObject` type, for example.).

since: 2.8

datalist_unset_flags

Turns off flag values for a data list. See g_datalist_unset_flags().

since: 2.8

dataset_destroy

Destroys the dataset, freeing all memory allocated, and calling any destroy functions set for data elements.

dataset_foreach

Calls the given function for each data element which is associated with the given location. Note that this function is NOT thread-safe. So unless `dataset_location` can be protected from any modifications during invocation of this function, it should not be called.

dataset_id_get_data

Gets the data element corresponding to a `GQuark`.

dataset_id_remove_no_notify

Removes an element, without calling its destroy notification function.

dataset_id_set_data_full

Sets the data element associated with the given `GQuark` id, and also the function to call when the data element is destroyed. Any previous data with the same key is removed, and its destroy function is called.

dcgettext

This is a variant of `g_dgettext()` that allows specifying a locale category instead of always using `LC_MESSAGES`. See `g_dgettext()` for more information about how this functions differs from calling `dcgettext()` directly.

since: 2.26

dgettext

This function is a wrapper of `dgettext()` which does not translate the message if the default domain as set with `textdomain()` has no translations for the current locale.

since: 2.18

direct_equal

Compares two #gpointer arguments and returns `TRUE` if they are equal. It can be passed to `g_hash_table_new()` as the `key_equal_func` parameter, when using opaque pointers compared by pointer value as keys in a `GHashTable`.

direct_hash

Converts a gpointer to a hash value. It can be passed to `g_hash_table_new()` as the `hash_func` parameter, when using opaque pointers compared by pointer value as keys in a `GHashTable`.

dngettext

This function is a wrapper of `dngettext()` which does not translate the message if the default domain as set with `textdomain()` has no translations for the current locale.

since: 2.18

double_equal

Compares the two #gdouble values being pointed to and returns `TRUE` if they are equal. It can be passed to `g_hash_table_new()` as the `key_equal_func` parameter, when using non-`NULL` pointers to doubles as keys in a `GHashTable`.

since: 2.22

double_hash

Converts a pointer to a #gdouble to a hash value. It can be passed to `g_hash_table_new()` as the `hash_func` parameter, It can be passed to `g_hash_table_new()` as the `hash_func` parameter, when using non-`NULL` pointers to doubles as keys in a `GHashTable`.

since: 2.22

dpgettext

This function is a variant of `g_dgettext()` which supports a disambiguating message context. GNU gettext uses the ‘\004’ character to separate the message context and message id in `msgctxtid`. If 0 is passed as `msgidoffset`, this function will fall back to trying to use the deprecated convention of using “|” as a separation character.

since: 2.16

dpgettext2

This function is a variant of `g_dgettext()` which supports a disambiguating message context. GNU gettext uses the ‘\004’ character to separate the message context and message id in `msgctxtid`.

since: 2.18

environ_getenv

Returns the value of the environment variable `variable` in the provided list `envp`.

since: 2.32

environ_setenv

Sets the environment variable `variable` in the provided list `envp` to `value`.

since: 2.32

environ_unsetenv

Removes the environment variable `variable` from the provided environment `envp`.

since: 2.32

file_error_from_errno

Gets a `GFileError` constant based on the passed-in `err_no`.

file_error_quark

file_get_contents

Reads an entire file into allocated memory, with good error checking.

file_open_tmp

Opens a file for writing in the preferred directory for temporary files (as returned by g_get_tmp_dir()).

file_read_link

Reads the contents of the symbolic link `filename` like the POSIX `readlink()` function.

since: 2.4

file_set_contents

Writes all of `contents` to a file named `filename`. This is a convenience wrapper around calling `g_file_set_contents_full()` with `flags` set to `G_FILE_SET_CONTENTS_CONSISTENT | G_FILE_SET_CONTENTS_ONLY_EXISTING` and `mode` set to `0666`.

since: 2.8

file_set_contents_full

Writes all of `contents` to a file named `filename`, with good error checking. If a file called `filename` already exists it will be overwritten.

since: 2.66

file_test

Returns `TRUE` if any of the tests in the bitfield `test` are `TRUE`. For example, `(G_FILE_TEST_EXISTS | G_FILE_TEST_IS_DIR)` will return `TRUE` if the file exists; the check whether it’s a directory doesn’t matter since the existence test is `TRUE`. With the current set of available tests, there’s no point passing in more than one test at a time.

filename_display_basename

Returns the display basename for the particular filename, guaranteed to be valid UTF-8. The display name might not be identical to the filename, for instance there might be problems converting it to UTF-8, and some files can be translated in the display.

since: 2.6

filename_display_name

Converts a filename into a valid UTF-8 string. The conversion is not necessarily reversible, so you should keep the original around and use the return value of this function only for display purposes. Unlike g_filename_to_utf8(), the result is guaranteed to be non-`NULL` even if the filename actually isn’t in the GLib file name encoding.

since: 2.6

filename_from_uri

Converts an escaped ASCII-encoded URI to a local filename in the encoding used for filenames.

filename_from_utf8

Converts a string from UTF-8 to the encoding GLib uses for filenames. Note that on Windows GLib uses UTF-8 for filenames; on other platforms, this function indirectly depends on the current locale.

filename_to_uri

Converts an absolute filename to an escaped ASCII-encoded URI, with the path component following Section 3.3. of RFC 2396.

filename_to_utf8

Converts a string which is in the encoding used by GLib for filenames into a UTF-8 string. Note that on Windows GLib uses UTF-8 for filenames; on other platforms, this function indirectly depends on the current locale.

find_program_in_path

Locates the first executable named `program` in the user’s path, in the same way that `execvp()` would locate it. Returns an allocated string with the absolute path name, or `NULL` if the program is not found in the path. If `program` is already an absolute path, returns a copy of `program` if `program` exists and is executable, and `NULL` otherwise.

On Windows, if `program` does not have a file type suffix, tries with the suffixes .exe, .cmd, .bat and .com, and the suffixes in the `PATHEXT` environment variable.

fopen

A wrapper for the stdio `fopen()` function. The `fopen()` function opens a file and associates a new stream with it.

since: 2.6

format_size

Formats a size (for example the size of a file) into a human readable string. Sizes are rounded to the nearest size prefix (kB, MB, GB) and are displayed rounded to the nearest tenth. E.g. the file size 3292528 bytes will be converted into the string “3.2 MB”. The returned string is UTF-8, and may use a non-breaking space to separate the number and units, to ensure they aren’t separated when line wrapped.

since: 2.30

format_size_for_display

Formats a size (for example the size of a file) into a human readable string. Sizes are rounded to the nearest size prefix (KB, MB, GB) and are displayed rounded to the nearest tenth. E.g. the file size 3292528 bytes will be converted into the string “3.1 MB”.

deprecated: 2.30 since: 2.16

format_size_full

Formats a size.

since: 2.30

fprintf

An implementation of the standard `fprintf()` function which supports positional parameters, as specified in the Single Unix Specification.

since: 2.2

free

Frees the memory pointed to by `mem`.

free_sized

Frees the memory pointed to by `mem`, assuming it is has the given `size`.

since: 2.76

freopen

A wrapper for the POSIX `freopen()` function. The `freopen()` function opens a file and associates it with an existing stream.

since: 2.6

fsync

A wrapper for the POSIX `fsync()` function. On Windows, `_commit()` will be used. On macOS, `fcntl(F_FULLFSYNC)` will be used. The `fsync()` function is used to synchronize a file’s in-core state with that of the disk.

since: 2.64

get_application_name

Gets a human-readable name for the application, as set by g_set_application_name(). This name should be localized if possible, and is intended for display to the user. Contrast with g_get_prgname(), which gets a non-localized name. If `g_set_application_name()` has not been called, returns the result of `g_get_prgname()` (which may be `NULL` if `g_set_prgname()` has also not been called).

since: 2.2

get_charset

Obtains the character set for the current locale; you might use this character set as an argument to g_convert(), to convert from the current locale’s encoding to some other encoding. (Frequently `g_locale_to_utf8()` and `g_locale_from_utf8()` are nice shortcuts, though.).

get_codeset

Gets the character set for the current locale.

get_console_charset

Obtains the character set used by the console attached to the process, which is suitable for printing output to the terminal.

since: 2.62

get_current_dir

Gets the current directory.

get_current_time

Queries the system wall-clock time.

deprecated: 2.62

get_environ

Gets the list of environment variables for the current process.

since: 2.28

get_filename_charsets

Determines the preferred character sets used for filenames. The first character set from the `charsets` is the filename encoding, the subsequent character sets are used when trying to generate a displayable representation of a filename, see g_filename_display_name().

since: 2.6

get_home_dir

Gets the current user’s home directory.

get_host_name

Return a name for the machine.

since: 2.8

get_language_names

Computes a list of applicable locale names, which can be used to e.g. construct locale-dependent filenames or search paths. The returned list is sorted from most desirable to least desirable and always contains the default locale “C”.

since: 2.6

get_language_names_with_category

Computes a list of applicable locale names with a locale category name, which can be used to construct the fallback locale-dependent filenames or search paths. The returned list is sorted from most desirable to least desirable and always contains the default locale “C”.

since: 2.58

get_locale_variants

Returns a list of derived variants of `locale`, which can be used to e.g. construct locale-dependent filenames or search paths. The returned list is sorted from most desirable to least desirable. This function handles territory, charset and extra locale modifiers. See `setlocale(3)` for information about locales and their format.

since: 2.28

get_monotonic_time

Queries the system monotonic time in microseconds.

since: 2.28

get_monotonic_time_ns

Queries the system monotonic time in nanoseconds.

since: 2.88

get_num_processors

Determine the approximate number of threads that the system will schedule simultaneously for this process. This is intended to be used as a parameter to `g_thread_pool_new()` for CPU bound tasks and similar cases.

since: 2.36

get_os_info

Get information about the operating system.

since: 2.64

get_prgname

Gets the name of the program. This name should not be localized, in contrast to g_get_application_name().

get_real_name

Gets the real name of the user. This usually comes from the user’s entry in the `passwd` file. The encoding of the returned string is system-defined. (On Windows, it is, however, always UTF-8.) If the real user name cannot be determined, the string “Unknown” is returned.

get_real_time

Queries the system wall-clock time.

since: 2.28

get_system_config_dirs

Returns an ordered list of base directories in which to access system-wide configuration information.

since: 2.6

get_system_data_dirs

Returns an ordered list of base directories in which to access system-wide application data.

since: 2.6

get_tmp_dir

Gets the directory to use for temporary files.

get_user_cache_dir

Returns a base directory in which to store non-essential, cached data specific to particular user.

since: 2.6

get_user_config_dir

Returns a base directory in which to store user-specific application configuration information such as user preferences and settings.

since: 2.6

get_user_data_dir

Returns a base directory in which to access application data such as icons that is customized for a particular user.

since: 2.6

get_user_name

Gets the user name of the current user. The encoding of the returned string is system-defined. On UNIX, it might be the preferred file name encoding, or something else, and there is no guarantee that it is even consistent on a machine. On Windows, it is always UTF-8.

get_user_runtime_dir

Returns a directory that is unique to the current user on the local system.

since: 2.28

get_user_special_dir

Returns the full path of a special directory using its logical id.

since: 2.14

get_user_state_dir

Returns a base directory in which to store state files specific to particular user.

since: 2.72

getenv

Returns the value of an environment variable.

hostname_is_ascii_encoded

Tests if `hostname` contains segments with an ASCII-compatible encoding of an Internationalized Domain Name. If this returns `TRUE`, you should decode the hostname with `g_hostname_to_unicode()` before displaying it to the user.

since: 2.22

hostname_is_ip_address

Tests if `hostname` is the string form of an IPv4 or IPv6 address. (Eg, “192.168.0.1”.).

since: 2.22

hostname_is_non_ascii

Tests if `hostname` contains Unicode characters. If this returns `TRUE`, you need to encode the hostname with `g_hostname_to_ascii()` before using it in non-IDN-aware contexts.

since: 2.22

hostname_to_ascii

Converts `hostname` to its canonical ASCII form; an ASCII-only string containing no uppercase letters and not ending with a trailing dot.

since: 2.22

hostname_to_unicode

Converts `hostname` to its canonical presentation form; a UTF-8 string in Unicode normalization form C, containing no uppercase letters, no forbidden characters, and no ASCII-encoded segments, and not ending with a trailing dot.

since: 2.22

iconv

Same as the standard UNIX routine iconv(), but may be implemented via libiconv on UNIX flavors that lack a native implementation.

idle_add

Adds a function to be called whenever there are no higher priority events pending to the default main loop.

idle_add_full

Adds a function to be called whenever there are no higher priority events pending.

idle_add_once

Adds a function to be called whenever there are no higher priority events pending to the default main loop.

since: 2.74

idle_remove_by_data

Removes the idle function with the given data.

idle_source_new

Creates a new idle source.

int64_equal

Compares the two #gint64 values being pointed to and returns `TRUE` if they are equal. It can be passed to `g_hash_table_new()` as the `key_equal_func` parameter, when using non-`NULL` pointers to 64-bit integers as keys in a `GHashTable`.

since: 2.22

int64_hash

Converts a pointer to a #gint64 to a hash value.

since: 2.22

int_equal

Compares the two #gint values being pointed to and returns `TRUE` if they are equal. It can be passed to `g_hash_table_new()` as the `key_equal_func` parameter, when using non-`NULL` pointers to integers as keys in a `GHashTable`.

int_hash

Converts a pointer to a #gint to a hash value. It can be passed to `g_hash_table_new()` as the `hash_func` parameter, when using non-`NULL` pointers to integer values as keys in a `GHashTable`.

intern_static_string

Returns a canonical representation for `string`. Interned strings can be compared for equality by comparing the pointers, instead of using strcmp(). `g_intern_static_string()` does not copy the string, therefore `string` must not be freed or modified.

since: 2.10

intern_string

Returns a canonical representation for `string`. Interned strings can be compared for equality by comparing the pointers, instead of using strcmp().

since: 2.10

io_add_watch

Adds the `GIOChannel` into the default main loop context with the default priority.

io_add_watch_full

Adds the `GIOChannel` into the default main loop context with the given priority.

io_create_watch

Creates a `GSource` that’s dispatched when `condition` is met for the given `channel`. For example, if condition is `G_IO_IN`, the source will be dispatched when there’s data available for reading.

listenv

Gets the names of all variables set in the environment.

since: 2.8

locale_from_utf8

Converts a string from UTF-8 to the encoding used for strings by the C runtime (usually the same as that used by the operating system) in the current locale. On Windows this means the system codepage.

locale_to_utf8

Converts a string which is in the encoding used for strings by the C runtime (usually the same as that used by the operating system) in the current locale into a UTF-8 string.

log

Logs an error or debugging message.

log_default_handler

The default log handler set up by GLib; `g_log_set_default_handler()` allows to install an alternate default log handler.

log_get_always_fatal

Gets the current fatal mask.

since: 2.86

log_get_debug_enabled

Return whether debug output from the GLib logging system is enabled.

since: 2.72

log_remove_handler

Removes the log handler.

log_set_always_fatal

Sets the message levels which are always fatal, in any log domain.

log_set_debug_enabled

Enable or disable debug output from the GLib logging system for all domains.

since: 2.72

log_set_default_handler

Installs a default log handler which is used if no log handler has been set for the particular log domain and log level combination.

since: 2.6

log_set_fatal_mask

Sets the log levels which are fatal in the given domain.

log_set_handler

Sets the log handler for a domain and a set of log levels.

log_set_handler_full

Like `g_log_set_handler()`, but takes a destroy notify for the `user_data`.

since: 2.46

log_set_writer_func

Set a writer function which will be called to format and write out each log message.

since: 2.50

log_structured

Log a message with structured data.

since: 2.50

log_structured_array

Log a message with structured data.

since: 2.50

log_structured_standard

log_variant

Log a message with structured data, accepting the data within a `GVariant`.

since: 2.50

log_writer_default

Format a structured log message and output it to the default log destination for the platform.

since: 2.50

log_writer_default_set_debug_domains

Reset the list of domains to be logged, that might be initially set by the `G_MESSAGES_DEBUG` or `DEBUG_INVOCATION` environment variables.

since: 2.80

log_writer_default_set_use_stderr

Configure whether the built-in log functions will output all log messages to `stderr`.

since: 2.68

log_writer_default_would_drop

Check whether `g_log_writer_default()` and `g_log_default_handler()` would ignore a message with the given domain and level.

since: 2.68

log_writer_format_fields

Format a structured log message as a string suitable for outputting to the terminal (or elsewhere).

since: 2.50

log_writer_is_journald

Check whether the given `output_fd` file descriptor is a connection to the systemd journal, or something else (like a log file or `stdout` or `stderr`).

since: 2.50

log_writer_journald

Format a structured log message and send it to the systemd journal as a set of key–value pairs.

since: 2.50

log_writer_standard_streams

Format a structured log message and print it to either `stdout` or `stderr`, depending on its log level.

since: 2.50

log_writer_supports_color

Check whether the given `output_fd` file descriptor supports ANSI color escape sequences.

since: 2.50

log_writer_syslog

Format a structured log message and send it to the syslog daemon. Only fields which are understood by this function are included in the formatted string which is printed.

since: 2.80

logv

Logs an error or debugging message.

lstat

A wrapper for the POSIX `lstat()` function. The `lstat()` function is like `stat()` except that in the case of symbolic links, it returns information about the symbolic link itself and not the file that it refers to. If the system does not support symbolic links `g_lstat()` is identical to g_stat().

since: 2.6

main_current_source

Returns the currently firing source for this thread.

since: 2.12

main_depth

Returns the depth of the stack of calls to `g_main_context_dispatch()` on any `GMainContext` in the current thread.

malloc

Allocates `n_bytes` bytes of memory. If `n_bytes` is 0 it returns `NULL`.

malloc0

Allocates `n_bytes` bytes of memory, initialized to 0’s. If `n_bytes` is 0 it returns `NULL`.

malloc0_n

This function is similar to g_malloc0(), allocating (`n_blocks` * `n_block_bytes`) bytes, but care is taken to detect possible overflow during multiplication.

since: 2.24

malloc_n

This function is similar to g_malloc(), allocating (`n_blocks` * `n_block_bytes`) bytes, but care is taken to detect possible overflow during multiplication.

since: 2.24

markup_collect_attributes

Collects the attributes of the element from the data passed to the `GMarkupParser` start_element function, dealing with common error conditions and supporting boolean values.

since: 2.16

markup_error_quark

markup_escape_text

Escapes text so that the markup parser will parse it verbatim. Less than, greater than, ampersand, etc. are replaced with the corresponding entities. This function would typically be used when writing out a file to be parsed with the markup parser.

markup_printf_escaped

Formats arguments according to `format`, escaping all string and character arguments in the fashion of g_markup_escape_text(). This is useful when you want to insert literal strings into XML-style markup output, without having to worry that the strings might themselves contain markup.

since: 2.4

markup_vprintf_escaped

Formats the data in `args` according to `format`, escaping all string and character arguments in the fashion of g_markup_escape_text(). See g_markup_printf_escaped().

since: 2.4

mem_is_system_malloc

Checks whether the allocator used by `g_malloc()` is the system’s malloc implementation. If it returns `TRUE` memory allocated with `malloc()` can be used interchangeably with memory allocated using g_malloc(). This function is useful for avoiding an extra copy of allocated memory returned by a non-GLib-based API.

deprecated: 2.46

mem_profile

GLib used to support some tools for memory profiling, but this no longer works. There are many other useful tools for memory profiling these days which can be used instead.

deprecated: 2.46

mem_set_vtable

This function used to let you override the memory allocation function. However, its use was incompatible with the use of global constructors in GLib and GIO, because those use the GLib allocators before main is reached. Therefore this function is now deprecated and is just a stub.

deprecated: 2.46

memdup

Allocates `byte_size` bytes of memory, and copies `byte_size` bytes into it from `mem`. If `mem` is `NULL` it returns `NULL`.

deprecated: 2.68

memdup2

Allocates `byte_size` bytes of memory, and copies `byte_size` bytes into it from `mem`. If `mem` is `NULL` it returns `NULL`.

since: 2.68

mkdir

A wrapper for the POSIX `mkdir()` function. The `mkdir()` function attempts to create a directory with the given name and permissions. The mode argument is ignored on Windows.

since: 2.6

mkdir_with_parents

Create a directory if it doesn’t already exist. Create intermediate parent directories as needed, too.

since: 2.8

mkdtemp

Creates a temporary directory in the current directory.

since: 2.30

mkdtemp_full

Creates a temporary directory in the current directory.

since: 2.30

mkstemp

Opens a temporary file in the current directory.

mkstemp_full

Opens a temporary file in the current directory.

since: 2.22

nullify_pointer

Set the pointer at the specified location to `NULL`.

number_parser_error_quark

on_error_query

Prompts the user with `[E]xit, [H]alt, show [S]tack trace or [P]roceed`. This function is intended to be used for debugging use only. The following example shows how it can be used together with the `g_log()` functions.

on_error_stack_trace

Invokes gdb, which attaches to the current process and shows a stack trace. Called by `g_on_error_query()` when the “[S]tack trace” option is selected. You can get the current process’s program name with g_get_prgname(), assuming that you have called `gtk_init()` or gdk_init().

open

A wrapper for the POSIX `open()` function. The `open()` function is used to convert a pathname into a file descriptor.

since: 2.6

option_error_quark

parse_debug_string

Parses a string containing debugging options into a %guint containing bit flags. This is used within GDK and GTK to parse the debug options passed on the command line or through environment variables.

path_get_basename

Gets the last component of the filename.

path_get_dirname

Gets the directory components of a file name. For example, the directory component of `/usr/bin/test` is `/usr/bin`. The directory component of `/` is `/`.

path_is_absolute

Returns `TRUE` if the given `file_name` is an absolute file name. Note that this is a somewhat vague concept on Windows.

path_skip_root

Returns a pointer into `file_name` after the root component, i.e. after the “/” in UNIX or “C:" under Windows. If `file_name` is not an absolute path it returns `NULL`.

pattern_match

Matches a string against a compiled pattern.

deprecated: 2.70

pattern_match_simple

Matches a string against a pattern given as a string.

pattern_match_string

Matches a string against a compiled pattern.

deprecated: 2.70

pointer_bit_lock

This is equivalent to g_bit_lock, but working on pointers (or other pointer-sized values).

since: 2.30

pointer_bit_lock_and_get

This is equivalent to g_bit_lock, but working on pointers (or other pointer-sized values).

since: 2.80

pointer_bit_lock_mask_ptr

This mangles `ptr` as `g_pointer_bit_lock()` and `g_pointer_bit_unlock()` do.

since: 2.80

pointer_bit_trylock

This is equivalent to g_bit_trylock(), but working on pointers (or other pointer-sized values).

since: 2.30

pointer_bit_unlock

This is equivalent to g_bit_unlock, but working on pointers (or other pointer-sized values).

since: 2.30

pointer_bit_unlock_and_set

This is equivalent to `g_pointer_bit_unlock()` and atomically setting the pointer value.

since: 2.80

poll

Polls `fds`, as with the `poll()` system call, but portably. (On systems that don’t have poll(), it is emulated using select().) This is used internally by `GMainContext`, but it can be called directly if you need to block until a file descriptor is ready, but don’t want to run the full main loop.

since: 2.20

prefix_error

Formats a string according to `format` and prefix it to an existing error message. If `err` is `NULL` (ie: no error variable) then do nothing.

since: 2.16

prefix_error_literal

Prefixes `prefix` to an existing error message. If `err` or `*err` is `NULL` (i.e.: no error variable) then do nothing.

since: 2.70

print

Outputs a formatted message via the print handler.

printerr

Outputs a formatted message via the error message handler.

printf

An implementation of the standard `printf()` function which supports positional parameters, as specified in the Single Unix Specification.

since: 2.2

printf_string_upper_bound

Calculates the maximum space needed to store the output of the `sprintf()` function.

propagate_error

If `dest` is `NULL`, free `src`; otherwise, moves `src` into `*dest`. The error variable `dest` points to must be `NULL`.

propagate_prefixed_error

If `dest` is `NULL`, free `src`; otherwise, moves `src` into `*dest`. `*dest` must be `NULL`. After the move, add a prefix as with g_prefix_error().

since: 2.16

qsort_with_data

This is just like the standard C `qsort()` function, but the comparison routine accepts a user data argument (like `qsort_r()`).

deprecated: 2.82

quark_from_static_string

Gets the `GQuark` identifying the given (static) string. If the string does not currently have an associated `GQuark`, a new `GQuark` is created, linked to the given string.

quark_from_string

Gets the `GQuark` identifying the given string. If the string does not currently have an associated `GQuark`, a new `GQuark` is created, using a copy of the string.

quark_to_string

Gets the string associated with the given `GQuark`.

quark_try_string

Gets the `GQuark` associated with the given string, or 0 if string is `NULL` or it has no associated `GQuark`.

random_double

Returns a random #gdouble equally distributed over the range [0..1).

random_double_range

Returns a random #gdouble equally distributed over the range [`begin`..`end`).

random_int

Return a random #guint32 equally distributed over the range [0..2^32-1].

random_int_range

Returns a random #gint32 equally distributed over the range [`begin`..`end`-1].

random_set_seed

Sets the seed for the global random number generator, which is used by the g_random_* functions, to `seed`.

rc_box_acquire

Acquires a reference on the data pointed by `mem_block`.

since: 2.58

rc_box_alloc

Allocates `block_size` bytes of memory, and adds reference counting semantics to it.

since: 2.58

rc_box_alloc0

Allocates `block_size` bytes of memory, and adds reference counting semantics to it.

since: 2.58

rc_box_dup

Allocates a new block of data with reference counting semantics, and copies `block_size` bytes of `mem_block` into it.

since: 2.58

rc_box_get_size

Retrieves the size of the reference counted data pointed by `mem_block`.

since: 2.58

rc_box_release

Releases a reference on the data pointed by `mem_block`.

since: 2.58

rc_box_release_full

Releases a reference on the data pointed by `mem_block`.

since: 2.58

realloc

Reallocates the memory pointed to by `mem`, so that it now has space for `n_bytes` bytes of memory. It returns the new address of the memory, which may have been moved. `mem` may be `NULL`, in which case it’s considered to have zero-length. `n_bytes` may be 0, in which case `NULL` will be returned and `mem` will be freed unless it is `NULL`.

realloc_n

This function is similar to g_realloc(), allocating (`n_blocks` * `n_block_bytes`) bytes, but care is taken to detect possible overflow during multiplication.

since: 2.24

ref_count_compare

Compares the current value of `rc` with `val`.

since: 2.58

ref_count_dec

Decreases the reference count.

since: 2.58

ref_count_inc

Increases the reference count.

since: 2.58

ref_count_init

Initializes a reference count variable to 1.

since: 2.58

ref_string_acquire

Acquires a reference on a string.

since: 2.58

ref_string_equal

Compares two ref-counted strings for byte-by-byte equality.

since: 2.84

ref_string_length

Retrieves the length of `str`.

since: 2.58

ref_string_new

Creates a new reference counted string and copies the contents of `str` into it.

since: 2.58

ref_string_new_intern

Creates a new reference counted string and copies the content of `str` into it.

since: 2.58

ref_string_new_len

Creates a new reference counted string and copies the contents of `str` into it, up to `len` bytes.

since: 2.58

ref_string_release

Releases a reference on a string; if it was the last reference, the resources allocated by the string are freed as well.

since: 2.58

reload_user_special_dirs_cache

Resets the cache used for g_get_user_special_dir(), so that the latest on-disk version is used. Call this only if you just changed the data on disk yourself.

since: 2.22

remove

A wrapper for the POSIX `remove()` function. The `remove()` function deletes a name from the filesystem.

since: 2.6

rename

A wrapper for the POSIX `rename()` function. The `rename()` function renames a file, moving it between directories if required.

since: 2.6

return_if_fail_warning

Internal function used to print messages from the public `g_return_if_fail()` and `g_return_val_if_fail()` macros.

rmdir

A wrapper for the POSIX `rmdir()` function. The `rmdir()` function deletes a directory from the filesystem.

since: 2.6

set_application_name

Sets a human-readable name for the application. This name should be localized if possible, and is intended for display to the user. Contrast with g_set_prgname(), which sets a non-localized name. `g_set_prgname()` will be called automatically by gtk_init(), but `g_set_application_name()` will not.

since: 2.2

set_error

Does nothing if `err` is `NULL`; if `err` is non-`NULL`, then `*err` must be `NULL`. A new `GError` is created and assigned to `*err`.

set_error_literal

Does nothing if `err` is `NULL`; if `err` is non-`NULL`, then `*err` must be `NULL`. A new `GError` is created and assigned to `*err`. Unlike g_set_error(), `message` is not a printf()-style format string. Use this function if `message` contains text you don’t have control over, that could include `printf()` escape sequences.

since: 2.18

set_prgname

Sets the name of the program. This name should not be localized, in contrast to g_set_application_name().

set_print_handler

Sets the print handler to `func`, or resets it to the default GLib handler if `NULL`.

set_printerr_handler

Sets the handler for printing error messages to `func`, or resets it to the default GLib handler if `NULL`.

set_str

Updates a pointer to a string to a copy of `new_str` and returns whether the string was changed.

since: 2.76

set_str_take

Updates a pointer to a string to `new_str` and returns whether the string was changed. Steals ownership of `new_str`.

unstable since: 2.90

set_strv

Safely replaces a string vector.

unstable since: 2.90

set_strv_take

Safely replaces a string vector, taking ownership of the new value.

unstable since: 2.90

setenv

Sets an environment variable. On UNIX, both the variable’s name and value can be arbitrary byte strings, except that the variable’s name cannot contain ‘=’. On Windows, they should be in UTF-8.

since: 2.4

shell_error_quark

shell_parse_argv

Parses a command line into an argument vector, in much the same way the shell would, but without many of the expansions the shell would perform (variable expansion, globs, operators, filename expansion, etc. are not supported).

shell_quote

Quotes a string so that the shell (/bin/sh) will interpret the quoted string to mean `unquoted_string`.

shell_unquote

Unquotes a string as the shell (/bin/sh) would.

slice_alloc

Allocates a block of memory from the libc allocator.

since: 2.10

slice_alloc0

Allocates a block of memory via `g_slice_alloc()` and initializes the returned memory to 0.

since: 2.10

slice_copy

Allocates a block of memory from the slice allocator and copies `block_size` bytes into it from `mem_block`.

since: 2.14

slice_free1

Frees a block of memory.

since: 2.10

slice_free_chain_with_offset

Frees a linked list of memory blocks of structure type `type`.

since: 2.10

slice_get_config

slice_get_config_state

slice_set_config

snprintf

A safer form of the standard `sprintf()` function. The output is guaranteed to not exceed `n` characters (including the terminating nul character), so it is easy to ensure that a buffer overflow cannot occur.

sort_array

This is just like the standard C `qsort()` function, but the comparison routine accepts a user data argument (like `qsort_r()`).

since: 2.82

spaced_primes_closest

Gets the smallest prime number from a built-in array of primes which is larger than `num`. This is used within GLib to calculate the optimum size of a `GHashTable`.

spawn_async

Executes a child program asynchronously.

spawn_async_with_fds

Executes a child program asynchronously.

since: 2.58

spawn_async_with_pipes

Identical to `g_spawn_async_with_pipes_and_fds()` but with `n_fds` set to zero, so no FD assignments are used.

spawn_async_with_pipes_and_fds

Executes a child program asynchronously (your program will not block waiting for the child to exit).

since: 2.68

spawn_check_exit_status

An old name for g_spawn_check_wait_status(), deprecated because its name is misleading.

deprecated: 2.70 since: 2.34

spawn_check_wait_status

Set `error` if `wait_status` indicates the child exited abnormally (e.g. with a nonzero exit code, or via a fatal signal).

since: 2.70

spawn_close_pid

On some platforms, notably Windows, the `GPid` type represents a resource which must be closed to prevent resource leaking. `g_spawn_close_pid()` is provided for this purpose. It should be used on all platforms, even though it doesn’t do anything under UNIX.

spawn_command_line_async

A simple version of `g_spawn_async()` that parses a command line with `g_shell_parse_argv()` and passes it to g_spawn_async().

spawn_command_line_sync

A simple version of `g_spawn_sync()` with little-used parameters removed, taking a command line instead of an argument vector.

spawn_error_quark

spawn_exit_error_quark

spawn_sync

Executes a child synchronously (waits for the child to exit before returning).

sprintf

An implementation of the standard `sprintf()` function which supports positional parameters, as specified in the Single Unix Specification.

since: 2.2

stat

A wrapper for the POSIX `stat()` function. The `stat()` function returns information about a file. On Windows the `stat()` function in the C library checks only the FAT-style READONLY attribute and does not look at the ACL at all. Thus on Windows the protection bits in the `st_mode` field are a fabrication of little use.

since: 2.6

steal_fd

Sets `fd_ptr` to `-1`, returning the value that was there before.

since: 2.70

steal_handle_id

Sets `handle_pointer` to `0`, returning the value that was there before.

since: 2.84

steal_pointer

Sets `pp` to `NULL`, returning the value that was there before.

since: 2.44

stpcpy

Copies a nul-terminated string into the destination buffer, including the trailing nul byte, and returns a pointer to the trailing nul byte in `dest`. The return value is useful for concatenating multiple strings without having to repeatedly scan for the end.
