---
title: "Symbolic execution"
source: https://en.wikipedia.org/wiki/Symbolic_execution
domain: weakest-precondition
license: CC-BY-SA-4.0
tags: weakest precondition, predicate transformer semantics, guarded command language, verification condition
fetched: 2026-07-02
---

# Symbolic execution

In computer science, **symbolic execution**(also **symbolic evaluation** or **symbex**) is a means of analyzing a program to determine what inputs cause each part of a program to execute. An interpreter follows the program, assuming symbolic values for inputs rather than obtaining actual inputs as normal execution of the program would. It thus arrives at expressions in terms of those symbols for expressions and variables in the program, and constraints in terms of those symbols for the possible outcomes of each conditional branch. Finally, the possible inputs that trigger a branch can be determined by solving the constraints.

The field of symbolic simulation applies the same concept to hardware. Symbolic computation applies the concept to the analysis of mathematical expressions.

## Example

Consider the program below, which reads in a value and fails if the input is 6.

```mw
#include <stdio.h>

// reads an integer from somewhere and returns it
int read();

int main() {
    int y = read();
    int z = y * 2;
    if (z == 12) {
        perror("Program failed!");
        return 1;
    } else {
        printf("OK");
        return 0;
    }
}
```

During a normal execution ("concrete" execution), the program would read a concrete input value (e.g., 5) and assign it to `y`. Execution would then proceed with the multiplication and the conditional branch, which would evaluate to false and print `OK`.

