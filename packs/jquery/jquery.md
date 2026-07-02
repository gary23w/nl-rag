---
title: "jQuery"
source: https://en.wikipedia.org/wiki/JQuery
domain: jquery
license: CC-BY-SA-4.0
tags: jquery, jquery selector, dom manipulation library, jquery ajax
fetched: 2026-07-02
---

# jQuery

**jQuery** is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation, as well as event handling, CSS animations, and Ajax. It is free, open-source software using the permissive MIT License. As of August 2022, jQuery is used by 77% of the 10 million most popular websites. Web analysis indicates that it is the most widely deployed JavaScript library by a large margin, having at least three to four times more usage than any other JavaScript library.

jQuery's syntax is designed to make it easier to navigate a document, select DOM elements, create animations, handle events, and develop Ajax applications. jQuery also provides capabilities for developers to create plug-ins on top of the JavaScript library. This enables developers to create abstractions for low-level interaction and animation, advanced effects and high-level, theme-able widgets. The modular approach to the jQuery library allows the creation of powerful dynamic web pages and Web applications.

The set of jQuery core features—DOM element selections, traversal, and manipulation—enabled by its *selector engine* (named "Sizzle" from v1.3), created a new "programming style", fusing algorithms and DOM data structures. This style influenced the architecture of other JavaScript frameworks like YUI v3 and Dojo, later stimulating the creation of the standard *Selectors API*.

Microsoft and Nokia bundle jQuery on their platforms. Microsoft includes it with Visual Studio for use within Microsoft's ASP.NET AJAX and ASP.NET MVC frameworks while Nokia has integrated it into the Web Run-Time widget development platform.

## Overview

jQuery, at its core, is a Document Object Model (DOM) manipulation library. The DOM is a tree-structure representation of all the elements of a Web page. jQuery simplifies the syntax for finding, selecting, and manipulating these DOM elements. For example, jQuery can be used for finding an element in the document with a certain property (e.g. all elements with the `h1` tag), changing one or more of its attributes (e.g. `color`, `visibility`), or making it respond to an event (e.g. a mouse click).

jQuery also provides a paradigm for event handling that goes beyond basic DOM element selection and manipulation. The event assignment and the event callback function definition are done in a single step in a single location in the code. jQuery also aims to incorporate other highly used JavaScript functionality (e.g. fade ins and fade outs when hiding elements, animations by manipulating CSS properties).

The principles of developing with jQuery are:

- Separation of JavaScript and HTML: The jQuery library provides simple syntax for adding event handlers to the DOM using JavaScript, rather than adding HTML event attributes to call JavaScript functions. Thus, it encourages developers to completely separate JavaScript code from HTML markup.
- Brevity and clarity: jQuery promotes brevity and clarity with features like "chainable" functions and shorthand function names.
- Elimination of cross-browser incompatibilities: The JavaScript engines of different browsers differ slightly so JavaScript code that works for one browser may not work for another. Like other JavaScript toolkits, jQuery handles all these cross-browser inconsistencies and provides a consistent interface that works across different browsers.
- Extensibility: New events, elements, and methods can be easily added and then reused as a plugin.

## History

jQuery was originally created in January 2006 at BarCamp NYC by John Resig, influenced by Dean Edwards' earlier cssQuery library. It is currently maintained by a team of developers led by Timmy Willison (with the jQuery selector engine, Sizzle, being led by Richard Gibson).

jQuery was originally licensed under the CC BY-SA 2.5, and relicensed to the MIT License in 2006. At the end of 2006, it was dual-licensed under GPL and MIT licenses. As this led to some confusion, in 2012 the GPL was dropped and is now only licensed under the MIT license.

### Popularity

- In 2015, jQuery was used on 62.7% of the top 1 million websites (according to BuiltWith), and 17% of all Internet websites.
- In 2017, jQuery was used on 69.2% of the top 1 million websites (according to Libscore).
- In 2018, jQuery was used on 78% of the top 1 million websites.
- In 2019, jQuery was used on 80% of the top 1 million websites (according to BuiltWith), and 74.1% of the top 10 million (per W3Techs).
- In 2021, jQuery was used on 77.8% of the top 10 million websites (according to W3Techs)*.*

