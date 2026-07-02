---
title: "Z-order"
source: https://en.wikipedia.org/wiki/Z-order
domain: sprite-rendering
license: CC-BY-SA-4.0
tags: sprite rendering, sprite sheet, texture atlas, sprite compositing
fetched: 2026-07-02
---

# Z-order

**Z-order** is an ordering of overlapping two-dimensional objects, such as windows in a stacking window manager, shapes in a vector graphics editor, or objects in a 3D application. One of the features of a typical GUI is that windows may overlap, so that one window hides part or all of another. When two windows overlap, their Z-order determines which one appears on top of the other.

## Definition

The term "Z-order" refers to the order of objects along the Z-axis. In coordinate geometry, X typically refers to the horizontal axis (left to right), Y to the vertical axis (up and down), and Z refers to the axis perpendicular to the other two (forward or backward). One can think of the windows in a GUI as a series of planes parallel to the surface of the monitor. The windows are therefore stacked along the Z-axis, and the Z-order information thus specifies the front-to-back ordering of the windows on the screen. An analogy would be some sheets of paper scattered on top of a table, each sheet being a window, the table your computer screen, and the top sheet having the highest Z value.

## Use

Typically, users of a GUI can affect the Z-order by selecting a window to be brought to the foreground (that is, "above" or "in front of" all the other windows). Some window managers allow interaction with windows while they are not in the foreground, while others will bring a window to the front whenever it receives input from the user. It is also possible for special windows to be designated "always on top"; these are then fixed to the top of the Z-order so that (with few exceptions) no other window can overlap them.

When dealing with visual objects on a computer screen, an object with a Z-order of 1 would be visually "underneath" an object with a Z-order of 2 or greater. This is the same as making "layers" of objects where the Z-order determines what object is on top of another. An HTML page can use CSS to specify the Z-order so that some objects can be layered over others.

Z-ordering is also used in 3D applications to determine object visibility based on overlap from other objects. This confers a speed advantage to the user as the computer does not need to render unseen objects. In practice, of course, some objects may be only partially obscured, and this is a complication that must be taken into account.

In early real-time 3D graphics, Z-order was applied on a per-polygon basis to avoid using Z-buffer, which was considered expensive at the time. In modern 3D graphics, Z-order is used for order-dependent rendering, for example with semi-transparent objects. It can also be used to reduce the problem of Z-fighting, by either rendering farther objects first and then using weak inequality as the depth test or, conversely, rendering front-to-back and using strict inequality.

## z-index

The actual number assigned to a particular place in the Z-order is sometimes known as the z-index. In particular the CSS property that sets the stack order of specific elements is known as the z-index. An element with greater stack order is always in front of another element with lower stack order.

Negative values can also be used in the same manner. A negative value will appear behind a positive one. `z-index` only works on elements that have a position value (e.g. `position: relative;`) and for many coders, this one of the first things to investigate when debugging why the z-index isn't working.

Like all other CSS properties, it can be set with JavaScript, with the following syntax:

```mw
object.style.zIndex = 1;
```
