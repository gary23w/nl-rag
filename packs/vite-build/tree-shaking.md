---
title: "Tree shaking - Glossary"
source: https://developer.mozilla.org/en-US/docs/Glossary/Tree_shaking
domain: vite-build
license: CC-BY-SA-4.0 / MIT (vitejs.dev)
tags: vite build, vite dev server, esm bundler, vite hmr
fetched: 2026-07-02
---

# Tree shaking

**Tree shaking** is a term commonly used within a JavaScript context to describe the removal of dead code.

It relies on the import and export statements to detect if code modules are exported and imported for use between JavaScript files.

In modern JavaScript applications, we use module bundlers (e.g., webpack or Rollup) to automatically remove dead code when bundling multiple JavaScript files into single files. This is important for preparing code that is production ready, for example with clean structures and minimal file size.
