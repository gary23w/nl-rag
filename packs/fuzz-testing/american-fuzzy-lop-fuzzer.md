---
title: "American Fuzzy Lop (software)"
source: https://en.wikipedia.org/wiki/American_fuzzy_lop_(fuzzer)
domain: fuzz-testing
license: CC-BY-SA-4.0
tags: fuzz testing, coverage guided fuzzing, american fuzzy lop, code coverage, static program analysis
fetched: 2026-07-02
---

# American Fuzzy Lop (software)

(Redirected from

American fuzzy lop (fuzzer)

)

**American Fuzzy Lop** (**AFL**), stylized in all lowercase as **american fuzzy lop**, is a free software fuzzer that employs genetic algorithms in order to efficiently increase code coverage of the test cases. So far it has detected hundreds of significant software bugs in major free software projects, including X.Org Server, PHP, OpenSSL, pngcrush, bash, Firefox, BIND, Qt, and SQLite.

Initially released in November 2013, AFL quickly became one of the most widely used fuzzers in security research. For many years after its release, AFL has been considered a "state of the art" fuzzer. AFL is considered "a de-facto standard for fuzzing", and the release of AFL contributed significantly to the development of fuzzing as a research area. AFL is widely used in academia; academic fuzzers are often forks of AFL, and AFL is commonly used as a baseline to evaluate new techniques.

The source code of American fuzzy lop is published on GitHub. Its name is a reference to a breed of rabbit, the American Fuzzy Lop.

## Overview

AFL requires the user to provide a sample command that runs the tested application and at least one small example input. The input can be fed to the tested program either via standard input or as an input file specified in the process command line. Fuzzing networked programs is currently not directly supported, although in some cases there are feasible solutions to this problem. For example, in case of an audio player, American fuzzy lop can be instructed to open a short sound file with it. Then, the fuzzer attempts to actually execute the specified command and if that succeeds, it tries to reduce the input file to the smallest one that triggers the same behavior.

After this initial phase, AFL begins the actual process of fuzzing by applying various modifications to the input file. When the tested program crashes or hangs, this usually implies the discovery of a new bug, possibly a security vulnerability. In this case, the modified input file is saved for further user inspection.

In order to maximize the fuzzing performance, American fuzzy lop expects the tested program to be compiled with the aid of a utility program that instruments the code with helper functions which track control flow. This allows the fuzzer to detect when the target's behavior changes in response to the input. In cases when this is not possible, black-box testing is supported as well.

## Fuzzing algorithm

Fuzzers attempt to find unexpected behaviors (i.e., bugs) in a target program by repeatedly executing the program on various inputs. As described above, AFL is a gray-box fuzzer, meaning it expects instrumentation to measure code coverage to have been injected into the target program at compile time and uses the coverage metric to direct the generation of new inputs. AFL's fuzzing algorithm has influenced many subsequent gray-box fuzzers.

The inputs to AFL are an instrumented **target program** (the system under test) and **corpus**, that is, a collection of inputs to the target. Inputs are also known as **test cases**. The algorithm maintains a queue of inputs, which is initialized to the input corpus. The overall algorithm works as follows:

1. Load the next input from the queue
2. Minimize the test case
3. Mutate the test case. If any mutant results in additional code coverage, add it to the queue. If the mutant results in a crash or hang, save it to disk for later inspection.
4. Go to step 1

### Mutation

To generate new inputs, AFL applies various **mutations** to existing inputs. These mutations are mostly agnostic to the input format of the target program; they generally treat the input as simple blob of binary data.

At first, AFL applies a deterministic sequence of mutations to each input. These are applied at various offsets in the input. They include:

- Flipping (i.e., negating or inverting) 1-32 bits
- Incrementing and decrementing 8-, 16-, and 32-bit integers, in both little- and big-endian encodings
- Overwriting parts of the input with "approximately two dozen 'interesting' values", including zero and maximum and minimum signed and unsigned integers of various widths, again in both little- and big-endian encodings.
- Replacing parts of the input with data drawn from a "dictionary" of user-specified or auto-detected tokens (e.g., magic bytes, or keywords in a text-based format)

