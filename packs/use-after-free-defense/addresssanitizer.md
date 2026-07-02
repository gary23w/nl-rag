---
title: "Code sanitizer"
source: https://en.wikipedia.org/wiki/AddressSanitizer
domain: use-after-free-defense
license: CC-BY-SA-4.0
tags: use after free defense, dangling pointer mitigation, temporal memory safety, quarantine allocator hardening
fetched: 2026-07-02
---

# Code sanitizer

(Redirected from

AddressSanitizer

)

A **code sanitizer** is a programming tool that detects bugs in the form of undefined or suspicious behavior by a compiler inserting instrumentation code at runtime. Sanitizers have evolved over several decades to detect memory errors in unsafe programming languages, beginning with early pointer and array access checks in 1994 and type-safe retrofitting in 2005, followed by a significant expansion into sophisticated spatial and temporal memory safety tools between 2009 and 2019. As of 2024, the most popular sanitizer is ASan, originally designed by Google. It is integrated into most mainstream compilers due to its relatively small memory and performance overhead.

## AddressSanitizer

Google's ASan, introduced in 2012, uses a shadow memory scheme to detect memory bugs. It is available in:

- Clang (starting from version 3.1)
- GCC (starting from version 4.8)
- Xcode (starting from version 7.0)
- MSVC (widely available starting from version 16.9).

The original design of the sanitizer increases processing time by about 73% and memory usage by 240%. There is a hardware-accelerated ASan called HWAsan available for AArch64 and (in a limited fashion) x86_64.

AddressSanitizer does not detect any uninitialized memory reads (but this is detected by MemorySanitizer), and detects only some use-after-return bugs. It is also not capable of detecting all arbitrary memory corruption bugs, nor all arbitrary write bugs due to integer underflow/overflows (when the integer with undefined behavior is used to calculate memory address offsets). Adjacent buffers in structs and classes are not protected from overflow, in part to prevent breaking backwards compatibility.

### KernelAddressSanitizer

The **KernelAddressSanitizer** (**KASan**) detects dynamic memory errors in the Linux kernel. Kernel instrumentation requires a special feature in the compiler supplying the -fsanitize=kernel-address command line option, since kernels do not use the same address space as normal programs.

KASan is also available for use with Windows kernel drivers beginning in Windows 11 22H2 and above. Similarly to Linux, compiling a Windows driver with KASAN requires passing the /fsanitize=kernel-address command line option to the MSVC compiler.

## Other sanitizers

Google also produced **LeakSanitizer** (LSan, memory leaks), **ThreadSanitizer** (TSan, data races and deadlocks), **MemorySanitizer** (MSan, uninitialized memory), and **UndefinedBehaviorSanitizer** (**UBSan**, undefined behaviors, with fine-grained control). These tools are generally available in Clang/LLVM and GCC. Similar to KASan, there are kernel-specific versions of LSan, MSan, TSan, as well as completely original kernel sanitizers such as KFENCE and KCSan.

Additional sanitizer tools (grouped by compilers under -fsanitize or a similar flag) include:

- LLVM control-flow integrity and its kernel counterpart, which checks virtual tables and type casts for forward-edge CFI
- MemTagSanitizer, an ASan-like tool that uses Armv8.5-A features for very low overhead
- ShadowCallStack, an AArch64 tool that provides a shadow stack protection
- Scudo Hardened Allocator, an alternative memory allocator that includes GWP-ASan, a probabilistic ASan analogue with low overhead
- libFuzzer, an LLVM tool that adds code coverage to fuzzing

## Usage

A code sanitizer detects suspicious behavior as the program runs. One common way to use a sanitizer is to combine it with fuzzing, which generates inputs likely to trigger bugs.

## Users

Chromium and Firefox developers are active users of AddressSanitizer; the tool has found hundreds of bugs in these web browsers. A number of bugs were found in FFmpeg and FreeType. The Linux kernel has enabled the AddressSanitizer for the x86-64 architecture as of Linux version 4.0.

## Examples

### ASan: Heap-use-after-free

```mw
// To compile: g++ -O -g -fsanitize=address heap-use-after-free.cc
int main(int argc, char **argv) {
  int *array = new int[100];
  delete [] array;
  return array[argc];  // BOOM
}
```

