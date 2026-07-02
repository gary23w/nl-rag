---
title: "Window - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Window
domain: custom-elements
license: CC-BY-SA-4.0
tags: custom elements, custom element registry, autonomous html element, define web component
fetched: 2026-07-02
---

# Window

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **`Window`** interface represents a window containing a DOM document; the `document` property points to the DOM document loaded in that window.

A window for a given document can be obtained using the `document.defaultView` property.

A global variable, `window`, representing the window in which the script is running, is exposed to JavaScript code.

The `Window` interface is home to a variety of functions, namespaces, objects, and constructors which are not necessarily directly associated with the concept of a user interface window. However, the `Window` interface is a suitable place to include these items that need to be globally available. Many of these are documented in the JavaScript Reference and the DOM Reference.

In a tabbed browser, each tab is represented by its own `Window` object; the global `window` seen by JavaScript code running within a given tab always represents the tab in which the code is running. That said, even in a tabbed browser, some properties and methods still apply to the overall window that contains the tab, such as `resizeTo()` and `innerHeight`. Generally, anything that can't reasonably pertain to a tab pertains to the window instead.

## Instance properties

*This interface inherits properties from the `EventTarget` interface.*

Note that properties which are objects (e.g., for overriding the prototype of built-in elements) are listed in a separate section below.

**`Window.caches` Read only Secure context**

Returns the `CacheStorage` object associated with the current context. This object enables functionality such as storing assets for offline use, and generating custom responses to requests.

**`Window.clientInformation` Read only**

An alias for `Window.navigator`.

**`Window.closed` Read only**

This property indicates whether the current window is closed or not.

**`Window.cookieStore` Read only Secure context**

Returns a reference to the `CookieStore` object for the current document context.

**`Window.crashReport` Read only Secure context**

Returns a `CrashReportContext` object that enables arbitrary data to be recorded for the current top-level browsing context, which is then added to a `CrashReport` and sent to a reporting endpoint when a browser crash occurs.

**`Window.credentialless` Read only**

Returns a boolean that indicates whether the current document was loaded inside a credentialless `<iframe>`. See IFrame credentialless for more details.

**`Window.crossOriginIsolated` Read only**

Returns a boolean value that indicates whether the website is in a cross-origin isolation state.

**`Window.crypto` Read only**

Returns the `Crypto` object associated to the global object.

**`Window.customElements` Read only**

Returns a reference to the `CustomElementRegistry` object, which can be used to register new custom elements and get information about previously registered custom elements.

**`Window.devicePixelRatio` Read only**

Returns the ratio between physical pixels and device independent pixels in the current display.

**`Window.document` Read only**

Returns a reference to the document that the window contains.

**`Window.documentPictureInPicture` Read only Secure context**

Returns a reference to the document Picture-in-Picture window for the current document context.

**`Window.fence` Read only**

Returns a `Fence` object instance for the current document context. Available only to documents embedded inside a `<fencedframe>`.

**`Window.frameElement` Read only**

Returns the element in which the window is embedded, or null if the window is not embedded.

**`Window.frames` Read only**

Returns an array of the subframes in the current window.

**`Window.fullScreen`**

This property indicates whether the window is displayed in full screen or not.

**`Window.history` Read only**

Returns a reference to the history object.

**`Window.indexedDB` Read only**

Provides a mechanism for applications to asynchronously access capabilities of indexed databases; returns an `IDBFactory` object.

**`Window.innerHeight` Read only**

Gets the height of the content area of the browser window including, if rendered, the horizontal scrollbar.

**`Window.innerWidth` Read only**

Gets the width of the content area of the browser window including, if rendered, the vertical scrollbar.

**`Window.isSecureContext` Read only**

Returns a boolean indicating whether the current context is secure (`true`) or not (`false`).

**`Window.launchQueue` Read only**

When a progressive web app (PWA) is launched with a `launch_handler` `client_mode` value of `focus-existing`, `navigate-new`, or `navigate-existing`, the `launchQueue` provides access to the `LaunchQueue` class, which allows custom launch navigation handling to be implemented for the PWA.

**`Window.length` Read only**

Returns the number of frames in the window. See also `window.frames`.

**`Window.localStorage` Read only**

Returns a reference to the local storage object used to store data that may only be accessed by the origin that created it.

**`Window.location`**

Gets/sets the location, or current URL, of the window object.

**`Window.locationbar` Read only**

Returns the locationbar object.

**`Window.menubar` Read only**

