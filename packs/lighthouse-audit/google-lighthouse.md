---
title: "Lighthouse (software)"
source: https://en.wikipedia.org/wiki/Google_Lighthouse
domain: lighthouse-audit
license: CC-BY-SA-4.0
tags: lighthouse audit, navigation timing api, resource timing api, user timing marks
fetched: 2026-07-02
---

# Lighthouse (software)

(Redirected from

Google Lighthouse

)

**Lighthouse** is an open-source, automated tool for measuring the quality of web pages developed by Google. It can be run against any web page, public or requiring authentication. Lighthouse audits performance, accessibility, and search engine optimization factors of web pages, which is the major difference from Google PageSpeed, as Lighthouse provides more detailed technical information. It also includes the ability to test progressive web applications for compliance with standards and best practices. Lighthouse aims to help web developers; the tool can be run using a Chrome browser extension or via the terminal (command line) for batch auditing a list of URLs. Google's recommendation is to use the online version of PageSpeed Insights as of 15 May 2015.

Lighthouse [Version 10 - May 2023] includes a metric for Progressive Web Applications to ensure that PWAs are fast, reliable, installable, and optimized for modern mobile technology.

Lighthouse can audit webpages in both desktop and mobile versions. In command line mode, developers are able to select specific factors to audit and configure other options using arguments.

Recent versions of Lighthouse offer insights into how to optimize the Core Web Vitals metrics, which serve as user experience and performance signals used by Google's search algorithm to rank pages, as announced by Google engineer Addy Osmani in 2021. Google uses three primary parameters to measure Core Web Vitals compliance:

- **Largest Contentful Paint (LCP):** Measures loading performance, targeting the point when the page's main content has likely loaded.
- **Cumulative Layout Shift (CLS):** Measures visual stability by detecting unexpected layout shifts during the page lifecycle.
- **Interaction to Next Paint (INP):** Measures overall user interaction responsiveness. On 10 May 2023, Google announced that INP would replace the older First Input Delay (FID) metric to capture the total time taken for all user interactions rather than just the first one. This change officially went into effect in March 2024.

Lighthouse also calculates **Total Blocking Time (TBT)**, which serves as an excellent lab proxy for evaluating responsiveness issues during page loading.
