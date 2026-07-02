---
title: "Canvas element"
source: https://en.wikipedia.org/wiki/Canvas_element
domain: canvas-api
license: CC-BY-SA-2.5
tags: canvas api, canvas element, 2d rendering context, canvasrenderingcontext2d
fetched: 2026-07-02
---

# Canvas element

The HTML **canvas element** allows for dynamic, scriptable rendering of 2D shapes and bitmap images. Introduced in HTML5, it is a low level, procedural model that updates a bitmap. The `<canvas>` element also helps in making 2D games.

While the `<canvas>` element offers its own 2D drawing API, it also supports the WebGL API to allow 3D rendering with OpenGL ES.

## History

Canvas was initially introduced by Apple for use in their own Mac OS X WebKit component in 2004, powering applications like Dashboard widgets and the Safari browser. Later, in 2005, it was adopted in version 1.8 of Gecko browsers, and Opera in 2006, and standardized by the Web Hypertext Application Technology Working Group (WHATWG) on new proposed specifications for next generation web technologies.

## Usage

A `canvas` consists of a drawable region defined in HTML code with *height* and *width* attributes. JavaScript code may access the area through a full set of drawing functions similar to those of other common 2D APIs, thus allowing for dynamically generated graphics. Some anticipated uses of canvas include building graphs, animations, games, and image composition.

Interacting with the canvas involves obtaining the canvas' rendering context, which determines whether to use the canvas API, WebGL, or WebGL2 rendering context.

## Example

The following code creates a `<canvas>` element in an HTML page:

```mw
<canvas id="example" width="200" height="200">
This text is displayed if your browser does not support HTML canvas element.
</canvas>
```

Using JavaScript, you can draw on the canvas:

```mw
var example = document.getElementById('example');
var context = example.getContext('2d');
context.fillStyle = 'red';
context.fillRect(30, 30, 50, 50);
```

This code draws a red rectangle on the screen.

The Canvas API also provides `save()` and `restore()`, for saving and restoring all the canvas context's attributes.

## Canvas element size versus drawing surface size

A canvas actually has two sizes: the size of the element itself and the size of the element's drawing surface. Setting the element's width and height attributes sets both of these sizes; CSS attributes affect only the element's size and not the drawing surface.

By default, both the canvas element's size and the size of its drawing surface is 300 screen pixels wide and 150 screen pixels high. In the listing shown in the example, which uses CSS to set the canvas element's size, the size of the element is 600 pixels wide and 300 pixels high, but the size of the drawing surface remains unchanged at the default value of 300 pixels × 150 pixels. When a canvas element's size does not match the size of its drawing surface, the browser scales the drawing surface to fit the element (which may result in surprising and unwanted effects).

Example setting element size and drawing surface size to different values:

```mw
<!DOCTYPE html>
<html>
    <head>
    <title>Canvas element size: 600 x 300,
    Canvas drawing surface size: 300 x 150</title>
    <style>
        body {
            background: #dddddd;
        }
        #canvas {
            margin: 20px;
            padding: 20px;
            background: #ffffff;
            border: thin inset #aaaaaa;
            width: 600px;
            height: 300px;
        }
    </style>
    </head>
    <body>
        <canvas id="canvas">
        Canvas not supported
        </canvas>
    </body>
</html>
```

## Canvas versus Scalable Vector Graphics (SVG)

SVG is an alternative approach to drawing shapes in browsers. Unlike canvas, which is raster-based, SVG is vector-based, so that each drawn shape is remembered as an object in a scene graph or Document Object Model, which is subsequently rendered to a bitmap. This means that if attributes of an SVG object are changed, the browser can automatically re-render the scene.

Canvas objects, on the other hand, are drawn in immediate mode. In the canvas example above, the rectangle draw operation modifies the canvas, and its representation as a rectangle is forgotten by the system. If the rectangle's position were to be changed, the canvas would need to be redrawn, including any objects that might have been covered by the rectangle. In the equivalent SVG case, one could simply change the position attributes of the rectangle and the browser would determine how to repaint it. There are additional JavaScript libraries that abstract the canvas model to have svg-like scene capabilities within the canvas element. Multiple canvas layers can also be used, meaning that only specific layers need to be recreated when changes are required.

SVG images are represented in XML, and complex scenes can be created and maintained with XML editing tools.

The SVG scene graph enables event handlers to be associated with objects, so a rectangle may respond to an `onClick` event. To get the same functionality with canvas, one must manually match the coordinates of the mouse click with the coordinates of the drawn rectangle to determine whether it was clicked.

Conceptually, canvas is a lower-level API upon which higher-level interfaces might be built (for example, SVG support). There are JavaScript libraries that provide partial SVG implementations using canvas for browsers that do not provide SVG but support canvas, such as the browsers in Android 2.x. However, this is not normally the case—they are independent standards. The situation is complicated because there are scene graph libraries for canvas, and SVG has some bitmap manipulation functionality.

## Reactions

At the time of its introduction, the canvas element was met with mixed reactions from the web standards community. There have been arguments against Apple's decision to create a new proprietary element instead of supporting the SVG standard. There are other concerns about syntax, such as the absence of a namespace.

### Intellectual property over canvas

On March 14, 2007, WebKit developer Dave Hyatt forwarded an email from Apple's Senior Patent Counsel, Helene Plotka Workman, which stated that Apple reserved all intellectual property rights relative to WHATWG's Web Applications 1.0 Working Draft, dated March 24, 2005, Section 10.1, entitled "Graphics: The bitmap canvas", but left the door open to licensing the patents should the specification be transferred to a standards body with a formal patent policy. This caused considerable discussion among web developers and raised questions concerning the WHATWG's lack of a policy on patents in comparison to the World Wide Web Consortium (W3C)'s explicit favoring of royalty-free licenses. Apple later disclosed the patents under the W3C's royalty-free patent licensing terms. The disclosure means that Apple is required to provide royalty-free licensing for the patent whenever the Canvas element becomes part of a future W3C recommendation created by the HTML working group.

### Privacy concerns

Canvas fingerprinting is one of a number of browser fingerprinting techniques for tracking online users that allow websites to identify and track visitors using the HTML `<canvas>` element. The technique received wide media coverage in 2014, after researchers from Princeton University and KU Leuven University described it in their paper *The Web never forgets*. The privacy concerns regarding canvas fingerprinting center around the fact that even deleting cookies and clearing the cache will not be sufficient for users to avoid online tracking.

## Browser support

The element is supported by the current versions of Mozilla Firefox, Google Chrome, Internet Explorer, Safari, Konqueror, Opera and Microsoft Edge.
