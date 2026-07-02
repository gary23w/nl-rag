---
title: "GitHub"
source: https://github.com/uuidjs/uuid
domain: uuid-generation
license: CC-BY-SA-4.0
tags: uuid generation, universally unique identifier, rfc 4122 uuid, random identifier
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

uuidjs

/

uuid

Public

- Uh oh! There was an error while loading. Please reload this page.
- Notifications You must be signed in to change notification settings
- Fork 977
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History628 Commits628 Commits |   |   |   |
| .github | .github |   |   |
| .vscode | .vscode |   |   |
| examples | examples |   |   |
| scripts | scripts |   |   |
| src | src |   |   |
| test/browser | test/browser |   |   |
| .gitignore | .gitignore |   |   |
| .npmrc | .npmrc |   |   |
| AUTHORS | AUTHORS |   |   |
| CHANGELOG.md | CHANGELOG.md |   |   |
| CONTRIBUTING.md | CONTRIBUTING.md |   |   |
| LICENSE.md | LICENSE.md |   |   |
| README.md | README.md |   |   |
| README_js.md | README_js.md |   |   |
| biome.jsonc | biome.jsonc |   |   |
| bundlewatch.config.json | bundlewatch.config.json |   |   |
| lefthook.yml | lefthook.yml |   |   |
| package-lock.json | package-lock.json |   |   |
| package.json | package.json |   |   |
| prettier.config.js | prettier.config.js |   |   |
| tsconfig.json | tsconfig.json |   |   |
| wdio.conf.js | wdio.conf.js |   |   |
|   |   |   |   |

## Repository files navigation

# uuid (CI) (Browser)

For the creation of RFC9562 (formerly RFC4122) UUIDs

- **Complete** - Support for all RFC9562 UUID versions
- **Cross-platform** - Support for...
  - Typescript
  - Chrome, Safari, Firefox, and Edge
  - NodeJS
  - React Native / Expo
- **Secure** - Uses modern `crypto` API for random values
- **Compact** - Zero-dependency, tree-shakable
- **CLI** - `uuid` command line utility

Note

Starting with `uuid@12` CommonJS is no longer supported. See implications and motivation for details.

## Quickstart

**1. Install**

```highlight
npm install uuid
```

**2. Create a UUID**

```highlight
import { v4 as uuidv4 } from 'uuid';

uuidv4(); // ⇨ 'b18794e8-5d0d-417c-b361-ba38e78411b4'
```

For timestamp UUIDs, namespace UUIDs, and other options read on ...

## API Summary

|   |   |   |
|---|---|---|
| `uuid.NIL` | The nil UUID string (all zeros) | New in `uuid@8.3` |
| `uuid.MAX` | The max UUID string (all ones) | New in `uuid@9.1` |
| `uuid.parse()` | Convert UUID string to array of bytes | New in `uuid@8.3` |
| `uuid.stringify()` | Convert array of bytes to UUID string | New in `uuid@8.3` |
| `uuid.v1()` | Create a version 1 (timestamp) UUID |   |
| `uuid.v1ToV6()` | Create a version 6 UUID from a version 1 UUID | New in `uuid@10` |
| `uuid.v3()` | Create a version 3 (namespace w/ MD5) UUID |   |
| `uuid.v4()` | Create a version 4 (random) UUID |   |
| `uuid.v5()` | Create a version 5 (namespace w/ SHA-1) UUID |   |
| `uuid.v6()` | Create a version 6 (timestamp, reordered) UUID | New in `uuid@10` |
| `uuid.v6ToV1()` | Create a version 1 UUID from a version 6 UUID | New in `uuid@10` |
| `uuid.v7()` | Create a version 7 (Unix Epoch time-based) UUID | New in `uuid@10` |
| `uuid.v8()` | "Intentionally left blank" |   |
| `uuid.validate()` | Test a string to see if it is a valid UUID | New in `uuid@8.3` |
| `uuid.version()` | Detect RFC version of a UUID | New in `uuid@8.3` |

## API

### uuid.NIL

The nil UUID string (all zeros).

Example:

```highlight
import { NIL as NIL_UUID } from 'uuid';

NIL_UUID; // ⇨ '00000000-0000-0000-0000-000000000000'
```

### uuid.MAX

The max UUID string (all ones).

Example:

```highlight
import { MAX as MAX_UUID } from 'uuid';

MAX_UUID; // ⇨ 'ffffffff-ffff-ffff-ffff-ffffffffffff'
```

### uuid.parse(str)

Convert UUID string to array of bytes

