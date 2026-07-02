---
title: "Autoconf (part 18/26)"
source: https://www.gnu.org/software/autoconf/manual/autoconf.html
domain: gnu-autotools
license: CC-BY-SA-4.0
tags: gnu autotools, autoconf configure, automake build, build automation
fetched: 2026-07-02
part: 18/26
---

## 13 Portable C and C++ Programming

C and C++ programs often use low-level features of the underlying system, and therefore are often more difficult to make portable to other platforms.

Several standards have been developed to help make your programs more portable. If you write programs with these standards in mind, you can have greater confidence that your programs work on a wide variety of systems. Language Standards Supported by GCC for a list of C-related standards. Many programs also assume the POSIX standard.

The first widely used C variant was K&R C, which predates any C standard. K&R C compilers are no longer of practical interest, though, and Autoconf assumes at least C89, the first C standard, which is sometimes called “C90” due to a delay in standardization. C has since gone through the standards C99, C11, C17, and C23, and Autoconf is compatible with all these standards.

Program portability is a huge topic, and this section can only briefly introduce common pitfalls. See Portability between System Types in *The GNU Coding Standards*, for more information.

### 13.1 Varieties of Unportability

Autoconf tests and ordinary programs often need to test what is allowed on a system, and therefore they may need to deliberately exceed the boundaries of what the standards allow, if only to see whether an optional feature is present. When you write such a program, you should keep in mind the difference between constraints, unspecified behavior, and undefined behavior.

In C, a *constraint* is a rule that the compiler must enforce. An example constraint is that C programs must not declare a bit-field with negative width. Tests can therefore reliably assume that programs with negative-width bit-fields are rejected by a compiler that conforms to the standard.

*Unspecified behavior* is valid behavior, where the standard allows multiple possibilities. For example, the order of evaluation of function arguments is unspecified. Some unspecified behavior is *implementation-defined*, i.e., documented by the implementation, but since Autoconf tests cannot read the documentation they cannot distinguish between implementation-defined and other unspecified behavior. It is common for Autoconf tests to probe implementations to determine otherwise-unspecified behavior.

*Undefined behavior* is invalid behavior, where the standard allows the implementation to do anything it pleases. For example, dereferencing a null pointer leads to undefined behavior. If possible, test programs should avoid undefined behavior, since a program with undefined behavior might succeed on a test that should fail.

The above rules apply to programs that are intended to conform to the standard. However, strictly-conforming programs are quite rare, since the standards are so limiting. A major goal of Autoconf is to support programs that use implementation features not described by the standard, and it is fairly common for test programs to violate the above rules, if the programs work well enough in practice.

### 13.2 Integer Overflow

Although some traditional C programs assume that signed integer overflow wraps around reliably using two’s complement arithmetic, the C standard says that program behavior is undefined on overflow, and these C programs may not work on many modern implementations.

#### 13.2.1 Basics of Integer Overflow

In languages like C, integer overflow wraps around for unsigned integer types that are at least as wide as `unsigned int`; e.g., `UINT_MAX + 1` yields zero. This is guaranteed by the C standard and is portable in practice, unless you specify aggressive, nonstandard optimization options suitable only for special applications.

In contrast, the C standard says that signed integer overflow leads to undefined behavior where a program can do anything, including dumping core or overrunning a buffer. The misbehavior can even precede the overflow. Such an overflow can occur during addition, subtraction, multiplication, division, and left shift. It can even occur for unsigned types like `unsigned short int` that are narrower than `int`, as values of these types are widened to `int` before computation.

Despite this requirement of the standard, some C programs assume that signed integer overflow silently wraps around modulo a power of two, using two’s complement arithmetic, so long as you convert the resulting value to a signed integer type. These programs can have problems, especially when optimization is enabled. If you assume a GCC-like compiler, you can work around the problems by compiling with GCC’s `-fwrapv` option; however, this is not portable.

