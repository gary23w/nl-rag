---
title: "GLib (part 3/3)"
source: https://docs.gtk.org/glib/
domain: gtk4
license: CC-BY-SA-4.0
tags: gtk4 toolkit, gtk widgets, gnome application, libadwaita styling
fetched: 2026-07-02
part: 3/3
---

# GLib

Determines whether a character is digit (0-9).

ascii_isgraph

Determines whether a character is a printing character and not a space.

ascii_islower

Determines whether a character is an ASCII lower case letter.

ascii_isprint

Determines whether a character is a printing character.

ascii_ispunct

Determines whether a character is a punctuation character.

ascii_isspace

Determines whether a character is a white-space character.

ascii_isupper

Determines whether a character is an ASCII upper case letter.

ascii_isxdigit

Determines whether a character is a hexadecimal-digit character.

assert

Debugging macro to terminate the application if the assertion fails.

assert_cmpfloat

Debugging macro to compare two floating point numbers.

since: 2.16

assert_cmpfloat_with_epsilon

Debugging macro to compare two floating point numbers within an epsilon.

since: 2.58

assert_cmphex

Debugging macro to compare to unsigned integers.

since: 2.16

assert_cmpint

Debugging macro to compare two integers.

since: 2.16

assert_cmpmem

Debugging macro to compare memory regions.

since: 2.46

assert_cmpstr

Debugging macro to compare two strings.

since: 2.16

assert_cmpstrv

Debugging macro to check if two `NULL`-terminated string arrays (i.e. 2 `GStrv`) are equal.

since: 2.68

assert_cmpuint

Debugging macro to compare two unsigned integers.

since: 2.16

assert_cmpvariant

Debugging macro to compare two `GVariant` values.

since: 2.60

assert_error

Debugging macro to check that a method has returned the correct `GError`.

since: 2.20

assert_false

Debugging macro to check an expression is false.

since: 2.38

assert_no_errno

Debugging macro to check that an expression has a non-negative return value, as used by traditional POSIX functions (such as `rmdir()`) to indicate success.

since: 2.66

assert_no_error

Debugging macro to check that a `GError` is not set.

since: 2.20

assert_nonnull

Debugging macro to check an expression is not `NULL`.

since: 2.40

assert_not_reached

Debugging macro to terminate the application if it is ever reached.

assert_null

Debugging macro to check an expression is `NULL`.

since: 2.38

assert_true

Debugging macro to check that an expression is true.

since: 2.38

ATEXIT

atomic_rc_box_new

A convenience macro to allocate atomically reference counted data with the size of the given `type`.

since: 2.58

atomic_rc_box_new0

A convenience macro to allocate atomically reference counted data with the size of the given `type`, and set its contents to zero.

since: 2.58

AUTO_LOCK

Works like `G_MUTEX_AUTO_LOCK()`, but for a lock defined with `G_LOCK_DEFINE()`.

since: 2.80

BREAKPOINT

Inserts a breakpoint instruction into the code.

C_STD_CHECK_VERSION

Macro to check if the current compiler supports a specified `version` of the C standard. Such value must be numeric and can be provided both in the short form for the well-known versions (e.g. `90`, `99`…) or in the complete form otherwise (e.g. `199000L`, `199901L`, `205503L`…).

since: 2.76

CHECK_VERSION

Checks whether the version of the GLib library that is being compiled against is greater than or equal to the given one.

chunk_free

deprecated: 2.10

chunk_new

deprecated: 2.10

chunk_new0

deprecated: 2.10

critical

Logs a ‘critical warning’ (`G_LOG_LEVEL_CRITICAL`).

CXX_STD_CHECK_VERSION

Macro to check if the current compiler supports a specified `version` of the C++ standard. Such value must be numeric and can be provided both in the short form for the well-known versions (e.g. `11`, `17`…) or in the complete form otherwise (e.g. `201103L`, `201703L`, `205503L`…).

since: 2.76

datalist_id_remove_data

Removes an element, using its `GQuark` identifier.

datalist_id_set_data

Sets the data corresponding to the given `GQuark` id. Any previous data with the same key is removed, and its destroy function is called.

datalist_remove_data

Removes an element using its string identifier. The data element’s destroy function is called if it has been set.

datalist_remove_no_notify

Removes an element, without calling its destroy notifier.

datalist_set_data

Sets the data element corresponding to the given string identifier.

datalist_set_data_full

Sets the data element corresponding to the given string identifier, and the function to be called when the data element is removed.

dataset_get_data

Gets the data element corresponding to a string.

dataset_id_remove_data

Removes a data element from a dataset. The data element’s destroy function is called if it has been set.

dataset_id_set_data

Sets the data element associated with the given `GQuark` id. Any previous data with the same key is removed, and its destroy function is called.

