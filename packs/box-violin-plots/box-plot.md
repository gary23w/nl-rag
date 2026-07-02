---
title: "Box plot"
source: https://en.wikipedia.org/wiki/Box_plot
domain: box-violin-plots
license: CC-BY-SA-4.0
tags: box plot, violin plot, bagplot, strip plot
fetched: 2026-07-02
---

# Box plot

In descriptive statistics, a **box plot** or **boxplot** is a method for demonstrating graphically the locality, spread and skewness groups of numerical data through their quartiles.

In addition to the box on a box plot, there can be lines (which are called *whiskers*) extending from the box indicating variability outside the upper and lower quartiles, thus, the plot is also called the **box-and-whisker plot** and the **box-and-whisker diagram**. Outliers that differ significantly from the rest of the dataset may be plotted as individual points beyond the whiskers on the box plot. Box plots are non-parametric: they display variation in samples of a statistical population without making any assumptions of the underlying statistical distribution (though Tukey's box plot assumes symmetry for the whiskers and normality for their length).

The spacings in each subsection of the box plot indicate the degree of dispersion (spread) and skewness of the data, which are usually described using the five-number summary. In addition, the box plot allows one to visually estimate various L-estimators, notably the interquartile range, midhinge, range, mid-range, and trimean. Box plots can be drawn either horizontally or vertically.

## History

The range-bar method was first introduced by Mary Eleanor Spear in her book "Charting Statistics" in 1952 and again in her book "Practical Charting Techniques" in 1969. The box-and-whisker plot was first introduced in 1970 by John Tukey, who later published on the subject in his book "Exploratory Data Analysis" in 1977.

## Elements

A box plot is a standardized way of displaying the dataset based on the five-number summary: the minimum, the maximum, the sample median, and the first and third quartiles.

- **Minimum (*Q*0 or 0th percentile)**: the lowest data point in the data set excluding any outliers
- **Maximum (*Q*4 or 100th percentile)**: the highest data point in the data set excluding any outliers
- **Median (*Q*2 or 50th percentile)**: the middle value in the data set
- **First quartile (*Q*1 or 25th percentile)**: also known as the *lower quartile* *q**n*(0.25), it is the median of the lower half of the dataset
- **Third quartile (*Q*3 or 75th percentile)**: also known as the *upper quartile* *q**n*(0.75), it is the median of the upper half of the dataset

In addition to the minimum and maximum values used to construct a box plot, another important element that can also be employed to obtain a box plot is the interquartile range (IQR), as denoted below:

- **Interquartile range (IQR)**: the distance between the upper and lower quartiles

${\text{IQR}}=Q_{3}-Q_{1}=q_{n}(0.75)-q_{n}(0.25)$

### Box

The box is drawn from *Q*1 to *Q*3 with a horizontal line drawn inside it to denote the median. Some box plots include an additional character to represent the mean of the data.

### Whiskers

The whiskers must end at an observed data point, but can be defined in various ways. In the most straightforward method, the boundary of the lower whisker is the minimum value of the data set, and the boundary of the upper whisker is the maximum value of the data set. Because of this variability, it is appropriate to describe the convention that is being used for the whiskers and outliers in the caption of the box plot.

Another popular choice for the boundaries of the whiskers is based on the 1.5 IQR value. From above the upper quartile (***Q*3**), a distance of 1.5 times the IQR is measured out and a whisker is drawn *up to* the largest observed data point from the dataset that falls within this distance. Similarly, a distance of 1.5 times the IQR is measured out below the lower quartile (***Q*1**) and a whisker is drawn *down to* the lowest observed data point from the dataset that falls within this distance. Because the whiskers must end at an observed data point, the whisker lengths can look unequal, even though 1.5 IQR is the same for both sides. All other observed data points outside the boundary of the whiskers are plotted as **outliers**. The outliers can be plotted on the box plot as a dot, a small circle, a star, *etc.* (see example below).

There are other representations in which the whiskers can stand for several other things, such as:

- One standard deviation above and below the mean of the data set
- The 9th percentile and the 91st percentile of the data set
- The 2nd percentile and the 98th percentile of the data set

Rarely, box plot can be plotted without the whiskers. This can be appropriate for sensitive information to avoid whiskers (and outliers) disclosing actual values observed.

The unusual percentiles 2%, 9%, 91%, 98% are sometimes used for whisker cross-hatches and whisker ends to depict the seven-number summary. If the data are normally distributed, the locations of the seven marks on the box plot will be equally spaced. On some box plots, a cross-hatch is placed before the end of each whisker.

## Variations

Since the mathematician John W. Tukey first popularized this type of visual data display in 1969, several variations on the classical box plot have been developed, and the two most commonly found variations are the variable-width box plots and the notched box plots.

**Variable-width box** plots illustrate the size of each group whose data is being plotted by making the width of the box proportional to the size of the group. A popular convention is to make the box width proportional to the square root of the size of the group.

**Notched box** plots apply a "notch" or narrowing of the box around the median. Notches are useful in offering a rough guide of the significance of the difference of medians; if the notches of two boxes do not overlap, this will provide evidence of a statistically significant difference between the medians. The height of the notches is proportional to the interquartile range (IQR) of the sample and is inversely proportional to the square root of the size of the sample. However, there is an uncertainty about the most appropriate multiplier (as this may vary depending on the similarity of the variances of the samples). The width of the notch is arbitrarily chosen to be visually pleasing, and should be consistent amongst all box plots being displayed on the same page.

One convention for obtaining the boundaries of these notches is to use a distance of $\pm {\frac {1.58{\text{ IQR}}}{\sqrt {n}}}$ around the median.

**Adjusted box** plots are intended to describe skew distributions, and they rely on the medcouple statistic of skewness. For a medcouple value of MC, the lengths of the upper and lower whiskers on the box plot are respectively defined to be:

${\begin{matrix}1.5{\text{IQR}}\cdot e^{3{\text{MC}}},&1.5{\text{ IQR}}\cdot e^{-4{\text{MC}}}{\text{ if }}{\text{MC}}\geq 0,\\1.5{\text{IQR}}\cdot e^{4{\text{MC}}},&1.5{\text{ IQR}}\cdot e^{-3{\text{MC}}}{\text{ if }}{\text{MC}}\leq 0.\end{matrix}}$

For a symmetrical data distribution, the medcouple will be zero, and this reduces the adjusted box plot to the Tukey's box plot with equal whisker lengths of $1.5{\text{ IQR}}$ for both whiskers.

**Other kinds of box plots**, such as the violin plots and the bean plots can show the difference between single-modal and multimodal distributions, which cannot be observed from the original classical box plot.

## Examples

### Example without outliers

A series of hourly temperatures were measured throughout the day in degrees Fahrenheit. The recorded values are listed in order as follows (°F): 57, 57, 57, 58, 63, 66, 66, 67, 67, 68, 69, 70, 70, 70, 70, 72, 73, 75, 75, 76, 76, 78, 79, 81.

A box plot of the data set can be generated by first calculating five relevant values of this data set: minimum, maximum, median (***Q*2**), first quartile (***Q*1**), and third quartile (***Q*3**).

The minimum is the smallest number of the data set. In this case, the minimum recorded day temperature is 57°F.

The maximum is the largest number of the data set. In this case, the maximum recorded day temperature is 81°F.

The median is the "middle" number of the ordered data set. This means that exactly 50% of the elements are below the median and 50% of the elements are greater than the median. The median of this ordered data set is 70°F.

The first quartile value (***Q*1** **or 25th percentile)** is the number that marks one quarter of the ordered data set. In other words, there are exactly 25% of the elements that are less than the first quartile and exactly 75% of the elements that are greater than it. The first quartile value can be easily determined by finding the "middle" number between the minimum and the median. For the hourly temperatures, the "middle" number found between 57°F and 70°F is 66°F.

The third quartile value (***Q*3** **or 75th percentile)** is the number that marks three quarters of the ordered data set. In other words, there are exactly 75% of the elements that are less than the third quartile and 25% of the elements that are greater than it. The third quartile value can be easily obtained by finding the "middle" number between the median and the maximum. For the hourly temperatures, the "middle" number between 70°F and 81°F is 75°F.

The interquartile range, or IQR, can be calculated by subtracting the first quartile value (***Q*1**) from the third quartile value (***Q*3**):

${\text{IQR}}=Q_{3}-Q_{1}=75^{\circ }F-66^{\circ }F=9^{\circ }F.$

Hence, $1.5{\text{IQR}}=1.5\cdot 9^{\circ }F=13.5^{\circ }F.$

1.5 IQR above the third quartile is:

$Q_{3}+1.5{\text{ IQR}}=75^{\circ }F+13.5^{\circ }F=88.5^{\circ }F.$

1.5 IQR below the first quartile is:

$Q_{1}-1.5{\text{ IQR}}=66^{\circ }F-13.5^{\circ }F=52.5^{\circ }F.$

The upper whisker boundary of the box plot is the largest data value that is within 1.5 IQR above the third quartile. Here, 1.5 IQR above the third quartile is 88.5°F and the maximum is 81°F. Therefore, the upper whisker is drawn at the value of the maximum, which is 81°F.

Similarly, the lower whisker boundary of the box plot is the smallest data value that is within 1.5 IQR below the first quartile. Here, 1.5 IQR below the first quartile is 52.5°F and the minimum is 57°F. Therefore, the lower whisker is drawn at the value of the minimum, which is 57°F.

### Example with outliers

Above is an example without outliers. Here is a follow-up example for generating box plot with outliers:

The ordered set for the recorded temperatures is (°F): 52, 57, 57, 58, 63, 66, 66, 67, 67, 68, 69, 70, 70, 70, 70, 72, 73, 75, 75, 76, 76, 78, 79, 89.

In this example, only the first and the last number are changed. The median, third quartile, and first quartile remain the same.

In this case, the maximum value in this data set is 89°F, and 1.5 IQR above the third quartile is 88.5°F. The maximum is greater than 1.5 IQR plus the third quartile, so the maximum is an outlier. Therefore, the upper whisker is drawn at the greatest value smaller than 1.5 IQR above the third quartile, which is 79°F.

Similarly, the minimum value in this data set is 52°F, and 1.5 IQR below the first quartile is 52.5°F. The minimum is smaller than 1.5 IQR minus the first quartile, so the minimum is also an outlier. Therefore, the lower whisker is drawn at the smallest value greater than 1.5 IQR below the first quartile, which is 57°F.

### In the case of large datasets

An additional example for obtaining box plot from a data set containing a large number of data points is:

#### General equation to compute empirical quantiles

$q_{n}(p)=x_{(k)}+\alpha (x_{(k+1)}-x_{(k)})$

${\text{with }}k=[p(n+1)]{\text{ and }}\alpha =p(n+1)-k$

Here

$x_{(k)}$

stands for the general ordering of the data points (i.e. if

$i<k$

, then

$x_{(i)}<x_{(k)}$

)

Using the above example that has 24 data points (*n* = 24), one can calculate the median, first and third quartile either mathematically or visually.

**Median**

${\begin{aligned}q_{n}(0.5)&=x_{(12)}+(0.5\cdot 25-12)\cdot (x_{(13)}-x_{(12)})\\[5pt]&=70+(0.5\cdot 25-12)\cdot (70-70)=70^{\circ }{\text{F}}\end{aligned}}$

**First quartile**

${\begin{aligned}q_{n}(0.25)&=x_{(6)}+(0.25\cdot 25-6)\cdot (x_{(7)}-x_{(6)})\\[5pt]&=66+(0.25\cdot 25-6)\cdot (66-66)=66^{\circ }{\text{F}}\end{aligned}}$

**Third quartile**

${\begin{aligned}q_{n}(0.75)&=x_{(18)}+(0.75\cdot 25-18)\cdot (x_{(19)}-x_{(18)})\\[5pt]&=75+(0.75\cdot 25-18)\cdot (75-75)=75^{\circ }{\text{F}}\end{aligned}}$

## Visualization

Although box plots may seem more primitive than histograms or kernel density estimates, they do have a number of advantages. First, the box plot enables statisticians to do a quick graphical examination on one or more data sets. Box plots also take up less space and are therefore particularly useful for comparing distributions between several groups or sets of data in parallel. Lastly, the overall structure of histograms and kernel density estimate can be strongly influenced by the choice of number and width of bins techniques and the choice of bandwidth, respectively.

Although looking at a statistical distribution is more common than looking at a box plot, it can be useful to compare the box plot against the probability density function (theoretical histogram) for a normal N(0,*σ*2) distribution and observe their characteristics directly.
