---
title: "GitHub"
source: https://github.com/ReactiveX/rxjs
domain: rxjs-observable
license: CC-BY-SA-4.0
tags: rxjs observable, reactive extensions, observable stream, async event pipeline
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

ReactiveX

/

rxjs

Public

- Notifications You must be signed in to change notification settings
- Fork 3k
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History5,461 Commits5,461 Commits |   |   |   |
| .github | .github |   |   |
| apps/rxjs.dev | apps/rxjs.dev |   |   |
| packages | packages |   |   |
| resources/CI-CD | resources/CI-CD |   |   |
| scripts | scripts |   |   |
| .editorconfig | .editorconfig |   |   |
| .eslintignore | .eslintignore |   |   |
| .eslintrc.json | .eslintrc.json |   |   |
| .gitignore | .gitignore |   |   |
| .prettierrc.json | .prettierrc.json |   |   |
| CODE_OF_CONDUCT.md | CODE_OF_CONDUCT.md |   |   |
| CONTRIBUTING.md | CONTRIBUTING.md |   |   |
| LICENSE.txt | LICENSE.txt |   |   |
| README.md | README.md |   |   |
| SECURITY.md | SECURITY.md |   |   |
| nx.json | nx.json |   |   |
| package.json | package.json |   |   |
| yarn.lock | yarn.lock |   |   |
|   |   |   |   |

## Repository files navigation

# (RxJS Logo) RxJS: Reactive Extensions For JavaScript

(CI) (npm version) (Join the chat at https://gitter.im/Reactive-Extensions/RxJS)

# RxJS 8 Monorepo

Look for RxJS and related packages under the /packages directory. Applications like the rxjs.dev documentation site are under the /apps directory.

Apache 2.0 License

- Code of Conduct
- Contribution Guidelines
- Maintainer Guidelines
- API Documentation

Reactive Extensions Library for JavaScript. This is a rewrite of Reactive-Extensions/RxJS and is the latest production-ready version of RxJS. This rewrite is meant to have better performance, better modularity, better debuggable call stacks, while staying mostly backwards compatible, with some breaking changes that reduce the API surface.

## Versions In This Repository

- master - This is all of the current work, which is against v8 of RxJS right now
- 7.x - This is the branch for version 7.X
- 6.x - This is the branch for version 6.X

Most PRs should be made to **master**.

## Important

By contributing or commenting on issues in this repository, whether you've read them or not, you're agreeing to the Contributor Code of Conduct. Much like traffic laws, ignorance doesn't grant you immunity.

## Development

Because of this issue we're using `yarn`. (Basically the docs app uses `@types/jasmine`, and the package uses `@types/mocha` and they get hoisted to the top level by `npm install` with workspaces, and then TypeScript vomits everywhere when you try to build).

1. `cd` to the repository root
2. `yarn install` to install all dependencies
3. `yarn workspace rxjs test` will run the RxJS test suite
4. `yarn workspace rxjs.dev start` will start the rxjs.dev documentation site local development server
