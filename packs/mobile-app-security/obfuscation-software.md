---
title: "Obfuscation (software)"
source: https://en.wikipedia.org/wiki/Obfuscation_(software)
domain: mobile-app-security
license: CC-BY-SA-4.0
tags: mobile application security, mobile secure storage, app transport security, reverse engineering resistance
fetched: 2026-07-02
---

# Obfuscation (software)

In software development, **obfuscation** is the practice of creating source or machine code that is intentionally difficult for humans or computers to understand. Similar to obfuscation in natural language, code obfuscation may involve using unnecessarily roundabout ways to write statements. Programmers may obfuscate code to conceal its purpose, logic, or embedded values. The primary reasons for doing so are to prevent tampering, deter reverse engineering, or to create a puzzle or recreational challenge to deobfuscate the code, a challenge often included in crackmes. While obfuscation can be done manually, it is more commonly performed using obfuscators.

## Overview

The architecture and characteristics of some languages may make them easier to obfuscate than others. C, C++, and the Perl programming language are some examples of languages easy to obfuscate. Haskell is also quite obfuscatable despite being quite different in structure.

The properties that make a language obfuscatable are not immediately obvious.

## Techniques

Types of obfuscations include simple keyword substitution, use or non-use of whitespace to create artistic effects, and self-generating or heavily compressed programs.

According to Nick Montfort, techniques may include:

1. naming obfuscation, which includes naming variables in a meaningless or deceptive way;
2. data/code/comment confusion, which includes making some actual code look like comments or confusing syntax with data;
3. double coding, which can be displaying code in poetry form or interesting shapes.

More sophisticated techniques that obfuscate a program at the semantic level through program transformations also exist (rather than at the source level). These include:

1. Control flow obfuscating transformations, such as merging the computation of unrelated expressions and splitting the computation of related expressions, randomizing the order of statements that can be computed in any order, and inserting predicates whose values are known to the obfuscator but are computed in non-obvious ways;
2. Data structure obfuscating transformations, such as modifying the structure of arrays and rearranging the inheritance graph;
3. Obfuscating transformations of the procedural structure of the code by inserting new procedural abstractions and changing existing procedural abstractions to completely change the code's structure;
4. Obfuscating the data flow of a program.

### Example

The following illustrates simple source-code obfuscation. Both programs print the same output, but the second version is intentionally harder to understand.

**Clear code:**

```mw
#include <stdio.h>

int main(void) {
    int x = 5;
    int y = 7;
    printf("%d\n", x + y);
    return 0;
}
```

**Obfuscated code:**

```mw
#include <stdio.h>
int main(){int _=5,__=7;printf("%d\n",_-~__-1);}
```

In the obfuscated version, meaningful variable names are removed and arithmetic expressions are rewritten in a less readable form, while preserving the program’s behavior.

### Payload encoding for malware evasion

XOR encryption and Base64 encoding are two common methods used to hide malware from antivirus detection. Both work by changing how malicious code appears in its file form, which prevents security software from recognizing dangerous patterns.

In XOR obfuscation, an attacker chooses a secret key and applies the XOR bitwise operation to the malware binary. This transforms the executable into what looks like random data. Function names in the import table vanish, PE headers become corrupted, and the entire file loses its structure. The obfuscated payload then gets embedded into a *dropper*, which is a normal-looking executable that contains the hidden malware as a resource or data section. When a user runs the dropper, it performs the XOR operation again with the same key to reconstruct the original malware, then either executes it directly from memory or writes it to disk before running it.

This process removes several indicators that antivirus software relies on. The MZ header⁠‍—‍‌the 2-byte signature "MZ" which marks the beginning of every Windows executable‍—‍‌gets completely obscured by the XOR operation. Security programs frequently scan for this two-byte signature when searching for embedded executables. Base64 encoding achieves similar results through a different method: it converts binary data into ASCII text such that an executable file ends up looking like plain text (rather than like a program).

