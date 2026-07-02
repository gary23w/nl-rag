---
title: "PureScript"
source: https://www.purescript.org/
domain: purescript
license: CC-BY-SA-4.0
tags: purescript, pure script language, purescript lang
fetched: 2026-07-02
---

## A strongly-typed functional programming language that compiles to JavaScript

### Benefits

- Compile to readable JavaScript and reuse existing JavaScript code easily
- An extensive collection of libraries for development of web applications, web servers, apps and more
- Excellent tooling and editor support with instant rebuilds
- An active community with many learning resources
- Build real-world applications using functional techniques and expressive types, such as:
  - Algebraic data types and pattern matching
  - Row polymorphism and extensible records
  - Higher kinded types
  - Type classes with functional dependencies
  - Higher-rank polymorphism

### Hello, PureScript!

```
import Prelude
import Effect.Console (log)

greet :: String -> String
greet name = "Hello, " <> name <> "!"

main = log (greet "World")
```

Quick Start Guide

Try PureScript

## Get the compiler

### Binaries

Precompiled binaries are available for OSX, Linux, and Windows from the latest release page on GitHub.

### npm

`npm install -g purescript`

(Installation via `npm` requires Node version 8 or later)

### Tools

The recommended build tool for PureScript is Spago, which can be installed using `npm`:

`npm install -g spago`

You might like to install some of these additional tools and editor plugins.

NPM is recommended for managing JavaScript dependencies in your project.

## Learn more

### Libraries

The Pursuit package database hosts searchable documentation for PureScript packages.

### Documentation

The free PureScript By Example book contains several practical projects for PureScript beginners.

Visit the documentation repository on GitHub, the central place where you can find articles, in-depth learning resources for beginners, and more.

### Community

There are several places in which people gather to discuss PureScript:

- **Discourse** - The PureScript Discourse instance.
- **Discord** - The PureScript Discord server.
