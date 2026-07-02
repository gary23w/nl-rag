---
title: "Autoconf (part 11/26)"
source: https://www.gnu.org/software/autoconf/manual/autoconf.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 11/26
---

# Autoconf

**Macro: **m4_for***(*var*, *first*, *last*, [*step*], *expression*)* ¶**

Loop over the numeric values between *first* and *last* including bounds by increments of *step*. For each iteration, expand *expression* with the numeric value assigned to *var*. If *step* is omitted, it defaults to ‘1’ or ‘-1’ depending on the order of the limits. If given, *step* has to match this order. The number of iterations is determined independently from definition of *var*; iteration cannot be short-circuited or lengthened by modifying *var* from within *expression*.

**Macro: **m4_foreach***(*var*, *list*, *expression*)* ¶**

Loop over the comma-separated M4 list *list*, assigning each value to *var*, and expand *expression*. The following example outputs two lines:

```
m4_foreach([myvar], [[foo], [bar, baz]],
           [echo myvar
])dnl
⇒echo foo
⇒echo bar, baz
```

Note that for some forms of *expression*, it may be faster to use `m4_map_args`.

**Macro: **m4_foreach_w***(*var*, *list*, *expression*)* ¶**

Loop over the white-space-separated list *list*, assigning each value to *var*, and expand *expression*. If *var* is only referenced once in *expression*, it is more efficient to use `m4_map_args_w`.

The deprecated macro `AC_FOREACH` is an alias of `m4_foreach_w`.

**Macro: **m4_map***(*macro*, *list*)* ¶**

**Macro: **m4_mapall***(*macro*, *list*)* ¶**

**Macro: **m4_map_sep***(*macro*, *separator*, *list*)* ¶**

**Macro: **m4_mapall_sep***(*macro*, *separator*, *list*)* ¶**

Loop over the comma separated quoted list of argument descriptions in *list*, and invoke *macro* with the arguments. An argument description is in turn a comma-separated quoted list of quoted elements, suitable for `m4_apply`. The macros `m4_map` and `m4_map_sep` ignore empty argument descriptions, while `m4_mapall` and `m4_mapall_sep` invoke *macro* with no arguments. The macros `m4_map_sep` and `m4_mapall_sep` additionally expand *separator* between invocations of *macro*.

Note that *separator* is expanded, unlike in `m4_join`. When separating output with commas, this means that the map result can be used as a series of arguments, by using a single-quoted comma as *separator*, or as a single string, by using a double-quoted comma.

```
m4_map([m4_count], [])
⇒
m4_map([ m4_count], [[],
                     [[1]],
                     [[1], [2]]])
⇒ 1 2
m4_mapall([ m4_count], [[],
                        [[1]],
                        [[1], [2]]])
⇒ 0 1 2
m4_map_sep([m4_eval], [,], [[[1+2]],
                            [[10], [16]]])
⇒3,a
m4_map_sep([m4_echo], [,], [[[a]], [[b]]])
⇒a,b
m4_count(m4_map_sep([m4_echo], [,], [[[a]], [[b]]]))
⇒2
m4_map_sep([m4_echo], [[,]], [[[a]], [[b]]])
⇒a,b
m4_count(m4_map_sep([m4_echo], [[,]], [[[a]], [[b]]]))
⇒1
```

**Macro: **m4_map_args***(*macro*, *arg*…)* ¶**

Repeatedly invoke *macro* with each successive *arg* as its only argument. In the following example, three solutions are presented with the same expansion; the solution using `m4_map_args` is the most efficient.

```
m4_define([active], [ACTIVE])dnl
m4_foreach([var], [[plain], [active]], [ m4_echo(m4_defn([var]))])
⇒ plain active
m4_map([ m4_echo], [[[plain]], [[active]]])
⇒ plain active
m4_map_args([ m4_echo], [plain], [active])
⇒ plain active
```

In cases where it is useful to operate on additional parameters besides the list elements, the macro `m4_curry` can be used in *macro* to supply the argument currying necessary to generate the desired argument list. In the following example, `list_add_n` is more efficient than `list_add_x`. On the other hand, using `m4_map_args_sep` can be even more efficient.

```
m4_define([list], [[1], [2], [3]])dnl
m4_define([add], [m4_eval(([$1]) + ([$2]))])dnl
dnl list_add_n(N, ARG...)
dnl Output a list consisting of each ARG added to N
m4_define([list_add_n],
[m4_shift(m4_map_args([,m4_curry([add], [$1])], m4_shift($@)))])dnl
list_add_n([1], list)
⇒2,3,4
list_add_n([2], list)
⇒3,4,5
m4_define([list_add_x],
[m4_shift(m4_foreach([var], m4_dquote(m4_shift($@)),
  [,add([$1],m4_defn([var]))]))])dnl
list_add_x([1], list)
⇒2,3,4
```

**Macro: **m4_map_args_pair***(*macro*, [*macro-end* = *macro*], *arg*…)* ¶**

For every pair of arguments *arg*, invoke *macro* with two arguments. If there is an odd number of arguments, invoke *macro-end*, which defaults to *macro*, with the remaining argument.

```
m4_map_args_pair([, m4_reverse], [], [1], [2], [3])
⇒, 2, 1, 3
m4_map_args_pair([, m4_reverse], [, m4_dquote], [1], [2], [3])
⇒, 2, 1, [3]
m4_map_args_pair([, m4_reverse], [, m4_dquote], [1], [2], [3], [4])
⇒, 2, 1, 4, 3
```

