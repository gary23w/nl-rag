---
title: "TypeScript"
source: https://en.wikipedia.org/wiki/TypeScript
domain: source-maps
license: CC-BY-SA-4.0
tags: source maps, javascript source mapping, minified code debugging, transpiled code mapping
fetched: 2026-07-02
---

# TypeScript

**TypeScript** (**TS**) is a high-level programming language that adds static typing with optional type annotations to JavaScript. It is designed for developing large applications. It transpiles to JavaScript. It is developed by Microsoft as free and open-source software released under an Apache License 2.0.

TypeScript may be used to develop JavaScript applications for both client-side and server-side execution (as with React.js, Node.js, Deno or Bun). Multiple options are available for transpiling. The default TypeScript Compiler can be used, or the Babel compiler can be invoked to convert TypeScript to JavaScript.

TypeScript supports definition files that can contain type information of existing JavaScript libraries, much like C++ header files can describe the structure of existing object files. This enables other programs to use the values defined in the files as if they were statically typed TypeScript entities. There are third-party header files for popular libraries such as jQuery, MongoDB, and D3.js. TypeScript headers for the Node.js library modules are also available, allowing development of Node.js programs within TypeScript.

The TypeScript compiler is written in TypeScript and compiled to JavaScript. It is licensed under the Apache License 2.0. Anders Hejlsberg, lead architect of C# and creator of Delphi and Turbo Pascal, has worked on developing TypeScript.

## History

TypeScript was released to the public in October 2012, with version 0.8, after two years of internal development at Microsoft. Soon after the initial public release, Miguel de Icaza praised the language, but criticized the lack of mature integrated development environment (IDE) support apart from Microsoft Visual Studio, which was unavailable then on Linux and macOS. As of April 2021 there is support in other IDEs and text editors, including Emacs, Vim, WebStorm, Atom and Microsoft's own Visual Studio Code. TypeScript 0.9, released in 2013, added support for generics.

TypeScript 1.0 was released at Microsoft's Build developer conference in 2014. Visual Studio 2013 Update 2 provided built-in support for TypeScript. Further improvement were made in July 2014, when the development team announced a new TypeScript compiler, asserted to have a five-fold performance increase. Simultaneously, the source code, which was initially hosted on CodePlex, was moved to GitHub.

On 22 September 2016, TypeScript 2.0 was released, introducing several features, including the ability for programmers to optionally enforce null safety.

TypeScript 3.0 was released on 30 July 2018, bringing many language additions like tuples in rest parameters and spread expressions, rest parameters with tuple types, generic rest parameters and so on.

TypeScript 4.0 was released on 20 August 2020. While 4.0 did not introduce any breaking changes, it added language features such as Custom JSX Factories and Variadic Tuple Types.

TypeScript 5.0 was released on 16 March 2023 and included support for decorators.

On March 11, 2025, Anders Hejlsberg announced on the TypeScript blog that the team is working on a Go port of the TypeScript compiler to be released as TypeScript version 7.0 later this year. It is expected to feature a 10x speedup.

On December 2nd, 2025, Daniel Rosenwasser announced on the blog that TypeScript 6.0 will be the last release written in TypeScript itself, and TypeScript 7.0 will be the first Go-based release.

## Design

TypeScript originated from the shortcomings of JavaScript for developing large-scale applications both at Microsoft and among their external customers. Challenges with dealing with complex JavaScript code led to demand for custom tooling to ease developing of components in the language.

Developers sought a solution that would not break compatibility with the ECMAScript (ES) standard and its ecosystem, so a compiler was developed to transform a superset of JavaScript with type annotations and classes (TypeScript files) back into vanilla ECMAScript 5 code. TypeScript classes were based on the then-proposed ECMAScript 6 class specification to make writing prototypal inheritance less verbose and error-prone, and type annotations enabled IntelliSense and improved tooling.

## Features

TypeScript adds the following syntax extensions to JavaScript:

- Type signatures (annotations) and compile-time type checking
- Type inference
- Interfaces
- Enumerated types
- Generics
- Namespaces
- Tuples

Syntactically, TypeScript is very similar to JScript .NET, another Microsoft implementation of the ECMA-262 language standard that added support for static typing and classical object-oriented language features such as classes, inheritance, interfaces, and namespaces. Other inspirations include Java and C#.

## Compatibility with JavaScript

As TypeScript is simply a superset of JavaScript, existing JavaScript can be adapted to TypeScript and TypeScript program can seamlessly consume JavaScript. The compiler can target all ECMAScript versions 5 and above, transpiling modern features like classes and arrow functions to their older counterparts.

With TypeScript, it is possible to use existing JavaScript code, incorporate popular JavaScript libraries, and call TypeScript-generated code from other JavaScript. Type declarations for these libraries are usually provided with the source code but can be declared or installed separately if needed.

## Development tools

### Compiler

