---
title: "Bullet graph"
source: https://en.wikipedia.org/wiki/Bullet_graph
domain: dashboard-design
license: CC-BY-SA-4.0
tags: information dashboard, business dashboard, kpi display, bullet graph
fetched: 2026-07-02
---

# Bullet graph

A **bullet graph** is a variation of a bar graph developed by Stephen Few. Seemingly inspired by the traditional thermometer charts and progress bars found in many dashboards, the bullet graph serves as a replacement for dashboard gauges and meters. Bullet graphs were developed to overcome the fundamental issues of gauges and meters: they typically display too little information, require too much space, and are cluttered with useless and distracting decorations. The bullet graph features a single, primary measure (for example, current year-to-date revenue), compares that measure to one or more other measures to enrich its meaning (for example, compared to a target), and displays it in the context of qualitative ranges of performance, such as poor, satisfactory, and good. The qualitative ranges are displayed as varying intensities of a single hue to make them discernible by those who are color blind and to restrict the use of colors on the dashboard to a minimum.

Bullet graphs can be created in R (programming language) using the bulletgraph() function developed by Marco Torchiano. Below is an example of R code using the bulletgraph() function to create a black-and-white and colored bullet graph.

```mw
> # Copy bullet graph functions by M. Torchiano (http://softeng.polito.it/software/R/BulletGraph.R) into R script
> par(mfrow=c(2,1), mar=c(2,9,.1,1))
> bulletgraph(x = 270, ref = 260, limits = c(0,200,250,300), name = "Revenue 2024 YTD", subname = "(US$ in millions)", colored = F)
> bulletgraph(x = 270, ref = 260, limits = c(0,200,250,300), name = "Revenue 2024 YTD", subname = "(US$ in millions)", colored = T)
```

For each example:

- The thick, horizontal center line represents the actual value.
- The thin, black vertical line represents a target value.
- The colored or grey scale bands represent ranges, such as poor, average, and good.

Bullet graphs may be horizontal or vertical and may be stacked to allow comparisons of several measures at once.

More information about bullet graphs can be found in the book *Information Dashboard Design* by Stephen Few.