dataset_remove_data

Removes a data element corresponding to a string. Its destroy function is called if it has been set.

dataset_remove_no_notify

Removes an element, without calling its destroy notifier.

dataset_set_data

Sets the data corresponding to the given string identifier.

dataset_set_data_full

Sets the data corresponding to the given string identifier, and the function to call when the data element is destroyed.

debug

A convenience function/macro to log a debug message.

since: 2.6

DEBUG_HERE

A convenience form of g_log_structured(), recommended to be added to functions when debugging. It prints the current monotonic time and the code location using `G_STRLOC`.

since: 2.50

DEFINE_AUTO_CLEANUP_CLEAR_FUNC

Defines the appropriate cleanup function for a type.

since: 2.44

DEFINE_AUTO_CLEANUP_FREE_FUNC

Defines the appropriate cleanup function for a type.

since: 2.44

DEFINE_AUTOPTR_CLEANUP_FUNC

Defines the appropriate cleanup function for a pointer type.

since: 2.44

DEFINE_EXTENDED_ERROR

A convenience macro which defines two functions. First, returning the `GQuark` for the extended error type `ErrorType`; it is called `error_type_quark()`. Second, returning the private data from a passed `GError`; it is called `error_type_get_private()`.

since: 2.68

DEFINE_QUARK

A convenience macro which defines a function returning the `GQuark` for the name `QN`. The function will be named `q_n_quark`().

since: 2.34

DEPRECATED_ENUMERATOR_FOR

DEPRECATED_FOR

DEPRECATED_MACRO_FOR

DEPRECATED_TYPE_FOR

ENCODE_VERSION

Encode a major.minor version as a single integer.

since: 2.32

error

A convenience function/macro to log an error message.

GINT64_CONSTANT

GNUC_ALLOC_SIZE

Expands to the GNU C `alloc_size` function attribute if the compiler is a new enough gcc. This attribute tells the compiler that the function returns a pointer to memory of a size that is specified by the `xth` function parameter.

since: 2.18

GNUC_ALLOC_SIZE2

Expands to the GNU C `alloc_size` function attribute if the compiler is a new enough gcc. This attribute tells the compiler that the function returns a pointer to memory of a size that is specified by the product of two function parameters.

since: 2.18

GNUC_CHECK_VERSION

Expands to a check for a compiler with **GNUC** defined and a version greater than or equal to the major and minor numbers provided. For example, the following would only match on compilers such as GCC 4.8 or newer.

since: 2.42

GNUC_DEPRECATED_FOR

Like `G_GNUC_DEPRECATED`, but names the intended replacement for the deprecated symbol if the version of gcc in use is new enough to support custom deprecation messages.

since: 2.26

GNUC_FORMAT

Expands to the GNU C `format_arg` function attribute if the compiler is gcc. This function attribute specifies that a function takes a format string for a `printf()`, `scanf()`, `strftime()` or `strfmon()` style function and modifies it, so that the result can be passed to a `printf()`, `scanf()`, `strftime()` or `strfmon()` style function (with the remaining arguments to the format function the same as they would have been for the unmodified string).

GNUC_PRINTF

Expands to the GNU C `format` function attribute if the compiler is gcc. This is used for declaring functions which take a variable number of arguments, with the same syntax as `printf()`. It allows the compiler to type-check the arguments passed to the function.

GNUC_SCANF

Expands to the GNU C `format` function attribute if the compiler is gcc. This is used for declaring functions which take a variable number of arguments, with the same syntax as `scanf()`. It allows the compiler to type-check the arguments passed to the function.

GNUC_STRFTIME

Expands to the GNU C `strftime` format function attribute if the compiler is gcc. This is used for declaring functions which take a format argument which is passed to `strftime()` or an API implementing its formats. It allows the compiler check the format passed to the function.

since: 2.60

GOFFSET_CONSTANT

GUINT64_CONSTANT

hash_table_freeze

This function is deprecated and will be removed in the next major release of GLib. It does nothing.

hash_table_thaw

This function is deprecated and will be removed in the next major release of GLib. It does nothing.

HOOK_ACTIVE

Returns `TRUE` if the `GHook` is active, which is normally the case until the `GHook` is destroyed.

hook_append

Appends a `GHook` onto the end of a `GHookList`.

HOOK_FLAGS

Gets the flags of a hook.

HOOK_IN_CALL

Returns `TRUE` if the `GHook` function is currently executing.

htonl

Converts a 32-bit integer value from host to network byte order.

htons

Converts a 16-bit integer value from host to network byte order.

info

A convenience function/macro to log an informational message.

since: 2.40

LIKELY

Hints the compiler that the expression is likely to evaluate to a true value. The compiler may use this information for optimizations.

since: 2.2

list_next