## Features

jQuery includes the following features:

- DOM element selections using the multi-browser open source selector engine Sizzle, a spin-off of the jQuery project
- DOM manipulation based on CSS selectors that uses elements' names and attributes, such as id and class, as criteria to select nodes in the DOM
- Events
- Effects and animations
- Ajax
- Deferred and Promise objects to control asynchronous processing
- JSON parsing
- Extensibility through plug-ins
- Utilities, such as feature detection
- Compatibility methods that are natively available in modern browsers, but need fallbacks for old browsers, such as `jQuery.inArray()` and `jQuery.each()`.
- Cross-browser support

### Browser support

jQuery 3.0 and newer supports "current−1 versions" (meaning the current stable version of the browser and the version that preceded it) of Firefox (and ESR), Chrome, Safari, and Edge as well as Internet Explorer 9 and newer. On mobile it supports iOS 7 and newer, and Android 4.0 and newer.

## Distribution

The jQuery library is typically distributed as a single JavaScript file that defines all its interfaces, including DOM, Events, and Ajax functions. It can be included within a Web page by linking to a local copy or by linking to one of the many copies available from public servers. jQuery has a content delivery network (CDN) hosted by MaxCDN. Google in Google Hosted Libraries service and Microsoft host the library as well.

Example of linking a copy of the library locally (from the same server that hosts the Web page):

```mw
<script src="jquery-4.0.0.min.js"></script>
```

Example of linking a copy of the library from jQuery's public CDN:

```mw
<script
  src="https://code.jquery.com/jquery-4.0.0.min.js"
  integrity="sha256-OaVG6prZf4v69dPg6PhVattBXkcOWQB62pdZ3ORyrao="
  crossorigin="anonymous"></script>
```

## Interface

### Functions

jQuery provides two kinds of functions, static utility functions and jQuery object methods. Each has its own usage style.

Both are accessed through jQuery's main identifier: `jQuery`. This identifier has an alias named `$`. All functions can be accessed through either of these two names.

#### jQuery methods

The `jQuery` function is a factory for creating a jQuery object that represents one or more DOM nodes. jQuery objects have methods to manipulate these nodes. These methods (sometimes called *commands)*, are *chainable* as each method also returns a jQuery object.

Access to and manipulation of multiple DOM nodes in jQuery typically begins with calling the `$` function with a CSS selector string. This returns a jQuery object referencing all the matching elements in the HTML page. `$("div.test")`, for example, returns a jQuery object with all the `div` elements that have the class `test`. This node set can be manipulated by calling methods on the returned jQuery object.

#### Static utilities

These are utility functions and do not directly act upon a jQuery object. They are accessed as static methods on the jQuery or $ identifier. For example, `$.ajax()` is a static method.

### No-conflict mode

jQuery provides a `$.noConflict()` function, which relinquishes control of the `$` name. This is useful if jQuery is used on a Web page also linking another library that demands the `$` symbol as its identifier. In no-conflict mode, developers can use `jQuery` as a replacement for `$` without losing functionality.

### Typical start-point

Typically, jQuery is used by putting initialization code and event handling functions in `$(*handler*)`. This is triggered by jQuery when the browser has finished constructing the DOM for the current Web page.

```mw
$(function () {
        // This anonymous function is called when the page has completed loading.
        // Here, one can place code to create jQuery objects, handle events, etc.
});
```

or

```mw
$(fn); // The function named fn, defined elsewhere, is called when the page has loaded.
```

Historically, `$(document).ready(callback)` has been the de facto idiom for running code after the DOM is ready. However, since jQuery 3.0, developers are encouraged to use the much shorter `$(handler)` signature instead.

### Chaining

jQuery object methods typically also return a jQuery object, which enables the use of *method chains*:

```mw
$('div.test')
  .on('click', handleTestClick)
  .addClass('foo');
```

This line finds all `div` elements with class attribute `test` , then registers an event handler on each element for the "click" event, then adds the class attribute `foo` to each element.

Certain jQuery object methods retrieve specific values (instead of modifying a state). An example of this is the `val()` method, which returns the current value of a text input element. In these cases, a statement such as `$('#user-email').val()` cannot be used for chaining as the return value does not reference a jQuery object.

