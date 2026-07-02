---
title: "Writing and organizing Cypress tests"
source: https://docs.cypress.io/guides/core-concepts/writing-and-organizing-tests
domain: cypress-e2e
license: CC-BY-SA-4.0
tags: cypress testing, end-to-end testing, web testing, browser tests
fetched: 2026-07-02
---

# Writing and organizing Cypress tests

Cypress App

# Writing and Organizing Tests

info

##### What you'll learn

- How Cypress organizes your project and why it uses the conventions it does
- The types of files Cypress works with and the role each one plays
- How to write tests, including structure, hooks, configuration, and assertions
- How to read the four test statuses Cypress reports
- Which files Cypress watches so your tests re-run as you write them

## Project structure

Cypress favors **convention over configuration**. When you add a new project, Cypress scaffolds a suggested folder structure so you can start writing tests immediately, without deciding where everything should live or wiring up a build step. Everything below can be reconfigured, but the defaults are designed to get out of your way.

By default Cypress creates:

- JavaScript
- TypeScript

```
E2E:
/cypress.config.js
/cypress/fixtures/example.json
/cypress/support/commands.js
/cypress/support/e2e.js

Component:
/cypress.config.js
/cypress/fixtures/example.json
/cypress/support/commands.js
/cypress/support/component.js
/cypress/support/component-index.html

Both:
/cypress.config.js
/cypress/fixtures/example.json
/cypress/support/commands.js
/cypress/support/e2e.js
/cypress/support/component.js
/cypress/support/component-index.html
```

```
E2E:
/cypress.config.ts
/cypress/fixtures/example.json
/cypress/support/commands.ts
/cypress/support/e2e.ts

Component:
/cypress.config.ts
/cypress/fixtures/example.json
/cypress/support/commands.ts
/cypress/support/component.ts
/cypress/support/component-index.html

Both:
/cypress.config.ts
/cypress/fixtures/example.json
/cypress/support/commands.ts
/cypress/support/e2e.ts
/cypress/support/component.ts
/cypress/support/component-index.html
```

### Configuring file locations

These locations are conventions, not requirements. You can point Cypress at different folders for your tests, fixtures, and support files, which is useful when you're fitting Cypress into an existing repository layout. If you're starting your first project, we recommend sticking with the defaults above so your setup matches our docs and examples.

You can change these paths in your configuration file. See the Cypress configuration reference for the full list of options.

info

What files should I add to my '.gitignore file' ?

Cypress may create asset files in a `downloadsFolder`, a `screenshotsFolder` or a `videosFolder` to store any downloads, screenshots or videos created during the testing of your application. Because these are generated artifacts rather than source, many users add these folders to their .gitignore file (see below for an example). Additionally, if you are storing sensitive variables in your Cypress configuration these should also be ignored when you check into source control.

### Spec files

Spec files are where your tests live. For end-to-end testing they're located in `cypress/e2e` by default, while component testing specs typically live next to the components they test anywhere in your project. Either way, you can configure a different location. To make adoption easy, Cypress lets you write specs in whichever flavor of JavaScript your team already uses:

- `.js`
- `.jsx`
- `.ts`
- `.tsx`
- `.coffee`

Cypress also supports `ES2015` out of the box. You can use either `ES2015 modules` or `CommonJS modules`, which means you can `import` or `require` both **npm packages** and **local relative modules** to share code across specs.

info

Example Recipe

Check out our recipe using ES2015 and CommonJS modules.

#### How Cypress finds your specs

Cypress doesn't treat every file in your test folder as a spec. It only loads files that match the `specPattern` glob, which by default requires the `.cy.` infix in the filename:

- **E2E:** `cypress/e2e/**/*.cy.{js,jsx,ts,tsx}`
- **Component:** `**/*.cy.{js,jsx,ts,tsx}`

This convention lets you keep helper files and specs side by side without Cypress trying to run your helpers as tests. The trade-off is that a file named `cypress/e2e/login.js` is **not** discovered, while `cypress/e2e/login.cy.js` is. If a test you've written isn't showing up, the filename almost always doesn't match `specPattern`, so that's the first thing to check. You can override `specPattern` in your configuration if you prefer a different naming convention.

