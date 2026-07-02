---
title: "Progressive enhancement"
source: https://en.wikipedia.org/wiki/Progressive_enhancement
domain: server-side-rendering
license: CC-BY-SA-4.0
tags: server-side rendering, dynamic web page, server-side scripting, html hydration
fetched: 2026-07-02
---

# Progressive enhancement

**Progressive enhancement** is a strategy in web design that puts emphasis on web content first, allowing everyone to access the basic content and functionality of a web page, while users with additional browser features or faster Internet access receive the enhanced version instead. This strategy speeds up loading and facilitates crawling by web search engines, as text on a page is loaded immediately through the HTML source code rather than having to wait for JavaScript to initiate and load the content subsequently, meaning content ready for consumption "out of the box" is served immediately, and not behind additional layers.

This strategy involves separating the presentation semantics from the content, with presentation being implemented in one or more optional layers, activated based on aspects of the browser or Internet connection of the client. In practice, this means serving content through HTML, the "lowest common denominator" of web standards, and applying styling and animation through CSS to the technically possible extent, then applying further enhancements through JavaScript. Deprecated Adobe Flash could be thought of as having shared the final spot with JavaScript while it was widely in use. Since web browsers can load site features to the extent supported rather than failing to load the entire site due to one error or missing feature in JavaScript, a progressively enhancing site is more stable and backwards compatible.

## History

"Progressive enhancement" was coined by Steven Champeon and Nick Finck at the SXSW Interactive conference on March 11, 2003, in Austin, and through a series of articles for Webmonkey which were published between March and June 2003.

Specific Cascading Style Sheets (CSS) techniques pertaining to flexibility of the page layout accommodating different screen resolutions is the concept associated with the responsive web design approach. In 2012, net Magazine chose Progressive Enhancement as #1 on its list of Top Web Design Trends for 2012 (responsive design was #2). Google has encouraged the adoption of progressive enhancement to help "our systems (and a wider range of browsers) see usable content and basic functionality when certain web design features are not yet supported".

### Introduction

The strategy is an evolution of a previous web design strategy known as graceful degradation, wherein Web pages were designed for the latest browsers first, but then made to work well in older versions of browser software. Graceful degradation aims to allow a page to "degrade" – to remain presentable and accessible even if certain technologies expected by the design are absent.

In progressive enhancement the strategy is deliberately reversed: The web content is created with a markup document, geared towards the lowest common denominator of browser software functionality. If content is to be revealed interactively through JavaScript, such as a collapsible navigation menu, the HTML markup reveals all the content by default and JavaScript itself hides some of the content. The developer adds all desired functionality to the presentation and behavior of the page, using modern CSS, Scalable Vector Graphics (SVG), or JavaScript.

### Background

The progressive enhancement approach is derived from Champeon's early experience (c. 1993–1994) with Standard Generalized Markup Language (SGML), predating HTML and other Web presentation languages.

Writing content with semantic markup and considering the presentation of the content separately, rather than being embedded in the markup itself, is a concept referred to as the rule of *separation of presentation and content*. Champeon expressed a hope that, since web browsers provide a default presentation style for HTML content, this would result in websites with their content written as semantic HTML, leaving presentation choice to the web browser. However, the needs of web designers led to the HTML standard being extended with hardcoded features that allowed HTML content to prescribe specific styles, and taking away this option from consumers and their web browsers. These features forced publishers to choose between adopting a new disruptive technologies or allowing content to remain accessible to audiences that used other browsers, a dilemma between design and compatibility. During the 1990s, an increasing number of websites would not work in anything but the latest versions of popular browsers.

This trend reversed after the 1990s, once CSS was widely supported, through grassroots educational efforts (from Eric Costello, Owen Briggs, Dave Shea, and others) showing Web designers how to use CSS for layout purposes.

## Core principles

The progressive enhancement strategy consists of the following core principles:

- Basic content should be accessible to all web browsers.
- Basic functionality should be accessible to all web browsers.
- Sparse, semantic markup contains all content.
- Enhanced layout is provided by externally linked CSS.
- Enhanced behavior is provided by externally linked JavaScript.
- End-user web browser preferences are respected.

