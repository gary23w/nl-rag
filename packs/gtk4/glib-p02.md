---
title: "GLib (part 2/3)"
source: https://docs.gtk.org/glib/
domain: gtk4
license: CC-BY-SA-4.0
tags: gtk4 toolkit, gtk widgets, gnome application, libadwaita styling
fetched: 2026-07-02
part: 2/3
---

# GLib

str_equal

Compares two strings for byte-by-byte equality and returns `TRUE` if they are equal. It can be passed to `g_hash_table_new()` as the `key_equal_func` parameter, when using non-`NULL` strings as keys in a `GHashTable`.

str_has_prefix

Looks whether the string `str` begins with `prefix`.

since: 2.2

str_has_suffix

Looks whether a string ends with `suffix`.

since: 2.2

str_hash

Converts a string to a hash value.

str_is_ascii

Determines if a string is pure ASCII. A string is pure ASCII if it contains no bytes with the high bit set.

since: 2.40

str_match_string

Checks if a search conducted for `search_term` should match `potential_hit`.

since: 2.40

str_to_ascii

Transliterate `str` to plain ASCII.

since: 2.40

str_tokenize_and_fold

Tokenizes `string` and performs folding on each token.

since: 2.40

strcanon

For each character in `string`, if the character is not in `valid_chars`, replaces the character with `substitutor`.

strcasecmp

A case-insensitive string comparison, corresponding to the standard `strcasecmp()` function on platforms which support it.

deprecated: 2.2

strchomp

Removes trailing whitespace from a string.

strchug

Removes leading whitespace from a string, by moving the rest of the characters forward.

strcmp0

Compares `str1` and `str2` like `strcmp()`.

since: 2.16

strcompress

Makes a copy of a string replacing C string-style escape sequences with their one byte equivalent:.

strconcat

Concatenates all of the given strings into one long string.

strdelimit

Converts any delimiter characters in `string` to `new_delimiter`.

strdown

Converts a string to lower case.

deprecated: 2.2

strdup

Duplicates a string. If `str` is `NULL` it returns `NULL`.

strdup_printf

Similar to the standard C `sprintf()` function but safer, since it calculates the maximum space required and allocates memory to hold the result.

strdup_vprintf

Similar to the standard C `vsprintf()` function but safer, since it calculates the maximum space required and allocates memory to hold the result.

strdupv

Copies an array of strings. The copy is a deep copy; each string is also copied.

strerror

Returns a string corresponding to the given error code, e.g. “no such process”.

strescape

It replaces the following special characters in the string `source` with their corresponding C escape sequence:.

strfreev

Frees an array of strings, as well as each string it contains.

strip_context

An auxiliary function for `gettext()` support (see Q_()).

since: 2.4

strjoin

Joins a number of strings together to form one long string, with the optional `separator` inserted between each of them.

strjoinv

Joins an array of strings together to form one long string, with the optional `separator` inserted between each of them.

strlcat

Portability wrapper that calls `strlcat()` on systems which have it, and emulates it otherwise. Appends nul-terminated `src` string to `dest`, guaranteeing nul-termination for `dest`. The total size of `dest` won’t exceed `dest_size`.

strlcpy

Portability wrapper that calls `strlcpy()` on systems which have it, and emulates `strlcpy()` otherwise. Copies `src` to `dest`; `dest` is guaranteed to be nul-terminated; `src` must be nul-terminated; `dest_size` is the buffer size, not the number of bytes to copy.

strncasecmp

A case-insensitive string comparison, corresponding to the standard `strncasecmp()` function on platforms which support it. It is similar to `g_strcasecmp()` except it only compares the first `n` characters of the strings.

deprecated: 2.2

strndup

Duplicates the first `n` bytes of a string, returning a newly-allocated buffer `n` + 1 bytes long which will always be nul-terminated. If `str` is less than `n` bytes long the buffer is padded with nuls. If `str` is `NULL` it returns `NULL`.

strnfill

