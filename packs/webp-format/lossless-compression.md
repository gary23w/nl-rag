---
title: "Lossless compression"
source: https://en.wikipedia.org/wiki/Lossless_compression
domain: webp-format
license: CC-BY-SA-4.0
tags: webp image, vp8 intra, lossy webp, web image format
fetched: 2026-07-02
---

# Lossless compression

**Lossless compression** is a class of data compression that allows the original data to be perfectly reconstructed from the compressed data with no loss of information. Lossless compression is possible because most real-world data exhibits statistical redundancy. By contrast, lossy compression permits reconstruction only of an approximation of the original data, though usually with greatly improved compression rates (and therefore reduced media sizes).

By operation of the pigeonhole principle, no lossless compression algorithm can shrink the size of all possible data: Some data will get longer by at least one symbol or bit.

Compression algorithms are usually effective for human- and machine-readable documents and cannot shrink the size of random data that contain no redundancy. Different algorithms exist that are designed either with a specific type of input data in mind or with specific assumptions about what kinds of redundancy the uncompressed data are likely to contain.

Lossless data compression is used in many applications. For example, it is used in the ZIP file format and in the GNU tool gzip. It is also often used as a component within lossy data compression technologies (e.g. lossless mid/side joint stereo preprocessing by MP3 encoders and other lossy audio encoders).

Lossless compression is used in cases where it is important that the original and the decompressed data be identical, or where deviations from the original data would be unfavourable. Common examples are executable programs, text documents, and source code. Some image file formats, like PNG or GIF, use only lossless compression, while others like TIFF and MNG may use either lossless or lossy methods. Lossless audio formats are most often used for archiving or production purposes, while smaller lossy audio files are typically used on portable players and in other cases where storage space is limited or exact replication of the audio is unnecessary.

## Techniques

Most lossless compression programs do two things in sequence: the first step generates a *statistical model* for the input data, and the second step uses this model to map input data to bit sequences in such a way that "probable" (i.e. frequently encountered) data will produce shorter output than "improbable" data.

The primary encoding algorithms used to produce bit sequences are Huffman coding (also used by the deflate algorithm) and arithmetic coding. Arithmetic coding achieves compression rates close to the best possible for a particular statistical model, which is given by the information entropy, whereas Huffman compression is simpler and faster but produces poor results for models that deal with symbol probabilities close to 1.

There are two primary ways of constructing statistical models: in a *static* model, the data is analyzed and a model is constructed, then this model is stored with the compressed data. This approach is simple and modular, but has the disadvantage that the model itself can be expensive to store, and also that it forces using a single model for all data being compressed, and so performs poorly on files that contain heterogeneous data. *Adaptive* models dynamically update the model as the data is compressed. Both the encoder and decoder begin with a trivial model, yielding poor compression of initial data, but as they learn more about the data, performance improves. Most popular types of compression used in practice now use adaptive coders.

Lossless compression methods may be categorized according to the type of data they are designed to compress. While, in principle, any general-purpose lossless compression algorithm (*general-purpose* meaning that they can accept any bitstring) can be used on any type of data, many are unable to achieve significant compression on data that are not of the form for which they were designed to compress. Many of the lossless compression techniques used for text also work reasonably well for indexed-color images.

### Multimedia

These techniques take advantage of the specific characteristics of images such as the common phenomenon of contiguous 2-D areas of similar tones. Every pixel but the first is replaced by the difference to its left neighbor. This leads to small values having a much higher probability than large values. This is often also applied to sound files, and can compress files that contain mostly low frequencies and low volumes. For images, this step can be repeated by taking the difference to the top pixel, and then in videos, the difference to the pixel in the next frame can be taken.

The adaptive encoding uses the probabilities from the previous sample in sound encoding, from the left and upper pixel in image encoding, and additionally from the previous frame in video encoding. In the wavelet transformation, the probabilities are also passed through the hierarchy.

### Historical legal issues

Many of these methods are implemented in open-source and proprietary tools, particularly LZW and its variants. Some algorithms are patented in the United States and other countries and their legal usage requires licensing by the patent holder. Because of patents on certain kinds of LZW compression, and in particular licensing practices by patent holder Unisys that many developers considered abusive, some open source proponents encouraged people to avoid using the Graphics Interchange Format (GIF) for compressing still image files in favor of Portable Network Graphics (PNG), which combines the LZ77-based deflate algorithm with a selection of domain-specific prediction filters. However, the patents on LZW expired on June 20, 2003.

Many of the lossless compression techniques used for text also work reasonably well for indexed images, but there are other techniques that do not work for typical text that are useful for some images (particularly simple bitmaps), and other techniques that take advantage of the specific characteristics of images (such as the common phenomenon of contiguous 2-D areas of similar tones, and the fact that color images usually have a preponderance of a limited range of colors out of those representable in the color space).