## Support and adoption

- In August 2003 Jim Wilkinson created a progressive enhancement wiki page to collect some tricks and tips and to explain the overall strategy.
- Designers such as Jeremy Keith have shown how the approach can be used harmoniously with still other approaches to modern web design (such as Ajax) to provide flexible, but powerful, user experiences.
- Aaron Gustafson wrote a series for A List Apart covering the fundamentals of progressive enhancement, from the underlying philosophy to CSS approaches to how to handle JavaScript.
- CSS Zen Garden by Molly Holzschlag and Dave Shea, spread the adoption of the term to refer to CSS-based design strategies.
- Organizations such as the Web Standards Project (WaSP), which was behind the creation of Acid2 and Acid3 tests, have embraced progressive enhancement as a basis for their educational efforts.
- In 2006 Nate Koechley at Yahoo! made extensive reference to progressive enhancement in his own approach to Web design and browser support, Graded Browser Support (GBS).
- Steve Chipman at AOL has referred to progressive enhancement (by DOM scripting) as a basis for his Web design strategy.
- David Artz, leader of AOL's Optimization team, developed a suite of Accessible Rendering Technologies, and invented a technique for disassembly of the "enhancement" on the fly, saving the user's preference.
- Progressive enhancement is used in the front ends of MediaWiki-powered sites such as Wikipedia, as it is readable, navigable, and even editable using the basic HTML interface without styling or scripts, though is enhanced by such. For example, the wikitext editor's toolbar is loaded and operates through JavaScript.
- Chris Heilmann discussed the importance of targeted delivery of CSS so that each browser only gets the content (and enhancements) it can handle.
- Scott Jehl of Filament Group proposed a "Test-Driven Progressive Enhancement", recommending to test the device capabilities (rather than inferring them from the detected user agent) before providing enhancements.
- Wt is an open-source server-side web application framework which transparently implements progressive enhancement during its bootstrap, progressing from plain HTML to full Ajax.

## Benefits

### Accessibility, compatibility, and outreach

Web pages created according to the principles of progressive enhancement are by their nature more accessible, backwards compatible, and outreaching, because the strategy demands that basic content always be available, not obstructed by features or scripting that may be easily disabled, unsupported (e.g. by text-based web browsers), or blocked on computers in sensitive environments. Additionally, the sparse markup principle makes it easier for tools that read content aloud to find that content. It is unclear as to how well progressive enhancement sites work with older tools designed to deal with table layouts, "tag soup", and the like.

### Speed, efficiency, and user control

The client is able to select which parts of a page to download beyond basic HTML (e.g. styling, images, etc.), and can opt only to download parts necessary for desired usage to speed up loading and reduce bandwidth and power consumption. For example, a client may choose to only download basic HTML, without loading style sheets, scripts, and media (e.g. images), due to low internet speeds caused by geographical location, poor cellular signal, or throttled speed due to exhausted high-speed data plan. This also reduces bandwidth consumption on the server side.

In comparison, pages whose initial content is loaded through AJAX require the client to inefficiently run JavaScript to download and view page content, rather than downloading the content immediately.

Improved results with respect to search engine optimization (SEO) is another side effect of a progressive enhancement-based Web design strategy. Because the basic content is always accessible to search engine spiders, pages built with progressive enhancement methods avoid problems that may hinder search engine indexing, whereas having to render the basic page content through JavaScript execution would make crawling slow and inefficient.

## Criticism and responses

Some skeptics, such as Garret Dimon, have expressed their concern that progressive enhancement is not workable in situations that rely heavily on JavaScript to achieve certain user interface presentations or behaviors. Laurie Gray (Information Architect at KnowledgeStorm) countered with the point that informational pages should be coded using progressive enhancement in order to be indexed by search engine spiders. Geoff Stearns (author of SWFObject, a popular Flash application) argued that Flash-heavy pages should be coded using progressive enhancement.

Designers Douglas Bowman and Bob Stein expressed doubts concerning the principle of the separation of content and presentation in absolute terms, pushing instead for a realistic recognition that the two are inextricably linked.
