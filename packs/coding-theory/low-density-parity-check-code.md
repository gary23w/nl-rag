---
title: "Low-density parity-check code"
source: https://en.wikipedia.org/wiki/Low-density_parity-check_code
domain: coding-theory
license: CC-BY-SA-4.0
tags: coding theory, linear code, hamming distance, convolutional code
fetched: 2026-07-02
---

# Low-density parity-check code

**Low-density parity-check** (**LDPC**) **codes**, also known as **Gallager codes**, are a class of error-correction codes first proposed in 1960. Together with the closely related turbo codes, they have gained prominence in coding theory and information theory since the late 1990s. The codes today are widely used in applications ranging from wireless communications to flash-memory storage. Together with turbo codes, they sparked a revolution in coding theory, achieving order-of-magnitude improvements in performance compared to traditional error correction codes.

LDPC codes were originally conceived by Robert G. Gallager in 1960. Gallager devised the codes in his doctoral dissertation at the Massachusetts Institute of Technology. The codes were largely ignored at the time, as their iterative decoding algorithm (despite having linear complexity) was prohibitively computationally expensive for the hardware available. They came back into favor in the mid 1990s, both because improved hardware made them practical, and because they provided a high performance and patent-free alternative to turbo codes.

Central to the performance of LDPC codes is their adaptability to the iterative belief-propagation decoding algorithm. Under this algorithm, they can be designed to approach theoretical limits (capacities) of many channels at low computation costs.

## History

Renewed interest in LDPC codes emerged following the invention of the closely related turbo codes (1993), whose similarly iterative decoding algorithm outperformed other codes used at that time. LDPC codes were subsequently rediscovered in 1996. Initial industry preference for LDPC codes over turbo codes stemmed from patent-related constraints on the latter. Since their discovery, advances in LDPC codes have seen them surpass turbo codes in terms of error floor and performance in the higher code rate range, leaving turbo codes better suited for the lower code rates. Although the fundamental patent for turbo codes expired in 2013, in many cases LDPC codes are still preferred for their technical merits.

Theoretical interest in LDPC codes also follows from their amenability to mathematical analysis. In his dissertation, Gallager showed that LDPC codes achieve the Gilbert–Varshamov bound for linear codes over binary fields with high probability. Over the binary erasure channel, code sequences were designed at rates arbitrarily close to channel capacity, with provably vanishing decoding error probability and linear decoding complexity. In 2020 it was shown that Gallager's LDPC codes achieve list decoding capacity and also achieve the Gilbert–Varshamov bound for linear codes over general fields.

Theoretically, analysis of LDPC codes focuses on sequences of codes of fixed code rate and increasing block length. These sequences are typically tailored to a set of channels. For appropriately designed sequences, the decoding error under belief propagation can often be proven to be vanishingly small (approaches zero with the block length) at rates that are very close to the capacities of the channels. Furthermore, this can be achieved at a complexity that is linear in the block length.

This theoretical performance is made possible using a flexible design method that is based on sparse Tanner graphs (specialized bipartite graphs).

LDPC code ensembles have also been analyzed using methods from statistical physics. Murayama, Kabashima, Saad, and Vicente studied regular LDPC codes through a spin-system analogy and the replica method, and later work extended this analysis to LDPC codes over Galois fields.

Since 2013, LDPC codes have also been proposed as a means of correcting errors in quantum computers, as they require few additional qubits to correct errors, as demonstrated by Gottesman, the University of Strasburg, Alice & Bob, and others. A 2025 study reported LDPC-CSS quantum codes for the quantum depolarizing channel whose numerical decoding performance approached the hashing bound, while retaining decoding complexity linear in the number of physical qubits.

## Applications

In 2003, an irregular repeat accumulate (IRA) style LDPC code beat six turbo codes to become the error-correcting code in the new DVB-S2 standard for digital television. The decision was based on technical factors such as ease of parallelization and error floors, plus the patent-free status of LDPC.

In 2008, LDPC beat convolutional turbo codes as the forward error correction (FEC) system for the ITU-T G.hn standard. G.hn chose LDPC codes over turbo codes because of their lower decoding complexity (especially when operating at data rates close to 1.0 Gbit/s) and because the proposed turbo codes exhibited a significant error floor at the desired range of operation.

LDPC codes are also used for 10GBASE-T Ethernet, which sends data at 10 gigabits per second over twisted-pair cables. As of 2009, LDPC codes are also part of the Wi-Fi 802.11 standard as an optional part of 802.11n and 802.11ac, in the High Throughput (HT) PHY specification. LDPC is a mandatory part of 802.11ax (Wi-Fi 6).

