---
title: "GitHub"
source: https://github.com/puppeteer/puppeteer
domain: puppeteer-automation
license: CC-BY-SA-4.0
tags: puppeteer automation, headless chrome control, devtools protocol driver, browser scripting
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

puppeteer

/

puppeteer

Public

- Notifications You must be signed in to change notification settings
- Fork 9.5k
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History6,387 Commits6,387 Commits |   |   |   |
| .agents/skills/puppeteer-verification | .agents/skills/puppeteer-verification |   |   |
| .devcontainer | .devcontainer |   |   |
| .github | .github |   |   |
| .vscode | .vscode |   |   |
| docker | docker |   |   |
| docs | docs |   |   |
| examples | examples |   |   |
| packages | packages |   |   |
| test-d | test-d |   |   |
| test | test |   |   |
| tools | tools |   |   |
| website | website |   |   |
| .editorconfig | .editorconfig |   |   |
| .gitattributes | .gitattributes |   |   |
| .gitignore | .gitignore |   |   |
| .mocharc.cjs | .mocharc.cjs |   |   |
| .npmrc | .npmrc |   |   |
| .nvmrc | .nvmrc |   |   |
| .prettierignore | .prettierignore |   |   |
| .release-please-manifest.json | .release-please-manifest.json |   |   |
| CHANGELOG.md | CHANGELOG.md |   |   |
| Herebyfile.mjs | Herebyfile.mjs |   |   |
| LICENSE | LICENSE |   |   |
| README.md | README.md |   |   |
| SECURITY.md | SECURITY.md |   |   |
| eslint.config.mjs | eslint.config.mjs |   |   |
| package-lock.json | package-lock.json |   |   |
| package.json | package.json |   |   |
| prettier.config.js | prettier.config.js |   |   |
| puppeteer.config.js | puppeteer.config.js |   |   |
| release-please-config.json | release-please-config.json |   |   |
| tsconfig.base.json | tsconfig.base.json |   |   |
| tsdoc.json | tsdoc.json |   |   |
| versions.json | versions.json |   |   |
|   |   |   |   |

## Repository files navigation

# Puppeteer

(build) (npm puppeteer package)

> Puppeteer is a JavaScript library which provides a high-level API to control Chrome or Firefox over the DevTools Protocol or WebDriver BiDi. Puppeteer runs in the headless (no visible UI) by default

## Get started | API | FAQ | Contributing | Troubleshooting

## Installation

```highlight
npm i puppeteer # Downloads compatible Chrome during installation.
npm i puppeteer-core # Alternatively, install as a library, without downloading Chrome.
```

:::note

Modern package managers (including npm (see the RFC), pnpm, Yarn, Bun, and Deno) block dependency install scripts by default. If the install script is blocked, Puppeteer will not download the browser during installation, leading to runtime errors.

You can manually download the required browsers after installation by running:

```highlight
npx puppeteer browsers install
```

Alternatively, you can configure your package manager to allow the install script to run (for example, with npm, by adding `"puppeteer"` to `"allowScripts"` in your `package.json`).

:::

## MCP

Install `chrome-devtools-mcp`, a Puppeteer-based MCP server for browser automation and debugging.

Puppeteer also supports the experimental WebMCP API.

## Example

```highlight
import puppeteer from 'puppeteer';
// Or import puppeteer from 'puppeteer-core';

// Launch the browser and open a new blank page.
const browser = await puppeteer.launch();
const page = await browser.newPage();

// Navigate the page to a URL.
await page.goto('https://developer.chrome.com/');

// Set the screen size.
await page.setViewport({width: 1080, height: 1024});

// Open the search menu using the keyboard.
await page.keyboard.press('/');

// Type into search box using accessible input name.
await page.locator('::-p-aria(Search)').fill('automate beyond recorder');

// Wait and click on first result.
await page.locator('.devsite-result-item-link').click();

// Locate the full title with a unique string.
const textSelector = await page
  .locator('::-p-text(Customize and automate)')
  .waitHandle();
const fullTitle = await textSelector?.evaluate(el => el.textContent);

// Print the full title.
console.log('The title of this blog post is "%s".', fullTitle);

await browser.close();
```
