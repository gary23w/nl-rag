---
title: "Detection limit"
source: https://en.wikipedia.org/wiki/Detection_limit
domain: analytical-chemistry
license: CC-BY-SA-4.0
tags: analytical chemistry, quantitative analysis, calibration curve, detection limit
fetched: 2026-07-02
---

# Detection limit

The **limit of detection** (**LOD** or **LoD**) is the lowest signal, or the lowest corresponding quantity to be determined (or extracted) from the signal, that can be observed with a sufficient degree of confidence or statistical significance. However, the exact threshold (level of decision) used to decide when a signal significantly emerges above the continuously fluctuating background noise remains arbitrary and is a matter of policy and often of debate among scientists, statisticians and regulators depending on the stakes in different fields.

## Significance in analytical chemistry

In analytical chemistry, the **detection limit**, **lower limit of detection**, also termed **LOD** for **limit of detection** or **analytical sensitivity** (not to be confused with statistical sensitivity), is the lowest quantity of a substance that can be distinguished from the absence of that substance (a *blank value*) with a stated confidence level (generally 99%). The detection limit is estimated from the mean of the blank, the standard deviation of the blank, the slope (analytical sensitivity) of the calibration plot and a defined confidence factor (e.g. 3.2 being the most accepted value for this arbitrary value). Another consideration that affects the detection limit is the adequacy and the accuracy of the model used to predict concentration from the raw analytical signal.

As a typical example, from a calibration plot following a linear equation taken here as the simplest possible model:

$f(x)=ax+b$

where, $f(x)$ corresponds to the signal measured (e.g. voltage, luminescence, energy, etc.), "b" the value in which the straight line cuts the ordinates axis, "a" the sensitivity of the system (i.e., the slope of the line, or the function relating the measured signal to the quantity to be determined) and "x" the value of the quantity (e.g. temperature, concentration, pH, etc.) to be determined from the signal $f(x)$ , the LOD for "x" is calculated as the "x" value in which $f(x)$ equals to the average value of blanks "y" plus "t" times its standard deviation "s" (or, if zero, the standard deviation corresponding to the lowest value measured) where "t" is the chosen confidence value (e.g. for a confidence of 95% it can be considered t = 3.2, determined from the limit of blank).

Thus, in this didactic example:

${\text{LOD for }}x={\frac {\left(f(x)-b\right)}{a}}={\frac {\left(y+3.2s-b\right)}{a}}$

There are a number of concepts derived from the detection limit that are commonly used. These include the **instrument detection limit** (**IDL**), the **method detection limit** (**MDL**), the **practical quantitation limit** (**PQL**), and the **limit of quantitation** (**LOQ**). Even when the same terminology is used, there can be differences in the LOD according to nuances of what definition is used and what type of noise contributes to the measurement and calibration.

The figure below illustrates the relationship between the blank, the *limit of detection* (LOD), and the *limit of quantitation* (LOQ) by showing the probability density function for normally distributed measurements at the blank, at the LOD defined as 3 × standard deviation of the blank, and at the LOQ defined as 10 × standard deviation of the blank. (The identical spread along Abscissa of these two functions is problematic.) For a signal at the LOD, the alpha error (probability of false positive) is small (1%). However, the beta error (probability of a false negative) is 50% for a sample that has a concentration at the LOD (red line). This means a sample could contain an impurity at the LOD, but there is a 50% chance that a measurement would give a result less than the LOD. At the LOQ (blue line), there is minimal chance of a false negative.

Illustration of the concept of detection limit and quantitation limit by showing the theoretical

normal distributions

associated with blank, detection limit (LOD), and quantitation limit (LOQ) level samples.

## Instrument detection limit

Most analytical instruments produce a signal even when a blank (matrix without analyte) is analyzed. This signal is referred to as the noise level. The instrument detection limit (IDL) is the analyte concentration that is required to produce a signal greater than three times the standard deviation of the noise level. This may be practically measured by analyzing 8 or more standards at the estimated IDL then calculating the standard deviation from the measured concentrations of those standards.

