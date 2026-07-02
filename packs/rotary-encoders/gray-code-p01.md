---
title: "Gray code (part 1/2)"
source: https://en.wikipedia.org/wiki/Gray_code
domain: rotary-encoders
license: CC-BY-SA-4.0
tags: rotary encoder, incremental encoder, gray code, resolver device
fetched: 2026-07-02
part: 1/2
---

# Gray code

|   | Gray code |   |   |   |
|---|---|---|---|---|
| 4 | 3 | 2 | 1 |   |
| 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 |
| 2 | 0 | 0 | 1 | 1 |
| 3 | 0 | 0 | 1 | 0 |
| 4 | 0 | 1 | 1 | 0 |
| 5 | 0 | 1 | 1 | 1 |
| 6 | 0 | 1 | 0 | 1 |
| 7 | 0 | 1 | 0 | 0 |
| 8 | 1 | 1 | 0 | 0 |
| 9 | 1 | 1 | 0 | 1 |
| 10 | 1 | 1 | 1 | 1 |
| 11 | 1 | 1 | 1 | 0 |
| 12 | 1 | 0 | 1 | 0 |
| 13 | 1 | 0 | 1 | 1 |
| 14 | 1 | 0 | 0 | 1 |
| 15 | 1 | 0 | 0 | 0 |

The **reflected binary code** (**RBC**), also known as **reflected binary** (**RB**) or **Gray code** after Frank Gray, is an ordering of the binary numeral system such that two successive values differ in only one bit (binary digit).

For example, the representation of the decimal value "1" in binary would normally be "001", and "2" would be "010". In Gray code, these values are represented as "001" and "011". That way, incrementing a value from 1 to 2 requires only one bit to change, instead of two.

Gray codes are widely used to prevent spurious output from electromechanical switches and to facilitate error correction in digital communications such as digital terrestrial television and some cable TV systems. The use of Gray code in these devices helps simplify logic operations and reduce errors in practice.


## Function

Many devices indicate position by closing and opening switches. If that device uses natural binary codes, positions 3 and 4 are next to each other but all three bits of the binary representation differ:

| Decimal | Binary |
|---|---|
| … | … |
| 3 | 011 |
| 4 | 100 |
| … | … |

The problem with natural binary codes is that physical switches are not ideal: it is very unlikely that physical switches will change states exactly in synchrony. In the transition between the two states shown above, all three switches change state. In the brief period while all are changing, the switches will read some spurious position. Even without keybounce, the transition might look like 011 — 001 — 101 — 100. When the switches appear to be in position 001, the observer cannot tell if that is the "real" position 1, or a transitional state between two other positions. If the output feeds into a sequential system, possibly via combinational logic, then the sequential system may store a false value.

This problem can be solved by changing only one switch at a time, so there is never any ambiguity of position, resulting in codes assigning to each of a contiguous set of integers, or to each member of a circular list, a word of symbols such that no two code words are identical and each two adjacent code words differ by exactly one symbol. These codes are also known as *unit-distance*, *single-distance*, *single-step*, *monostrophic* or *syncopic codes*, in reference to the Hamming distance of 1 between adjacent codes.


## Invention

In principle, there can be more than one such code for a given word length, but the term Gray code was first applied to a particular binary code for non-negative integers, the *binary-reflected Gray code*, or **BRGC**. The Bell Labs researcher George R. Stibitz described such a code in a 1941 patent application, granted in 1943. Frank Gray introduced the term *reflected binary code* in his 1947 patent application, remarking that the code had "as yet no recognized name". He derived the name from the fact that it "may be built up from the conventional binary code by a sort of reflection process".

In the standard encoding of the Gray code the least significant bit follows a repetitive pattern of 2 on, 2 off (… 11001100 …); the next digit a pattern of 4 on, 4 off; the *i*-th least significant bit a pattern of 2*i* on 2*i* off. The most significant digit is an exception to this: for an *n*-bit Gray code, the most significant digit follows the pattern 2*n* − 1 on, 2*n* − 1 off, which is the same (cyclic) sequence of values as for the second-most significant digit, but shifted forwards 2*n* − 2 places. The four-bit version of this is shown below:

| Decimal | Binary | Gray |
|---|---|---|
| 0 | 0000 | 0000 |
| 1 | 0001 | 0001 |
| 2 | 0010 | 0011 |
| 3 | 0011 | 0010 |
| 4 | 0100 | 0110 |
| 5 | 0101 | 0111 |
| 6 | 0110 | 0101 |
| 7 | 0111 | 0100 |
| 8 | 1000 | 1100 |
| 9 | 1001 | 1101 |
| 10 | 1010 | 1111 |
| 11 | 1011 | 1110 |
| 12 | 1100 | 1010 |
| 13 | 1101 | 1011 |
| 14 | 1110 | 1001 |
| 15 | 1111 | 1000 |

For decimal 15 the code rolls over to decimal 0 with only one switch change. This is called the *cyclic* or *adjacency property* of the code.

In modern digital communications, Gray codes play an important role in error correction. For example, in a digital modulation scheme such as QAM where data are typically transmitted in symbols of four bits, or more, the signal's constellation diagram is arranged so that the bit patterns conveyed by adjacent constellation points differ by only one bit. By combining this with forward error correction capable of correcting single-bit errors, it is possible for a receiver to correct any transmission errors that cause a constellation point to deviate into the area of an adjacent point. This makes the transmission system less susceptible to noise.

Despite the fact that Stibitz described this code before Gray, the reflected binary code was later named after Gray by others who used it. Two different 1953 patent applications use "Gray code" as an alternative name for the "reflected binary code"; one of those also lists "minimum error code" and "cyclic permutation code" among the names. A 1954 patent application refers to "the Bell Telephone Gray code". Other names include "cyclic binary code", "cyclic progression code", "cyclic permuting binary" or "cyclic permuted binary" (CPB).

The Gray code is sometimes misattributed to 19th century electrical device inventor Elisha Gray.


## History and practical application

### Mathematical puzzles

Reflected binary codes were applied to mathematical puzzles before they became known to engineers.

The binary-reflected Gray code represents the underlying scheme of the classical Chinese rings puzzle, a sequential mechanical puzzle mechanism described by the French Louis Gros in 1872.

It can serve as a solution guide for the Towers of Hanoi problem, based on a game by the French Édouard Lucas in 1883. Similarly, the so-called Towers of Bucharest and Towers of Klagenfurt game configurations yield ternary and pentary Gray codes.

Martin Gardner wrote a popular account of the Gray code in his August 1972 "Mathematical Games" column in *Scientific American*.

The code also forms a Hamiltonian cycle in a hypercube graph, of length $2^{d}.$

### Telegraphy codes

When the French engineer Émile Baudot changed from using a 6-unit (6-bit) code to 5-unit code for his printing telegraph system, in 1875 or 1876, he ordered the alphabetic characters on his print wheel using a reflected binary code, and assigned the codes using only three of the bits to vowels. With vowels and consonants sorted in their alphabetical order, and other symbols appropriately placed, the 5-bit character code has been recognized as a reflected binary code. This code became known as Baudot code and, with minor changes, was eventually adopted as International Telegraph Alphabet No. 1 (ITA1, CCITT-1) in 1932.

About the same time, the German-Austrian Otto Schäffler demonstrated another printing telegraph in Vienna using a 5-bit reflected binary code for the same purpose, in 1874.

### Analog-to-digital signal conversion

Frank Gray, who became famous for inventing the signaling method that came to be used for compatible color television, invented a method to convert analog signals to reflected binary code groups using vacuum tube-based apparatus. Filed in 1947, the method and apparatus were granted a patent in 1953, and the name of Gray stuck to the codes. The "PCM tube" apparatus that Gray patented was made by Raymond W. Sears of Bell Labs, working with Gray and William M. Goodall, who credited Gray for the idea of the reflected binary code.

Gray was most interested in using the codes to minimize errors in converting analog signals to digital; his codes are still used today for this purpose.

### Position encoders

Gray codes are used in linear and rotary position encoders (absolute encoders and quadrature encoders) in preference to weighted binary encoding. This avoids the possibility that, when multiple bits change in the binary representation of a position, a misread will result from some of the bits changing before others.

For example, some rotary encoders provide a disk which has an electrically conductive Gray code pattern on concentric rings (tracks). Each track has a stationary metal spring contact that provides electrical contact to the conductive code pattern. Together, these contacts produce output signals in the form of a Gray code. Other encoders employ non-contact mechanisms based on optical or magnetic sensors to produce the Gray code output signals.