For historical reasons C17 and earlier also allowed implementations with ones’ complement or signed magnitude arithmetic, but C23 requires two’s complement and it is safe to assume two’s complement nowadays.

Also, overflow can occur when converting an out-of-range value to a signed integer type. Here a standard implementation must define what happens, and this can include raising an exception. Although practical implementations typically wrap around silently in this case, a few debugging implementations trap instead.

#### 13.2.2 Examples of Code Assuming Wraparound Overflow

There was long a tension between what the C standard requires for signed integer overflow, and what traditional C programs commonly assumed. The standard allows aggressive optimizations based on assumptions that overflow never occurs, but traditionally many C programs relied on overflow wrapping around. Although these programs did not conform to the standard, they formerly worked in practice because traditionally compilers did not optimize in such a way that would break the programs. Nowadays, though, compilers do perform these optimizations, so portable programs can no longer assume reliable wraparound on signed integer overflow.

The C Standard says that if a program has signed integer overflow its behavior is undefined, and the undefined behavior can even precede the overflow. To take an extreme example:

```
if (password == expected_password)
  allow_superuser_privileges ();
else if (counter++ == INT_MAX)
  abort ();
else
  printf ("%d password mismatches\n", counter);
```

If the `int` variable `counter` equals `INT_MAX`, `counter++` must overflow and the behavior is undefined, so the C standard allows the compiler to optimize away the test against `INT_MAX` and the `abort` call. Worse, if an earlier bug in the program lets the compiler deduce that `counter == INT_MAX` or that `counter` previously overflowed, the C standard allows the compiler to optimize away the password test and generate code that allows superuser privileges unconditionally.

Here is an example derived from the 7th Edition Unix implementation of `atoi` (1979-01-10):

```
char *p;
int f, n;
...
while (*p >= '0' && *p <= '9')
  n = n * 10 + *p++ - '0';
return (f ? -n : n);
```

Even if the input string is in range, on most modern machines this has signed overflow when computing the most negative integer (the `-n` overflows) or a value near an extreme integer (the `+` overflows).

Here is another example, derived from the 7th Edition implementation of `rand` (1979-01-10). Here the programmer expects both multiplication and addition to wrap on overflow:

```
static long int randx = 1;
...
randx = randx * 1103515245 + 12345;
return (randx >> 16) & 077777;
```

In the following example, derived from the GNU C Library 2.15 implementation of `mktime` (2012-03-21), the code assumes wraparound arithmetic in `+` to detect signed overflow:

```
time_t t, t1, t2;
int sec_requested, sec_adjustment;
...
t1 = t + sec_requested;
t2 = t1 + sec_adjustment;
if (((t1 < t) != (sec_requested < 0))
    | ((t2 < t1) != (sec_adjustment < 0)))
  return -1;
```

Although some of these examples will likely behave as if signed integer overflow wraps around reliably, other examples are likely to misbehave when optimization is enabled. All these examples should be avoided in portable code because signed integer overflow is not reliable on modern systems, and it’s not worth worrying about which of these examples happen to work on most platforms and which do not.

#### 13.2.3 Optimizations That Break Wraparound Arithmetic

Compilers sometimes generate code that is incompatible with wraparound integer arithmetic. A simple example is an algebraic simplification: a compiler might translate `(i * 2000) / 1000` to `i * 2` because it assumes that `i * 2000` does not overflow. The translation is not equivalent to the original when overflow occurs: e.g., in the typical case of 32-bit signed two’s complement wraparound `int`, if `i` has type `int` and value `1073742`, the original expression returns −2147483 but the optimized version returns the mathematically correct value 2147484.

More subtly, loop induction optimizations often exploit the undefined behavior of signed overflow. Consider the following contrived function `sumc`:

```
int
sumc (int lo, int hi)
{
  int sum = 0;
  for (int i = lo; i <= hi; i++)
    sum ^= i * 53;
  return sum;
}
```

To avoid multiplying by 53 each time through the loop, an optimizing compiler might internally transform `sumc` to the equivalent of the following:

