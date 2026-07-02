---
title: "URLPattern - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/URLPattern
domain: url-pattern-api
license: CC-BY-SA-4.0
tags: url pattern api, url matching syntax, route pattern parsing, named path group
fetched: 2026-07-02
---

# URLPattern

Baseline

2025

Newly available

Since September 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

- Learn more
- See full compatibility

**Note:** This feature is available in Web Workers.

The **`URLPattern`** interface of the URL Pattern API matches URLs or parts of URLs against a pattern. The pattern can contain capturing groups that extract parts of the matched URL.

More information about the syntax of patterns can be found on the API overview page: URL Pattern API.

## Constructor

**`URLPattern()`**

Returns a new `URLPattern` object based on the given pattern and base URL.

## Instance properties

**`hash` Read only**

A string containing a pattern to match the *hash* part of a URL.

**`hasRegExpGroups` Read only**

A boolean indicating whether or not any of the `URLPattern` components contain regular expression capturing groups.

**`hostname` Read only**

A string containing a pattern to match the *hostname* part of a URL.

**`password` Read only**

A string containing a pattern to match the *password* part of a URL.

**`pathname` Read only**

A string containing a pattern to match the *pathname* part of a URL.

**`port` Read only**

A string containing a pattern to match the *port* part of a URL.

**`protocol` Read only**

A string containing a pattern to match the *protocol* part of a URL.

A string containing a pattern to match the *search* part of a URL.

**`username` Read only**

A string containing a pattern to match the *username* part of a URL.

## Instance methods

**`exec()`**

Returns an object with the matched parts of the URL or `null` if the URL does not match.

**`test()`**

Returns `true` if the URL matches the given pattern, `false` otherwise.

## Specifications

| Specification |
|---|
| URL Pattern # urlpattern |

## Browser compatibility