If you still can't tell why a spec isn't being picked up, open or run Cypress with debug logs enabled to see exactly how it resolves spec files:

```shell
DEBUG=cypress:cli,cypress:data-context:sources:FileDataSource,cypress:data-context:sources:ProjectDataSource npx cypress open
```

info

How `specPattern`, `--spec`, and `excludeSpecPattern` work together

`specPattern` defines the full set of files Cypress *considers* to be specs. Two other options refine that set:

- `excludeSpecPattern` removes files from the set. Any file matching `specPattern` but also matching `excludeSpecPattern` is ignored, which is handy for hiding sample specs or a group of work-in-progress files.
- The `--spec` command line flag (and the `spec` Module API option) limits a single run to a subset of specs. It can only narrow what already matches `specPattern`, never add files outside it.

In short: `specPattern` is the master list, `excludeSpecPattern` subtracts from it, and `--spec` picks which of the remaining specs to run this time.

### Support file

The support file is your hook into every spec. It runs **before** every single spec file, which makes it the natural home for setup and behavior you want available everywhere, without importing it into each spec yourself. That's why it's the recommended place for custom commands and global overrides.

To control what loads first, set the `supportFile` path. By default it looks for:

- **E2E:** `cypress/support/e2e.{js,jsx,ts,tsx}`
- **Component:** `cypress/support/component.{js,jsx,ts,tsx}`

#### Execution

When Cypress runs a spec file via `cypress open` or `cypress run`, it loads the support file first and then the spec file.

#### supportFile per testing type

`supportFile` is configured separately for each testing type. Set it under the `e2e` key for end-to-end testing and under the `component` key for component testing in your Cypress configuration. For example, to override the default support file locations:

- cypress.config.js
- cypress.config.ts

```js
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
    supportFile: 'cypress/support/my-e2e-support.ts',
  },
  component: {
    supportFile: 'cypress/support/my-component-support.ts',
  },
})
```

```typescript
import { defineConfig } from 'cypress'

export default defineConfig({
  e2e: {
    supportFile: 'cypress/support/my-e2e-support.ts',
  },
  component: {
    supportFile: 'cypress/support/my-component-support.ts',
  },
})
```

#### Organizing imports

From your support file you can `import` or `require` other files to keep things organized as it grows.

caution

Keep your support file lean. Cypress bundles the support file and everything it imports, then loads that bundle **before every single spec file**, so the cost of anything you import there is paid on every spec run. Avoid importing large modules or anything that isn't needed for testing (especially Node.js-only code like database drivers or `fs`, which can't run in the browser). Import heavy or spec-specific code directly in the spec files that need it instead.

See Keep support and spec imports lean in the test performance guide for examples.

#### Global hooks

Because the support file runs first, it's a convenient place to define `before` or `beforeEach` behavior that should apply to every spec:

```javascript
beforeEach(() => {
  cy.log('I run before every test in every spec file!')
})
```

### Fixtures

Fixtures are external pieces of static data your tests can load on demand. Think of them as the canned data your tests run against. Keeping this data in its own file (rather than inline in the test) makes specs easier to read and lets you reuse the same data across many tests. Fixture files live in `cypress/fixtures` by default, but can be configured to another directory.

Cypress recognizes a range of fixture file types and parses or encodes each based on its extension: `.json`, `.js`, `.coffee`, `.html`, `.txt`, `.csv`, `.png`, `.jpg`, `.jpeg`, `.gif`, `.tif`, `.tiff`, and `.zip`. Any other extension is read as `utf8` unless you pass a different encoding. See `cy.fixture()` for the full encoding details.

There are a few ways to use a fixture:

- `cy.fixture()` loads the file's contents directly, most often when you're stubbing Network Requests so your tests don't depend on a live backend.
- A static `import`/`require` of a JSON fixture pulls the data into your spec at build time, e.g. `import user from '../fixtures/user.json'`.
- `cy.intercept()` can respond to a request straight from a fixture with the `fixture` option, e.g. `cy.intercept('GET', '/users', { fixture: 'users.json' })`.
- `.selectFile()` attaches a fixture to a file input when you're testing uploads.