A convenience macro to get the next element in a `GList`. Note that it is considered perfectly acceptable to access `list`->next directly.

list_previous

A convenience macro to get the previous element in a `GList`. Note that it is considered perfectly acceptable to access `list`->prev directly.

LOCK

Works like g_mutex_lock(), but for a lock defined with `G_LOCK_DEFINE`.

LOCK_DEFINE

The `G_LOCK_` macros provide a convenient interface to `GMutex`. `G_LOCK_DEFINE` defines a lock. It can appear in any place where variable definitions may appear in programs, i.e. in the first block of a function or outside of functions. The `name` parameter will be mangled to get the name of the `GMutex`. This means that you can use names of existing variables as the parameter - e.g. the name of the variable you intend to protect with the lock. Look at our `give_me_next_number()` example using the `G_LOCK` macros:.

LOCK_DEFINE_STATIC

This works like `G_LOCK_DEFINE`, but it creates a static object.

LOCK_EXTERN

This declares a lock, that is defined with `G_LOCK_DEFINE` in another module.

LOCK_NAME

main_destroy

Frees the memory allocated for the `GMainLoop`.

deprecated: 2.2

main_is_running

Checks if the main loop is running.

deprecated: 2.2

main_iteration

Runs a single iteration for the default `GMainContext`.

deprecated: 2.2

main_new

Creates a new `GMainLoop` for th default main context.

deprecated: 2.2

main_pending

Checks if any events are pending for the default `GMainContext` (i.e. ready to be processed).

deprecated: 2.2

main_quit

Stops the `GMainLoop`. If `g_main_run()` was called to run the `GMainLoop`, it will now return.

deprecated: 2.2

main_run

Runs a main loop until it stops running.

deprecated: 2.2

main_set_poll_func

Sets the function to use for the handle polling of file descriptors for the default main context.

deprecated: 2.2

mem_chunk_create

deprecated: 2.10

memmove

Copies a block of memory `len` bytes long, from `src` to `dest`. The source and destination areas may overlap.

deprecated: 2.40

message

A convenience function/macro to log a normal message.

MUTEX_AUTO_LOCK

Declare a `GMutexLocker` variable with `g_autoptr()` and lock the mutex. The mutex will be unlocked automatically when leaving the scope. The variable is declared with `G_GNUC_UNUSED` to avoid compiler warning if it is not used in the scope.

since: 2.80.0

N_ELEMENTS

Determines the number of elements in an array. The array must be declared so the compiler knows its size at compile-time; this macro will not work on an array allocated on the heap, only static arrays or arrays on the stack.

new

Allocates `n_structs` elements of type `struct_type`. The returned pointer is cast to a pointer to the given type. If `n_structs` is 0 it returns `NULL`. Care is taken to avoid overflow when calculating the size of the allocated block.

new0

Allocates `n_structs` elements of type `struct_type`, initialized to 0’s. The returned pointer is cast to a pointer to the given type. If `n_structs` is 0 it returns `NULL`. Care is taken to avoid overflow when calculating the size of the allocated block.

newa

Wraps `g_alloca()` in a more typesafe manner.

newa0

Wraps `g_alloca0()` in a more typesafe manner.

since: 2.72

node_append

Inserts a `GNode` as the last child of the given parent.

node_append_data

Inserts a new `GNode` as the last child of the given parent.

node_first_child

Gets the first child of a `GNode`.

node_insert_data

Inserts a new `GNode` at the given position.

node_insert_data_after

Inserts a new `GNode` after the given sibling.

node_insert_data_before

Inserts a new `GNode` before the given sibling.

node_next_sibling

Gets the next sibling of a `GNode`.

node_prepend_data

Inserts a new `GNode` as the first child of the given parent.

node_prev_sibling

Gets the previous sibling of a `GNode`.

ntohl

Converts a 32-bit integer value from network to host byte order.

ntohs

Converts a 16-bit integer value from network to host byte order.

once

The first call to this routine by a process with a given `GOnce` struct calls `func` with the given argument. Thereafter, subsequent calls to `g_once()` with the same `GOnce` struct do not call `func` again, but return the stored result of the first call. On return from g_once(), the status of `once` will be `G_ONCE_STATUS_READY`.

since: 2.4

PASTE

Yields a new preprocessor pasted identifier `identifier1identifier2` from its expanded arguments `identifier1` and `identifier2`. For example, the following code:

```
#define GET(traveller,method) G_PASTE(traveller_get_, method) (traveller)
const gchar *name = GET (traveller, name);
const gchar *quest = GET (traveller, quest);
GdkColor *favourite = GET (traveller, favourite_colour);
```

since: 2.20

PASTE_ARGS

PRIVATE_INIT

A macro to assist with the static initialisation of a `GPrivate`.

since: 2.32

ptr_array_index

