---
title: "Return-oriented programming"
source: https://en.wikipedia.org/wiki/Return-oriented_programming
domain: stack-smashing-protection
license: CC-BY-SA-4.0
tags: stack smashing protection, return address integrity, stack guard defense, prologue epilogue canary
fetched: 2026-07-02
---

# Return-oriented programming

**Return-oriented programming** (**ROP**) is a computer security exploit technique that allows an attacker to execute code despite the presence of security defenses that would otherwise prevent it, such as executable-space protection and code signing.

In this technique, an attacker gains control of the call stack to hijack program control flow and then executes carefully chosen machine instruction sequences that are already present in the machine's memory, called "gadgets". Each gadget typically ends in a return instruction and is located in a subroutine within the existing program and/or shared library code. Chained together, these gadgets allow an attacker to perform arbitrary operations on a machine employing defenses that catch simpler attacks.

## Background

Return-oriented programming is an advanced version of a stack smashing attack. Generally, these types of attacks arise when an adversary manipulates the call stack by taking advantage of a bug in the program, often a buffer overrun. In a buffer overrun, a function that does not perform proper bounds checking before storing user-provided data into memory will accept more input data than it can store properly. If the data is being written onto the stack, the excess data may overflow the space allocated to the function's variables (e.g., "locals" in the stack diagram to the right) and overwrite the return address. This address will later be used by the function to redirect control flow back to the caller. If it has been overwritten, control flow will be diverted to the location specified by the new return address.

In a standard buffer overrun attack, the attacker would simply write attack code (the "payload") onto the stack and then overwrite the return address with the location of these newly written instructions. Until the late 1990s, major operating systems did not offer any protection against these attacks. For example, Microsoft Windows provided no buffer-overrun protections until 2004. Eventually, operating systems began to combat the exploitation of buffer overflow bugs by marking the memory where data is written as non-executable, a technique known as executable-space protection. With this enabled, the machine would refuse to execute any code located in user-writable areas of memory, preventing the attacker from placing payload on the stack and jumping to it via a return address overwrite. Later on, hardware support became available to strengthen this protection.

With data execution prevention, an adversary cannot directly execute instructions written to a buffer because the buffer's memory section is marked as non-executable. To defeat this protection, a return-oriented programming attack does not inject malicious instructions, but rather uses instruction sequences already present in executable memory, called "gadgets", by manipulating return addresses. A typical data execution prevention implementation cannot defend against this attack because the adversary did not directly execute the malicious code, but rather combined sequences of "good" instructions by changing stored return addresses; therefore the code used would be marked as executable.

### Return-into-library technique

The widespread implementation of data execution prevention made traditional buffer overflow vulnerabilities difficult or impossible to exploit in the manner described above. Instead, an attacker was restricted to code already in memory marked executable, such as the program code itself and any linked shared libraries. Since shared libraries, such as libc, often contain subroutines for performing system calls and other functionality potentially useful to an attacker, they are the most likely candidates for finding code to assemble an attack.

In a return-into-library attack, an attacker hijacks program control flow by exploiting a buffer overrun vulnerability, exactly as discussed above. Instead of attempting to write an attack payload onto the stack, the attacker instead chooses an available library function and overwrites the return address with its entry location. Further stack locations are then overwritten, obeying applicable calling conventions, to carefully pass the proper parameters to the function so it performs functionality useful to the attacker. This technique was first presented by Solar Designer in 1997, and was later extended to unlimited chaining of function calls.

### Borrowed code chunks

The rise of 64-bit x86 processors brought with it a change to the subroutine calling convention that required the first few arguments to a function to be passed in registers instead of on the stack. This meant that an attacker could no longer set up a library function call with desired arguments just by manipulating the call stack via a buffer overrun exploit. Shared library developers also began to remove or restrict library functions that performed actions particularly useful to an attacker, such as system call wrappers. As a result, return-into-library attacks became much more difficult to mount successfully.

The next evolution came in the form of an attack that used chunks of library functions, instead of entire functions themselves, to exploit buffer overrun vulnerabilities on machines with defenses against simpler attacks. This technique looks for functions that contain instruction sequences that pop values from the stack into registers. Careful selection of these code sequences allows an attacker to put suitable values into the proper registers to perform a function call under the new calling convention. The rest of the attack proceeds as a return-into-library attack.

## Attacks

Return-oriented programming builds on the borrowed code chunks approach and extends it to provide Turing-complete functionality to the attacker, including loops and conditional branches. Put another way, return-oriented programming provides a fully functional "language" that an attacker can use to make a compromised machine perform any operation desired. Hovav Shacham published the technique in 2007 and demonstrated how all the important programming constructs can be simulated using return-oriented programming against a target application linked with the C standard library and containing an exploitable buffer overrun vulnerability.