### Node events (setupNodeEvents)

Your tests run in the browser, but some things, like touching the file system, talking to a database, or controlling how specs are bundled, can only happen in Node.js. Cypress lets you run that Node.js-side code through the `setupNodeEvents` function in your Cypress configuration, defined per testing type under the `e2e` or `component` options. It runs in the background Node.js process before the project is loaded, before the browser launches, and during your test run, and your tests reach it through the cy.task() command.

This is where you tap into Node events to do things like control how spec files are bundled with preprocessors, find and launch browsers via the browser launch API, and run other tasks that need access to the operating system. Read our plugins guide for details and examples.

### Generated assets

When a run produces artifacts (files your app downloaded, screenshots, or videos), Cypress saves them to dedicated folders so you can inspect what happened after the fact. Because these are regenerated on every run, you'll usually want to keep them out of source control. For example, using the default folder locations:

.gitignore

```
# Cypress asset folders to exclude from source control
cypress/downloads/
cypress/screenshots/
cypress/videos/
```

#### Downloads

Any files downloaded while testing an application's file download feature will be stored in the `downloadsFolder` which is set to `cypress/downloads` by default.

```
/cypress
  /downloads
    - records.csv
```

#### Screenshots

If screenshots were taken via the cy.screenshot() command or automatically when a test fails, the screenshots are stored in the `screenshotsFolder` which is set to `cypress/screenshots` by default.

```
/cypress
  /screenshots
    /app.cy.js
      - Navigates to main menu (failures).png
```

To learn more about screenshots and settings available, see Screenshots and Videos

#### Videos

Any videos recorded of the run are stored in the `videosFolder` which is set to `cypress/videos` by default.

```
/cypress
  /videos
    - app.cy.js.mp4
```

#### How asset file paths are generated

Screenshots and videos are saved inside their respective folders (`cypress/screenshots`, `cypress/videos`), and Cypress mirrors each spec's folder structure underneath so every asset lines up with the spec that produced it.

To keep those paths from getting needlessly deep, Cypress first removes the **common ancestor**: the longest folder path shared by *every* spec in the run (the specs matched by `specPattern`, or by the `--spec` flag / `spec` Module API option when you've narrowed the run). Only the part of each spec's path that is unique is kept.

One consequence is that the same spec can produce assets at different paths depending on which other specs ran alongside it, because adding or removing specs can change the shared ancestor. The examples below show how the kept portion of the path changes with the set of specs in the run: first a single end-to-end spec, then two colocated component specs.

**Example 1: a single spec in the run**

The spec's entire folder path is shared (there's nothing to compare it against), so only the filename remains:

- Spec file found
  - `cypress/e2e/path/to/file/one.cy.js`
- Common ancestor (calculated at runtime)
  - `cypress/e2e/path/to/file`
- Generated screenshot file
  - `cypress/screenshots/one.cy.js/your-screenshot.png`
- Generated video file
  - `cypress/videos/one.cy.js.mp4`

**Example 2: two component specs in the run**

Component specs usually sit right next to the components they test. Here the two specs only share `src/components/`, so the differing tail of each path (`Button/`, `inputs/Input/`) is preserved:

- Spec files found
  - `src/components/Button/Button.cy.tsx`
  - `src/components/inputs/Input/Input.cy.tsx`
- Common ancestor (calculated at runtime)
  - `src/components/`
- Generated screenshot files
  - `cypress/screenshots/Button/Button.cy.tsx/your-screenshot.png`
  - `cypress/screenshots/inputs/Input/Input.cy.tsx/your-screenshot.png`
- Generated video files
  - `cypress/videos/Button/Button.cy.tsx.mp4`
  - `cypress/videos/inputs/Input/Input.cy.tsx.mp4`

tip

**Want stable, predictable paths?** Rather than reconstructing where an asset landed, read the path Cypress actually used:

- `cy.screenshot()` reports the saved location to its `onAfterScreenshot` callback, and you can pass an explicit `name` to control the filename.
- The `after:screenshot` and `after:spec` Node events hand you the resolved `path` (and video path) after each screenshot or spec finishes.