Returns the pointer at the given index of the pointer array.

rand_boolean

Returns a random #gboolean from `rand_`. This corresponds to an unbiased coin toss.

random_boolean

Returns a random #gboolean. This corresponds to an unbiased coin toss.

rc_box_new

A convenience macro to allocate reference counted data with the size of the given `type`.

since: 2.58

rc_box_new0

A convenience macro to allocate reference counted data with the size of the given `type`, and set its contents to zero.

since: 2.58

REC_MUTEX_AUTO_LOCK

Declare a `GRecMutexLocker` variable with `g_autoptr()` and lock the mutex. The mutex will be unlocked automatically when leaving the scope. The variable is declared with `G_GNUC_UNUSED` to avoid compiler warning if it is not used in the scope.

since: 2.80.0

renew

Reallocates the memory pointed to by `mem`, so that it now has space for `n_structs` elements of type `struct_type`. It returns the new address of the memory, which may have been moved. Care is taken to avoid overflow when calculating the size of the allocated block.

return_if_fail

return_if_reached

return_val_if_fail

return_val_if_reached

RW_LOCK_READER_AUTO_LOCK

Declare a `GRWLockReaderLocker` variable with `g_autoptr()` and lock for reading. The mutex will be unlocked automatically when leaving the scope. The variable is declared with `G_GNUC_UNUSED` to avoid compiler warning if it is not used in the scope.

since: 2.80.0

RW_LOCK_WRITER_AUTO_LOCK

Declare a `GRWLockWriterLocker` variable with `g_autoptr()` and lock for writing. The mutex will be unlocked automatically when leaving the scope. The variable is declared with `G_GNUC_UNUSED` to avoid compiler warning if it is not used in the scope.

since: 2.80.0

scanner_add_symbol

Adds a symbol to the default scope.

deprecated: 2.2

scanner_foreach_symbol

Calls a function for each symbol in the default scope.

deprecated: 2.2

scanner_freeze_symbol_table

There is no reason to use this macro, since it does nothing.

deprecated: 2.2

scanner_remove_symbol

Removes a symbol from the default scope.

deprecated: 2.2

scanner_thaw_symbol_table

There is no reason to use this macro, since it does nothing.

deprecated: 2.2

size_checked_add

Performs a checked addition of `a` and `b`, storing the result in `dest`.

since: 2.48

size_checked_mul

Performs a checked multiplication of `a` and `b`, storing the result in `dest`.

since: 2.48

SIZEOF_MEMBER

Returns the size of `member` in the struct definition without having a declared instance of `struct_type`.

since: 2.64

slice_dup

A convenience macro to duplicate a block of memory using the slice allocator.

since: 2.14

slice_free

A convenience macro to free a block of memory that has been allocated from the slice allocator.

since: 2.10

slice_free_chain

Frees a linked list of memory blocks of structure type `type`.

since: 2.10

slice_new

A convenience macro to allocate a block of memory from the slice allocator.

since: 2.10

slice_new0

A convenience macro to allocate a block of memory from the slice allocator and set the memory to 0.

since: 2.10

slist_next

A convenience macro to get the next element in a `GSList`. Note that it is considered perfectly acceptable to access `slist`->next directly.

SOURCE_FUNC

Cast a function pointer to a `GSourceFunc`, suppressing warnings from GCC 8 onwards with `-Wextra` or `-Wcast-function-type` enabled about the function types being incompatible.

since: 2.58

STATIC_ASSERT

The G_STATIC_ASSERT() macro lets the programmer check a condition at compile time, the condition needs to be compile time computable. The macro can be used in any place where a typedef is valid.

since: 2.20

STATIC_ASSERT_EXPR

The G_STATIC_ASSERT_EXPR() macro lets the programmer check a condition at compile time. The condition needs to be compile time computable.

since: 2.30

static_mutex_lock

Works like g_mutex_lock(), but for a `GStaticMutex`.

deprecated: 2.32

static_mutex_trylock

Works like g_mutex_trylock(), but for a `GStaticMutex`.

deprecated: 2.32

static_mutex_unlock

Works like g_mutex_unlock(), but for a `GStaticMutex`.

deprecated: 2.32

STRINGIFY

Accepts a macro or a string and converts it into a string after preprocessor argument expansion. For example, the following code:.

STRINGIFY_ARG

strstrip

Removes leading and trailing whitespace from a string.

STRUCT_MEMBER

Returns a member of a structure at a given offset, using the given type.

STRUCT_MEMBER_P

Returns an untyped pointer to a given offset of a struct.

STRUCT_OFFSET

Returns the offset, in bytes, of a member of a struct.

test_add

Hooks up a new test case at `testpath`.

since: 2.16

test_assert_expected_messages

Asserts that all messages previously indicated via `g_test_expect_message()` have been seen and suppressed.

