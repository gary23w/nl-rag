---
title: "Cypress API: Table of Contents"
source: https://docs.cypress.io/api/table-of-contents
domain: cypress-e2e
license: CC-BY-SA-4.0
tags: cypress testing, end-to-end testing, web testing, browser tests
fetched: 2026-07-02
---

# Cypress API: Table of Contents

Cypress App

# Table of Contents

## Commands

Cypress commands don't do anything at the moment they are invoked, but rather enqueue themselves to be run later. Commands can be chained together because Cypress manages a Promise chain on your behalf, with each command yielding a 'subject' to the next command, until the chain ends or an error is encountered.

Learn more about how commands chain together in the Introduction to Chains of Commands.

Cypress commands can be classified one of the following

- `query` - commands that read the state of your application
- `assertion` - command which assert on a given state
- `action` - interact with your application as a user would
- `other` - any other command that is useful for writing tests

The differences between queries and other commands are outline in the Retry-ability Guide.

### Queries

Queries are Cypress commands that read the state of your application. They return a subject for further commands to act or assert on, and retry as needed to make sure the DOM element or other data they yield is always up to date.

| Command | Usage |
|---|---|
| `.as()` | Assign an alias for later use. Reference the alias later within a `cy.get()` query or `cy.wait()` command. |
| `.children()` | Get the children of each element within a set of DOM elements. |
| `.closest()` | Get the first ancestral element that matches a selector. |
| `.contains()` | Select a DOM element by text content. |
| `.document()` | Get the `window.document` of the active page. |
| `.eq()` | Select a DOM element by index from a collection. |
| `.filter()` | Filter elements with a selector. |
| `.find()` | Find descendent elements with a selector. |
| `.first()` | Select the first item in a collection. |
| `.focused()` | Get the DOM element that is currently focused. |
| `.get()` | Find DOM elements by selector, or read an alias previously created with the `.as()` command. |
| `.hash()` | Get the URL hash of the active page. |
| `.invoke()` | Invoke a function on the previously yielded subject. |
| `.its()` | Get a property's value on the previously yielded subject. |
| `.last()` | Select the last item in a collection. |
| `.location()` | Get the `window.location` object of the active page. |
| `.next()` | Get the next sibling element. |
| `.nextAll()` | Get all following sibling elements. |
| `.nextUntil()` | Get all following sibling elements until reaching a selector. |
| `.not()` | Filter selected elements with a selector. |
| `.parent()` | Get the parent of a DOM element. |
| `.parents()` | Get all parent elements of a DOM element. |
| `.parentsUntil()` | Get all parent elements up to a selector. |
| `.prev()` | Get the previous sibling element. |
| `.prevAll()` | Get all previous sibling elements. |
| `.prevUntil()` | Get all following previous sibling elements until reaching a selector. |
| `.root()` | Get the root DOM element. |
| `.shadow()` | Traverse into the shadow DOM of an element. |
| `.siblings()` | Get all sibling elements. |
| `.title()` | Get the `document.title` property of the active page. |
| `.url()` | Get the URL of the active page. |
| `.window()` | Get the `window` object of the active page. |

### Assertions

Assertions are Cypress commands that assert on the state of your application. They pause your test until the given condition is met, or until they time out. Learn more about Cypress assertions in the Introduction to Assertions and the Assertions Reference.

| Command | Usage |
|---|---|
| `.and()` | Alias for `.should(). Assert on the state of your application`. |
| `.should()` | Assert on the state of your application. Assertions are automatically retried until they pass or time out. |

### Actions

Actions are Cypress commands that interact with your application as a user would. They wait for elements to be actionable before interacting with the page.

Learn more about action commands in our Actionability Guide.

| Command | Usage |
|---|---|
| `.check()` | Check checkbox or radio elements. |
| `.clear()` | Clear the value of an input or textarea. |
| `.click()` | Click a DOM element. |
| `.dblclick()` | Double-click a DOM element. |
| `.rightclick()` | Right click a DOM element. |
| `.scrollIntoView()` | Scroll an element into view. |
| `.scrollTo()` | Scroll to a specific position. |
| `.select()` | Select an `<option>` within a `<select>`. |
| `.selectFile()` | Selects a file in an HTML5 input element, or simulates dragging a file into the browser. |
| `.trigger()` | Trigger an event on a DOM element. |
| `.type()` | Type into a DOM element. |
| `.uncheck()` | Uncheck checkbox(es). |

