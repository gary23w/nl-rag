---
title: "GitHub"
source: https://github.com/ai/nanoid
domain: nanoid-ids
license: CC-BY-SA-4.0
tags: nanoid generator, compact unique id, url-safe identifier, collision resistant id
fetched: 2026-07-02
---

# GitHub

ai

/

nanoid

Public

- Uh oh! There was an error while loading. Please reload this page.
- Notifications You must be signed in to change notification settings
- Fork 857
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History1,242 Commits1,242 Commits |   |   |   |
| .github | .github |   |   |
| bin | bin |   |   |
| img | img |   |   |
| non-secure | non-secure |   |   |
| test | test |   |   |
| url-alphabet | url-alphabet |   |   |
| .devcontainer.json | .devcontainer.json |   |   |
| .editorconfig | .editorconfig |   |   |
| .gitignore | .gitignore |   |   |
| .npmignore | .npmignore |   |   |
| .prettierignore | .prettierignore |   |   |
| .prettierrc.js | .prettierrc.js |   |   |
| CHANGELOG.md | CHANGELOG.md |   |   |
| LICENSE | LICENSE |   |   |
| README.ar.md | README.ar.md |   |   |
| README.id-ID.md | README.id-ID.md |   |   |
| README.ja.md | README.ja.md |   |   |
| README.ko.md | README.ko.md |   |   |
| README.md | README.md |   |   |
| README.ru.md | README.ru.md |   |   |
| README.zh-CN.md | README.zh-CN.md |   |   |
| SECURITY.md | SECURITY.md |   |   |
| index.browser.js | index.browser.js |   |   |
| index.d.ts | index.d.ts |   |   |
| index.js | index.js |   |   |
| jsr.json | jsr.json |   |   |
| nanoid.js | nanoid.js |   |   |
| oxfmt.config.ts | oxfmt.config.ts |   |   |
| oxlint.config.ts | oxlint.config.ts |   |   |
| package.json | package.json |   |   |
| pnpm-lock.yaml | pnpm-lock.yaml |   |   |
| pnpm-workspace.yaml | pnpm-workspace.yaml |   |   |
|   |   |   |   |

## Repository files navigation

# Nano ID

(Nano ID logo by Anton Lovchikov)

**English** | 日本語 | Русский | 简体中文 | Bahasa Indonesia | 한국어 | العربية

A tiny, secure, URL-friendly, unique string ID generator for JavaScript.

> “An amazing level of senseless perfectionism, which is simply impossible not to respect.”

- **Small.** 118 bytes (minified and brotlied). No dependencies. Size Limit controls the size.
- **Safe.** It uses hardware random generator. Can be used in clusters.
- **Short IDs.** It uses a larger alphabet than UUID (`A-Za-z0-9_-`). So ID size was reduced from 36 to 21 symbols.
- **Portable.** Nano ID was ported to over 20 programming languages.

```highlight
import { nanoid } from 'nanoid'
model.id = nanoid() //=> "V1StGXR8_Z5jdHi6B-myT"
```

Made at **Evil Martians**, product consulting for **developer tools**.

## Table of Contents

- Table of Contents
- Comparison with UUID
- Benchmark
- Security
- Install
  - ESM
  - CommonJS
  - JSR
  - CDN
- API
  - Blocking
  - Non-Secure
  - Custom Alphabet or Size
  - Custom Random Bytes Generator
- Usage
  - React
  - React Native
  - PouchDB and CouchDB
  - CLI
  - TypeScript
  - Other Programming Languages
- Tools

## Comparison with UUID

Nano ID is quite comparable to UUID v4 (random-based). It has a similar number of random bits in the ID (126 in Nano ID and 122 in UUID), so it has a similar collision probability:

> For there to be a one in a billion chance of duplication, 103 trillion version 4 IDs must be generated.

There are two main differences between Nano ID and UUID v4:

1. Nano ID uses a bigger alphabet, so a similar number of random bits are packed in just 21 symbols instead of 36.
2. Nano ID code is **4 times smaller** than `uuid/v4` package: 118 bytes instead of 423.

## Benchmark

```highlight
$ node ./test/benchmark.js
nope-id                 27,398,074 ops/sec
crypto.randomUUID       14,055,107 ops/sec
uuid v4                  9,256,301 ops/sec
@napi-rs/uuid            7,100,180 ops/sec
uid/secure               7,312,765 ops/sec
@lukeed/uuid             5,543,254 ops/sec
nanoid                   4,954,561 ops/sec
customAlphabet           6,708,339 ops/sec
nanoid for browser         497,980 ops/sec
secure-random-string       412,049 ops/sec
uid-safe.sync              420,669 ops/sec

Non-secure:
uid                     27,106,859 ops/sec
nanoid/non-secure        2,672,540 ops/sec
rndm                     2,666,518 ops/sec
```

