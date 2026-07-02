---
title: "Why Cypress? End-to-end, component & accessibility testing"
source: https://docs.cypress.io/guides/overview/why-cypress
domain: cypress-e2e
license: CC-BY-SA-4.0
tags: cypress testing, end-to-end testing, web testing, browser tests
fetched: 2026-07-02
---

# Why Cypress?

info

##### What you'll learn

- What Cypress does, and where it fits as your team grows
- How Cypress reduces the cost and risk of shipping software
- The features of Cypress App, Cypress Cloud, UI Coverage, and Cypress Accessibility
- Our mission and what we believe in
- Key differences between Cypress and other testing tools

## What is Cypress?

Cypress is a quality platform for teams shipping modern web applications. We bring together end-to-end testing, component testing, accessibility checks, and a clear view of test coverage into a connected workflow that runs locally and in CI, so you can catch problems before your users do.

Most teams come to Cypress looking for a better way to write tests for their front end. They stay because, as the team and the application grow, **Cypress does more than a testing tool would.**

The same platform helps a single developer write their first test, a QA team manage thousands of specs, an accessibility partner track regressions, and an engineering lead see whether a release is safe to ship.

**What you write in Cypress becomes part of how your team ships software.** Tests run while you build. Results flow into CI. Failures, flake patterns, accessibility issues, and untested areas of your app surface in one place the whole team can act on.

**By the time a change is ready to merge, your team should already know whether it's safe to ship.** That's how Cypress reduces the cost and risk of releasing software: fewer surprises in production, fewer hours lost to test maintenance, and a release cadence you can trust.

Cypress provides solutions for:

- End-to-end testing
- Component testing
- Accessibility testing
- UI Coverage
- and more...

Cypress can test anything that runs in a browser and surface insights into how to improve the health of your test suite and the quality of your application.

## Products

- Cypress App, a free, open source, locally installed app for writing and running tests.
- Cypress Cloud, a paid service for recording tests, surfacing test results, and providing test analytics.
- UI Coverage, a premium solution providing a visual overview of test coverage across every page and component of your app, offering clear insights into uncovered areas that everyone can understand.
- Cypress Accessibility, a premium solution providing accessibility checks, which helps detect barriers for people with disabilities using your application.

## How Cypress grows with your team

**Install the Cypress app and start writing tests as you build.** The app is free and open source.

This is where the day-to-day cost of testing lives. Most teams spend more time debugging broken tests than writing new ones, and most of that time goes to one question: what was the state of the app when the test failed?

Cypress is built around making that question fast to answer:

- **Time Travel** snapshots let you replay every step of a test locally instead of guessing.
- **Automatic waiting** removes the timing logic that other tools require you to hand-write and maintain.
- **Studio AI** records interactions and suggests assertions, so you spend less time authoring boilerplate.

Less time on test maintenance is more time shipping features.

### Move to CI with Cypress Cloud

**When you start running Cypress in your CI pipeline, new problems show up.** Tests pass locally and fail in CI. Someone marks a test as flaky and a week later three more are flaky. Engineers burn afternoons digging through CI logs. Your team lead asks "are we good to merge?" and nobody has a confident answer.

Cypress Cloud replaces guesswork with evidence:

- **Test Replay** allows you to replay the test exactly as it executed during the run for zero-configuration debugging.
- **Flaky test management** surfaces flake patterns so they get fixed instead of quietly suppressed.
- **Branch Review** gives every pull request a pre-merge picture of the test signal, so "are we good to merge?" has a real answer before code lands on main.
- **Smart Orchestration** keeps CI fast as your suite grows by parallelizing specs, prioritizing the ones most likely to fail, and canceling builds that are clearly broken.

Faster, more trustworthy CI is the difference between a team that ships every day and a team that ships when they get lucky.

If your team uses AI coding assistants, Cloud MCP gives them the same run and failure context inside your IDE. You'll never have to wonder: *Why did this fail?*

### Scale quality with premium products

**As your application grows, two harder questions arrive.** Have we actually tested everything that matters? Is what we're shipping accessible to everyone trying to use it?

The stakes grow with the questions. Accessibility issues caught in development cost a few hours of engineering time. The same issues caught by a compliance review, a procurement gate, or a public complaint cost a great deal more. Coverage gaps that hide in plain sight turn into the production incidents that derail your roadmap.

