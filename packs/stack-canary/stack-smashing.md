---
title: "Stack buffer overflow"
source: https://en.wikipedia.org/wiki/Stack_smashing
domain: stack-canary
license: CC-BY-SA-4.0
tags: stack canary protection, stack buffer overflow defense, buffer overflow protection, stack smashing detection, compiler hardening feature
fetched: 2026-07-02
---

# Stack buffer overflow

(Redirected from

Stack smashing

)

In software, a **stack buffer overflow** or **stack buffer overrun** occurs when a program writes to a memory address on the program's call stack outside of the intended data structure, which is usually a fixed-length buffer. Stack buffer overflow bugs are caused when a program writes more data to a buffer located on the stack than what is actually allocated for that buffer. This almost always results in corruption of adjacent data on the stack, and in cases where the overflow was triggered by mistake, will often cause the program to crash or operate incorrectly. Stack buffer overflow is a type of the more general programming malfunction known as buffer overflow (or buffer overrun). Overfilling a buffer on the stack is more likely to derail program execution than overfilling a buffer on the heap because the stack contains the return addresses for all active function calls.

A stack buffer overflow can be caused deliberately as part of an attack known as **stack smashing**. If the affected program is running with special privileges, or accepts data from untrusted network hosts (e.g. a webserver) then the bug is a potential security vulnerability. If the stack buffer is filled with data supplied from an untrusted user then that user can corrupt the stack in such a way as to inject executable code into the running program and take control of the process. This is one of the oldest and more reliable methods for attackers to gain unauthorized access to a computer.

## Exploiting stack buffer overflows

The canonical method for exploiting a stack-based buffer overflow is to overwrite the function return address with a pointer to attacker-controlled data (usually on the stack itself). This is illustrated with `strcpy()` in the following example:

```mw
#include <string.h>

void foo(char* bar) {
    char c[12];

    strcpy(c, bar); // no bounds checking
}

int main(int argc, char* argv[]) {
    foo(argv[1]);
    return 0;
}
```

