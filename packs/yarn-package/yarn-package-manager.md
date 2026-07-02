---
title: "yarn (package manager)"
source: https://en.wikipedia.org/wiki/Yarn_(package_manager)
domain: yarn-package
license: CC-BY-SA-4.0
tags: yarn package, node package manager, javascript packages, workspaces monorepo
fetched: 2026-07-02
---

# yarn (package manager)

**Yarn** is one of the main JavaScript package managers, initially started in 2016 by Sebastian McKenzie of Meta (formerly Facebook) for the Node.js JavaScript runtime environment. An alternative to the npm package manager, Yarn was created as a collaboration of Facebook (now Meta), Exponent (now Expo.dev), Google, and Tilde (the company behind Ember.js) to solve consistency, security, and performance problems with large codebases.

While bootstrapped by tech companies, the project was setup from the get go as its own GitHub organization, and eventually became fully autonomous in 2019, following its lead maintainer as he left Facebook for Datadog.

## Yarn 2 & Yarn Plug'n'Play

In 2020 the Yarn team released a major update, Yarn 2.0, also codenamed "Berry". This version came with a full rewriting of both the codebase (which migrated to TypeScript in the process) and test suite. Many features were introduced, a cleaving one being a new unique installation strategy called Yarn Plug'n'Play.

Under this default but optional mode, Yarn wouldn't generate a `node_modules` folder anymore, instead opting to generate a single Node.js resolver file named `.pnp.cjs`. While justified by the Yarn team as a need to address multiple design flaws in the typical Node.js module resolution, this change required some support from other projects in the ecosystem which took some time to materialise, adding friction to the migration from Yarn 1.22. to Yarn 2.0.

## Plugins

Users can write their own plugins for Yarn.

### Constraints

Yarn constraints allow users to enforce rules for their dependencies or manifest fields across scoped workspaces.

### Offline cache

Downloaded packages are cached and stored as a single file.

### Plug'n'Play

Plug'n'Play allows users to run Node projects without `node_modules` folder, defining the way or location to resolve dependencies package files with the Plug-n-Play-control file. This feature is aimed to fix an unwell structured `node_modules` architecture and resulting in a faster Node.js application start-up time.

### Plugins

Plugins can add new resolvers, fetchers, linkers, commands, and can also register to some events or be integrated with each other, most features of Yarn are implemented through plugins, including `yarn add` and `yarn install`, which are also preinstalled plugins.

### Protocols

Users can define which protocol will be used to resolve certain packages, for example, the *git* protocol is used for downloading a public package from a Git repository, and the *patch* protocol is used for creating a patched copy of the original package.

### Release Workflow

Release Workflow automatically upgrades relative packages among monorepos workspaces when root packages are upgraded.

### Workspaces

Workspaces allow multiple projects to work together in the same repository and automatically apply changes to other relatives when source code is modified, allowing installation of multiple packages in a single pass by running the installation command only once.

### Zero-Installs

Zero-Installs solve the needs of installation of packages when packages is required to install when the codes is just fresh fetched to local.

## Comparison to npm

- Yarn can install packages from local cache.
- Yarn binds versions of the package strongly.
- Yarn uses checksum for ensuring data integrity, while npm uses SHA-512 to check data integrity of the packages downloaded.
- Yarn installs packages in parallel, while npm installs one package at a time.

## Syntax

To install yarn:

```
npm install -g yarn
```

To install a package with yarn:

```
yarn add package-name
```

To install a package with yarn for development and testing purposes:

```
yarn add package-name --dev
```

NB: in the first versions, it was:

```
yarn install package-name --save-dev
```
