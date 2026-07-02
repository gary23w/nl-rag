---
title: "The GNU Awk User’s Guide (part 24/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 24/38
---

## 15 Namespaces in `gawk`

This chapter describes a feature that is specific to `gawk`.

> **CAUTION:** This feature described in this chapter is new. It is entirely possible, and even likely, that there are dark corners (if not bugs) still lurking within the implementation. If you find any such, please report them (See Reporting Problems and Bugs).

### 15.1 Standard `awk`’s Single Namespace

In standard `awk`, there is a single, global, *namespace*. This means that *all* function names and global variable names must be unique. For example, two different `awk` source files cannot both define a function named `min()`, or define the same identifier, used as a scalar in one and as an array in the other.

This situation is okay when programs are small, say a few hundred lines, or even a few thousand, but it prevents the development of reusable libraries of `awk` functions, and can inadvertently cause independently-developed library files to accidentally step on each other’s “private” global variables (see Naming Library Function Global Variables).

Most other programming languages solve this issue by providing some kind of namespace control: a way to say “this function is in namespace *xxx*, and that function is in namespace *yyy*.” (Of course, there is then still a single namespace for the namespaces, but the hope is that there are much fewer namespaces in use by any given program, and thus much less chance for collisions.) These facilities are sometimes referred to as *packages* or *modules*.

Starting with version 5.0, `gawk` provides a simple mechanism to put functions and global variables into separate namespaces.

### 15.2 Qualified Names

A *qualified name* is an identifier that includes a namespace name, the namespace separator `::`, and a *component* name. For example, one might have a function named `posix::getpid()`. Here, the namespace is `posix` and the function name within the namespace (the component) is `getpid()`. The namespace and component names are separated by a double-colon. Only one such separator is allowed in a qualified name.

> **NOTE:** Unlike C++, the `::` is *not* an operator. No spaces are allowed between the namespace name, the `::`, and the component name.

You must use qualified names from one namespace to access variables and functions in another. This is especially important when using variable names to index the special `SYMTAB` array (see Built-in Variables That Convey Information), and when making indirect function calls (see Indirect Function Calls).

### 15.3 The Default Namespace

The default namespace, not surprisingly, is `awk`. All of the predefined `awk` and `gawk` variables are in this namespace, and thus have qualified names like `awk::ARGC`, `awk::NF`, and so on.

Furthermore, even when you have changed the namespace for your current source file (see Changing The Namespace), `gawk` forces unqualified identifiers whose names are all uppercase letters to be in the `awk` namespace. This makes it possible for you to easily reference `gawk`’s global variables from different namespaces. It also keeps your code looking natural.

### 15.4 Changing The Namespace

In order to set the current namespace, use an `@namespace` directive at the top level of your program:

```
@namespace "passwd"

BEGIN { ... }
...
```

After this directive, all simple non-completely-uppercase identifiers are placed into the `passwd` namespace.

You can change the namespace multiple times within a single source file, although this is likely to become confusing if you do it too much.

> **NOTE:** Association of unqualified identifiers to a namespace is handled while `gawk` parses your program, *before* it starts to run. There is no concept of a “current” namespace once your program starts executing. Be sure you understand this.

Each source file for -i and -f starts out with an implicit ‘@namespace "awk"’. Similarly, each chunk of command-line code supplied with -e has such an implicit initial statement (see Command-Line Options).

Files included with `@include` (see Including Other Files into Your Program) “push” and “pop” the current namespace. That is, each `@include` saves the current namespace and starts over with an implicit ‘@namespace "awk"’ which remains in effect until an explicit `@namespace` directive is seen. When `gawk` finishes processing the included file, the saved namespace is restored and processing continues where it left off in the original file.

The use of `@namespace` has no influence upon the order of execution of `BEGIN`, `BEGINFILE`, `END`, and `ENDFILE` rules.

### 15.5 Namespace and Component Naming Rules

A number of rules apply to the namespace and component names, as follows.