This code takes an argument from the command line and copies it to a local stack variable `c`. This works fine for command-line arguments smaller than 12 characters (as can be seen in figure B below). Any arguments larger than 11 characters long will result in corruption of the stack. (The maximum number of characters that is safe is one less than the size of the buffer here because in the C programming language, strings are terminated by a null byte character. A twelve-character input thus requires thirteen bytes to store, the input followed by the sentinel zero byte. The zero byte then ends up overwriting a memory location that's one byte beyond the end of the buffer.)

The program stack in `foo()` with various inputs:

|   |   |   |
|---|---|---|

In figure C above, when an argument larger than 11 bytes is supplied on the command line `foo()` overwrites local stack data, the saved frame pointer, and most importantly, the return address. When `foo()` returns, it pops the return address off the stack and jumps to that address (i.e. starts executing instructions from that address). Thus, the attacker has overwritten the return address with a pointer to the stack buffer `char c[12]`, which now contains attacker-supplied data. In an actual stack buffer overflow exploit the string of "A"'s would instead be shellcode suitable to the platform and desired function. If this program had special privileges (e.g. the SUID bit set to run as the superuser), then the attacker could use this vulnerability to gain superuser privileges on the affected machine.

The attacker can also modify internal variable values to exploit some bugs. With this example:

```mw
#include <stdio.h>
#include <string.h>

void foo(char* bar) {
    float myFloat = 10.5; // Addr = 0x0023FF4C
    char c[28]; // Addr = 0x0023FF30

    // Will print 10.500000
    printf("myFloat value = %f\n", myFloat);

    /* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       Memory map:
       @ : c allocated memory
       # : myFloat allocated memory

           *c                      *myFloat
       0x0023FF30                  0x0023FF4C
           |                           |
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@#####
      foo("my string is too long !!!!! XXXXX");

    memcpy will put 0x1010C042 (little endian) in myFloat value.
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/

    memcpy(c, bar, strlen(bar));  // no bounds checking...

    // Will print 96.031372
    printf("myFloat value = %f\n", myFloat);
}

int main(int argc, char* argv[]) {
    foo("my string is too long !!!!! \x10\x10\xc0\x42");
    return 0;
}
```

There are typically two methods that are used to alter the stored address in the stack - direct and indirect. Attackers started developing indirect attacks, which have fewer dependencies, in order to bypass protection measures that were made to reduce direct attacks.

A number of platforms have subtle differences in their implementation of the call stack that can affect the way a stack buffer overflow exploit will work. Some machine architectures store the top-level return address of the call stack in a register. This means that any overwritten return address will not be used until a later unwinding of the call stack. Another example of a machine-specific detail that can affect the choice of exploitation techniques is the fact that most RISC-style machine architectures will not allow unaligned access to memory. Combined with a fixed length for machine opcodes, this machine limitation can make the technique of jumping to the stack almost impossible to implement (with the one exception being when the program actually contains the unlikely code to explicitly jump to the stack register).

### Stacks that grow up

Within the topic of stack buffer overflows, an often-discussed-but-rarely-seen architecture is one in which the stack grows in the opposite direction. This change in architecture is frequently suggested as a solution to the stack buffer overflow problem because any overflow of a stack buffer that occurs within the same stack frame cannot overwrite the return pointer. However, any overflow that occurs in a buffer from a previous stack frame will still overwrite a return pointer and allow for malicious exploitation of the bug. For instance, in the example above, the return pointer for `foo` will not be overwritten because the overflow actually occurs within the stack frame for `memcpy`. However, because the buffer that overflows during the call to `memcpy` resides in a previous stack frame, the return pointer for `memcpy` will have a numerically higher memory address than the buffer. This means that instead of the return pointer for `foo` being overwritten, the return pointer for `memcpy` will be overwritten. At most, this means that growing the stack in the opposite direction will change some details of how stack buffer overflows are exploitable, but it will not reduce significantly the number of exploitable bugs.

## Protection schemes

Over the years, a number of control-flow integrity schemes have been developed to inhibit malicious stack buffer overflow exploitation. These may usually be classified into three categories:

- Detect that a stack buffer overflow has occurred and thus prevent redirection of the instruction pointer to malicious code.
- Prevent the execution of malicious code from the stack without directly detecting the stack buffer overflow.
- Randomize the memory space such that finding executable code becomes unreliable.

### Stack canaries

Stack canaries, named for their analogy to a canary in a coal mine, are used to detect a stack buffer overflow before execution of malicious code can occur. This method works by placing a small integer, the value of which is randomly chosen at program start, in memory just before the stack return pointer. Most buffer overflows overwrite memory from lower to higher memory addresses, so in order to overwrite the return pointer (and thus take control of the process) the canary value must also be overwritten. This value is checked to make sure it has not changed before a routine uses the return pointer on the stack. This technique can greatly increase the difficulty of exploiting a stack buffer overflow because it forces the attacker to gain control of the instruction pointer by some non-traditional means such as corrupting other important variables on the stack.

### Nonexecutable stack

Another approach to preventing stack buffer overflow exploitation is to enforce a memory policy on the stack memory region that disallows execution from the stack (W^X, "Write XOR Execute"). This means that in order to execute shellcode from the stack an attacker must either find a way to disable the execution protection from memory, or find a way to put their shellcode payload in a non-protected region of memory. This method is becoming more popular now that hardware support for the no-execute flag is available in most desktop processors.

While this method prevents the canonical stack smashing exploit, stack overflows can be exploited in other ways. First, it is common to find ways to store shellcode in unprotected memory regions like the heap, and so very little need change in the way of exploitation.

Another attack is the so-called return to libc method for shellcode creation. In this attack the malicious payload will load the stack not with shellcode, but with a proper call stack so that execution is vectored to a chain of standard library calls, usually with the effect of disabling memory execute protections and allowing shellcode to run as normal. This works because the execution never actually vectors to the stack itself.

A variant of return-to-libc is return-oriented programming (ROP), which sets up a series of return addresses, each of which executes a small sequence of cherry-picked machine instructions within the existing program code or system libraries, sequence which ends with a return. These so-called *gadgets* each accomplish some simple register manipulation or similar execution before returning, and stringing them together achieves the attacker's ends. It is even possible to use "returnless" return-oriented programming by exploiting instructions or groups of instructions that behave much like a return instruction.

### Randomization

Instead of separating the code from the data, another mitigation technique is to introduce randomization to the memory space of the executing program. Since the attacker needs to determine where executable code that can be used resides, either an executable payload is provided (with an executable stack) or one is constructed using code reuse such as in ret2libc or return-oriented programming (ROP). Randomizing the memory layout will, as a concept, prevent the attacker from knowing where any code is. However, implementations typically will not randomize everything; usually the executable itself is loaded at a fixed address and hence even when ASLR (address space layout randomization) is combined with a non-executable stack the attacker can use this fixed region of memory. Therefore, all programs should be compiled with PIE (position-independent executables) such that even this region of memory is randomized. The entropy of the randomization is different from implementation to implementation and a low enough entropy can in itself be a problem in terms of brute forcing the memory space that is randomized.

### Bypass countermeasures

The previous mitigations make the steps of the exploitation harder. But it is still possible to exploit a stack buffer overflow if some vulnerabilities are presents or if some conditions are met.

#### Stack canary bypass

##### Information leak with format string vulnerability exploitation

An attacker is able to exploit the format string vulnerability for revealing the memory locations in the vulnerable program.

#### Non executable stack bypass

When Data Execution Prevention is enabled to forbid any execute access to the stack, the attacker can still use the overwritten return address (the instruction pointer) to point to data in a code segment (.text on Linux) or every other executable section of the program. The goal is to reuse existing code.

##### Rop chain

Consists to overwrite the return pointer a bit before a return instruction (ret in x86) of the program. The instructions between the new return pointer and the return instruction will be executed and the return instruction will return to the payload controlled by the exploiter.

##### Jop chain

Jump Oriented Programming is a technique that uses jump instructions to reuse code instead of the ret instruction.

#### Randomization bypass

A limitation of ASLR realization on 64-bit systems is that it is vulnerable to memory disclosure and information leakage attacks. The attacker can launch the ROP by revealing a single function address using information leakage attack. The following section describes the similar existing strategy for breaking down the ASLR protection.

## Notable examples

- The Morris worm in 1988 spread in part by exploiting a stack buffer overflow in the Unix finger server.
- The Slammer worm in 2003 spread by exploiting a stack buffer overflow in Microsoft's SQL server.
- The Blaster worm in 2003 spread by exploiting a stack buffer overflow in Microsoft DCOM service.
- The Witty worm in 2004 spread by exploiting a stack buffer overflow in the Internet Security Systems BlackICE Desktop Agent.
- There are a couple of examples of the Wii allowing arbitrary code to be run on an unmodified system. The "Twilight hack" which involves giving a lengthy name to the main character's horse in *The Legend of Zelda: Twilight Princess*, and "Smash Stack" for *Super Smash Bros. Brawl* which involves using an SD card to load a specially prepared file into the in-game level editor. Though both can be used to execute any arbitrary code, the latter is often used to simply reload *Brawl* itself with modifications applied.
