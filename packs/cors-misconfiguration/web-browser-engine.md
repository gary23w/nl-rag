---
title: "Browser engine"
source: https://en.wikipedia.org/wiki/Web_browser_engine
domain: cors-misconfiguration
license: CC-BY-SA-4.0
tags: cross-origin resource sharing, cors misconfiguration, origin allowlist policy, preflight request handling
fetched: 2026-07-02
---

# Browser engine

(Redirected from

Web browser engine

)

A **browser engine** (also known as a **layout engine** or **rendering engine**) is a core software component of every major web browser. The primary job of a browser engine is to transform HTML documents and other resources of a web page into an interactive visual representation on a user's device.

## Name and scope

Besides "browser engine", two other related terms are commonly used: "layout engine" and "rendering engine". In theory, layout and rendering (or "painting") could be handled by different engines. In practice, however, these components are tightly coupled and rarely encountered on their own outside of the browser engine.

In addition to layout and rendering, a browser engine enforces the security policy between documents, handles navigation through hyperlinks and data submitted through forms, and implements the document object model (DOM) exposed to scripts associated with the document.

To provide a wide range of dynamic behavior for web pages, every major browser supports JavaScript. However, JavaScript is implemented as a separate JavaScript engine, which has enabled its usage elsewhere. In a browser, the two engines are coordinated via the DOM and Web IDL bindings.

Browser engines are also used in non-browser applications. An email client needs one to display HTML email. Beginning in the 2010s, many apps have been created with the frameworks based on Google's Chromium project; each of these standalone apps functions much like a web app. (Two examples are Spotify and Slack.)

## Layout and rendering

The layout of a web page is typically specified by Cascading Style Sheets (CSS). Each style sheet is a series of rules for how the page should be presented. For example, some rules specify typography details, such as font, color, and text size, while others determine the placement of images. The engine combines all relevant CSS rules to calculate precise graphical coordinates and pixel values for the visual representation it will paint on the screen.

The engine updates the visual representation in response to new events, including the user scrolling the page, content being asynchronously fetched, video playback, and canvas animations. It also may begin rendering before a page's resources are downloaded, which can result in visual changes as more data is received, such as images being gradually filled in or a flash of unstyled content.

## Notable engines

- Apple created the WebKit engine for its Safari browser by forking the KHTML engine of the KDE project. Apple mandates that all browsers on App Store for iOS must use WebKit as their engine. (In 2024, the mandate was removed for the European Union and in 2025 for Japan, but it is still enforced elsewhere.)
- Google originally used WebKit for its Chrome browser but eventually forked it to create the Blink engine. All Chromium-based browsers use Blink, as do applications built with CEF, Electron, or any other framework that embeds Chromium.
- Microsoft has two proprietary engines, Trident and EdgeHTML. Trident, also called MSHTML, is used in the Internet Explorer browser. EdgeHTML, being a fork of Trident, was the original engine of the Edge browser (now called Edge Legacy); it's still found in some UWP apps. The new, Chromium-based Edge was remade with the Blink engine.
- Mozilla develops the Gecko engine for its Firefox browser and the Thunderbird email client.

The following chart shows the duration of active development (when relevant new web standards continue to be added) for each engine in this section. Note that Gecko, WebKit, and Blink are still actively developed.
