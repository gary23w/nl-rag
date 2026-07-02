---
title: "Bubble chart"
source: https://en.wikipedia.org/wiki/Bubble_chart
domain: scatter-bubble-charts
license: CC-BY-SA-4.0
tags: scatter plot, bubble chart, scatterplot smoothing, local regression
fetched: 2026-07-02
---

# Bubble chart

A **bubble chart** is a type of chart that displays three dimensions of data. Each entity with its triplet (*v*1, *v*2, *v*3) of associated data is plotted as a disk that expresses two of the *vi* values through the disk's *xy* location and the third through its size. Bubble charts can facilitate the understanding of social, economical, medical, and other scientific relationships.

Bubble charts can be considered a variation of the scatter plot, in which the data points are replaced with bubbles. As the documentation for Microsoft Office explains, "You can use a bubble chart instead of a scatter chart if your data has three data series that each contain a set of values. The sizes of the bubbles are determined by the values in the third data series.".

## Choosing bubble sizes correctly

Using bubbles to represent scalar (one-dimensional) values can be misleading. The human visual system most naturally experiences a disk's size in terms of its diameter, rather than area. This is why most charting software requests the radius or diameter of the bubble as the third data value (after horizontal and vertical axis data). Scaling the size of bubbles based on area can be misleading [ibid].

This scaling issue can lead to extreme misinterpretations, especially where the range of the data has a large spread. And because many people are unfamiliar with—or do not stop to consider—the issue and its impact on perception, those who are aware of it often have to hesitate in interpreting a bubble chart because they cannot assume that the scaling correction was indeed made. It is therefore important that bubble charts not only be scaled correctly, but also be clearly labeled to document that it is area, rather than radius or diameter, that conveys the data.

Judgments based on bubble sizes can be problematic regardless of whether area or diameter is used. For example, bubble charts can lead to misinterpretations such as the *weighted average illusion*, where the sizes of bubbles are taken into account when estimating the mean x- and y-values of the scatterplot. The range of bubble sizes used is often arbitrary. For example, the maximum bubble size is often set to some fraction of the total width of the chart, and therefore will not equal the true measurement value.

## Displaying zero or negative data values in bubble charts

The metaphoric representation of data values as disk areas cannot be extended for displaying values that are negative or zero. As a fallback, some users of bubble charts resort to graphic symbology to express nonpositive data values. As an example, a negative value $v<0$ can be represented by a disk of area v in which is centered some chosen symbol like "×" to indicate that the size of the bubble represents the absolute value of a negative data value. And this approach can be reasonably effective in situations where data values' magnitudes (absolute values) are themselves somewhat important—in other words, where values of v and $-v$ are similar in some context-specific way—so that their being represented by congruent disks makes sense.

To represent zero-valued data, some users dispense with disks altogether, using, say, a square centered at the appropriate location. Others use full circles for positive, and empty circles for negative values.

## Incorporating further dimensions of data

Additional information about the entities beyond their three primary values can often be incorporated by rendering their disks in colors and patterns that are chosen in a systematic way. And, of course, supplemental information can be added by annotating disks with textual information, sometimes as simple as unique identifying labels for cross-referencing to explanatory keys and the like.

## Other uses

- In architecture, the term "bubble chart" is also applied to a first architectural sketch of the layout constructed with bubbles.
- In software engineering, "bubble chart" can refer to a data flow, a data structure or other diagram in which entities are depicted with circles or bubbles and relationships are represented by links drawn between the circles.
- In Information visualization, a "bubble chart" may refer to a technique in which a set of numeric quantities is represented by closely packed circles whose areas are proportional to the quantities. Unlike a traditional bubble chart, such displays don't assign meaning to x- or y-axis positions, but seek to pack circles as tightly as possible to make efficient use of space. These bubble charts were introduced by Fernanda Viegas and Martin Wattenberg and have since become a popular method of displaying data. Circular packing charts are included in popular visualization toolkits such as D3 and have been used by the New York Times.
