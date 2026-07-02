---
title: "GitHub"
source: https://github.com/motdotla/dotenv
domain: dotenv-config
license: CC-BY-SA-4.0
tags: dotenv config, environment variable loading, dotenv file, twelve-factor config
fetched: 2026-07-02
---

# GitHub

motdotla

/

dotenv

Public

- Uh oh! There was an error while loading. Please reload this page.
- Notifications You must be signed in to change notification settings
- Fork 946
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History999 Commits999 Commits |   |   |   |
| .github | .github |   |   |
| lib | lib |   |   |
| skills | skills |   |   |
| tests | tests |   |   |
| .editorconfig | .editorconfig |   |   |
| .gitignore | .gitignore |   |   |
| .npmignore | .npmignore |   |   |
| .npmrc | .npmrc |   |   |
| CHANGELOG.md | CHANGELOG.md |   |   |
| CONTRIBUTING.md | CONTRIBUTING.md |   |   |
| LICENSE | LICENSE |   |   |
| README-es.md | README-es.md |   |   |
| README.md | README.md |   |   |
| SECURITY.md | SECURITY.md |   |   |
| config.d.ts | config.d.ts |   |   |
| config.js | config.js |   |   |
| dotenv.png | dotenv.png |   |   |
| dotenv.svg | dotenv.svg |   |   |
| package-lock.json | package-lock.json |   |   |
| package.json | package.json |   |   |
|   |   |   |   |

## Repository files navigation

(dotenvx)

# dotenv (NPM version) (downloads)

(dotenv)

Dotenv is a zero-dependency module that loads environment variables from a `.env` file into `process.env`. Storing configuration in the environment separate from code is based on The Twelve-Factor App methodology.

Watch the tutorial

## Usage

Install it.

```highlight
npm install dotenv --save
```

Create a `.env` file in the root of your project:

```highlight
# .env
HELLO="Dotenv"
OPENAI_API_KEY="your-api-key-goes-here"
```

As early as possible in your application, import and configure dotenv:

```highlight
// index.js
require('dotenv').config()
// or import 'dotenv/config' // for esm

console.log(`Hello ${process.env.HELLO}`)
```

```highlight
$ node index.js
◇ injected env (2) from .env
Hello Dotenv
```

That's it. `process.env` now has the keys and values you defined in your `.env` file.

## Agent Usage

Install this repo as an agent skill package:

```highlight
npx skills add motdotla/dotenv
```

```highlight
# ask Claude or Codex to do things like:
set up dotenv
upgrade dotenv to dotenvx
```

## Advanced

ES6

Import with ES6:

```highlight
import 'dotenv/config'
```

ES6 import if you need to set config options:

```highlight
import dotenv from 'dotenv'
dotenv.config({ path: '/custom/path/to/.env' })
```

bun

```highlight
bun add dotenv
```

yarn

```highlight
yarn add dotenv
```

pnpm

```highlight
pnpm add dotenv
```

Monorepos

For monorepos with a structure like `apps/backend/app.js`, put it the `.env` file in the root of the folder where your `app.js` process runs.

```highlight
# app/backend/.env
S3_BUCKET="YOURS3BUCKET"
SECRET_KEY="YOURSECRETKEYGOESHERE"
```

Multiline Values

If you need multiline variables, for example private keys, those are now supported (`>= v15.0.0`) with line breaks:

```highlight
PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----
...
Kh9NV...
...
-----END RSA PRIVATE KEY-----"
```

Alternatively, you can double quote strings and use the `\n` character:

```highlight
PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----\nKh9NV...\n-----END RSA PRIVATE KEY-----\n"
```

Comments

Comments may be added to your file on their own line or inline:

```highlight
# This is a comment
SECRET_KEY=YOURSECRETKEYGOESHERE # comment
SECRET_HASH="something-with-a-#-hash"
```

Comments begin where a `#` exists, so if your value contains a `#` please wrap it in quotes. This is a breaking change from `>= v15.0.0` and on.

Parsing

The engine which parses the contents of your file containing environment variables is available to use. It accepts a String or Buffer and will return an Object with the parsed keys and values.