After applying all available deterministic mutations, AFL moves on to **havoc**, a stage where between 2 and 128 mutations are applied in a row. These mutations are any of:

- The deterministic mutations described above
- Overwriting bytes with random values
- Operations over multi-byte "blocks":
  - Deleting blocks
  - Duplicating blocks
  - Setting each byte in a block to a single value

If AFL cycles through the entire queue without generating any input that achieves new code coverage, it begins **splicing**. Splicing takes two inputs from the queue, truncates them at arbitrary positions, concatenates them together, and applies the havoc stage to the result.

### Measuring coverage

AFL pioneered the use of **binned hitcounts** for measuring code coverage. The author claims that this technique mitigates path explosion.

Conceptually, AFL counts the number of times a given execution of the target traverses each edge in the target's control-flow graph; the documentation refers to these edges as **tuples** and the counts as **hitcounts**. At the end of the execution, the hitcounts are **binned** or **bucketed** into the following eight buckets: 1, 2, 3, 4–7, 8–15, 16–31, 32–127, and 128 and greater. AFL maintains a global set of (tuple, binned count) pairs that have been produced by any execution thus far. An input is considered "interesting" and is added to the queue if it produces a (tuple, binned count) pair that is not yet in the global set.

In practice, the hitcounts are collected and processed using an efficient but lossy scheme. The compile-time instrumentation injects code that is conceptually similar to the following at each branch in the control-flow graph of the target program:

```mw
cur_location = <COMPILE_TIME_RANDOM>;
shared_mem[cur_location ^ prev_location]++;
prev_location = cur_location >> 1;
```

where `<COMPILE_TIME_RANDOM>` is a random integer and `shared_mem` is a 64 kibibyte region of memory shared between the fuzzer and the target.

This representation is more fine-grained (distinguishes between more executions) than simple block or statement coverage, but still allows for a linear-time "interestingness" test.

### Minimization

On the assumption that smaller inputs take less time to execute, AFL attempts to minimize or **trim** the test cases in the queue. Trimming works by removing blocks from the input; if the trimmed input still results in the same coverage (see #Measuring coverage), then the original input is discarded and the trimmed input is saved in the queue.

### Scheduling

AFL selects a subset of **favored** inputs from the queue; non-favored inputs are skipped with some probability.

## Features

### Performance features

One of the challenges American fuzzy lop had to solve involved an efficient spawning of hundreds of processes per second. Apart from the original engine that spawned every process from scratch, American fuzzy lop offers the default engine that relies heavily on the `fork` system call. This can further be sped up by leveraging LLVM deferred fork server mode or the similar persistent mode, but this comes at the cost of having to modify the tested program. Also, American fuzzy lop supports fuzzing the same program over the network.

### User interface

American fuzzy lop features a colorful command line interface that displays real-time statistics about the fuzzing process. Various settings may be triggered by either command line options or environment variables. Apart from that, programs may read runtime statistics from files in a machine-readable format.

### Utility programs

In addition to `afl-fuzz` and tools that can be used for binary instrumentation, American fuzzy lop features utility programs meant for monitoring of the fuzzing process. Apart from that, there is `afl-cmin` and `afl-tmin`, which can be used for test case and test corpus minimization. This can be useful when the test cases generated by `afl-fuzz` would be used by other fuzzers.

## Forks

AFL has been forked many times in order to examine new fuzzing techniques, or to apply fuzzing to different kinds of programs. A few notable forks include:

- AFL++
- MOPT-AFL
- AFLFast
- AFLSmart
- AFLGo
- SymCC-AFL
- WinAFL, "a fork of AFL for fuzzing Windows binaries"

### AFL++

**AFL++** (**AFLplusplus**) is a community-maintained fork of AFL created due to the relative inactivity of Google's upstream AFL development since September 2017. It includes new features and speedups.

Google's OSS-Fuzz initiative, which provides free fuzzing services to open source software, replaced its AFL option with AFL++ in January 2021.