If you still need the folder layout itself to be consistent, keep all your specs under a single common directory so the common ancestor doesn't shift as you add, remove, or filter specs.

#### Storing assets in Cypress Cloud

Managing these artifacts by hand gets tedious as a suite grows. Instead of administering assets yourself, you can save them to the cloud with Cypress Cloud.

Replay the test as it executed during the recorded run with full debug capability using (Replay Icon) Cypress Test Replay.

Screenshots and videos are attached to their respective test results and kept for the length of your data retention period, and are easily shared or browsed through our web interface. To learn more about videos and settings available, see Screenshots and Videos.

## Writing tests

Cypress is built on top of Mocha and Chai, two libraries the JavaScript community has relied on for years. Building on them rather than inventing a new test language means the syntax is already familiar and battle-tested: Cypress supports both Chai's `BDD` and `TDD` assertion styles, and your tests will mostly follow those conventions.

info

Prefer a low-code way to author tests? Cypress Studio generates test commands for you as you click and type in your app, so you can build up a spec without writing it by hand. Connect Cypress Cloud to also unlock **Studio AI**, which suggests assertions for you while you record.

### Test Structure

The test interface, borrowed from Mocha, provides `describe()`, `context()`, `it()` and `specify()`. You use `describe()`/`context()` to group related tests and `it()`/`specify()` to define an individual test, which keeps your specs readable and your test output organized.

`context()` is identical to `describe()` and `specify()` is identical to `it()`, so choose whatever terminology works best for you.

A typical spec groups related tests with `describe()` (optionally nesting `context()` blocks for sub-areas) and defines each individual test with `it()`:

```javascript
describe('Account settings', () => {
  beforeEach(() => {
    
    cy.visit('/account')
  })

  context('profile', () => {
    it('shows the current user name', () => {
      cy.get('[data-testid="profile-name"]').should('have.value', 'Jane Lane')
    })

    specify('saves an updated email address', () => {
      cy.get('[data-testid="email"]').clear().type('[email protected]')
      cy.get('[data-testid="save"]').click()
      cy.contains('Profile updated').should('be.visible')
    })
  })
})
```

### Assertion Styles

Cypress supports both BDD (`expect`/`should`) and TDD (`assert`) style plain assertions, so you can write assertions in whichever style your team prefers. Read more about plain assertions.

```javascript
it('asserts in BDD style with expect', () => {
  expect('Jane Lane').to.have.length(9)
})

it('asserts in TDD style with assert', () => {
  assert.lengthOf('Jane Lane', 9, 'name is 9 characters long')
})
```

The .should() command and its alias .and() can also be used to more easily chain assertions off of Cypress commands. Read more about assertions.

```js
cy.get('[data-testid="profile-name"]').should('have.value', 'Jane Lane')
```

### Hooks

Hooks (also borrowed from Mocha) let you run setup and teardown code around your tests instead of repeating it inside each one. Use them to establish the conditions a group of tests needs before they run, or to tidy up afterward.

```javascript
before(() => {
  
  
})

beforeEach(() => {
  
  
})

afterEach(() => {
  
})

after(() => {
  
})

describe('Hooks', () => {
  before(() => {
    
  })

  beforeEach(() => {
    
  })

  afterEach(() => {
    
  })

  after(() => {
    
  })
})
```

#### Hook and test execution order

- All `before()` hooks run (once)
- Any `beforeEach()` hooks run
- Tests run
- Any `afterEach()` hooks run
- All `after()` hooks run (once)

danger

🚨 Before writing `after()` or `afterEach()` hooks, please see our thoughts on the anti-pattern of cleaning up state with `after()` or `afterEach()`.

### Focusing and skipping tests

While developing, you rarely want to run the entire suite on every save. Cypress lets you focus on or skip specific tests so your feedback loop stays fast.

To run a specified suite or test, append `.only` to the function. All nested suites will also be executed. This gives you the ability to run one test at a time and is the recommended way to write a test suite.