Returns the menubar object.

**`Window.mozInnerScreenX` Read only**

Returns the horizontal (X) coordinate of the top-left corner of the window's viewport, in screen coordinates. This value is reported in CSS pixels. See `mozScreenPixelsPerCSSPixel` in `nsIDOMWindowUtils` for a conversion factor to adapt to screen pixels if needed.

**`Window.mozInnerScreenY` Read only**

Returns the vertical (Y) coordinate of the top-left corner of the window's viewport, in screen coordinates. This value is reported in CSS pixels. See `mozScreenPixelsPerCSSPixel` for a conversion factor to adapt to screen pixels if needed.

**`Window.name`**

Gets/sets the name of the window.

**`Window.navigation` Read only**

Returns the current `window`'s associated `Navigation` object. The entry point for the Navigation API.

**`Window.navigator` Read only**

Returns a reference to the navigator object.

**`Window.opener`**

Returns a reference to the window that opened this current window.

**`Window.origin` Read only**

Returns the global object's origin, serialized as a string.

**`Window.originAgentCluster` Read only**

Returns `true` if this window belongs to an origin-keyed agent cluster.

**`Window.outerHeight` Read only**

Gets the height of the outside of the browser window.

**`Window.outerWidth` Read only**

Gets the width of the outside of the browser window.

**`Window.pageXOffset` Read only**

An alias for `window.scrollX`.

**`Window.pageYOffset` Read only**

An alias for `window.scrollY`.

**`Window.parent` Read only**

Returns a reference to the parent of the current window or subframe.

**`Window.performance` Read only**

Returns a `Performance` object, which includes the `timing` and `navigation` attributes, each of which is an object providing performance-related data. See also Using Navigation Timing for additional information and examples.

**`Window.personalbar` Read only**

Returns the personalbar object.

**`Window.scheduler` Read only**

Returns the `Scheduler` object associated with the current context. This is the entry point for using the Prioritized Task Scheduling API.

**`Window.screen` Read only**

Returns a reference to the screen object associated with the window.

**`Window.screenX` and `Window.screenLeft` Read only**

Both properties return the horizontal distance from the left border of the user's browser viewport to the left side of the screen.

**`Window.screenY` and `Window.screenTop` Read only**

Both properties return the vertical distance from the top border of the user's browser viewport to the top side of the screen.

**`Window.scrollbars` Read only**

Returns the scrollbars object.

**`Window.scrollMaxX` Read only**

The maximum offset that the window can be scrolled to horizontally, that is the document width minus the viewport width.

**`Window.scrollMaxY` Read only**

The maximum offset that the window can be scrolled to vertically (i.e., the document height minus the viewport height).

**`Window.scrollX` Read only**

Returns the number of pixels that the document has already been scrolled horizontally.

**`Window.scrollY` Read only**

Returns the number of pixels that the document has already been scrolled vertically.

**`Window.self` Read only**

Returns an object reference to the window object itself.

**`Window.sessionStorage`**

Returns a reference to the session storage object used to store data that may only be accessed by the origin that created it.

**`Window.sharedStorage` Read only Secure context**

Returns the `WindowSharedStorage` object for the current origin. This is the main entry point for writing data to shared storage using the Shared Storage API.

**`Window.speechSynthesis` Read only**

Returns a `SpeechSynthesis` object, which is the entry point into using Web Speech API speech synthesis functionality.

**`Window.statusbar` Read only**

Returns the statusbar object.

**`Window.toolbar` Read only**

Returns the toolbar object.

**`Window.top` Read only**

Returns a reference to the topmost window in the window hierarchy. This property is read only.

**`Window.trustedTypes` Read only**

Returns the `TrustedTypePolicyFactory` object associated with the global object, providing the entry point for using the Trusted Types API.

**`Window.viewport` Read only**

Returns a `Viewport` object instance, which provides information about the current state of the device's viewport.

**`Window.visualViewport` Read only**

Returns a `VisualViewport` object which represents the visual viewport for a given window.

**`Window.window` Read only**

Returns a reference to the current window.

**`window[0]`, `window[1]`, etc.**

Returns a reference to the `window` object in the frames. See `Window.frames` for more details.

**Named properties**

Some elements in the document are also exposed as window properties:

- For each `<embed>`, `<form>`, `<iframe>`, `<img>`, and `<object>` element, its `name` (if non-empty) is exposed. For example, if the document contains `<form name="my_form">`, then `window["my_form"]` (and its equivalent `window.my_form`) returns a reference to that element.
- For each HTML element, its `id` (if non-empty) is exposed.