As mentioned previously, lossless sound compression is a somewhat specialized area. Lossless sound compression algorithms can take advantage of the repeating patterns shown by the wave-like nature of the data‍—‍essentially using autoregressive models to predict the "next" value and encoding the (possibly small) difference between the expected value and the actual data. If the difference between the predicted and the actual data (called the *error*) tends to be small, then certain difference values (like 0, +1, −1 etc. on sample values) become very frequent, which can be exploited by encoding them in few output bits.

It is sometimes beneficial to compress only the differences between two versions of a file (or, in video compression, of successive images within a sequence). This is called delta encoding (from the Greek letter Δ, which in mathematics, denotes a difference), but the term is typically only used if both versions are meaningful outside compression and decompression. For example, while the process of compressing the error in the above-mentioned lossless audio compression scheme could be described as delta encoding from the approximated sound wave to the original sound wave, the approximated version of the sound wave is not meaningful in any other context.

## Methods

No lossless compression algorithm can efficiently compress all possible data . For this reason, many different algorithms exist that are designed either with a specific type of input data in mind or with specific assumptions about what kinds of redundancy the uncompressed data are likely to contain.

Some of the most common lossless compression algorithms are listed below.

### General purpose

- ANS – Entropy encoding, used by LZFSE and Zstandard
- Arithmetic coding – Entropy encoding
- Burrows–Wheeler transform reversible transform for making textual data more compressible, used by bzip2
- Huffman coding – Entropy encoding, pairs well with other algorithms
- Lempel-Ziv compression (LZ77 and LZ78) – Dictionary-based algorithm that forms the basis for many other algorithms
  - Deflate – Combines LZ77 with Huffman coding, used by ZIP, gzip, zlib, and PNG images
  - Brotli – Uses LZ77 with a high sliding window size (up to 16 MiB), Huffman coding, and context modeling.
  - LZ4 – Very fast compression and decompression.
  - Lempel–Ziv–Markov chain algorithm (LZMA) – Very high compression ratio, used by 7zip and xz
  - Lempel–Ziv–Storer–Szymanski (LZSS) – Used by WinRAR in tandem with Huffman coding
  - Lempel–Ziv–Welch (LZW) – Used by GIF images and Unix's `compress` utility
- Prediction by partial matching (PPM) – Optimized for compressing plain text
- Run-length encoding (RLE) – Simple scheme that provides good compression of data containing many runs of the same value

### Audio

- Adaptive Transform Acoustic Coding (ATRAC)
- Apple Lossless (ALAC – Apple Lossless Audio Codec)
- Audio Lossless Coding (also known as MPEG-4 ALS)
- Direct Stream Transfer (DST)
- Dolby TrueHD
- DTS-HD Master Audio
- Free Lossless Audio Codec (FLAC)
- Meridian Lossless Packing (MLP)
- Monkey's Audio (Monkey's Audio APE)
- MPEG-4 SLS (also known as HD-AAC)
- OptimFROG
- Original Sound Quality (OSQ)
- RealPlayer (RealAudio Lossless)
- Shorten (SHN)
- TTA (True Audio Lossless)
- WavPack (WavPack lossless)
- Windows Media Audio 9 Lossless (WMA Lossless)

### Raster graphics

- Lossless only encoding
  - BMP
  - PNG – Portable Network Graphics
  - GIF – Graphics Interchange Format
- Lossy and Lossless encoding options
  - AVIF – AV1 Image File Format
  - FLIF – Free Lossless Image Format
  - HEIF – High Efficiency Image File Format, using HEVC
  - ILBM – (RLE compression of Amiga IFF images)
  - JBIG2 – compression of B&W images
  - JPEG 2000 – (via Le Gall–Tabatabai 5/3 reversible integer wavelet transform)
  - JPEG-LS
  - JPEG XL
  - JPEG XR – formerly *WMPhoto* and *HD Photo*
  - LDCT – Discrete Cosine Transform
  - PCX – PiCture eXchange
  - QOI – Quite OK Image Format
  - TGA – Truevision TGA
  - TIFF – Tag Image File Format
  - WebP

### 3D Graphics

- OpenCTM – Lossless compression of 3D triangle meshes

### Video

See list of lossless video codecs

### Cryptography

Cryptosystems often compress data (the "plaintext") *before* encryption for added security. When properly implemented, compression greatly increases the unicity distance by removing patterns that might facilitate cryptanalysis. However, many ordinary lossless compression algorithms produce headers, wrappers, tables, or other predictable output that might instead make cryptanalysis easier. Thus, cryptosystems must utilize compression algorithms whose output does not contain these predictable patterns.

### Genetics and genomics