since: 2.34

test_initialized

Returns true if `g_test_init()` has been called.

since: 2.36

test_perf

Returns true if tests are run in performance mode.

test_queue_unref

Enqueue an object to be released with `g_object_unref()` during the next teardown phase.

since: 2.16

test_quick

Returns true if tests are run in quick mode.

test_quiet

Returns true if tests are run in quiet mode.

test_rand_bit

Get a reproducible random bit (0 or 1).

since: 2.16

test_slow

Returns true if tests are run in slow mode.

test_thorough

Returns true if tests are run in thorough mode.

test_trap_assert_failed

Assert that the last test subprocess failed.

since: 2.16

test_trap_assert_passed

Assert that the last test subprocess passed.

since: 2.16

test_trap_assert_stderr

Assert that the stderr output of the last test subprocess matches `serrpattern`.

since: 2.16

test_trap_assert_stderr_unmatched

Assert that the stderr output of the last test subprocess does not match `serrpattern`.

since: 2.16

test_trap_assert_stdout

Assert that the stdout output of the last test subprocess matches `soutpattern`.

since: 2.16

test_trap_assert_stdout_unmatched

Assert that the stdout output of the last test subprocess does not match `soutpattern`.

since: 2.16

test_undefined

Returns true if tests may provoke assertions and other formally-undefined behaviour, to verify that appropriate warnings are given.

test_verbose

Returns true if tests are run in verbose mode.

thread_supported

This macro returns `TRUE` if the thread system is initialized, and `FALSE` if it is not.

try_new

Attempts to allocate `n_structs` elements of type `struct_type`, and returns `NULL` on failure. Contrast with g_new(), which aborts the program on failure. The returned pointer is cast to a pointer to the given type. The function returns `NULL` when `n_structs` is 0 or if an overflow occurs.

since: 2.8

try_new0

Attempts to allocate `n_structs` elements of type `struct_type`, initialized to 0’s, and returns `NULL` on failure. Contrast with g_new0(), which aborts the program on failure. The returned pointer is cast to a pointer to the given type. The function returns `NULL` when `n_structs` is 0 or if an overflow occurs.

since: 2.8

try_renew

Attempts to reallocate the memory pointed to by `mem`, so that it now has space for `n_structs` elements of type `struct_type`, and returns `NULL` on failure. Contrast with g_renew(), which aborts the program on failure. It returns the new address of the memory, which may have been moved. The function returns `NULL` if an overflow occurs.

since: 2.8

TRYLOCK

Works like g_mutex_trylock(), but for a lock defined with `G_LOCK_DEFINE`.

typeof

uint64_checked_add

Performs a checked addition of `a` and `b`, storing the result in `dest`.

since: 2.48

uint64_checked_mul

Performs a checked multiplication of `a` and `b`, storing the result in `dest`.

since: 2.48

uint_checked_add

Performs a checked addition of `a` and `b`, storing the result in `dest`.

since: 2.48

uint_checked_mul

Performs a checked multiplication of `a` and `b`, storing the result in `dest`.

since: 2.48

UNAVAILABLE

UNAVAILABLE_ENUMERATOR

UNAVAILABLE_MACRO

UNAVAILABLE_STATIC_INLINE

UNAVAILABLE_TYPE

UNLIKELY

Hints the compiler that the expression is unlikely to evaluate to a true value. The compiler may use this information for optimizations.

since: 2.2

UNLOCK

Works like g_mutex_unlock(), but for a lock defined with `G_LOCK_DEFINE`.

utf8_next_char

Skips to the next character in a UTF-8 string.

VARIANT_BUILDER_INIT

A stack-allocated `GVariantBuilder` must be initialized if it is used together with `g_auto()`. This macro can be used as initializer when declaring the builder, but it cannot be assigned to a variable.

since: 2.50

VARIANT_BUILDER_INIT_UNSET

A stack-allocated `GVariantBuilder` must be initialized if it is used together with `g_auto()`. This macro can be used as initializer when declaring the builder, but it cannot be assigned to a variable.

since: 2.84

VARIANT_DICT_INIT

A stack-allocated `GVariantDict` must be initialized if it is used together with `g_auto()` to avoid warnings or crashes if function returns before `g_variant_dict_init()` is called on the builder.

since: 2.50

warn_if_fail

Logs a warning if the expression is not true.

since: 2.16

warn_if_reached

Logs a warning.

since: 2.16

warning

A convenience function/macro to log a warning message.

warning_once

Logs a warning only once.

since: 2.64

WIN32_DLLMAIN_FOR_DLL_NAME

On Windows, this macro defines a DllMain() function that stores the actual DLL name that the code being compiled will be included in.

#### Constants

