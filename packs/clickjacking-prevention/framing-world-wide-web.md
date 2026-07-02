---
title: "Frame (World Wide Web)"
source: https://en.wikipedia.org/wiki/Framing_(World_Wide_Web)
domain: clickjacking-prevention
license: CC-BY-SA-4.0
tags: clickjacking defense, ui redress attack, frame ancestors policy, frame busting technique
fetched: 2026-07-02
---

# Frame (World Wide Web)

(Redirected from

Framing (World Wide Web)

)

In the context of a web browser, a **frame** is a part of a web page or browser window which displays content independent of its container, with the ability to load content independently. The HTML or media elements in a frame may come from a web site distinct from the site providing the enclosing content. This practice, known as **framing**, is today often regarded as a violation of same-origin policy.

In HTML, a **frameset** is a group of named frames to which web pages and media can be directed; an **iframe** provides for a frame to be placed inside the body of a document.

Since the early 2000s, concern for usability and accessibility has motivated diminished use of framesets and the HTML5 standard does not support them.

## Tags and attributes

The frames in HTML are created using the `<frameset></frameset>` tag pair. The `<frameset>` tag is a container tag for all other tags that are used to create frames. The `<frameset>` tag replaces the `<body>` tag in frameset documents.The `<frameset>` tag defines how to divide the window into frames.

Each frameset defines a set of rows or columns. If user define frames by using the `rows` attribute then horizontal frames are created. If user define frames by using `cols` then vertical frames are created.

The `<noframes>` element may be included so web browsers with frames disabled (or browsers that do not support frames) can display something to the user, as in this example:

```mw
<frameset cols="85%, 15%">
  <frame src="http://www.example.com/frame_1.html" name="frame_1">
  <frame src="http://alt.example.com/frame_2.html" name="frame_2">
  <noframes>
    Your browser does not support frames. 
    <a href="http://www.example.com/frame_1.html">Click here</a> to view frame 1. 
    <a href="http://alt.example.com/frame_2.html">Click here</a> for frame 2.
  </noframes>
</frameset>
```

Framesets have a `border` attribute. If set to an integer greater than 0, the user can resize the frames by dragging this border, unless a `noresize` attribute is present in a frame element. If border is set to 0, no border will be displayed and content in different frames will abut each other without delineation.

The `iframe` element is used inline within a normal HTML body, and defines the initial content and name similarly to the `frame` element. Any text inside an `<iframe></iframe>` tag pair will be displayed in browsers that do not understand the iframe tag.

```mw
<iframe src="http://www.example.com/frame_1.html" height="480" width="640">
    Your browser does not support iframes. <a href="http://www.example.com/frame_1.html">Click here</a> to view the content.
</iframe>
```

## History

Netscape Navigator 2.0 introduced the elements used for frames in March 1996. Other browser vendors such as Apple with Cyberdog followed later that year. At that time, Netscape proposed frames to the World Wide Web Consortium (W3C) for inclusion in the HTML 3.0 standard.

Frames were used to display and navigate early online magazines and web apps, such as webmail services and web chat sites. Frames had the advantage of allowing elements to be displayed sitewide without requiring server features such as server-side includes or CGI support. These features were not common on early web servers accessible to the public.

Early websites often used a frame at the top to display a banner which could not be scrolled away. These banner frames sometimes included the site's logo as well as advertising.

XHTML 1.1, the intended successor to HTML 4, removed all frames. XFrames, the intended eventual replacement, provided the composite URI to address a populated frameset.

The later HTML5 standard removed framesets by means differing from XHTML. The `iframe` element remains with a number of "sandboxing" options intended for sharing content between sites.

## Advantages

By allowing content to be loaded and navigated independently, frames offered several advantages over the plain HTML in use when they were first developed:

- Simplifying maintenance of content shared across all or most pages, such as navigation data. If an item needs to be added to a sidebar navigation menu, the web page author needs to change only one web page file, whereas each individual page on a traditional non-frameset website would have to be edited if the sidebar menu appeared on all of them.
- Reducing the amount of bandwidth needed by not re-downloading parts of the page which had not changed.
- Allowing several pieces of information to be viewed side by side, with the ability for each section to be scrolled independently. This might include the side-by-side comparison of two pictures or videos, or two different ways to understand something, such as an independently scrolling page of text next to video, images, animation, 3D rotating objects, etc.
- Allowing footnotes or digressions to appear in a dedicated section of the page when linked to, so that the reader does not lose their place in the main text.
- The main advantage to frames is that they enable parts of the page to remain stationary while other parts scroll. This is useful for elements you may not want to scroll out of view, such as navigational options or banner advertising.
- Frames unify resources that reside on separate servers. For instance, you may use frames to combine your own material (and navigation graphics) with threaded discussion material generated

## Criticism

The practice of framing HTML content led to numerous criticisms, most centering on usability and accessibility concerns. These include:

- Framing breaks the identity between the content and URL as displayed in the browser, making it difficult to link to or bookmark a particular item of content within the frameset
- The implementation of frames is inconsistent across different browsers
- Browsers which render material linearly do not handle frames well.
  - Screen reader programs
  - text or audio browsers
  - Email browsers such as Agora
  - Mobile browsers
- Framing complicates web indexing and can be detrimental to search engine optimization.
- Framing confuses the boundaries between content on different servers, which raises issues of copyright infringement
- Visitors arriving from search engines may land on a page intended for display in a frame, resulting in the visitor having no way to navigate to the rest of the site
- Frames change the behavior of the back button.
- Users usually do not expect browsers to print frames the way they do.
- External links on web pages which use frames may cause other pages to appear in the frameset, since the default behaviour for a link is to load in the current frame if the author does not specify otherwise. This could be used by unscrupulous webmasters to make it appear as though content from another site was actually part of the site hosting the frameset.
- If the screen resolution or browser window size is too low then each frame will have scroll bars which can look messy and uses up already limited space. Such behaviour typically resulted more from bad site design (fixed layouts instead of fluid layouts), whereby not all frameset features were put into proper use. This behaviour could be mitigated by:
  - disabling scrolling for smaller frames that typically did not require a scrollbar;
  - using fluid design characteristics in target pages instead of fixed designs, so that the content would not cause horizontal scrollbars in the first place.

## Security

Frames create both technical and user-interface difficulties for enforcement of the same-origin policy. As an example of the latter, an outer page can trick a user into performing an action on an inner page (loaded using the iframe element) which has been made 99% transparent.

## Alternatives

As web technology developed, many of the purposes for which frames were used became possible in ways that avoided the problems identified with frames.

- Cascading Style Sheets (CSS) allowed elements of a page to be scrolled independently (using the `overflow` property) or held on screen while other content is scrolled (using `position:fixed`)
- Server-Side Includes allowed shared content to be edited once and automatically delivered to the client as part of a finished page; as server CPU and connection speeds increased, the extra work required to do this on the fly became a lesser consideration.
- CGI and web-oriented scripting languages and web development frameworks such as PHP and Active Server Pages, as well as database-backed Content Management Systems such as WordPress, provided much richer options for maintaining content and providing navigation.
- Client-side scripting and Dynamic HTML allowed parts of a page to be visually replaced based on a user's actions. This allowed much more flexibility for showing "side" content, such as footnotes or instructions, as these could now be displayed and hidden anywhere on the page rather than requiring a pre-defined frame.
- AJAX allowed for dynamic display within a page of content even when it needs to be fetched from the server, for instance based on the logged in user or events elsewhere.