Genetics compression algorithms (not to be confused with genetic algorithms) are the latest generation of lossless algorithms that compress data (typically sequences of nucleotides) using both conventional compression algorithms and specific algorithms adapted to genetic data. In 2012, a team of scientists from Johns Hopkins University published the first genetic compression algorithm that does not rely on external genetic databases for compression. HAPZIPPER was tailored for HapMap data and achieves over 20-fold compression (95% reduction in file size), providing 2- to 4-fold better compression much faster than leading general-purpose compression utilities.

Genomic sequence compression algorithms, also known as DNA sequence compressors, explore the fact that DNA sequences have characteristic properties, such as inverted repeats. The most successful compressors are XM and GeCo. For eukaryotes XM is slightly better in compression ratio, though for sequences larger than 100 MB its computational requirements are impractical.

### Executables

Self-extracting executables contain a compressed application and a decompressor. When executed, the decompressor transparently decompresses and runs the original application. This is especially often used in demo coding, where competitions are held for demos with strict size limits, as small as 1 kilobyte. This type of compression is not strictly limited to binary executables, but can also be applied to scripts, such as JavaScript.

## Benchmarks

Lossless compression algorithms and their implementations are routinely tested in head-to-head benchmarks. There are a number of better-known compression benchmarks. Some benchmarks cover only the data compression ratio, so winners in these benchmarks may be unsuitable for everyday use due to the slow speed of the top performers. Another drawback of some benchmarks is that their data files are known, so some program writers may optimize their programs for best performance on a particular data set. The winners on these benchmarks often come from the class of context-mixing compression software.

Matt Mahoney, in his February 2010 edition of the free booklet *Data Compression Explained*, additionally lists the following:

- The Calgary Corpus dating back to 1987 is no longer widely used due to its small size. Matt Mahoney maintained the Calgary Compression Challenge, created and maintained from May 21, 1996, through May 21, 2016, by Leonid A. Broukhis.
- The Large Text Compression Benchmark and the similar Hutter Prize both use a trimmed Wikipedia XML UTF-8 data set.
- The Generic Compression Benchmark, maintained by Matt Mahoney, tests compression of data generated by random Turing machines.
- Sami Runsas (the author of NanoZip) maintained Compression Ratings, a benchmark similar to Maximum Compression multiple file test, but with minimum speed requirements. It offered the calculator that allowed the user to weight the importance of speed and compression ratio. The top programs were fairly different due to the speed requirement. In January 2010, the top program was NanoZip followed by FreeArc, CCM, flashzip, and 7-Zip.
- The Monster of Compression benchmark by Nania Francesco Antonio tested compression on 1Gb of public data with a 40-minute time limit. In December 2009, the top ranked archiver was NanoZip 0.07a and the top ranked single file compressor was ccmx 1.30c.

The Compression Ratings website published a chart summary of the "frontier" in compression ratio and time.

### Silesia corpus

The **Silesia corpus** is a collection of files that was created in 2003 as an alternative for the Canterbury corpus and Calgary corpus, based on concerns about how well these represented modern files. It contains various data types, including large text documents, executable files, and databases. It is widely used in data compression research.

The corpus consists of 12 files, totaling 211MB. The files were chosen to represent what the author considered to be data types likely to grow rapidly in size over time, such as computer programs and databases, along with more traditional compression benchmarks, such as large text files.

| File | Size (B) | Description | Type of data |
|---|---|---|---|
| dickens | 10192446 | The works of Charles Dickens | English text |
| mozilla | 51220480 | Executable files for Mozilla 1.0 | Executable |
| mr | 9970564 | MRI Images | 3D image |
| nci | 33553445 | A database of chemical structures | Database |
| office | 6152192 | A shared library from OpenOffice | Executable |
| osdb | 10085684 | A Sample MySQL database from the Open Source Database Benchmark | Database |
| reymont | 6625583 | The text of the book *Chłopi* by Władysław Reymont | PDF in Polish |
| samba | 21606400 | The source code of Samba 2‑2.3 | Executable |
| sao | 7251944 | The SAO star catalogue | Binary database |
| webster | 41458703 | The 1913 Webster Unabridged Dictionary | HTML |
| xml | 5345280 | Collected XML files | XML |
| x-ray | 8474240 | A medical X-Ray | Image |
| **Total** | 211938580 |   |   |

Because it has a broader and more modern selection of datatypes, it is considered a better source of test data for compression algorithms when compared to the Calgary corpus.

## Limitations

Lossless data compression algorithms cannot guarantee compression for all input data sets. In other words, for any lossless data compression algorithm, there will be an input data set that does not get smaller when processed by the algorithm, and for any lossless data compression algorithm that makes at least one file smaller, there will be at least one file that it makes larger. This is easily proven with elementary mathematics using a counting argument called the pigeonhole principle, as follows:

- Assume that each file is represented as a string of bits of some arbitrary length.
- Suppose that there is a compression algorithm that transforms every file into an output file that is no longer than the original file, and that at least one file will be compressed into an output file that is shorter than the original file.
- Let *M* be the least number such that there is a file *F* with length *M* bits that compresses to something shorter. Let *N* be the length (in bits) of the compressed version of *F*.
- Because *N*<*M*, **every** file of length *N* keeps its size during compression. There are 2*N* such files possible. Together with *F*, this makes 2*N*+1 files that all compress into one of the 2*N* files of length *N*.
- But 2*N* is smaller than 2*N*+1, so by the pigeonhole principle there must be some file of length *N* that is simultaneously the output of the compression function on two different inputs. That file cannot be decompressed reliably (which of the two originals should that yield?), which contradicts the assumption that the algorithm was lossless.
- We must therefore conclude that our original hypothesis (that the compression function makes no file longer) is necessarily untrue.

Most practical compression algorithms provide an "escape" facility that can turn off the normal coding for files that would become longer by being encoded. In theory, only a single additional bit is required to tell the decoder that the normal coding has been turned off for the entire input; however, most encoding algorithms use at least one full byte (and typically more than one) for this purpose. For example, deflate compressed files never need to grow by more than 5 bytes per 65,535 bytes of input.

In fact, if we consider files of length N, if all files were equally probable, then for any lossless compression that reduces the size of some file, the expected length of a compressed file (averaged over all possible files of length N) must necessarily be *greater* than N. So if we know nothing about the properties of the data we are compressing, we might as well not compress it at all. A lossless compression algorithm is useful only when we are more likely to compress certain types of files than others; then the algorithm could be designed to compress those types of data better.

Thus, the main lesson from the argument is not that one risks big losses, but merely that one cannot always win. To choose an algorithm always means implicitly to select a *subset* of all files that will become usefully shorter. This is the theoretical reason why we need to have different compression algorithms for different kinds of files: there cannot be any algorithm that is good for all kinds of data.

The "trick" that allows lossless compression algorithms, used on the type of data they were designed for, to consistently compress such files to a shorter form is that the files the algorithms are designed to act on all have some form of easily modeled redundancy that the algorithm is designed to remove, and thus belong to the subset of files that that algorithm can make shorter, whereas other files would not get compressed or even get bigger. Algorithms are generally quite specifically tuned to a particular type of file: for example, lossless audio compression programs do not work well on text files, and vice versa.

In particular, files of random data cannot be consistently compressed by any conceivable lossless data compression algorithm; indeed, this result is used to *define* the concept of randomness in Kolmogorov complexity.

It is provably impossible to create an algorithm that can losslessly compress any data. While there have been many claims through the years of companies achieving "perfect compression" where an arbitrary number *N* of random bits can always be compressed to *N* − 1 bits, these kinds of claims can be safely discarded without even looking at any further details regarding the purported compression scheme. Such an algorithm contradicts fundamental laws of mathematics because, if it existed, it could be applied repeatedly to losslessly reduce any file to length 1.

On the other hand, it has also been proven that there is no algorithm to determine whether a file is incompressible in the sense of Kolmogorov complexity. Hence it is possible that any particular file, even if it appears random, may be significantly compressed, even including the size of the decompressor. An example is the digits of the mathematical constant *pi*, which appear random but can be generated by a very small program. However, even though it cannot be determined whether a particular file is incompressible, a simple theorem about incompressible strings shows that over 99% of files of any given length cannot be compressed by more than one byte (including the size of the decompressor).

### Mathematical background

Abstractly, a compression algorithm can be viewed as a function on sequences (normally of octets). Compression is successful if the resulting sequence is shorter than the original sequence (and the instructions for the decompression map). For a compression algorithm to be lossless, the compression map must form an injection from "plain" to "compressed" bit sequences. The pigeonhole principle prohibits a bijection between the collection of sequences of length *N* and any subset of the collection of sequences of length *N*−1. Therefore, it is not possible to produce a lossless algorithm that reduces the size of every possible input sequence.

### Points of application in real compression theory

Real compression algorithm designers accept that streams of high information entropy cannot be compressed, and accordingly, include facilities for detecting and handling this condition. An obvious way of detection is applying a raw compression algorithm and testing if its output is smaller than its input. Sometimes, detection is made by heuristics; for example, a compression application may consider files whose names end in ".zip", ".arj" or ".lha" uncompressible without any more sophisticated detection. A common way of handling this situation is quoting input, or uncompressible parts of the input in the output, minimizing the compression overhead. For example, the zip data format specifies the 'compression method' of 'Stored' for input files that have been copied into the archive verbatim.