If a property corresponds to a single element, that element is directly returned. If the property corresponds to multiple elements, then an `HTMLCollection` is returned containing all of them. If any of the elements is a navigable `<iframe>` or `<object>`, then the `contentWindow` of first such iframe is returned instead.

### Deprecated properties

**`Window.event` Read only**

Returns the **current event**, which is the event currently being handled by the JavaScript code's context, or `undefined` if no event is currently being handled. The `Event` object passed directly to event handlers should be used instead whenever possible.

**`Window.external` Read only**

Returns an object with functions for adding external search providers to the browser.

**`Window.orientation` Read only**

Returns the orientation in degrees (in 90 degree increments) of the viewport relative to the device's natural orientation.

**`Window.status`**

Gets/sets the text in the statusbar at the bottom of the browser.

## Instance methods

*This interface inherits methods from the `EventTarget` interface.*

**`Window.atob()`**

Decodes a string of data which has been encoded using base-64 encoding.

**`Window.alert()`**

Displays an alert dialog.

**`Window.blur()`**

Sets focus away from the window.

**`Window.btoa()`**

Creates a base-64 encoded ASCII string from a string of binary data.

**`Window.cancelAnimationFrame()`**

Enables you to cancel a callback previously scheduled with `Window.requestAnimationFrame`.

**`Window.cancelIdleCallback()`**

Enables you to cancel a callback previously scheduled with `Window.requestIdleCallback`.

**`Window.clearInterval()`**

Cancels the repeated execution set using `Window.setInterval()`.

**`Window.clearTimeout()`**

Cancels the delayed execution set using `Window.setTimeout()`.

**`Window.close()`**

Closes the current window.

**`Window.confirm()`**

Displays a dialog with a message that the user needs to respond to.

**`Window.createImageBitmap()`**

Accepts a variety of different image sources, and returns a `Promise` which resolves to an `ImageBitmap`. Optionally the source is cropped to the rectangle of pixels originating at *(sx, sy)* with width sw, and height sh.

**`Window.dump()`**

Writes a message to the console.

**`Window.fetch()`**

Starts the process of fetching a resource from the network.

**`Window.fetchLater()`**

Creates a deferred fetch, which is sent once the page is navigated away from (it is destroyed or enters the bfcache), or after a provided `activateAfter` timeout — whichever comes first.

**`Window.find()`**

Searches for a given string in a window.

**`Window.focus()`**

Sets focus on the current window.

**`Window.getComputedStyle()`**

Gets computed style for the specified element. Computed style indicates the computed values of all CSS properties of the element.

**`Window.getDefaultComputedStyle()`**

Gets default computed style for the specified element, ignoring author stylesheets.

**`Window.getScreenDetails()` Secure context**

Returns a `Promise` that fulfills with a `ScreenDetails` object instance representing the details of all the screens available to the user's device.

**`Window.getSelection()`**

Returns the selection object representing the selected item(s).

**`Window.matchMedia()`**

Returns a `MediaQueryList` object representing the specified media query string.

**`Window.moveBy()`**

Moves the current window by a specified amount.

**`Window.moveTo()`**

Moves the window to the specified coordinates.

**`Window.open()`**

Opens a new window.

**`Window.postMessage()`**

Provides a secure means for one window to send a string of data to another window, which need not be within the same domain as the first.

**`Window.print()`**

Opens the Print Dialog to print the current document.

**`Window.prompt()`**

Returns the text entered by the user in a prompt dialog.

**`Window.queryLocalFonts()` Secure context**

Returns a `Promise` that fulfills with an array of `FontData` objects representing the font faces available locally.

**`Window.queueMicrotask()`**

Queues a microtask to be executed at a safe time prior to control returning to the browser's event loop.

**`Window.reportError()`**

Reports an error in a script, emulating an unhandled exception.

**`Window.requestAnimationFrame()`**

Tells the browser that an animation is in progress, requesting that the browser schedule a repaint of the window for the next animation frame.

**`Window.requestIdleCallback()`**

Enables the scheduling of tasks during a browser's idle periods.

**`Window.resizeBy()`**

Resizes the current window by a certain amount.

**`Window.resizeTo()`**

Dynamically resizes window.

**`Window.scroll()`**

Scrolls the window to a particular place in the document.

**`Window.scrollBy()`**

Scrolls the document in the window by the given amount.

**`Window.scrollByLines()`**