The TypeScript compiler, named `tsc`, is written in TypeScript. As a result, it can be compiled into regular JavaScript and can then be executed in any JavaScript engine (e.g. a browser). The compiler package comes bundled with a script host that can execute the compiler. It is also available as a Node.js package that uses Node.js as a host. The compiler is currently being rewritten in Go for version 7.

The compiler can *target* a given edition of ECMAScript (such as ECMAScript 5 for legacy browser compatibility), but by default compiles for the latest standards.

### IDE and editor support

- Microsoft provides a plug-in for Visual Studio 2012 and WebMatrix, full integrated support in Visual Studio 2013, Visual Studio 2015, and basic text editor support for Emacs and Vim.
- Visual Studio Code supports TypeScript in addition to several other languages, and offers features like debugging and intelligent code completion.
- alm.tools is an open source cloud IDE for TypeScript built using TypeScript, ReactJS and TypeStyle.
- JetBrains supports TypeScript with code completion, refactoring and debugging in its IDEs built on IntelliJ platform, such as PhpStorm 6, WebStorm 6, and IntelliJ IDEA, as well as their Visual Studio Add-in and extension, ReSharper 8.1.
- Atom has a TypeScript plugin with support for code completion, navigation, formatting, and fast compilation.
- The online Cloud9 IDE and Codenvy support TypeScript.
- A plugin is available for the NetBeans IDE.
- A plugin is available for the Eclipse IDE (version Kepler)
- TypEcs is available for the Eclipse IDE.
- The Cross Platform Cloud IDE Codeanywhere supports TypeScript.
- Webclipse An Eclipse plugin designed to develop TypeScript and Angular 2.
- Angular IDE A standalone IDE available via npm to develop TypeScript and Angular 2 applications, with integrated terminal support.
- Tide – TypeScript Interactive Development Environment for Emacs.

### Integration with build automation tools

Using plug-ins, TypeScript can be integrated with build automation tools, including Grunt (grunt-ts), Apache Maven (TypeScript Maven Plugin), Gulp (gulp-typescript) and Gradle (TypeScript Gradle Plugin).

### Linting tools

TSLint scans TypeScript code for conformance to a set of standards and guidelines. ESLint, a standard JavaScript linter, also provided some support for TypeScript via community plugins. However, ESLint's inability to leverage TypeScript's language services precluded certain forms of semantic linting and program-wide analysis. In early 2019, the TSLint team announced the linter's deprecation in favor of `typescript-eslint`, a joint effort of the TSLint, ESLint and TypeScript teams to consolidate linting under the ESLint umbrella for improved performance, community unity and developer accessibility.

## Release history

Legend:

Unsupported

Supported

Latest version

Preview version

Future version

