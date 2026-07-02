---
title: "GitHub"
source: https://github.com/expressjs/express
domain: express-middleware
license: CC-BY-SA-4.0
tags: express middleware, express router, request handler chain, node web middleware
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

expressjs

/

express

Public

- Uh oh! There was an error while loading. Please reload this page.
- Notifications You must be signed in to change notification settings
- Fork 24k
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History6,153 Commits6,153 Commits |   |   |   |
| .github | .github |   |   |
| examples | examples |   |   |
| lib | lib |   |   |
| test | test |   |   |
| .editorconfig | .editorconfig |   |   |
| .eslintignore | .eslintignore |   |   |
| .eslintrc.yml | .eslintrc.yml |   |   |
| .gitignore | .gitignore |   |   |
| .npmrc | .npmrc |   |   |
| History.md | History.md |   |   |
| LICENSE | LICENSE |   |   |
| Readme.md | Readme.md |   |   |
| index.js | index.js |   |   |
| package.json | package.json |   |   |
|   |   |   |   |

## Repository files navigation

(Express Logo)

**Fast, unopinionated, minimalist web framework for Node.js.**

**This project has a Code of Conduct.**

## Table of contents

- Table of contents
- Installation
- Features
- Docs & Community
- Quick Start
- Philosophy
- Examples
- Contributing
  - Security Issues
  - Running Tests
- Current project team members
  - TC (Technical Committee)
    - TC emeriti members
  - Triagers
    - Emeritus Triagers
- License

(NPM Version) (NPM Downloads) (Linux Build) (Test Coverage) (OpenSSF Scorecard Badge)

```highlight
import express from 'express'

const app = express()

app.get('/', (req, res) => {
  res.send('Hello World')
})

app.listen(3000, () => {
  console.log('Server is running on http://localhost:3000')
})
```

## Installation

This is a Node.js module available through the npm registry.

Before installing, download and install Node.js. Node.js 18 or higher is required.

If this is a brand new project, make sure to create a `package.json` first with the `npm init` command.

Installation is done using the `npm install` command:

```highlight
npm install express
```

Follow our installing guide for more information.

## Features

- Robust routing
- Focus on high performance
- Super-high test coverage
- HTTP helpers (redirection, caching, etc)
- View system supporting 14+ template engines
- Content negotiation
- Executable for generating applications quickly

## Docs & Community

- Website and Documentation - [website repo]
- GitHub Organization for Official Middleware & Modules
- Github Discussions for discussion on the development and usage of Express

**PROTIP** Be sure to read the migration guide to v5

## Quick Start

The quickest way to get started with express is to utilize the executable `express(1)` to generate an application as shown below:

Install the executable. The executable's major version will match Express's:

```highlight
npm install -g express-generator@4
```

Create the app:

```highlight
express /tmp/foo && cd /tmp/foo
```

Install dependencies:

```highlight
npm install
```

Start the server:

```highlight
npm start
```

View the website at: http://localhost:3000

## Philosophy

The Express philosophy is to provide small, robust tooling for HTTP servers, making it a great solution for single page applications, websites, hybrids, or public HTTP APIs.

Express does not force you to use any specific ORM or template engine. With support for over 14 template engines via @ladjs/consolidate, you can quickly craft your perfect framework.

## Examples

To view the examples, clone the Express repository:

```highlight
git clone https://github.com/expressjs/express.git --depth 1 && cd express
```

Then install the dependencies:

```highlight
npm install
```

Then run whichever example you want:

```highlight
node examples/content-negotiation
```

## Contributing

The Express.js project welcomes all constructive contributions. Contributions take many forms, from code for bug fixes and enhancements, to additions and fixes to documentation, additional tests, triaging incoming pull requests and issues, and more!

See the Contributing Guide for more technical details on contributing.

### Security Issues

If you discover a security vulnerability in Express, please see Security Policies and Procedures.

### Running Tests

To run the test suite, first install the dependencies:

```highlight
npm install
```

Then run `npm test`:

```highlight
npm test
```

## Current project team members

For information about the governance of the express.js project, see GOVERNANCE.md.

The original author of Express is TJ Holowaychuk

List of all contributors

### TC (Technical Committee)

- UlisesGascon - **Ulises Gascón** (he/him)
- jonchurch - **Jon Church**
- wesleytodd - **Wes Todd**
- LinusU - **Linus Unnebäck**
- blakeembrey - **Blake Embrey**
- sheplu - **Jean Burellier**
- crandmck - **Rand McKinney**
- ctcpip - **Chris de Almeida**

TC emeriti members

#### TC emeriti members

- dougwilson - **Douglas Wilson**
- hacksparrow - **Hage Yaapa**
- jonathanong - **jongleberry**
- niftylettuce - **niftylettuce**
- troygoode - **Troy Goode**

### Triagers

- aravindvnair99 - **Aravind Nair**
- bjohansebas - **Sebastian Beltran**
- carpasse - **Carlos Serrano**
- CBID2 - **Christine Belzie**
- UlisesGascon - **Ulises Gascón** (he/him)
- IamLizu - **S M Mahmudul Hasan** (he/him)
- Phillip9587 - **Phillip Barta**
- efekrskl - **Efe Karasakal**
- rxmarbles - **Rick Markins** (he/him)
- krzysdz
- GroophyLifefor - **Murat Kirazkaya**

Triagers emeriti members

#### Emeritus Triagers

- AuggieH - **Auggie Hudak**
- G-Rath - **Gareth Jones**
- MohammadXroid - **Mohammad Ayashi**
- NawafSwe - **Nawaf Alsharqi**
- NotMoni - **Moni**
- VigneshMurugan - **Vignesh Murugan**
- davidmashe - **David Ashe**
- digitaIfabric - **David**
- e-l-i-s-e - **Elise Bonner**
- fed135 - **Frederic Charette**
- firmanJS - **Firman Abdul Hakim**
- getspooky - **Yasser Ameur**
- ghinks - **Glenn**
- ghousemohamed - **Ghouse Mohamed**
- gireeshpunathil - **Gireesh Punathil**
- jake32321 - **Jake Reed**
- jonchurch - **Jon Church**
- lekanikotun - **Troy Goode**
- marsonya - **Lekan Ikotun**
- mastermatt - **Matt R. Wilson**
- maxakuru - **Max Edell**
- mlrawlings - **Michael Rawlings**
- rodion-arr - **Rodion Abdurakhimov**
- sheplu - **Jean Burellier**
- tarunyadav1 - **Tarun yadav**
- tunniclm - **Mike Tunnicliffe**
- enyoghasim - **David Enyoghasim**
- 0ss - **Salah**
- ejcheng- **Eric Cheng** (he/him)
- dakshkhetan - **Daksh Khetan** (he/him)
- lucasraziel - **Lucas Soares Do Rego**
- mertcanaltin - **Mert Can Altin**
- dpopp07 - **Dustin Popp**
- Sushmeet - **Sushmeet Sunger**
- 3imed-jaberi - **Imed Jaberi**

## License

MIT
