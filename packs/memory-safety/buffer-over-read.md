---
title: "Out-of-bounds read"
source: https://en.wikipedia.org/wiki/Buffer_over-read
domain: memory-safety
license: CC-BY-SA-4.0
tags: memory safety, spatial memory safety, temporal memory safety, memory safe language
fetched: 2026-07-02
---

# Out-of-bounds read

(Redirected from

Buffer over-read

)

In computer security and programming, an **out-of-bounds read** is a software anomaly where a program, while reading data from a buffer, reads outside of the buffer's boundary from adjacent memory. This is a special case of violation of memory safety and is a form of data confidentiality violation (see CIA triad). A **buffer over-read** and **buffer under-read** are special cases of out-of-bounds reads.

Out-of-bounds reads are the basis of many software vulnerabilities. In some cases, they can be maliciously exploited to access privileged information. For example, they can sometimes be triggered, as in the Heartbleed bug, by maliciously crafted inputs that are designed to exploit a lack of bounds checking to read inaccessible parts of memory.

At other times, out-of-bounds reads can result in other erratic program behavior, including memory access errors (including invalid page faults), incorrect results, or crashes. For example, the widespread IT outages in 2024 were caused by an out-of-bounds memory error in cybersecurity software developed by CrowdStrike.

Programming languages commonly associated with out-of-bounds reads include C and C++, which provide no built-in protection against using pointers to access data in any part of virtual memory, and which do not automatically check that reading data from a block of memory is safe; respective examples are attempting to read more elements than contained in an array, or failing to append a trailing terminator to a null-terminated string.

Bounds checking, sandboxing, static analysis, using memory safe programming languages, and program verification can prevent buffer over-reads, while techniques such as fuzz testing can help detect them.

## Examples of out-of-bounds reads

Major historical examples of out-of-bounds reads include:

- Heartbleed (2012) was a major bug in OpenSSL allowing clients to read from arbitrary memory.

- In 2013, a denial-of-service attack was reported in the PHP programming language, caused by a buffer over-read when creating a DateInterval object.

- The 2024 CrowdStrike-related IT outages were caused by an out-of-bounds memory read leading to a page fault.

## Categorization

Mitre Corporation (MITRE) categorizes out-of-bounds reads under Common Weakness Enumeration CWE-125, with child categories CWE-126 (buffer over-read) and CWE-127 (buffer under-read).

MITRE lists the corresponding attack pattern under Common Attack Pattern Enumeration and Classification "CAPEC-540: Overread Buffers." This attack is listed at a low likelihood of attack, but a high typical severity if an attack does occur.

## Mitigation

MITRE recommends that buffer over-reads can be effectively detected with static analysis (more specifically, static application security testing). It recommends dynamic analysis (such as AddressSanitizer) as having moderate effectiveness at detection.

For the parent weakness out-of-bounds reads (CWE-125), MITRE recommends data validation (e.g., check that data is in bounds), as well as language selection: "Use a language that provides appropriate memory abstractions." See also List of programming languages by type#Languages by memory management type. Fuzzing is also listed as a highly effective detection method.
