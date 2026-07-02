---
title: "Hit-testing"
source: https://en.wikipedia.org/wiki/Hit-testing
domain: intersection-observer-deep
license: CC-BY-SA-4.0
tags: intersection observer internals, root margin threshold, intersection ratio callback, viewport visibility tracking
fetched: 2026-07-02
---

# Hit-testing

In computer graphics programming, **hit-testing** (**hit detection**, **picking**, or **pick correlation**) is the process of determining whether a user-controlled cursor (such as a mouse cursor or touch-point on a touch-screen interface) intersects a given graphical object (such as a shape, line, or curve) drawn on the screen. Hit-testing may be performed on the movement or activation of a mouse or other pointing device.

Hit-testing is used by GUI environments to respond to user actions, such as selecting a menu item or a target in a game based on its visual location. In web programming languages such as HTML, SVG, and CSS, this is associated with the concept of pointer-events (e.g. user-initiated cursor movement or object selection).

Collision detection is a related concept for detecting intersections of two or more different graphical objects, rather than intersection of a cursor with one or more graphical objects.

## Algorithm

There are many different algorithms that may be used to perform hit-testing, with different performance or accuracy outcomes. One common hit-test algorithm for axis aligned bounding boxes. A key idea is that the box being tested must be either entirely above, entirely below, entirely to the right or left of the current box. If this is not possible, they are colliding. Example logic is presented in the pseudo-code below:

```mw
function HitTest(Rectangle r1, Rectangle r2) returns boolean
{
    return not((r1.X + r1.Width < r2.X) or (r1.X > r2.X + r2.Width) or (r1.Y + r1.Height < r2.Y) or (r1.Y > r2.Y + r2.Height));
}
```

In Python:

```mw
def hit_test(r1: Rectangle, r2: Rectangle) -> bool:
    """Return true if it hits else return false."""
    return not (
        (r1.x + r1.width < r2.x) or
        (r1.x > r2.x + r2.width) or
        (r1.y + r1.height < r2.y) or
        (r1.y > r2.y + r2.height)
    )
```
