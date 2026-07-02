---
title: "Headless browser"
source: https://en.wikipedia.org/wiki/Headless_browser
domain: selenium-python
license: CC-BY-SA-4.0
tags: python selenium, selenium webdriver, browser automation python
fetched: 2026-07-02
---

# Headless browser

A **headless browser** is a web browser without a graphical user interface.

Headless browsers provide automated control of a web page in an environment similar to popular web browsers, but they are executed via a command-line interface or using network communication. They are particularly useful for testing web pages as they are able to render and understand HTML the same way a browser would, including styling elements such as page layout, color, font selection and execution of JavaScript and Ajax which are usually not available when using other testing methods.

Since version 59 of Google Chrome and version 56 of Firefox, there is native support for remote control of the browser. This made earlier efforts obsolete, notably PhantomJS.

## Use cases

The main use cases for headless browsers are:

- Test automation in modern web applications (web testing)
- Taking screenshots of web pages.
- Running automated tests for JavaScript libraries.
- Automating interaction of web pages.

### Other uses

Headless browsers are also useful for web scraping. Google stated in 2009 that using a headless browser could help their search engine index content from websites that use Ajax.

Headless browsers have also been misused in various ways:

- Perform DDoS attacks on web sites.
- Increase advertisement impressions.
- Automate web sites in unintended ways e.g. for credential stuffing.

However, a study of browser traffic in 2018 found no preference by malicious actors for headless browsers. There is no indication that headless browsers are used more frequently than non-headless browsers for malicious purposes, like DDoS attacks, SQL injections or cross-site scripting attacks.

## Usage

As several major browsers natively support headless mode through APIs, some software exists to perform browser automation through a unified interface. These include:

- Selenium WebDriver – a W3C compliant implementation of WebDriver
- Playwright – a Node.js library to automate Chromium, Firefox and WebKit
- Puppeteer – a Node.js library to automate Chrome or Firefox

### Test automation

Some test automation software and frameworks include headless browsers as part of their testing apparati.

- Capybara uses headless browsing, either via WebKit or Headless Chrome to mimic user behavior in its testing protocols.
- Jasmine uses Selenium by default, but can use WebKit or Headless Chrome, to run browser tests.
- Cypress, a frontend testing framework
- QF-Test, a software tool for automated testing of programs via the graphical user interface where a headless browser can also be used for testing.

### Alternatives

Another approach is to use software that provides browser APIs. For example, Deno provides browser APIs as part of its design. For Node.js, jsdom is the most complete provider. While most are able to support common browser features (HTML parsing, cookies, XHR, some JavaScript, etc.), they do not render the DOM and have limited support for DOM events. They usually perform faster than full browsers, but are unable to correctly interpret many popular websites.

Another is HtmlUnit, a headless browser written in Java. HtmlUnit uses the Rhino engine to provide JavaScript and Ajax support as well as partial rendering capability.

## List of headless browsers

These are various software that provide headless browser APIs.

- DotNetBrowser is a proprietary .NET Chromium-based library that provides the off-screen rendering mode and can be used without embedding or displaying windows.
- Lightpanda is an open-source headless browser written in Zig. Unlike Chromium-based headless browsers, it was developed for headless operation and supports the Chrome DevTools Protocol (CDP), DOM access, and JavaScript execution, but not graphical rendering.
- SimpleBrowser is a headless web browser written in C# supporting .NET Standard 2.0
- Splash is a headless web browser written in Python using the WebKit layout engine via Qt. It has an HTTP API, Lua scripting support and a built-in IPython (Jupyter)-based IDE. Development started at ScrapingHub in 2013; it is partially funded by DARPA.
- Zombie.js is a simulated browser environment for Node.js.

An earlier effort (2008) was envjs from John Resig, which was a simulated browser environment written in JavaScript for the Rhino engine.
