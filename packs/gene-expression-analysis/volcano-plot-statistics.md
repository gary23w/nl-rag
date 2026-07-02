---
title: "Volcano plot (statistics)"
source: https://en.wikipedia.org/wiki/Volcano_plot_(statistics)
domain: gene-expression-analysis
license: CC-BY-SA-4.0
tags: gene expression profiling, dna microarray, differential gene expression, rna sequencing
fetched: 2026-07-02
---

# Volcano plot (statistics)

In statistics, a **volcano plot** is a type of scatter-plot that is used to quickly identify changes in large data sets composed of replicate data. It plots significance versus fold-change on the y and x axes, respectively. These plots are increasingly common in omic experiments such as genomics, proteomics, and metabolomics where one often has a list of many thousands of replicate data points between two conditions and one wishes to quickly identify the most meaningful changes. A volcano plot combines a measure of statistical significance from a statistical test (e.g., a p value from an ANOVA model) with the magnitude of the change, enabling quick visual identification of those data-points (genes, etc.) that display large magnitude changes that are also statistically significant.

A volcano plot is a sophisticated data visualization tool used in statistical and genomic analyses to illustrate the relationship between the magnitude of change and statistical significance. It is constructed by plotting the negative logarithm (base 10) of the p-value on the y-axis, ensuring that data points with lower p-values—indicative of higher statistical significance—are positioned toward the top of the plot. The x-axis represents the logarithm of the fold change between two conditions, allowing for a symmetric representation of both upregulated and downregulated changes relative to the center. This transformation ensures that equivalent deviations in either direction are equidistant from the origin, facilitating intuitive interpretation.

The plot inherently highlights two critical regions of interest: data points that reside in the upper extremes of the graph while being significantly displaced to the left or right. These points correspond to variables that exhibit both substantial fold changes (magnitude of effect) and exceptional statistical significance, making them prime candidates for further investigation in differential analyses. The volcano plot, therefore, serves as a powerful means of identifying key biomarkers, differentially expressed genes, or other significant entities within complex datasets.

Additional information can be added by coloring the points according to a third dimension of data (such as signal intensity), but this is not uniformly employed. Volcano plots are also used to graphically display a significance analysis of microarrays (SAM) gene selection criterion, an example of regularization.

The concept of volcano plot can be generalized to other applications, where the x axis is related to a measure of the strength of a statistical signal, and y axis is related to a measure of the statistical significance of the signal. For example, in a genetic association case-control study, such as genome-wide association study, a point in a volcano plot represents a single-nucleotide polymorphism. Its x value can be the logarithm of the odds ratio and its y value can be -log10 of the p value from a Chi-square test or a Chi-square test statistic.

Volcano plots show a characteristic upwards two arm shape because the x axis, i.e. the underlying log2-fold changes, are generally normal distributed whereas the y axis, the log10-p values, tend toward greater significance for fold-changes that deviate more strongly from zero. The density of the normal distribution takes the form

$y=e^{-x^{2}}$

.

So the $\ln$ of that is

$\ln(y)=-x^{2}$

and the negative $\ln$ is

$-\ln(y)=x^{2}$

which is a parabola whose arms reach upwards on the right and left sides. The upper bound of the data is one parabola and the lower bound is another parabola.