```
$ ./a.out
==5587==ERROR: AddressSanitizer: heap-use-after-free on address 0x61400000fe44 at pc 0x47b55f bp 0x7ffc36b28200 sp 0x7ffc36b281f8
READ of size 4 at 0x61400000fe44 thread T0
    #0 0x47b55e in main /home/test/example_UseAfterFree.cc:5
    #1 0x7f15cfe71b14 in __libc_start_main (/lib64/libc.so.6+0x21b14)
    #2 0x47b44c in _start (/root/a.out+0x47b44c)

0x61400000fe44 is located 4 bytes inside of 400-byte region [0x61400000fe40,0x61400000ffd0)
freed by thread T0 here:
    #0 0x465da9 in operator delete[](void*) (/root/a.out+0x465da9)
    #1 0x47b529 in main /home/test/example_UseAfterFree.cc:4

previously allocated by thread T0 here:
    #0 0x465aa9 in operator new[](unsigned long) (/root/a.out+0x465aa9)
    #1 0x47b51e in main /home/test/example_UseAfterFree.cc:3

SUMMARY: AddressSanitizer: heap-use-after-free /home/test/example_UseAfterFree.cc:5 main
Shadow bytes around the buggy address:
  [...]
  0x0c287fff9fb0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
=>0x0c287fff9fc0: fa fa fa fa fa fa fa fa[fd]fd fd fd fd fd fd fd
  0x0c287fff9fd0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  [...]
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:     fa
  Heap right redzone:    fb
  Freed heap region:     fd
  Stack left redzone:    f1
  Stack mid redzone:     f2
  Stack right redzone:   f3
  Stack partial redzone: f4
  Stack after return:    f5
  Stack use after scope: f8
  Global redzone:        f9
  Global init order:     f6
  Poisoned by user:      f7
  ASan internal:         fe
==5587==ABORTING
```

### ASan: Heap-buffer-overflow

```mw
// RUN: clang++ -O -g -fsanitize=address heap-buf-of.cc && ./a.out
int main(int argc, char **argv) {
  int *array = new int[100];
  array[0] = 0;
  int res = array[argc + 100];  // BOOM
  delete [] array;
  return res;
}
```

```
==25372==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61400000ffd4 at pc 0x0000004ddb59 bp 0x7fffea6005a0 sp 0x7fffea600598
READ of size 4 at 0x61400000ffd4 thread T0
    #0 0x46bfee in main /tmp/main.cpp:4:13

0x61400000ffd4 is located 4 bytes to the right of 400-byte region [0x61400000fe40,0x61400000ffd0)
allocated by thread T0 here:
    #0 0x4536e1 in operator delete[](void*)
    #1 0x46bfb9 in main /tmp/main.cpp:2:16
```

### ASan: Stack-buffer-overflow

```mw
// RUN: clang -O -g -fsanitize=address stack-buf-of.cc && ./a.out
int main(int argc, char **argv) {
  int stack_array[100];
  stack_array[1] = 0;
  return stack_array[argc + 100];  // BOOM
}
```

```
==7405==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7fff64740634 at pc 0x46c103 bp 0x7fff64740470 sp 0x7fff64740468
READ of size 4 at 0x7fff64740634 thread T0
    #0 0x46c102 in main /tmp/example_StackOutOfBounds.cc:5

Address 0x7fff64740634 is located in stack of thread T0 at offset 436 in frame
    #0 0x46bfaf in main /tmp/example_StackOutOfBounds.cc:2

  This frame has 1 object(s):
    [32, 432) 'stack_array' <== Memory access at offset 436 overflows this variable
```

### ASan: Global-buffer-overflow

```mw
// RUN: clang -O -g -fsanitize=address global-buf-of.cc && ./a.out
int global_array[100] = {-1};
int main(int argc, char **argv) {
  return global_array[argc + 100];  // BOOM
}
```

```
==7455==ERROR: AddressSanitizer: global-buffer-overflow on address 0x000000689b54 at pc 0x46bfd8 bp 0x7fff515e5ba0 sp 0x7fff515e5b98
READ of size 4 at 0x000000689b54 thread T0
    #0 0x46bfd7 in main /tmp/example_GlobalOutOfBounds.cc:4

0x000000689b54 is located 4 bytes to the right of 
  global variable 'global_array' from 'example_GlobalOutOfBounds.cc' (0x6899c0) of size 400
```

### UBSan: nullptr-dereference

```mw
// RUN: g++ -O -g -fsanitize=null null-dereference.c && ./a.out
int main(int argc, char **argv) {
  const char * ptr = nullptr;
  return *ptr;  // BOOM
}
```

```
null-dereference.c:4:10: runtime error: load of null pointer of type 'const char'
Segmentation fault (core dumped)
```