```javascript
describe('Account settings', () => {
  
  it.only('updates the email address', () => {
    cy.get('[data-testid="email"]').clear().type('[email protected]')
    cy.get('[data-testid="save"]').click()
    cy.contains('Profile updated').should('be.visible')
  })

  it('updates the display name', () => {
    cy.get('[data-testid="profile-name"]').clear().type('Jane Lane')
    cy.get('[data-testid="save"]').click()
  })

  it('uploads a new avatar', () => {
    cy.get('[data-testid="avatar"]').selectFile('cypress/fixtures/avatar.png')
  })
})
```

To skip a specified suite or test, append `.skip()` to the function. All nested suites will also be skipped.

```javascript
it.skip('uploads a new avatar', () => {
  cy.get('[data-testid="avatar"]').selectFile('cypress/fixtures/avatar.png')
})
```

### Test Isolation

tip

**Best Practice:** Tests should always be able to be run independently from one another **and still pass**.

Tests that quietly depend on each other are a leading cause of flaky suites: a test passes only because an earlier test left the browser in a particular state, and the moment you reorder, skip, or run them in isolation, things break. As stated in our mission, we hold ourselves accountable to champion a testing process that actually works, and have built Cypress to guide developers toward writing independent tests from the start.

We do this by cleaning up test state and the browser context *before* each test so the actions of one test can't affect another. The goal for each test is to **reliably pass** whether it runs in isolation or alongside others, which removes a whole category of nondeterministic failures that are painful to debug.

The behavior of running tests in a clean browser context is called `testIsolation`.

Test isolation is **enabled by default** (`testIsolation: true`) and applies only to end-to-end testing. It is a global configuration and can be overridden for end-to-end testing at the `describe` level with the `testIsolation` option.

To learn more about this behavior and the trade-offs of disabling it, review our Test Isolation guide.

### Test Configuration

Sometimes a test or suite needs different settings than the rest of your project, such as a specific viewport, a particular browser, or a different retry count. Rather than changing global configuration, you can apply test configuration locally by passing a configuration object as the second argument to the test or suite function.

These values take effect only for the suite or tests where they're set, then revert to their previous defaults once those tests complete, so the override stays scoped and doesn't leak into the rest of your run.

#### Syntax

```javascript
describe(name, config, fn)
context(name, config, fn)
it(name, config, fn)
specify(name, config, fn)
```

#### Allowed config values

caution

**Note:** Some configuration values are readonly and cannot be changed via test configuration. Be sure to review the list of test configuration options.

#### Suite configuration

If you want to target a suite of tests to run or be excluded when run in a specific browser, you can override the `browser` configuration within the suite configuration. The `browser` option accepts the same arguments as Cypress.isBrowser().

The following suite of tests will be skipped if running tests in Chrome browsers.

```js
describe('When NOT in Chrome', { browser: '!chrome' }, () => {
  it('Shows warning', () => {
    cy.get('[data-testid="browser-warning"]').should(
      'contain',
      'For optimal viewing, use Chrome browser'
    )
  })

  it('Links to browser compatibility doc', () => {
    cy.get('a.browser-compat')
      .should('have.attr', 'href')
      .and('include', 'browser-compatibility')
  })
})
```

The following suite of tests will only execute when running in the Firefox browser. Additionally, it will overwrite the viewport resolution.

```js
describe(
  'When in Firefox',
  {
    browser: 'firefox',
    viewportWidth: 1024,
    viewportHeight: 700,
  },
  () => {
    it('Sets the expected viewport and API URL', () => {
      expect(cy.config('viewportWidth')).to.equal(1024)
      expect(cy.config('viewportHeight')).to.equal(700)
    })
  }
)
```

#### Single test configuration

You can configure the number of retry attempts during `cypress run` or `cypress open`. See Test Retries for more information.

```js
it('should redirect unauthenticated user to sign-in page', {
    retries: {
      runMode: 3,
      openMode: 2
    }
  } () => {
    
  })
})
```

#### Exposing public configuration to a suite or test

You can also pass an `expose` object so plugins can declare public configuration per suite or test, readable with `Cypress.expose()`. Use this only for non-sensitive values, since exposed configuration is accessible in the browser context.

### Dynamically generating tests

Because tests are just JavaScript, you can generate them programmatically. This keeps your specs DRY when you need to run the same assertions across a list of inputs: change the data and the tests follow, with no copy-paste.