```
int
transformed_sumc (int lo, int hi)
{
  int sum = 0;
  int hic = hi * 53;
  for (int ic = lo * 53; ic <= hic; ic += 53)
    sum ^= ic;
  return sum;
}
```

This transformation is allowed by the C standard, but it is invalid for wraparound arithmetic when `INT_MAX / 53 < hi`, because then the overflow in computing expressions like `hi * 53` can cause the expression `i <= hi` to yield a different value from the transformed expression `ic <= hic`.

For this reason, compilers that use loop induction and similar techniques often do not support reliable wraparound arithmetic when a loop induction variable like `ic` is involved. Since loop induction variables are generated by the compiler, and are not visible in the source code, it is not always trivial to say whether the problem affects your code.

Hardly any code actually depends on wraparound arithmetic in cases like these, so in practice these loop induction optimizations are almost always useful. However, edge cases in this area can cause problems. For example:

```
for (int j = 1; 0 < j; j *= 2)
  test (j);
```

Here, the loop attempts to iterate through all powers of 2 that `int` can represent, but the C standard allows a compiler to optimize away the comparison and generate an infinite loop, under the argument that behavior is undefined on overflow. As of this writing this optimization is done on some platforms by GCC with -O2, so this code is not portable in practice.

#### 13.2.4 Practical Advice for Signed Overflow Issues

Ideally the safest approach is to avoid signed integer overflow entirely. For example, instead of multiplying two signed integers, you can convert them to double-width integers, multiply the wider values, then test whether the result is in the narrower range. Or you can use more-complicated code employing unsigned integers of the same width.

Rewriting code in this way will be inconvenient, though, especially if the signed values might be negative and no wider type is available. Using unsigned arithmetic to check for overflow is particularly painful to do portably and efficiently when dealing with an integer type like `uid_t` whose width and signedness vary from platform to platform. Also, this approach may hurt performance.

Hence it is often useful to maintain code that needs wraparound on overflow, instead of rewriting the code. The rest of this section attempts to give practical advice for this situation.

To detect integer overflow portably when attempting operations like `sum = a + b`, you can use the C23 `<stdckdint.h>` macros `ckd_add`, `ckd_sub`, and `ckd_mul`. The following code adds two integers with overflow wrapping around reliably in the sum:

```
#include <stdckdint.h>
...
/* Set sum = a + b, with wraparound.  */
if (ckd_add (&sum, a, b))
  /* 'sum' has just the low order bits.  */;
else
  /* 'sum' is the correct answer.  */;
```

To be portable to pre-C23 platforms you can use Gnulib’s `stdckdint` module, which emulates this part of C23 (see Gnulib). Invoking the `stdckdint` macros typically costs just one machine instruction for the arithmetic and another instruction for the rare branch on overflow.

If your code uses a signed loop index, make sure that the index cannot overflow, along with all signed expressions derived from the index. Here is a contrived example of problematic code with two instances of overflow.

```
for (int i = INT_MAX - 10; i <= INT_MAX; i++)
  if (i + 1 < 0)
    {
      report_overflow ();
      break;
    }
```

Because of the two overflows, a compiler might optimize away or transform the two comparisons in a way that is incompatible with the wraparound assumption.

If your code is intended to be compiled only by GCC and assumes wraparound behavior, and you want to insulate it against any GCC optimizations that would fail to support that behavior, you should use GCC’s -fwrapv option, which causes signed overflow to wrap around reliably (except for division and remainder, as discussed in the next section).

If you need to write portable code and therefore cannot assume that signed integer overflow wraps around reliably, you should consider debugging with a GCC option that causes signed overflow to raise an exception. These options include -fsanitize=undefined and -ftrapv.

#### 13.2.5 Signed Integer Division and Integer Overflow

Overflow in signed integer division is not always harmless: for example, on CPUs of the i386 family, dividing `INT_MIN` by `-1` yields a SIGFPE signal which by default terminates the program. Worse, taking the remainder of these two values typically yields the same signal on these CPUs, behavior that the C standard allows.

