---
title: "Base calling"
source: https://en.wikipedia.org/wiki/Base_calling
domain: variant-calling-gatk
license: CC-BY-SA-4.0
tags: variant calling, single-nucleotide polymorphism, variant call format, base calling
fetched: 2026-07-02
---

# Base calling

**Base calling** is the process of assigning nucleobases to chromatogram peaks, light intensity signals, or electrical current changes resulting from nucleotides passing through a nanopore. One computer program for accomplishing this job is Phred, which was a widely used base calling software program by both academic and commercial DNA sequencing laboratories because of its high base calling accuracy.

Currently basecalling is commonly handled by on-instrument software, such as the proprietary Real-Time Analysis (RTA) pipeline, which is highly integrated and updated with each platform release.

Base callers for Nanopore sequencing like Guppy or Dorado, use neural networks trained on current signals obtained from accurate sequencing data.

## Base calling accuracy

Base calling can be assessed by two metrics, read accuracy and consensus accuracy. Read accuracy refers to the called base's accuracy to a known reference. Consensus accuracy refers to how accurate a consensus sequence is compared to overlapping reads from the same genetic locus.
