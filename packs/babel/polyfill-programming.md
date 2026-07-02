---
title: "Polyfill (programming)"
source: https://en.wikipedia.org/wiki/Polyfill_(programming)
domain: babel
license: CC-BY-SA-4.0
tags: babel transpiler, babel transcompiler, ecmascript polyfill, jsx transform
fetched: 2026-07-02
---

# Polyfill (programming)

In software development, a **polyfill** is code that implements a new standard feature of a deployment environment within an old version of that environment that does not natively support the feature. Most often, it refers to JavaScript code that implements an HTML5 or CSS web standard, either an established standard (supported by some browsers) on older browsers, or a proposed standard (not supported by any browsers) on existing browsers. Polyfills are also used in PHP and Python.

Polyfills allow web developers to use an API regardless of whether or not it is supported by a browser, and usually with minimal overhead. Typically they first check if a browser supports an API, and use it if available, otherwise using their own implementation. Polyfills themselves use other, more supported features, and thus different polyfills may be needed for different browsers. The term is also used as a verb: *polyfilling* is providing a polyfill for a feature.

## Definition

The term is a neologism, coined by Remy Sharp, who required a word that meant "replicate an API using JavaScript (or Flash or whatever) if the browser doesn’t have it natively" while co-writing the book *Introducing HTML5* in 2009. Formally, "a shim is a library that brings a new API to an older environment, using only the means of that environment." Polyfills exactly fit this definition; the term *shim* was also used for early polyfills. However, to Sharp *shim* connoted non-transparent APIs and workarounds, such as spacer GIFs for layout, sometimes known as `shim.gif`, and similar terms such as *progressive enhancement* and *graceful degradation* were not appropriate, so he invented a new term. The term is based on the multipurpose filling paste brand *Polyfilla,* a paste used to cover up cracks and holes in walls, and the meaning "fill in holes (in functionality) in many (poly-) ways." The word has since gained popularity, particularly due to its use by Paul Irish and in Modernizr documentation.

The distinction that Sharp makes is:

> What makes a polyfill different from the techniques we have already, like a shim, is this: if you removed the polyfill script, your code would continue to work, without any changes required *in spite of the polyfill being removed.*

This distinction is not drawn by other authors. At times various other distinctions are drawn between shims, polyfills, and fallbacks, but there are no generally accepted distinctions: most consider polyfills a form of shim. The term *polyfiller* is also occasionally found.

## Examples

### core-js

core-js is one of the most popular JavaScript standard library polyfills. Includes polyfills for ECMAScript up to the latest version of the standard: promises, symbols, collections, iterators, typed arrays, many other features, ECMAScript proposals, some cross-platform WHATWG / W3C features and proposals like `URL`. You can load only required features or use it without global namespace pollution. It can be integrated with Babel, which allows it to automatically inject required core-js modules into your code.

### html5shiv

In IE versions prior to 9, unknown HTML elements like `<section>` and `<nav>` would be parsed as empty elements, breaking the page's nesting structure and making those elements impossible to style using CSS. One of the most widely used polyfills, html5shiv, exploits another quirk of IE to work around this bug: calling `document.createElement("tagname")` for each of the new HTML5 elements, which causes IE to parse them correctly. It also includes basic default styling for those HTML5 elements.

### -prefix-free

Though most polyfills target out-of-date browsers, some exist to simply push modern browsers forward a little bit more. Lea Verou's -prefix-free polyfill is such a polyfill, allowing current browsers to recognise the unprefixed versions of several CSS3 properties instead of requiring the developer to write out all the vendor prefixes. It reads the page's stylesheets and replaces any unprefixed properties with their prefixed counterparts recognised by the current browser.

### Selectivizr

Keith Clark's Selectivizr is a popular polyfill that makes many CSS3 selectors work in IE 8 and below. It reads the page's stylesheets looking for a number of known CSS3 selectors, then uses a JavaScript selector library to query the document for elements matching those selectors, applying the styles directly to those elements. It supports several JavaScript selector libraries such as jQuery.

### Flexie

One of the features of CSS3, Flexible Box Layout (a.k.a. Flexbox) promises to be an extremely powerful tool for laying out interface elements. WebKit and Mozilla engines have supported a preliminary draft syntax for years. Flexie implements support for that same syntax in IE and Opera. However, the draft spec has undergone a drastic revision to a new (and much more powerful) syntax, which is not yet supported by Flexie. Flexie can still be used along with the old syntax, but the developer must make sure they include the new syntax for future browsers as well.

### CSS3 PIE

PIE ("Progressive Internet Explorer") implements some of the most popular missing CSS3 box decoration properties in IE, including border-radius and box-shadow for IE 8 and below, and linear-gradient backgrounds for IE 9 and below. Invoked as a HTC behavior (a proprietary IE feature), it looks for the unsupported CSS3 properties on specific elements and renders those properties using VML for IE 6–8 and SVG for IE 9. Its rendering is mostly indistinguishable from native browser implementations and it handles dynamic DOM modification well.

### JSON 2

Douglas Crockford originally wrote json2.js as an API for reading and writing his (then up-and-coming) JSON data format. It became so widely used that browser vendors decided to implement its API natively and turn it into a *de facto* standard; Since json2.js now implements features native to newer browsers into older browsers, it has become a polyfill instead of a library.

### es5-shim

ECMAScript 5th Edition ("ES5") brings some useful new scripting features, and since they're syntactically compatible with older JavaScript engines they can mostly be polyfilled by patching methods onto built-in JS objects. This es5-shim polyfill does it in two parts: es5-shim.js contains those methods that can be fully polyfilled, and es5-sham.js contains partial implementations of the other methods which rely too much on the underlying engine to work accurately.

### FlashCanvas

FlashCanvas is an implementation of the HTML5 Canvas API using an Adobe Flash plug-in. A rare commercial polyfill, it comes in a paid version, as well as a free version, which lacks a few advanced features like shadows.

### MediaElement.js

John Dyer's MediaElement.js polyfills support for `<video>` and `<audio>` elements, including the HTML5 MediaElement API, in older browsers using Flash or Silverlight plug-ins. It also provides an optional media player UI for those elements, which is consistent across all browsers.

### Polyfill.io

A JavaScript library created by Andrew Betts that implemented Polyfill. In February 2024, the library's domain was acquired by China-based company Funnull and within a few months became part of a supply chain attack.

### BrowserID

Authentication protocol proposed by Mozilla, failed to gain traction.

### Webshims Lib

Alexander Farkas's Webshims Lib aggregates many other polyfills together into a single package and conditionally loads only those needed by the visiting browser.

### Hyphenopoly.js

Hyphenopoly.js enables automatic hyphenation if it is not already supported by the browser for the respective document language.
