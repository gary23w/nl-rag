---
title: "GitHub"
source: https://github.com/pinojs/pino
domain: pino-logging
license: CC-BY-SA-4.0
tags: pino logging, fast json logger, low overhead logging, node structured logs
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

pinojs

/

pino

Public

- Notifications You must be signed in to change notification settings
- Fork 973
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History1,986 Commits1,986 Commits |   |   |   |
| .github | .github |   |   |
| benchmarks | benchmarks |   |   |
| build | build |   |   |
| docs | docs |   |   |
| docsify | docsify |   |   |
| examples | examples |   |   |
| lib | lib |   |   |
| test | test |   |   |
| .gitignore | .gitignore |   |   |
| .nojekyll | .nojekyll |   |   |
| .npmignore | .npmignore |   |   |
| .npmrc | .npmrc |   |   |
| .prettierignore | .prettierignore |   |   |
| CNAME | CNAME |   |   |
| CONTRIBUTING.md | CONTRIBUTING.md |   |   |
| LICENSE | LICENSE |   |   |
| README.md | README.md |   |   |
| SECURITY.md | SECURITY.md |   |   |
| bin.js | bin.js |   |   |
| browser.js | browser.js |   |   |
| eslint.config.js | eslint.config.js |   |   |
| favicon-16x16.png | favicon-16x16.png |   |   |
| favicon-32x32.png | favicon-32x32.png |   |   |
| favicon.ico | favicon.ico |   |   |
| file.js | file.js |   |   |
| inc-version.sh | inc-version.sh |   |   |
| index.html | index.html |   |   |
| package.json | package.json |   |   |
| pino-banner.png | pino-banner.png |   |   |
| pino-logo-hire.png | pino-logo-hire.png |   |   |
| pino-tree.png | pino-tree.png |   |   |
| pino.d.ts | pino.d.ts |   |   |
| pino.js | pino.js |   |   |
| pretty-demo.png | pretty-demo.png |   |   |
| tsconfig.json | tsconfig.json |   |   |
|   |   |   |   |

## Repository files navigation

(banner)

# pino

(npm version) (Build Status) (js-standard-style)

Very low overhead JavaScript logger.

## Documentation

- Benchmarks ⇗
- API ⇗
- Browser API ⇗
- Redaction ⇗
- Child Loggers ⇗
- Transports ⇗
- Diagnostics ⇗
- Web Frameworks ⇗
- Pretty Printing ⇗
- Asynchronous Logging ⇗
- Ecosystem ⇗
- Help ⇗
- Long Term Support Policy ⇗

## Runtimes

### Node.js

Pino is built to run on Node.js.

### Bare

Pino works on Bare with the `pino-bare` compatibility module.

### Pear

Pino works on Pear, which is built on Bare, with the `pino-bare` compatibility module.

## Install

Using NPM:

```
$ npm install pino
```

Using YARN:

```
$ yarn add pino
```

If you would like to install pino v6, refer to https://github.com/pinojs/pino/tree/v6.x.

## Usage

```highlight
const logger = require('pino')()

logger.info('hello world')

const child = logger.child({ a: 'property' })
child.info('hello child!')
```

This produces:

```
{"level":30,"time":1531171074631,"msg":"hello world","pid":657,"hostname":"Davids-MBP-3.fritz.box"}
{"level":30,"time":1531171082399,"msg":"hello child!","pid":657,"hostname":"Davids-MBP-3.fritz.box","a":"property"}
```

For using Pino with a web framework see:

- Pino with Fastify
- Pino with Express
- Pino with Hapi
- Pino with Restify
- Pino with Koa
- Pino with Node core `http`
- Pino with Nest
- Pino with Hono

## Essentials

### Development Formatting

The `pino-pretty` module can be used to format logs during development:

(pretty demo)

### Transports & Log Processing

Due to Node's single-threaded event-loop, it's highly recommended that sending, alert triggering, reformatting, and all forms of log processing are conducted in a separate process or thread.

In Pino terminology, we call all log processors "transports" and recommend that the transports be run in a worker thread using our `pino.transport` API.

For more details see our Transports⇗ document.

### Low overhead

Using minimum resources for logging is very important. Log messages tend to get added over time and this can lead to a throttling effect on applications – such as reduced requests per second.

In many cases, Pino is over 5x faster than alternatives.

See the Benchmarks document for comparisons.

### Bundling support

Pino supports being bundled using tools like webpack or esbuild.

See Bundling document for more information.

## The Team

### Matteo Collina

https://github.com/mcollina

https://www.npmjs.com/~matteo.collina

https://twitter.com/matteocollina

### David Mark Clements

https://github.com/davidmarkclements

https://www.npmjs.com/~davidmarkclements

https://twitter.com/davidmarkclem

### James Sumners

https://github.com/jsumners

https://www.npmjs.com/~jsumners

https://twitter.com/jsumners79

### Thomas Watson Steen

https://github.com/watson

https://www.npmjs.com/~watson

https://twitter.com/wa7son

## Contributing

Pino is an **OPEN Open Source Project**. This means that:

> Individuals making significant and valuable contributions are given commit-access to the project to contribute as they see fit. This project is more like an open wiki than a standard guarded open source project.

See the CONTRIBUTING.md file for more details.

## Acknowledgments

This project was kindly sponsored by nearForm. This project is kindly sponsored by Platformatic.

Logo and identity designed by Cosmic Fox Design: https://www.behance.net/cosmicfox.

## License

Licensed under MIT.
