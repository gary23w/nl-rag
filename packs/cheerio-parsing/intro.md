---
title: "Welcome to Cheerio!"
source: https://cheerio.js.org/docs/intro
domain: cheerio-parsing
license: CC-BY-SA-4.0
tags: cheerio parsing, server-side html parsing, jquery-like dom traversal, scraping markup selector
fetched: 2026-07-02
---

# Welcome to Cheerio!

# Welcome to Cheerio!

Let’s get a quick overview of **Cheerio in less than 5 minutes**.

## Getting Started

Let’s install Cheerio and its dependencies.

### Setting up Node.js

To install Cheerio, you will need to have Node.js installed on your system.

- Download the latest version of Node.js:
  - When installing Node.js, you are recommended to check all checkboxes related to dependencies.

### Installing Cheerio

Once you have set up Node.js, you can use the following command to install Cheerio:

```
npm install cheerio
```

### Importing Cheerio

Once Cheerio is installed, you can import it into your JavaScript code using the `import` statement:

```
import * as cheerio from 'cheerio';
```

If you are on an older environment (or prefer using CommonJS), you can use the `require` function:

```
const cheerio = require('cheerio');
```

## Using Cheerio

After importing Cheerio, you can start using it to manipulate and scrape web page data.

### Loading a Document

The easiest way of loading HTML is to use the `load` function:

```
const $ = cheerio.load('<h2 class="title">Hello world</h2>');
```

This will load the HTML string into Cheerio and return a `Cheerio` object. You can then use this object to traverse the DOM and manipulate the data.

Learn more about loading documents.

Note

**Cheerio is not a web browser.** Cheerio parses markup and provides an API for traversing/manipulating the resulting data structure. It does not interpret the result as a web browser does. Specifically, it does *not* produce a visual rendering, apply CSS, load external resources, or execute JavaScript which is common for a SPA (single page application). This makes Cheerio **much, much faster than other solutions**. If your use case requires any of this functionality, you should consider browser automation software like Puppeteer and Playwright or DOM emulation projects like JSDom.

### Selecting Elements

Once you have loaded a document, you can use the returned function to select elements from the document.

Here, we will select the `h2` element with the class `title`, and then get the text from it:

```
$('h2.title').text(); // "Hello world"
```

Learn more about selecting elements.

### Traversing the DOM

The `$` function returns a `Cheerio` object, which is similar to an array of DOM elements. It is possible to use this object as a starting point to further traverse the DOM. For example, you can use the `find` function to select elements within the selected elements:

```
$('h2.title').find('.subtitle').text();
```

There are many other functions that can be used to traverse the DOM. Learn more about traversing the DOM.

### Manipulating Elements

Once you have selected an element, you can use the `Cheerio` object to manipulate the element.

Here, we will select the `h2` element with the class `title`, and then change the text inside it. We also add a new `h3` element to the document:

```
$('h2.title').text('Hello there!');

$('h2').after('<h3>How are you?</h3>');
```

Learn more about manipulating elements.

Edit this page on GitHub