Regardless of the mechanism or precision of a moving encoder, position measurement error can occur at specific positions (at code boundaries) because the code may be changing at the exact moment it is read (sampled). A binary output code could cause significant position measurement errors because it is impossible to make all bits change at exactly the same time. If, at the moment the position is sampled, some bits have changed and others have not, the sampled position will be incorrect. In the case of absolute encoders, the indicated position may be far away from the actual position and, in the case of incremental encoders, this can corrupt position tracking.

In contrast, the Gray code used by position encoders ensures that the codes for any two consecutive positions will differ by only one bit and, consequently, only one bit can change at a time. In this case, the maximum position error will be small, indicating a position adjacent to the actual position.

### Genetic algorithms

Due to the Hamming distance properties of Gray codes, they are sometimes used in genetic algorithms. They may be useful in this field because mutations in the code allow for mostly incremental changes, but occasionally a single bit-change can cause a big leap and lead to new properties.

### Boolean circuit minimization

Gray codes are also used in labelling the axes of Karnaugh maps since 1953 as well as in Händler circle graphs since 1958, both graphical methods for logic circuit minimization.

### Error correction

In modern digital communications, 1D- and 2D-Gray codes play an important role in error prevention before applying an error correction. For example, in a digital modulation scheme such as QAM where data is typically transmitted in symbols of 4 bits or more, the signal's constellation diagram is arranged so that the bit patterns conveyed by adjacent constellation points differ by only one bit. By combining this with forward error correction capable of correcting single-bit errors, it is possible for a receiver to correct any transmission errors that cause a constellation point to deviate into the area of an adjacent point. This makes the transmission system less susceptible to noise.

- (Codes 4-PSK) Codes 4-PSK
- (Codes 8-PSK) Codes 8-PSK
- (Codes 16-QAM) Codes 16-QAM

### Communication between clock domains

Digital logic designers use Gray codes extensively for passing multi-bit count information between synchronous logic that operates at different clock frequencies. The logic is considered operating in different "clock domains". It is fundamental to the design of large chips that operate with many different clocking frequencies.

### Cycling through states with minimal effort

If a system has to cycle sequentially through all possible combinations of on-off states of some set of controls, and the changes of the controls require non-trivial expense (e.g. time, wear, human work), a Gray code minimizes the number of setting changes to just one change for each combination of states. An example would be testing a piping system for all combinations of settings of its manually operated valves.

A balanced Gray code can be constructed, that flips every bit equally often. Since bit-flips are evenly distributed, this is optimal in the following way: balanced Gray codes minimize the maximal count of bit-flips for each digit.

#### Gray code counters and arithmetic

George R. Stibitz utilized a reflected binary code in a binary pulse counting device in 1941.

A typical use of Gray code counters is building a FIFO (first-in, first-out) data buffer that has read and write ports that exist in different clock domains. The input and output counters inside such a dual-port FIFO are often stored using Gray code to prevent invalid transient states from being captured when the count crosses clock domains. The updated read and write pointers need to be passed between clock domains when they change, to be able to track FIFO empty and full status in each domain. Each bit of the pointers is sampled non-deterministically for this clock domain transfer. So for each bit, either the old value or the new value is propagated. Therefore, if more than one bit in the multi-bit pointer is changing at the sampling point, a "wrong" binary value (neither new nor old) can be propagated. By guaranteeing only one bit can be changing, Gray codes guarantee that the only possible sampled values are the new or old multi-bit value. Typically Gray codes of power-of-two length are used.

Sometimes digital buses in electronic systems are used to convey quantities that can only increase or decrease by one at a time, for example the output of an event counter which is being passed between clock domains or to a digital-to-analog converter. The advantage of Gray codes in these applications is that differences in the propagation delays of the many wires that represent the bits of the code cannot cause the received value to go through states that are out of the Gray code sequence. This is similar to the advantage of Gray codes in the construction of mechanical encoders, however the source of the Gray code is an electronic counter in this case. The counter itself must count in Gray code, or if the counter runs in binary then the output value from the counter must be reclocked after it has been converted to Gray code, because when a value is converted from binary to Gray code, it is possible that differences in the arrival times of the binary data bits into the binary-to-Gray conversion circuit will mean that the code could go briefly through states that are wildly out of sequence. Adding a clocked register after the circuit that converts the count value to Gray code may introduce a clock cycle of latency, so counting directly in Gray code may be advantageous.

