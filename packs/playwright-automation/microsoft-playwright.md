---
title: "GitHub"
source: https://github.com/microsoft/playwright
domain: playwright-automation
license: CC-BY-SA-4.0
tags: playwright automation, cross-browser automation, headless browser control, auto-waiting locator
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

microsoft

/

playwright

Public

- Notifications You must be signed in to change notification settings
- Fork 6k
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History17,390 Commits17,390 Commits |   |   |   |
| .azure-pipelines | .azure-pipelines |   |   |
| .claude/skills | .claude/skills |   |   |
| .github | .github |   |   |
| browser_patches | browser_patches |   |   |
| docs/src | docs/src |   |   |
| examples | examples |   |   |
| packages | packages |   |   |
| tests | tests |   |   |
| utils | utils |   |   |
| .editorconfig | .editorconfig |   |   |
| .gitattributes | .gitattributes |   |   |
| .gitignore | .gitignore |   |   |
| CLAUDE.md | CLAUDE.md |   |   |
| CODE_OF_CONDUCT.md | CODE_OF_CONDUCT.md |   |   |
| CONTRIBUTING.md | CONTRIBUTING.md |   |   |
| FILING_ISSUES.md | FILING_ISSUES.md |   |   |
| LICENSE | LICENSE |   |   |
| NOTICE | NOTICE |   |   |
| README.md | README.md |   |   |
| SECURITY.md | SECURITY.md |   |   |
| SUPPORT.md | SUPPORT.md |   |   |
| eslint.config.mjs | eslint.config.mjs |   |   |
| package-lock.json | package-lock.json |   |   |
| package.json | package.json |   |   |
| tsconfig.json | tsconfig.json |   |   |
|   |   |   |   |

## Repository files navigation

# 🎭 Playwright

(npm version) (Chromium version) (Firefox version) (WebKit version) (Join Discord)

## Documentation | API reference

Playwright is a framework for web automation and testing. It drives Chromium, Firefox, and WebKit with a single API — in your tests, in your scripts, and as a tool for AI agents.

## Get Started

Choose the path that fits your workflow:

|   | Best for | Install |
|---|---|---|
| **Playwright Test** | End-to-end testing | `npm init playwright@latest` |
| **Playwright CLI** | Coding agents (Claude Code, Copilot) | `npm i -g @playwright/cli@latest` |
| **Playwright MCP** | AI agents and LLM-driven automation | `npx @playwright/mcp@latest` |
| **Playwright Library** | Browser automation scripts | `npm i playwright` |
| **VS Code Extension** | Test authoring and debugging in VS Code | Install from Marketplace |

## Playwright Test

Playwright Test is a full-featured test runner built for end-to-end testing. It runs tests across Chromium, Firefox, and WebKit with full browser isolation, auto-waiting, and web-first assertions.

### Install

```highlight
npm init playwright@latest
```

Or add manually:

```highlight
npm i -D @playwright/test
npx playwright install
```

### Write a test

```highlight
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

### Run tests

```highlight
npx playwright test
```

Tests run in parallel across all configured browsers, in headless mode by default. Each test gets a fresh browser context — full isolation with near-zero overhead.

### Key capabilities

**Auto-wait and web-first assertions.** No artificial timeouts. Playwright waits for elements to be actionable, and assertions automatically retry until conditions are met.

**Locators.** Find elements with resilient locators that mirror how users see the page:

```highlight
page.getByRole('button', { name: 'Submit' })
page.getByLabel('Email')
page.getByPlaceholder('Search...')
page.getByTestId('login-form')
```

**Test isolation.** Each test runs in its own browser context — equivalent to a fresh browser profile. Save authentication state once and reuse it across tests:

```highlight
// Save state after login
await page.context().storageState({ path: 'auth.json' });