- It is a syntax error to use qualified names for function parameter names.
- It is a syntax error to use any standard `awk` reserved word (such as `if` or `for`), or the name of any standard built-in function (such as `sin()` or `gsub()`) as either part of a qualified name. Thus, the following produces a syntax error: @namespace "example" function gsub(str, pat, result) { ... }
- Outside the `awk` namespace, the names of the additional `gawk` built-in functions (such as `gensub()` or `strftime()`) *may* be used as component names (see Gawk Extension Functions). The same set of names may be used as namespace names, although this has the potential to be confusing.
- The additional `gawk` built-in functions may still be called from outside the `awk` namespace by qualifying them. For example, `awk::systime()`. Here is a somewhat silly example demonstrating this rule and the previous one: BEGIN { print "in awk namespace, systime() =", systime() } @namespace "testing" function systime() { print "in testing namespace, systime() =", awk::systime() } BEGIN { systime() } When run, it produces output like this: $ gawk -f systime.awk -| in awk namespace, systime() = 1500488503 -| in testing namespace, systime() = 1500488503
- `gawk` pre-defined variable names may be used: `NF::NR` is valid, if possibly not all that useful.

### 15.6 Internal Name Management

For backwards compatibility, all identifiers in the `awk` namespace are stored internally as unadorned identifiers (that is, without a leading ‘awk::’). This is mainly relevant when using such identifiers as indices for `SYMTAB`, `FUNCTAB`, and `PROCINFO["identifiers"]` (see Built-in Variables That Convey Information), and for use in indirect function calls (see Indirect Function Calls).

In program code, to refer to variables and functions in the `awk` namespace from another namespace, you must still use the ‘awk::’ prefix. For example:

```
@namespace "awk"          This is the default namespace

BEGIN {
    Title = "My Report"   Qualified name is awk::Title
}

@namespace "report"       Now in report namespace

function compute()        This is really report::compute()
{
    print awk::Title      But would be SYMTAB["Title"]
    ...
}
```

### 15.7 Namespace Example

The following example is a revised version of the suite of routines developed in Reading the User Database. See there for an explanation of how the code works.

The formulation here, due mainly to Andrew Schorr, is rather elegant. All of the implementation functions and variables are in the `passwd` namespace, whereas the main interface functions are defined in the `awk` namespace.

```
# ns_passwd.awk --- access password file information

@namespace "passwd"

BEGIN {
    # tailor this to suit your system
    Awklib = "/usr/local/libexec/awk/"
}

function Init(    oldfs, oldrs, olddol0, pwcat, using_fw, using_fpat)
{
    if (Inited)
        return

    oldfs = FS
    oldrs = RS
    olddol0 = $0
    using_fw = (PROCINFO["FS"] == "FIELDWIDTHS")
    using_fpat = (PROCINFO["FS"] == "FPAT")
    FS = ":"
    RS = "\n"

    pwcat = Awklib "pwcat"
    while ((pwcat | getline) > 0) {
        Byname[$1] = $0
        Byuid[$3] = $0
        Bycount[++Total] = $0
    }
    close(pwcat)
    Count = 0
    Inited = 1
    FS = oldfs
    if (using_fw)
        FIELDWIDTHS = FIELDWIDTHS
    else if (using_fpat)
        FPAT = FPAT
    RS = oldrs
    $0 = olddol0
}

function awk::getpwnam(name)
{
    Init()
    return Byname[name]
}

function awk::getpwuid(uid)
{
    Init()
    return Byuid[uid]
}

function awk::getpwent()
{
    Init()
    if (Count < Total)
        return Bycount[++Count]
    return ""
}

function awk::endpwent()
{
    Count = 0
}
```

As you can see, this version also follows the convention mentioned in Naming Library Function Global Variables, whereby global variable and function names start with a capital letter.

Here is a simple test program. Since it’s in a separate file, unadorned identifiers are sought for in the `awk` namespace:

```
BEGIN {
    while ((p = getpwent()) != "")
        print p
}
```

Here’s what happens when it’s run:

```
$ gawk -f ns_passwd.awk -f testpasswd.awk
-| root:x:0:0:root:/root:/bin/bash
-| daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
-| bin:x:2:2:bin:/bin:/usr/sbin/nologin
-| sys:x:3:3:sys:/dev:/usr/sbin/nologin
...
```