The detection limit (according to IUPAC) is the smallest concentration, or the smallest absolute amount, of analyte that has a signal statistically significantly larger than the signal arising from the repeated measurements of a reagent blank.

Mathematically, the analyte's signal at the detection limit ( $S_{dl}$ ) is given by:

$S_{dl}=S_{reag}+3\ \sigma _{reag}$

where, $S_{reag}$ is the mean value of the signal for a reagent blank measured multiple times, and $\sigma _{reag}$ is the known standard deviation for the reagent blank's signal.

Other approaches for defining the detection limit have also been developed. In atomic absorption spectrometry usually the detection limit is determined for a certain element by analyzing a diluted solution of this element and recording the corresponding absorbance at a given wavelength. The measurement is repeated 10 times. The 3σ of the recorded absorbance signal can be considered as the detection limit for the specific element under the experimental conditions: selected wavelength, type of flame or graphite oven, chemical matrix, presence of interfering substances, instrument... .

## Method detection limit

Often there is more to the analytical method than just performing a reaction or submitting the analyte to direct analysis. Many analytical methods developed in the laboratory, especially these involving the use of a delicate scientific instrument, require a sample preparation, or a pretreatment of the samples prior to being analysed. For example, it might be necessary to heat a sample that is to be analyzed for a particular metal with the addition of acid first (digestion process). The sample may also be diluted or concentrated prior to analysis by means of a given instrument. Additional steps in an analysis method add additional opportunities for errors. Since detection limits are defined in terms of errors, this will naturally increase the measured detection limit. This "*global*" detection limit (including all the steps of the analysis method) is called the method detection limit (MDL). The practical way for determining the MDL is to analyze seven samples of concentration near the expected limit of detection. The standard deviation is then determined. The one-sided Student's t-distribution is determined and multiplied versus the determined standard deviation. For seven samples (with six degrees of freedom) the t value for a 99% confidence level is 3.14. Rather than performing the complete analysis of seven identical samples, if the Instrument Detection Limit is known, the MDL may be estimated by multiplying the Instrument Detection Limit, or Lower Level of Detection, by the dilution prior to analyzing the sample solution with the instrument. This estimation, however, ignores any uncertainty that arises from performing the sample preparation and will therefore probably underestimate the true MDL.

## Limit of each model

The issue of limit of detection, or limit of quantification, is encountered in all scientific disciplines. This explains the variety of definitions and the diversity of jurisdiction specific solutions developed to address preferences. In the simplest cases as in nuclear and chemical measurements, definitions and approaches have probably received the clearer and the simplest solutions. In biochemical tests and in biological experiments depending on many more intricate factors, the situation involving false positive and false negative responses is more delicate to handle. In many other disciplines such as geochemistry, seismology, astronomy, dendrochronology, climatology, life sciences in general, and in many other fields impossible to enumerate extensively, the problem is wider and deals with signal extraction out of a background of noise. It involves complex statistical analysis procedures and therefore it also depends on the models used, the hypotheses and the simplifications or approximations to be made to handle and manage uncertainties. When the data resolution is poor and different signals overlap, different deconvolution procedures are applied to extract parameters. The use of different phenomenological, mathematical and statistical models may also complicate the exact mathematical definition of limit of detection and how it is calculated. This explains why it is not easy to come to a general consensus, if any, about the precise mathematical definition of the expression of limit of detection. However, one thing is clear: it always requires a sufficient number of data (or accumulated data) and a rigorous statistical analysis to render better signification statistically.

## Limit of quantification

The limit of quantification (LoQ, or LOQ) is the lowest value of a signal (or concentration, activity, response...) that can be quantified with acceptable precision and accuracy.

The LoQ is the limit at which the difference between two distinct signals / values can be discerned with a reasonable certainty, *i.e.*, when the signal is statistically different from the background. The LoQ may be drastically different between laboratories, so another detection limit is commonly used that is referred to as the **Practical Quantification Limit** (PQL).
