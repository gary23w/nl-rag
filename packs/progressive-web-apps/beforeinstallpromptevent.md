---
title: "BeforeInstallPromptEvent - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/BeforeInstallPromptEvent
domain: progressive-web-apps
license: CC-BY-SA-2.5
tags: progressive web app, pwa, web app manifest, installable web app
fetched: 2026-07-02
---

# BeforeInstallPromptEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The **`BeforeInstallPromptEvent`** is the interface of the `beforeinstallprompt` event fired at the `Window` object before a user is prompted to "install" a website to a home screen on mobile.

This interface inherits from the `Event` interface.

## Constructor

**`BeforeInstallPromptEvent()`**

Creates a new `BeforeInstallPromptEvent` object.

## Instance properties

*Inherits properties from its parent, `Event`.*

**`BeforeInstallPromptEvent.platforms` Read only**

Returns an array of string items containing the platforms on which the event was dispatched. This is provided for user agents that want to present a choice of versions to the user such as, for example, "web" or "play" which would allow the user to choose between a web version or an Android version.

**`BeforeInstallPromptEvent.userChoice` Read only**

Returns a `Promise` that resolves to an object describing the user's choice when they were prompted to install the app.

## Instance methods

**`BeforeInstallPromptEvent.prompt()`**

Show a prompt asking the user if they want to install the app. This method returns a `Promise` that resolves to an object describing the user's choice when they were prompted to install the app.

## Examples

In the following example an app provides its own install button, which has an `id` of `"install"`. Initially the button is hidden.

```html
<button id="install" hidden>Install</button>
```

The `beforeinstallprompt` handler:

- Cancels the event, which prevents the browser displaying its own install UI on some platforms
- Assigns the `BeforeInstallPromptEvent` object to a variable, so it can be used later
- Reveals the app's install button.

```js
let installPrompt = null;
const installButton = document.querySelector("#install");

window.addEventListener("beforeinstallprompt", (event) => {
  event.preventDefault();
  installPrompt = event;
  installButton.removeAttribute("hidden");
});
```

When clicked, the app's install button:

- Calls the `prompt()` method of the stored event object, to trigger the installation prompt.
- Resets its state by clearing the `installPrompt` variable and hiding itself again.

```js
installButton.addEventListener("click", async () => {
  if (!installPrompt) {
    return;
  }
  const result = await installPrompt.prompt();
  console.log(`Install prompt was: ${result.outcome}`);
  installPrompt = null;
  installButton.setAttribute("hidden", "");
});
```

## Browser compatibility
