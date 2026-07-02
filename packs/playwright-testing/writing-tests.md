---
title: "Writing tests"
source: https://playwright.dev/docs/writing-tests
domain: playwright-testing
license: CC-BY-SA-4.0
tags: playwright testing, browser automation, end-to-end testing, web locators
fetched: 2026-07-02
---

# Writing tests

## Introduction

Playwright tests are simple: they **perform actions** and **assert the state** against expectations.

Playwright automatically waits for actionability checks to pass before performing each action. You don't need to add manual waits or deal with race conditions. Playwright assertions are designed to describe expectations that will eventually be met, eliminating flaky timeouts and racy checks.

**You will learn**

- How to write the first test
- How to perform actions
- How to use assertions
- How tests run in isolation
- How to use test hooks

## First test

Take a look at the following example to see how to write a test.

tests/example.spec.ts

```js
import { test, expect } from '@playwright/test';

test('has title', async ({ page }) => {
  await page.goto('https://playwright.dev/');

  
  await expect(page).toHaveTitle(/Playwright/);
});

test('get started link', async ({ page }) => {
  await page.goto('https://playwright.dev/');

  
  await page.getByRole('link', { name: 'Get started' }).click();

  
  await expect(page.getByRole('heading', { name: 'Installation' })).toBeVisible();
});
```

note

Add `// @ts-check` at the start of each test file when using JavaScript in VS Code to get automatic type checking.

## Actions

### Navigation

Most tests start by navigating to a URL. After that, the test interacts with page elements.

```js
await page.goto('https://playwright.dev/');
```

Playwright waits for the page to reach the load state before continuing. Learn more about page.goto() options.

### Interactions

Performing actions starts with locating elements. Playwright uses Locators API for that. Locators represent a way to find element(s) on the page at any moment. Learn more about the different types of locators available.

Playwright waits for the element to be actionable before performing the action, so you don't need to wait for it to become available.

```js
const getStarted = page.getByRole('link', { name: 'Get started' });

await getStarted.click();
```

In most cases, it'll be written in one line:

```js
await page.getByRole('link', { name: 'Get started' }).click();
```

### Basic actions

Here are the most popular Playwright actions. For the complete list, check the Locator API section.

| Action | Descriptionlocator.check()Check the input checkboxlocator.click()Click the elementlocator.uncheck()Uncheck the input checkboxlocator.hover()Hover mouse over the elementlocator.fill()Fill the form field, input textlocator.focus()Focus the elementlocator.press()Press single keylocator.setInputFiles()Pick files to uploadlocator.selectOption()Select option in the drop down |
|---|---|

## Assertions

Playwright includes test assertions in the form of `expect` function. To make an assertion, call `expect(value)` and choose a matcher that reflects the expectation.

Playwright includes async matchers that wait until the expected condition is met. Using these matchers makes tests non-flaky and resilient. For example, this code waits until the page gets the title containing "Playwright":

```js
await expect(page).toHaveTitle(/Playwright/);
```

Here are the most popular async assertions. For the complete list, see assertions guide:

| Assertion | Descriptionexpect(locator).toBeChecked()Checkbox is checkedexpect(locator).toBeEnabled()Control is enabledexpect(locator).toBeVisible()Element is visibleexpect(locator).toContainText()Element contains textexpect(locator).toHaveAttribute()Element has attributeexpect(locator).toHaveCount()List of elements has given lengthexpect(locator).toHaveText()Element matches textexpect(locator).toHaveValue()Input element has valueexpect(page).toHaveTitle()Page has titleexpect(page).toHaveURL()Page has URL |
|---|---|

Playwright also includes generic matchers like `toEqual`, `toContain`, `toBeTruthy` that can be used to assert any conditions. These assertions do not use the `await` keyword as they perform immediate synchronous checks on already available values.

```js
expect(success).toBeTruthy();
```

### Test Isolation

Playwright Test is based on the concept of test fixtures such as the built in page fixture, which is passed into your test. Pages are isolated between tests due to the Browser Context, which is equivalent to a brand new browser profile. Every test gets a fresh environment, even when multiple tests run in a single browser.

tests/example.spec.ts

```js
import { test } from '@playwright/test';

test('example test', async ({ page }) => {
  
});

test('another test', async ({ page }) => {
  
});
```

### Using Test Hooks

You can use various test hooks such as `test.describe` to declare a group of tests and `test.beforeEach` and `test.afterEach` which are executed before/after each test. Other hooks include the `test.beforeAll` and `test.afterAll` which are executed once per worker before/after all tests.

tests/example.spec.ts

```js
import { test, expect } from '@playwright/test';

test.describe('navigation', () => {
  test.beforeEach(async ({ page }) => {
    
    await page.goto('https://playwright.dev/');
  });

  test('main navigation', async ({ page }) => {
    
    await expect(page).toHaveURL('https://playwright.dev/');
  });
});
```

## What's Next

- Run single test, multiple tests, headed mode
- Generate tests with Codegen
- See a trace of your tests
- Explore UI Mode
- Run tests on CI with GitHub Actions