**Macro: **m4_map_args_sep***([*pre*], [*post*], [*sep*], *arg*…)* ¶**

Expand the sequence `*pre*[*arg*]*post*` for each argument, additionally expanding *sep* between arguments. One common use of this macro is constructing a macro call, where the opening and closing parentheses are split between *pre* and *post*; in particular, `m4_map_args([*macro*], [*arg*])` is equivalent to `m4_map_args_sep([*macro*(], [)], [], [*arg*])`. This macro provides the most efficient means for iterating over an arbitrary list of arguments, particularly when repeatedly constructing a macro call with more arguments than *arg*.

**Macro: **m4_map_args_w***(*string*, [*pre*], [*post*], [*sep*])* ¶**

Expand the sequence `*pre*[word]*post*` for each word in the whitespace-separated *string*, additionally expanding *sep* between words. This macro provides the most efficient means for iterating over a whitespace-separated string. In particular, `m4_map_args_w([*string*], [*action*(], [)])` is more efficient than `m4_foreach_w([var], [*string*], [*action*(m4_defn([var]))])`.

**Macro: **m4_shiftn***(*count*, …)* ¶**

**Macro: **m4_shift2***(…)* ¶**

**Macro: **m4_shift3***(…)* ¶**

`m4_shiftn` performs *count* iterations of `m4_shift`, along with validation that enough arguments were passed in to match the shift count, and that the count is positive. `m4_shift2` and `m4_shift3` are specializations of `m4_shiftn`, introduced in Autoconf 2.62, and are more efficient for two and three shifts, respectively.

**Macro: **m4_stack_foreach***(*macro*, *action*)* ¶**

**Macro: **m4_stack_foreach_lifo***(*macro*, *action*)* ¶**

For each of the `m4_pushdef` definitions of *macro*, expand *action* with the single argument of a definition of *macro*. `m4_stack_foreach` starts with the oldest definition, while `m4_stack_foreach_lifo` starts with the current definition. *action* should not push or pop definitions of *macro*, nor is there any guarantee that the current definition of *macro* matches the argument that was passed to *action*. The macro `m4_curry` can be used if *action* needs more than one argument, although in that case it is more efficient to use *m4_stack_foreach_sep*.

Due to technical limitations, there are a few low-level m4sugar functions, such as `m4_pushdef`, that cannot be used as the *macro* argument.

```
m4_pushdef([a], [1])m4_pushdef([a], [2])dnl
m4_stack_foreach([a], [ m4_incr])
⇒ 2 3
m4_stack_foreach_lifo([a], [ m4_curry([m4_substr], [abcd])])
⇒ cd bcd
```

**Macro: **m4_stack_foreach_sep***(*macro*, [*pre*], [*post*], [*sep*])* ¶**

**Macro: **m4_stack_foreach_sep_lifo***(*macro*, [*pre*], [*post*], [*sep*])* ¶**

Expand the sequence `*pre*[definition]*post*` for each `m4_pushdef` definition of *macro*, additionally expanding *sep* between definitions. `m4_stack_foreach_sep` visits the oldest definition first, while `m4_stack_foreach_sep_lifo` visits the current definition first. This macro provides the most efficient means for iterating over a pushdef stack. In particular, `m4_stack_foreach([*macro*], [*action*])` is short for `m4_stack_foreach_sep([*macro*], [*action*(], [)])`.

#### 8.3.6 Evaluation Macros

The following macros give some control over the order of the evaluation by adding or removing levels of quotes.

**Macro: **m4_apply***(*macro*, *list*)* ¶**

Apply the elements of the quoted, comma-separated *list* as the arguments to *macro*. If *list* is empty, invoke *macro* without arguments. Note the difference between `m4_indir`, which expects its first argument to be a macro name but can use names that are otherwise invalid, and `m4_apply`, where *macro* can contain other text, but must end in a valid macro name.

```
m4_apply([m4_count], [])
⇒0
m4_apply([m4_count], [[]])
⇒1
m4_apply([m4_count], [[1], [2]])
⇒2
m4_apply([m4_join], [[|], [1], [2]])
⇒1|2
```

**Macro: **m4_count***(*arg*, …)* ¶**

This macro returns the number of arguments it was passed.

**Macro: **m4_curry***(*macro*, *arg*…)* ¶**

This macro performs argument currying. The expansion of this macro is another macro name that expects exactly one argument; that argument is then appended to the *arg* list, and then *macro* is expanded with the resulting argument list.

```
m4_curry([m4_curry], [m4_reverse], [1])([2])([3])
⇒3, 2, 1
```

Unfortunately, due to a limitation in M4 1.4.x, it is not possible to pass the definition of a builtin macro as the argument to the output of `m4_curry`; the empty string is used instead of the builtin token. This behavior is rectified by using M4 1.6 or newer.

**Macro: **m4_do***(*arg*, …)* ¶**

This macro loops over its arguments and expands each *arg* in sequence. Its main use is for readability; it allows the use of indentation and fewer `dnl` to result in the same expansion. This macro guarantees that no expansion will be concatenated with subsequent text; to achieve full concatenation, use `m4_unquote(m4_join([], *arg…*))`.