Research from the 2020 Machine Learning Security Evasion Competition showed that these methods can bypass modern detection systems. Participants used combinations of XOR encoding, Base64 encoding, and dead code insertion to evade all three competition models with fewer than five attempts per sample. Entropy-based detection also failed, and in some cases Base64 encoding actually lowered the entropy compared to the original malware files.

The simplicity of these techniques is what makes them particularly dangerous. XOR and Base64 encoding require only basic programming skills to implement, yet they proved effective against advanced machine learning classifiers. This has pushed security researchers toward new defenses, including automated XOR key recovery tools and deeper analysis of embedded resources in executable files.

### Automated tools

A variety of tools exist to perform or assist with code obfuscation. These include experimental research tools developed by academics, hobbyist tools, commercial products written by professionals, and open-source software. Additionally, deobfuscation tools exist, aiming to reverse the obfuscation process.

While most commercial obfuscation solutions transform either program source code or platform-independent bytecode, *i.e.* portable code (as used by Java and .NET), some also work directly on compiled binaries.

- Some Python examples can be found in the official Python programming FAQ and elsewhere.
- The *movfuscator* C compiler for the x86_32 ISA uses only the *mov* instruction in order to obfuscate.

### Recreational

Writing and reading obfuscated source code can be a brain teaser. A number of programming contests reward the most creatively obfuscated code, such as the International Obfuscated C Code Contest and the Obfuscated Perl Contest.

Short obfuscated Perl programs may be used in signatures of Perl programmers, known as JAPHs ("Just another Perl hacker").

### Cryptographic

Cryptographers have explored the idea of obfuscating code so that reverse-engineering the code is *cryptographically* hard. This is formalized in the many proposals for indistinguishability obfuscation, a cryptographic primitive that, if possible to build securely, would allow one to construct many other kinds of cryptography, including completely novel types that no one knows how to make. (A stronger notion, black-box obfuscation, is known to be impossible in general.)

## Disadvantages of obfuscation

- While obfuscation can make reading, writing, and reverse-engineering a program difficult and time-consuming, it will not necessarily make it impossible.
- It adds time and complexity to the build process for the developers.
- It can make debugging issues after the software has been obfuscated extremely difficult.
- Once code is no longer maintained, hobbyists may want to maintain the program, add mods, or understand it better. Obfuscation makes it hard for end users to do useful things with the code.
- Certain kinds of obfuscation (i.e. code that isn't just a local binary and downloads mini binaries from a web server as needed) can degrade performance and/or require Internet.

### Notifying users of obfuscated code

Some anti-virus softwares, such as AVG AntiVirus, will alert their users when they land on a website with code that is manually obfuscated, as one of the purposes of obfuscation can be to hide malicious code. However, some developers may employ code obfuscation for the purpose of reducing file size or increasing security. The average user may not expect their antivirus software to provide alerts about an otherwise harmless piece of code, especially from trusted corporations, so such a feature may actually deter users from using legitimate software.

Mozilla and Google disallow browser extensions containing obfuscated code in their browser (Firefox and Chrome, respectively) add-on stores.

### Obfuscation and copyleft licenses

There has been debate on whether it is illegal to skirt copyleft software licenses by releasing source code in obfuscated form, such as in cases in which the author is less willing to make the source code available. The issue is addressed in the GNU General Public License by requiring the "preferred form for making modifications" to be made available. The GNU website states "Obfuscated 'source code' is not real source code and does not count as source code."

## Decompilers

A decompiler is a tool that can reverse-engineer source code from an executable or library. This process is sometimes referred to as a man-in-the-end (mite) attack, inspired by the traditional "man-in-the-middle attack" in cryptography. The decompiled source code is often hard to read, containing random function and variable names, incorrect variable types, and logic that differs from the original source code due to compiler optimizations.

## Model obfuscation

**Model obfuscation** is a technique to hide the internal structure of a machine learning model. Obfuscation turns a model into a black box. It is contrary to explainable AI. Obfuscation models can also be applied to training data before feeding it into the model to add random noise. This hides sensitive information about the properties of individual and groups of samples.