Some OFDM systems add an additional outer error correction that fixes the occasional errors (the "error floor") that get past the LDPC correction inner code even at low bit error rates. For example, the Reed-Solomon code with LDPC Coded Modulation (RS-LCM) uses a Reed-Solomon outer code. The DVB-S2, the DVB-T2, and the DVB-C2 standards all use a BCH code outer code to mop up residual errors after LDPC decoding.

5G NR uses polar code for the control channels and LDPC for the data channels.

Although LDPC code has had its success in commercial hard disk drives, to fully exploit its error correction capability in SSDs demands unconventional fine-grained flash memory sensing, leading to an increased memory read latency. LDPC-in-SSD is an effective approach to deploy LDPC in SSDs with a very small latency increase, which turns LDPC-in-SSD into a reality. Since then, LDPC has been widely adopted in commercial SSDs in both customer grades and enterprise grades by major storage vendors. Many TLC (and later) SSDs are using LDPC codes. A fast hard-decode (binary erasure) is first attempted, which can fall back into the slower but more powerful soft decoding.

## Operational use

LDPC codes functionally are defined by a sparse parity-check matrix. This sparse matrix is often randomly generated, subject to the sparsity constraints—LDPC code construction is discussed later. These codes were first designed by Robert Gallager in 1960.

Below is a graph fragment of an example LDPC code using Forney's factor graph notation. In this graph, *n* variable nodes in the top of the graph are connected to (*n*−*k*) constraint nodes in the bottom of the graph.

This is a popular way of graphically representing an (*n*, *k*) LDPC code. The bits of a valid message, when placed on the **T**s at the top of the graph, satisfy the graphical constraints. Specifically, all lines connecting to a variable node (box with an "=" sign) have the same value, and all values connecting to a factor node (box with a "+" sign) must sum, modulo two, to zero (in other words, they must sum to an even number, or there must be an even number of odd values).

Ignoring any lines going out of the picture, there are eight possible six-bit strings corresponding to valid codewords: (i.e., 000000, 001110, 010111, 011001, 100101, 101011, 110010, 111100). This LDPC code fragment represents a three-bit message encoded as six bits. Redundancy is used here to increase the chance of recovering from channel errors. This is a (6, 3) linear code, with *n* = 6 and *k* = 3.

Again ignoring lines going out of the picture, the parity-check matrix representing this graph fragment is

$\mathbf {H} ={\begin{pmatrix}1&1&1&1&0&0\\0&0&1&1&0&1\\1&0&0&1&1&0\\\end{pmatrix}}.$

In this matrix, each row represents one of the three parity-check constraints, while each column represents one of the six bits in the received codeword.

In this example, the eight codewords can be obtained by putting the parity-check matrix **H** into this form ${\begin{bmatrix}-P^{T}|I_{n-k}\end{bmatrix}}$ through basic row operations in GF(2):

$\mathbf {H} ={\begin{pmatrix}1&1&1&1&0&0\\0&0&1&1&0&1\\1&0&0&1&1&0\\\end{pmatrix}}_{1}\sim {\begin{pmatrix}1&1&1&1&0&0\\0&0&1&1&0&1\\0&1&1&0&1&0\\\end{pmatrix}}_{2}\sim {\begin{pmatrix}1&1&1&1&0&0\\0&1&1&0&1&0\\0&0&1&1&0&1\\\end{pmatrix}}_{3}\sim {\begin{pmatrix}1&1&1&1&0&0\\0&1&1&0&1&0\\1&1&0&0&0&1\\\end{pmatrix}}_{4}.$

Step 1: H.

Step 2: Row 1 is added to row 3.

Step 3: Row 2 and 3 are swapped.

Step 4: Row 1 is added to row 3.

From this, the generator matrix **G** can be obtained as ${\begin{bmatrix}I_{k}|P\end{bmatrix}}$ (noting that in the special case of this being a binary code $P=-P$ ), or specifically:

$\mathbf {G} ={\begin{pmatrix}1&0&0&1&0&1\\0&1&0&1&1&1\\0&0&1&1&1&0\\\end{pmatrix}}.$

Finally, by multiplying all eight possible 3-bit strings by **G**, all eight valid codewords are obtained. For example, the codeword for the bit-string "101" is obtained by

