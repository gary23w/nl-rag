---
title: "BAM (file format)"
source: https://en.wikipedia.org/wiki/Binary_Alignment_Map
domain: samtools-bam
license: CC-BY-SA-4.0
tags: samtools toolkit, sequence alignment map, binary alignment map, pileup format
fetched: 2026-07-02
---

# BAM (file format)

(Redirected from

Binary Alignment Map

)

The **BAM file format** (which stands for **Binary Alignment Map**) is the lossless, compressed binary representation of a Sequence Alignment Map file. It is compressed by BGZF library and supports fast, random access. BAM is one of the most common file formats for raw genome sequencing data.

## Schema

BAM is the compressed binary representation of SAM (Sequence Alignment Map), a compact and index-able representation of nucleotide sequence alignments. The goal of indexing is to retrieve alignments that overlap a specific location quickly without having to go through all of them. Before indexing, BAM must be sorted by reference ID and then leftmost coordinate. BAM is in compressed BGZF format.

The structure of BAM files include a header section and an alignment section:

- Header—The sample name, sample length, and alignment method are all included in this section. The alignments section contains alignments that are linked to specific information in the header section.
- Alignments—The read name, read sequence, read quality, alignment information, and custom tags are all included in this file. The chromosome, start coordinate, alignment quality, and match descriptor string are all included in the read name.
  - Alignment Section includes the following:
    - Read Group (RG)
    - Barcode Tag (BC)
    - Single-end alignment quality (SM)
    - Paired-end alignment quality (AS)
    - Edit distance tag (NM)
    - Amplicon name tag (XN)

BAM format uses 0-based coordinate system, where as SAM uses 1-based coordinate system. BAM can represent values in the range [−2^31 , 2^32).

## Tools

To view a list of sequencing and analysis tools that work with SAM/BAM click here.
