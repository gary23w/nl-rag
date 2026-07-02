---
title: "Single-molecule real-time sequencing"
source: https://en.wikipedia.org/wiki/Single-molecule_real-time_sequencing
domain: next-gen-sequencing
license: CC-BY-SA-4.0
tags: next generation sequencing, massively parallel sequencing, sequencing by synthesis, nanopore sequencing
fetched: 2026-07-02
---

# Single-molecule real-time sequencing

**Single-molecule real-time** (**SMRT**) **sequencing** is a parallelized single molecule DNA sequencing method. Single-molecule real-time sequencing utilizes a zero-mode waveguide (ZMW). A single DNA polymerase enzyme is affixed at the bottom of a ZMW with a single molecule of DNA as a template. The ZMW is a structure that creates an illuminated observation volume that is small enough to observe only a single nucleotide of DNA being incorporated by DNA polymerase. Each of the four DNA bases is attached to one of four different fluorescent dyes. When a nucleotide is incorporated by the DNA polymerase, the fluorescent tag is cleaved off and diffuses out of the observation area of the ZMW where its fluorescence is no longer observable. A detector detects the fluorescent signal of the nucleotide incorporation, and the base call is made according to the corresponding fluorescence of the dye.

## Technology

The DNA sequencing is done on a chip that contains many ZMWs. Inside each ZMW, a single active DNA polymerase with a single molecule of single stranded DNA template is immobilized to the bottom through which light can penetrate and create a visualization chamber that allows monitoring of the activity of the DNA polymerase at a single molecule level. The signal from a phospho-linked nucleotide incorporated by the DNA polymerase is detected as the DNA synthesis proceeds which results in the DNA sequencing in real time.

### Template preparation

To prepare the library, DNA fragments are put into a circular form using hairpin adapter ligations.

### Phospholinked nucleotide

For each of the nucleotide bases, there is a corresponding fluorescent dye molecule that enables the detector to identify the base being incorporated by the DNA polymerase as it performs the DNA synthesis. The fluorescent dye molecule is attached to the phosphate chain of the nucleotide. When the nucleotide is incorporated by the DNA polymerase, the fluorescent dye is cleaved off with the phosphate chain as a part of a natural DNA synthesis process during which a phosphodiester bond is created to elongate the DNA chain. The cleaved fluorescent dye molecule then diffuses out of the detection volume so that the fluorescent signal is no longer detected.

### Zero-Mode Waveguide

The zero-mode waveguide (ZMW) is a nanophotonic confinement structure that consists of a circular hole in an aluminum cladding film deposited on a clear silica substrate.

The ZMW holes are ~70 nm in diameter and ~100 nm in depth. Due to the behavior of light when it travels through a small aperture, the optical field decays exponentially inside the chamber.

The observation volume within an illuminated ZMW is ~20 zeptoliters (20 X 10−21 liters). The observation volume being so low eliminates background fluorescence from the free, unincorporated fluorescent nucleotides present in the solution. Within this volume, the activity of DNA polymerase incorporating a single nucleotide can be readily detected where each nucleotide is a separate color.

## Sequencing Performance

Sequencing performance can be measured in read length, accuracy, and total throughput per experiment. PacBio sequencing systems using ZMWs have the advantage of long read lengths, although error rates are on the order of 5-15% and sample throughput is lower than Illumina sequencing platforms.

On 19 Sep 2018, Pacific Biosciences [PacBio] released the Sequel 6.0 chemistry, synchronizing the chemistry version with the software version. Performance is contrasted for large-insert libraries with high molecular weight DNA versus shorter-insert libraries below ~15,000 bases in length. For larger templates average read lengths are up to 30,000 bases. For shorter-insert libraries, average read length are up to 100,000 bases while reading the same molecule in a circle several times. The latter shorter-insert libraries then yield up to 50 billion bases from a single SMRT Cell.

## History

Pacific Biosciences (PacBio) commercialized SMRT sequencing in 2011, after releasing a beta version of its RS instrument in late 2010.

### RS and RS II

At commercialization, read length had a normal distribution with a mean of about 1100 bases. A new chemistry kit released in early 2012 increased the sequencer's read length; an early customer of the chemistry cited mean read lengths of 2500 to 2900 bases.

The XL chemistry kit released in late 2012 increased average read length to more than 4300 bases.

On August 21, 2013, PacBio released a new DNA polymerase Binding Kit P4. This P4 enzyme has average read lengths of more than 4,300 bases when paired with the C2 sequencing chemistry and more than 5,000 bases when paired with the XL chemistry. The enzyme’s accuracy is similar to C2, reaching QV50 between 30X and 40X coverage. The resulting P4 attributes provided higher-quality assemblies using fewer SMRT Cells and with improved variant calling. When coupled with input DNA size selection (using an electrophoresis instrument such as BluePippin) yields average read length over 7 kilobases.

On October 3, 2013, PacBio released new reagent combination for PacBio RS II, the P5 DNA polymerase with C3 chemistry (P5-C3). Together, they extend sequencing read lengths to an average of approximately 8,500 bases, with the longest reads exceeding 30,000 bases. Throughput per SMRT cell is around 500 million bases demonstrated by sequencing results from the CHM1 cell line.

On October 15, 2014, PacBio announced the release of new chemistry P6-C4 for the RS II system, which represents the company's 6th generation of polymerase and 4th generation chemistry--further extending the average read length to 10,000 - 15,000 bases, with the longest reads exceeding 40,000 bases. The throughput with the new chemistry was estimated between 500 million to 1 billion bases per SMRT Cell, depending on the sample being sequenced. This was the final version of chemistry released for the RS instrument.