```
m4_define([ab],[1])m4_define([bc],[2])m4_define([abc],[3])dnl
m4_do([a],[b])c
⇒abc
m4_unquote(m4_join([],[a],[b]))c
⇒3
m4_define([a],[A])m4_define([b],[B])m4_define([c],[C])dnl
m4_define([AB],[4])m4_define([BC],[5])m4_define([ABC],[6])dnl
m4_do([a],[b])c
⇒ABC
m4_unquote(m4_join([],[a],[b]))c
⇒3
```

**Macro: **m4_dquote***(*arg*, …)* ¶**

Return the arguments as a quoted list of quoted arguments. Conveniently, if there is just one *arg*, this effectively adds a level of quoting.

**Macro: **m4_dquote_elt***(*arg*, …)* ¶**

Return the arguments as a series of double-quoted arguments. Whereas `m4_dquote` returns a single argument, `m4_dquote_elt` returns as many arguments as it was passed.

**Macro: **m4_echo***(*arg*, …)* ¶**

Return the arguments, with the same level of quoting. Other than discarding whitespace after unquoted commas, this macro is a no-op.

**Macro: **m4_expand***(*arg*)* ¶**

Return the expansion of *arg* as a quoted string. Whereas `m4_quote` is designed to collect expanded text into a single argument, `m4_expand` is designed to perform one level of expansion on quoted text. One distinction is in the treatment of whitespace following a comma in the original *arg*. Any time multiple arguments are collected into one with `m4_quote`, the M4 argument collection rules discard the whitespace. However, with `m4_expand`, whitespace is preserved, even after the expansion of macros contained in *arg*. Additionally, `m4_expand` is able to expand text that would involve an unterminated comment, whereas expanding that same text as the argument to `m4_quote` runs into difficulty in finding the end of the argument. Since manipulating diversions during argument collection is inherently unsafe, `m4_expand` issues an error if *arg* attempts to change the current diversion (see Diversion support).

```
m4_define([active], [ACT, IVE])dnl
m4_define([active2], [[ACT, IVE]])dnl
m4_quote(active, active)
⇒ACT,IVE,ACT,IVE
m4_expand([active, active])
⇒ACT, IVE, ACT, IVE
m4_quote(active2, active2)
⇒ACT, IVE,ACT, IVE
m4_expand([active2, active2])
⇒ACT, IVE, ACT, IVE
m4_expand([# m4_echo])
⇒# m4_echo
m4_quote(# m4_echo)
)
⇒# m4_echo)
⇒
```

Note that `m4_expand` cannot handle an *arg* that expands to literal unbalanced quotes, but that quadrigraphs can be used when unbalanced output is necessary. Likewise, unbalanced parentheses should be supplied with double quoting or a quadrigraph.

```
m4_define([pattern], [[!@<:@]])dnl
m4_define([bar], [BAR])dnl
m4_expand([case $foo in
  m4_defn([pattern])@:}@ bar ;;
  *[)] blah ;;
esac])
⇒case $foo in
⇒  [![]) BAR ;;
⇒  *) blah ;;
⇒esac
```

**Macro: **m4_ignore***(…)* ¶**

This macro was introduced in Autoconf 2.62. Expands to nothing, ignoring all of its arguments. By itself, this isn’t very useful. However, it can be used to conditionally ignore an arbitrary number of arguments, by deciding which macro name to apply to a list of arguments.

```
dnl foo outputs a message only if [debug] is defined.
m4_define([foo],
[m4_ifdef([debug],[AC_MSG_NOTICE],[m4_ignore])([debug message])])
```

Note that for earlier versions of Autoconf, the macro `__gnu__` can serve the same purpose, although it is less readable.

**Macro: **m4_make_list***(*arg*, …)* ¶**

This macro exists to aid debugging of M4sugar algorithms. Its net effect is similar to `m4_dquote`—it produces a quoted list of quoted arguments, for each *arg*. The difference is that this version uses a comma-newline separator instead of just comma, to improve readability of the list; with the result that it is less efficient than `m4_dquote`.

```
m4_define([zero],[0])m4_define([one],[1])m4_define([two],[2])dnl
m4_dquote(zero, [one], [[two]])
⇒[0],[one],[[two]]
m4_make_list(zero, [one], [[two]])
⇒[0],
⇒[one],
⇒[[two]]
m4_foreach([number], m4_dquote(zero, [one], [[two]]), [ number])
⇒ 0 1 two
m4_foreach([number], m4_make_list(zero, [one], [[two]]), [ number])
⇒ 0 1 two
```

**Macro: **m4_quote***(*arg*, …)* ¶**

Return the arguments as a single entity, i.e., wrap them into a pair of quotes. This effectively collapses multiple arguments into one, although it loses whitespace after unquoted commas in the process.

**Macro: **m4_reverse***(*arg*, …)* ¶**

Outputs each argument with the same level of quoting, but in reverse order, and with space following each comma for readability.

```
m4_define([active], [ACT,IVE])
⇒
m4_reverse(active, [active])
⇒active, IVE, ACT
```

**Macro: **m4_unquote***(*arg*, …)* ¶**

This macro was introduced in Autoconf 2.62. Expand each argument, separated by commas. For a single *arg*, this effectively removes a layer of quoting, and `m4_unquote([*arg*])` is more efficient than the equivalent `m4_do([*arg*])`. For multiple arguments, this results in an unquoted list of expansions. This is commonly used with `m4_split`, in order to convert a single quoted list into a series of quoted elements.

The following example aims at emphasizing the difference between several scenarios: not using these macros, using `m4_defn`, using `m4_quote`, using `m4_dquote`, and using `m4_expand`.