### Creating new DOM elements

Besides accessing existing DOM nodes through jQuery, it is also possible to create new DOM nodes, if the string passed as the argument to `$()` factory looks like HTML. For example, the below code finds an HTML `select` element, and creates a new `option` element with the value `VAG` and the label `Volkswagen`, which is then appended to the select menu:

```mw
$('select#car-brands')
  .append($('<option>')
    .prop(value,"VAG")
    .text('Volkswagen')
  );
```

### Ajax

It is possible to make Ajax requests (with cross-browser support) with `$.ajax()` to load and manipulate remote data.

```mw
$.ajax({
  type: 'POST',
  url: '/process/submit.php',
  data: {
    name : 'John',
    location : 'Boston',
  },
}).then(function(msg) {
  alert('Data Saved: ' + msg);
}).catch(function(xmlHttpRequest, statusText, errorThrown) {
  alert(
    'Your form submission failed.\n\n'
      + 'XML Http Request: ' + JSON.stringify(xmlHttpRequest)
      + ',\nStatus Text: ' + statusText
      + ',\nError Thrown: ' + errorThrown);
});
```

This example posts the data `name=John` and `location=Boston` to `/process/submit.php` on the server. When this request finishes the success function is called to alert the user. If the request fails it will alert the user to the failure, the status of the request, and the specific error.

The above example uses the `.then()` and `.catch()` methods to register callbacks that run when the response has completed. These promise callbacks must be used due to the asynchronous nature of Ajax requests.

## jQuery plug-ins

jQuery's architecture allows developers to create plug-in code to extend its function. There are thousands of jQuery plug-ins available on the Web that cover a range of functions, such as Ajax helpers, Web services, datagrids, dynamic lists, XML and XSLT tools, drag and drop, events, cookie handling, and modal windows.

An important source of jQuery plug-ins is the plugins sub-domain of the jQuery Project website. The plugins in this subdomain, however, were accidentally deleted in December 2011 in an attempt to rid the site of spam. The new site is a GitHub-hosted repository, which required developers to resubmit their plugins and to conform to new submission requirements. jQuery provides a "Learning Center" that can help users understand JavaScript and get started developing jQuery plugins.

