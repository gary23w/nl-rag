---
title: "Data build tool"
source: https://en.wikipedia.org/wiki/Data_build_tool
domain: dbt-transform
license: CC-BY-SA-4.0
tags: data build tool, sql transformation, analytics engineering, elt modeling, materialized view
fetched: 2026-07-02
---

# Data build tool

**Data build tool** (**dbt**) is an open-source command line tool that helps analysts and engineers transform data in their warehouse more effectively.

## History

It started at RJMetrics in 2016 as a solution to add basic transformation capabilities to Stitch (acquired by Talend in 2018). The earliest versions of dbt allowed analysts to contribute to the data transformation process following the best practices of software engineering.

From the beginning, dbt was open source. In 2018, the dbt Labs team (then called Fishtown Analytics) released a commercial product on top of dbt Core.

## Funding

In April 2020, dbt Labs announced its Series A led by Andreessen Horowitz. In November, dbt Labs announced its Series B led by Andreessen Horowitz and Sequoia. And in June 2021, dbt Labs raised its Series C led by Altimeter, Sequoia, and Andreessen Horowitz. In February 2022, the company raised $222 million for its Series D, at a $4.2 billion valuation. In October 2025, dbt Labs announced a definitive agreement to merge with Fivetran in an all-stock deal, with Fivetran CEO George Fraser to lead the combined company and dbt Labs founder Tristan Handy serving as president; the merger was pending regulatory approval as of 2026, with the combined entity projected to approach $600 million in annual recurring revenue.

## Overview

Dbt enables analytics engineers to transform data in their warehouses by writing select statements, and turns these select statements into tables and views. Dbt does the transformation (T) in extract, load, transform (ELT) processes – it does not extract or load data, but is designed to be performant at transforming data already inside of a warehouse. Dbt has the goal of allowing analysts to work more like software engineers, in line with the dbt viewpoint.

Dbt uses YAML files to declare properties. `seed` is a type of reference table used in dbt for static or infrequently changed data, like for example country codes or lookup tables), which are CSV based and typically stored in a seeds folder.