```
$ cat example.m4
dnl Overquote, so that quotes are visible.
m4_define([show], [$[]1 = [$1], $[]@ = [$@]])
m4_define([a], [A])
m4_define([mkargs], [1, 2[,] 3])
m4_define([arg1], [[$1]])
m4_divert([0])dnl
show(a, b)
show([a, b])
show(m4_quote(a, b))
show(m4_dquote(a, b))
show(m4_expand([a, b]))

arg1(mkargs)
arg1([mkargs])
arg1(m4_defn([mkargs]))
arg1(m4_quote(mkargs))
arg1(m4_dquote(mkargs))
arg1(m4_expand([mkargs]))
$ autom4te -l m4sugar example.m4
$1 = A, $@ = [A],[b]
$1 = a, b, $@ = [a, b]
$1 = A,b, $@ = [A,b]
$1 = [A],[b], $@ = [[A],[b]]
$1 = A, b, $@ = [A, b]

1
mkargs
1, 2[,] 3
1,2, 3
[1],[2, 3]
1, 2, 3
```

#### 8.3.7 String manipulation in M4

The following macros may be used to manipulate strings in M4. Many of the macros in this section intentionally result in quoted strings as output, rather than subjecting the arguments to further expansions. As a result, if you are manipulating text that contains active M4 characters, the arguments are passed with single quoting rather than double.

**Macro: **m4_append***(*macro-name*, *string*, [*separator*])* ¶**

**Macro: **m4_append_uniq***(*macro-name*, *string*, [*separator*] [*if-uniq*], [*if-duplicate*])* ¶**

Redefine *macro-name* to its former contents with *separator* and *string* added at the end. If *macro-name* was undefined before (but not if it was defined but empty), then no *separator* is added. As of Autoconf 2.62, neither *string* nor *separator* are expanded during this macro; instead, they are expanded when *macro-name* is invoked.

`m4_append` can be used to grow strings, and `m4_append_uniq` to grow strings without duplicating substrings. Additionally, `m4_append_uniq` takes two optional parameters as of Autoconf 2.62; *if-uniq* is expanded if *string* was appended, and *if-duplicate* is expanded if *string* was already present. Also, `m4_append_uniq` warns if *separator* is not empty, but occurs within *string*, since that can lead to duplicates.

Note that `m4_append` can scale linearly in the length of the final string, depending on the quality of the underlying M4 implementation, while `m4_append_uniq` has an inherent quadratic scaling factor. If an algorithm can tolerate duplicates in the final string, use the former for speed. If duplicates must be avoided, consider using `m4_set_add` instead (see Set manipulation in M4).

```
m4_define([active], [ACTIVE])dnl
m4_append([sentence], [This is an])dnl
m4_append([sentence], [ active ])dnl
m4_append([sentence], [symbol.])dnl
sentence
⇒This is an ACTIVE symbol.
m4_undefine([active])dnl
⇒This is an active symbol.
m4_append_uniq([list], [one], [, ], [new], [existing])
⇒new
m4_append_uniq([list], [one], [, ], [new], [existing])
⇒existing
m4_append_uniq([list], [two], [, ], [new], [existing])
⇒new
m4_append_uniq([list], [three], [, ], [new], [existing])
⇒new
m4_append_uniq([list], [two], [, ], [new], [existing])
⇒existing
list
⇒one, two, three
m4_dquote(list)
⇒[one],[two],[three]
m4_append([list2], [one], [[, ]])dnl
m4_append_uniq([list2], [two], [[, ]])dnl
m4_append([list2], [three], [[, ]])dnl
list2
⇒one, two, three
m4_dquote(list2)
⇒[one, two, three]
```

**Macro: **m4_append_uniq_w***(*macro-name*, *strings*)* ¶**

This macro was introduced in Autoconf 2.62. It is similar to `m4_append_uniq`, but treats *strings* as a whitespace separated list of words to append, and only appends unique words. *macro-name* is updated with a single space between new words.

```
m4_append_uniq_w([numbers], [1 1 2])dnl
m4_append_uniq_w([numbers], [ 2 3 ])dnl
numbers
⇒1 2 3
```

**Macro: **m4_chomp***(*string*)* ¶**

**Macro: **m4_chomp_all***(*string*)* ¶**

Output *string* in quotes, but without a trailing newline. The macro `m4_chomp` is slightly faster, and removes at most one newline; the macro `m4_chomp_all` removes all consecutive trailing newlines. Unlike `m4_flatten`, embedded newlines are left intact, and backslash does not influence the result.

**Macro: **m4_combine***([*separator*], *prefix-list*, [*infix*], *suffix-1*, [*suffix-2*], …)* ¶**

This macro produces a quoted string containing the pairwise combination of every element of the quoted, comma-separated *prefix-list*, and every element from the *suffix* arguments. Each pairwise combination is joined with *infix* in the middle, and successive pairs are joined by *separator*. No expansion occurs on any of the arguments. No output occurs if either the *prefix* or *suffix* list is empty, but the lists can contain empty elements.

```
m4_define([a], [oops])dnl
m4_combine([, ], [[a], [b], [c]], [-], [1], [2], [3])
⇒a-1, a-2, a-3, b-1, b-2, b-3, c-1, c-2, c-3
m4_combine([, ], [[a], [b]], [-])
⇒
m4_combine([, ], [[a], [b]], [-], [])
⇒a-, b-
m4_combine([, ], [], [-], [1], [2])
⇒
m4_combine([, ], [[]], [-], [1], [2])
⇒-1, -2
```

