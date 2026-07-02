---
title: "PaintWorkletGlobalScope - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/PaintWorklet
domain: css-paint-api
license: CC-BY-SA-4.0
tags: css painting api, paint worklet registration, programmatic css background, custom paint function
fetched: 2026-07-02
---

# PaintWorkletGlobalScope

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

The **`PaintWorkletGlobalScope`** interface of the CSS Painting API represents the global object available inside a paint `Worklet`.

## Privacy concerns

To avoid leaking visited links, this feature is currently disabled in Chrome-based browsers for `<a>` elements with an `href` attribute, and for children of such elements. For details, see the following:

- The CSS Painting API Privacy Considerations section
- The CSS Painting API spec issue "CSS Paint API leaks browsing history"

## Instance properties

*This interface inherits properties from `WorkletGlobalScope`.*

**`PaintWorkletGlobalScope.devicePixelRatio` Read only**

Returns the current device's ratio of physical pixels to logical pixels.

## Instance methods

*This interface inherits methods from `WorkletGlobalScope`.*

**`PaintWorkletGlobalScope.registerPaint()`**

Registers a class to programmatically generate an image where a CSS property expects a file.

## Examples

The following three examples go together to show creating, loading, and using a paint `Worklet`.

### Create a paint worklet

The following shows an example worklet module. This should be in a separate js file. Note that `registerPaint()` is called without a reference to a paint `Worklet`.

```js
class CheckerboardPainter {
  paint(ctx, geom, properties) {
    // The global object here is a PaintWorkletGlobalScope
    // Methods and properties can be accessed directly
    // as global features or prefixed using self
    const dpr = self.devicePixelRatio;

    // Use `ctx` as if it was a normal canvas
    const colors = ["red", "green", "blue"];
    const size = 32;
    for (let y = 0; y < geom.height / size; y++) {
      for (let x = 0; x < geom.width / size; x++) {
        const color = colors[(x + y) % colors.length];
        ctx.beginPath();
        ctx.fillStyle = color;
        ctx.rect(x * size, y * size, size, size);
        ctx.fill();
      }
    }
  }
}

// Register our class under a specific name
registerPaint("checkerboard", CheckerboardPainter);
```

### Load a paint worklet

The following example demonstrates loading the above worklet from its js file and does so by feature detection.

```js
if ("paintWorklet" in CSS) {
  CSS.paintWorklet.addModule("checkerboard.js");
}
```

### Use a paint worklet

This example shows how to use a paint `Worklet` in a stylesheet, including the simplest way to provide a fallback if `CSS.paintWorklet` isn't supported.

```css
textarea {
  background-image: url("checkerboard.png"); /* Fallback */
  background-image: paint(checkerboard);
}
```

You can also use the `@supports` at-rule.

```css
@supports (background: paint(id)) {
  textarea {
    background-image: paint(checkerboard);
  }
}
```

## Specifications

| Specification |
|---|
| CSS Painting API Level 1 # paintworkletglobalscope |

## Browser compatibility
