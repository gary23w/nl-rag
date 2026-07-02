---
title: "History - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/History
domain: history-api
license: CC-BY-SA-4.0
tags: history api, push state navigation, session history entry, popstate history traversal
fetched: 2026-07-02
---

# History

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

- Learn more
- See full compatibility

The **`History`** interface of the History API allows manipulation of the browser *session history*, that is the pages visited in the tab or frame that the current page is loaded in.

There is only one instance of `history` (It is a *singleton*.) accessible via the global object `history`.

**Note:** This interface is only available on the main thread (`Window`). It cannot be accessed in `Worker` or `Worklet` contexts.

## Instance properties

*The `History` interface doesn't inherit any property.*

**`length` Read only**

Returns an `Integer` representing the number of elements in the session history, including the currently loaded page. For example, for a page loaded in a new tab this property returns `1`.

**`scrollRestoration`**

Allows web applications to explicitly set default scroll restoration behavior on history navigation. This property can be either `auto` or `manual`.

**`state` Read only**

Returns an `any` value representing the state at the top of the history stack. This is a way to look at the state without having to wait for a `popstate` event.

## Instance methods

*The `History`* *interface doesn't inherit any methods.*

**`back()`**

This asynchronous method goes to the previous page in session history, the same action as when the user clicks the browser's Back button. Equivalent to `history.go(-1)`.

Calling this method to go back beyond the first page in the session history has no effect and doesn't raise an exception.

**`forward()`**

This asynchronous method goes to the next page in session history, the same action as when the user clicks the browser's Forward button; this is equivalent to `history.go(1)`.

Calling this method to go forward beyond the most recent page in the session history has no effect and doesn't raise an exception.

**`go()`**

Asynchronously loads a page from the session history, identified by its relative location to the current page, for example `-1` for the previous page or `1` for the next page. If you specify an out-of-bounds value (for instance, specifying `-1` when there are no previously-visited pages in the session history), this method silently has no effect. Calling `go()` without parameters or a value of `0` reloads the current page.

**`pushState()`**

Pushes the given data onto the session history stack with the specified title (and, if provided, URL). The data is treated as opaque by the DOM; you may specify any JavaScript object that can be serialized. Note that all browsers but Safari currently ignore the *title* parameter. For more information, see Working with the History API.

**`replaceState()`**

Updates the most recent entry on the history stack to have the specified data, title, and, if provided, URL. The data is treated as opaque by the DOM; you may specify any JavaScript object that can be serialized. Note that all browsers but Safari currently ignore the *title* parameter. For more information, see Working with the History API.

## Specifications

| Specification |
|---|
| HTML # the-history-interface |

## Browser compatibility