**Macro: **m4_escape***(*string*)* ¶**

Convert all instances of ‘[’, ‘]’, ‘#’, and ‘$’ within *string* into their respective quadrigraphs. The result is still a quoted string.

**Macro: **m4_flatten***(*string*)* ¶**

Flatten *string* into a single line. Delete all backslash-newline pairs, and replace all remaining newlines with a space. The result is still a quoted string.

**Macro: **m4_join***([*separator*], *args*…)* ¶**

**Macro: **m4_joinall***([*separator*], *args*…)* ¶**

Concatenate each *arg*, separated by *separator*. `joinall` uses every argument, while `join` omits empty arguments so that there are no back-to-back separators in the output. The result is a quoted string.

```
m4_define([active], [ACTIVE])dnl
m4_join([|], [one], [], [active], [two])
⇒one|active|two
m4_joinall([|], [one], [], [active], [two])
⇒one||active|two
```

Note that if all you intend to do is join *args* with commas between them, to form a quoted list suitable for `m4_foreach`, it is more efficient to use `m4_dquote`.

**Macro: **m4_newline***([*text*])* ¶**

This macro was introduced in Autoconf 2.62, and expands to a newline, followed by any *text*. It is primarily useful for maintaining macro formatting, and ensuring that M4 does not discard leading whitespace during argument collection.

**Macro: **m4_normalize***(*string*)* ¶**

Remove leading and trailing spaces and tabs, sequences of backslash-then-newline, and replace multiple spaces, tabs, and newlines with a single space. This is a combination of `m4_flatten` and `m4_strip`. To determine if *string* consists only of bytes that would be removed by `m4_normalize`, you can use `m4_ifblank`.

**Macro: **m4_re_escape***(*string*)* ¶**

Backslash-escape all characters in *string* that are active in regexps.

**Macro: **m4_split***(*string*, [*regexp* = ‘[\t ]+’])* ¶**

Split *string* into an M4 list of elements quoted by ‘[’ and ‘]’, while keeping white space at the beginning and at the end. If *regexp* is given, use it instead of ‘[\t ]+’ for splitting. If *string* is empty, the result is an empty list.

**Macro: **m4_strip***(*string*)* ¶**

Strip whitespace from *string*. Sequences of spaces and tabs are reduced to a single space, then leading and trailing spaces are removed. The result is still a quoted string. Note that this does not interfere with newlines; if you want newlines stripped as well, consider `m4_flatten`, or do it all at once with `m4_normalize`. To quickly test if *string* has only whitespace, use `m4_ifblank`.

**Macro: **m4_text_box***(*message*, [*frame* = ‘-’])* ¶**

Add a text box around *message*, using *frame* as the border character above and below the message. The *frame* argument must be a single byte, and does not support quadrigraphs. The frame correctly accounts for the subsequent expansion of *message*. For example:

```
m4_define([macro], [abc])dnl
m4_text_box([macro])
⇒## --- ##
⇒## abc ##
⇒## --- ##
```

The *message* must contain balanced quotes and parentheses, although quadrigraphs can be used to work around this.

**Macro: **m4_text_wrap***(*string*, [*prefix*], [*prefix1* = *prefix*], [*width* = ‘79’])* ¶**

Break *string* into a series of whitespace-separated words, then output those words separated by spaces, and wrapping lines any time the output would exceed *width* columns. If given, *prefix1* begins the first line, and *prefix* begins all wrapped lines. If *prefix1* is longer than *prefix*, then the first line consists of just *prefix1*. If *prefix* is longer than *prefix1*, padding is inserted so that the first word of *string* begins at the same indentation as all wrapped lines. Note that using literal tab characters in any of the arguments will interfere with the calculation of width. No expansions occur on *prefix*, *prefix1*, or the words of *string*, although quadrigraphs are recognized.

For some examples:

```
m4_text_wrap([Short string */], [   ], [/* ], [20])
⇒/* Short string */
m4_text_wrap([Much longer string */], [   ], [/* ], [20])
⇒/* Much longer
⇒   string */
m4_text_wrap([Short doc.], [          ], [  --short ], [30])
⇒  --short Short doc.
m4_text_wrap([Short doc.], [          ], [  --too-wide ], [30])
⇒  --too-wide
⇒          Short doc.
m4_text_wrap([Super long documentation.], [     ],
             [  --too-wide ], 30)
⇒  --too-wide
⇒     Super long
⇒     documentation.
```

**Macro: **m4_tolower***(*string*)* ¶**

**Macro: **m4_toupper***(*string*)* ¶**

Return *string* with letters converted to upper or lower case, respectively.

#### 8.3.8 Arithmetic computation in M4

The following macros facilitate integer arithmetic operations.

Where a parameter is documented as taking an arithmetic expression, you can use anything that can be parsed by `m4_eval`. Any other numeric parameter should consist of an optional sign followed by one or more decimal digits; it is treated as a decimal integer.

Macros that expand to a number do so as either ‘0’, or an optional ‘-’ followed by a nonzero decimal digit followed by zero or more decimal digits.

Due to `m4` limitations, arithmetic expressions and numeric parameters should use only numbers that fit into a 32-bit signed integer.

**Macro: **m4_cmp***(*expr-1*, *expr-2*)* ¶**