Two premium products meet this stage:

- **Cypress Accessibility** surfaces accessibility issues continuously during your normal test runs, with no setup, code changes, or performance penalty. Issues get caught in development rather than after launch.
- **UI Coverage** gives engineers, product, and QA a single shared view of which parts of your app your tests reach and which they don't.

## Features

Below are some of the key features of each product.

### Cypress App

*The day-to-day cost of testing lives in your local dev loop. The Cypress app is built to keep that loop short.*

- **Time Travel:** Cypress takes snapshots as your tests run. Hover over commands in the Command Log to see exactly what happened at each step.
- **Debuggability:** Stop guessing why your tests are failing. Debug directly from familiar tools like Developer Tools. Our readable errors and stack traces make debugging lightning fast.
- **Automatic Waiting:** Never add waits or sleeps to your tests. Cypress automatically waits for commands and assertions before moving on. No more async hell.
- **Spies, Stubs, and Clocks:** Verify and control the behavior of functions, server responses, or timers. The same functionality you love from unit testing is right at your fingertips.
- **Network Traffic Control:** Easily control, stub, and test edge cases without involving your server. You can stub network traffic however you like.
- **Consistent Results:** Our architecture doesn't use Selenium or WebDriver. Say hello to fast, consistent and reliable tests that are flake-free.
- **Cypress Studio & Studio AI:** Record interactions in your app to generate and extend E2E tests, and let Studio AI recommend assertions automatically so you write less and cover more.
- **Cross Browser Testing:** Run tests within Firefox and Chrome-family browsers (including Edge and Electron) locally and in a Continuous Integration pipeline.

### Cypress Cloud

*Cypress Cloud turns CI test results from something you hope to interpret correctly into a signal your whole team can act on.*

- **Test Replay:** Record to Cypress Cloud and replay the test exactly as it executed during the run for zero-configuration debugging using Test Replay.
- **Smart Orchestration:** Once you're set up to record to Cypress Cloud, easily parallelize your test suite, rerun failed specs first with Spec Prioritization, and cancel test runs on failures with Auto Cancellation for tight feedback loops.
- **Flake Detection:** Discover and diagnose unreliable tests with Cypress Cloud's Flaky test management.
- **Branch Review:** Quickly identify the impact a pull request might have on your test suite in a single view using Branch Review. Compare which tests are failing, flaky, pending, added, or modified between the source and base branches and prevent the merging of low-quality code.
- **Integrations:** Integrate with GitHub, GitLab, or Bitbucket to see test results directly on every push or pull request. Cypress Cloud also integrates with Slack, Jira, and Microsoft Teams to keep your team in the loop.
- **Test Analytics:** Track test results over time with Test Analytics to identify trends, regressions, and improvements in your test suite. Use our Data Extract API to extract the data that is important to your team.
- **Cypress Cloud MCP** : Give AI coding assistants a direct window into your application's health and stability without leaving your IDE by connecting to Cypress Cloud MCP.

### Cypress Accessibility

*Accessibility issues caught during testing are cheap to fix. The same issues caught by a compliance review, a procurement gate, or a user complaint are not.*

- **Accessibility Checks:** Maximize the value of your existing Cypress tests by instantly adding thousands of accessibility checks with no setup, code changes, or performance penalty.
- **Run-level reports:** Get a detailed report of accessibility issues found in your test runs with Run-level reports.
- **Results where you work:** Use the Results API to integrate results into CI, and Cloud MCP to surface them in your AI agent for faster diagnosis and iteration.
- **Branch Review:** Compare any report against a baseline to review only the new violations, without any noise from existing issues.

### UI Coverage

*You can't act on coverage gaps you can't see. UI Coverage makes them visible to the whole team.*

- **Visualize Coverage:** UI Coverage provides a visual overview of test coverage across every page and component of your app, offering clear insights into uncovered areas that everyone can understand.
- **Results where you work:** Use the Results API to integrate results into CI, and Cloud MCP to surface them in your AI agent for faster diagnosis and iteration.
- **Branch Review:** Compare runs to see newly introduced elements in your application or unexpected reductions in test coverage.

## Solutions

Cypress can be used to ensure several different types of tests. Used together, they give you broader, more dependable coverage before release.

### End-to-end Testing

