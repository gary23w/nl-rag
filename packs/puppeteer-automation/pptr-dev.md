---
title: "Puppeteer"
source: https://pptr.dev/
domain: puppeteer-automation
license: CC-BY-SA-4.0
tags: puppeteer automation, headless chrome control, devtools protocol driver, browser scripting
fetched: 2026-07-02
---

# Puppeteer

Version: 25.3.0

# Puppeteer

(build) (npm puppeteer package)

> Puppeteer is a JavaScript library which provides a high-level API to control Chrome or Firefox over the DevTools Protocol or WebDriver BiDi. Puppeteer runs in the headless (no visible UI) by default

## Get started | API | FAQ | Contributing | Troubleshooting

## Installation

- npm
- Yarn
- pnpm
- Bun

```bash
npm i puppeteer 
npm i puppeteer-core 
```

```bash
yarn add puppeteer 
yarn add puppeteer-core 
```

```bash
pnpm add puppeteer 
pnpm add puppeteer-core 
```

```bash
bun add puppeteer 
bun add puppeteer-core 
```

note

Modern package managers (including npm (see the RFC), pnpm, Yarn, Bun, and Deno) block dependency install scripts by default. If the install script is blocked, Puppeteer will not download the browser during installation, leading to runtime errors.

You can manually download the required browsers after installation by running:

- npm
- Yarn
- pnpm
- Bun

```bash
npx puppeteer browsers install
```

```bash
yarn dlx puppeteer browsers install
```

```bash
pnpm dlx puppeteer browsers install
```

```bash
bun x puppeteer browsers install
```

Alternatively, you can configure your package manager to allow the install script to run (for example, with npm, by adding `"puppeteer"` to `"allowScripts"` in your `package.json`).

## MCP

Install `chrome-devtools-mcp`, a Puppeteer-based MCP server for browser automation and debugging.

Puppeteer also supports the experimental WebMCP API.

## Example

```ts
import puppeteer from 'puppeteer';

const browser = await puppeteer.launch();
const page = await browser.newPage();

await page.goto('https://developer.chrome.com/');

await page.setViewport({width: 1080, height: 1024});

await page.keyboard.press('/');

await page.locator('::-p-aria(Search)').fill('automate beyond recorder');

await page.locator('.devsite-result-item-link').click();

const textSelector = await page
  .locator('::-p-text(Customize and automate)')
  .waitHandle();
const fullTitle = await textSelector?.evaluate(el => el.textContent);

console.log('The title of this blog post is "%s".', fullTitle);

await browser.close();
```