Creates a new string `length` bytes long filled with `fill_char`.

strreverse

Reverses all of the bytes in a string. For example, `g_strreverse ("abcdef")` will result in “fedcba”.

strrstr

Searches the string `haystack` for the last occurrence of the string `needle`.

strrstr_len

Searches the string `haystack` for the last occurrence of the string `needle`, limiting the length of the search to `haystack_len`.

strsignal

Returns a string describing the given signal, e.g. “Segmentation fault”. If the signal is unknown, it returns “unknown signal (<signum>)”.

strsplit

Splits a string into a maximum of `max_tokens` pieces, using the given `delimiter`. If `max_tokens` is reached, the remainder of `string` is appended to the last token.

strsplit_set

Splits `string` into a number of tokens not containing any of the bytes in `delimiters`.

since: 2.4

strstr_len

Searches the string `haystack` for the first occurrence of the string `needle`, limiting the length of the search to `haystack_len` or a nul terminator byte (whichever is reached first).

strtod

Converts a string to a floating point value.

strup

Converts a string to upper case.

deprecated: 2.2

strv_contains

Checks if an array of strings contains the string `str` according to `g_str_equal()`. `strv` must not be `NULL`.

since: 2.44

strv_equal

Checks if two arrays of strings contain exactly the same elements in exactly the same order.

since: 2.60

strv_get_type

strv_length

Returns the length of an array of strings. `str_array` must not be `NULL`.

since: 2.6

test_add_data_func

Creates a new test case.

since: 2.16

test_add_data_func_full

Creates a new test case.

since: 2.34

test_add_func

Creates a new test case.

since: 2.16

test_add_vtable

test_bug

Adds a message to test reports that associates a bug URI with a test case.

since: 2.16

test_bug_base

Specifies the base URI for bug reports.

since: 2.16

test_build_filename

Creates the pathname to a data file that is required for a test.

since: 2.38

test_create_case

Creates a new `GTestCase`.

since: 2.16

test_create_suite

Creates a new test suite with the name `suite_name`.

since: 2.16

test_disable_crash_reporting

Attempts to disable system crash reporting infrastructure.

since: 2.78

test_expect_message

Indicates that a message with the given `log_domain` and `log_level`, with text matching `pattern`, is expected to be logged.

since: 2.34

test_fail

Indicates that a test failed.

since: 2.30

test_fail_printf

Indicates that a test failed and records a message.

since: 2.70

test_failed

Returns whether a test has already failed.

since: 2.38

test_get_dir

Gets the pathname of the directory containing test files of the type specified by `file_type`.

since: 2.38

test_get_filename

Gets the pathname to a data file that is required for a test.

since: 2.38

test_get_path

Gets the test path for the test currently being run.

since: 2.68

test_get_root

Gets the toplevel test suite for the test path API.

since: 2.16

test_incomplete

Indicates that a test failed because of some incomplete functionality.

since: 2.38

test_incomplete_printf

Indicates that a test failed because of some incomplete functionality.

since: 2.70

test_init

Initializes the GLib testing framework.

since: 2.16

test_log_set_fatal_handler

Installs a non-error fatal log handler which can be used to decide whether log messages which are counted as fatal abort the program.

since: 2.22

test_log_type_name

test_maximized_result

Reports the result of a performance or measurement test.

since: 2.16

test_message

Adds a message to the test report.

since: 2.16

test_minimized_result

Reports the result of a performance or measurement test.

since: 2.16

test_queue_destroy

Enqueues a callback `destroy_func` to be executed during the next test case teardown phase.

since: 2.16

test_queue_free

Enqueues a pointer to be released with `g_free()` during the next teardown phase.

since: 2.16

test_rand_double

Gets a reproducible random floating point number.

since: 2.16

test_rand_double_range

Gets a reproducible random floating point number out of a specified range.

since: 2.16

test_rand_int

Gets a reproducible random integer number.

since: 2.16

test_rand_int_range

Gets a reproducible random integer number out of a specified range.