A return-oriented programming attack is superior to the other attack types discussed, both in expressive power and in resistance to defensive measures. None of the counter-exploitation techniques mentioned above, including removing potentially dangerous functions from shared libraries altogether, are effective against a return-oriented programming attack.

### On the x86-architecture

Although return-oriented programming attacks can be performed on a variety of architectures, Shacham's paper and the majority of follow-up work focus on the Intel x86 architecture. The x86 architecture is a variable-length CISC instruction set. Return-oriented programming on the x86 takes advantage of the fact that the instruction set is very "dense", that is, any random sequence of bytes is likely to be interpretable as some valid set of x86 instructions.

It is therefore possible to search for an opcode that alters control flow, most notably the return instruction (0xC3) and then look backwards in the binary for preceding bytes that form possibly useful instructions. These sets of instruction "gadgets" can then be chained by overwriting the return address, via a buffer overrun exploit, with the address of the first instruction of the first gadget. The first address of subsequent gadgets is then written successively onto the stack. At the conclusion of the first gadget, a return instruction will be executed, which will pop the address of the next gadget off the stack and jump to it. At the conclusion of that gadget, the chain continues with the third, and so on. By chaining the small instruction sequences, an attacker is able to produce arbitrary program behavior from pre-existing library code. Shacham asserts that given any sufficiently large quantity of code (including, but not limited to, the C standard library), sufficient gadgets will exist for Turing-complete functionality.

An automated tool has been developed to help automate the process of locating gadgets and constructing an attack against a binary. This tool, known as ROPgadget, searches through a binary looking for potentially useful gadgets, and attempts to assemble them into an attack payload that spawns a shell to accept arbitrary commands from the attacker.

### On address space layout randomization

The address space layout randomization also has vulnerabilities. According to the paper of Shacham et al., the ASLR on 32-bit architectures is limited by the number of bits available for address randomization. Only 16 of the 32 address bits are available for randomization, and 16 bits of address randomization can be defeated by brute force attack in minutes. 64-bit architectures are more robust, with 40 of the 64 bits available for randomization. A brute force attack against 40-bit randomization is possible, but is unlikely to go unnoticed. In addition to brute force attacks, techniques for removing randomization exist.

Even with perfect randomization, any information leakage of memory contents would help calculate the base address of, for example, a shared library at runtime.

### Without use of the return instruction

According to the paper of Checkoway et al., it is possible to perform return-oriented-programming on x86 and ARM architectures without using a return instruction (0xC3 on x86). They instead used carefully crafted instruction sequences that already exist in the machine's memory to behave like a return instruction. A return instruction has two effects: firstly, it reads the four-byte value at the top of the stack, and sets the instruction pointer to that value, and secondly, it increases the stack pointer value by four (equivalent to a pop operation). On the x86 architecture, sequences of jmp and pop instructions can act as a return instruction. On ARM, sequences of load and branch instructions can act as a return instruction.

Since this new approach does not use a return instruction, it has negative implications for defense. When a defense program checks not only for several returns but also for several jump instructions, this attack may be detected.

## Defenses

### G-Free

The G-Free technique was developed by Kaan Onarlioglu, Leyla Bilge, Andrea Lanzi, Davide Balzarotti, and Engin Kirda. It is a practical solution against any possible form of return-oriented programming. The solution eliminates all unaligned free-branch instructions (instructions like RET or CALL which attackers can use to change control flow) inside a binary executable, and protects the free-branch instructions from being used by an attacker. The way G-Free protects the return address is similar to the XOR canary implemented by StackGuard. Further, it checks the authenticity of function calls by appending a validation block. If the expected result is not found, G-Free causes the application to crash.

### Address space layout randomization

A number of techniques have been proposed to subvert attacks based on return-oriented programming. Most rely on randomizing the location of program and library code, so that an attacker cannot accurately predict the location of instructions that might be useful in gadgets and therefore cannot mount a successful return-oriented programming attack chain. One fairly common implementation of this technique, address space layout randomization (ASLR), loads shared libraries into a different memory location at each program load. Although widely deployed by modern operating systems, ASLR is vulnerable to information leakage attacks and other approaches to determine the address of any known library function in memory. If an attacker can successfully determine the location of one known instruction, the position of all others can be inferred and a return-oriented programming attack can be constructed.

This randomization approach can be taken further by relocating all the instructions and/or other program state (registers and stack objects) of the program separately, instead of just library locations. This requires extensive runtime support, such as a software dynamic translator, to piece the randomized instructions back together at runtime. This technique is successful at making gadgets difficult to find and utilize, but comes with significant overhead.

