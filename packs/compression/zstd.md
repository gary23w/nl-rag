---
title: "zstd"
source: https://en.wikipedia.org/wiki/Zstd
domain: compression
license: CC-BY-SA-4.0
tags: data compression, huffman, lz77, deflate, run-length encoding, codec
fetched: 2026-07-02
---

# zstd

**Zstandard** is a lossless data compression algorithm developed by Yann Collet at Facebook. **Zstd** is the corresponding reference implementation in C, released as open-source software on 31 August 2016.

The algorithm was published in 2018 as RFC 8478, which also defines an associated media type "application/zstd", filename extension "zst", and HTTP content encoding "zstd".

## Features

Zstandard was designed to give a compression ratio comparable to that of the DEFLATE algorithm (developed in 1991 and used in the original ZIP and gzip programs), but faster, especially for decompression. It is tunable with compression levels ranging from negative 7 (fastest) to 22 (slowest in compression speed, but best compression ratio).

Starting from version 1.3.2 (October 2017), zstd optionally implements very-long-range search and deduplication (`--long`, 128 MiB window) similar to rzip or lrzip.

Compression speed can vary by a factor of 20 or more between the fastest and slowest levels, while decompression is uniformly fast, varying by less than 20% between the fastest and slowest levels. The Zstandard command-line has an "adaptive" (`--adapt`) mode that varies compression level depending on I/O conditions, mainly how fast it can write the output.

Zstandard at its maximum compression level gives a compression ratio close to lzma, lzham, and ppmx. As of 2019, Zstandard reaches the Pareto frontier for decompression, as it produces output faster than any other open source algorithm with a similar or better compression ratio.

Dictionaries can have a large impact on the compression ratio of small files, so Zstandard can use a user-provided compression dictionary. It also offers a training mode, able to generate a dictionary from a set of samples. In particular, one dictionary can be loaded to process large sets of files with redundancy between files, but not necessarily within each file, such as for log files.

## Design

Zstandard combines a dictionary-matching stage (LZ77) with a large search window and a fast entropy-coding stage. It uses Huffman coding alongside finite-state entropy (FSE), a variant of tANS.

## Usage

The Linux kernel has included Zstandard since November 2017 (version 4.14) as a compression method for the btrfs and squashfs filesystems, as well as for loadable kernel modules.

In 2017, Allan Jude integrated Zstandard into the FreeBSD kernel, and it was subsequently integrated as a compressor option for core dumps (both user programs and kernel panics). It was also used to create a proof-of-concept OpenZFS compression method which was integrated in 2020.

The AWS Redshift and RocksDB databases include support for field compression using Zstandard.

In March 2018, Canonical tested the use of zstd as a deb package compression method by default for the Ubuntu Linux distribution. Compared with xz compression of deb packages, zstd at level 19 decompresses significantly faster, but at the cost of 6% larger package files. Support was added to Debian (and subsequently, Ubuntu) in April 2018 (in version 1.6~rc1).

Fedora added ZStandard support to RPM in May 2018 (Fedora release 28) and used it for packaging the release in October 2019 (Fedora 31). In Fedora 33, the filesystem is compressed by default with zstd.

Arch Linux added support for zstd as a package compression method in October 2019 with the release of the pacman 5.2 package manager and in January 2020 switched from xz to zstd for the packages in the official repository. Arch uses `zstd -c -T0 --ultra -20 -`; while the size of all compressed packages combined increased by 0.8% (compared to xz), the decompression speed is 14 times faster, decompression memory increased by 50 MiB when using multiple threads, and compression memory increased but scales with the number of threads used. Arch Linux later also switched to zstd as the default compression algorithm for mkinitcpio initial ramdisk generator.

On 15 June 2020, Zstandard was implemented in version 6.3.8 of the zip file format with codec number 93, deprecating the previous codec number of 20 as it was implemented in version 6.3.7, released on 1 June.

On 31 October 2023 Official Zstd support for compression/decompression was added to Windows Explorer in Windows 11 (via update package KB5031455)

In March 2024, Google Chrome version 123 (and Chromium-based browsers such as Brave or Microsoft Edge) added zstd support in the HTTP header `Content-Encoding`. In May 2024, Firefox release 126.0 added zstd support in the HTTP header `Content-Encoding`.

## License

The reference implementation is licensed under the BSD license, published at GitHub. Since version 1.0, published 31 August 2016, it had an additional Grant of Patent Rights.

From version 1.3.1, released 20 August 2017, this patent grant was dropped and the license was changed to a BSD + GPLv2 dual license.
