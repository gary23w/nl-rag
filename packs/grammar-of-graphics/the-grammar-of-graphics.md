---
title: "Wilkinson's Grammar of Graphics"
source: https://en.wikipedia.org/wiki/The_Grammar_of_Graphics
domain: grammar-of-graphics
license: CC-BY-SA-4.0
tags: grammar of graphics, ggplot2, semiology of graphics, layered grammar
fetched: 2026-07-02
---

# Wilkinson's Grammar of Graphics

(Redirected from

The Grammar of Graphics

)

The **Grammar of Graphics** (GoG) is a grammar-based system for representing graphics to provide grammatical constraints on the composition of data and information visualizations. A graphical grammar differs from a graphics pipeline as it focuses on semantic components such as scales and guides, statistical functions, coordinate systems, marks and aesthetic attributes. For example, a bar chart can be converted into a pie chart by specifying a polar coordinate system without any other change in graphical specification.

The grammar of graphics concept was launched by Leland Wilkinson in 2001 (Wilkinson et al., 2001; Wilkinson, 2005) and graphical grammars have since been written in a variety of languages with various parameterisations and extensions. The major implementations of graphical grammars are nViZn created by a team at SPSS/IBM, followed by Polaris focusing on multidimensional relational databases which is commercialised as Tableau, a revised Layered Grammar of Graphics by Hadley Wickham in Ggplot2, and Vega-Lite which is a visualisation grammar with added interactivity. The grammar of graphics continues to evolve with alternate parameterisations, extensions, or new specifications.

## Wilkinson's Grammar of Graphics

### Theory

Wilkinson conceived the seven elements of a graphics to be

- **Variables**: mapping of objects to values represented in a graphic
- **Algebra**: operations to combine variables and specify dimensions of graphs
- **Geometry**: creation of geometric graphs from variables
- **Aesthetics**: sensory attributes
- **Statistics**: functions to change the appearance and representation of graphs
- **Scales**: represent variables on measured dimensions
- **Coordinates**: mapping to coordinate systems

With these, Wilkinson hypothesised that

1. These seven constructs are orthogonal and virtually all known statistical charts can be generated relatively parsimoniously
2. This computational system is not a taxonomy of charts and rather it describes the meaning of what we do when we construct statistical graphics.

### Implementations

Wilkinson wrote SYSTAT, a statistical software package, in the early 1980s. This program was noted for its comprehensive graphics, including the first software implementation of the heatmap display now widely used among biologists. After his company grew to 50 employees, he sold it to SPSS in 1995. At SPSS, he assembled a team of graphics programmers who developed the nViZn platform that produces the visualizations in SPSS, Clementine, and other analytics products.

While at Stanford, Tableau founders Hanrahan and Stolte, as well as Diane Tang, created the predecessor to Tableau, named Polaris. Polaris was a data visualization software tool, built with the support of a United States Department of Energy defense program, the Accelerated Strategic Computing Initiative (ASCI). The main differences between Wilkinson's system and Polaris are the use of SQL relational algebra for database services and using shelves instead of cross and nest operators.

## Wickham's Layered Grammar of Graphics

### Theory

Hadley Wickham conceived an alternate parameterisation of the syntax Wilkinson had derived, creating a layered grammar of graphics which he implemented as ggplot2 for R (programming language) users. This added a hierarchy of defaults based around the idea of building up a graphic from multiple layers. Wickham conceived these elements to be:

- **Defaults**: consists of data and mapping
  - **Data**: dataset
  - **Mapping**: aesthetic mappings
- **Layer**: consists of data, mapping, geom, stat, and position
  - **Data**: dataset, or inherit from defaults
  - **Mapping**: aesthetic mappings, or inherit from defaults
  - **Geom**: geometric object
  - **Stat**: statistical transformation
  - **Position**: position adjustment
- **Scale**: mapping of data to aesthetic attributes
- **Coord**: mapping of data to the plane of the plot
- **Facet**: split up the data

### Reception