${\begin{pmatrix}1&0&1\\\end{pmatrix}}\odot {\begin{pmatrix}1&0&0&1&0&1\\0&1&0&1&1&1\\0&0&1&1&1&0\\\end{pmatrix}}={\begin{pmatrix}1&0&1&0&1&1\\\end{pmatrix}}$

,

where $\odot$ is symbol of mod 2 multiplication.

As a check, the row space of **G** is orthogonal to **H** such that $G\odot H^{T}=0$ .

The input bit-string "101" is found as the first 3 bits of the codeword "101011", due to the presence of the identity matrix $I_{k}$ . The trailing three bits "011" of the codeword are the parity bits.

## Example encoder

Each bit of all possible messages can be generated by direct multiplication with the G matrix defined in the previous section. However, this method is seldom used in practice, where codes are picked for ease of encoding. In practice this means the input bits are copied straight to the output, and the check bits computed with a series of encoders. In theory there can be one encoder required for each check bit, but in practice the hardware cost is reduced by picking encoders that can be re-used.

During the encoding of a frame, the input data bits (D) are repeated and distributed to a set of constituent encoders. The constituent encoders are typically accumulators and each accumulator is used to generate a parity symbol. A single copy of the original data (S0,K-1) is transmitted with the parity bits (P) to make up the code symbols. The S bits from each constituent encoder are discarded.

The parity bit may be used within another constituent code.

In an example using the DVB-S2 rate 2/3 code the encoded block size is 64800 symbols (N=64800) with 43200 data bits (K=43200) and 21600 parity bits (M=21600). Each constituent code (check node) encodes 16 data bits except for the first parity bit which encodes 8 data bits. The first 4680 data bits are repeated 13 times (used in 13 parity codes), while the remaining data bits are used in 3 parity codes (irregular LDPC code).

For comparison, classic turbo codes typically use two constituent codes configured in parallel, each of which encodes the entire input block (K) of data bits. These constituent encoders are recursive convolutional codes (RSC) of moderate depth (8 or 16 states) that are separated by a code interleaver which interleaves one copy of the frame.

The LDPC code, in contrast, uses many low depth constituent codes (accumulators) in parallel, each of which encode only a small portion of the input frame. The many constituent codes can be viewed as many low depth (2 state) "convolutional codes" that are connected via the repeat and distribute operations. The repeat and distribute operations perform the function of the interleaver in the turbo code.

The ability to more precisely manage the connections of the various constituent codes and the level of redundancy for each input bit give more flexibility in the design of LDPC codes, which can lead to better performance than turbo codes in some instances. Turbo codes still seem to perform better than LDPCs at low code rates, or at least the design of well performing low rate codes is easier for turbo codes.

As a practical matter, the hardware that forms the accumulators is reused during the encoding process. That is, once a first set of parity bits are generated and the parity bits stored, the same accumulator hardware is used to generate a next set of parity bits.

## Decoding

As with other codes, the maximum likelihood decoding of an LDPC code on the binary symmetric channel is an NP-complete problem, shown by reduction from 3-dimensional matching. So assuming P != NP, which is widely believed, then performing optimal decoding for an arbitrary code of any useful size is not practical.

However, sub-optimal techniques based on iterative belief propagation decoding give excellent results and can be practically implemented. The sub-optimal decoding techniques view each parity check that makes up the LDPC as an independent single parity check (SPC) code. Each SPC code is decoded separately using soft-in-soft-out (SISO) techniques such as SOVA, BCJR, MAP, and other derivates thereof. The soft decision information from each SISO decoding is cross-checked and updated with other redundant SPC decodings of the same information bit. Each SPC code is then decoded again using the updated soft decision information. This process is iterated until a valid codeword is achieved or decoding is exhausted. This type of decoding is often referred to as sum-product decoding.

The decoding of the SPC codes is often referred to as the "check node" processing, and the cross-checking of the variables is often referred to as the "variable-node" processing.

In a practical LDPC decoder implementation, sets of SPC codes are decoded in parallel to increase throughput.

In contrast, belief propagation on the binary erasure channel is particularly simple where it consists of iterative constraint satisfaction.

For example, consider that the valid codeword, 101011, from the example above, is transmitted across a binary erasure channel and received with the first and fourth bit erased to yield ?01?11. Since the transmitted message must have satisfied the code constraints, the message can be represented by writing the received message on the top of the factor graph.

In this example, the first bit cannot yet be recovered, because all of the constraints connected to it have more than one unknown bit. In order to proceed with decoding the message, constraints connecting to only one of the erased bits must be identified. In this example, only the second constraint suffices. Examining the second constraint, the fourth bit must have been zero, since only a zero in that position would satisfy the constraint.

