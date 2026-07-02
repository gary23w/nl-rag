---
title: "Uncontrolled format string"
source: https://en.wikipedia.org/wiki/Uncontrolled_format_string
domain: stack-canary
license: CC-BY-SA-4.0
tags: stack canary protection, stack buffer overflow defense, buffer overflow protection, stack smashing detection, compiler hardening feature
fetched: 2026-07-02
---

# Uncontrolled format string

**Uncontrolled format string** is a type of code injection vulnerability discovered around 1989 that can be used in security exploits. Originally thought harmless, format string exploits can be used to crash a program or to execute harmful code. The problem stems from the use of unchecked user input as the format string parameter in certain C functions that perform formatting, such as `printf()`. A malicious user may use the `%s` and `%x` format tokens, among others, to print data from the call stack or possibly other locations in memory. One may also write arbitrary data to arbitrary locations using the `%n` format token, which commands `printf()` and similar functions to write the number of bytes formatted to an address stored on the stack.

## Details

A typical exploit uses a combination of these techniques to take control of the instruction pointer (IP) of a process, for example by forcing a program to overwrite the address of a library function or the return address on the stack with a pointer to some malicious shellcode. The padding parameters to format specifiers are used to control the number of bytes output and the `%x` token is used to pop bytes from the stack until the beginning of the format string itself is reached. The start of the format string is crafted to contain the address that the `%n` format token can then overwrite with the address of the malicious code to execute.

This is a common vulnerability because format bugs were previously thought harmless and resulted in vulnerabilities in many common tools. MITRE's CVE project lists roughly 500 vulnerable programs as of June 2007, and a trend analysis ranks it the 9th most-reported vulnerability type between 2001 and 2006.

Format string bugs most commonly appear when a programmer wishes to output a string containing user supplied data (either to a file, to a buffer, or to the user). The programmer may mistakenly write `printf(buffer)` instead of `printf("%s", buffer)`. The first version interprets `buffer` as a format string, and parses any formatting instructions it may contain. The second version simply prints a string to the screen, as the programmer intended. Both versions behave identically in the absence of format specifiers in the string, which makes it easy for the mistake to go unnoticed by the developer.

Format bugs arise because C's argument passing conventions are not type-safe. In particular, the `varargs` mechanism allows functions to accept any number of arguments (e.g. `printf`) by "popping" as many arguments off the call stack as they wish, trusting the early arguments to indicate how many additional arguments are to be popped, and of what types.

Format string bugs can occur in other programming languages besides C, such as Perl, although they appear with less frequency and usually cannot be exploited to execute code of the attacker's choice.

## History

Format bugs were first noted in 1989 by the fuzz testing work done at the University of Wisconsin, which discovered an "interaction effect" in the C shell (csh) between its command history mechanism and an error routine that assumed safe string input.

The use of format string bugs as an attack vector was discovered in September 1999 by Tymm Twillman during a security audit of the ProFTPD daemon. The audit uncovered an `snprintf` that directly passed user-generated data without a format string. Extensive tests with contrived arguments to printf-style functions showed that it was possible to use this for privilege escalation. This led to the first posting in September 1999 on the Bugtraq mailing list regarding this class of vulnerabilities, including a basic exploit. It was still several months, however, before the security community became aware of the full dangers of format string vulnerabilities as exploits for other software using this method began to surface. The first exploits that brought the issue to common awareness (by providing remote root access via code execution) were published simultaneously on the Bugtraq list in June 2000 by Przemysław Frasunek and a person using the nickname *tf8*. They were shortly followed by an explanation, posted by a person using the nickname *lamagra*. "Format bugs" was posted to the Bugtraq list by Pascal Bouchareine in July 2000. The seminal paper "Format String Attacks" by Tim Newsham was published in September 2000 and other detailed technical explanation papers were published in September 2001 such as *Exploiting Format String Vulnerabilities*, by team Teso.

In modern languages such as Java (with `String.format()`), C# (with `String.Format()` or its interpolated strings), and C++ (with `std::format()`), this type of format string attacks is no longer possible, but other format string vulnerabilities may still exist, such as the one that enabled Log4Shell.

## Prevention in compilers

Many compilers can statically check format strings and produce warnings for dangerous or suspect formats. In the GNU Compiler Collection, the relevant compiler flags are, `-Wall`,`-Wformat`, `-Wno-format-extra-args`, `-Wformat-security`, `-Wformat-nonliteral`, and `-Wformat=2`.

Most of these are only useful for detecting bad format strings that are known at compile-time. If the format string may come from the user or from a source external to the application, the application must validate the format string before using it. Care must also be taken if the application generates or selects format strings on the fly. If the GNU C library is used, the `-D_FORTIFY_SOURCE=2` parameter can be used to detect certain types of attacks occurring at run-time. The `-Wformat-nonliteral` check is more stringent.

## Detection

Contrary to many other security issues, the root cause of format string vulnerabilities is relatively easy to detect in x86-compiled executables: For `printf`-family functions, proper use implies a separate argument for the format string and the arguments to be formatted. Faulty uses of such functions can be spotted by simply counting the number of arguments passed to the function; an "argument deficiency" is then a strong indicator that the function was misused.

### Detection in x86-compiled binaries

Counting the number of arguments is often made easy on x86 due to a calling convention where the caller removes the arguments that were pushed onto the stack by adding to the stack pointer after the call, so a simple examination of the stack correction yields the number of arguments passed to the `printf`-family function.'