Scrolls the document by the given number of lines.

**`Window.scrollByPages()`**

Scrolls the current document by the specified number of pages.

**`Window.scrollTo()`**

Scrolls to a particular set of coordinates in the document.

**`Window.setInterval()`**

Schedules a function to execute every time a given number of milliseconds elapses.

**`Window.setTimeout()`**

Schedules a function to execute in a given amount of time.

**`Window.showDirectoryPicker()` Secure context**

Displays a directory picker which allows the user to select a directory.

**`Window.showOpenFilePicker()` Secure context**

Shows a file picker that allows a user to select a file or multiple files.

**`Window.showSaveFilePicker()` Secure context**

Shows a file picker that allows a user to save a file.

**`Window.sizeToContent()`**

Sizes the window according to its content.

**`Window.stop()`**

This method stops window loading.

**`Window.structuredClone()`**

Creates a deep clone of a given value using the structured clone algorithm.

### Deprecated methods

**`Window.captureEvents()`**

Registers the window to capture all events of the specified type.

**`Window.clearImmediate()`**

Cancels the repeated execution set using `setImmediate()`.

**`Window.releaseEvents()`**

Releases the window from trapping events of a specific type.

**`Window.requestFileSystem()`**

Lets a website or app gain access to a sandboxed file system for its own use.

**`Window.setImmediate()`**

Executes a function after the browser has finished other heavy tasks.

**`Window.setResizable()`**

Does nothing (no-op). Kept for backward compatibility with Netscape 4.x.

**`Window.webkitConvertPointFromNodeToPage()`**

Transforms a `WebKitPoint` from the node's coordinate system to the page's coordinate system.

**`Window.webkitConvertPointFromPageToNode()`**

Transforms a `WebKitPoint` from the page's coordinate system to the node's coordinate system.

## Events

Listen to these events using `addEventListener()` or by assigning an event listener to the `oneventname` property of this interface. In addition to the events listed below, many events can bubble from the `Document` contained in the window object.

**`error`**

Fired when a resource failed to load, or can't be used. For example, if a script has an execution error or an image can't be found or is invalid.

**`languagechange`**

Fired at the global scope object when the user's preferred language changes.

**`resize`**

Fired when the window has been resized.

**`storage`**

Fired when a storage area (`localStorage` or `sessionStorage`) has been modified in the context of another document.

### Connection events

**`offline`**

Fired when the browser has lost access to the network and the value of `navigator.onLine` has switched to `false`.

**`online`**

Fired when the browser has gained access to the network and the value of `navigator.onLine` has switched to `true`.

### Device orientation events

**`devicemotion` Secure context**

Fired at a regular interval, indicating the amount of physical force of acceleration the device is receiving and the rate of rotation, if available.

**`deviceorientation` Secure context**

Fired when fresh data is available from the magnetometer orientation sensor about the current orientation of the device as compared to the Earth coordinate frame.

**`deviceorientationabsolute` Secure context**

Fired when fresh data is available from the magnetometer orientation sensor about the current absolute orientation of the device as compared to the Earth coordinate frame.

### Focus events

**`blur`**

Fired when an element has lost focus.

**`focus`**

Fired when an element has gained focus.

### Gamepad events

**`gamepadconnected`**

Fired when the browser detects that a gamepad has been connected or the first time a button/axis of the gamepad is used.

**`gamepaddisconnected`**

Fired when the browser detects that a gamepad has been disconnected.

### History events

**`hashchange`**

Fired when the fragment identifier of the URL has changed (the part of the URL beginning with and following the `#` symbol).

**`pagehide`**

Sent when the browser hides the current document while in the process of switching to displaying in its place a different document from the session's history. This happens, for example, when the user clicks the Back button or when they click the Forward button to move ahead in session history.

**`pagereveal`**

Fired when a document is first rendered, either when loading a fresh document from the network or activating a document (either from back/forward cache (bfcache) or prerender).

**`pageshow`**

Sent when the browser makes the document visible due to navigation tasks, including not only when the page is first loaded, but also situations such as the user navigating back to the page after having navigated to another within the same tab.

**`pageswap`**

Fired when a document is about to be unloaded due to a navigation.

**`popstate`**

Fired when the active history entry changes.

### Load & unload events

**`beforeunload`**

Fired when the window, the document and its resources are about to be unloaded.

**`load`**

Fired when the whole page has loaded, including all dependent resources such as stylesheets images.

**`unload`**

Fired when the document or a child resource is being unloaded.