This procedure is then iterated. The new value for the fourth bit can now be used in conjunction with the first constraint to recover the first bit as seen below. This means that the first bit must be a one to satisfy the leftmost constraint.

Thus, the message can be decoded iteratively. For other channel models, the messages passed between the variable nodes and check nodes are real numbers, which express probabilities and likelihoods of belief.

This result can be validated by multiplying the corrected codeword **r** by the parity-check matrix **H**:

$\mathbf {z} =\mathbf {H\odot r} ={\begin{pmatrix}1&1&1&1&0&0\\0&0&1&1&0&1\\1&0&0&1&1&0\\\end{pmatrix}}\odot {\begin{pmatrix}1\\0\\1\\0\\1\\1\\\end{pmatrix}}={\begin{pmatrix}0\\0\\0\\\end{pmatrix}}.$

Because the outcome **z** (the syndrome) of this operation is the three × one zero vector, the resulting codeword **r** is successfully validated.

After the decoding is completed, the original message bits '101' can be extracted by looking at the first 3 bits of the codeword.

While illustrative, this erasure example does not show the use of soft-decision decoding or soft-decision message passing, which is used in virtually all commercial LDPC decoders.

### Updating node information

Starting in 2010, there has also been a great deal of work spent studying the effects of alternative schedules for variable-node and constraint-node update. The original technique that was used for decoding LDPC codes was known as *flooding*. This type of update required that, before updating a variable node, all constraint nodes needed to be updated and vice versa. In later work by Vila Casado *et al.*, alternative update techniques were studied, in which variable nodes are updated with the newest available check-node information.

The intuition behind these algorithms is that variable nodes whose values vary the most are the ones that need to be updated first. Highly reliable nodes, whose log-likelihood ratio (LLR) magnitude is large and does not change significantly from one update to the next, do not require updates with the same frequency as other nodes, whose sign and magnitude fluctuate more widely. These scheduling algorithms show greater speed of convergence and lower error floors than those that use flooding. These lower error floors are achieved by the ability of the Informed Dynamic Scheduling (IDS) algorithm to overcome trapping sets of near codewords.

When nonflooding scheduling algorithms are used, an alternative definition of iteration is used. For an (*n*, *k*) LDPC code of rate *k*/*n*, a full *iteration* occurs when *n* variable and *n* − *k* constraint nodes have been updated, no matter the order in which they were updated.

## Code construction

For large block sizes, LDPC codes are commonly constructed by first studying the behaviour of decoders. As the block size tends to infinity, LDPC decoders can be shown to have a noise threshold below which decoding is reliably achieved, and above which decoding is not achieved, colloquially referred to as the cliff effect. This threshold can be optimised by finding the best proportion of arcs from check nodes and arcs from variable nodes. An approximate graphical approach to visualising this threshold is an EXIT chart.

The construction of a specific LDPC code after this optimization falls into two main types of techniques:

- Pseudorandom approaches
- Combinatorial approaches

Construction by a pseudo-random approach builds on theoretical results that, for large block size, a random construction gives good decoding performance. In general, pseudorandom codes have complex encoders, but pseudorandom codes with the best decoders can have simple encoders. Various constraints are often applied to help ensure that the desired properties expected at the theoretical limit of infinite block size occur at a finite block size.

Combinatorial approaches can be used to optimize the properties of small block-size LDPC codes or to create codes with simple encoders.

Some LDPC codes are based on Reed–Solomon codes, such as the RS-LDPC code used in the 10 Gigabit Ethernet standard. Compared to randomly generated LDPC codes, structured LDPC codes—such as the LDPC code used in the DVB-S2 standard—can have simpler and therefore lower-cost hardware—in particular, codes constructed such that the H matrix is a circulant matrix.

Yet another way of constructing LDPC codes is to use finite geometries. This method was proposed by Y. Kou *et al.* in 2001.

## Compared to turbo codes

LDPC codes can be compared with other powerful coding schemes, e.g. turbo codes. In one hand, BER performance of turbo codes is influenced by low codes limitations. LDPC codes have no limitations of minimum distance, that indirectly means that LDPC codes may be more efficient on relatively large code rates (e.g. 3/4, 5/6, 7/8) than turbo codes. However, LDPC codes are not the complete replacement: turbo codes are the best solution at the lower code rates (e.g. 1/6, 1/3, 1/2).