|   |   |
|---|---|
| `str` | A valid UUID `String` |
| *returns* | `Uint8Array[16]` |
| *throws* | `TypeError` if `str` is not a valid UUID |

Note

Ordering of values in the byte arrays used by `parse()` and `stringify()` follows the left ↠ right order of hex-pairs in UUID strings. As shown in the example below.

Example:

```highlight
import { parse as uuidParse } from 'uuid';

// Parse a UUID
uuidParse('6ec0bd7f-11c0-43da-975e-2a8ad9ebae0b'); // ⇨
// Uint8Array(16) [
//   110, 192, 189, 127,  17,
//   192,  67, 218, 151,  94,
//    42, 138, 217, 235, 174,
//    11
// ]
```

### uuid.stringify(arr[, offset])

Convert array of bytes to UUID string

|   |   |
|---|---|
| `arr` | `Array`-like collection of 16 values (starting from `offset`) between 0-255. |
| [`offset` = 0] | `Number` Starting index in the Array |
| *returns* | `String` |
| *throws* | `TypeError` if a valid UUID string cannot be generated |

Note

Ordering of values in the byte arrays used by `parse()` and `stringify()` follows the left ↠ right order of hex-pairs in UUID strings. As shown in the example below.

Example:

```highlight
import { stringify as uuidStringify } from 'uuid';

const uuidBytes = Uint8Array.of(
  0x6e,
  0xc0,
  0xbd,
  0x7f,
  0x11,
  0xc0,
  0x43,
  0xda,
  0x97,
  0x5e,
  0x2a,
  0x8a,
  0xd9,
  0xeb,
  0xae,
  0x0b
);

uuidStringify(uuidBytes); // ⇨ '6ec0bd7f-11c0-43da-975e-2a8ad9ebae0b'
```

### uuid.v1([options[, buffer[, offset]]])

Create an RFC version 1 (timestamp) UUID

|   |   |
|---|---|
| [`options`] | `Object` with one or more of the following properties: |
| [`options.node = (random)` ] | RFC "node" field as an `Array[6]` of byte values (per 4.1.6) |
| [`options.clockseq = (random)`] | RFC "clock sequence" as a `Number` between 0 - 0x3fff |
| [`options.msecs = (current time)`] | RFC "timestamp" field (`Number` of milliseconds, unix epoch) |
| [`options.nsecs = 0`] | RFC "timestamp" field (`Number` of nanoseconds to add to `msecs`, should be 0-10,000) |
| [`options.random = (random)`] | `Array` of 16 random bytes (0-255) used to generate other fields, above |
| [`options.rng`] | Alternative to `options.random`, a `Function` that returns an `Array` of 16 random bytes (0-255) |
| [`buffer`] | `Uint8Array` or `Uint8Array` subtype (e.g. Node.js `Buffer`). If provided, binary UUID is written into the array, starting at `offset` |
| [`offset` = 0] | `Number` Index to start writing UUID bytes in `buffer` |
| *returns* | UUID `String` if no `buffer` is specified, otherwise returns `buffer` |
| *throws* | `Error` if more than 10M UUIDs/sec are requested |

Example:

```highlight
import { v1 as uuidv1 } from 'uuid';

uuidv1(); // ⇨ '57fd0000-c7d3-11ef-841d-514d2167fc5b'
```

Example using `options`:

```highlight
import { v1 as uuidv1 } from 'uuid';

const options = {
  node: Uint8Array.of(0x01, 0x23, 0x45, 0x67, 0x89, 0xab),
  clockseq: 0x1234,
  msecs: new Date('2011-11-01').getTime(),
  nsecs: 5678,
};
uuidv1(options); // ⇨ '710b962e-041c-11e1-9234-0123456789ab'
```

### uuid.v1ToV6(uuid)

Convert a UUID from version 1 to version 6

```highlight
import { v1ToV6 } from 'uuid';

v1ToV6('92f62d9e-22c4-11ef-97e9-325096b39f47'); // ⇨ '1ef22c49-2f62-6d9e-97e9-325096b39f47'
```

### uuid.v3(name, namespace[, buffer[, offset]])

Create an RFC version 3 (namespace w/ MD5) UUID

API is identical to `v5()`, but uses "v3" instead.

Important

Per the RFC, "*If backward compatibility is not an issue, SHA-1 [Version 5] is preferred*."

### uuid.v4([options[, buffer[, offset]]])

Create an RFC version 4 (random) UUID

