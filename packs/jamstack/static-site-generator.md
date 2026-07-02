---
title: "Static site generator"
source: https://en.wikipedia.org/wiki/Static_site_generator
domain: jamstack
license: CC-BY-SA-4.0
tags: jamstack architecture, prebuilt markup delivery, client side rendering, web development workflow
fetched: 2026-07-02
---

# Static site generator

**Static site generators** (**SSGs**) are software engines that use text input files (such as Markdown, reStructuredText, AsciiDoc and JSON) to generate static web pages. Unlike dynamic websites, these static pages do not change based on the request. This simplifies the requirements for the backend and allows the site to be distributed via content delivery networks (CDNs). The simple design also makes it harder for attackers to modify the website due to the smaller attack surface of these relatively simple backends. Some of the most popular static site generators are Jekyll, Hugo, Eleventy, Gatsby, and Next.js. SSGs are typically for rarely changing, informative content, such as product pages, news articles, software documentation, and blogs.

## Architecture

SSGs typically consist of a template written in HTML with a templating system, such as Liquid (Jekyll) or Go template (Hugo). The same structure (typically a Git repository) includes content in a plain-text format such as Markdown or reStructuredText, or in a structural meta format such as JSON or XML. A single plain-text file may correspond to a single web page. Alternatively, a single structural metadata file may correspond to an entire website if a single-page application framework like AngularJS is used. The website variable settings are stored in a plaintext configuration file `_config.yml` (YAML), `_config.toml` (TOML) or `_config.json` (JSON). Page files typically also start with a YAML, TOML, or JSON preamble to define variables such as title, permalink, or date. Files with names that begin with an underscore (`_`) such as `_index.md` (as opposed to `index.md`) are considered templates or archetypes and are thus not rendered as pages themselves.

## Examples

Several hundred SSGs have been documented to exist, with the vast majority being written in languages that are already prominent on the web, such as Python, Go, JavaScript and TypeScript.

| System label/name | Language | Notes |
|---|---|---|
| Jekyll | Ruby | Uses Liquid templating language. |
| Hugo | Go | Uses Go templates and its main selling point is its high speed when compiling. |
| Next.js | JavaScript | Uses React templates. |
| Pelican | Python | Uses Jinja2 templates. Compiles HTML from reStructuredText or Markdown. |
| Astro | JavaScript | Uses the .astro syntax language by default (familiar to HTML or JSX). Supports multiple frameworks: Svelte, React, Preact, Vue, SolidJS, Lit, AlpineJS. Compiles HTML from Markdown or MDX. |
| Docusaurus | JavaScript | Compiles HTML from MDX, Markdown, JavaScript and React. Uses Node.js. Customization with React. |
| Eleventy | JavaScript | Supports 10 template languages. |

## Comparison with server-side systems

Many *server-side template systems* have the option to publish output pages on the server, where the published pages are static. This is common on content management systems, like Vignette, but is not considered out-server generation. In the majority of cases, this "publish option" doesn't interfere with the *template system*, and it can be made by external software, as Wget.

People began to use server-side dynamic pages generated from templates with pre-existing software adapted for this task. This early software was the preprocessors and macro languages, adapted for web use, running on CGI. Next, a simple but relevant technology was the direct execution made on extension modules, starting with SSI.