### Other Commands

Cypress has a variety of additional commands to help write tests.

| Command | Usage |
|---|---|
| `.blur()` | Blur a focused element. Blur is not an action command, because users cannot directly unfocus an element, only focus a new one, but `.blur()` can be used as a testing shortcut. |
| `.clearAllCookies()` | Clear all browser cookies. |
| `.clearAllLocalStorage()` | Clear `localStorage` data for all origins with which the test has interacted. |
| `.clearAllSessionStorage()` | Clear `sessionStorage` data for all origins with which the test has interacted. |
| `.clearCookie()` | Clear a specific browser cookie. |
| `.clearCookies()` | Clear browser cookies for a domain. |
| `.clearLocalStorage()` | Clear data in `localStorage` for current domain and subdomain. |
| `.clock()` | Override the browser's built-in time objects (`Date`, `setTimeout` and similar), allowing them to be controlled via `cy.tick()`. |
| `.debug()` | Set a `debugger` statement and log what the previous command yields. |
| `.each()` | Invoke a callback on each item in an array. |
| `.end()` deprecated | Explicitly end a chain of Cypress commands. |
| `.env()` | Access secret environment variables in your tests. |
| `.exec()` | Execute a system command. |
| `.fixture()` | Load a fixed set of data from disk. |
| `.focus()` | Focus on a DOM element. Focus is not an action command, because users cannot directly focus an element, but `.focus()` can be used as a testing shortcut. |
| `.getAllCookies()` | Get all browser cookies. |
| `.getAllLocalStorage()` | Get `localStorage` data for all origins with which the test has interacted. |
| `.getAllSessionStorage()` | Get `sessionStorage` data for all origins with which the test has interacted. |
| `.getCookie()` | Get a browser cookie by its name. |
| `.getCookies()` | Get browser cookies for the current domain or a specified domain. |
| `.go()` | Navigate back or forward using the browser's history. |
| `.hover()` | Cypress does not have a cy.hover() command. See Issue #10. |
| `.intercept()` | Spy and stub network requests and responses. |
| `.log()` | Print a message to the Cypress Command Log. |
| `.mount()` | Mount a component for Cypress Component Testing. |
| `.origin()` | Visit multiple domains of different origin in a single test. |
| `.pause()` | Pause test execution, allowing interaction with the application under test before resuming. |
| `.press()` | Trigger native key events in your application to simulate real user keyboard interactions. |
| `.prompt()` | Use natural language to generate Cypress tests with AI. |
| `.readFile()` | Read a file from disk. |
| `.reload()` | Reload the page. |
| `.request()` | Make an HTTP request. |
| `.screenshot()` | Take a screenshot of the application under test. |
| `.session()` | Cache and restore cookies, localStorage, and sessionStorage (i.e. session data) in order to recreate a consistent browser context between tests. |
| `.setCookie()` | Set a browser cookie. |
| `.spread()` | Invoke a callback function with multiple arguments. Similar to `.then()`. |
| `.spy()` | Wrap a method in a spy in order to record calls to the function. |
| `.stub()` | Replace a method, record its usage and control its behavior. |
| `.submit()` | Submit a form. |
| `.task()` | Execute code in Node via the `task` plugin event. |
| `.then()` | Invoke a callback function with the current subject, allowing you to execute code at specific points during a Cypress test. |
| `.tick()` | Move time after overriding a native time functions with `cy.clock()`. |
| `.viewport()` | Control the size and orientation of the screen for your application. |
| `.visit()` | Visit a remote URL. Many tests begin with this command. |
| `.wait()` | Wait a number of milliseconds, or wait for an aliased resource to resolve. |
| `.within()` | Scopes all subsequent cy commands to within this element. Useful when working within a particular group of elements such as a `<form>`. |
| `.wrap()` | Yield the object passed into `.wrap()`. If the object is a promise, yield its resolved value. |
| `.writeFile()` | Write to a file with the specified contents. |

## Cypress API

### Events

Cypress emits a series of events as it runs in your browser. These events are useful not only to control your application's behavior, but also for debugging purposes. Learn more about them in the Catalog of Events.

### Custom Commands and Queries

Cypress exposes interfaces to write Custom Commands and Custom Queries. See those pages for more details.

The Cypress community has created a large number of

Command Plugins which you can install or download.