Compare the arithmetic expressions *expr-1* and *expr-2*, and expand to ‘-1’ if *expr-1* is smaller, ‘0’ if they are equal, and ‘1’ if *expr-1* is larger.

**Macro: **m4_list_cmp***(*list-1*, *list-2*)* ¶**

Compare the two M4 lists consisting of comma-separated arithmetic expressions, left to right. Expand to ‘-1’ for the first element pairing where the value from *list-1* is smaller, ‘1’ where the value from *list-2* is smaller, or ‘0’ if both lists have the same values. If one list is shorter than the other, the remaining elements of the longer list are compared against zero.

```
m4_list_cmp([1, 0],       [1])
⇒0
m4_list_cmp([1, [1 * 0]], [1, 0])
⇒0
m4_list_cmp([1, 2],       [1, 0])
⇒1
m4_list_cmp([1, [1+1], 3],[1, 2])
⇒1
m4_list_cmp([1, 2, -3],   [1, 2])
⇒-1
m4_list_cmp([1, 0],       [1, 2])
⇒-1
m4_list_cmp([1],          [1, 2])
⇒-1
```

**Macro: **m4_max***(*arg*, …)* ¶**

This macro was introduced in Autoconf 2.62. Expand to the value of the maximum arithmetic expression among all the arguments.

**Macro: **m4_min***(*arg*, …)* ¶**

This macro was introduced in Autoconf 2.62. Expand to the value of the minimum arithmetic expression among all the arguments.

**Macro: **m4_sign***(*expr*)* ¶**

Expand to ‘-1’ if the arithmetic expression *expr* is negative, ‘1’ if it is positive, and ‘0’ if it is zero.

**Macro: **m4_version_compare***(*version-1*, *version-2*)* ¶**

This macro was introduced in Autoconf 2.53, but had a number of usability limitations that were not lifted until Autoconf 2.62. Compare the version strings *version-1* and *version-2*, and expand to ‘-1’ if *version-1* is smaller, ‘0’ if they are the same, or ‘1’ *version-2* is smaller. Version strings must be a list of elements separated by ‘.’, ‘,’ or ‘-’, where each element is a number along with optional case-insensitive letters designating beta releases. The comparison stops at the leftmost element that contains a difference, although a 0 element compares equal to a missing element.

It is permissible to include commit identifiers in *version*, such as an abbreviated SHA1 of the commit, provided there is still a monotonically increasing prefix to allow for accurate version-based comparisons. For example, this paragraph was written when the development snapshot of autoconf claimed to be at version ‘2.61a-248-dc51’, or 248 commits after the 2.61a release, with an abbreviated commit identification of ‘dc51’.

```
m4_version_compare([1.1], [2.0])
⇒-1
m4_version_compare([2.0b], [2.0a])
⇒1
m4_version_compare([1.1.1], [1.1.1a])
⇒-1
m4_version_compare([1.2], [1.1.1a])
⇒1
m4_version_compare([1.0], [1])
⇒0
m4_version_compare([1.1pre], [1.1PRE])
⇒0
m4_version_compare([1.1a], [1,10])
⇒-1
m4_version_compare([2.61a], [2.61a-248-dc51])
⇒-1
m4_version_compare([2.61b], [2.61a-248-dc51])
⇒1
```

**Macro: **m4_version_prereq***(*version*, [*if-new-enough*], [*if-old* = ‘m4_fatal’])* ¶**

Compares *version* against the version of Autoconf currently running. If the running version is at *version* or newer, expand *if-new-enough*, but if *version* is larger than the version currently executing, expand *if-old*, which defaults to printing an error message and exiting m4sugar with status 63. When given only one argument, this behaves like `AC_PREREQ` (see Dealing with Autoconf versions). Remember that the autoconf philosophy favors feature checks over version checks.

#### 8.3.9 Set manipulation in M4

Sometimes, it is necessary to track a set of data, where the order does not matter and where there are no duplicates in the set. The following macros facilitate set manipulations. Each set is an opaque object, which can only be accessed via these basic operations. The underlying implementation guarantees linear scaling for set creation, which is more efficient than using the quadratic `m4_append_uniq`. Both set names and values can be arbitrary strings, except for unbalanced quotes. This implementation ties up memory for removed elements until the next operation that must traverse all the elements of a set; and although that may slow down some operations until the memory for removed elements is pruned, it still guarantees linear performance.

**Macro: **m4_set_add***(*set*, *value*, [*if-uniq*], [*if-dup*])* ¶**

Adds the string *value* as a member of set *set*. Expand *if-uniq* if the element was added, or *if-dup* if it was previously in the set. Operates in amortized constant time, so that set creation scales linearly.

**Macro: **m4_set_add_all***(*set*, *value*…)* ¶**

Adds each *value* to the set *set*. This is slightly more efficient than repeatedly invoking `m4_set_add`.

**Macro: **m4_set_contains***(*set*, *value*, [*if-present*], [*if-absent*])* ¶**

Expands *if-present* if the string *value* is a member of *set*, otherwise *if-absent*.

```
m4_set_contains([a], [1], [yes], [no])
⇒no
m4_set_add([a], [1], [added], [dup])
⇒added
m4_set_add([a], [1], [added], [dup])
⇒dup
m4_set_contains([a], [1], [yes], [no])
⇒yes
m4_set_remove([a], [1], [removed], [missing])
⇒removed
m4_set_contains([a], [1], [yes], [no])
⇒no
m4_set_remove([a], [1], [removed], [missing])
⇒missing
```