Cypress was originally designed to run end-to-end (E2E) tests on anything that runs in a browser. A typical E2E test visits the application in a browser and performs actions via the UI just like a real user would. They catch the failures your users would actually see, which is what makes them so valuable in the moments before code ships.

```js
it('adds todos', () => {
  cy.visit('https://example.cypress.io/')
  cy.get('[data-cy="new-todo"]').type('write tests{enter}')
  
  cy.get('[data-cy="todos"]').should('have.length', 1)
})
```

### Component Testing

Cypress Component Testing mounts your components directly in a real browser, giving you a live, visual workbench to build and test components from any front-end UI library — no matter how simple or complex. Because tests run in the same environment your users experience, you catch rendering issues, interaction bugs, and edge cases before they ever reach end-to-end testing or production.

Learn more about how to test components for React, Angular, Vue, and Svelte.

- React
- Angular
- Vue
- Svelte

```ts
import Button from './Button'

it('uses custom text for the button label', () => {
  cy.mount(<Button>Click me!</Button>)
  
  cy.get('button').should('contains.text', 'Click me!')
})
```

```ts
import ButtonComponent from './button.component'

it('uses custom text for the button label', () => {
  cy.mount('<app-button>Click me!</app-button>', {
    declarations: [ButtonComponent],
  })
  
  cy.get('button').should('contains.text', 'Click me!')
})
```

```ts
import Button from './Button.vue'

it('uses custom text for the button label', () => {
  cy.mount(Button, {
    slots: {
      default: 'Click me!',
    },
  })
  
  cy.get('button').should('contains.text', 'Click me!')
})
```

```ts
import Button from './Button.svelte'

it('uses custom text for the button label', () => {
  cy.mount(Button, { props: { msg: 'Click me!' } })
  
  cy.get('button').should('contains.text', 'Click me!')
})
```

### Accessibility Testing

You can write Cypress tests to check the accessibility of your application, and use plugins to run broad accessibility scans. When combined with Cypress Accessibility in Cypress Cloud, insights can be surfaced when specific accessibility standards are not met through your testing, with no configuration required. See our Accessibility Testing guide for more details.

```js
it('adds todos', () => {
  cy.visit('https://example.cypress.io/')
  cy.get('img#logo')
    
    .should('have.attr', 'alt', 'Cypress Logo')
})
```

### UI Coverage

You can increase release confidence by closing testing gaps in critical app flows using UI Coverage. Use data-driven insights to cover untested areas, reduce incidents, and improve app quality across the team.

### Other

Cypress can perform arbitrary HTTP calls, thus you can use it for API testing.

```js
it('adds a todo', () => {
  cy.request('POST', '/todos', { title: 'Write API Tests' })
    .its('body')
    .should('contain', { title: 'Write API Tests' })
})
```

And through a large number of official and 3rd party plugins you can write many other types of tests!

## Our mission

Our mission is to build a thriving testing solution that enhances productivity, makes testing an enjoyable experience, and generates developer happiness. We hold ourselves accountable to champion a testing process **that actually works**.

We believe our documentation should be approachable. This means enabling our readers to understand fully not just the **what** but the **why** as well.

We want to help developers build a new generation of modern applications faster, better, and without the stress and anxiety associated with managing tests. We aim to elevate the art of software development by leveraging test results to generate actionable insights for long-term stability by proactively identifying areas for improvement.

We know that in order for us to be successful we must enable, nurture, and foster an ecosystem that thrives on open source. Every line of test code is an investment in **your codebase**, it will never be coupled to us as a paid service or company. Tests will be able to run and work independently, *always*.

We believe testing needs a lot of ❤️ and we are here to build a tool, a service, and a community that everyone can learn and benefit from. We're solving the hardest pain points shared by every developer working on the web. We believe in this mission and hope that you will join us to make Cypress a lasting ecosystem that makes everyone happy.

## Key Differences

### Architecture

Most testing tools (like Selenium) operate by running outside of the browser and executing remote commands across the network. *Cypress is the exact opposite.* Cypress is executed in the same run loop as your application.

Behind Cypress is a Node server process. Cypress and the Node process constantly communicate, synchronize, and perform tasks on behalf of each other. Having access to both parts (front and back) gives us the ability to respond to your application's events in real time, while at the same time work outside of the browser for tasks that require a higher privilege.