|   |   |
|---|---|
| [`options`] | `Object` with one or more of the following properties: |
| [`options.random`] | `Array` of 16 random bytes (0-255) |
| [`options.rng`] | Alternative to `options.random`, a `Function` that returns an `Array` of 16 random bytes (0-255) |
| [`buffer`] | `Uint8Array` or `Uint8Array` subtype (e.g. Node.js `Buffer`). If provided, binary UUID is written into the array, starting at `offset` |
| [`offset` = 0] | `Number` Index to start writing UUID bytes in `buffer` |
| *returns* | UUID `String` if no `buffer` is specified, otherwise returns `buffer` |

Example:

```highlight
import { v4 as uuidv4 } from 'uuid';

uuidv4(); // ⇨ 'b18794e8-5d0d-417c-b361-ba38e78411b4'
```

Example using predefined `random` values:

```highlight
import { v4 as uuidv4 } from 'uuid';

const v4options = {
  random: Uint8Array.of(
    0x10,
    0x91,
    0x56,
    0xbe,
    0xc4,
    0xfb,
    0xc1,
    0xea,
    0x71,
    0xb4,
    0xef,
    0xe1,
    0x67,
    0x1c,
    0x58,
    0x36
  ),
};
uuidv4(v4options); // ⇨ '109156be-c4fb-41ea-b1b4-efe1671c5836'
```

### uuid.v5(name, namespace[, buffer[, offset]])

Create an RFC version 5 (namespace w/ SHA-1) UUID

|   |   |
|---|---|
| `name` | `String \| Array` |
| `namespace` | `String \| Array[16]` Namespace UUID |
| [`buffer`] | `Uint8Array` or `Uint8Array` subtype (e.g. Node.js `Buffer`). If provided, binary UUID is written into the array, starting at `offset` |
| [`offset` = 0] | `Number` Index to start writing UUID bytes in `buffer` |
| *returns* | UUID `String` if no `buffer` is specified, otherwise returns `buffer` |

Note

The RFC `DNS` and `URL` namespaces are available as `v5.DNS` and `v5.URL`.

Example with custom namespace:

```highlight
import { v5 as uuidv5 } from 'uuid';

// Define a custom namespace.  Readers, create your own using something like
// https://www.uuidgenerator.net/
const MY_NAMESPACE = '1b671a64-40d5-491e-99b0-da01ff1f3341';

uuidv5('Hello, World!', MY_NAMESPACE); // ⇨ '630eb68f-e0fa-5ecc-887a-7c7a62614681'
```

Example with RFC `URL` namespace:

```highlight
import { v5 as uuidv5 } from 'uuid';

uuidv5('https://www.w3.org/', uuidv5.URL); // ⇨ 'c106a26a-21bb-5538-8bf2-57095d1976c1'
```

### uuid.v6([options[, buffer[, offset]]])

Create an RFC version 6 (timestamp, reordered) UUID

This method takes the same arguments as uuid.v1().

```highlight
import { v6 as uuidv6 } from 'uuid';

uuidv6(); // ⇨ '1efc7d35-7fd0-6000-841d-504d2167fc5b'
```

Example using `options`:

```highlight
import { v6 as uuidv6 } from 'uuid';

const options = {
  node: [0x01, 0x23, 0x45, 0x67, 0x89, 0xab],
  clockseq: 0x1234,
  msecs: new Date('2011-11-01').getTime(),
  nsecs: 5678,
};
uuidv6(options); // ⇨ '1e1041c7-10b9-662e-9234-0123456789ab'
```

### uuid.v6ToV1(uuid)

Convert a UUID from version 6 to version 1

```highlight
import { v6ToV1 } from 'uuid';

v6ToV1('1ef22c49-2f62-6d9e-97e9-325096b39f47'); // ⇨ '92f62d9e-22c4-11ef-97e9-325096b39f47'
```

### uuid.v7([options[, buffer[, offset]]])

Create an RFC version 7 (random) UUID

|   |   |
|---|---|
| [`options`] | `Object` with one or more of the following properties: |
| [`options.msecs = (current time)`] | RFC "timestamp" field (`Number` of milliseconds, unix epoch) |
| [`options.random = (random)`] | `Array` of 16 random bytes (0-255) used to generate other fields, above |
| [`options.rng`] | Alternative to `options.random`, a `Function` that returns an `Array` of 16 random bytes (0-255) |
| [`options.seq = (random)`] | 32-bit sequence `Number` between 0 - 0xffffffff. This may be provided to help ensure uniqueness for UUIDs generated within the same millisecond time interval. Default = random value. |
| [`buffer`] | `Uint8Array` or `Uint8Array` subtype (e.g. Node.js `Buffer`). If provided, binary UUID is written into the array, starting at `offset` |
| [`offset` = 0] | `Number` Index to start writing UUID bytes in `buffer` |
| *returns* | UUID `String` if no `buffer` is specified, otherwise returns `buffer` |