### Manifest events

**`appinstalled`**

Fired when the browser has successfully installed a page as an application.

**`beforeinstallprompt`**

Fired when a user is about to be prompted to install a web application.

### Messaging events

**`message`**

Fired when the window receives a message, for example from a call to `Window.postMessage()` from another browsing context.

**`messageerror`**

Fired when a `Window` object receives a message that can't be deserialized.

### Print events

**`afterprint`**

Fired after the associated document has started printing or the print preview has been closed.

**`beforeprint`**

Fired when the associated document is about to be printed or previewed for printing.

### Promise rejection events

**`rejectionhandled`**

Sent every time a JavaScript `Promise` is rejected, regardless of whether or not there is a handler in place to catch the rejection.

**`unhandledrejection`**

Sent when a JavaScript `Promise` is rejected but there is no handler in place to catch the rejection.

### Scroll events

**`scrollsnapchange`**

Fired on the scroll container at the end of a scrolling operation when a new scroll snap target has been selected.

**`scrollsnapchanging`**

Fired on the scroll container when the browser determines a new scroll snap target is pending, i.e., it will be selected when the current scroll gesture ends.

### Deprecated events

**`orientationchange`**

Fired when the orientation of the device has changed.

**`vrdisplayactivate`**

Fired when a display is able to be presented to.

**`vrdisplayconnect`**

Fired when a compatible VR device has been connected to the computer.

**`vrdisplaydisconnect`**

Fired when a compatible VR device has been disconnected from the computer.

**`vrdisplaydeactivate`**

Fired when a display can no longer be presented to.

**`vrdisplaypresentchange`**

Fired when the presenting state of a VR device changes — i.e., goes from presenting to not presenting, or vice versa.

### Bubbled events

Not all events that bubble can reach the `Window` object. Only the following do and can be listened for on the `Window` object:

- `abort`
- `auxclick`
- `beforeinput`
- `beforematch`
- `beforetoggle`
- `cancel`
- `canplay`
- `canplaythrough`
- `change`
- `click`
- `close`
- `contextlost`
- `contextmenu`
- `contextrestored`
- `copy`
- `cuechange`
- `cut`
- `dblclick`
- `drag`
- `dragend`
- `dragenter`
- `dragleave`
- `dragover`
- `dragstart`
- `drop`
- `durationchange`
- `emptied`
- `ended`
- `formdata`
- `input`
- `invalid`
- `keydown`
- `keypress`
- `keyup`
- `loadeddata`
- `loadedmetadata`
- `loadstart`
- `mousedown`
- `mouseenter`
- `mouseleave`
- `mousemove`
- `mouseout`
- `mouseover`
- `mouseup`
- `paste`
- `pause`
- `play`
- `playing`
- `progress`
- `ratechange`
- `reset`
- `scrollend`
- `securitypolicyviolation`
- `seeked`
- `seeking`
- `select`
- `slotchange`
- `stalled`
- `submit`
- `suspend`
- `timeupdate`
- `toggle`
- `volumechange`
- `waiting`
- `wheel`

## Interfaces

See DOM Reference.

## Listening for events on Window

HTML elements have three ways to listen for events:

- Add an event listener to the element using the `EventTarget.addEventListener` method.
- Assign an event handler to the element's `oneventname` property in JavaScript.
- Add an `on`-prefixed attribute to the element in the HTML.

To listen for events on `Window` objects, in general, you can only use the first two methods, because `Window` has no corresponding HTML element. However, there's a specific group of events whose listeners can be added to the `<body>` (or the deprecated `<frameset>`) element that's owned by the `Window`'s document, using the second or third methods. These events are:

- `afterprint`
- `beforeprint`
- `beforeunload`
- `blur`
- `error`
- `focus`
- `hashchange`
- `languagechange`
- `load`
- `message`
- `messageerror`
- `offline`
- `online`
- `pagehide`
- `pagereveal`
- `pageshow`
- `pageswap`
- `popstate`
- `rejectionhandled`
- `resize`
- `scroll`
- `storage`
- `unhandledrejection`
- `unload`

This means the following are strictly equivalent:

```js
window.onresize = (e) => console.log(e.currentTarget);
document.body.onresize = (e) => console.log(e.currentTarget);
```

```html
<body onresize="console.log(event.currentTarget)"></body>
```

In all three cases, you see the `Window` object logged as `currentTarget`.

## Specifications

| Specification |
|---|
| HTML # the-window-object |

## Browser compatibility
