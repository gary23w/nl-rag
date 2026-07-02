---
title: "GitHub"
source: https://github.com/lodash/lodash
domain: lodash-utils
license: CC-BY-SA-4.0
tags: lodash utility, javascript utility library, functional helpers, collection iteration
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

lodash

/

lodash

Public

- Notifications You must be signed in to change notification settings
- Fork 7.2k
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History7,707 Commits7,707 Commits |   |   |   |
| .github | .github |   |   |
| dist | dist |   |   |
| doc | doc |   |   |
| fp | fp |   |   |
| lib | lib |   |   |
| perf | perf |   |   |
| test | test |   |   |
| vendor | vendor |   |   |
| .editorconfig | .editorconfig |   |   |
| .gitattributes | .gitattributes |   |   |
| .gitignore | .gitignore |   |   |
| .jscsrc | .jscsrc |   |   |
| .markdown-doctest-setup.js | .markdown-doctest-setup.js |   |   |
| CHANGELOG | CHANGELOG |   |   |
| GOVERNANCE.md | GOVERNANCE.md |   |   |
| LICENSE | LICENSE |   |   |
| README.md | README.md |   |   |
| SECURITY.md | SECURITY.md |   |   |
| incident_response_plan.md | incident_response_plan.md |   |   |
| lodash.js | lodash.js |   |   |
| package-lock.json | package-lock.json |   |   |
| package.json | package.json |   |   |
| playwright.config.js | playwright.config.js |   |   |
| renovate.json | renovate.json |   |   |
| threat-model.md | threat-model.md |   |   |
|   |   |   |   |

## Repository files navigation

# lodash v4.18.1

Site | Docs | FP Guide | Contributing | Wiki | Code of Conduct | Governance | Twitter | Chat

Important

As announced on the OpenJS Foundation blog, Lodash has received support from the Sovereign Tech Agency and will transition to the Feature-Complete maturity stage so that it remains stable, secure, and sustainable long-term. As part of this effort, Lodash is rebooting its governance. A draft charter will be published shortly. The upcoming Technical Steering Committee (TSC) is already at work. For transparency, its members are listed in GOVERNANCE.md.

The Lodash library exported as a UMD module.

Generated using lodash-cli:

```highlight
$ npm run build
$ lodash -o ./dist/lodash.js
$ lodash core -o ./dist/lodash.core.js
```

## Download

- Core build (~4 kB gzipped)
- Full build (~24 kB gzipped)
- CDN copies

Lodash is released under the MIT license & supports modern environments. Review the build differences & pick one that’s right for you.

## Installation

In a browser:

```highlight
<script src="lodash.js"></script>
```

Using npm:

```highlight
$ npm i -g npm
$ npm i --save lodash
```

In Node.js:

```highlight
// Load the full build.
var _ = require('lodash');
// Load the core build.
var _ = require('lodash/core');
// Load the FP build for immutable auto-curried iteratee-first data-last methods.
var fp = require('lodash/fp');

// Load method categories.
var array = require('lodash/array');
var object = require('lodash/fp/object');

// Cherry-pick methods for smaller browserify/rollup/webpack bundles.
var at = require('lodash/at');
var curryN = require('lodash/fp/curryN');
```

## Why Lodash?

Lodash makes JavaScript easier by taking the hassle out of working with arrays, numbers, objects, strings, etc. Lodash’s modular methods are great for:

- Iterating arrays, objects, & strings
- Manipulating & testing values
- Creating composite functions

## Module Formats

Lodash is available in a variety of builds & module formats.

- lodash & per method packages
- lodash-es, babel-plugin-lodash, & lodash-webpack-plugin
- lodash/fp
- lodash-amd