### 13.3 Preprocessor Arithmetic

In C99 and later, preprocessor arithmetic, used for `#if` expressions, must be evaluated as if all signed values are of type `intmax_t` and all unsigned values of type `uintmax_t`. Many compilers are buggy in this area, though. For example, as of 2007, Sun C mishandles `#if LLONG_MIN < 0` on a platform with 32-bit `long int` and 64-bit `long long int`. Also, some older preprocessors mishandle constants ending in `LL`. To work around these problems, you can compute the value of expressions like `LONG_MAX < LLONG_MAX` at `configure`-time rather than at `#if`-time.

### 13.4 Properties of Null Pointers

Most modern hosts reliably fail when you attempt to dereference a null pointer.

On almost all modern hosts, null pointers use an all-bits-zero internal representation, so you can reliably use `memset` with 0 to set all the pointers in an array to null values.

If `p` is a null pointer to an object type, the C expression `p + 0` always evaluates to `p` on modern hosts, even though the standard says that it has undefined behavior.

### 13.5 Buffer Overruns and Subscript Errors

Buffer overruns and subscript errors are the most common dangerous errors in C programs. They result in undefined behavior because storing outside an array typically modifies storage that is used by some other object, and most modern systems lack runtime checks to catch these errors. Programs should not rely on buffer overruns being caught.

There is one exception to the usual rule that a portable program cannot address outside an array. In C, it is valid to compute the address just past an object, e.g., `&a[N]` where `a` has `N` elements, so long as you do not dereference the resulting pointer. But it is not valid to compute the address just before an object, e.g., `&a[-1]`; nor is it valid to compute two past the end, e.g., `&a[N+1]`. On most platforms `&a[-1] < &a[0] && &a[N] < &a[N+1]`, but this is not reliable in general, and it is usually easy enough to avoid the potential portability problem, e.g., by allocating an extra unused array element at the start or end.

Valgrind can catch many overruns. GCC users might also consider using the -fsanitize= options to catch overruns. See Program Instrumentation Options in *Using the GNU Compiler Collection (GCC)*.

Buffer overruns are usually caused by off-by-one errors, but there are more subtle ways to get them.

Using `int` values to index into an array or compute array sizes causes problems on typical 64-bit hosts where an array index might be *2^{31}* or larger. Index values of type `size_t` avoid this problem, but cannot be negative. Index values of type `ptrdiff_t` are signed, and are wide enough in practice.

If you add or multiply two numbers to calculate an array size, e.g., `malloc (x * sizeof y + z)`, havoc ensues if the addition or multiplication overflows.

Many implementations of the `alloca` function silently misbehave and can generate buffer overflows if given sizes that are too large. The size limits are implementation dependent, but are at least 4000 bytes on all platforms that we know about.

The standard functions `asctime`, `asctime_r`, `ctime`, `ctime_r`, and `gets` are prone to buffer overflows, and portable code should not use them unless the inputs are known to be within certain limits. The time-related functions can overflow their buffers if given timestamps out of range (e.g., a year less than -999 or greater than 9999). Time-related buffer overflows cannot happen with recent-enough versions of the GNU C library, but are possible with other implementations. The `gets` function is the worst, since it almost invariably overflows its buffer when presented with an input line larger than the buffer.

### 13.6 Volatile Objects

The keyword `volatile` is often misunderstood in portable code. Its use inhibits some memory-access optimizations, but programmers often wish that it had a different meaning than it actually does.

`volatile` was designed for code that accesses special objects like memory-mapped device registers whose contents spontaneously change. Such code is inherently low-level, and it is difficult to specify portably what `volatile` means in these cases. The C standard says, “What constitutes an access to an object that has volatile-qualified type is implementation-defined,” so in theory each implementation is supposed to fill in the gap by documenting what `volatile` means for that implementation. In practice, though, this documentation is usually absent or incomplete.

