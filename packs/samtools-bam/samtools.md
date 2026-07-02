---
title: "SAMtools"
source: https://en.wikipedia.org/wiki/Samtools
domain: samtools-bam
license: CC-BY-SA-4.0
tags: samtools toolkit, sequence alignment map, binary alignment map, pileup format
fetched: 2026-07-02
---

# SAMtools

(Redirected from

Samtools

)

**SAMtools** is a set of utilities for interacting with and post-processing short DNA sequence read alignments in the SAM (Sequence Alignment/Map), BAM (Binary Alignment/Map) and CRAM formats, written by Heng Li. These files are generated as output by short read aligners like BWA. Both simple and advanced tools are provided, supporting complex tasks like variant calling and alignment viewing as well as sorting, indexing, data extraction and format conversion. SAM files can be very large (tens of Gigabytes is common), so compression is used to save space. SAM files are human-readable text files, and BAM files are simply their binary equivalent, whilst CRAM files are a restructured column-oriented binary container format. BAM files are typically compressed and more efficient for software to work with than SAM. SAMtools makes it possible to work directly with a compressed BAM file, without having to uncompress the whole file. Additionally, since the format for a SAM/BAM file is somewhat complex - containing reads, references, alignments, quality information, and user-specified annotations - SAMtools reduces the effort needed to use SAM/BAM files by hiding low-level details.

As third-party projects were trying to use code from SAMtools despite it not being designed to be embedded in that way, the decision was taken in August 2014 to split the SAMtools package into a stand-alone software library with a well-defined API (HTSlib), a project for variant calling and manipulation of variant data (BCFtools), and the stand-alone SAMtools package for working with sequence alignment data.

## Usage and commands

Like many Unix commands, SAMtool commands follow a stream model, where data runs through each command as if carried on a conveyor belt. This allows combining multiple commands into a data processing pipeline. Although the final output can be very complex, only a limited number of simple commands are needed to produce it. If not specified, the standard streams (stdin, stdout, and stderr) are assumed. Data sent to stdout are printed to the screen by default but are easily redirected to another file using the normal Unix redirectors (> and >>), or to another command via a pipe (|).

## SAMtools commands

SAMtools provides the following commands, each invoked as `samtools <subcommand>`:

**view**

The

view

command filters SAM or BAM formatted data. Using options and arguments it understands what data to select (possibly all of it) and passes only that data through. Input is usually a sam or bam file specified as an argument, but could be sam or bam data piped from any other command. Possible uses include extracting a subset of data into a new file, converting between BAM and SAM formats, and just looking at the raw file contents. The order of extracted reads is preserved.

**sort**

The

sort

command sorts a BAM file based on its position in the reference, as determined by its alignment. The element + coordinate in the reference that the first matched base in the read aligns to is used as the key to order it by. [TODO: verify]. The sorted output is dumped to a new file by default, although it can be directed to stdout (using the -o option). As sorting is memory intensive and BAM files can be large, this command supports a sectioning mode (with the -m options) to use at most a given amount of memory and generate multiple output file. These files can then be merged to produce a complete sorted BAM file

[TODO - investigate the details of this more carefully]

.

**index**

The

index

command creates a new index file that allows fast look-up of data in a (sorted) SAM or BAM. Like an index on a database, the generated

*.sam.sai

or

*.bam.bai

file allows programs that can read it to more efficiently work with the data in the associated files.

**tview**

The

tview

command starts an interactive ascii-based viewer that can be used to visualize how reads are aligned to specified small regions of the reference genome. Compared to a graphics based viewer like IGV,

it has few features. Within the view, it is possible to jumping to different positions along reference elements (using 'g') and display help information ('?').

**mpileup**

The

mpileup

command produces a

pileup format

(or BCF) file giving, for each genomic coordinate, the overlapping read bases and indels at that position in the input BAM files(s). This can be used for SNP calling for example.

**flagstat**