```highlight
const dotenv = require('dotenv')
const buf = Buffer.from('BASIC=basic')
const config = dotenv.parse(buf) // will return an object
console.log(typeof config, config) // object { BASIC : 'basic' }
```

Preload

> Note: Consider using `dotenvx` instead of preloading. I am now doing (and recommending) so.
> 
> It serves the same purpose (you do not need to require and load dotenv), adds better debugging, and works with ANY language, framework, or platform. – motdotla

You can use the `--require` (`-r`) command line option to preload dotenv. By doing this, you do not need to require and load dotenv in your application code.

```highlight
$ node -r dotenv/config your_script.js
```

The configuration options below are supported as command line arguments in the format `dotenv_config_<option>=value`

```highlight
$ node -r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env dotenv_config_debug=true
```

Additionally, you can use environment variables to set configuration options. Command line arguments will precede these.

```highlight
$ DOTENV_CONFIG_<OPTION>=value node -r dotenv/config your_script.js
```

```highlight
$ DOTENV_CONFIG_ENCODING=latin1 DOTENV_CONFIG_DEBUG=true node -r dotenv/config your_script.js dotenv_config_path=/custom/path/to/.env
```

Variable Expansion

Use dotenvx for variable expansion.

Reference and expand variables already on your machine for use in your .env file.

```highlight
# .env
USERNAME="username"
DATABASE_URL="postgres://${USERNAME}@localhost/my_database"
```

```highlight
// index.js
console.log('DATABASE_URL', process.env.DATABASE_URL)
```

```highlight
$ dotenvx run --debug -- node index.js
⟐ injected env (2) from .env · dotenvx@1.59.1
DATABASE_URL postgres://username@localhost/my_database
```

Command Substitution

Use dotenvx for command substitution.

Add the output of a command to one of your variables in your .env file.

```highlight
# .env
DATABASE_URL="postgres://$(whoami)@localhost/my_database"
```

```highlight
// index.js
console.log('DATABASE_URL', process.env.DATABASE_URL)
```

```highlight
$ dotenvx run --debug -- node index.js
⟐ injected env (1) from .env · dotenvx@1.59.1
DATABASE_URL postgres://yourusername@localhost/my_database
```

Encryption

Use dotenvx for encryption.

Add encryption to your `.env` files with a single command.

```
$ dotenvx set HELLO Production -f .env.production
$ echo "console.log('Hello ' + process.env.HELLO)" > index.js

$ DOTENV_PRIVATE_KEY_PRODUCTION="<.env.production private key>" dotenvx run -- node index.js
⟐ injected env (2) from .env.production · dotenvx@1.59.1
Hello Production
```

learn more

Multiple Environments

Use dotenvx to manage multiple environments.

Run any environment locally. Create a `.env.ENVIRONMENT` file and use `-f` to load it. It's straightforward, yet flexible.

```highlight
$ echo "HELLO=production" > .env.production
$ echo "console.log('Hello ' + process.env.HELLO)" > index.js

$ dotenvx run -f=.env.production -- node index.js
Hello production
> ^^
```

or with multiple .env files

```highlight
$ echo "HELLO=local" > .env.local
$ echo "HELLO=World" > .env
$ echo "console.log('Hello ' + process.env.HELLO)" > index.js

$ dotenvx run -f=.env.local -f=.env -- node index.js
Hello local
```

more environment examples

Production

Use dotenvx for production deploys.

Create a `.env.production` file.

```highlight
$ echo "HELLO=production" > .env.production
```

Encrypt it.

```highlight
$ dotenvx encrypt -f .env.production
```

Set `DOTENV_PRIVATE_KEY_PRODUCTION` (found in `.env.keys`) on your server.

```
$ heroku config:set DOTENV_PRIVATE_KEY_PRODUCTION=value
```

Commit your `.env.production` file to code and deploy.

```
$ git add .env.production
$ git commit -m "encrypted .env.production"
$ git push heroku main
```

Dotenvx will decrypt and inject the secrets at runtime using `dotenvx run -- node index.js`.

