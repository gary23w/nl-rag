---
title: "Graham scan"
source: https://en.wikipedia.org/wiki/Graham_scan
domain: convex-hull-algorithms
license: CC-BY-SA-4.0
tags: convex hull algorithm, graham scan, quickhull method, gift wrapping
fetched: 2026-07-02
---

# Graham scan

**Graham's scan** is a method of finding the convex hull of a finite set of points in the plane with time complexity O(*n* log *n*). It is named after Ronald Graham, who published the original algorithm in 1972. The algorithm finds all vertices of the convex hull ordered along its boundary. It uses a stack to detect and remove concavities in the boundary efficiently.

## Algorithm

The first step in this algorithm is to find the point with the lowest y-coordinate. If the lowest y-coordinate exists in more than one point in the set, the point with the lowest x-coordinate out of the candidates should be chosen. Call this point *P*. This step takes O(*n*), where *n* is the number of points in question.

Next, the set of points must be sorted in increasing order of the angle they and the point *P* make with the x-axis. Any general-purpose sorting algorithm is appropriate for this, for example heapsort (which is O(*n* log *n*)).

Sorting in order of angle does not require computing the angle. It is possible to use any function of the angle which is monotonic in the interval $[0,\pi ]$ . The cosine is easily computed using the dot product, or the slope of the line may be used. If numeric precision is at stake, the comparison function used by the sorting algorithm can use the sign of the cross product to determine relative angles.

If several points are of the same angle, either break ties by increasing distance (Manhattan or Chebyshev distance may be used instead of Euclidean for easier computation, since the points lie on the same ray), or delete all but the furthest point.

The algorithm proceeds by considering each of the points in the sorted array in sequence. For each point, it is first determined whether traveling from the two points immediately preceding this point constitutes making a left turn or a right turn. If a right turn, the second-to-last point is not part of the convex hull, and lies 'inside' it. The same determination is then made for the set of the latest point and the two points that immediately precede the point found to have been inside the hull, and is repeated until a "left turn" set is encountered, at which point the algorithm moves on to the next point in the set of points in the sorted array minus any points that were found to be inside the hull; there is no need to consider these points again. (If at any stage the three points are collinear, one may opt either to discard or to report it, since in some applications it is required to find all points on the boundary of the convex hull.)

Again, determining whether three points constitute a "left turn" or a "right turn" does not require computing the actual angle between the two line segments, and can actually be achieved with simple arithmetic only. For three points $P_{1}=(x_{1},y_{1})$ , $P_{2}=(x_{2},y_{2})$ and $P_{3}=(x_{3},y_{3})$ , compute the *z*-coordinate of the cross product of the two vectors ${\overrightarrow {P_{1}P_{2}}}$ and ${\overrightarrow {P_{1}P_{3}}}$ , which is given by the expression $(x_{2}-x_{1})(y_{3}-y_{1})-(y_{2}-y_{1})(x_{3}-x_{1})$ . If the result is 0, the points are collinear; if it is positive, the three points constitute a "left turn" or counter-clockwise orientation, otherwise a "right turn" or clockwise orientation (for counter-clockwise numbered points).

This process will eventually return to the point at which it started, at which point the algorithm is completed and the stack now contains the points on the convex hull in counterclockwise order.

## Time complexity

Sorting the points has time complexity O(*n* log *n*). While it may seem that the time complexity of the loop is O(*n*2), because for each point it goes back to check if any of the previous points make a "right turn", it is actually O(*n*), because each point is considered at most twice in some sense. Each point can appear only once as a point $(x_{2},y_{2})$ in a "left turn" (because the algorithm advances to the next point $(x_{3},y_{3})$ after that), and as a point $(x_{2},y_{2})$ in a "right turn" (because the point $(x_{2},y_{2})$ is removed). The overall time complexity is therefore O(*n* log *n*), since the time to sort dominates the time to actually compute the convex hull.

## Pseudocode

The pseudocode below uses a function ccw: ccw > 0 if three points make a counter-clockwise turn, ccw < 0 if clockwise, and ccw = 0 if collinear. (In real applications, if the coordinates are arbitrary real numbers, the function requires exact comparison of floating-point numbers, and one has to beware of numeric singularities for "nearly" collinear points.)

Then let the result be stored in the `stack`.

```
let points be the list of points
let stack = empty_stack()

find the lowest y-coordinate and leftmost point, called P0
sort points by polar angle with P0, if several points have the same polar angle then only keep the farthest

for point in points:
    # pop the last point from the stack if we turn clockwise to reach this point
    while count stack > 1 and ccw(next_to_top(stack), top(stack), point) <= 0:
        pop stack
    push point to stack
end
```

Now the stack contains the convex hull, where the points are oriented counter-clockwise and P0 is the first point.

Here, `next_to_top()` is a function for returning the item one entry below the top of stack, without changing the stack, and similarly, `top()` for returning the topmost element.

This pseudocode is adapted from *Introduction to Algorithms*.
