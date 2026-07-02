---
title: "Introduction to Lighthouse"
source: https://developer.chrome.com/docs/lighthouse/overview
domain: lighthouse-audit
license: CC-BY-SA-4.0
tags: lighthouse audit, navigation timing api, resource timing api, user timing marks
fetched: 2026-07-02
---

# Introduction to Lighthouse Stay organized with collections Save and categorize content based on your preferences.

Lighthouse is an open-source, automated tool to help you improve the quality of web pages. You can run it on any web page, public or requiring authentication. It has audits for performance, accessibility, SEO, and more.

You can run Lighthouse in Chrome DevTools, from the command line, or as a Node module. Give Lighthouse a URL to audit, it runs a series of audits against the page, and then it generates a report on how well the page performed. Use the failed audits as indicators for how to improve the page. Each audit has a reference that explains why the audit is important, as well as how to fix it.

You can also use Lighthouse CI to prevent regressions on your sites.

## Get started

Choose the Lighthouse workflow that suits you best:

- In Chrome DevTools. Audit pages that require authentication and read your reports in a user-friendly format, right from the browser.
- From the command line. Automate your Lighthouse runs with shell scripts.
- As a Node module. Integrate Lighthouse into your continuous integration systems.
- From a web UI. Run Lighthouse and link to reports, no installation needed.

### Run Lighthouse in Chrome DevTools

Lighthouse has its own panel in Chrome DevTools. To run a report:

1. Download Google Chrome for Desktop.
2. Open Chrome, and go to the URL you want to audit. You can audit any URL on the web.
3. Open Chrome DevTools.
4. Click the **Lighthouse** tab.
5. Click **Analyze page load**. DevTools shows you a list of audit categories. Leave them all enabled.
6. Click **Run audit**. After 30 to 60 seconds, Lighthouse gives you a report on the page.

### Install and run the Node command line tool

To install the Node module:

1. Download Google Chrome for Desktop.
2. Install the current Long-Term Support version of Node.
3. Install Lighthouse. The `-g` flag installs it as a global module.

```
npm install -g lighthouse
```

To run an audit:

```
lighthouse <url>
```

To see all the options:

```
lighthouse --help
```

#### Run the Node module programmatically

See Using programmatically for an example of running Lighthouse programmatically, as a Node module.

### Run PageSpeed Insights

To run Lighthouse on PageSpeed Insights:

1. Go to PageSpeed Insights.
2. Enter a web page URL.
3. Click **Analyze**.

### Run Lighthouse as a Chrome Extension

To install the extension:

1. Download Google Chrome for Desktop.
2. Install the Lighthouse Chrome Extension from the Chrome Webstore.

To run an audit:

1. In Chrome, go to the page you want to audit.
2. Click **Lighthouse**, next to the Chrome address bar or in Chrome's extension menu. Once clicked, the Lighthouse menu expands.
3. Click **Generate report**. Lighthouse runs its audits against the currently-focused page, then opens up a new tab with a report of the results.

## Share and view reports online

Use the Lighthouse Viewer to view and share reports online.

### Share reports as JSON

The Lighthouse Viewer needs the JSON output of a Lighthouse report. Generate the JSON outputs as follows:

- **From a Lighthouse report**. Click more_vert for the menu, then click **Save as JSON**
- **Command line**. Run: `shell lighthouse --output json --output-path <path/for/output.json>`

To view the report data:

1. Open the Lighthouse Viewer.
2. Drag the JSON file onto the Viewer, or click anywhere in the Viewer to open your file navigator and select the file.

### Share reports as GitHub Gists

If you don't want to manually pass around JSON files, you can also share your reports as secret GitHub gists. One benefit of gists is free version control.

To export a report as a gist from the report:

1. Click the more_vert menu, then click **Open In Viewer**. The report is located at `https://googlechrome.github.io/lighthouse/viewer/`.
2. From the Viewer, click more_vert menu, then click **Save as Gist**. The first time you do this, a popup asks permission to access your basic GitHub data, and to read and write to your gists.

To export a report as a gist from the CLI version of Lighthouse, manually create a gist and copy-paste the report's JSON output into the gist. The gist filename containing the JSON output must end in `.lighthouse.report.json`. See Share reports as JSON for an example of how to generate JSON output from the command line tool.

To view a report that's been saved as a gist:

- Add `?gist=<ID>` to the Viewer's URL, where `<ID>` is the ID of the gist. `text https://googlechrome.github.io/lighthouse/viewer/?gist=<ID>`
- Open the Viewer, and paste the URL of a gist into it.

## Lighthouse extensibility

Lighthouse aims to provide guidance that is relevant and actionable for all web developers. To this end, there are two features available that allow you to tailor Lighthouse to your specific needs.

### Stack packs

Developers use many different technologies (backend, content management systems, and JavaScript frameworks) to build their web pages. Instead of surfacing general recommendations, Lighthouse provides relevant and actionable advice, depending on the tools used.

*Stack packs* allow Lighthouse to detect what platform your site is built on and display specific stack-based recommendations. These recommendations are defined and curated by experts from the community.

To contribute a stack pack, review the Contributing Guidelines.

### Lighthouse plugins

Lighthouse plugins allow domain experts to extend the functionality of Lighthouse for their community's specific needs. You can leverage the data that Lighthouse collects to create new audits. At its core, a Lighthouse plugin is a node module that implements a set of checks to be run by Lighthouse and added to the report as a new category.

For more information about how to create your own plugin, check out our Plugin Handbook in the Lighthouse GitHub repo.

## Integrate Lighthouse

If you're a company or an individual who is integrating Lighthouse as part of the products or services you're offering, that's great! We want as many people as possible to use Lighthouse.

Refer to the Guidelines and Brand Assets for Integrating Lighthouse to show that Lighthouse is used, while protecting our brand.

## Contribute to Lighthouse

Lighthouse is open source and contributions are welcome! Check out the repository's Issue tracker to find bugs that you can fix, or audits that you can create or improve upon. The Issues are a good place to discuss performance metrics, ideas for new audits, or anything else related to Lighthouse.

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-02 UTC.
