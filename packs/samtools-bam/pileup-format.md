---
title: "Pileup format"
source: https://en.wikipedia.org/wiki/Pileup_format
domain: samtools-bam
license: CC-BY-SA-4.0
tags: samtools toolkit, sequence alignment map, binary alignment map, pileup format
fetched: 2026-07-02
---

# Pileup format

**Pileup format** is a text-based format for summarizing the base calls of aligned reads to a reference sequence. This format facilitates visual display of SNP/indel calling and alignment. It was first used by Tony Cox and Zemin Ning at the Wellcome Trust Sanger Institute, and became widely known through its implementation within the SAMtools software suite.

## Format

### Example

| Sequence | Position | Reference Base | Read Count | Read Results | Quality |
|---|---|---|---|---|---|
| seq1 | 272 | T | 24 | ,.$.....,,.,.,...,,,.,..^+. | `<<<+;<<<<<<<<<<<=<;<;7<&` |
| seq1 | 273 | T | 23 | ,.....,,.,.,...,,,.,..A | `<<<;<<<<<<<<<3<=<<<;<<+` |
| seq1 | 274 | T | 23 | ,.$....,,.,.,...,,,.,... | `7<7;<;<<<<<<<<<=<;<;<<6` |
| seq1 | 275 | A | 23 | ,$....,,.,.,...,,,.,...^l. | `<+;9*<<<<<<<<<=<<:;<<<<` |
| seq1 | 276 | G | 22 | ...T,,.,.,...,,,.,.... | `33;+<<7=7<<7<&<<1;<<6<` |
| seq1 | 277 | T | 22 | ....,,.,.,.C.,,,.,..G. | `+7<;<<<<<<<&<=<<:;<<&<` |
| seq1 | 278 | G | 23 | ....,,.,.,...,,,.,....^k. | `%38*<<;<7<<7<=<<<;<<<<<` |
| seq1 | 279 | C | 23 | A..T,,.,.,...,,,.,..... | `75&<<<<<<<<<=<<<9<<:<<<` |

### The columns

Each line consists of 5 (or optionally 6) tab-separated columns:

1. Sequence identifier
2. Position in sequence (starting from 1)
3. Reference nucleotide at that position
4. Number of aligned reads covering that position (depth of coverage)
5. Bases at that position from aligned reads
6. Phred Quality of those bases, represented in ASCII with -33 offset (OPTIONAL)

### Column 5: The bases string

- . (dot) means a base that matched the reference on the forward strand
- , (comma) means a base that matched the reference on the reverse strand
- </> (less-/greater-than sign) denotes a reference skip. This occurs, for example, if a base in the reference genome is intronic and a read maps to two flanking exons. If quality scores are given in a sixth column, they refer to the quality of the read and not the specific base.
- AGTCN (upper case) denotes a base that did not match the reference on the forward strand
- agtcn (lower case) denotes a base that did not match the reference on the reverse strand
- A sequence matching the regular expression `\+[0-9]+[ACGTNacgtn]+` denotes an insertion of one or more bases starting from the next position. For example, +2AG means insertion of AG in the forward strand
- A sequence matching the regular expression `\-[0-9]+[ACGTNacgtn]+` denotes a deletion of one or more bases starting from the next position. For example, -2ct means deletion of CT in the reverse strand
- ^ (caret) marks the start of a read segment and the ASCII of the character following `^' minus 33 gives the mapping quality
- $ (dollar) marks the end of a read segment
- * (asterisk) is a placeholder for a deleted base in a multiple basepair deletion that was mentioned in a previous line by the `-[0-9]+[ACGTNacgtn]+` notation

### Column 6: The base quality string

This is an optional column. If present, the ASCII value of the character minus 33 gives the mapping Phred quality of each of the bases in the previous column 5. This is similar to quality encoding in the FASTQ format.

## File extension

There is no standard file extension for a Pileup file, but .msf (multiple sequence file), .pup and .pileup are used.