Syncing

Use dotenvx to sync your .env files.

Encrypt them with `dotenvx encrypt -f .env` and safely include them in source control. Your secrets are securely synced with your git.

This still subscribes to the twelve-factor app rules by generating a decryption key separate from code.

More Examples

See examples of using dotenv with various frameworks, languages, and configurations.

- nodejs
- nodejs (debug on)
- nodejs (override on)
- nodejs (processEnv override)
- esm
- esm (preload)
- typescript
- typescript parse
- typescript config
- webpack
- webpack (plugin)
- react
- react (typescript)
- express
- nestjs
- fastify

## FAQ

Should I commit my `.env` file?

No.

Unless you encrypt it with dotenvx. Then we recommend you do.

What about variable expansion?

Use dotenvx.

Should I have multiple `.env` files?

We recommend creating one `.env` file per environment. Use `.env` for local/development, `.env.production` for production and so on. This still follows the twelve factor principles as each is attributed individually to its own environment. Avoid custom set ups that work in inheritance somehow (`.env.production` inherits values from `.env` for example). It is better to duplicate values if necessary across each `.env.environment` file.

> In a twelve-factor app, env vars are granular controls, each fully orthogonal to other env vars. They are never grouped together as “environments”, but instead are independently managed for each deploy. This is a model that scales up smoothly as the app naturally expands into more deploys over its lifetime.
> 
> – The Twelve-Factor App

Additionally, we recommend using dotenvx to encrypt and manage these.

How do I use dotenv with `import`?

Simply..

```highlight
// index.mjs (ESM)
import 'dotenv/config' // see https://github.com/motdotla/dotenv#how-do-i-use-dotenv-with-import
import express from 'express'
```

A little background..

> When you run a module containing an `import` declaration, the modules it imports are loaded first, then each module body is executed in a depth-first traversal of the dependency graph, avoiding cycles by skipping anything already executed.
> 
> – ES6 In Depth: Modules

What does this mean in plain language? It means you would think the following would work but it won't.

`errorReporter.mjs`:

```highlight
class Client {
  constructor (apiKey) {
    console.log('apiKey', apiKey)

    this.apiKey = apiKey
  }
}

export default new Client(process.env.API_KEY)
```

`index.mjs`:

```highlight
// Note: this is INCORRECT and will not work
import * as dotenv from 'dotenv'
dotenv.config()

import errorReporter from './errorReporter.mjs' // process.env.API_KEY will be blank!
```

`process.env.API_KEY` will be blank.

Instead, `index.mjs` should be written as..

```highlight
import 'dotenv/config'

import errorReporter from './errorReporter.mjs'
```

Does that make sense? It's a bit unintuitive, but it is how importing of ES6 modules work. Here is a working example of this pitfall.

There are two alternatives to this approach:

1. Preload with dotenvx: `dotenvx run -- node index.js` (*Note: you do not need to `import` dotenv with this approach*)
2. Create a separate file that will execute `config` first as outlined in this comment on #133

Can I customize/write plugins for dotenv?

Yes! `dotenv.config()` returns an object representing the parsed `.env` file. This gives you everything you need to continue setting values on `process.env`. For example:

```highlight
const dotenv = require('dotenv')
const variableExpansion = require('dotenv-expand')
const myEnv = dotenv.config()
variableExpansion(myEnv)
```

What rules does the parsing engine follow?

The parsing engine currently supports the following rules:

- `BASIC=basic` becomes `{BASIC: 'basic'}`
- empty lines are skipped
- lines beginning with `#` are treated as comments
- `#` marks the beginning of a comment (unless when the value is wrapped in quotes)
- empty values become empty strings (`EMPTY=` becomes `{EMPTY: ''}`)
- inner quotes are maintained (think JSON) (`JSON={"foo": "bar"}` becomes `{JSON:"{\"foo\": \"bar\"}"`)
- whitespace is removed from both ends of unquoted values (see more on `trim`) (`FOO= some value` becomes `{FOO: 'some value'}`)
- single and double quoted values are escaped (`SINGLE_QUOTE='quoted'` becomes `{SINGLE_QUOTE: "quoted"}`)
- single and double quoted values maintain whitespace from both ends (`FOO=" some value "` becomes `{FOO: ' some value '}`)
- double quoted values expand new lines (`MULTILINE="new\nline"` becomes

```
{MULTILINE: 'new
line'}
```

- backticks are supported (BACKTICK_KEY=`This has 'single' and "double" quotes inside of it.`)

What about syncing and securing .env files?

Use dotenvx to unlock syncing encrypted .env files over git.

How do I specify config options with ES6 import?

When using `import 'dotenv/config'`, you can't pass options directly. Here are a few ways to handle it.

**Option 1: Import and call `config()` yourself (Recommended)**

```highlight
// index.mjs
import dotenv from 'dotenv'

dotenv.config({
  path: '/custom/path/to/.env',
  debug: true
})

// Now import everything else
import express from 'express'
```

Because ES6 imports are hoisted, put the `dotenv` import and `config()` call at the very top, before any other imports that rely on `process.env`.

**Option 2: Use environment variables**

```highlight
DOTENV_CONFIG_DEBUG=true DOTENV_CONFIG_PATH=/custom/path/to/.env node index.mjs
```

Then in your code you can keep the shorthand:

```highlight
import 'dotenv/config'
```

**Option 3: A tiny wrapper file**

Create `load-env.mjs`:

```highlight
import dotenv from 'dotenv'
dotenv.config({ path: '/custom/path/to/.env', debug: true })
```

Then in your main file:

```highlight
import './load-env.mjs'
import express from 'express'
```

Not the most elegant, but it works reliably when hoisting gets in the way.

What if I accidentally commit my `.env` file to code?

Remove it, remove git history and then install the git pre-commit hook to prevent this from ever happening again.

```
npm i -g @dotenvx/dotenvx
dotenvx precommit --install
```

What happens to environment variables that were already set?

By default, we will never modify any environment variables that have already been set. In particular, if there is a variable in your `.env` file which collides with one that already exists in your environment, then that variable will be skipped.

If instead, you want to override `process.env` use the `override` option.

```highlight
require('dotenv').config({ override: true })
```

How can I prevent committing my `.env` file to a Docker build?

Use the docker prebuild hook.

```highlight
# Dockerfile
...
RUN curl -fsS https://dotenvx.sh/ | sh
...
RUN dotenvx prebuild
CMD ["dotenvx", "run", "--", "node", "index.js"]
```

How come my environment variables are not showing up for React?

Your React code is run in Webpack, where the `fs` module or even the `process` global itself are not accessible out-of-the-box. `process.env` can only be injected through Webpack configuration.

If you are using `react-scripts`, which is distributed through `create-react-app`, it has dotenv built in but with a quirk. Preface your environment variables with `REACT_APP_`. See this stack overflow for more details.

If you are using other frameworks (e.g. Next.js, Gatsby...), you need to consult their documentation for how to inject environment variables into the client.

Why is the `.env` file not loading my environment variables successfully?

Most likely your `.env` file is not in the correct place. See this stack overflow.

Turn on debug mode and try again..

```highlight
require('dotenv').config({ debug: true })
```

You will receive a helpful error outputted to your console.

Why am I getting the error `Module not found: Error: Can't resolve 'crypto|os|path'`?

You are using dotenv on the front-end and have not included a polyfill. Webpack < 5 used to include these for you. Do the following:

```highlight
npm install node-polyfill-webpack-plugin
```

Configure your `webpack.config.js` to something like the following.

```highlight
require('dotenv').config()

const path = require('path');
const webpack = require('webpack')

const NodePolyfillPlugin = require('node-polyfill-webpack-plugin')

module.exports = {
  mode: 'development',
  entry: './src/index.ts',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
  plugins: [
    new NodePolyfillPlugin(),
    new webpack.DefinePlugin({
      'process.env': {
        HELLO: JSON.stringify(process.env.HELLO)
      }
    }),
  ]
};
```

Alternatively, just use dotenv-webpack which does this and more behind the scenes for you.

## Docs

Dotenv exposes four functions:

- `config`
- `parse`
- `populate`

### Config

`config` will read your `.env` file, parse the contents, assign it to `process.env`, and return an Object with a `parsed` key containing the loaded content or an `error` key if it failed.

```highlight
const result = dotenv.config()

if (result.error) {
  throw result.error
}

console.log(result.parsed)
```

You can additionally, pass options to `config`.

#### Options

##### path

Default: `path.resolve(process.cwd(), '.env')`

Specify a custom path if your file containing environment variables is located elsewhere.

```highlight
require('dotenv').config({ path: '/custom/path/to/.env' })
```

By default, `config` will look for a file called .env in the current working directory.

Pass in multiple files as an array, and they will be parsed in order and combined with `process.env` (or `option.processEnv`, if set). The first value set for a variable will win, unless the `options.override` flag is set, in which case the last value set will win. If a value already exists in `process.env` and the `options.override` flag is NOT set, no changes will be made to that value.

```highlight
require('dotenv').config({ path: ['.env.local', '.env'] })
```

##### quiet

Default: `false`

Suppress runtime logging message.

```highlight
// index.js
require('dotenv').config({ quiet: false }) // change to true to suppress
console.log(`Hello ${process.env.HELLO}`)
```

```highlight
# .env
HELLO=World
```

```highlight
$ node index.js
Hello World
```

##### encoding

Default: `utf8`

Specify the encoding of your file containing environment variables.

```highlight
require('dotenv').config({ encoding: 'latin1' })
```

##### debug

Default: `false`

Turn on logging to help debug why certain keys or values are not being set as you expect.

```highlight
require('dotenv').config({ debug: process.env.DEBUG })
```

##### override

Default: `false`

Override any environment variables that have already been set on your machine with values from your .env file(s). If multiple files have been provided in `option.path` the override will also be used as each file is combined with the next. Without `override` being set, the first value wins. With `override` set the last value wins.

```highlight
require('dotenv').config({ override: true })
```

##### processEnv

Default: `process.env`

Specify an object to write your environment variables to. Defaults to `process.env` environment variables.

```highlight
const myObject = {}
require('dotenv').config({ processEnv: myObject })

console.log(myObject) // values from .env
console.log(process.env) // this was not changed or written to
```

### Parse

The engine which parses the contents of your file containing environment variables is available to use. It accepts a String or Buffer and will return an Object with the parsed keys and values.

```highlight
const dotenv = require('dotenv')
const buf = Buffer.from('BASIC=basic')
const config = dotenv.parse(buf) // will return an object
console.log(typeof config, config) // object { BASIC : 'basic' }
```

#### Options

##### debug

Default: `false`

Turn on logging to help debug why certain keys or values are not being set as you expect.

```highlight
const dotenv = require('dotenv')
const buf = Buffer.from('hello world')
const opt = { debug: true }
const config = dotenv.parse(buf, opt)
// expect a debug message because the buffer is not in KEY=VAL form
```

### Populate

The engine which populates the contents of your .env file to `process.env` is available for use. It accepts a target, a source, and options. This is useful for power users who want to supply their own objects.

For example, customizing the source:

```highlight
const dotenv = require('dotenv')
const parsed = { HELLO: 'world' }

dotenv.populate(process.env, parsed)

console.log(process.env.HELLO) // world
```

For example, customizing the source AND target:

```highlight
const dotenv = require('dotenv')
const parsed = { HELLO: 'universe' }
const target = { HELLO: 'world' } // empty object

dotenv.populate(target, parsed, { override: true, debug: true })

console.log(target) // { HELLO: 'universe' }
```

#### options

##### Debug

Default: `false`

Turn on logging to help debug why certain keys or values are not being populated as you expect.

##### override

Default: `false`

Override any environment variables that have already been set.

## CHANGELOG

See CHANGELOG.md

## Who's using dotenv?

These npm modules depend on it.

Projects that expand it often use the keyword "dotenv" on npm.
