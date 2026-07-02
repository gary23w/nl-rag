---
title: "ECMAScript"
source: https://en.wikipedia.org/wiki/ECMAScript
domain: babel
license: CC-BY-SA-4.0
tags: babel transpiler, babel transcompiler, ecmascript polyfill, jsx transform
fetched: 2026-07-02
---

# ECMAScript

**ECMAScript** (/ˈɛkməskrɪpt/; **ES**) is the standard for the JavaScript language, intended to ensure the interoperability of web pages across different web browsers. It is standardized by Ecma International's TC39 technical committee in the document ECMA-262, with i18n ("Intl") APIs standardized in the document ECMA-402.

ECMAScript is commonly used for client-side scripting on the World Wide Web, and is increasingly being used for server-side scripting and services using runtime environments such as Node.js, Deno and Bun.

The ECMAScript standard does not include any input/output (I/O), such as networking, storage, or graphics facilities. In practice, the web browser or other runtime system provides JavaScript APIs for I/O.

## Standards

Ecma International's Technical Committee 39 publishes multiple standards defining JavaScript, formally known as **ECMAScript**. These include the language syntax, semantics, libraries, and complementary technologies that support the language. The standards are detailed below.

### ECMAScript Language Specification (ECMA-262)

Defines the JavaScript language, formally known as ECMAScript. ECMA-262 only specifies language syntax and the semantics of the core application programming interface (API), such as `Array`, `Function`, and `globalThis`, while valid implementations of JavaScript add their own functionality such as input/output and file system handling.

### ECMAScript Internationalization API Specification (ECMA-402)

Defines the JavaScript i18n (`Intl`) APIs, and is a complement to ECMA-262. Its functionality has been selected from that of internationalization APIs such as those of the International Components for Unicode (ICU) library of the .NET framework, or of the Java platform.

### JSON Data Interchange Syntax (ECMA-404)

Defines the JSON (JavaScript Object Notation) syntax, a human-readable open standard file format and data interchange format. It was derived from JavaScript, but is a programming language-independent data format.

### Source Map Format Specification (ECMA-426)

Defines the Source map format, used for mapping transpiled source code back to its original sources. The original source map format was created by Joseph Schorr for use by the Closure Inspector minification project, to enable source-level debugging of optimized JavaScript code. In 2024, the source map format was published as an Ecma standard.

## History

The ECMAScript specification is a standardized specification of a scripting language developed by Brendan Eich of Netscape; initially named Mocha, then LiveScript, and finally JavaScript. In December 1995, Sun Microsystems and Netscape announced JavaScript in a press release. In November 1996, Netscape announced a meeting of the Ecma International standards organization to advance the standardization of JavaScript. The first edition of ECMA-262 was adopted by the Ecma General Assembly in June 1997. Several editions of the language standard have been published since then. The name "ECMAScript" was a compromise between the organizations involved in standardizing the language, especially Netscape and Microsoft, whose disputes dominated the early standards sessions. Eich commented that "ECMAScript was always an unwanted trade name that sounds like a skin disease." ECMAScript has been formalized through operational semantics by work at Stanford University and the Department of Computing, Imperial College London for security analysis and standardization. "ECMA" stood for "European Computer Manufacturers Association" until 1994.

### Evolution

Ecma's Technical Committee 39 (TC39) is responsible for the maintenance of ECMAScript. New proposals to the language go through a staged process, with each stage representing the completeness of the proposal's specification. Consensus must be reached within the committee to advance a proposal to the next stage. Proposals that reach stage 4, the final stage, will be included into the next version of the standard. Since the release of version 6 in June 2015, new major versions have been finalized and published every June.

## Features

The ECMAScript language includes structured, dynamic, functional, and prototype-based features.

### Imperative and structured

ECMAScript JavaScript supports C-style structured programming. Previously, JavaScript only supported function scoping using the keyword `var`, but ECMAScript 2015 added the keywords `let` and `const`, allowing JavaScript to support both block scoping and function scoping. JavaScript supports automatic semicolon insertion, meaning that semicolons that normally terminate a statement in C may be omitted in JavaScript.

Like C-style languages, control flow is done with the `while`, `for`, `do` / `while`, `if` / `else`, and `switch` statements. Functions are weakly typed and may accept and return any type. Arguments not provided default to `undefined`.

### Weakly typed

ECMAScript is weakly typed. This means that certain types are assigned implicitly based on the operation being performed. However, there are several quirks in JavaScript's implementation of the conversion of a variable from one type to another.

### Dynamic

ECMAScript is dynamically typed. Thus, a type is associated with a value rather than an expression. ECMAScript supports various ways to test the type of objects, including duck typing.

### Transpiling

Since ES 2015, transpiling JavaScript has become very common. Transpilation is a source-to-source compilation in which newer versions of JavaScript are used, and a transpiler rewrites the source code so that it is supported by older browsers. Usually, transpilers transpile down to ES3 to maintain compatibility with all versions of browsers. The settings to transpile to a specific version can be configured according to need. Transpiling adds an extra step to the build process and is sometimes done to avoid needing polyfills. Polyfills create new features for older environments that lack them. Polyfills do this at runtime in the interpreter, such as the user's browser or on the server. Instead, transpiling rewrites the ECMA code itself during the build phase of development before it reaches the interpreter.

## Conformance

In 2010, Ecma International started developing a standards test for Ecma 262 ECMAScript. Test262 is an ECMAScript conformance test suite that can be used to check how closely a JavaScript implementation follows the ECMAScript Specification. The test suite contains thousands of individual tests, each of which tests some specific requirement(s) of the ECMAScript specification. The development of Test262 is a project of the Ecma Technical Committee 39 (TC39). The testing framework and the individual tests are contributed to Ecma by member organizations of TC39.

Important contributions were made by Google (Sputnik test suite) and Microsoft, who both contributed thousands of tests. The Test262 test suite consisted of 38014 tests as of January 2020. ECMAScript specifications through ES7 are well-supported in major web browsers. The table below shows the conformance rate for current versions of software with respect to the most recent editions of ECMAScript.

| Scripting engine | Reference application(s) | Conformance |   |   |   |
|---|---|---|---|---|---|
| ES5 | ES6 (2015) | ES2016+ | ES.Next |   |   |
| SpiderMonkey | Firefox 120 | 100% | 98% | 98% | 5% |
| V8 | Google Chrome 117, Microsoft Edge 113, Opera 98 | 100% | 98% | 98% | 5% |
| JavaScriptCore | Safari 17 | 99% | 100% | 98% | 11% |
