---
title: "Tagged pointer"
source: https://en.wikipedia.org/wiki/Tagged_pointer
domain: memory-tagging-extension
license: CC-BY-SA-4.0
tags: memory tagging extension, hardware memory tagging, tagged pointer safety, lock and key memory model
fetched: 2026-07-02
---

# Tagged pointer

In computer science, a **tagged pointer** is a pointer (concretely a memory address) with additional data associated with it, such as an indirection bit or reference count. This additional data is often "folded" into the pointer, meaning stored inline in the data representing the address, taking advantage of certain properties of memory addressing. The name comes from "tagged architecture" systems, which reserved bits at the hardware level to indicate the significance of each word; the additional data is called a "tag" or "tags", though strictly speaking "tag" refers to data specifying a *type,* not other data; however, the usage "tagged pointer" is ubiquitous.

## Folding tags into the pointer

There are various techniques for folding tags into a pointer.

Most architectures are byte-addressable (the smallest addressable unit is a byte), but certain types of data will often be *aligned* to the size of the data, often a word or multiple thereof. This discrepancy leaves a few of the least significant bits of the pointer unused, which can be used for tags – most often as a bit field (each bit a separate tag) – as long as code that uses the pointer masks out these bits before accessing memory. E.g., on a 32-bit architecture (for both addresses and word size), a word is 32 bits = 4 bytes, so word-aligned addresses are always a multiple of 4, hence end in 00, leaving the last 2 bits available; while on a 64-bit architecture, a word is 64 bits = 8 bytes, so word-aligned addresses end in 000, leaving the last 3 bits available. In cases where data is aligned at a multiple of word size, further bits are available. In case of word-addressable architectures, word-aligned data does not leave any bits available, as there is no discrepancy between alignment and addressing, but data aligned at a multiple of word size does.

Conversely, in some operating systems, virtual addresses are narrower than the overall architecture width, which leaves the most significant bits available for tags; this can be combined with the previous technique in case of aligned addresses. This is particularly the case on 64-bit architectures, as 64 bits of address space are far above the data requirements of all but the largest applications, and thus many practical 64-bit processors have narrower addresses. Note that the virtual address width may be narrower than the physical address width, which in turn may be narrower than the architecture width; for tagging of pointers in user space, the virtual address space provided by the operating system (in turn provided by the memory management unit) is the relevant width. In fact, some processors specifically forbid use of such tagged pointers at the processor level, notably x86-64, which requires the use of canonical form addresses by the operating system, with most significant bits all 0s or all 1s.

Lastly, the virtual memory system in most modern operating systems reserves a block of logical memory around address 0 as unusable. This means that, for example, a pointer to 0 is never a valid pointer and can be used as a special null pointer value. Unlike the previously mentioned techniques, this only allows a single special pointer value, not extra data for pointers generally.

## History

One of the earliest examples of hardware support for tagged pointers in a commercial platform was the IBM System/38. IBM later added tagged pointer support to the PowerPC architecture to support the IBM i operating system, which is an evolution of the System/38 platform.

A significant example of the use of tagged pointers is the Objective-C runtime on iOS 7 on ARM64, notably used on the iPhone 5S. In iOS 7, virtual addresses only contain 33 bits of address information but are 64-bits long leaving 31 bits for tags. Objective-C class pointers are 8-byte aligned freeing up an additional 3 bits of address space, and the tag fields are used for many purposes, such as storing a reference count and whether the object has a destructor.

Early versions of macOS used tagged addresses called Handles to store references to data objects. The high bits of the address indicated whether the data object was locked, purgeable, and/or originated from a resource file, respectively. This caused compatibility problems, when macOS addressing advanced from 24 bits to 32 bits in System 7.

## Null versus aligned pointer

Use of zero to represent a null pointer is extremely common, with many programming languages (such as Ada) explicitly relying on this behavior. In theory, other values in an operating system-reserved block of logical memory could be used to tag conditions other than a null pointer, but these uses appear to be rare, perhaps because they are at best non-portable. It is generally accepted practice in software design that if a special pointer value distinct from null (such as a sentinel in certain data structures) is needed, the programmer should explicitly provide for it.

Taking advantage of the alignment of pointers provides more flexibility than null pointers/sentinels because it allows pointers to be tagged with information about the type of data pointed to, conditions under which it may be accessed, or other similar information about the pointer's use. This information can be provided along with every valid pointer. In contrast, null pointers/sentinels provide only a finite number of tagged values distinct from valid pointers.

In a tagged architecture, a number of bits in every word of memory are reserved to act as a tag. Tagged architectures, such as the Lisp machines, often have hardware support for interpreting and processing tagged pointers.

GNU libc `malloc()` provides 8-byte aligned memory addresses for 32-bit platforms, and 16-byte alignment for 64-bit platforms. Larger alignment values can be obtained with `posix_memalign()`.

## Examples

### Example 1

In the following C code, the value of zero is used to indicate a null pointer:

```mw
void optionally_return_a_value (int* optional_return_value_pointer) {
  /* ... */
  int value_to_return = 1;

  /* is it non-NULL? (note that NULL, logical false, and zero compare equally in C) */
  if (optional_return_value_pointer)
    /* if so, use it to pass a value to the calling function */
    *optional_return_value_pointer = value_to_return;

  /* otherwise, the pointer is never dereferenced */
}
```

### Example 2

Here, the programmer has provided a global variable, whose address is then used as a sentinel:

```mw
#define SENTINEL &sentinel_s

node_t sentinel_s;

void do_something_to_a_node (node_t * p) {
  if (NULL == p)
    /* do something */
  else if (SENTINEL == p)
    /* do something else */
  else
    /* treat p as a valid pointer to a node */
}
```

### Example 3

Assume we have a data structure `table_entry` that is always aligned to a 16 byte boundary. In other words, the least significant 4 bits of a table entry's address are always 0 (24 = 16). We could use these 4 bits to mark the table entry with extra information. For example, bit 0 might mean read only, bit 1 might mean dirty (the table entry needs to be updated), and so on.

If pointers are 16-bit values, then:

- `0x3421` is a read-only pointer to the `table_entry` at address `0x3420`
- `0xf472` is a pointer to a dirty `table_entry` at address `0xf470`

## Advantages

The major advantage of tagged pointers is that they take up less space than a pointer along with a separate tag field. This can be especially important when a pointer is a return value from a function. It can also be important in large tables of pointers.

A more subtle advantage is that by storing a tag in the same place as the pointer, it is often possible to guarantee the atomicity of an operation that updates both the pointer and its tag without external synchronization mechanisms. This can be an extremely large performance gain, especially in operating systems.

## Disadvantages

Tagged pointers have some of the same difficulties as xor linked lists, although to a lesser extent. For example, not all debuggers will be able to properly follow tagged pointers; however, this is not an issue for a debugger that is designed with tagged pointers in mind.

The use of zero to represent a null pointer does not suffer from these disadvantages: it is pervasive, most programming languages treat zero as a special null value, and it has thoroughly proven its robustness. An exception is the way that zero participates in overload resolution in C++, where zero is treated as an integer rather than a pointer; for this reason the special value nullptr is preferred over the integer zero. However, with tagged pointers zeros are usually not used to represent null pointers.