```javascript
describe('if your app uses jQuery', () => {
  ;['mouseover', 'mouseout', 'mouseenter', 'mouseleave'].forEach((event) => {
    it('triggers event: ' + event, () => {
      
      
      cy.get('#with-jquery')
        .invoke('trigger', event)
        .get('[data-testid="messages"]')
        .should('contain', 'the event ' + event + 'was fired')
    })
  })
})
```

The code above will produce a suite with 4 tests:

```
> if your app uses jQuery
  > triggers event: 'mouseover'
  > triggers event: 'mouseout'
  > triggers event: 'mouseenter'
  > triggers event: 'mouseleave'
```

#### Driving tests from external data

A common use of dynamic tests is **data-driven testing**: keeping your test cases (and often their titles) in an external data source, then generating one test per row. The important constraint is that the `describe()`/`it()` structure is built **synchronously when the spec loads**. Cypress commands like `cy.fixture()` and `cy.task()` run *inside* a test and resolve asynchronously, so they can supply data **within** a test but cannot be used to create the `it()` blocks themselves. The data has to be available at load time.

For **JSON** data, a static `import`/`require` is all you need, since the bundler inlines it at build time:

```javascript
import scenarios from '../fixtures/scenarios.json'

describe('Login scenarios', () => {
  scenarios.forEach((scenario) => {
    it(scenario.title, () => {
      cy.visit('/login')
      cy.get('[data-testid="username"]').type(scenario.username)
      cy.get('[data-testid="password"]').type(scenario.password)
      cy.get('[data-testid="submit"]').click()
      cy.contains(scenario.expectedMessage).should('be.visible')
    })
  })
})
```

Each `it()` title comes straight from the data, so the row's `title` is what shows up in your test output.

For formats that need parsing in Node.js first, such as **CSV or Excel**, read and parse the file inside `setupNodeEvents` and hand the parsed rows to the browser with the `expose` configuration, then read them in your spec with `Cypress.expose()`. Use `expose` only for non-sensitive data, since exposed values are accessible in the browser context.

- cypress.config.js
- cypress.config.ts

```js
const { defineConfig } = require('cypress')

const { readFileSync } = require('fs')
const { parse } = require('csv-parse/sync')

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      const csv = readFileSync('cypress/fixtures/scenarios.csv', 'utf8')

      config.expose = {
        ...config.expose,
        scenarios: parse(csv, { columns: true }),
      }

      return config
    },
  },
})
```

```typescript
import { defineConfig } from 'cypress'

import { readFileSync } from 'fs'
import { parse } from 'csv-parse/sync'

export default defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      const csv = readFileSync('cypress/fixtures/scenarios.csv', 'utf8')

      config.expose = {
        ...config.expose,
        scenarios: parse(csv, { columns: true }),
      }

      return config
    },
  },
})
```

cypress/e2e/login.cy.js

```javascript
describe('Login scenarios', () => {
  Cypress.expose('scenarios').forEach((scenario) => {
    it(scenario.title, () => {
      
    })
  })
})
```

## Running and watching tests

You can run a test by clicking on the spec filename. For example the Cypress RealWorld App has multiple test files, but below we run the "new-transaction.spec.ts" test file by clicking on it.

### Watching tests

A big part of why Cypress feels productive is the tight feedback loop. When you run with cypress open, Cypress watches the filesystem for changes to your spec files. Soon after you add or update a test, Cypress reloads it and re-runs every test in that spec file, so you can write tests as you build a feature and the UI always reflects your latest edits, with no manual re-run.

#### What is watched?

**Files**

- Cypress configuration
- cypress.env.json

**Spec files**

Cypress watches your entire project root for spec files. Any file that matches your `specPattern`, wherever it lives in the project, is detected. When a change is made, the active spec file, the support file, and any files they `import` (or `require`) are recompiled through the preprocessor and the browser reloads.

#### What isn't watched?

Files that aren't part of the spec graph; this includes, but isn't limited to, the following:

- Your application code
- `node_modules`
- `cypress/fixtures/`

