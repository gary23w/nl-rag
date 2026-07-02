---
title: "Variant Call Format"
source: https://en.wikipedia.org/wiki/Variant_Call_Format
domain: genomics-computing
license: CC-BY-SA-4.0
tags: genomics computing, dna sequencing, genome assembly, de bruijn graph
fetched: 2026-07-02
---

# Variant Call Format

The **Variant Call Format** or **VCF** is a standard text file format used in bioinformatics for storing gene sequence or DNA sequence variations. The format was developed in 2010 for the 1000 Genomes Project and has since been used by other large-scale genotyping and DNA sequencing projects. VCF is a common output format for variant calling programs due to its relative simplicity and scalability. Many tools have been developed for editing and manipulating VCF files, including VCFtools, which was released in conjunction with the VCF format in 2011, and BCFtools, which was included as part of SAMtools until being split into an independent package in 2014.

The standard is currently in version 4.5, although the 1000 Genomes Project has developed its own specification for structural variations such as duplications, which are not easily accommodated into the existing schema.

Additional file formats have been developed based on VCF, including **genomic VCF** (**gVCF**). gVCF is an extended format which includes additional information about "blocks" that match the reference and their qualities.

## Example

```
##fileformat=VCFv4.3
##fileDate=20090805
##source=myImputationProgramV3.1
##reference=file:///seq/references/1000GenomesPilot-NCBI36.fasta
##contig=<ID=20,length=62435964,assembly=B36,md5=f126cdf8a6e0c7f379d618ff66beb2da,species="Homo sapiens",taxonomy=x>
##phasing=partial
##INFO=<ID=NS,Number=1,Type=Integer,Description="Number of Samples With Data">
##INFO=<ID=DP,Number=1,Type=Integer,Description="Total Depth">
##INFO=<ID=AF,Number=A,Type=Float,Description="Allele Frequency">
##INFO=<ID=AA,Number=1,Type=String,Description="Ancestral Allele">
##INFO=<ID=DB,Number=0,Type=Flag,Description="dbSNP membership, build 129">
##INFO=<ID=H2,Number=0,Type=Flag,Description="HapMap2 membership">
##FILTER=<ID=q10,Description="Quality below 10">
##FILTER=<ID=s50,Description="Less than 50% of samples have data">
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="Genotype Quality">
##FORMAT=<ID=DP,Number=1,Type=Integer,Description="Read Depth">
##FORMAT=<ID=HQ,Number=2,Type=Integer,Description="Haplotype Quality">
#CHROM POS      ID         REF   ALT    QUAL  FILTER   INFO                             FORMAT       NA00001         NA00002          NA00003
20     14370    rs6054257  G     A      29    PASS    NS=3;DP=14;AF=0.5;DB;H2           GT:GQ:DP:HQ  0|0:48:1:51,51  1|0:48:8:51,51   1/1:43:5:.,.
20     17330    .          T     A      3     q10     NS=3;DP=11;AF=0.017               GT:GQ:DP:HQ  0|0:49:3:58,50  0|1:3:5:65,3     0/0:41:3
20     1110696  rs6040355  A     G,T    67    PASS    NS=2;DP=10;AF=0.333,0.667;AA=T;DB GT:GQ:DP:HQ  1|2:21:6:23,27  2|1:2:0:18,2     2/2:35:4
20     1230237  .          T     .      47    PASS    NS=3;DP=13;AA=T                   GT:GQ:DP:HQ  0|0:54:7:56,60  0|0:48:4:51,51   0/0:61:2
20     1234567  microsat1  GTC   G,GTCT 50    PASS    NS=3;DP=9;AA=G                    GT:GQ:DP     0/1:35:4        0/2:17:2         1/1:40:3
```

## The VCF header

The header begins the file and provides metadata describing the body of the file. Header lines are denoted as starting with #. Special keywords in the header are denoted with ##. Recommended keywords include fileformat, fileDate and reference.