Test configuration: Framework 13 7840U, Fedora 39, Node.js 21.6.

## Security

*See a good article about random generators theory: Secure random values (in Node.js)*

- **Unpredictability.** Instead of using the unsafe `Math.random()`, Nano ID uses the `crypto` module in Node.js and the Web Crypto API in browsers. These modules use unpredictable hardware random generator.
- **Uniformity.** `random % alphabet` is a popular mistake to make when coding an ID generator. The distribution will not be even; there will be a lower chance for some symbols to appear compared to others. So, it will reduce the number of tries when brute-forcing. Nano ID uses a better algorithm and is tested for uniformity. (Nano ID uniformity)
- **Well-documented:** all Nano ID hacks are documented. See comments in the source.
- **Vulnerabilities:** to report a security vulnerability, please use the Tidelift security contact. Tidelift will coordinate the fix and disclosure.

## Install

### ESM

Nano ID 5 works with ESM projects (with `import`) in tests or Node.js scripts.

```highlight
npm install nanoid
```

### CommonJS

Nano ID can be used with CommonJS in one of the following ways:

- You can use `require()` to import Nano ID. You need to use latest Node.js 22.12 (works out-of-the-box) or Node.js 20 (with `--experimental-require-module`).
- For Node.js 18 you can dynamically import Nano ID as follows: let nanoid module.exports.createID = async () => { if (!nanoid) ({ nanoid } = await import('nanoid')) return nanoid() // => "V1StGXR8_Z5jdHi6B-myT" }
- You can use Nano ID 3.x (we still support it): npm install nanoid@3

### JSR

JSR is a replacement for npm with open governance and active development (in contrast to npm).

```highlight
npx jsr add @sitnik/nanoid
```

You can use it in Node.js, Deno, Bun, etc.

```highlight
// Replace `nanoid` to `@sitnik/nanoid` in all imports
import { nanoid } from '@sitnik/nanoid'
```

For Deno install it by `deno add jsr:@sitnik/nanoid` or import from `jsr:@sitnik/nanoid`.

### CDN

For quick hacks, you can load Nano ID from CDN. Though, it is not recommended to be used in production because of the lower loading performance.

```highlight
import { nanoid } from 'https://cdn.jsdelivr.net/npm/nanoid/nanoid.js'
```

## API

Nano ID has 2 APIs: normal and non-secure.

By default, Nano ID uses URL-friendly symbols (`A-Za-z0-9_-`) and returns an ID with 21 characters (to have a collision probability similar to UUID v4).

### Blocking

The safe and easiest way to use Nano ID.

In rare cases could block CPU from other work while noise collection for hardware random generator.

```highlight
import { nanoid } from 'nanoid'
model.id = nanoid() //=> "V1StGXR8_Z5jdHi6B-myT"
```

If you want to reduce the ID size (and increase collisions probability), you can pass the size as an argument.

```highlight
nanoid(10) //=> "IRFa-VaY2b"
```

Don’t forget to check the safety of your ID size in our ID collision probability calculator.

You can also use a custom alphabet or a random generator.

### Non-Secure

By default, Nano ID uses hardware random bytes generation for security and low collision probability. If you are not so concerned with security, you can use it for environments without hardware random generators.

```highlight
import { nanoid } from 'nanoid/non-secure'
const id = nanoid() //=> "Uakgb_J5m9g-0JDMbcJqLJ"
```

### Custom Alphabet or Size

`customAlphabet` returns a function that allows you to create `nanoid` with your own alphabet and ID size.

```highlight
import { customAlphabet } from 'nanoid'
const nanoid = customAlphabet('1234567890abcdef', 10)
model.id = nanoid() //=> "4f90d13a42"
```

```highlight
import { customAlphabet } from 'nanoid/non-secure'
const nanoid = customAlphabet('1234567890abcdef', 10)
user.id = nanoid()
```

Check the safety of your custom alphabet and ID size in our ID collision probability calculator. For more alphabets, check out the options in `nanoid-dictionary`.

Alphabet must contain 256 symbols or less. Otherwise, the security of the internal generator algorithm is not guaranteed.

In addition to setting a default size, you can change the ID size when calling the function:

```highlight
import { customAlphabet } from 'nanoid'
const nanoid = customAlphabet('1234567890abcdef', 10)
model.id = nanoid(5) //=> "f01a2"
```

### Custom Random Bytes Generator

`customRandom` allows you to create a `nanoid` and replace alphabet and the default random bytes generator.

In this example, a seed-based generator is used:

```highlight
import { customRandom } from 'nanoid'

const rng = seedrandom(seed)
const nanoid = customRandom('abcdef', 10, size => {
  return new Uint8Array(size).map(() => 256 * rng())
})

nanoid() //=> "fbaefaadeb"
```

`random` callback must accept the array size and return an array with random numbers.

If you want to use the same URL-friendly symbols with `customRandom`, you can get the default alphabet using the `urlAlphabet`.

```highlight
import { customRandom, urlAlphabet } from 'nanoid'
const nanoid = customRandom(urlAlphabet, 10, random)
```

Note, that between Nano ID versions we may change random generator call sequence. If you are using seed-based generators, we do not guarantee the same result.

## Usage

### React

There’s no correct way to use Nano ID for React `key` prop since it should be consistent among renders.

```highlight
function Todos({ todos }) {
  return (
    <ul>
      {todos.map(todo => (
        <li key={nanoid()}>
          {' '}
          /* DON’T DO IT */
          {todo.text}
        </li>
      ))}
    </ul>
  )
}
```

You should rather try to reach for stable ID inside your list item.

```highlight
const todoItems = todos.map(todo => <li key={todo.id}>{todo.text}</li>)
```

In case you don’t have stable IDs you'd rather use index as `key` instead of `nanoid()`:

```highlight
const todoItems = todos.map((text, index) => (
  <li key={index}>
    {' '}
    /* Still not recommended but preferred over nanoid(). Only do this if items
    have no stable IDs. */
    {text}
  </li>
))
```

In case you just need random IDs to link elements like labels and input fields together, `useId` is recommended. That hook was added in React 18.

### React Native

React Native does not have built-in random generator. The following polyfill works for plain React Native and Expo starting with `39.x`.

1. Check `react-native-get-random-values` docs and install it.
2. Import it before Nano ID.

```highlight
import 'react-native-get-random-values'
import { nanoid } from 'nanoid'
```

### PouchDB and CouchDB

In PouchDB and CouchDB, IDs can’t start with an underscore `_`. A prefix is required to prevent this issue, as Nano ID might use a `_` at the start of the ID by default.

Override the default ID with the following option:

```highlight
db.put({
  _id: 'id' + nanoid(),
  …
})
```

### CLI

You can get unique ID in terminal by calling `npx nanoid`. You need only Node.js in the system. You do not need Nano ID to be installed anywhere.

```highlight
$ npx nanoid
npx: installed 1 in 0.63s
LZfXLFzPPR4NNrgjlWDxn
```

Size of generated ID can be specified with `--size` (or `-s`) option:

```highlight
$ npx nanoid --size 10
L3til0JS4z
```

Custom alphabet can be specified with `--alphabet` (or `-a`) option (note that in this case `--size` is required):

```highlight
$ npx nanoid --alphabet abc --size 15
bccbcabaabaccab
```

### TypeScript

Nano ID allows casting generated strings into opaque strings in TypeScript. For example:

```highlight
declare const userIdBrand: unique symbol
type UserId = string & { [userIdBrand]: true }

// Use explicit type parameter:
mockUser(nanoid<UserId>())

interface User {
  id: UserId
  name: string
}

const user: User = {
  // Automatically casts to UserId:
  id: nanoid(),
  name: 'Alice'
}
```

### Other Programming Languages

Nano ID was ported to many languages. You can use these ports to have the same ID generator on the client and server side.

- C
- C#
- C++
- Clojure and ClojureScript
- ColdFusion/CFML
- Crystal
- Dart & Flutter
- Elixir
- Gleam
- Go
- Haskell
- Haxe
- Janet
- Java
- Kotlin
- MySQL/MariaDB
- Nim
- OCaml
- Perl
- PHP
- Python native implementation with dictionaries and fast implementation (written in Rust)
- Postgres Extension and Native Function
- R (with dictionaries)
- Ruby
- Rust
- Swift
- Unison
- V
- Zig

For other environments, CLI is available to generate IDs from a command line.

## Tools

- ID size calculator shows collision probability when adjusting the ID alphabet or size.
- `nanoid-dictionary` with popular alphabets to use with `customAlphabet`.
- `nanoid-good` to be sure that your ID doesn’t contain any obscene words.
