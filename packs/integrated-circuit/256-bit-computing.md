---
title: "256-bit computing"
source: https://en.wikipedia.org/wiki/256-bit_computing
domain: integrated-circuit
license: CC-BY-SA-4.0
tags: integrated circuit
fetched: 2026-07-03
---

# 256-bit computing

In computer architecture, **256-bit** integers, memory addresses, or other data units are those that are 256 bits (32 octets) wide. Also, 256-bit central processing unit (CPU) and arithmetic logic unit (ALU) architectures are those that are based on registers, address buses, or data buses of that size. There are currently no mainstream general-purpose processors built to operate on 256-bit integers or addresses, though a number of processors do operate on 256-bit data.

## Representation

A 256-bit quantity can store 2256 different values. The range of integer values that can be stored in 256 bits depends on the integer representation used.

The range of a signed 256-bit integer is from `−57,896,044,618,658,097,711,785,492,504,343,953,926,634,992,332,820,282,019,728,792,003,956,564,819,968` to `57,896,044,618,658,097,711,785,492,504,343,953,926,634,992,332,820,282,019,728,792,003,956,564,819,967`.

256-bit processors could be used for addressing directly up to 2256 bytes. Already 2128 (for 128-bit addressing) would greatly exceed the total data stored on Earth as of 2018, which has been estimated to be around 33.3 ZBs (over 274 bytes).

## History

Xbox 360 was the first high-definition gaming console to utilize the ATI Technologies 256-bit GPU Xenos before the introduction of the current gaming consoles especially Nintendo Switch.

Some buses on the newer System on a chip (e.g. Tegra developed by Nvidia) utilize 64-bit, 128-bit, 256-bit, or higher.

## Hardware

CPUs feature SIMD instruction sets (Advanced Vector Extensions and the FMA instruction set etc.) where 256-bit vector registers are used to store several smaller numbers, such as eight 32-bit floating-point numbers, and a single instruction can operate on all these values in parallel. However, these processors do not operate on individual numbers that are 256 binary digits in length, only their registers have the size of 256-bits. Binary digits are found together in 128-bit collections.

Modern GPU chips may operate data across a 256-bit memory bus (or possibly a 512-bit bus with HBM3).

The Efficeon processor was Transmeta's second-generation 256-bit VLIW design which employed a software engine to convert code written for x86 processors to the native instruction set of the chip.

The DARPA funded Data-Intensive Architecture (DIVA) system incorporated processor-in-memory (PIM) 5-stage pipelined 256-bit datapath, complete with register file and ALU blocks in a "WideWord" processor in 2002.

## Software

- 256 bits is a common key size for symmetric ciphers in cryptography, such as Advanced Encryption Standard (AES).
- Increasing the word size can accelerate multiple precision mathematical libraries. Applications include cryptography.
- Researchers at the University of Cambridge use a 256-bit capability pointer, which includes capability and addressing information, on early implementations of their CHERI capability system.
- SHA-256 hash function.
- Smart contracts use 256- or 257-bit integers; 256-bit words for the Ethereum Virtual Machine. "We realize that a 257 bits byte is quite unusual, but for smart contracts it is ok to have at least 256 bits numbers. The leading VM for smart contracts, Ethereum VM, introduced this practice and other blockchain VMs followed."
- The Zig programming language has built-in support for signed and unsigned arbitrary bit-width integers for all supported platforms, including 256-bit. The calling convention for exported functions using such integers however, has not been specified in ABIs.