### 15.8 Including A File Without Changing The Namespace

As mentioned at the end of Including Other Files into Your Program, files included with `@include` are treated as if they had ‘@namespace "awk"’ at their beginning. Sometimes, though, this behavior is undesirable.

Consider, for example, the case where you have some significant functions in one namespace:

```
@namespace "mylib"

function major_func1(a, b, c) { ... }
function major_func2(a, b, c) { ... }
...
```

From another namespace, you want to call these functions, frequently:

```
@namespace "myproj1"
function job1(a, b, c) {
    ...
    if (mylib::major_func1(a, b, c))
        ...
    else if (mylib::major_func2(a, b, c))
        ...
    ...
}
... and so on ...
```

Using the ‘mylib::’ prefix everywhere starts to get painful.

You might then try to write some *forwarding functions*, which you would `@include` in each namespace. For example, something like this in a file named mylib_forward.awk:

```
function major_func1(a, b, c)
{
    return mylib::major_func1(a, b, c)
}

function major_func2(a, b, c)
{
    return mylib::major_func2(a, b, c)
}
```

You might then try to `@include` this file in each namespace:

```
@namespace "myproj1"
@include "mylib_forward.awk"

function job1(a, b, c) {
    ...
    if (major_func1(a, b, c))       # calls forwarding function
        ...
    else if (major_func2(a, b, c))  # ditto
        ...
    ...
}
...

@namespace "myproj2"
@include "mylib_forward.awk"
...
```

But this won’t work, since `@include` resets the namespace to ‘awk’.

For this reason, `@nsinclude` was added. It works exactly the same as `@include`, but it does not change the namespace:

```
@namespace "myproj1"
@nsinclude "mylib_forward.awk"

function job1(a, b, c) {
    ...
    if (major_func1(a, b, c))       # calls forwarding function
        ...
    else if (major_func2(a, b, c))  # ditto
        ...
    ...
}
...

@namespace "myproj2"
@nsinclude "mylib_forward.awk"
...
```

This will work the way we want it to.

### 15.9 Namespaces and Other `gawk` Features

This section looks briefly at how the namespace facility interacts with other important `gawk` features.

The profiler and pretty-printer (see Profiling Your `awk` Programs) have been enhanced to understand namespaces and the namespace naming rules presented in Namespace and Component Naming Rules. In particular, the output groups functions in the same namespace together, and has `@namespace` directives in front of rules as necessary. This allows component names to be simple identifiers, instead of using qualified identifiers everywhere.

Interaction with the debugger (see Introduction to the `gawk` Debugger) has not had to change (at least as of this writing). Some of the internal byte codes changed in order to accommodate namespaces, and the debugger’s `dump` command was adjusted to match.

The extension API (see Writing Extensions for `gawk`) has always allowed for placing functions into a different namespace, although this was not previously implemented. However, the symbol lookup and symbol update routines did not have provision for including a namespace. That has now been corrected (see Variable Access and Update by Name). See Enabling In-Place File Editing, for a nice example of an extension that leverages a namespace shared by cooperating `awk` and C code.

### 15.10 Summary

- Standard `awk` provides a single namespace for all global identifiers (scalars, arrays, and functions). This is limiting when one wants to develop libraries of reusable functions or function suites.
- `gawk` provides multiple namespaces by using qualified names: names consisting of a namespace name, a double colon, `::`, and a component name. Namespace names might still possibly conflict, but this is true of any language providing namespaces, modules, or packages.
- The default namespace is `awk`. The rules for namespace and component names are provided in Namespace and Component Naming Rules. The rules are designed in such a way as to make namespace-aware code continue to look and work naturally while still providing the necessary power and flexibility.
- Other parts of `gawk` have been extended as necessary to integrate namespaces smoothly with their operation. This applies most notably to the profiler / pretty-printer (see Profiling Your `awk` Programs) and to the extension facility (see Writing Extensions for `gawk`).
- Overall, the namespace facility was designed and implemented such that backwards compatibility is paramount. Programs that don’t use namespaces should see absolutely no difference in behavior when run by a namespace-capable version of `gawk`.