since: 2.16

test_run

Runs all tests under the toplevel suite.

since: 2.16

test_run_suite

Executes the tests within `suite` and all nested test suites.

since: 2.16

test_set_nonfatal_assertions

Changes the behaviour of the various assertion macros.

since: 2.38

test_skip

Indicates that a test was skipped.

since: 2.38

test_skip_printf

Indicates that a test was skipped.

since: 2.70

test_subprocess

Returns true if the test program is running under `g_test_trap_subprocess()`.

since: 2.38

test_summary

Sets the summary for a test.

since: 2.62

test_timer_elapsed

Gets the number of seconds since the last start of the timer with `g_test_timer_start()`.

since: 2.16

test_timer_last

Reports the last result of `g_test_timer_elapsed()`.

since: 2.16

test_timer_start

Starts a timing test.

since: 2.16

test_trap_assertions

test_trap_fork

Forks the current test program to execute a test case that might not return or that might abort.

deprecated: Unknown since: 2.16

test_trap_has_passed

Checks the result of the last `g_test_trap_subprocess()` call.

since: 2.16

test_trap_has_skipped

Checks the result of the last `g_test_trap_subprocess()` call.

since: 2.88

test_trap_reached_timeout

Checks the result of the last `g_test_trap_subprocess()` call.

since: 2.16

test_trap_subprocess

Respawns the test program to run only `test_path` in a subprocess.

since: 2.38

test_trap_subprocess_with_envp

Respawns the test program to run only `test_path` in a subprocess with a given environment.

since: 2.80

timeout_add

Sets a function to be called at regular intervals, with the default priority, `G_PRIORITY_DEFAULT`.

timeout_add_full

Sets a function to be called at regular intervals, with the given priority.

timeout_add_once

Sets a function to be called after `interval` milliseconds have elapsed, with the default priority, `G_PRIORITY_DEFAULT`.

since: 2.74

timeout_add_seconds

Sets a function to be called at regular intervals with the default priority, `G_PRIORITY_DEFAULT`.

since: 2.14

timeout_add_seconds_full

Sets a function to be called at regular intervals, with `priority`.

since: 2.14

timeout_add_seconds_once

This function behaves like `g_timeout_add_once()` but with a range in seconds.

since: 2.78

timeout_source_new

Creates a new timeout source.

timeout_source_new_seconds

Creates a new timeout source.

since: 2.14

try_malloc

Attempts to allocate `n_bytes`, and returns `NULL` on failure. Contrast with g_malloc(), which aborts the program on failure.

try_malloc0

Attempts to allocate `n_bytes`, initialized to 0’s, and returns `NULL` on failure. Contrast with g_malloc0(), which aborts the program on failure.

since: 2.8

try_malloc0_n

This function is similar to g_try_malloc0(), allocating (`n_blocks` * `n_block_bytes`) bytes, but care is taken to detect possible overflow during multiplication.

since: 2.24

try_malloc_n

This function is similar to g_try_malloc(), allocating (`n_blocks` * `n_block_bytes`) bytes, but care is taken to detect possible overflow during multiplication.

since: 2.24

try_realloc

Attempts to realloc `mem` to a new size, `n_bytes`, and returns `NULL` on failure. Contrast with g_realloc(), which aborts the program on failure.

try_realloc_n

This function is similar to g_try_realloc(), allocating (`n_blocks` * `n_block_bytes`) bytes, but care is taken to detect possible overflow during multiplication.

since: 2.24

ucs4_to_utf16

Convert a string from UCS-4 to UTF-16.

ucs4_to_utf8

Convert a string from a 32-bit fixed width representation as UCS-4. to UTF-8.

unichar_break_type

Determines the break type of `c`. `c` should be a Unicode character (to derive a character from UTF-8 encoded text, use g_utf8_get_char()). The break type is used to find word and line breaks (“text boundaries”), Pango implements the Unicode boundary resolution algorithms and normally you would use a function such as `pango_break()` instead of caring about break types yourself.

