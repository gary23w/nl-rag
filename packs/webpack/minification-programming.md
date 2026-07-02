---
title: "Minification (programming)"
source: https://en.wikipedia.org/wiki/Minification_(programming)
domain: webpack
license: CC-BY-SA-4.0
tags: webpack bundler, webpack loader, webpack bundle, module bundler config
fetched: 2026-07-02
---

# Minification (programming)

**Minification** (also **minimisation** or **minimization**) is the process of removing all unnecessary characters from the source code of interpreted programming languages or markup languages without changing its functionality. These unnecessary characters usually include whitespace characters, new line characters, comments, and sometimes block delimiters, which are used to add readability to the code but are not required for it to execute. Minification reduces the size of the source code, making its transmission over a network (e.g. the Internet) more efficient. In programmer culture, aiming at extremely minified source code is the purpose of recreational code golf competitions and a part of the demoscene.

Minification can be distinguished from the more general concept of data compression in that the minified source can be interpreted immediately without the need for a decompression step: the same interpreter can work with both the original as well as with the minified source.

The goals of minification are not the same as the goals of obfuscation; the former is often intended to be reversed using a pretty printer or unminifier. However, to achieve its goals, minification sometimes uses techniques also used by obfuscation; for example, shortening variable names and refactoring the source code. When minification uses such techniques, the pretty-printer or unminifier can only fully reverse the minification process if it is supplied details of the transformations done by such techniques. If not supplied those details, the reversed source code will contain different variable names and control flow, even though it will have the same functionality as the original source code.

## Example

For example, the JavaScript code

```mw
// This is a comment that will be removed by the minifier
var array = [];
for (var i = 0; i < 20; i++) {
  array[i] = i;
}
```

is equivalent to but longer than

```mw
for(var a=[],i=0;i<20;a[i]=i++);
```

## History

In 2001 Douglas Crockford introduced JSMin, which removed comments and whitespace from JavaScript code. It was followed by YUI Compressor in 2007. In 2009, Google opened up its Closure toolkit, including Closure Compiler which contained a source mapping feature together with a Firefox extension called Closure Inspector. In 2010, Mihai Bazon introduced UglifyJS, which was superseded by UglifyJS2 in 2012; the rewrite was to allow for source map support. From 2017, Alex Lam took over maintenance and development of UglifyJS2, replacing it with UglifyJS3 which unified the CLI with the API. In 2018, Terser has been forked from uglify-es and has gained momentum since; in 2020 it outstripped UglifyJS when measured in daily downloads. Since late 2018, Terser has recommended the bundler RollupJS.

## Source mapping

A **source map** is a file format that allows software tools for JavaScript to display different code to a user than the code actually executed by the computer. For example, to aid in debugging of minified code, by "mapping" this code to the original unminified source code instead.

The original format was created by Joseph Schorr as part of the Closure Inspector minification project. Version 2 and 3 of the format reduced the size of the map files considerably. In 2024, source maps were standardized by Ecma International's TC39 technical committee as ECMA-426.

## Types

JavaScript and Cascading Style Sheets (CSS) resources may be minified, preserving their behavior while considerably reducing their file size. Libraries available online are capable of minification and optimization to varying degrees. Some libraries also merge multiple script files into a single file for client download. JavaScript source maps can make code readable and debuggable even after it has been combined and minified.