// Reuse in other tests
test.use({ storageState: 'auth.json' });
```

**Tracing.** Capture execution traces, screenshots, and videos on failure. Inspect every action, DOM snapshot, network request, and console message in the Trace Viewer:

```highlight
// playwright.config.ts
export default defineConfig({
  use: {
    trace: 'on-first-retry',
  },
});
```

```highlight
npx playwright show-trace trace.zip
```

**Parallelism.** Tests run in parallel by default across all configured browsers.

Full testing documentation

## Playwright CLI

Playwright CLI is a command-line interface for browser automation designed for coding agents. It's more token-efficient than MCP — commands avoid loading large tool schemas and accessibility trees into the model context.

### Install

```highlight
npm install -g @playwright/cli@latest
```

Optionally install skills for richer agent integration:

```highlight
playwright-cli install --skills
```

### Usage

Point your coding agent at a task:

```
Test the "add todo" flow on https://demo.playwright.dev/todomvc using playwright-cli.
Take screenshots for all successful and failing scenarios.
```

Or run commands directly:

```highlight
playwright-cli open https://demo.playwright.dev/todomvc/ --headed
playwright-cli type "Buy groceries"
playwright-cli press Enter
playwright-cli screenshot
```

### Session monitoring

Use `playwright-cli show` to open a visual dashboard with live screencast previews of all running browser sessions. Click any session to zoom in and take remote control.

```highlight
playwright-cli show
```

Full CLI documentation | GitHub

## Playwright MCP

The Playwright MCP server gives AI agents full browser control through the Model Context Protocol. Agents interact with pages using structured accessibility snapshots — no vision models or screenshots required.

### Setup

Add to your MCP client (VS Code, Cursor, Claude Desktop, Windsurf, etc.):

```highlight
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

**One-click install for VS Code:**

(Install in VS Code)

**For Claude Code:**

```highlight
claude mcp add playwright npx @playwright/mcp@latest
```

### How it works

Ask your AI assistant to interact with any web page:

```
Navigate to https://demo.playwright.dev/todomvc and add a few todo items.
```

The agent sees the page as a structured accessibility tree:

```
- heading "todos" [level=1]
- textbox "What needs to be done?" [ref=e5]
- listitem:
  - checkbox "Toggle Todo" [ref=e10]
  - text: "Buy groceries"
```

It uses element refs like `e5` and `e10` to click, type, and interact — deterministically and without visual ambiguity. Tools cover navigation, form filling, screenshots, network mocking, storage management, and more.

Full MCP documentation | GitHub

## Playwright Library

Use `playwright` as a library for browser automation scripts — web scraping, PDF generation, screenshot capture, and any workflow that needs programmatic browser control without a test runner.

### Install

```highlight
npm i playwright
```

### Examples

**Take a screenshot:**

```highlight
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto('https://playwright.dev/');
await page.screenshot({ path: 'screenshot.png' });
await browser.close();
```

**Generate a PDF:**

```highlight
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto('https://playwright.dev/');
await page.pdf({ path: 'page.pdf', format: 'A4' });
await browser.close();
```

**Emulate a mobile device:**

```highlight
import { chromium, devices } from 'playwright';

const browser = await chromium.launch();
const context = await browser.newContext(devices['iPhone 15']);
const page = await context.newPage();
await page.goto('https://playwright.dev/');
await page.screenshot({ path: 'mobile.png' });
await browser.close();
```

**Intercept network requests:**

```highlight
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();
await page.route('**/*.{png,jpg,jpeg}', route => route.abort());
await page.goto('https://playwright.dev/');
await browser.close();
```

Library documentation | API reference

## VS Code Extension

The Playwright VS Code extension brings test running, debugging, and code generation directly into your editor.

**Run and debug tests** from the editor with a single click. Set breakpoints, inspect variables, and step through test execution with a live browser view.

**Generate tests with CodeGen.** Click "Record new" to open a browser — navigate and interact with your app while Playwright writes the test code for you.

**Pick locators.** Hover over any element in the browser to see the best available locator, then click to copy it to your clipboard.

**Trace Viewer integration.** Enable "Show Trace Viewer" in the sidebar to get a full execution trace after each test run — DOM snapshots, network requests, console logs, and screenshots at every step.

Install the extension | VS Code guide

## Cross-Browser Support

|   | Linux | macOS | Windows |
|---|---|---|---|
| Chromium1 150.0.7871.46 | ✅ | ✅ | ✅ |
| WebKit 26.5 | ✅ | ✅ | ✅ |
| Firefox 151.0 | ✅ | ✅ | ✅ |

Headless and headed execution on all platforms. 1 Uses Chrome for Testing by default.

## Other Languages

Playwright is also available for Python, .NET, and Java.

## Resources

- Documentation
- API reference
- MCP server
- CLI for coding agents
- VS Code extension
- Contribution guide
- Changelog
- Discord