Throughput per experiment for the technology is both influenced by the read length of DNA molecules sequenced as well as total multiplex of a SMRT Cell. The prototype of the SMRT Cell contained about 3000 ZMW holes that allowed parallelized DNA sequencing. At commercialization, the SMRT Cells were each patterned with 150,000 ZMW holes that were read in two sets of 75,000. In April 2013, the company released a new version of the sequencer called the "PacBio RS II" that uses all 150,000 ZMW holes concurrently, doubling the throughput per experiment. The highest throughput mode in November 2013 used P5 binding, C3 chemistry, BluePippin size selection, and a PacBio RS II officially yielded 350 million bases per SMRT Cell though a human *de novo* data set released with the chemistry averaging 500 million bases per SMRT Cell. Throughput varies based on the type of sample being sequenced. With the introduction of P6-C4 chemistry typical throughput per SMRT Cell increased to 500 million bases to 1 billion bases.

|   | C1 | C2 | P4-XL | P5-C3 | P6-C4 |
|---|---|---|---|---|---|
| **Average read length bases** | 1100 | 2500 - 2900 | 4300 - 5000 | 8500 | 10,000 - 15,000 |
| **Throughput per SMRT Cell** | 30M - 40M | 60M - 100M | 250M - 300M | 350M - 500M | 500M - 1B |

### Sequel

In September 2015, the company announced the launch of a new sequencing instrument, the Sequel System, that increased capacity to 1 million ZMW holes.

With the Sequel instrument initial read lengths were comparable to the RS, then later chemistry releases increased read length.

On January 23, 2017, the V2 chemistry was released. It increased average read lengths to between 10,000 and 18,000 bases.

On March 8, 2018, the 2.1 chemistry was released. It increased average read length to 20,000 bases and half of all reads above 30,000 bases in length. Yield per SMRT Cell increased to 10 or 20 billion bases, for either large-insert libraries or shorter-insert (e.g. amplicon) libraries respectively.

On 19 September 2018, the company announced the Sequel 6.0 chemistry with average read lengths increased to 100,000 bases for shorter-insert libraries and 30,000 for longer-insert libraries. SMRT Cell yield increased up to 50 billion bases for shorter-insert libraries.

|   | V2 | 2.1 | 6.0 |
|---|---|---|---|
| **Average read length bases** | 10,000 - 18,000 | 20,000 - 30,000 | 30,000 - 100,000 |
| **Throughput per SMRT Cell** | 5B - 8B | 10B - 20B | 20B - 50B |

### 8M Chip

In April 2019 the company released a new SMRT Cell with eight million ZMWs, increasing the expected throughput per SMRT Cell by a factor of eight. Early access customers in March 2019 reported throughput over 58 customer run cells of 250 GB of raw yield per cell with templates about 15 kb in length, and 67.4 GB yield per cell with templates in higher weight molecules. System performance is now reported in either high-molecular-weight continuous long reads or in pre-corrected HiFi (also known as Circular Consensus Sequence (CCS)) reads. For high-molecular-weight reads roughly half of all reads are longer than 50 kb in length.

|   | Early Access | 1.0 | 2.0 |
|---|---|---|---|
| **Throughput per SMRT Cell** | ~67.4 GB | Up to 160 GB | Up to 200 GB |

The HiFi performance includes corrected bases with quality above Phred score Q20, using repeated amplicon passes for correction. These take amplicons up to 20kb in length.

|   | Early Access | 1.0 | 2.0 |
|---|---|---|---|
| **Raw reads per SMRT Cell** | ~250 GB | Up to 360 GB | Up to 500 GB |
| **Corrected reads per SMRT Cell (>Q20)** | ~25 GB | Up to 36 GB | Up to 50 GB |

## Application

Single-molecule real-time sequencing may be applicable for a broad range of genomics research.

For *de novo* genome sequencing, read lengths from the single-molecule real-time sequencing are comparable to or greater than that from the Sanger sequencing method based on dideoxynucleotide chain termination. The longer read length allows *de novo* genome sequencing and easier genome assemblies. Scientists are also using single-molecule real-time sequencing in hybrid assemblies for de novo genomes to combine short-read sequence data with long-read sequence data. In 2012, several peer-reviewed publications were released demonstrating the automated finishing of bacterial genomes, including one paper that updated the Celera Assembler with a pipeline for genome finishing using long SMRT sequencing reads. In 2013, scientists estimated that long-read sequencing could be used to fully assemble and finish the majority of bacterial and archaeal genomes.

The same DNA molecule can be resequenced independently by creating the circular DNA template and utilizing a strand displacing enzyme that separates the newly synthesized DNA strand from the template. In August 2012, scientists from the Broad Institute published an evaluation of SMRT sequencing for SNP calling.

The dynamics of polymerase can indicate whether a base is methylated. Scientists demonstrated the use of single-molecule real-time sequencing for detecting methylation and other base modifications. In 2012 a team of scientists used SMRT sequencing to generate the full methylomes of six bacteria. In November 2012, scientists published a report on genome-wide methylation of an outbreak strain of E. coli.

Long reads make it possible to sequence full gene isoforms, including the 5' and 3' ends. This type of sequencing is useful to capture isoforms and splice variants.

SMRT sequencing has several applications in reproductive medical genetics research when investigating families with suspected parental gonadal mosaicism. Long reads enable haplotype phasing in patients to investigate parent-of-origin of mutations. Deep sequencing enables determination of allele frequencies in sperm cells, of relevance for estimation of recurrence risk for future affected offspring.