One area of confusion is the distinction between objects defined with volatile types, and volatile lvalues. From the C standard’s point of view, an object defined with a volatile type has externally visible behavior. You can think of such objects as having little oscilloscope probes attached to them, so that the user can observe some properties of accesses to them, just as the user can observe data written to output files. However, accesses via volatile lvalues to ordinary objects are merely side effects (i.e., changes to the state of the execution environment), and the implementation is not required to document their visibility any further. For example:

```
/* Declare and access a volatile object.
   Accesses to X are "visible" to users.  */
static int volatile x;
x = 1;

/* Access two ordinary objects via a volatile lvalue.
   Although each read and write is a side effect,
   the accesses are not directly "visible" to users.  */
int y = 0;
int *z = malloc (sizeof *z);
*z = 7;
int volatile *p;
p = &y;
*p = *p + 1;
p = z;
*p = *p + 1;
```

Programmers often wish that `volatile` meant “Perform the memory access here and now, without merging several memory accesses, without changing the memory word size, and without reordering.” But the C standard does not require this. For objects defined with a volatile type, accesses must be done before the next sequence point; but otherwise merging, reordering, and word-size change is allowed.

Even when accessing objects defined with a volatile type, the C standard allows only extremely limited signal handlers: in C23 the behavior is undefined if a signal handler refers to any non-local object that is not a lock-free atomic object and that is not `constexpr` (other than by writing to a `sig_atomic_t volatile` object), or calls any standard library function other than from a small set that includes `abort`, `_Exit`, `quick_exit`, some `<stdatomic.h>` functions, and `signal`. Hence C compilers need not worry about a signal handler disturbing ordinary computation. POSIX allows some additional behavior in a portable signal handler, but is still quite restrictive. See When is a Volatile Object Accessed? in *Using the GNU Compiler Collection (GCC)*, for some restrictions imposed by GCC. See Defining Signal Handlers in *The GNU C Library*, for some restrictions imposed by the GNU C library. Restrictions differ on other platforms.

If possible, it is best to use a signal handler that fits within the limits imposed by the C and POSIX standards.

If this is not practical, you can try the following rules of thumb. A signal handler should access only volatile lvalues, preferably lvalues that refer to objects defined with a volatile type, and should not assume that the accessed objects have an internally consistent state if they are larger than a machine word. Furthermore, installers should employ compilers and compiler options that are commonly used for building operating system kernels, because kernels often need more from `volatile` than the C Standard requires, and installers who compile an application in a similar environment can sometimes benefit from the extra constraints imposed by kernels on compilers. Admittedly we are hand-waving somewhat here, as there are few guarantees in this area; the rules of thumb may help to fix some bugs but there is a good chance that they will not fix them all.

For `volatile`, C++ has the same problems that C does. Multithreaded applications have even more problems with `volatile`, but they are beyond the scope of this section.

The bottom line is that using `volatile` typically hurts performance but should not hurt correctness. In some cases its use does help correctness, but these cases are often so poorly understood that all too often adding `volatile` to a data structure merely alleviates some symptoms of a bug while not fixing the bug in general.

### 13.7 Floating Point Portability

Almost all modern systems use IEEE-754 floating point, and it is safe to assume IEEE-754 in most portable code these days. For more information, please see David Goldberg’s classic paper What Every Computer Scientist Should Know About Floating-Point Arithmetic.

### 13.8 Exiting Portably

A C or C++ program can exit with status *N* by returning *N* from the `main` function. Portable programs are supposed to exit either with status 0 or `EXIT_SUCCESS` to succeed, or with status `EXIT_FAILURE` to fail, but in practice it is portable to fail by exiting with status 1, and test programs that assume POSIX can fail by exiting with status values from 1 through 255.

A program can also exit with status *N* by passing *N* to the `exit` function, and a program can fail by calling the `abort` function. If a program is specialized to just some platforms, it can fail by calling functions specific to those platforms, e.g., `_exit` (POSIX). However, like other functions, an exit function should be declared, typically by including a header. For example, if a C program calls `exit`, it should include stdlib.h either directly or via the default includes (see Default Includes).

