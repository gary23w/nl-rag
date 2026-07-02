---
title: "Z-factor"
source: https://en.wikipedia.org/wiki/Z-factor
domain: high-throughput-screening
license: CC-BY-SA-4.0
tags: assay automation, microplate, z factor, compound deck
fetched: 2026-07-02
---

# Z-factor

The **Z-factor** is a measure of statistical effect size. It has been proposed for use in high-throughput screening (HTS), where it is also known as Z-prime, to judge whether the response in a particular assay is large enough to warrant further attention.

## Background

In HTS, experimenters often compare a large number (hundreds of thousands to tens of millions) of single measurements of unknown samples to positive and negative control samples. The particular choice of experimental conditions and measurements is called an assay. Large screens are expensive in time and resources. Therefore, prior to starting a large screen, smaller test (or pilot) screens are used to assess the quality of an assay, in an attempt to predict if it would be useful in a high-throughput setting. The Z-factor is an attempt to quantify the suitability of a particular assay for use in a full-scale HTS.

## Definition

### Z-factor

The Z-factor is defined in terms of four parameters: the means ( $\mu$ ) and standard deviations ( $\sigma$ ) of samples (s) and controls (c). Given these values ( $\mu _{s}$ , $\sigma _{s}$ , and $\mu _{c}$ , $\sigma _{c}$ ), the Z-factor is defined as:

${\text{Z-factor}}=1-{3(\sigma _{s}+\sigma _{c}) \over |\mu _{s}-\mu _{c}|}$

For assays of agonist/activation type, the control (c) data ( $\mu _{c}$ , $\sigma _{c}$ ) in the equation are substituted with the positive control (p) data ( $\mu _{p}$ , $\sigma _{p}$ ) which represent maximal activated signal; for assays of antagonist/inhibition type, the control (c) data ( $\mu _{c}$ , $\sigma _{c}$ ) in the equation are substituted with the negative control (n) data ( $\mu _{n}$ , $\sigma _{n}$ ) which represent minimal signal.

In practice, the Z-factor is estimated from the sample means and sample standard deviations

${\text{Estimated Z-factor}}=1-{3({\hat {\sigma }}_{s}+{\hat {\sigma }}_{c}) \over |{\hat {\mu }}_{s}-{\hat {\mu }}_{c}|}$

### Z'-factor

The Z'-factor (Z-prime factor) is defined in terms of four parameters: the means ( $\mu$ ) and standard deviations ( $\sigma$ ) of both the positive (p) and negative (n) controls ( $\mu _{p}$ , $\sigma _{p}$ , and $\mu _{n}$ , $\sigma _{n}$ ). Given these values, the Z'-factor is defined as:

${\text{Z'-factor}}=1-{3(\sigma _{p}+\sigma _{n}) \over |\mu _{p}-\mu _{n}|}$

The Z'-factor is a characteristic parameter of the assay itself, without intervention of samples.

## Interpretation

The Z-factor defines a characteristic parameter of the capability of hit identification for each given assay. The following categorization of HTS assay quality by the value of the Z-Factor is a modification of Table 1 shown in Zhang *et al.* (1999); note that the Z-factor cannot exceed one.

| Z-factor value | Related to screening | Interpretation |
|---|---|---|
| 1.0 | An ideal assay |   |
| 1.0 > Z ≥ 0.5 | An excellent assay | Note that if $\sigma _{p}=\sigma _{n}$ , 0.5 is equivalent to a separation of **12** standard deviations between $\mu _{p}$ and $\mu _{n}$ . |
| 0.5 > Z > 0 | A marginal assay |   |
| 0 | A "yes/no" type assay |   |
| < 0 | Screening essentially impossible | There is too much overlap between the positive and negative controls for the assay to be useful. |

Note that by the standards of many types of experiments, a zero Z-factor would suggest a large effect size, rather than a borderline useless result as suggested above. For example, if σp=σn=1, then μp=6 and μn=0 gives a zero Z-factor. But for normally-distributed data with these parameters, the probability that the positive control value would be less than the negative control value is less than 1 in 105. Extreme conservatism is used in high throughput screening due to the large number of tests performed.

## Limitations

The constant factor 3 in the definition of the Z-factor is motivated by the normal distribution, for which more than 99% of values occur within three times standard deviations of the mean. If the data follow a strongly non-normal distribution, the reference points (e.g. the meaning of a negative value) may be misleading.

Another issue is that the usual estimates of the mean and standard deviation are not robust; accordingly many users in the high-throughput screening community prefer the "Robust Z-prime" which substitutes the median for the mean and the median absolute deviation for the standard deviation. Extreme values (outliers) in either the positive or negative controls can adversely affect the Z-factor, potentially leading to an apparently unfavorable Z-factor even when the assay would perform well in actual screening . In addition, the application of the single Z-factor-based criterion to two or more positive controls with different strengths in the same assay will lead to misleading results . The absolute sign in the Z-factor makes it inconvenient to derive the statistical inference of Z-factor mathematically. A recently proposed statistical parameter, strictly standardized mean difference (SSMD), can address these issues. One estimate of SSMD is robust to outliers.