### APIs

Cypress exposes a number of properties and methods on the global `Cypress` object.

The *key* difference between Cypress APIs and Cypress commands is that Cypress APIs execute the moment they are invoked and are **not** enqueued to run at a later time.

| Property | Usage |
|---|---|
| `Cypress.arch` | CPU architecture name of the underlying OS, as returned from Node's `os.arch()`. |
| `Cypress.browser` | Information about the current browser, such as browser family and version. |
| `Cypress.Commands` | Create new custom commands and extend or override existing ones. |
| `Cypress.config()` | Get and set Cypress configuration from inside your tests. |
| `Cypress.Cookies.debug()` | Generate console logs whenever a cookie is modified. |
| `Cypress.currentRetry` | A number representing the current test retry count. |
| `Cypress.currentTest` | An object with information about the currently executing test. |
| `Cypress.log` | This is the internal API for controlling what gets printed to the Command Log. Useful when writing your own custom commands. |
| `Cypress.dom` | A collection of DOM related helper methods. |
| `Cypress.ElementSelector` | Configure selector priority used by Cypress Studio and cy.prompt(). |
| `Cypress.env` deprecated | Get environment variables from inside your tests. |
| `Cypress.expose` | Expose configuration values to the browser context. |
| `Cypress.isBrowser()` | Checks if the current browser matches the given name or filter. |
| `Cypress.isCy()` | checks if a variable is a valid instance of cy or a cy chainable. |
| `Cypress.Keyboard.defaults()` | Set default values for how the `.type()` command is executed. |
| `Cypress.platform` | The underlaying OS name, as returned by Node's `os.platform()`. |
| `Cypress.require` | Enables utilizing dependencies within the cy.origin() callback function. |
| `Cypress.Screenshot.defaults()` | Set defaults for screenshots captured by the `.screenshot()` command and the automatic screenshots taken during test failures. |
| `Cypress.session` | A collection of helper methods related to the `.session()` command. |
| `Cypress.spec` | An object with information about the currently executing spec file. |
| `Cypress.testingType` | The current testing type, eg. `"e2e"` or `"component". |
| `Cypress.version` | The current Cypress version. |

## Utilities

Cypress makes several common libraries available directly on the global `Cypress` object.

| Utility | Usage |
|---|---|
| `Cypress.$` | Cypress automatically includes jQuery and exposes it as `Cypress.$`. |
| `Cypress.Blob` | Cypress automatically includes a Blob library and exposes it as `Cypress.Blob`. |
| `Cypress.Buffer` | Cypress automatically includes a Buffer polyfill for the browser and exposes it as `Cypress.Buffer`. |
| `Cypress._` | Cypress automatically includes lodash and exposes it as `Cypress._`. |
| `Cypress.minimatch` | Cypress automatically includes minimatch and exposes it as `Cypress.minimatch`. |
| `Cypress.Promise` | Cypress automatically includes `Bluebird` and exposes it as `Cypress.Promise`. |
| `Cypress.sinon` | Cypress automatically includes Sinon.JS and exposes it as `Cypress.sinon`. |

## Node Events

The Node Events allow you to hook into and extend Cypress behavior. For more details, see the How to use a Plugin and Node Events Overview.

| API | Usage |
|---|---|
| After Run Event | The `after:run` event fires after a run is finished. When running cypress via cypress open, the event will fire when closing a project. |
| After Screenshot Event | After a screenshot is taken, you can get details about it via the `after:screenshot` plugin event. |
| After Spec Event | The `after:spec` event fires after a spec file is run. When running cypress via cypress open, the event will fire when the browser closes. |
| Before Run Event | The `before:run` event fires before a run starts. When running cypress via cypress open, the event will fire when opening a project. |
| Before Spec Event | The `before:spec` event fires before a spec file is run. When running cypress via cypress open, the event will fire when the browser launches. |
| Browser Launch API | Before Cypress launches a browser, it gives you the opportunity to modify the browser preferences, install extensions, add and remove command-line arguments, and modify other options from the `setupNodeEvents` function. |
| Configuration API | Cypress enables you to dynamically modify configuration values and environment variables from your Cypress configuration. |
| Preprocessors API | A preprocessor is the plugin responsible for preparing a support file or a test file for the browser. A preprocessor also typically watches the source files for changes, processes them again, and then notifies Cypress to re-run the tests. |

## Contents