To produce the next count value in a Gray-code counter, it is necessary to have some combinational logic that will increment the current count value that is stored. One way to increment a Gray code number is to convert it into ordinary binary code, add one to it with a standard binary adder, and then convert the result back to Gray code. Other methods of counting in Gray code are discussed in a report by Robert W. Doran, including taking the output from the first latches of the master-slave flip flops in a binary ripple counter.

#### Gray code addressing

As the execution of executable code typically causes an instruction memory access pattern of locally consecutive addresses, bus encodings using Gray code addressing instead of binary addressing can reduce the number of state changes of the address bits significantly, thereby reducing the CPU power consumption in some low-power designs.

#### Evenness and oddness of Gray codes

In the natural binary code system, the least significant bit indicates if the number is even (0) or odd (1), a property absent in the Gray code. Because just one bit is changed in consecutive Gray codes, the number of 1 bits will alternate between even and odd, so, to check a Gray code's evenness, it's necessary to count them, that is, an even number of 1s means the Gray code is even:

| Decimal | Binary | Evenness | Binary bit count | Gray | Gray bit count |
|---|---|---|---|---|---|
| 0 | 0000 | even | 0 | 0000 | 0 |
| 1 | 0001 | odd | 1 | 0001 | 1 |
| 2 | 0010 | even | 1 | 0011 | 2 |
| 3 | 0011 | odd | 2 | 0010 | 1 |
| 4 | 0100 | even | 1 | 0110 | 2 |
| 5 | 0101 | odd | 2 | 0111 | 3 |
| 6 | 0110 | even | 2 | 0101 | 2 |
| 7 | 0111 | odd | 3 | 0100 | 1 |
| 8 | 1000 | even | 1 | 1100 | 2 |
| 9 | 1001 | odd | 2 | 1101 | 3 |
| 10 | 1010 | even | 2 | 1111 | 4 |
| 11 | 1011 | odd | 3 | 1110 | 3 |
| 12 | 1100 | even | 2 | 1010 | 2 |
| 13 | 1101 | odd | 3 | 1011 | 3 |
| 14 | 1110 | even | 3 | 1001 | 2 |
| 15 | 1111 | odd | 4 | 1000 | 1 |

Some processors, like Zilog's Z80, Japan ASCII's R800, and Intel's 8086, have *parity* status flags, which indicate bitwise evenness of some registers, facilitating checking if the number of up bits in them is even.


## Constructing an *n*-bit Gray code

The binary-reflected Gray code list for *n* bits can be generated recursively from the list for *n* − 1 bits by reflecting the list (i.e. listing the entries in reverse order), prefixing the entries in the original list with a binary 0, prefixing the entries in the reflected list with a binary 1, and then concatenating the original list with the reversed list. For example, generating the *n* = 3 list from the *n* = 2 list:

| 2-bit list: | 00, 01, 11, 10 |   |
|---|---|---|
| Reflected: |   | 10, 11, 01, 00 |
| Prefix old entries with 0: | 000, 001, 011, 010, |   |
| Prefix new entries with 1: |   | 110, 111, 101, 100 |
| Concatenated: | 000, 001, 011, 010, | 110, 111, 101, 100 |

The one-bit Gray code is *G*1 = (0,1). This can be thought of as built recursively as above from a zero-bit Gray code *G*0 = ( Λ ) consisting of a single entry of zero length. This iterative process of generating *G**n*+1 from *G**n* makes the following properties of the standard reflecting code clear:

- *G**n* is a permutation of the numbers 0, …, 2*n* − 1. (Each number appears exactly once in the list.)
- *G**n* is embedded as the first half of *G**n*+1.
- Therefore, the coding is *stable*, in the sense that once a binary number appears in *G**n* it appears in the same position in all longer lists; so it makes sense to talk about *the* reflective Gray code value of a number: *G*(*m*) = the *m*th reflecting Gray code, counting from 0.
- Each entry in *G**n* differs by only one bit from the previous entry. (The Hamming distance is 1.)
- The last entry in *G**n* differs by only one bit from the first entry. (The code is cyclic.)

