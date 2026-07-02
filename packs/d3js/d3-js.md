---
title: "D3.js"
source: https://en.wikipedia.org/wiki/D3.js
domain: d3js
license: CC-BY-SA-4.0
tags: d3.js, d3js, data-driven documents, svg data binding
fetched: 2026-07-02
---

# D3.js

**D3.js** (also known as **D3**, short for **Data-Driven Documents**) is a JavaScript library for producing dynamic, interactive data visualizations in web browsers. It makes use of Scalable Vector Graphics (SVG), HTML5, and Cascading Style Sheets (CSS) standards. It is the successor to the earlier Protovis framework. Its development was noted in 2011, as version 2.0.0 was released in August 2011. With the release of version 4.0.0 in June 2016, D3 was changed from a single library into a collection of smaller, modular libraries that can be used independently.

## Context

There have been various previous attempts to bring data visualization to web browsers. The most notable examples were the Prefuse, Flare, and Protovis toolkits, which can all be considered as direct predecessors of D3.js.

Prefuse was a visualization toolkit created in 2005 that required usage of Java, and visualizations were rendered within browsers with a Java plug-in. Flare was a similar toolkit from 2007 that used ActionScript, and required a Flash plug-in for rendering.

In 2009, based on the experience of developing and utilizing Prefuse and Flare, Jeffrey Heer, Mike Bostock, and Vadim Ogievetsky of Stanford University's Stanford Visualization Group created Protovis, a JavaScript library to generate SVG graphics from data. The library was known to data visualization practitioners and academics.

In 2011, the development of Protovis was stopped to focus on a new project, D3.js. Informed by experiences with Protovis, Bostock, along with Heer and Ogievetsky, developed D3.js to provide a more expressive framework that, at the same time, focuses on web standards and provides improved performance.

## Technical principles

The D3.js library uses pre-built functions to select elements, create SVG objects, style them, or add transitions, dynamic effects, or tooltips. These objects can also be styled using CSS. Large datasets can be bound to SVG objects using D3.js functions to generate text/graphic charts and diagrams. The data can be in various formats such as JSON, comma-separated values (CSV) or geoJSON, but, if required, JavaScript functions can be written to read other data formats.

### Selections

The central principle of D3.js design is to enable the programmer to first use a CSS-style selector to select a given set of Document Object Model (DOM) nodes, then use operators to manipulate them in a similar manner to jQuery. For example, one may select all HTML paragraph elements (represented by `<p>...</p>`), and then change their text color, e.g. to lavender:

```mw
d3.selectAll("p")                 // select all <p> elements
  .style("color", "lavender")     // set style "color" to value "lavender"
  .attr("class", "squares")       // set attribute "class" to value "squares"
  .attr("x", 50);                 // set attribute "x" (horizontal position) to value 50px
```

The selection can be based on an HTML tag, class, identifier, attribute, or place in the hierarchy. Once elements are selected, one can apply operations to them. This includes getting and setting attributes, display texts, and styles (as in the above example). Elements may also be added and removed. This process of modifying, creating and removing HTML elements can be made dependent on data, which is the basic concept of D3.js.

### Transitions

By declaring a transition, values for attributes and styles can be smoothly interpolated over a certain time. The following code will make all HTML `<p>...</p>` elements on a page gradually change their text color to pink:

```mw
d3.selectAll("p")             // select all <p> elements
  .transition("trans_1")      // transition with name "trans_1"
    .delay(0)                 // transition starting 0ms after trigger
    .duration(500)            // transitioning for 500ms
    .ease(d3.easeLinear)      // transition easing progression is linear...
  .style("color", "pink");    // ... to color: pink
```

### Data-binding

For more advanced uses, loaded data drives the creation of elements. D3.js loads a given dataset, then, for each of its elements, creates an SVG object with associated properties (shape, colors, values) and behaviors (transitions, events).

```mw
// Data
var countriesData = [
  { name: "Ireland", income: 53000, life: 78, pop: 6378, color: "black" },
  { name: "Norway", income: 73000, life: 87, pop: 5084, color: "blue" },
  { name: "Tanzania", income: 27000, life: 50, pop: 3407, color: "grey" }
];
// Create SVG container
var svg = d3.select("#hook").append("svg")
  .attr("width", 120)
  .attr("height", 120)
  .style("background-color", "#D0D0D0");
// Create SVG elements from data 
svg.selectAll("circle")                  // create virtual circle template
  .data(countriesData)                   // bind data
  .join("circle")                                 // joins data to the selection and creates circle elements for each individual data
  .attr("id", function(d) { return d.name })            // set the circle's id according to the country name
  .attr("cx", function(d) { return d.income / 1000 })   // set the circle's horizontal position according to income 
  .attr("cy", function(d) { return d.life })            // set the circle's vertical position according to life expectancy 
  .attr("r",  function(d) { return d.pop / 1000 * 2 })  // set the circle's radius according to country's population 
  .attr("fill", function(d) { return d.color });        // set the circle's color according to country's color
```

Generated SVG graphics are designed according to the provided data.

### Appending nodes using data

Once a dataset is bound to a document, use of D3.js typically follows a pattern wherein an explicit `.enter()` function, an implicit "update," and an explicit `.exit()` function is invoked for each item in the bound dataset. Any methods chained after the `.enter()` command will be called for each item in the dataset not already represented by a DOM node in the selection (the previous `selectAll()`). Likewise, the implicit update function is called on all existing selected nodes for which there is a corresponding item in the dataset, and `.exit()` is called on all existing selected nodes that do not have an item in the dataset to bind to them. The D3.js documentation provides several examples of how this works.

## Community

D3.js is a popular toolset used by many individuals and organizations for data visualization. Some organizations that use it include The New York Times, Airbnb, and MTV. Mike Bostock created bl.ocks as a website for sharing D3 visualizations and code snippets, which used GitHub Gist to host the code. He later created Observable as a place where programmers could make and share visualizations. (Similar to bl.ocks but the code is all hosted on the observable site). There are also D3 communities on many programming sites like CodePen.