unichar_combining_class

Determines the canonical combining class of a Unicode character.

since: 2.14

unichar_compose

Performs a single composition step of the Unicode canonical composition algorithm.

since: 2.30

unichar_decompose

Performs a single decomposition step of the Unicode canonical decomposition algorithm.

since: 2.30

unichar_digit_value

Determines the numeric value of a character as a decimal digit.

unichar_fully_decompose

Computes the canonical or compatibility decomposition of a Unicode character. For compatibility decomposition, pass `TRUE` for `compat`; for canonical decomposition pass `FALSE` for `compat`.

since: 2.30

unichar_get_mirror_char

In Unicode, some characters are “mirrored”. This means that their images are mirrored horizontally in text that is laid out from right to left. For instance, “(” would become its mirror image, “)”, in right-to-left text.

since: 2.4

unichar_get_script

Looks up the `GUnicodeScript` for a particular character (as defined by Unicode Standard Annex #24). No check is made for `ch` being a valid Unicode character; if you pass in invalid character, the result is undefined.

since: 2.14

unichar_isalnum

Determines whether a character is alphanumeric. Given some UTF-8 text, obtain a character value with g_utf8_get_char().

unichar_isalpha

Determines whether a character is alphabetic (i.e. a letter). Given some UTF-8 text, obtain a character value with g_utf8_get_char().

unichar_iscntrl

Determines whether a character is a control character. Given some UTF-8 text, obtain a character value with g_utf8_get_char().

unichar_isdefined

Determines if a given character is assigned in the Unicode standard.

unichar_isdigit

Determines whether a character is numeric (i.e. a digit). This covers ASCII 0-9 and also digits in other languages/scripts. Given some UTF-8 text, obtain a character value with g_utf8_get_char().

unichar_isgraph

Determines whether a character is printable and not a space (returns `FALSE` for control characters, format characters, and spaces). `g_unichar_isprint()` is similar, but returns `TRUE` for spaces. Given some UTF-8 text, obtain a character value with g_utf8_get_char().

unichar_islower

Determines whether a character is a lowercase letter. Given some UTF-8 text, obtain a character value with g_utf8_get_char().

unichar_ismark

Determines whether a character is a mark (non-spacing mark, combining mark, or enclosing mark in Unicode speak). Given some UTF-8 text, obtain a character value with g_utf8_get_char().

since: 2.14

unichar_isprint

Determines whether a character is printable. Unlike g_unichar_isgraph(), returns `TRUE` for spaces. Given some UTF-8 text, obtain a character value with g_utf8_get_char().

unichar_ispunct

Determines whether a character is punctuation or a symbol. Given some UTF-8 text, obtain a character value with g_utf8_get_char().

unichar_isspace

Determines whether a character is a space, tab, or line separator (newline, carriage return, etc.). Given some UTF-8 text, obtain a character value with g_utf8_get_char().

unichar_istitle

Determines if a character is titlecase. Some characters in Unicode which are composites, such as the DZ digraph have three case variants instead of just two. The titlecase form is used at the beginning of a word where only the first letter is capitalized. The titlecase form of the DZ digraph is U+01F2 LATIN CAPITAL LETTTER D WITH SMALL LETTER Z.

unichar_isupper

Determines if a character is uppercase.

unichar_iswide

Determines if a character is typically rendered in a double-width cell.

unichar_iswide_cjk

Determines if a character is typically rendered in a double-width cell under legacy East Asian locales. If a character is wide according to g_unichar_iswide(), then it is also reported wide with this function, but the converse is not necessarily true. See the Unicode Standard Annex #11 for details.

since: 2.12

unichar_isxdigit

Determines if a character is a hexadecimal digit.

unichar_iszerowidth

Determines if a given character typically takes zero width when rendered. The return value is `TRUE` for all non-spacing and enclosing marks (e.g., combining accents), format characters, zero-width space, but not U+00AD SOFT HYPHEN.

since: 2.14

unichar_to_utf8

Converts a single character to UTF-8.

unichar_tolower

Converts a character to lower case.

unichar_totitle

Converts a character to the titlecase.

unichar_toupper

Converts a character to uppercase.

unichar_type

Classifies a Unicode character by type.

unichar_validate

Checks whether `ch` is a valid Unicode character.

unichar_xdigit_value

Determines the numeric value of a character as a hexadecimal digit.

unicode_canonical_decomposition

Computes the canonical decomposition of a Unicode character.

deprecated: 2.30

unicode_canonical_ordering

Computes the canonical ordering of a string in-place. This rearranges decomposed characters in the string according to their combining classes. See the Unicode manual for more information.

unlink

A wrapper for the POSIX `unlink()` function. The `unlink()` function deletes a name from the filesystem. If this was the last link to the file and no processes have it opened, the diskspace occupied by the file is freed.

since: 2.6

unsetenv

Removes an environment variable from the environment.

since: 2.4

usleep

Pauses the current thread for the given number of microseconds.

utf16_to_ucs4

Convert a string from UTF-16 to UCS-4.

utf16_to_utf8

Convert a string from UTF-16 to UTF-8.

utf8_casefold

Converts a string into a form that is independent of case. The result will not correspond to any particular case, but can be compared for equality or ordered with the results of calling `g_utf8_casefold()` on other strings.

utf8_collate

Compares two strings for ordering using the linguistically correct rules for the current locale. When sorting a large number of strings, it will be significantly faster to obtain collation keys with `g_utf8_collate_key()` and compare the keys with `strcmp()` when sorting instead of sorting the original strings.

utf8_collate_key

Converts a string into a collation key that can be compared with other collation keys produced by the same function using strcmp().

utf8_collate_key_for_filename

Converts a string into a collation key that can be compared with other collation keys produced by the same function using strcmp().

since: 2.8

utf8_find_next_char

Finds the start of the next UTF-8 character in the string after `p`.

utf8_find_prev_char

Given a position `p` with a UTF-8 encoded string `str`, find the start of the previous UTF-8 character starting before `p`. Returns `NULL` if no UTF-8 characters are present in `str` before `p`.

utf8_get_char

Converts a sequence of bytes encoded as UTF-8 to a Unicode character.

utf8_get_char_validated

Convert a sequence of bytes encoded as UTF-8 to a Unicode character.

utf8_make_valid

If the provided string is valid UTF-8, return a copy of it. If not, return a copy in which bytes that could not be interpreted as valid Unicode are replaced with the Unicode replacement character (U+FFFD).

since: 2.52

utf8_normalize

Converts a string into canonical form, standardizing such issues as whether a character with an accent is represented as a base character and combining accent or as a single precomposed character. The string has to be valid UTF-8, otherwise `NULL` is returned. You should generally call `g_utf8_normalize()` before comparing two Unicode strings.

utf8_offset_to_pointer

Converts from an integer character offset to a pointer to a position within the string.

utf8_pointer_to_offset

Converts from a pointer to position within a string to an integer character offset.

utf8_prev_char

Finds the previous UTF-8 character in the string before `p`.

utf8_strchr

Finds the leftmost occurrence of the given Unicode character in a UTF-8 encoded string, while limiting the search to `len` bytes.

utf8_strdown

Converts all Unicode characters in the string that have a case to lowercase. The exact manner that this is done depends on the current locale, and may result in the number of characters in the string changing.

utf8_strlen

Computes the length of the string in characters, not including the terminating nul character. If the `max`’th byte falls in the middle of a character, the last (partial) character is not counted.

utf8_strncpy

Like the standard C `strncpy()` function, but copies a given number of characters instead of a given number of bytes.

utf8_strrchr

Find the rightmost occurrence of the given Unicode character in a UTF-8 encoded string, while limiting the search to `len` bytes.

utf8_strreverse

Reverses a UTF-8 string.

since: 2.2

utf8_strup

Converts all Unicode characters in the string that have a case to uppercase. The exact manner that this is done depends on the current locale, and may result in the number of characters in the string increasing. (For instance, the German ess-zet will be changed to SS.).

utf8_substring

Copies a substring out of a UTF-8 encoded string. The substring will contain `end_pos` - `start_pos` characters.

since: 2.30

utf8_to_ucs4

Convert a string from UTF-8 to a 32-bit fixed width representation as UCS-4.

utf8_to_ucs4_fast

Convert a string from UTF-8 to a 32-bit fixed width representation as UCS-4, assuming valid UTF-8 input.

utf8_to_utf16

Convert a string from UTF-8 to UTF-16.

utf8_truncate_middle

Cuts off the middle of the string, preserving half of `truncate_length` characters at the beginning and half at the end.

since: 2.78

utf8_validate

Validates UTF-8 encoded text.

utf8_validate_len

Validates UTF-8 encoded text.

since: 2.60

utime

A wrapper for the POSIX `utime()` function. The `utime()` function sets the access and modification timestamps of a file.

since: 2.18

uuid_string_is_valid

Parses the string `str` and verify if it is a UUID.

since: 2.52

uuid_string_random

Generates a random UUID (RFC 4122 version 4) as a string. It has the same randomness guarantees as `GRand`, so must not be used for cryptographic purposes such as key generation, nonces, salts or one-time pads.

since: 2.52

variant_get_gtype

vasprintf

An implementation of the GNU `vasprintf()` function which supports positional parameters, as specified in the Single Unix Specification. This function is similar to `g_vsprintf()`, except that it allocates a string to hold the output, instead of putting the output in a buffer you allocate in advance.

since: 2.4

vfprintf

An implementation of the standard `fprintf()` function which supports positional parameters, as specified in the Single Unix Specification.

since: 2.2

vprintf

An implementation of the standard `vprintf()` function which supports positional parameters, as specified in the Single Unix Specification.

since: 2.2

vsnprintf

A safer form of the standard `vsprintf()` function. The output is guaranteed to not exceed `n` characters (including the terminating nul character), so it is easy to ensure that a buffer overflow cannot occur.

vsprintf

An implementation of the standard `vsprintf()` function which supports positional parameters, as specified in the Single Unix Specification.

since: 2.2

warn_message

Internal function used to print messages from the public `g_warn_if_reached()` and `g_warn_if_fail()` macros.

#### Function Macros

abort

A wrapper for the POSIX `abort()` function.

since: 2.50

ALIGNOF

Return the minimal alignment required by the platform ABI for values of the given type. The address of a variable or struct member of the given type must always be a multiple of this alignment. For example, most platforms require int variables to be aligned at a 4-byte boundary, so `G_ALIGNOF (int)` is 4 on most platforms.

since: 2.60

alloca

Allocates `size` bytes on the stack; these bytes will be freed when the current stack frame is cleaned up. This macro essentially just wraps the `alloca()` function present on most UNIX variants. Thus it provides the same advantages and pitfalls as alloca():.

alloca0

Wraps `g_alloca()` and initializes allocated memory to zeroes. If `size` is `0` it returns `NULL`.

since: 2.72

APPROX_VALUE

Evaluates to a truth value if the absolute difference between `a` and `b` is smaller than `epsilon`, and to a false value otherwise.

since: 2.58

array_append_val

Adds the value on to the end of the array. The array will grow in size automatically if necessary.

array_index

Returns the element of a `GArray` at the given index. The return value is cast to the given type. This is the main way to read or write an element in a `GArray`.

array_insert_val

Inserts an element into an array at the given index.

array_prepend_val

Adds the value on to the start of the array. The array will grow in size automatically if necessary.

ascii_isalnum

Determines whether a character is alphanumeric.

ascii_isalpha

Determines whether a character is alphabetic (i.e. a letter).

ascii_iscntrl

Determines whether a character is a control character.

ascii_isdigit
