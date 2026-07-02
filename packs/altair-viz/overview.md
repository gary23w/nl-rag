---
title: "Overview"
source: https://altair-viz.github.io/getting_started/overview.html
domain: altair-viz
license: CC-BY-SA-4.0
tags: python altair, altair declarative viz, vega grammar python
fetched: 2026-07-02
---

# Overview

Vega-Altair is a declarative statistical visualization library for Python, based on Vega and Vega-Lite.

It offers a powerful and concise grammar that enables you to quickly build a wide range of statistical visualizations. Here is an example of using the API to visualize a dataset with an interactive scatter plot:

```python
# import altair with an abbreviated alias
import altair as alt

# load a sample dataset as a pandas DataFrame
from altair.datasets import data
cars = data.cars()

# make the chart
alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()
```

The key idea is that you are declaring links between *data columns* and *visual encoding channels*, such as the x-axis, y-axis and color. The rest of the plot details are handled automatically. Building on this declarative system, a surprising range of plots, from simple to sophisticated, can be created using a concise grammar.

The project is named after the brightest star in the constellation Aquila. From Earth’s sky Altair appears close to Vega, the star from which our parent project drew its name.

This documentation serves as the main reference for learning about Altair. Additional learning material and tutorials can be found in the Learning Material section. It can also be helpful to browse the Vega-Lite documentation.