| Version number | Release date | Significant changes |
|---|---|---|
| Unsupported: 0.8 | 1 October 2012 (2012-10-01) |   |
| Unsupported: 0.9 | 18 June 2013 (2013-06-18) |   |
| Unsupported: 1.0 | 12 April 2014 (2014-04-12) |   |
| Unsupported: 1.1 | 6 October 2014 (2014-10-06) | performance improvements |
| Unsupported: 1.3 | 12 November 2014 (2014-11-12) | `protected` modifier, tuple types |
| Unsupported: 1.4 | 20 January 2015 (2015-01-20) | union types, `let` and `const` declarations, template strings, type guards, type aliases |
| Unsupported: 1.5 | 20 July 2015 (2015-07-20) | ES6 modules, `namespace` keyword, `for..of` support, decorators |
| Unsupported: 1.6 | 16 September 2015 (2015-09-16) | JSX support, intersection types, local type declarations, abstract classes and methods, user-defined type guard functions |
| Unsupported: 1.7 | 30 November 2015 (2015-11-30) | `async` and `await` support, |
| Unsupported: 1.8 | 22 February 2016 (2016-02-22) | constraints generics, control flow analysis errors, string literal types, `allowJs` |
| Unsupported: 2.0 | 22 September 2016 (2016-09-22) | null- and undefined-aware types, control flow based type analysis, discriminated union types, `never` type, `readonly` keyword, type of `this` for functions |
| Unsupported: 2.1 | 8 November 2016 (2016-11-08) | `keyof` and lookup types, mapped types, object spread and rest, |
| Unsupported: 2.2 | 22 February 2017 (2017-02-22) | mix-in classes, `object` type, |
| Unsupported: 2.3 | 27 April 2017 (2017-04-27) | `async` iteration, generic parameter defaults, strict option |
| Unsupported: 2.4 | 27 June 2017 (2017-06-27) | dynamic import expressions, string enums, improved inference for generics, strict contravariance for callback parameters |
| Unsupported: 2.5 | 31 August 2017 (2017-08-31) | optional catch clause variables |
| Unsupported: 2.6 | 31 October 2017 (2017-10-31) | strict function types |
| Unsupported: 2.7 | 31 January 2018 (2018-01-31) | constant-named properties, fixed-length tuples |
| Unsupported: 2.8 | 27 March 2018 (2018-03-27) | conditional types, improved `keyof` with intersection types |
| Unsupported: 2.9 | 14 May 2018 (2018-05-14) | support for symbols and numeric literals in `keyof` and mapped object types |
| Unsupported: 3.0 | 30 July 2018 (2018-07-30) | project references, extracting and spreading parameter lists with tuples |
| Unsupported: 3.1 | 27 September 2018 (2018-09-27) | mappable tuple and array types |
| Unsupported: 3.2 | 30 November 2018 (2018-11-30) | stricter checking for `bind`, `call`, and `apply` |
| Unsupported: 3.3 | 31 January 2019 (2019-01-31) | relaxed rules on methods of union types, incremental builds for composite projects |
| Unsupported: 3.4 | 29 March 2019 (2019-03-29) | faster incremental builds, type inference from generic functions, `readonly` modifier for arrays, `const` assertions, type-checking global `this` |
| Unsupported: 3.5 | 29 May 2019 (2019-05-29) | faster incremental builds, omit helper type, improved excess property checks in union types, smarter union type checking |
| Unsupported: 3.6 | 28 August 2019 (2019-08-28) | Stricter generators, more accurate array spread, better Unicode support for identifiers |
| Unsupported: 3.7 | 5 November 2019 (2019-11-05) | Optional chaining, nullish coalescing |
| Unsupported: 3.8 | 20 February 2020 (2020-02-20) | Type-only imports and exports, ECMAScript private fields, top-level `await` |
| Unsupported: 3.9 | 12 May 2020 (2020-05-12) | Improvements in inference, speed improvements |
| Unsupported: 4.0 | 20 August 2020 (2020-08-20) | Variadic tuple types, labeled tuple elements |
| Unsupported: 4.1 | 19 November 2020 (2020-11-19) | Template literal types, key remapping in mapped types, recursive conditional types |
| Unsupported: 4.2 | 25 February 2021 (2021-02-25) | Smarter type alias preservation, leading/middle rest elements in tuple types, stricter checks for the `in` operator, `abstract` construct signatures |
| Unsupported: 4.3 | 26 May 2021 (2021-05-26) | Separate write types on properties, `override` and the `--noImplicitOverride` flag, template string type improvements |
| Unsupported: 4.4 | 26 August 2021 (2021-08-26) | Control flow analysis of aliased conditions and discriminants, symbol and template string pattern index signatures |
| Unsupported: 4.5 | 17 November 2021 (2021-11-17) | Type and promise improvements, supporting lib from `node_modules`, template string types as discriminants, and `es2022` module |
| Unsupported: 4.6 | 28 February 2022 (2022-02-28) | Type inference and checks improvements, support for ES2022 target, better ECMAScript handling |
| Unsupported: 4.7 | 24 May 2022 (2022-05-24) | Support for ES modules, instantiation expressions, variance annotations for type parameters, better control-flow checks and type check improvements |
| Unsupported: 4.8 | 25 August 2022 (2022-08-25) | Intersection and union types improvements, better type inference |
| Unsupported: 4.9 | 15 November 2022 (2022-11-15) | `satisfies` operator, auto-accessors in classes (proposal), improvements in type narrowing and checks |
| Unsupported: 5.0 | 16 March 2023 (2023-03-16) | ES decorators (proposal), type inference improvements, `bundler` module resolution mode, speed and size optimizations |
| Unsupported: 5.1 | 1 June 2023 (2023-06-01) | Easier implicit returns for `undefined` and unrelated types for getters and setters |
| Unsupported: 5.2 | 24 August 2023 (2023-08-24) | `using` declarations and explicit resource management, decorator metadata and named and anonymous tuple elements |
| Unsupported: 5.3 | 20 November 2023 (2023-11-20) | Improved type narrowing, correctness checks and performance optimizations |
| Unsupported: 5.4 | 6 March 2024 | `Object.groupBy` and `Map.groupBy` support |
| Unsupported: 5.5 | 20 June 2024 | Inferred Type Predicates, Regular Expression Syntax Checking, and Type Imports in JSDoc |
| Unsupported: 5.6 | 9 September 2024 | Advanced type inference, variadic tuple enhancements, partial module declarations. |
| Unsupported: 5.7 | 22 November 2024 |   |
| Unsupported: 5.8 | 28 February 2025 |   |
| Unsupported: 5.9 | 31 July 2025 |   |
| Latest version: 6.0 | 23 March 2026 | Introduce some deprecations and breaking changes to align with the upcoming native codebase. Strict mode is now enabled by default. Last version with compiler and language service based on JavaScript before rewrite to Go language. |
| Preview version: 7.0 |   | Rewrite in Go with faster performance. |