Example:

```highlight
import { v7 as uuidv7 } from 'uuid';

uuidv7(); // ⇨ '01941f29-7c00-75f4-a310-744d2167fc5b'
```

### uuid.v8()

***"Intentionally left blank"***

Note

Version 8 (experimental) UUIDs are "for experimental or vendor-specific use cases". The RFC does not define a creation algorithm for them, which is why this package does not offer a `v8()` method. The `validate()` and `version()` methods do work with such UUIDs, however.

### uuid.validate(str)

Test a string to see if it is a valid UUID

|   |   |
|---|---|
| `str` | `String` to validate |
| *returns* | `true` if string is a valid UUID, `false` otherwise |

Example:

```highlight
import { validate as uuidValidate } from 'uuid';

uuidValidate('not a UUID'); // ⇨ false
uuidValidate('6ec0bd7f-11c0-43da-975e-2a8ad9ebae0b'); // ⇨ true
```

Using `validate` and `version` together it is possible to do per-version validation, e.g. validate for only v4 UUIds.

```highlight
import { version as uuidVersion } from 'uuid';
import { validate as uuidValidate } from 'uuid';

function uuidValidateV4(uuid) {
  return uuidValidate(uuid) && uuidVersion(uuid) === 4;
}

const v1Uuid = 'd9428888-122b-11e1-b85c-61cd3cbb3210';
const v4Uuid = '109156be-c4fb-41ea-b1b4-efe1671c5836';

uuidValidateV4(v4Uuid); // ⇨ true
uuidValidateV4(v1Uuid); // ⇨ false
```

### uuid.version(str)

Detect RFC version of a UUID

|   |   |
|---|---|
| `str` | A valid UUID `String` |
| *returns* | `Number` The RFC version of the UUID |
| *throws* | `TypeError` if `str` is not a valid UUID |

Example:

```highlight
import { version as uuidVersion } from 'uuid';

uuidVersion('45637ec4-c85f-11ea-87d0-0242ac130003'); // ⇨ 1
uuidVersion('6ec0bd7f-11c0-43da-975e-2a8ad9ebae0b'); // ⇨ 4
```

Note

This method returns `0` for the `NIL` UUID, and `15` for the `MAX` UUID.

## Command Line

UUIDs can be generated from the command line using `uuid`.

```highlight
$ npx uuid
ddeb27fb-d9a0-4624-be4d-4615062daed4
```

The default is to generate version 4 UUIDS, however the other versions are supported. Type `uuid --help` for details:

```highlight
$ npx uuid --help

Usage:
  uuid
  uuid v1
  uuid v3 <name> <namespace uuid>
  uuid v4
  uuid v5 <name> <namespace uuid>
  uuid v7
  uuid --help

Note: <namespace uuid> may be "URL" or "DNS" to use the corresponding UUIDs
defined by RFC9562
```

## `options` Handling for Timestamp UUIDs

Prior to `uuid@11`, it was possible for `options` state to interfere with the internal state used to ensure uniqueness of timestamp-based UUIDs (the `v1()`, `v6()`, and `v7()` methods). Starting with `uuid@11`, this issue has been addressed by using the presence of the `options` argument as a flag to select between two possible behaviors:

- Without `options`: Internal state is utilized to improve UUID uniqueness.
- With `options`: Internal state is **NOT** used and, instead, appropriate defaults are applied as needed.

## Support

**Browsers**: `uuid` builds are tested against the latest version of desktop Chrome, Safari, Firefox, and Edge. Mobile versions of these same browsers are expected to work but aren't currently tested.

**Node**: `uuid` builds are tested against node (LTS releases), plus one prior. E.g. At the time of this writing `node@20` is the "maintenance" release and `node@24` is the "current" release, so `uuid` supports `node@20`-`node@24`.

**Typescript**: TS versions released within the past two years are supported. source

## Known issues

### "getRandomValues() not supported"

This error occurs in environments where the standard `crypto.getRandomValues()` API is not supported. This issue can be resolved by adding an appropriate polyfill:

#### React Native / Expo

1. Install `react-native-get-random-values`
2. Import it *before* `uuid`. Since `uuid` might also appear as a transitive dependency of some other imports it's safest to just import `react-native-get-random-values` as the very first thing in your entry point:

```highlight
import 'react-native-get-random-values';
import { v4 as uuidv4 } from 'uuid';
```

Generated from README_js.md by `runmd`
