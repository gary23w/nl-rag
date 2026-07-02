---
title: "GitHub"
source: https://github.com/yargs/yargs
domain: yargs-cli
license: CC-BY-SA-4.0
tags: yargs parser, cli option parsing, command builder, argv parsing
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

yargs

/

yargs

Public

- Notifications You must be signed in to change notification settings
- Fork 1k
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History1,859 Commits1,859 Commits |   |   |   |
| .github/workflows | .github/workflows |   |   |
| docs | docs |   |   |
| example | example |   |   |
| helpers | helpers |   |   |
| lib | lib |   |   |
| locales | locales |   |   |
| test | test |   |   |
| .eslintignore | .eslintignore |   |   |
| .eslintrc.json | .eslintrc.json |   |   |
| .gitattributes | .gitattributes |   |   |
| .gitignore | .gitignore |   |   |
| .nycrc | .nycrc |   |   |
| .prettierrc.cjs | .prettierrc.cjs |   |   |
| CHANGELOG.md | CHANGELOG.md |   |   |
| CODE_OF_CONDUCT.md | CODE_OF_CONDUCT.md |   |   |
| LICENSE | LICENSE |   |   |
| README.md | README.md |   |   |
| browser.d.ts | browser.d.ts |   |   |
| browser.mjs | browser.mjs |   |   |
| contributing.md | contributing.md |   |   |
| deno-types.ts | deno-types.ts |   |   |
| deno.ts | deno.ts |   |   |
| index.mjs | index.mjs |   |   |
| package.json | package.json |   |   |
| renovate.json | renovate.json |   |   |
| tsconfig.json | tsconfig.json |   |   |
| tsconfig.test.json | tsconfig.test.json |   |   |
| yargs-logo.png | yargs-logo.png |   |   |
|   |   |   |   |

## Repository files navigation

# Yargs

**Yargs be a node.js library fer hearties tryin' ter parse optstrings**

(ci) (NPM version) (js-standard-style) (Coverage) (Conventional Commits)

## Description

Yargs helps you build interactive command line tools, by parsing arguments and generating an elegant user interface.

It gives you:

- commands and (grouped) options (`my-program.js serve --port=5000`).
- a dynamically generated help menu based on your arguments:

```
mocha [spec..]

Run tests with Mocha

Commands
  mocha inspect [spec..]  Run tests with Mocha                         [default]
  mocha init <path>       create a client-side Mocha setup at <path>

Rules & Behavior
  --allow-uncaught           Allow uncaught errors to propagate        [boolean]
  --async-only, -A           Require all tests to use a callback (async) or
                             return a Promise                          [boolean]
```

- generate completion scripts for Bash and Zsh for your command
- and tons more.

## Installation

Stable version:

```highlight
npm i yargs
```

Bleeding edge version with the most recent features:

```highlight
npm i yargs@next
```

## Usage

### Simple Example

```highlight
#!/usr/bin/env node
import yargs from 'yargs';
import { hideBin } from 'yargs/helpers';
const argv = yargs(hideBin(process.argv)).parse()

if (argv.ships > 3 && argv.distance < 53.5) {
  console.log('Plunder more riffiwobbles!')
} else {
  console.log('Retreat from the xupptumblers!')
}
```

```highlight
$ ./plunder.js --ships=4 --distance=22
Plunder more riffiwobbles!

$ ./plunder.js --ships 12 --distance 98.7
Retreat from the xupptumblers!
```

> Note: `hideBin` is a shorthand for `process.argv.slice(2)`. It has the benefit that it takes into account variations in some environments, e.g., Electron.

### Complex Example

```highlight
#!/usr/bin/env node
import yargs from 'yargs';
import { hideBin } from 'yargs/helpers';

yargs(hideBin(process.argv))
  .command('serve [port]', 'start the server', (yargs) => {
    return yargs
      .positional('port', {
        describe: 'port to bind on',
        default: 5000
      })
  }, (argv) => {
    if (argv.verbose) console.info(`start server on :${argv.port}`)
    serve(argv.port)
  })
  .option('verbose', {
    alias: 'v',
    type: 'boolean',
    description: 'Run with verbose logging'
  })
  .parse()
```

Run the example above with `--help` to see the help for the application.

## Supported Platforms

### TypeScript

yargs has type definitions at @types/yargs.

```
npm i @types/yargs --save-dev
```

See usage examples in docs.

### Deno

As of `v16`, `yargs` supports Deno:

```highlight
import yargs from 'https://deno.land/x/yargs@v17.7.2-deno/deno.ts'
import { Arguments } from 'https://deno.land/x/yargs@v17.7.2-deno/deno-types.ts'

yargs(Deno.args)
  .command('download <files...>', 'download a list of files', (yargs: any) => {
    return yargs.positional('files', {
      describe: 'a list of files to do something with'
    })
  }, (argv: Arguments) => {
    console.info(argv)
  })
  .strictCommands()
  .demandCommand(1)
  .parse()
```

> Note: If you use version tags in url then you also have to add `-deno` flag on the end, like `@17.7.2-deno`

### Usage in Browser

See examples of using yargs in the browser in docs.

## Documentation

### Table of Contents

- Yargs' API
- Examples
- Parsing Tricks
  - Stop the Parser
  - Negating Boolean Arguments
  - Numbers
  - Arrays
  - Objects
  - Quotes
- Advanced Topics
  - Composing Your App Using Commands
  - Building Configurable CLI Apps
  - Customizing Yargs' Parser
- Contributing

## Supported Node.js Versions

Libraries in this ecosystem make a best effort to track Node.js' release schedule. Here's a post on why we think this is important.
