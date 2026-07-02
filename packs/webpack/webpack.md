---
title: "Webpack"
source: https://en.wikipedia.org/wiki/Webpack
domain: webpack
license: CC-BY-SA-4.0
tags: webpack bundler, webpack loader, webpack bundle, module bundler config
fetched: 2026-07-02
---

# Webpack

**webpack** is a free and open-source module bundler for JavaScript. It is made primarily for JavaScript, but it can transform front-end assets such as HTML, CSS, and images if the corresponding loaders are included. webpack takes modules with dependencies and generates static assets representing those modules.

webpack takes the dependencies and generates a dependency graph allowing web developers to use a modular approach for their web application development purposes. It can be used from the command line or can be configured using a configuration file which is named *webpack.config.js*. This file defines rules, plugins, etc., for a project. (webpack is highly extensible via rules which allow developers to write custom tasks that they want to perform when bundling files together.)

Node.js is required to use webpack.

webpack provides code on demand using the moniker *code splitting*. Two similar techniques are supported by webpack when it comes to dynamic code splitting. The first and recommended approach is to use the *import()* syntax that conforms to the ECMAScript proposal for dynamic imports. The legacy, webpack-specific approach is to use *require.ensure*.

## webpack development server

webpack also provides a built-in development server, *webpack-dev-server*, that can be used as an HTTP server for serving files while developing. It also provides the capability to use hot module replacement (HMR), which updates code on a webpage without requiring the developer to reload the page.