| ALLOC_AND_FREE | deprecated: 2.10 |
|---|---|
| ALLOC_ONLY | deprecated: 2.10 |
| ALLOCATOR_LIST | deprecated: 2.10 |
| ALLOCATOR_NODE | deprecated: 2.10 |
| ALLOCATOR_SLIST | deprecated: 2.10 |
| ANALYZER_ANALYZING |   |
| ASCII_DTOSTR_BUF_SIZE | A good size for a buffer to be passed into `g_ascii_dtostr()`. It is guaranteed to be enough for all output of that function on systems with 64bit IEEE-compatible doubles. |
| ATOMIC_REF_COUNT_INIT | Evaluates to the initial reference count for `gatomicrefcount`. |
| BIG_ENDIAN | Specifies one of the possible types of byte order. See `G_BYTE_ORDER`. |
| C_STD_VERSION | The C standard version the code is compiling against, it’s normally defined with the same value of `__STDC_VERSION__` for C standard compatible compilers, while it uses the lowest standard version in pure MSVC, given that in such compiler the definition depends on a compilation flag. |
| CSET_A_2_Z | The set of uppercase ASCII alphabet characters. Used for specifying valid identifier characters in `GScannerConfig`. |
| CSET_a_2_z | The set of lowercase ASCII alphabet characters. Used for specifying valid identifier characters in `GScannerConfig`. |
| CSET_DIGITS | The set of ASCII digits. Used for specifying valid identifier characters in `GScannerConfig`. |
| DATALIST_FLAGS_MASK | A bitmask that restricts the possible flags passed to g_datalist_set_flags(). Passing a flags value where flags & ~G_DATALIST_FLAGS_MASK != 0 is an error. |
| DATE_BAD_DAY | Represents an invalid `GDateDay`. |
| DATE_BAD_JULIAN | Represents an invalid Julian day number. |
| DATE_BAD_YEAR | Represents an invalid year. |
| DIR_SEPARATOR | The directory separator character. |
| DIR_SEPARATOR_S | The directory separator as a string. |
| E | The base of natural logarithms. |
| GINT16_FORMAT |   |
| GINT16_MODIFIER |   |
| GINT32_FORMAT |   |
| GINT32_MODIFIER |   |
| GINT64_FORMAT |   |
| GINT64_MODIFIER |   |
| GINTPTR_FORMAT |   |
| GINTPTR_MODIFIER |   |
| GNUC_FUNCTION | Expands to “” on all modern compilers, and to **FUNCTION** on gcc version 2.x. Don’t use it. deprecated: 2.16 |
| GNUC_PRETTY_FUNCTION | Expands to “” on all modern compilers, and to **PRETTY_FUNCTION** on gcc version 2.x. Don’t use it. deprecated: 2.16 |
| GSIZE_FORMAT |   |
| GSIZE_MODIFIER |   |
| GSSIZE_FORMAT |   |
| GSSIZE_MODIFIER |   |
| GUINT16_FORMAT |   |
| GUINT32_FORMAT |   |
| GUINT64_FORMAT |   |
| GUINTPTR_FORMAT |   |
| HAVE_GINT64 |   |
| HAVE_GNUC_VARARGS |   |
| HAVE_GNUC_VISIBILITY | Defined to 1 if gcc-style visibility handling is supported. |
| HAVE_GROWING_STACK |   |
| HAVE_ISO_VARARGS |   |
| HOOK_FLAG_USER_SHIFT | The position of the first bit which is not reserved for internal use be the `GHook` implementation, i.e. `1 << G_HOOK_FLAG_USER_SHIFT` is the first bit which can be used for application-defined flags. |
| IEEE754_DOUBLE_BIAS | The bias by which exponents in double-precision floats are offset. |
| IEEE754_FLOAT_BIAS | The bias by which exponents in single-precision floats are offset. |
| KEY_FILE_DESKTOP_GROUP | The name of the main group of a desktop entry file, as defined in the Desktop Entry Specification. |
| KEY_FILE_DESKTOP_KEY_ACTIONS | A key under `G_KEY_FILE_DESKTOP_GROUP`, whose value is a string list giving the available application actions. |
| KEY_FILE_DESKTOP_KEY_CATEGORIES | A key under `G_KEY_FILE_DESKTOP_GROUP`, whose value is a list of strings giving the categories in which the desktop entry should be shown in a menu. |
| KEY_FILE_DESKTOP_KEY_COMMENT | A key under `G_KEY_FILE_DESKTOP_GROUP`, whose value is a localized string giving the tooltip for the desktop entry. |
| KEY_FILE_DESKTOP_KEY_DBUS_ACTIVATABLE | A key under `G_KEY_FILE_DESKTOP_GROUP`, whose value is a boolean set to true if the application is D-Bus activatable. |
| KEY_FILE_DESKTOP_KEY_EXEC | A key under `G_KEY_FILE_DESKTOP_GROUP`, whose value is a string giving the command line to execute. |
| KEY_FILE_DESKTOP_KEY_GENERIC_NAME | A key under `G_KEY_FILE_DESKTOP_GROUP`, whose value is a localized string giving the generic name of the desktop entry. |
| KEY_FILE_DESKTOP_KEY_HIDDEN | A key under `G_KEY_FILE_DESKTOP_GROUP`, whose value is a boolean stating whether the desktop entry has been deleted by the user. |
| KEY_FILE_DESKTOP_KEY_ICON | A key under `G_KEY_FILE_DESKTOP_GROUP`, whose value is a localized string giving the name of the icon to be displayed for the desktop entry. |
| KEY_FILE_DESKTOP_KEY_MIME_TYPE | A key under `G_KEY_FILE_DESKTOP_GROUP`, whose value is a list of strings giving the MIME types supported by this desktop entry. |
| KEY_FILE_DESKTOP_KEY_NAME | A key under `G_KEY_FILE_DESKTOP_GROUP`, whose value is a localized string giving the specific name of the desktop entry. |
| KEY_FILE_DESKTOP_KEY_NO_DISPLAY | A key under `G_KEY_FILE_DESKTOP_GROUP`, whose value is a boolean stating whether the desktop entry should be shown in menus. |
| KEY_FILE_DESKTOP_KEY_NOT_SHOW_IN | A key under `G_KEY_FILE_DESKTOP_GROUP`, whose value is a list of strings identifying the environments that should not display the desktop entry. |
| KEY_FILE_DESKTOP_KEY_ONLY_SHOW_IN | A key under `G_KEY_FILE_DESKTOP_GROUP`, whose value is a list of strings identifying the environments that should display the desktop entry. |
| KEY_FILE_DESKTOP_KEY_PATH | A key under `G_KEY_FILE_DESKTOP_GROUP`, whose value is a string containing the working directory to run the program in. |
| KEY_FILE_DESKTOP_KEY_STARTUP_NOTIFY | A key under `G_KEY_FILE_DESKTOP_GROUP`, whose value is a boolean stating whether the application supports the Startup Notification Protocol Specification. |
| KEY_FILE_DESKTOP_KEY_STARTUP_WM_CLASS | A key under `G_KEY_FILE_DESKTOP_GROUP`, whose value is string identifying the WM class or name hint of a window that the application will create, which can be used to emulate Startup Notification with older applications. |
| KEY_FILE_DESKTOP_KEY_TERMINAL | A key under `G_KEY_FILE_DESKTOP_GROUP`, whose value is a boolean stating whether the program should be run in a terminal window. |
| KEY_FILE_DESKTOP_KEY_TRY_EXEC | A key under `G_KEY_FILE_DESKTOP_GROUP`, whose value is a string giving the file name of a binary on disk used to determine if the program is actually installed. |
| KEY_FILE_DESKTOP_KEY_TYPE | A key under `G_KEY_FILE_DESKTOP_GROUP`, whose value is a string giving the type of the desktop entry. |
| KEY_FILE_DESKTOP_KEY_URL | A key under `G_KEY_FILE_DESKTOP_GROUP`, whose value is a string giving the URL to access. |
| KEY_FILE_DESKTOP_KEY_VERSION | A key under `G_KEY_FILE_DESKTOP_GROUP`, whose value is a string giving the version of the Desktop Entry Specification used for the desktop entry file. |
| KEY_FILE_DESKTOP_TYPE_APPLICATION | The value of the `G_KEY_FILE_DESKTOP_KEY_TYPE`, key for desktop entries representing applications. |
| KEY_FILE_DESKTOP_TYPE_DIRECTORY | The value of the `G_KEY_FILE_DESKTOP_KEY_TYPE`, key for desktop entries representing directories. |
| KEY_FILE_DESKTOP_TYPE_LINK | The value of the `G_KEY_FILE_DESKTOP_KEY_TYPE`, key for desktop entries representing links to documents. |
| LITTLE_ENDIAN | Specifies one of the possible types of byte order. See `G_BYTE_ORDER`. |
| LN10 | The natural logarithm of 10. |
| LN2 | The natural logarithm of 2. |
| LOG_2_BASE_10 | Multiplying the base 2 exponent by this number yields the base 10 exponent. |
| LOG_DOMAIN | Defines the log domain. See Log Domains. |
| LOG_FATAL_MASK | GLib log levels that are considered fatal by default. |
| LOG_LEVEL_USER_SHIFT | Log levels below `1< |
| MAJOR_VERSION | The major version number of the GLib library. |
| MAXINT16 |   |
| MAXINT32 |   |
| MAXINT64 |   |
| MAXINT8 |   |
| MAXUINT16 |   |
| MAXUINT32 |   |
| MAXUINT64 |   |
| MAXUINT8 |   |
| MICRO_VERSION | The micro version number of the GLib library. |
| MININT16 | The minimum value which can be held in a #gint16. |
| MININT32 | The minimum value which can be held in a #gint32. |
| MININT64 | The minimum value which can be held in a #gint64. |
| MININT8 | The minimum value which can be held in a #gint8. |
| MINOR_VERSION | The minor version number of the GLib library. |
| MODULE_SUFFIX |   |
| NSEC_PER_SEC | Number of nanoseconds in one second (1 billion). This macro is provided for code readability. |
| OPTION_REMAINING | If a long option in the main group has this name, it is not treated as a regular option. Instead it collects all non-option arguments which would otherwise be left in `argv`. The option must be of type `G_OPTION_ARG_CALLBACK`, `G_OPTION_ARG_STRING_ARRAY` or `G_OPTION_ARG_FILENAME_ARRAY`. |
| PDP_ENDIAN | Specifies one of the possible types of byte order (currently unused). See `G_BYTE_ORDER`. |
| PI | The value of pi (ratio of circle’s circumference to its diameter). |
| PI_2 | Pi divided by 2. |
| PI_4 | Pi divided by 4. |
| PID_FORMAT | A format specifier that can be used in printf()-style format strings when printing a `GPid`. |
| POLLFD_FORMAT | A format specifier that can be used in printf()-style format strings when printing the `fd` member of a `GPollFD`. |
| PRIORITY_DEFAULT | Use this for default priority event sources. |
| PRIORITY_DEFAULT_IDLE | Use this for default priority idle functions. |
| PRIORITY_HIGH | Use this for high priority event sources. |
| PRIORITY_HIGH_IDLE | Use this for high priority idle functions. |
| PRIORITY_LOW | Use this for very low priority background tasks. |
| REF_COUNT_INIT | Evaluates to the initial reference count for `grefcount`. |
| SEARCHPATH_SEPARATOR | The search path separator character. This is ‘:’ on UNIX machines and ‘;’ under Windows. |
| SEARCHPATH_SEPARATOR_S | The search path separator as a string. This is “:” on UNIX machines and “;” under Windows. |
| SIZEOF_LONG |   |
| SIZEOF_SIZE_T |   |
| SIZEOF_SSIZE_T |   |
| SIZEOF_VOID_P |   |
| SOURCE_CONTINUE | Use this macro as the return value of a `GSourceFunc` to leave the `GSource` in the main loop. |
| SOURCE_REMOVE | Use this macro as the return value of a `GSourceFunc` to remove the `GSource` from the main loop. |
| SQRT2 | The square root of two. |
| STR_DELIMITERS | The standard delimiters, used in `g_strdelimit()`. |
| SYSDEF_AF_INET |   |
| SYSDEF_AF_INET6 |   |
| SYSDEF_AF_UNIX |   |
| SYSDEF_MSG_DONTROUTE |   |
| SYSDEF_MSG_OOB |   |
| SYSDEF_MSG_PEEK |   |
| TEST_OPTION_ISOLATE_DIRS | A value that can be passed as an option to `g_test_init()`. |
| TEST_OPTION_NO_PRGNAME | A value that can be passed as an option to `g_test_init()`. |
| TEST_OPTION_NONFATAL_ASSERTIONS | A value that can be passed as an option to `g_test_init()`. |
| TIME_SPAN_DAY | Evaluates to a time span of one day. |
| TIME_SPAN_HOUR | Evaluates to a time span of one hour. |
| TIME_SPAN_MILLISECOND | Evaluates to a time span of one millisecond. |
| TIME_SPAN_MINUTE | Evaluates to a time span of one minute. |
| TIME_SPAN_SECOND | Evaluates to a time span of one second. |
| UNICHAR_MAX_DECOMPOSITION_LENGTH | The maximum length (in codepoints) of a compatibility or canonical decomposition of a single Unicode character. |
| URI_RESERVED_CHARS_GENERIC_DELIMITERS | Generic delimiters characters as defined in RFC 3986. Includes `:/?#[]@`. |
| URI_RESERVED_CHARS_SUBCOMPONENT_DELIMITERS | Subcomponent delimiter characters as defined in RFC 3986. Includes `!$&'()*+,;=`. |
| USEC_PER_SEC | Number of microseconds in one second (1 million). This macro is provided for code readability. |
| VA_COPY_AS_ARRAY |   |
| VERSION_MIN_REQUIRED | A macro that should be defined by the user prior to including the glib.h header. The definition should be one of the predefined GLib version macros: `GLIB_VERSION_2_26`, `GLIB_VERSION_2_28`,… |
| WIN32_MSG_HANDLE |   |