The header contains keywords that optionally semantically and syntactically describe the fields used in the body of the file, notably INFO, FILTER, and FORMAT (see below).

In practice, VCF headers often contain substantial metadata added by upstream software, such as reference genome information, contig definitions, filter descriptions, sample declarations, provenance fields, and custom INFO or FORMAT tags. This metadata is important for validation and interpretation.

## The columns of a VCF

The body of VCF follows the header, and is tab separated into 8 mandatory columns and an unlimited number of optional columns that may be used to record other information about the sample(s). When additional columns are used, the first optional column is used to describe the format of the data in the columns that follow.

|   | Name | Brief description (see the specification for details). |
|---|---|---|
| 1 | CHROM | The name of the sequence (typically a chromosome) on which the variation is being called. This sequence is usually known as 'the reference sequence', i.e. the sequence against which the given sample varies. |
| 2 | POS | The 1-based position of the variation on the given sequence. |
| 3 | ID | The identifier of the variation, e.g. a dbSNP rs identifier, or if unknown a ".". Multiple identifiers should be separated by semi-colons without white-space. |
| 4 | REF | The reference base (or bases in the case of an indel) at the given position on the given reference sequence. |
| 5 | ALT | The list of alternative alleles at this position. |
| 6 | QUAL | A quality score associated with the inference of the given alleles. |
| 7 | FILTER | A flag indicating which of a given set of filters the variation has failed or PASS if all the filters were passed successfully. |
| 8 | INFO | An extensible list of key-value pairs (fields) describing the variation. See below for some common fields. Multiple fields are separated by semicolons with optional values in the format: `<key>=<data>[,data]`. |
| 9 | FORMAT | An (optional) extensible list of fields for describing the samples. See below for some common fields. |
| + | SAMPLEs | For each (optional) sample described in the file, values are given for the fields listed in FORMAT |

## Common INFO fields

Arbitrary keys are permitted, although the following sub-fields are reserved (albeit optional):

| Name | Brief description |
|---|---|
| AA | ancestral allele |
| AC | allele count in genotypes, for each ALT allele, in the same order as listed |
| AF | allele frequency for each ALT allele in the same order as listed (use this when estimated from primary data, not called genotypes) |
| AN | total number of alleles in called genotypes |
| BQ | RMS base quality at this position |
| CIGAR | cigar string describing how to align an alternate allele to the reference allele |
| DB | dbSNP membership |
| DP | combined depth across samples, e.g. DP=154 |
| END | end position of the variant described in this record (for use with symbolic alleles) |
| H2 | membership in hapmap2 |
| H3 | membership in hapmap3 |
| MQ | RMS mapping quality, e.g. MQ=52 |
| MQ0 | Number of MAPQ == 0 reads covering this record |
| NS | Number of samples with data |
| SB | strand bias at this position |
| SOMATIC | indicates that the record is a somatic mutation, for cancer genomics |
| VALIDATED | validated by follow-up experiment |
| 1000G | membership in 1000 Genomes |

Any other info fields are defined in the .vcf header.

## Common FORMAT fields

| Name | Brief description |
|---|---|
| AD | Read depth for each allele |
| ADF | Read depth for each allele on the forward strand |
| ADR | Read depth for each allele on the reverse strand |
| DP | Read depth |
| EC | Expected alternate allele counts |
| FT | Filter indicating if this genotype was "called" |
| GL | Genotype likelihoods |
| GP | Genotype posterior probabilities |
| GQ | Conditional genotype quality |
| GT | Genotype |
| HQ | Haplotype quality |
| MQ | RMS mapping quality |
| PL | Phred-scaled genotype likelihoods rounded to the closest integer |
| PQ | Phasing quality |
| PS | Phase set |

Any other format fields are defined in the .vcf header.

## Binary VCF

Binary VCF or BCF files are binary, BGZF compressed variation of VCF files. BCF files allow fast and efficient indexed queries through tools like Tabix once an index file has been created.