During symbolic execution, the program reads a symbolic value (e.g., `λ`) and assigns it to `y`. The program would then proceed with the multiplication and assign `λ * 2` to `z`. When reaching the `if` statement, it would evaluate `λ * 2 == 12`. At this point of the program, `λ` could take any value, and symbolic execution can therefore proceed along both branches, by "forking" two paths. Each path gets assigned a copy of the program state at the branch instruction as well as a path constraint. In this example, the path constraint is `λ * 2 == 12` for the `if` branch and `λ * 2 != 12` for the `else` branch. Both paths can be symbolically executed independently. When paths terminate (e.g., as a result of executing `fail()` or simply exiting), symbolic execution computes a concrete value for `λ` by solving the accumulated path constraints on each path. These concrete values can be thought of as concrete test cases that can, e.g., help developers reproduce bugs. In this example, the constraint solver would determine that in order to reach the `fail()` statement, `λ` would need to equal 6 or (if `int` is a 32-bit two's complement integer and integer overflow is taken into account) -2147483642.

## Limitations

### Path explosion

Symbolically executing all feasible program paths does not scale to large programs. The number of feasible paths in a program grows exponentially with an increase in program size and can even be infinite in the case of programs with unbounded loop iterations. Solutions to the *path explosion* problem generally use either heuristics for path-finding to increase code coverage, reduce execution time by parallelizing independent paths, or by merging similar paths. One example of merging is *veritesting*, which "employs static symbolic execution to amplify the effect of dynamic symbolic execution".

### Program-dependent efficiency

Symbolic execution is used to reason about a program path-by-path which is an advantage over reasoning about a program input-by-input as other testing paradigms use (e.g. dynamic program analysis). However, if few inputs take the same path through the program, there is little savings over testing each of the inputs separately.

### Memory aliasing

Symbolic execution is harder when the same memory location can be accessed through different names (aliasing). Aliasing cannot always be recognized statically, so the symbolic execution engine can't recognize that a change to the value of one variable also changes the other.

### Arrays

Since an array is a collection of many distinct values, symbolic executors must either treat the entire array as one value or treat each array element as a separate location. The problem with treating each array element separately is that a reference such as "A[i]" can only be specified dynamically, when the value for i has a concrete value.

### Environment interactions

Programs interact with their environment by performing system calls, receiving signals, etc. Consistency problems may arise when execution reaches components that are not under control of the symbolic execution tool (e.g., kernel or libraries). Consider the following example:

```mw
int main() {
    FILE *fp = fopen("my_document.txt", "w");
    char data[100];
    bool cond = /* some condition here */;
    if (cond) {
        fputs("Some data", fp);
    } else {
        fputs("Some other data", fp);
    }
    fgets(data, sizeof(data), fp);
}
```

This program opens a file and, based on some condition, writes different kind of data to the file. It then later reads back the written data. In theory, symbolic execution would fork two paths at line 5 and each path from there on would have its own copy of the file. The statement at line 11 would therefore return data that is consistent with the value of "condition" at line 5. In practice, file operations are implemented as system calls in the kernel, and are outside the control of the symbolic execution tool. The main approaches to address this challenge are:

**Executing calls to the environment directly.** The advantage of this approach is that it is simple to implement. The disadvantage is that the side effects of such calls will clobber all states managed by the symbolic execution engine. In the example above, the instruction at line 11 would return "some datasome other data" or "some other datasome data" depending on the sequential ordering of the states.

**Modeling the environment.** In this case, the engine instruments the system calls with a model that simulates their effects and that keeps all the side effects in per-state storage. The advantage is that one would get correct results when symbolically executing programs that interact with the environment. The disadvantage is that one needs to implement and maintain many potentially complex models of system calls. Tools such as KLEE, Cloud9, and Otter take this approach by implementing models for file system operations, sockets, IPC, etc.

**Forking the entire system state.** Symbolic execution tools based on virtual machines solve the environment problem by forking the entire VM state. For example, in S2E each state is an independent VM snapshot that can be executed separately. This approach alleviates the need for writing and maintaining complex models and allows virtually any program binary to be executed symbolically. However, it has higher memory usage overheads (VM snapshots may be large).

## Tools

| Tool | Target | URL | Can anybody use it/ Open source/ Downloadable |
|---|---|---|---|
| angr | libVEX based (supporting x86, x86-64, ARM, AARCH64, MIPS, MIPS64, PPC, PPC64, and Java) | http://angr.io/ | yes |
| BE-PUM | x86 | https://github.com/NMHai/BE-PUM | yes |
| BINSEC | x86, ARM, RISC-V (32 bits) | http://binsec.github.io | yes |
| crucible | LLVM, JVM, etc | https://github.com/GaloisInc/crucible | yes |
| ExpoSE | JavaScript | https://github.com/ExpoSEJS/ExpoSE | yes |
| FuzzBALL | VineIL / Native | http://bitblaze.cs.berkeley.edu/fuzzball.html | yes |
| GenSym | LLVM | https://github.com/Generative-Program-Analysis/GenSym | yes |
| Jalangi2 | JavaScript | https://github.com/Samsung/jalangi2 | yes |
| janala2 | Java | https://github.com/ksen007/janala2 | yes |
| JaVerT | JavaScript | https://www.doc.ic.ac.uk/~pg/publications/FragosoSantos2019JaVerT.pdf | yes |
| JBSE | Java | https://github.com/pietrobraione/jbse | yes |
| jCUTE | Java | https://github.com/osl/jcute | yes |
| KeY | Java | http://www.key-project.org/ | yes |
| Kite | LLVM | http://www.cs.ubc.ca/labs/isd/Projects/Kite/ | yes |
| KLEE | LLVM | https://klee.github.io/ | yes |
| Kudzu | JavaScript | http://webblaze.cs.berkeley.edu/2010/kudzu/kudzu.pdf | no |
| MPro | Ethereum Virtual Machine (EVM) / Native | https://sites.google.com/view/smartcontract-analysis/home | yes |
| Maat | Ghidra P-code / SLEIGH | https://maat.re/ | yes |
| Manticore | x86-64, ARMv7, Ethereum Virtual Machine (EVM) / Native | https://github.com/trailofbits/manticore/ | yes |
| Mayhem | Binary | http://forallsecure.com | no |
| Mythril | Ethereum Virtual Machine (EVM) / Native | https://github.com/ConsenSys/mythril | yes |
| Otter | C | https://bitbucket.org/khooyp/otter/overview | yes |
| Owi | C, C++, Rust, WebAssembly, Zig | https://github.com/ocamlpro/owi | yes |
| Oyente-NG | Ethereum Virtual Machine (EVM) / Native | http://www.comp.ita.br/labsca/waiaf/papers/RafaelShigemura_paper_16.pdf | no |
| Pathgrind | Native 32-bit Valgrind-based | https://github.com/codelion/pathgrind | yes |
| Pex | .NET Framework | http://research.microsoft.com/en-us/projects/pex/ | no |
| pysymemu | x86-64 / Native | https://github.com/feliam/pysymemu/ | yes |
| Rosette | Dialect of Racket | https://emina.github.io/rosette/ | yes |
| Rubyx | Ruby | http://www.cs.umd.edu/~avik/papers/ssarorwa.pdf | no |
| S2E | x86, x86-64, ARM / User and kernel-mode binaries | http://s2e.systems/ | yes |
| Symbolic PathFinder (SPF) | Java Bytecode | https://github.com/SymbolicPathFinder | yes |
| SymDroid | Dalvik bytecode | http://www.cs.umd.edu/~jfoster/papers/symdroid.pdf | no |
| SymJS | JavaScript | https://core.ac.uk/download/pdf/24067593.pdf | no |
| SymCC | LLVM | https://www.s3.eurecom.fr/tools/symbolic_execution/symcc.html | yes |
| Triton | x86, x86-64, ARM and AArch64 | https://triton.quarkslab.com | yes |
| Verifast | C, Java | https://people.cs.kuleuven.be/~bart.jacobs/verifast | yes |

## Earlier versions of the tools

1. EXE is an earlier version of KLEE. The EXE paper can be found here.

## History

The concept of symbolic execution was introduced academically in the 1970s with descriptions of: the Select system, the EFFIGY system, the DISSECT system, and Clarke's system.