A program can fail due to undefined behavior such as dereferencing a null pointer, but this is not recommended as undefined behavior allows an implementation to do whatever it pleases and this includes exiting successfully.


## 14 Manual Configuration

A few kinds of features can’t be guessed automatically by running test programs. For example, the details of the object-file format, or special options that need to be passed to the compiler or linker. Autoconf provides a uniform method for handling unguessable features, by giving each operating system a *canonical system type*, also known as a *canonical name* or *target triplet*.

If you use any of the macros described in this chapter, you must distribute the helper scripts `config.guess` and `config.sub` along with your source code. Some Autoconf macros use these macros internally, so you may need to distribute these scripts even if you do not use any of these macros yourself. See Configure Input: Source Code, Macros, and Auxiliary Files, for information about the `AC_CONFIG_AUX_DIR` macro which you can use to control in which directory `configure` looks for helper scripts, and where to get the scripts from.

### 14.1 Specifying target triplets

Autoconf-generated `configure` scripts can make decisions based on a canonical name for the system type, or *target triplet*, which has the form: ‘*cpu*-*vendor*-*os*’, where *os* can be ‘*system*’ or ‘*kernel*-*system*’

`configure` can usually guess the canonical name for the type of system it’s running on. To do so it runs a script called `config.guess`, which infers the name using the `uname` command or symbols predefined by the C preprocessor.

