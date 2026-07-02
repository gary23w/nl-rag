---
title: "Getting Started"
source: https://pugjs.org/api/getting-started.html
domain: pug-templating
license: CC-BY-SA-4.0
tags: pug templating, pug template engine, jade template engine, html template rendering
fetched: 2026-07-02
---

# Getting Started

## Installation

Pug is available via npm:

```
$ npm install pug
```

## Overview

The general rendering process of Pug is simple. `pug.compile()` will compile the Pug source code into a JavaScript function that takes a data object (called “`locals`”) as an argument. Call that resultant function with your data, and *voilà!*, it will return a string of HTML rendered with your data.

The compiled function can be re-used, and called with different sets of data.

```
p #{name}'s Pug source code!
```

```
const pug = require('pug');

const compiledFunction = pug.compileFile('template.pug');

console.log(compiledFunction({
  name: 'Timothy'
}));

console.log(compiledFunction({
  name: 'Forbes'
}));
```

Pug also provides the `pug.render()` family of functions that combine compiling and rendering into one step. However, the template function will be re-compiled every time `render` is called, which might impact performance. Alternatively, you can use the `cache` option with `render`, which will automatically store the compiled function into an internal cache.

```
const pug = require('pug');

console.log(pug.renderFile('template.pug', {
  name: 'Timothy'
}));
```
