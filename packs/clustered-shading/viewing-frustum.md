---
title: "Viewing frustum"
source: https://en.wikipedia.org/wiki/Viewing_frustum
domain: clustered-shading
license: CC-BY-SA-4.0
tags: clustered shading, tiled deferred shading, light culling clusters, clustered forward shading
fetched: 2026-07-02
---

# Viewing frustum

In 3D computer graphics, a **viewing frustum** or **view frustum** is the region of space in the modeled world that may appear on the screen; it is the field of view of a perspective virtual camera system.

The view frustum is typically obtained by taking a geometrical frustum—that is a truncation with parallel planes—of the **pyramid of vision**, which is the adaptation of (idealized) *cone of vision* that a camera or eye would have to the rectangular viewports typically used in computer graphics. Some authors use *pyramid of vision* as a synonym for view frustum itself, i.e. consider it truncated.

The exact shape of this region varies depending on what kind of camera lens is being simulated, but typically it is a frustum of a rectangular pyramid (hence the name). The planes that cut the frustum perpendicular to the viewing direction are called the *near plane* and the *far plane*. Objects closer to the camera than the near plane or beyond the far plane are not drawn. Sometimes, the far plane is placed infinitely far away from the camera so all objects within the frustum are drawn regardless of their distance from the camera.

Viewing-frustum culling is the process of removing from the rendering process those objects that lie completely outside the viewing frustum. Rendering these objects would be a waste of resources since they are not directly visible. To make culling fast, it is usually done using bounding volumes surrounding the objects rather than the objects themselves.

## Definitions

**VPN**

the view-plane normal – a

normal

to the view plane.

**VUV**

the view-up vector – the vector on the view plane that indicates the upward direction.

**VRP**

the viewing reference point – a point located on the view plane, and the origin of the VRC.

**PRP**

the projection reference point – the point where the image is projected from, for parallel projection, the PRP is at infinity.

**VRC**

the viewing-reference coordinate system.

The geometry is defined by a field of view angle (in the 'y' direction), as well as an aspect ratio. Further, a set of z-planes define the **near and far bounds** of the frustum. Together this information can be used to calculate a projection matrix for rendering transformation in a graphics pipeline.