**Macro: **m4_set_contents***(*set*, [*sep*])* ¶**

**Macro: **m4_set_dump***(*set*, [*sep*])* ¶**

Expands to a single string consisting of all the members of the set *set*, each separated by *sep*, which is not expanded. `m4_set_contents` leaves the elements in *set* but reclaims any memory occupied by removed elements, while `m4_set_dump` is a faster one-shot action that also deletes the set. No provision is made for disambiguating members that contain a non-empty *sep* as a substring; use `m4_set_empty` to distinguish between an empty set and the set containing only the empty string. The order of the output is unspecified; in the current implementation, part of the speed of `m4_set_dump` results from using a different output order than `m4_set_contents`. These macros scale linearly in the size of the set before memory pruning, and `m4_set_contents([*set*], [*sep*])` is faster than `m4_joinall([*sep*]m4_set_listc([*set*]))`.

```
m4_set_add_all([a], [1], [2], [3])
⇒
m4_set_contents([a], [-])
⇒1-2-3
m4_joinall([-]m4_set_listc([a]))
⇒1-2-3
m4_set_dump([a], [-])
⇒3-2-1
m4_set_contents([a])
⇒
m4_set_add([a], [])
⇒
m4_set_contents([a], [-])
⇒
```

**Macro: **m4_set_delete***(*set*)* ¶**

Delete all elements and memory associated with *set*. This is linear in the set size, and faster than removing one element at a time.

**Macro: **m4_set_difference***(*seta*, *setb*)* ¶**

**Macro: **m4_set_intersection***(*seta*, *setb*)* ¶**

**Macro: **m4_set_union***(*seta*, *setb*)* ¶**

Compute the relation between *seta* and *setb*, and output the result as a list of quoted arguments without duplicates and with a leading comma. Set difference selects the elements in *seta* but not *setb*, intersection selects only elements in both sets, and union selects elements in either set. These actions are linear in the sum of the set sizes. The leading comma is necessary to distinguish between no elements and the empty string as the only element.

```
m4_set_add_all([a], [1], [2], [3])
⇒
m4_set_add_all([b], [3], [], [4])
⇒
m4_set_difference([a], [b])
⇒,1,2
m4_set_difference([b], [a])
⇒,,4
m4_set_intersection([a], [b])
⇒,3
m4_set_union([a], [b])
⇒,1,2,3,,4
```

**Macro: **m4_set_empty***(*set*, [*if-empty*], [*if-elements*])* ¶**

Expand *if-empty* if the set *set* has no elements, otherwise expand *if-elements*. This macro operates in constant time. Using this macro can help disambiguate output from `m4_set_contents` or `m4_set_list`.

**Macro: **m4_set_foreach***(*set*, *variable*, *action*)* ¶**

For each element in the set *set*, expand *action* with the macro *variable* defined as the set element. Behavior is unspecified if *action* recursively lists the contents of *set* (although listing other sets is acceptable), or if it modifies the set in any way other than removing the element currently contained in *variable*. This macro is faster than the corresponding `m4_foreach([*variable*], m4_indir([m4_dquote]m4_set_listc([*set*])), [*action*])`, although `m4_set_map` might be faster still.

```
m4_set_add_all([a]m4_for([i], [1], [5], [], [,i]))
⇒
m4_set_contents([a])
⇒12345
m4_set_foreach([a], [i],
  [m4_if(m4_eval(i&1), [0], [m4_set_remove([a], i, [i])])])
⇒24
m4_set_contents([a])
⇒135
```

**Macro: **m4_set_list***(*set*)* ¶**

**Macro: **m4_set_listc***(*set*)* ¶**

Produce a list of arguments, where each argument is a quoted element from the set *set*. The variant `m4_set_listc` is unambiguous, by adding a leading comma if there are any set elements, whereas the variant `m4_set_list` cannot distinguish between an empty set and a set containing only the empty string. These can be directly used in macros that take multiple arguments, such as `m4_join` or `m4_set_add_all`, or wrapped by `m4_dquote` for macros that take a quoted list, such as `m4_map` or `m4_foreach`. Any memory occupied by removed elements is reclaimed during these macros.

```
m4_set_add_all([a], [1], [2], [3])
⇒
m4_set_list([a])
⇒1,2,3
m4_set_list([b])
⇒
m4_set_listc([b])
⇒
m4_count(m4_set_list([b]))
⇒1
m4_set_empty([b], [0], [m4_count(m4_set_list([b]))])
⇒0
m4_set_add([b], [])
⇒
m4_set_list([b])
⇒
m4_set_listc([b])
⇒,
m4_count(m4_set_list([b]))
⇒1
m4_set_empty([b], [0], [m4_count(m4_set_list([b]))])
⇒1
```

**Macro: **m4_set_map***(*set*, *action*)* ¶**

For each element in the set *set*, expand *action* with a single argument of the set element. Behavior is unspecified if *action* recursively lists the contents of *set* (although listing other sets is acceptable), or if it modifies the set in any way other than removing the element passed as an argument. This macro is faster than either corresponding counterpart of `m4_map_args([*action*]m4_set_listc([*set*]))` or `m4_set_foreach([*set*], [var], [*action*(m4_defn([var]))])`. It is possible to use `m4_curry` if more than one argument is needed for *action*, although it is more efficient to use `m4_set_map_sep` in that case.