Cypress ultimately controls the entire automation process from top to bottom, which puts it in the unique position of being able to understand everything happening in and outside of the browser. This means Cypress is capable of delivering more consistent results than any other testing tool.

Because Cypress is installed locally on your machine, it can additionally tap into the operating system for automation tasks. This makes performing tasks such as taking screenshots, recording videos, general file system operations and network operations possible.

### Native access

Because Cypress operates within your application, that means it has native access to every single object. Whether it is the `window`, the `document`, a DOM element, your application instance, a function, a timer, a service worker, or anything else - you have access to it in your Cypress tests.

For instance you can:

- Stub the browser or your application's functions and force them to behave as needed in your test case.
- Expose data stores so you can programmatically alter the state of your application directly from your test code.
- Test edge cases like 'empty views' by forcing your server to send empty responses.
- Test how your application responds to errors on your server by modifying response status codes to be 500.
- Modify DOM elements directly - like forcing hidden elements to be shown.
- Use 3rd party plugins programmatically. Instead of fussing with complex UI widgets like multi selects, autocompletes, drop downs, tree views or calendars, you can call methods directly from your test code to control them.
- Prevent Google Analytics from loading *before* any of your application code executes when testing.
- Get synchronous notifications whenever your application transitions to a new page or when it begins to unload.
- Control time by moving forward or backward so that timers or polls automatically fire without having to wait for the required time in your tests.
- Add your own event listeners to respond to your application. You could update your application code to behave differently when under tests in Cypress. You can control WebSocket messages from within Cypress, conditionally load 3rd party scripts, or call functions directly on your application.
- For Component Tests, Cypress is browser-based, allowing you to test not only your component's functionality but also styles and appearance. You can visually see your component in action and interact with it in the app.

### Shortcuts

Cypress allows for browser context to be cached with `cy.session()`. This means as a user, you only need to perform authentication once for the entirety of your test suite, and restore the saved session between each test. That means you do not have to visit a login page, type in a username and password and wait for the page to load and/or redirect for every test you run. You can accomplish this once with `cy.session()` and if needed, `cy.origin()`.

### Flake resistant

Flake is one of the largest hidden costs in any test suite. Reducing it is one of the most direct ways Cypress keeps a suite trustworthy over time.

Cypress knows and understands everything that happens in your application synchronously. It is notified the moment the page loads and the moment the page unloads. Cypress even knows how fast an element is animating and will wait for it to stop animating. Additionally, it automatically waits for elements to become visible, to become enabled, and to stop being covered. When pages begin to transition, Cypress will pause command execution until the following page is fully loaded. You can also tell Cypress to wait on specific network requests to finish.

### Debuggability

Above all else Cypress is built for usability.

- There are hundreds of custom error messages describing the exact reason Cypress failed your test.
- There is a rich UI which visually shows you the command execution, assertions, network requests, spies, stubs, page loads, or URL changes.
- The Cypress App takes snapshots of your application and enables you to time travel back to the state it was in when commands ran.
- You can use the Developer Tools while your tests run to see every console message or network request. You can inspect elements and use debugger statements in your spec or application code - you can use all the tools you're already comfortable with. This enables you to test and develop all at the same time.

### Trade offs

While there are many new and powerful capabilities of Cypress - there are also important trade-offs that we've made in making this possible.

If you're interested in understanding more, we've written an entire guide on this topic.

## Get Started

Install Cypress so you can quickly see your first passing test within minutes for End-to-end tests or Component tests.

## Cypress in the Real World

Cypress makes it quick and easy to start testing, and as you begin to test your app, **you'll often wonder if you're using best practices or scalable strategies**.

To guide the way, the Cypress team has created the Real World App (RWA), a full stack example application that demonstrates testing with **Cypress in practical and realistic scenarios.**

The RWA achieves full code-coverage with end-to-end tests across multiple browsers and device sizes, but also includes visual regression tests, API tests, unit tests, and runs them all in an efficient CI pipeline. Use the RWA to **learn, experiment, tinker, and practice** web application testing with Cypress.

The app is bundled with everything you need, just clone the repository and start testing.

## See also

- Install Cypress so you can quickly see your first passing test within minutes for
- Migrate from Playwright
- Migrate from Selenium
- Migrate from Protractor

## Contents
