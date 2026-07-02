---
title: "Animation - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/Animation
domain: web-animations
license: CC-BY-SA-2.5
tags: web animations api, keyframe animation, css transition, animation timeline
fetched: 2026-07-02
---

# Animation

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2020.

- Learn more
- See full compatibility

The **`Animation`** interface of the Web Animations API represents a single animation player and provides playback controls and a timeline for an animation node or source.

## Constructor

**`Animation()`**

Creates a new `Animation` object instance.

## Instance properties

**`Animation.currentTime`**

The current time value of the animation in milliseconds, whether running or paused. If the animation lacks a `timeline`, is inactive or hasn't been played yet, its value is `null`.

**`Animation.effect`**

Gets and sets the `AnimationEffect` associated with this animation. This will usually be a `KeyframeEffect` object.

**`Animation.finished` Read only**

Returns the current finished Promise for this animation.

**`Animation.id`**

Gets and sets the `String` used to identify the animation.

**`Animation.overallProgress` Read only**

Returns a number between `0` and `1` indicating the animation's overall progress towards its finished state.

**`Animation.pending` Read only**

Indicates whether the animation is currently waiting for an asynchronous operation such as initiating playback or pausing a running animation.

**`Animation.playState` Read only**

Returns an enumerated value describing the playback state of an animation.

**`Animation.playbackRate`**

Gets or sets the playback rate of the animation.

**`Animation.ready` Read only**

Returns the current ready Promise for this animation.

**`Animation.replaceState` Read only**

Indicates whether the animation is active, has been automatically removed after being replaced by another animation, or has been explicitly persisted by a call to `Animation.persist()`.

**`Animation.startTime`**

Gets or sets the scheduled time when an animation's playback should begin.

**`Animation.timeline`**

Gets or sets the `timeline` associated with this animation.

## Instance methods

**`Animation.cancel()`**

Clears all `keyframeEffects` caused by this animation and aborts its playback.

**`Animation.commitStyles()`**

Commits the current styling state of an animation to the element being animated, even after that animation has been removed. It will cause the current styling state to be written to the element being animated, in the form of properties inside a `style` attribute.

**`Animation.finish()`**

Seeks either end of an animation, depending on whether the animation is playing or reversing.

**`Animation.pause()`**

Suspends playing of an animation.

**`Animation.persist()`**

Explicitly persists an animation, preventing it from being automatically removed when another animation replaces it.

**`Animation.play()`**

Starts or resumes playing of an animation, or begins the animation again if it previously finished.

**`Animation.reverse()`**

Reverses playback direction, stopping at the start of the animation. If the animation is finished or unplayed, it will play from end to beginning.

**`Animation.updatePlaybackRate()`**

Sets the speed of an animation after first synchronizing its playback position.

## Events

**`cancel`**

Fires when the `Animation.cancel()` method is called or when the animation enters the `"idle"` play state from another state.

**`finish`**

Fires when the animation finishes playing.

**`remove`**

Fires when the animation is automatically removed by the browser.

## Accessibility concerns

Blinking and flashing animation can be problematic for people with cognitive concerns such as Attention Deficit Hyperactivity Disorder (ADHD). Additionally, certain kinds of motion can be a trigger for Vestibular disorders, epilepsy, and migraine, and Scotopic sensitivity.

Consider providing a mechanism for pausing or disabling animation, as well as using the Reduced Motion Media Query (or equivalent user agent client hint `Sec-CH-Prefers-Reduced-Motion`) to create a complimentary experience for users who have expressed a preference for no animated experiences.

- Designing Safer Web Animation For Motion Sensitivity · An A List Apart Article
- An Introduction to the Reduced Motion Media Query | CSS-Tricks
- Responsive Design for Motion | WebKit
- MDN Understanding WCAG, Guideline 2.2 explanations
- Understanding Success Criterion 2.2.2 | W3C Understanding WCAG 2.0

## Specifications

| Specification |
|---|
| Web Animations # the-animation-interface |

## Browser compatibility
