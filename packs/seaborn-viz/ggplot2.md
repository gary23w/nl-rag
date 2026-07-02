---
title: "ggplot2"
source: https://en.wikipedia.org/wiki/Ggplot2
domain: seaborn-viz
license: CC-BY-SA-4.0
tags: python seaborn, seaborn visualization, statistical plots python
fetched: 2026-07-02
---

# ggplot2

ggplot2

Base graphics

ggplot2 and base graphics defaults for a simple scatterplot image

**ggplot2** is an open-source data visualization package for the statistical programming language R. Created by Hadley Wickham in 2005, ggplot2 is an implementation of Leland Wilkinson's *Grammar of Graphics*—a general scheme for data visualization which breaks up graphs into semantic components such as scales and layers. ggplot2 can serve as a replacement for the base graphics in R and contains a number of defaults for web and print display of common scales. Since 2005, ggplot2 has grown in use to become one of the most popular R packages.

## Updates

On 2 March 2012, ggplot2 version 0.9.0 was released with numerous changes to internal organization, scale construction and layers.

On 25 February 2014, Hadley Wickham formally announced that "ggplot2 is shifting to maintenance mode. This means that we are no longer adding new features, but we will continue to fix major bugs, and consider new features submitted as pull requests. In recognition [of] this significant milestone, the next version of ggplot2 will be 1.0.0".

On 21 December 2015, ggplot2 2.0.0 was released. In the announcement, it was stated that "ggplot2 now has an official extension mechanism. This means that others can now easily create their [own] stats, geoms and positions, and provide them in other packages."

On 5 July 2018, ggplot2 3.0.0 was released (initially planned as a ggplot2 2.3.0). This now provides support for tidy evaluation allowing quasiquotation in ggplot2 functions.

On 11 September 2025, ggplot2 4.0.0 was released. The accompanying blog post indicated that the release included "a rewrite of the object oriented system from S3 to S7, large new features to smaller quality of life improvements and bugfixes."

## Comparison with base graphics and other packages

In contrast to base R graphics, ggplot2 allows the user to add, remove or alter components in a plot at a high level of abstraction. This abstraction comes at a cost, with ggplot2 being slower than lattice graphics.

Creating separate plots for various subsets of data in base R requires loops and manual management, whereas ggplot2 simplifies that process with a collection of "facet" functions to choose from.

One potential limitation of base R graphics is the "pen-and-paper model" utilized to populate the plotting device. Graphical output from the interpreter is added directly to the plotting device or window, rather than separately for each distinct element of a plot. In this respect it is similar to the lattice package, though Wickham argues ggplot2 inherits a more formal model of graphics from Wilkinson. As such, it allows for a high degree of modularity; the same underlying data can be transformed by many different scales or layers.

Plots may be created via the convenience function `qplot()` where arguments and defaults are meant to be similar to base R's `plot()` function. More complex plotting capacity is available via `ggplot()` which exposes the user to more explicit elements of the grammar.

## Impact

After ten years of being developed, ggplot2 has continued to make an impact on the data visualization community: it has had over 10 million downloads, up to 400,000 downloads in a given month, and is used by data scientists from the US government to journalists at *The New York Times* to analyze and present data. Wickham posits the success of ggplot2 comes from the increased popularity of the R language and the relative ease of making aesthetically appealing graphics. Along with more serious uses of ggplot2, Wickham also supports the more unusual use cases, like exploring factors for winning in the reality TV show RuPaul's Drag Race.

See implementations of The Grammar of Graphics.
