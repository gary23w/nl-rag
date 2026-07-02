---
title: "Tree shaking"
source: https://en.wikipedia.org/wiki/Tree_shaking
domain: rollup
license: CC-BY-SA-4.0 / MIT (rollupjs.org)
tags: rollup bundler, rollupjs, es module bundler, rollup tree shaking
fetched: 2026-07-02
---

# Tree shaking

In computing, **tree shaking** is a dead code elimination technique that is applied when optimizing code. Often contrasted with traditional single-library dead code elimination techniques common to minifiers, tree shaking eliminates unused functions from across the bundle by starting at the entry point and only including functions that may be executed. It is succinctly described as "live code inclusion".

## History

Dead code elimination in dynamic languages is a much harder problem than in static languages. The idea of a "treeshaker" originated in LISP in the 1990s. The idea is that all possible execution flows of a program can be represented as a tree of function calls, so that functions that are never called can be eliminated.

The algorithm was applied to JavaScript in Google Closure Tools and then to Dart in the dart2js compiler also written by Google, presented by Bob Nystrom in 2012 and described by the book *Dart in Action* by author Chris Buckett in 2013:

> When code is converted from Dart to JavaScript the compiler does 'tree shaking'. In JavaScript you have to add an entire library even if you only need it for one function, but thanks to tree shaking the Dart-derived JavaScript only includes the individual functions that you need from a library

— Chris Buckett

The next wave of popularity of the term is attributed to Rich Harris's Rollup project developed in 2015.

## Relation to ECMAScript 6 modules

The popularity of tree shaking in JavaScript is based on the fact that in contrast to CommonJS modules, ECMAScript 6 module loading is static and thus the whole dependency tree can be deduced by statically parsing the syntax tree. Thus tree shaking becomes an easy problem. However, tree shaking does not only apply at the import/export level: it can also work at the statement level, depending on the implementation.
