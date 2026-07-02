---
title: "IdleDeadline - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/IdleDeadline
domain: requestidlecallback
license: CC-BY-SA-4.0
tags: request idle callback, idle period scheduling, background task deadline, cooperative task chunking
fetched: 2026-07-02
---

# IdleDeadline

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

The `IdleDeadline` interface is used as the data type of the input parameter to idle callbacks established by calling `Window.requestIdleCallback()`. It offers a method, `timeRemaining()`, which lets you determine how much longer the user agent estimates it will remain idle and a property, `didTimeout`, which lets you determine if your callback is executing because its timeout duration expired.

To learn more about how request callbacks work, see Collaborative Scheduling of Background Tasks.

## Instance properties

**`IdleDeadline.didTimeout` Read only**

A Boolean whose value is `true` if the callback is being executed because the timeout specified when the idle callback was installed has expired.

## Instance methods

**`IdleDeadline.timeRemaining()`**

Returns a `DOMHighResTimeStamp`, which is a floating-point value providing an estimate of the number of milliseconds remaining in the current idle period. If the idle period is over, the value is 0. Your callback can call this repeatedly to see if there's enough time left to do more work before returning.

## Example

See our complete example in the article Cooperative Scheduling of Background Tasks API.

## Specifications

| Specification |
|---|
| requestIdleCallback() # the-idledeadline-interface |

## Browser compatibility