Alternately, the user can specify the system type with command line arguments to `configure` (see Specifying a System Type. Doing so is necessary when cross-compiling. In the most complex case of cross-compiling, three system types are involved. The options to specify them are:

**--build=*build-type***

the type of system on which the package is being configured and compiled. It defaults to the result of running `config.guess`. Specifying a *build-type* that differs from *host-type* enables cross-compilation mode.

**--host=*host-type***

the type of system on which the package runs. By default it is the same as the build machine. The tools that get used to build and manipulate binaries will, by default, all be prefixed with `*host-type*-`, such as `*host-type*-gcc`, `*host-type*-g++`, `*host-type*-ar`, and `*host-type*-nm`. If the binaries produced by these tools can be executed by the build system, the configure script will make use of it in `AC_RUN_IFELSE` invocations; otherwise, cross-compilation mode is enabled. Specifying a *host-type* that differs from *build-type*, when *build-type* was also explicitly specified, equally enables cross-compilation mode.

**--target=*target-type***

the type of system for which any compiler tools in the package produce code (rarely needed). By default, it is the same as host.

If you mean to override the result of `config.guess` but still produce binaries for the build machine, use --build, not --host.

So, for example, to produce binaries for 64-bit MinGW, use a command like this:

```
./configure --host=x86_64-w64-mingw64
```

If your system has the ability to execute MinGW binaries but you don’t want to make use of this feature and instead prefer cross-compilation guesses, use a command like this:

```
./configure --build=x86_64-pc-linux-gnu --host=x86_64-w64-mingw64
```

Note that if you do not specify --host, `configure` fails if it can’t run the code generated by the specified compiler. For example, configuring as follows fails:

```
./configure CC=x86_64-w64-mingw64-gcc
```

When cross-compiling, `configure` will warn about any tools (compilers, linkers, assemblers) whose name is not prefixed with the host type. This is an aid to users performing cross-compilation. Continuing the example above, if a cross-compiler named `cc` is used with a native `pkg-config`, then libraries found by `pkg-config` will likely cause subtle build failures; but using the names `x86_64-w64-mingw64-gcc` and `x86_64-w64-mingw64-pkg-config` avoids any confusion. Avoiding the warning is as simple as creating the correct symlinks naming the cross tools.

`configure` recognizes short aliases for some system types; for example, ‘mingw64’ can be used instead of ‘x86_64-pc-mingw64’. `configure` runs a script called `config.sub` to canonicalize system type aliases.

This section deliberately omits the description of the obsolete interface; see Hosts and Cross-Compilation.

### 14.2 Getting the Canonical System Type

The following macros make the system type available to `configure` scripts.

The variables ‘build_alias’, ‘host_alias’, and ‘target_alias’ are always exactly the arguments of --build, --host, and --target; in particular, they are left empty if the user did not use them, even if the corresponding `AC_CANONICAL` macro was run. Any configure script may use these variables anywhere. These are the variables that should be used when in interaction with the user.

If you need to recognize some special environments based on their system type, run the following macros to get canonical system names. These variables are not set before the macro call.

**Macro: **AC_CANONICAL_BUILD** ¶**

Compute the canonical build-system type variable, `build`, and its three individual parts `build_cpu`, `build_vendor`, and `build_os`.

If --build was specified, then `build` is the canonicalization of `build_alias` by `config.sub`, otherwise it is determined by the shell script `config.guess`.

**Macro: **AC_CANONICAL_HOST** ¶**

Compute the canonical host-system type variable, `host`, and its three individual parts `host_cpu`, `host_vendor`, and `host_os`.

If --host was specified, then `host` is the canonicalization of `host_alias` by `config.sub`, otherwise it defaults to `build`.

**Macro: **AC_CANONICAL_TARGET** ¶**

Compute the canonical target-system type variable, `target`, and its three individual parts `target_cpu`, `target_vendor`, and `target_os`.

If --target was specified, then `target` is the canonicalization of `target_alias` by `config.sub`, otherwise it defaults to `host`.

Note that there can be artifacts due to the backward compatibility code. See Hosts and Cross-Compilation, for more.

### 14.3 Using the System Type

In configure.ac the system type is generally used by one or more `case` statements to select system-specifics. Shell wildcards can be used to match a group of system types.

For example, an extra assembler code object file could be chosen, giving access to a CPU cycle counter register. `$(CYCLE_OBJ)` in the following would be used in a makefile to add the object to a program or library.

```
AS_CASE([$host],
  [aarch64*-*-*], [CYCLE_OBJ=pmccntr.o],
  [i?86-*-*],     [CYCLE_OBJ=rdtsc.o],
  [CYCLE_OBJ=""])
AC_SUBST([CYCLE_OBJ])
```

`AC_CONFIG_LINKS` (see Creating Configuration Links) is another good way to select variant source files, for example optimized code for some CPUs. The configured CPU type doesn’t always indicate exact CPU types, so some runtime capability checks may be necessary too.

```
AS_CASE([$host],
  [aarch64*-*-*], [AC_CONFIG_LINKS([dither.c:aarch64/dither.c])],
  [powerpc*-*-*], [AC_CONFIG_LINKS([dither.c:powerpc/dither.c])],
  [AC_CONFIG_LINKS([dither.c:generic/dither.c])])
```

The host system type can also be used to find cross-compilation tools with `AC_CHECK_TOOL` (see Generic Program and File Checks).

The above examples all show ‘$host’, since this is where the code is going to run. Only rarely is it necessary to test ‘$build’ (which is where the build is being done).

Whenever you’re tempted to use ‘$host’ it’s worth considering whether some sort of probe would be better. New system types come along periodically or previously missing features are added. Well-written probes can adapt themselves to such things, but hard-coded lists of names can’t. Here are some guidelines,

- Availability of libraries and library functions should always be checked by probing.
- Variant behavior of system calls is best identified with runtime tests if possible, but bug workarounds or obscure difficulties might have to be driven from ‘$host’.
- Assembler code is inevitably highly CPU-specific and is best selected according to ‘$host_cpu’.
- Assembler variations like underscore prefix on globals or ELF versus COFF type directives are however best determined by probing, perhaps even examining the compiler output.

‘$target’ is for use by a package creating a compiler or similar. For ordinary packages it’s meaningless and should not be used. It indicates what the created compiler should generate code for, if it can cross-compile. ‘$target’ generally selects various hard-coded CPU and system conventions, since usually the compiler or tools under construction themselves determine how the target works.