Your application code is intentionally left out: if you're developing with a modern JS-based stack, you likely already have some form of hot module replacement watching your application code (HTML, CSS, JS, etc.) and reloading it in response to changes, so Cypress doesn't duplicate that work.

#### Disable file watching

Set the `watchForFileChanges` configuration property to `false` to disable file watching:

- cypress.config.js
- cypress.config.ts

```js
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  watchForFileChanges: false,
})
```

```typescript
import { defineConfig } from 'cypress'

export default defineConfig({
  watchForFileChanges: false,
})
```

info

This only applies to cypress open. **Nothing** is watched during cypress run, so the `watchForFileChanges` property has no effect there.

#### The default preprocessor

The component responsible for the file-watching behavior in Cypress is the `@cypress/webpack-batteries-included-preprocessor`. This is the default preprocessor packaged with Cypress and is registered automatically when you don't provide your own `file:preprocessor` event. It builds on the lower-level `webpack-preprocessor` and bundles the loaders and configuration needed to give you TypeScript and JSX support out of the box with zero configuration. That zero-config support is the reason most projects never have to think about bundling at all.

If you need further control of the file-watching behavior you can configure this preprocessor explicitly: it exposes options that allow you to configure behavior such as *what* is watched and the delay before emitting an "update" event after a change.

Cypress also ships other file-watching preprocessors - you'll have to configure these explicitly if you want to use them.

- `@cypress/webpack-preprocessor`

## Understanding test results

Once a spec finishes, knowing how to read its results is what turns a run into actionable feedback. Every test ends in one of four statuses: **passed**, **failed**, **pending**, or **skipped**. These statuses are inherited from Mocha, the test runner Cypress is built on.

### Passed

Passed tests have successfully completed all their hooks and commands without failing any assertions. The test screenshot below shows a passed test:

Note that a test can pass after several test retries. In that case the Command Log shows some failed attempts, but ultimately the entire test finishes successfully.

### Failed

A failed hook or test means an assertion didn't pass or a command errored. That's the test doing its job: catching the problem in your suite before it reaches a user.

After a test fails, the Test Replay or screenshots and videos with Cypress Cloud can help find the problem so it can be fixed.

### Pending

A **pending** test is one that Cypress intentionally doesn't run because you told it not to. A test ends up pending in three ways:

- **It has no body**: a placeholder for a test you haven't written yet, such as `it('is not written yet')`.
- **It's explicitly skipped**: using `it.skip()` or the `xit()` alias.
- **It's excluded from the current browser**: a test configured with the `browser` option to run only in a browser you aren't currently using.

Each of the four tests below is pending (the browser-specific one is pending whenever the run isn't using Chrome):

```js
describe('TodoMVC', () => {
  it('is not written yet')

  it.skip('adds 2 todos', function () {
    cy.visit('/')
    cy.get('[data-testid="new-todo"]').as('new').type('learn testing{enter}')

    cy.get('@new').type('be cool{enter}')

    cy.get('[data-testid="todo-list"] li').should('have.length', 100)
  })

  xit('another test', () => {
    expect(false).to.true
  })

  it('only test chrome', { browser: 'chrome' }, () => {
    cy.visit('/')
    cy.contains('To Do')
  })
})
```

In each case you've knowingly told Cypress to hold off, so it reports the test as pending rather than passed or failed.

### Skipped

Unlike a pending test, which you deliberately leave out, a **skipped** test is one Cypress *meant* to run but couldn't because a shared hook failed.

Imagine a block of tests that all share a `beforeEach` hook, and that hook errors. For example, it visits a page that doesn't exist:

```js
beforeEach(() => {
  cy.visit('/does-not-exist')
})
```

The hook fails before the first test can run, so that test is marked **failed**. Because the same hook would fail identically for every other test in the block, Cypress doesn't re-run it; it marks the remaining tests as **skipped** instead.

Collapsing the command log shows the empty box next to the skipped test "adds 2 todos":

In short, a test is skipped when a `before`, `beforeEach`, or `afterEach` hook fails and prevents the tests that depend on it from running.

## See also

- Cypress Best Practices
- Retry-ability
- Variables and Aliases
- The Command Line
- Configuration
- Test Replay

## Contents
