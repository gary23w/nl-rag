---
title: "Framekiller"
source: https://en.wikipedia.org/wiki/Framekiller
domain: clickjacking-prevention
license: CC-BY-SA-4.0
tags: clickjacking defense, ui redress attack, frame ancestors policy, frame busting technique
fetched: 2026-07-02
---

# Framekiller

A **framekiller** (or **framebuster** or **framebreaker**) is a technique used by websites and web applications to prevent their web pages from being displayed within an HTML frame element. A frame is a subdivision of a Web browser window and can act like a smaller window. A framekiller is usually used to prevent a website from being loaded from within a frameset without permission, which might be part of an attack, as with clickjacking.

Framekiller scripts have largely been replaced by the usage of `X-Frame-Options` and `Content-Security-Policy` headers, which prevent the page from being loaded in a frame in the first place. These headers are supported by all modern browsers and do not require the use of JavaScript. These headers are also intended to be specified inside the web server software, rather than directly inside the HTML.

## Implementations

Framekillers are implemented using JavaScript that validates if the current window is the main window. The recommended approach is to block rendering of the window by default and only unblock it after confirming the current window is the main one:

```mw
<style>html {display: none;}</style>
<script>
    if (self == top) {
        document.documentElement.style.display = 'block'; 
    } else {
        top.location = self.location; 
    }
</script>
```

This approach was proposed in 2010 by Gustav Rydstedt, Elie Bursztein, Dan Boneh and Collin Jackson in a paper that highlighted the limitations of existing frame-busting techniques along with techniques allowing to bypass them.

### Alternative solutions

An alternative choice is to allow the user to determine whether to let the framekiller work.

```mw
var framekiller = false;
window.onbeforeunload = function() { 
  if (framekiller) {
    return "...";  // any message that helps user to make decision
  }
};
```

and the code below should be added after the frame tag:

```mw
// "my_frame" should be changed according to the real id of the frame in your page 
document.getElementById("my_frame").onload = function() { 
  framekiller = true;
};
```

### Original framekillers

Historically, the first framekiller scripts were as simple as this:

```mw
<script type="text/javascript">
  if (top != self) top.location.replace(location);
</script>
```

The logic here was to display the page, but check if the top location is the same as the current page, and replace the top by current if not. This method however can be easily bypassed by blocking execution of the framebuster script from the outer frame.

## Framekiller limitations

Client-side JavaScript solution relies on the end-user's browser enforcing their own security. This makes it a beneficial, but unreliable, means of disallowing your page to be embedded in other pages. The following situations may render the script above useless:

- The user agent does not support JavaScript.
- The user agent supports JavaScript but the user has turned support off.
- The user agent's JavaScript support is flawed or partially implemented.

## Anti-framekiller

The iframe in HTML5 has a sandbox attribute. The attribute's value is a set of allowed capabilities for the iframe's content. If the value is empty or not set, the iframe's content will not execute JavaScript, and won't allow top-level navigation. By specifying allow-scripts in the space separated set of exceptions in the value, the iframe will allow JavaScript, but will still disallow top-level navigation, rendering framekillers in the iframe impotent.