These characteristics suggest a simple and fast method of translating a binary value into the corresponding Gray code. Each bit is inverted if the next higher bit of the input value is set to one. This can be performed in parallel by a bit-shift and exclusive-or operation if they are available: the *n*th Gray code is obtained by computing $n\oplus \left\lfloor {\tfrac {n}{2}}\right\rfloor$ . Prepending a 0 bit leaves the order of the code words unchanged, prepending a 1 bit reverses the order of the code words. If the bits at position i of codewords are inverted, the order of neighbouring blocks of $2^{i}$ codewords is reversed. For example, if bit 0 is inverted in a 3 bit codeword sequence, the order of two neighbouring codewords is reversed

000,001,010,011,100,101,110,111 → 001,000,011,010,101,100,111,110

(invert bit 0)

If bit 1 is inverted, blocks of 2 codewords change order:

000,001,010,011,100,101,110,111 → 010,011,000,001,110,111,100,101

(invert bit 1)

If bit 2 is inverted, blocks of 4 codewords reverse order:

000,001,010,011,100,101,110,111 → 100,101,110,111,000,001,010,011

(invert bit 2)

Thus, performing an exclusive or on a bit $b_{i}$ at position i with the bit $b_{i+1}$ at position $i+1$ leaves the order of codewords intact if $b_{i+1}={\mathtt {0}}$ , and reverses the order of blocks of $2^{i+1}$ codewords if $b_{i+1}={\mathtt {1}}$ . Now, this is exactly the same operation as the reflect-and-prefix method to generate the Gray code.

A similar method can be used to perform the reverse translation, but the computation of each bit depends on the computed value of the next higher bit so it cannot be performed in parallel. Assuming $g_{i}$ is the i th Gray-coded bit ( $g_{0}$ being the most significant bit), and $b_{i}$ is the i th binary-coded bit ( $b_{0}$ being the most-significant bit), the reverse translation can be given recursively: $b_{0}=g_{0}$ , and $b_{i}=g_{i}\oplus b_{i-1}$ . Alternatively, decoding a Gray code into a binary number can be described as a prefix sum of the bits in the Gray code, where each individual summation operation in the prefix sum is performed modulo two.

To construct the binary-reflected Gray code iteratively, at step 0 start with the $\mathrm {code} _{0}={\mathtt {0}}$ , and at step $i>0$ find the bit position of the least significant 1 in the binary representation of i and flip the bit at that position in the previous code $\mathrm {code} _{i-1}$ to get the next code $\mathrm {code} _{i}$ . The bit positions start 0, 1, 0, 2, 0, 1, 0, 3, … See find first set for efficient algorithms to compute these values.


## Converting to and from Gray code

The following functions in C convert between binary numbers and their associated Gray codes. While it may seem that Gray-to-binary conversion requires each bit to be handled one at a time, faster algorithms exist.

```mw
typedef unsigned int uint;

// This function converts an unsigned binary number to reflected binary Gray code.
uint BinaryToGray(uint num)
{
    return num ^ (num >> 1); // The operator >> is shift right. The operator ^ is exclusive or.
}

// This function converts a reflected binary Gray code number to a binary number.
uint GrayToBinary(uint num)
{
    uint mask = num;
    while (mask) {           // Each Gray code bit is exclusive-ored with all more significant bits.
        mask >>= 1;
        num   ^= mask;
    }
    return num;
}

// A more efficient version for Gray codes 32 bits or fewer through the use of SWAR (SIMD within a register) techniques. 
// It implements a parallel prefix XOR function. The assignment statements can be in any order.
// 
// This function can be adapted for longer Gray codes by adding steps.

uint GrayToBinary32(uint num)
{
    num ^= num >> 16;
    num ^= num >>  8;
    num ^= num >>  4;
    num ^= num >>  2;
    num ^= num >>  1;
    return num;
}
// A Four-bit-at-once variant changes a binary number (abcd)2 to (abcd)2 ^ (00ab)2, then to (abcd)2 ^ (00ab)2 ^ (0abc)2 ^ (000a)2.
```

On newer processors, the number of ALU instructions in the decoding step can be reduced by taking advantage of the CLMUL instruction set. If MASK is the constant binary string of ones ended with a single zero digit, then carryless multiplication of MASK with the grey encoding of x will always give either x or its bitwise negation.