Another approach, taken by kBouncer, modifies the operating system to verify that return instructions actually divert control flow back to a location immediately following a call instruction. This prevents gadget chaining, but is not effective against jump-oriented programming attacks which alter jumps and other control-flow-modifying instructions instead of returns.

### Binary code randomization

Some modern systems such as Cloud Lambda (FaaS) and IoT remote updates use Cloud infrastructure to perform on-the-fly compilation before software deployment. A technique that introduces variations to each instance of an executing software program can dramatically increase software's immunity to ROP attacks. Brute forcing Cloud Lambda may result in attacking several instances of the randomized software which reduces the effectiveness of the attack. Asaf Shelly published the technique in 2017 and demonstrated the use of Binary Randomization in a software update system. For every updated device, the Cloud-based service introduced variations to code, performs online compilation, and dispatched the binary. This technique is very effective because ROP attacks rely on knowledge of the internal structure of the software. The drawback of the technique is that the software is never fully tested before it is deployed because it is not feasible to test all variations of the randomized software. This means that many Binary Randomization techniques are applicable for network interfaces and system programming and are less recommended for complex algorithms.

### SEHOP

Structured Exception Handler Overwrite Protection is a feature of Windows which protects against the most common stack overflow attacks, especially against attacks on a structured exception handler.

### Against control flow attacks

As small embedded systems are proliferating due to the expansion of the Internet Of Things, the need for protection of such embedded systems is also increasing. Using Instruction Based Memory Access Control (IB-MAC) implemented in hardware, it is possible to protect low-cost embedded systems against malicious control flow and stack overflow attacks. The protection can be provided by separating the data stack and the return stack. However, due to the lack of a memory management unit in some embedded systems, the hardware solution cannot be applied to all embedded systems.

### Against return-oriented rootkits

In 2010, Jinku Li et al. proposed that a suitably modified compiler could eliminate return-oriented "gadgets" by replacing each `call f` with the instruction sequence `pushl $index`; `jmp f` and each `ret` with the instruction sequence `popl %reg`; `jmp table(%reg)`, where `table` represents an immutable tabulation of all "legitimate" return addresses in the program and `index` represents a specific index into that table. This prevents the creation of a return-oriented gadget that returns straight from the end of a function to an arbitrary address in the middle of another function; instead, gadgets can return only to "legitimate" return addresses, which drastically increases the difficulty of creating useful gadgets. Li et al. claimed that "our return indirection technique essentially *de-generalizes* return-oriented programming back to the old style of return-into-libc." Their proof-of-concept compiler included a peephole optimization phase to deal with "certain machine instructions which happen to contain the return opcode in their opcodes or immediate operands", such as `movl $0xC3, %eax`.

### Pointer Authentication Codes (PAC)

The ARMv8.3-A architecture introduces a new feature at the hardware level that takes advantage of unused bits in the pointer address space to cryptographically sign pointer addresses using a specially designed tweakable block cipher which signs the desired value (typically, a return address) combined with a "local context" value (e.g., the stack pointer).

Before performing a sensitive operation (i.e., returning to the saved pointer) the signature can be checked to detect tampering or usage in the incorrect context (e.g., leveraging a saved return address from an exploit trampoline context).

Apple Silicons since A12 have upgraded to ARMv8.3 and use PACs. Linux gained support for pointer authentication within the kernel in version 5.7 released in 2020; support for userspace applications was added in 2018.

In 2022, researchers at MIT published a side-channel attack against PACs dubbed PACMAN.

### Branch Target Identification (BTI)

ARMv8.5-A introduced hardware level features to explicitly identify valid targets of branch instructions. The compiler inserts a special instruction, opcode named "BTI", at each expected landing point of indirect branch instructions. These identified branch destinations typically include function entry points and switch/case code blocks.

BTI instructions are used in code memory pages which are marked as "guarded" by the compiler and the linker. Any indirect branch instruction landing in a guarded page, at any instruction other than a BTI, generates a fault.

The identified destinations where a BTI instruction is inserted represent approximately 1% of all instructions in average application code. Therefore, using BTI increases the code size by the same amount.

The gadgets which are used in a ROP attack are located anywhere in the application code. Therefore, on average, 99% of the gadgets start with an instruction which is not a BTI. Branching to these gadgets consequently results in a fault. Considering that a ROP attack is made of a chain of multiple gadgets, the probability that all gadgets in a chain are part of the 1% which start with a BTI is very low.

PAC and BTI are complementary mechanisms to prevent rogue code injections using return-oriented and jump-oriented programming attacks. While PAC focuses on the source of a branch operation (a signed pointer), BTI focuses on the destination of the branch.