**Macro: **m4_set_map_sep***(*set*, [*pre*], [*post*], [*sep*])* ¶**

For each element in the set *set*, expand `*pre*[element]*post*`, additionally expanding *sep* between elements. Behavior is unspecified if the expansion recursively lists the contents of *set* (although listing other sets is acceptable), or if it modifies the set in any way other than removing the element visited by the expansion. This macro provides the most efficient means for non-destructively visiting the elements of a set; in particular, `m4_set_map([*set*], [*action*])` is equivalent to `m4_set_map_sep([*set*], [*action*(], [)])`.

**Macro: **m4_set_remove***(*set*, *value*, [*if-present*], [*if-absent*])* ¶**

If *value* is an element in the set *set*, then remove it and expand *if-present*. Otherwise expand *if-absent*. This macro operates in constant time so that multiple removals will scale linearly rather than quadratically; but when used outside of `m4_set_foreach` or `m4_set_map`, it leaves memory occupied until the set is later compacted by `m4_set_contents` or `m4_set_list`. Several other set operations are then less efficient between the time of element removal and subsequent memory compaction, but still maintain their guaranteed scaling performance.

**Macro: **m4_set_size***(*set*)* ¶**

Expand to the size of the set *set*. This implementation operates in constant time, and is thus more efficient than `m4_eval(m4_count(m4_set_listc([set])) - 1)`.

#### 8.3.10 Forbidden Patterns

M4sugar provides a means to define suspicious patterns, patterns describing tokens which should not be found in the output. For instance, if an Autoconf configure script includes tokens such as ‘AC_DEFINE’, or ‘dnl’, then most probably something went wrong (typically a macro was not evaluated because of overquotation).

M4sugar forbids all the tokens matching ‘^_?m4_’ and ‘^dnl$’. Additional layers, such as M4sh and Autoconf, add additional forbidden patterns to the list.

**Macro: **m4_pattern_forbid***(*pattern*)* ¶**

Declare that no token matching *pattern* must be found in the output. The output file is (temporarily) split into one word per line as part of the `autom4te` post-processing, with each line (and therefore word) then being checked against the Perl regular expression *pattern*. If the regular expression matches, and `m4_pattern_allow` does not also match, then an error is raised.

Comments are not checked; this can be a problem if, for instance, you have some macro left unexpanded after an ‘#include’. No consensus is currently found in the Autoconf community, as some people consider it should be valid to name macros in comments (which doesn’t make sense to the authors of this documentation: input, such as macros, should be documented by ‘dnl’ comments; reserving ‘#’-comments to document the output).

As an example, if you define your own macros that begin with ‘M_’ and are composed from capital letters and underscores, the specification of `m4_pattern_forbid([^M_[A-Z_]+])` will ensure all your macros are expanded when not used in comments.

As an example of a common use of this macro, consider what happens in packages that want to use the `pkg-config` script via the third-party `PKG_CHECK_MODULES` macro. By default, if a developer checks out the development tree but has not yet installed the pkg-config macros locally, they can manage to successfully run `autoconf` on the package, but the resulting configure file will likely result in a confusing shell message about a syntax error on the line mentioning the unexpanded `PKG_CHECK_MODULES` macro. On the other hand, if configure.ac includes `m4_pattern_forbid([^PKG_])`, the missing pkg-config macros will be detected immediately without allowing `autoconf` to succeed.

Of course, you might encounter exceptions to these generic rules, for instance you might have to refer to ‘$m4_flags’.

**Macro: **m4_pattern_allow***(*pattern*)* ¶**

Any token matching *pattern* is allowed, including if it matches an `m4_pattern_forbid` pattern.

For example, Gnulib uses `m4_pattern_forbid([^gl_])` to reserve the `gl_` namespace for itself, but also uses `m4_pattern_allow([^gl_ES$])` to avoid a false negative on the valid locale name.

### 8.4 Debugging via autom4te

At times, it is desirable to see what was happening inside m4, to see why output was not matching expectations. However, post-processing done by `autom4te` means that directly using the m4 builtin `m4_traceon` is likely to interfere with operation. Also, frequent diversion changes and the concept of forbidden tokens make it difficult to use `m4_defn` to generate inline comments in the final output.

There are a couple of tools to help with this. One is the use of the --trace option provided by `autom4te` (as well as each of the programs that wrap `autom4te`, such as `autoconf`), in order to inspect when a macro is called and with which arguments. For example, when this paragraph was written, the autoconf version could be found by:

```
$ autoconf --trace=AC_INIT
configure.ac:23:AC_INIT:GNU Autoconf:2.63b.95-3963:bug-autoconf@gnu.org
$ autoconf --trace='AC_INIT:version is $2'
version is 2.63b.95-3963
```

Another trick is to print out the expansion of various m4 expressions to standard error or to an independent file, with no further m4 expansion, and without interfering with diversion changes or the post-processing done to standard output. `m4_errprintn` shows a given expression on standard error. For example, if you want to see the expansion of an autoconf primitive or of one of your autoconf macros, you can do it like this:

```
$ cat <<\EOF > configure.ac
AC_INIT
m4_errprintn([The definition of AC_DEFINE_UNQUOTED:])
m4_errprintn(m4_defn([AC_DEFINE_UNQUOTED]))
AC_OUTPUT
EOF
$ autoconf
error→The definition of AC_DEFINE_UNQUOTED:
error→_AC_DEFINE_Q([], $@)
```
