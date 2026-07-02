---
title: "GitHub"
source: https://github.com/knex/knex
domain: knex-querybuilder
license: CC-BY-SA-4.0
tags: knex query builder, sql query builder, database migration tool, fluent sql interface
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

knex

/

knex

Public

- Notifications You must be signed in to change notification settings
- Fork 2.2k
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History3,212 Commits3,212 Commits |   |   |   |
| .github | .github |   |   |
| .husky | .husky |   |   |
| bin | bin |   |   |
| docs | docs |   |   |
| lib | lib |   |   |
| scripts | scripts |   |   |
| test-tsd | test-tsd |   |   |
| test-tstyche | test-tstyche |   |   |
| test | test |   |   |
| types | types |   |   |
| .codecov.yml | .codecov.yml |   |   |
| .editorconfig | .editorconfig |   |   |
| .eslintignore | .eslintignore |   |   |
| .eslintrc.js | .eslintrc.js |   |   |
| .gitignore | .gitignore |   |   |
| .npmrc | .npmrc |   |   |
| .prettierrc | .prettierrc |   |   |
| CHANGELOG.md | CHANGELOG.md |   |   |
| CONTRIBUTING.md | CONTRIBUTING.md |   |   |
| ECOSYSTEM.md | ECOSYSTEM.md |   |   |
| LICENSE | LICENSE |   |   |
| README.md | README.md |   |   |
| UPGRADING.md | UPGRADING.md |   |   |
| knex.d.mts | knex.d.mts |   |   |
| knex.js | knex.js |   |   |
| knex.mjs | knex.mjs |   |   |
| package.json | package.json |   |   |
| tsconfig.json | tsconfig.json |   |   |
|   |   |   |   |

## Repository files navigation

# knex.js

(npm version) (npm downloads) (codecov) (Dependencies Status) (Gitter chat)

> **A SQL query builder that is *flexible*, *portable*, and *fun* to use!**

A batteries-included, multi-dialect (PostgreSQL, MariaDB, MySQL, CockroachDB, MSSQL, SQLite3, Oracle (including Oracle Wallet Authentication)) query builder for Node.js, featuring:

- transactions
- connection pooling
- streaming queries
- both a promise and callback API
- a thorough test suite

Node.js versions 16+ are supported.

- Take a look at the full documentation to get started!
- Browse the list of plugins and tools built for knex
- Check out our recipes wiki to search for solutions to some specific problems
- In case of upgrading from an older version, see migration guide

You can report bugs and discuss features on the GitHub issues page or send tweets to @kibertoad.

For support and questions, join our Gitter channel.

For knex-based Object Relational Mapper, see:

- https://github.com/Vincit/objection.js
- https://github.com/mikro-orm/mikro-orm
- https://bookshelfjs.org

To see the SQL that Knex will generate for a given query, you can use Knex Query Lab

## Local Development Setup

### Prerequisites

- Node.js 16+
- Python 3.x with `setuptools` installed (required for building native dependencies like `better-sqlite3`) Python 3.12+ removed the built-in `distutils` module. If you encounter a `ModuleNotFoundError: No module named 'distutils'` error during `npm install`, install `setuptools` for the Python version used by node-gyp: pip install setuptools
- **Windows only:** Visual Studio Build Tools with the "Desktop development with C++" workload

### Install dependencies

```highlight
npm install
```

## Examples

We have several examples on the website. Here is the first one to get you started:

```highlight
const knex = require('knex')({
  client: 'sqlite3',
  connection: {
    filename: './data.db',
  },
});

try {
  // Create a table
  await knex.schema
    .createTable('users', (table) => {
      table.increments('id');
      table.string('user_name');
    })
    // ...and another
    .createTable('accounts', (table) => {
      table.increments('id');
      table.string('account_name');
      table.integer('user_id').unsigned().references('users.id');
    });

  // Then query the table...
  const insertedRows = await knex('users').insert({ user_name: 'Tim' });

  // ...and using the insert id, insert into the other table.
  await knex('accounts').insert({
    account_name: 'knex',
    user_id: insertedRows[0],
  });

  // Query both of the rows.
  const selectedRows = await knex('users')
    .join('accounts', 'users.id', 'accounts.user_id')
    .select('users.user_name as user', 'accounts.account_name as account');

  // map over the results
  const enrichedRows = selectedRows.map((row) => ({ ...row, active: true }));

  // Finally, add a catch statement
} catch (e) {
  console.error(e);
}
```

## TypeScript example

```highlight
import { Knex, knex } from 'knex';

interface User {
  id: number;
  age: number;
  name: string;
  active: boolean;
  departmentId: number;
}

const config: Knex.Config = {
  client: 'sqlite3',
  connection: {
    filename: './data.db',
  },
  useNullAsDefault: true,
};

const knexInstance = knex(config);

knexInstance<User>('users')
  .select()
  .then((users) => {
    console.log(users);
  })
  .catch((err) => {
    console.error(err);
  })
  .finally(() => {
    knexInstance.destroy();
  });
```

## Usage as ESM module

If you are launching your Node application with `--experimental-modules`, `knex.mjs` should be picked up automatically and named ESM import should work out-of-the-box. Otherwise, if you want to use named imports, you'll have to import knex like this:

```highlight
import { knex } from 'knex/knex.mjs';
```

You can also just do the default import:

```highlight
import knex from 'knex';
```

If you are not using TypeScript and would like the IntelliSense of your IDE to work correctly, it is recommended to set the type explicitly:

```highlight
/**
 * @type {Knex}
 */
const database = knex({
  client: 'mysql',
  connection: {
    host: '127.0.0.1',
    user: 'your_database_user',
    password: 'your_database_password',
    database: 'myapp_test',
  },
});
database.migrate.latest();
```