Wilkinson is generally positive on Wickham's parameterisation and implementation of ggplot2, praising its elegance and expressivity whilst claiming that his original Grammar of Graphics is capable of representing a wider range of statistical graphics.

### Implementations

ggplot2 is the first implementation of a layered grammar of graphics in R and implementations in other programming languages have ensued. These include direct ports plotnine for Python, gramm for MATLAB, Lets-Plot for Kotlin and gadfly for Julia. Projects inspired by elements of Wickham's grammar include Vega-Lite which specifies plots in JSON and uses a JavaScript engine. Implementations for Python include Vega-Altair (built on top of Vega-Lite).

## Vega-Lite: A Grammar of Interactive Graphics

### Theory

Vega-Lite combines ideas from Wilkinson's Grammar of Graphics and Wickham's Layered Grammar of Graphics with a composition algebra for layered and multi-view displays with a grammar of interaction. The Vega-Lite specification is instantiated in JSON and rendered by the lower-level Vega. The graphical grammar implemented by Vega-Lite is composed of the following:

- **Unit**: consists of data, transforms, mark-type and encoding
  - **Data**: relational table consisting of records (rows) and named attributes (columns)
  - **Transforms**: data transformations
  - **Mark-type:** geometric object for visual encoding
  - **Encodings:** mapping of data attributes to visual marks properties where each encoding consists of:
    - **Channel:** e.g. colour, shape, size, or text
    - **Field:** data attribute
    - **Data-type:** e.g. nominal, ordinal, quantitative, or temporal
    - **Value:** use a literal instead of a data-type
    - **Functions:** e.g. binning, aggregation, and sorting
    - **Scale:** maps from data domain to visual range
    - **Guide:** axis or legend for visualising scale
- **Composite Views:** compose views from multiple unit specifications with operators:
  - **Layer**: charts plotted on top of each other
  - **Hconcat/Vconcat**: place views side-by-side
  - **Facet**: subset data to produce a trellis plot
  - **Repeat**: multiple plots similar to facet but with full data replication in each cell
- **Interaction**: selections identify the set of points a user is interested in manipulating, with components:
  - **Selection**: get the minimal number of backing points
    - **Name**: reference
    - **Type**: how many backing values are stored
    - **Predicate**: determine the set of selected points e.g. single, list, interval
    - **Domain|Range**: store data domain or visual range
    - **Event**: e.g. mouseover, mousedown, mouseup,
    - **Init**: initialise with specific backing points
    - **Transforms**: e.g. project, toggle, translate, zoom, and nearest
    - **Resolve**: resolve selections to union or intersect

#### Implementations

Whilst Vega-Lite is the sole implementation of this graphics grammar specification with compilation to Vega, other implementations do create JSON files which can be interpreted by Vega-Lite.

- ggplot2 is an R package for plotting
- Tableau Software (originally known as Polaris) is a commercial software built using the Grammar of Graphics
- nViZn built by Wilkinson.
- SYSTAT (statistics package) built by Wilkinson
- ggpy, ggplot for Python, but has not been updated since 20 November 2016
- plotnine started as an effort to improve the scalability of ggplot for Python and is largely compatible with ggplot2 syntax.
- Plotly - Interactive, online ggplot2 graphs
- gramm, a plotting class for MATLAB inspired by ggplot2
- gadfly, a system for plotting and visualization written in Julia, based largely on ggplot2
- Chart::GGPlot - ggplot2 port in Perl, but has not been updated since 16 March 2023
- The Lets-Plot for Python library includes a native backend and a Python API, which was mostly based on the ggplot2 package.
- Lets-Plot Kotlin API is an open-source plotting library for statistical data implemented using the Kotlin programming language, and is built on the principles of layered graphics first described in the Leland Wilkinson's work *The Grammar of Graphics*.
- ggplotnim, plotting library using the Nim programming language inspired by ggplot2.
- Vega and Vega-Lite are plotting libraries that use JSON to specify plots.
- Vega-Altair, a Python library built on top of Vega-Lite
- chart-parts - React-friendly Grammar of Graphics, but has not been updated since 10 Dec 2021
- g2 - a JavaScript library