Additionally, for those looking to convert jQuery plugins or code to vanilla JavaScript, tools like the [jQuery to JavaScript Converter](https://codentools.com/jquery-convert-javascript) can be very helpful in automating part of the transition and reducing reliance on jQuery.

## Release history

| Version | Initial release | Latest update | Minified size (KB) | Additional notes |
|---|---|---|---|---|
| 1.0 | August 26, 2006 (2006-08-26) |   |   | First stable release |
| 1.1 | January 14, 2007 (2007-01-14) |   |   |   |
| 1.2 | September 10, 2007 (2007-09-10) | 1.2.6 | 54.5 |   |
| 1.3 | January 14, 2009 (2009-01-14) | 1.3.2 | 55.9 | Sizzle Selector Engine introduced into core |
| 1.4 | January 14, 2010 (2010-01-14) | 1.4.4 | 76.7 |   |
| 1.5 | January 31, 2011 (2011-01-31) | 1.5.2 | 83.9 | Deferred callback management, ajax module rewrite |
| 1.6 | May 3, 2011 (2011-05-03) | 1.6.4 (September 12, 2011 (2011-09-12)) | 89.5 | Significant performance improvements to the attr() and val() functions |
| 1.7 | November 3, 2011 (2011-11-03) | 1.7.2 (March 21, 2012 (2012-03-21)) | 92.6 | New Event APIs: .on() and .off(), while the old APIs are still supported. |
| 1.8 | August 9, 2012 (2012-08-09) | 1.8.3 (November 13, 2012 (2012-11-13)) | 91.4 | Sizzle Selector Engine rewritten, improved animations and $(html, props) flexibility. |
| 1.9 | January 15, 2013 (2013-01-15) | 1.9.1 (February 4, 2013 (2013-02-04)) | 90.5 | Removal of deprecated interfaces and code cleanup |
| 1.10 | May 24, 2013 (2013-05-24) | 1.10.2 (July 3, 2013 (2013-07-03)) | 90.9 | Incorporated bug fixes and differences reported from both the 1.9 and 2.0 beta cycles |
| 1.11 | January 24, 2014 (2014-01-24) | 1.11.3 (April 28, 2015 (2015-04-28)) | 93.7 |   |
| 1.12 | January 8, 2016 (2016-01-08) | 1.12.4 (May 20, 2016 (2016-05-20)) | 94.9 |   |
| 2.0 | April 18, 2013 (2013-04-18) | 2.0.3 (July 3, 2013 (2013-07-03)) | 81.7 | Dropped IE 6–8 support for performance improvements and reduction in filesize |
| 2.1 | January 24, 2014 (2014-01-24) | 2.1.4 (April 28, 2015 (2015-04-28)) | 82.4 |   |
| 2.2 | January 8, 2016 (2016-01-08) | 2.2.4 (May 20, 2016 (2016-05-20)) | 83.6 |   |
| 3.0 | June 9, 2016 (2016-06-09) | 3.0.0 (June 9, 2016 (2016-06-09)) | 84.3 | Promises/A+ support for Deferreds, $.ajax and $.when, .data() HTML5-compatible |
| 3.1 | July 7, 2016 (2016-07-07) | 3.1.1 (September 23, 2016 (2016-09-23)) | 84.7 | jQuery.readyException added, ready handler errors are now not silenced |
| 3.2 | March 16, 2017 (2017-03-16) | 3.2.1 (March 20, 2017 (2017-03-20)) | 84.6 | Added support for retrieving contents of `<template>` elements, and deprecation of various old methods. |
| 3.3 | January 19, 2018 (2018-01-19) | 3.3.1 (January 20, 2018 (2018-01-20)) | 84.9 | Deprecation of old functions, functions that accept classes now also support them in array format. |
| 3.4 | April 10, 2019 (2019-04-10) | 3.4.1 (May 1, 2019) | 86.1 | Performance improvements, `nonce` and `nomodule` support, fixes for radio elements, a minor security fix. |
| 3.5 | April 10, 2020 (2020-04-10) | 3.5.1 (May 4, 2020) | 87.4 | Security fixes, `.even()` & `.odd()` methods, `jQuery.trim` deprecated |
| 3.6 | March 2, 2021 (2021-03-02) | 3.6.4 (March 8, 2023) | 88.2 | Bug fixes, return JSON when there is a JSONP error, handling of new Chrome selectors |
| 3.7 | May 11, 2023 (2023-05-11) | 3.7.1 (August 28, 2023) | 85.4 | `.uniqueSort()` method, performance improvements, `.outerWidth(true)` & `.outerHeight(true)` handling of negative margins, focus fixes |
| 4.0 | January 17, 2026 (2026-01-17) | 4.0.0 (January 17, 2026) | 78.8 | Support for IE 10 and lower dropped (IE 11 is still supported), deprecated APIs removed, Array methods removed, focus event order changed, support for FormData, migration to ES modules |

## Testing framework

QUnit is a test automation framework used to test the jQuery project. The jQuery team developed it as an in-house unit testing library. The jQuery team uses it to test its code and plugins, but it can test any generic JavaScript code, including server-side JavaScript code.

As of 2011, the jQuery Testing Team uses QUnit with TestSwarm to test each jQuery codebase release.

## Alternatives to jQuery

> Simplifying tasks such as HTML document traversal, animation, and event handling, the stalwart jQuery JavaScript library changed the face of web development. As of May 2019, jQuery is still being used in 74 percent of known websites, according to web technology surveyor W3Techs. Nevertheless, the jQuery library, which debuted in August 2006, is now being viewed by some developers as an older technology whose time has passed. Alternatives to jQuery have emerged in recent years, such as the Cash library or even just modern, vanilla JavaScript, now that web browsers all handle JavaScript the same way and jQuery is no longer needed to solve compatibility issues. Arguments on Reddit and videos on YouTube make the case that jQuery has become obsolete, or at least is not as essential as it once was.

— Paul Krill, *InfoWorld* (2019)

As cross-browser compatibility is no longer as much of an issue, most of jQuery can nowadays be replaced with modern web standards, without losing much convenience. Partly due to this, GitHub removed jQuery from its pages in 2018.
